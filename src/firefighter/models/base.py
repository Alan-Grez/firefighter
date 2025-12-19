"""Base model interfaces."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class ModelResult:
    labels: pd.Series
    probabilities: pd.DataFrame | None = None


class BaseClassifier:
    """Simple classifier interface for incident classification."""

    def fit(self, features: pd.DataFrame, target: pd.Series) -> "BaseClassifier":
        raise NotImplementedError

    def predict(self, features: pd.DataFrame) -> ModelResult:
        raise NotImplementedError
