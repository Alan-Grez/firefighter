"""Command-line entrypoint for the end-to-end firefighter workflow."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

from firefighter.features.builder import encode_categoricals
from firefighter.geocoding.geocoder import GeocodingResult, geocode_address, geocode_corner
from firefighter.io.loader import load_dataset
from firefighter.models.base import BaseClassifier, ModelResult
from firefighter.models.classifier import DummyClassifier
from firefighter.pipelines.predict import run_prediction
from firefighter.visualization.plots import heatmap, spider


@dataclass(frozen=True)
class TemporalWindow:
    days: int | None = None
    hours: int | None = None

    def to_timedelta(self) -> pd.Timedelta:
        if self.days is None and self.hours is None:
            message = "Provide either days or hours for the temporal window."
            raise ValueError(message)
        return pd.Timedelta(days=self.days or 0, hours=self.hours or 0)


MODEL_REGISTRY: dict[str, type[BaseClassifier]] = {
    "dummy": DummyClassifier,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Firefighter end-to-end pipeline")
    parser.add_argument("--data", type=Path, required=True, help="Path to clean dataset")
    parser.add_argument("--date-column", type=str, default="fecha")
    parser.add_argument("--target-column", type=str, default="tipo_de_servicio")
    parser.add_argument("--address-column", type=str, default="direccion")
    parser.add_argument("--number-column", type=str, default=None)
    parser.add_argument("--corner-column", type=str, default="esquina")
    parser.add_argument("--window-days", type=int, default=None)
    parser.add_argument("--window-hours", type=int, default=None)
    parser.add_argument("--cutoff-date", type=str, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("reports"))
    parser.add_argument("--categorical-columns", type=str, default="")
    parser.add_argument("--model", type=str, default="dummy", choices=MODEL_REGISTRY.keys())
    return parser.parse_args()


def _parse_corner_value(corner_value: str) -> tuple[str | None, str | None]:
    separators = [" y ", " Y ", " & ", " / "]
    for separator in separators:
        if separator in corner_value:
            street_a, street_b = corner_value.split(separator, maxsplit=1)
            return street_a.strip() or None, street_b.strip() or None
    return corner_value.strip() or None, None


def _geocode_row(
    row: pd.Series,
    address_column: str,
    number_column: str | None,
    corner_column: str | None,
) -> tuple[GeocodingResult, str]:
    address_value = row.get(address_column) if address_column else None
    number_value = row.get(number_column) if number_column else None
    if pd.notna(address_value) and (pd.notna(number_value) or number_column is None):
        return geocode_address(str(address_value), number_value), "address"

    if corner_column:
        corner_value = row.get(corner_column)
        if pd.notna(corner_value):
            street_a, street_b = _parse_corner_value(str(corner_value))
            if street_a and street_b:
                return geocode_corner(street_a, street_b), "corner"
            if street_a:
                return geocode_address(street_a, None), "corner_fallback"

    return GeocodingResult(latitude=None, longitude=None, confidence=None), "missing"


def _apply_geocoding(
    data: pd.DataFrame,
    address_column: str,
    number_column: str | None,
    corner_column: str | None,
) -> pd.DataFrame:
    results = data.apply(
        _geocode_row,
        axis=1,
        result_type="expand",
        args=(address_column, number_column, corner_column),
    )
    geocode_results = results[0].apply(lambda result: result)
    data = data.copy()
    data["latitude"] = geocode_results.apply(lambda result: result.latitude)
    data["longitude"] = geocode_results.apply(lambda result: result.longitude)
    data["geocode_confidence"] = geocode_results.apply(lambda result: result.confidence)
    data["geocode_source"] = results[1]
    return data


def _build_temporal_features(data: pd.DataFrame, date_column: str) -> pd.DataFrame:
    dates = pd.to_datetime(data[date_column])
    features = data.copy()
    features["event_dayofweek"] = dates.dt.dayofweek
    features["event_hour"] = dates.dt.hour
    features["event_month"] = dates.dt.month
    return features


def _build_model_features(
    data: pd.DataFrame,
    date_column: str,
    categorical_columns: list[str],
) -> pd.DataFrame:
    features = _build_temporal_features(data, date_column=date_column)
    feature_columns = ["event_dayofweek", "event_hour", "event_month", "latitude", "longitude"]
    features = features.assign(
        latitude=pd.to_numeric(features.get("latitude"), errors="coerce").fillna(0.0),
        longitude=pd.to_numeric(features.get("longitude"), errors="coerce").fillna(0.0),
    )
    model_features = features[feature_columns]
    if categorical_columns:
        model_features = pd.concat([model_features, features[categorical_columns]], axis=1)
        model_features = encode_categoricals(model_features, columns=categorical_columns)
    return model_features


def _build_prediction_table(data: pd.DataFrame, result: ModelResult) -> go.Figure:
    table_data = {
        "fecha": data["fecha"].astype(str) if "fecha" in data.columns else data.index.astype(str),
        "direccion": data.get("direccion", pd.Series([""] * len(data))),
        "esquina": data.get("esquina", pd.Series([""] * len(data))),
        "prediccion": result.labels.astype(str),
    }
    table_frame = pd.DataFrame(table_data)
    return go.Figure(
        data=[
            go.Table(
                header={"values": list(table_frame.columns)},
                cells={"values": [table_frame[col].tolist() for col in table_frame.columns]},
            )
        ]
    )


def _save_plot(figure: go.Figure, output_dir: Path, filename: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    figure.write_html(output_path)
    return output_path


def _select_prediction_data(
    data: pd.DataFrame, date_column: str, cutoff: pd.Timestamp
) -> pd.DataFrame:
    future = data.loc[pd.to_datetime(data[date_column]) > cutoff]
    if not future.empty:
        return future
    return data


def main() -> None:
    args = parse_args()
    data = load_dataset(path=args.data)
    data = _apply_geocoding(
        data,
        address_column=args.address_column,
        number_column=args.number_column,
        corner_column=args.corner_column,
    )

    cutoff = pd.to_datetime(args.cutoff_date)
    window = TemporalWindow(days=args.window_days, hours=args.window_hours).to_timedelta()
    dates = pd.to_datetime(data[args.date_column])
    window_start = cutoff - window

    training_mask = (dates <= cutoff) & (dates >= window_start)
    training_data = data.loc[training_mask].copy()
    prediction_data = _select_prediction_data(data, args.date_column, cutoff)

    categorical_columns = [col for col in args.categorical_columns.split(",") if col]
    train_features = _build_model_features(
        training_data,
        date_column=args.date_column,
        categorical_columns=categorical_columns,
    )
    target = training_data[args.target_column]

    model_class = MODEL_REGISTRY[args.model]
    model = model_class().fit(train_features, target)

    prediction_features = _build_model_features(
        prediction_data,
        date_column=args.date_column,
        categorical_columns=categorical_columns,
    )
    result = run_prediction(model, prediction_features)

    prediction_data = prediction_data.copy()
    prediction_data["prediccion"] = result.labels

    heatmap_data = prediction_data.dropna(subset=["latitude", "longitude"]).copy()
    if heatmap_data.empty:
        heatmap_data = prediction_data.assign(latitude=0.0, longitude=0.0)
    heatmap_data["count"] = 1

    heatmap_figure = heatmap(heatmap_data, x="longitude", y="latitude", value="count")
    spider_counts = result.labels.value_counts()
    spider_figure = spider(
        spider_counts.tolist() or [0],
        spider_counts.index.tolist() or ["sin_predicciones"],
        title="Distribución de predicciones",
    )
    table_figure = _build_prediction_table(prediction_data, result)

    output_dir = args.output_dir
    _save_plot(heatmap_figure, output_dir, "heatmap.html")
    _save_plot(spider_figure, output_dir, "spider.html")
    _save_plot(table_figure, output_dir, "predictions_table.html")


if __name__ == "__main__":
    main()
