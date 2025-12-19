"""Plotting helpers for dashboards and reports."""

from __future__ import annotations

from typing import Iterable, Mapping

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plot_predictions_map(
    data: pd.DataFrame,
    latitude: str = "latitude",
    longitude: str = "longitude",
    probability: str = "prediction_probability",
    title: str = "Mapa de calor de predicciones",
) -> go.Figure:
    """Create a density map for prediction probabilities."""

    if probability not in data.columns:
        data = data.assign(**{probability: 1.0})

    center_lat = pd.to_numeric(data[latitude], errors="coerce").mean()
    center_lon = pd.to_numeric(data[longitude], errors="coerce").mean()

    figure = px.density_mapbox(
        data,
        lat=latitude,
        lon=longitude,
        z=probability,
        radius=18,
        center={"lat": center_lat or 0.0, "lon": center_lon or 0.0},
        zoom=10,
        mapbox_style="carto-positron",
        title=title,
    )
    return figure


def plot_service_radar(
    probabilities: Iterable[float],
    services: Iterable[str],
    title: str = "Distribución de probabilidades por servicio",
) -> go.Figure:
    """Create a radar plot for 10-X service probabilities."""

    figure = go.Figure(
        data=[
            go.Scatterpolar(r=list(probabilities), theta=list(services), fill="toself")
        ]
    )
    figure.update_layout(title=title)
    return figure


def plot_predictions_table(
    data: pd.DataFrame,
    timestamp_column: str,
    prediction_column: str = "prediccion",
    title: str = "Resumen de predicciones",
) -> go.Figure:
    """Create a prediction summary table including timestamps."""

    table_data: Mapping[str, Iterable[str]] = {
        "timestamp": pd.to_datetime(data[timestamp_column]).astype(str),
        "direccion": data.get("direccion", pd.Series([""] * len(data))).astype(str),
        "esquina": data.get("esquina", pd.Series([""] * len(data))).astype(str),
        "direccion_resuelta": data.get(
            "direccion_resuelta", pd.Series([""] * len(data))
        ).astype(str),
        "prediccion": data[prediction_column].astype(str),
    }

    table_frame = pd.DataFrame(table_data)
    figure = go.Figure(
        data=[
            go.Table(
                header={"values": list(table_frame.columns)},
                cells={"values": [table_frame[col].tolist() for col in table_frame.columns]},
            )
        ]
    )
    figure.update_layout(title=title)
    return figure
