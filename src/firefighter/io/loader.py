"""Input/output helpers for structured datasets."""

from pathlib import Path
from typing import Literal

import pandas as pd


def load_dataset(path: Path, file_type: Literal["csv", "parquet"] | None = None) -> pd.DataFrame:
    """Load a clean CSV or Parquet file into a dataframe.

    Args:
        path: Path to the dataset.
        file_type: Optional explicit file type override.

    Returns:
        Loaded pandas DataFrame.
    """

    resolved_type = file_type or path.suffix.lower().lstrip(".")
    if resolved_type == "csv":
        return pd.read_csv(path)
    if resolved_type == "parquet":
        return pd.read_parquet(path)
    message = f"Unsupported file type: {resolved_type}"
    raise ValueError(message)
