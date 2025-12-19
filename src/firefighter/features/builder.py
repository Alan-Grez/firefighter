"""Feature engineering helpers."""

from __future__ import annotations

import pandas as pd


def build_temporal_window(data: pd.DataFrame, date_column: str, window_days: int) -> pd.DataFrame:
    """Filter rows within a temporal window ending at the max date.

    Args:
        data: Source dataframe.
        date_column: Column with datetime-like values.
        window_days: Size of the window in days.

    Returns:
        Filtered dataframe.
    """

    if date_column not in data.columns:
        message = f"Missing date column: {date_column}"
        raise KeyError(message)
    dates = pd.to_datetime(data[date_column])
    max_date = dates.max()
    window_start = max_date - pd.Timedelta(days=window_days)
    return data.loc[dates >= window_start].copy()


def encode_categoricals(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """One-hot encode categorical columns."""

    return pd.get_dummies(data, columns=columns, dtype=int)
