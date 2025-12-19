"""Classifier implementations for 10-X-Y and 10-X models."""

from __future__ import annotations

import pandas as pd

from firefighter.models.base import BaseClassifier, ModelResult


class DummyClassifier(BaseClassifier):
    """Baseline classifier that returns the most frequent class."""

    def __init__(self) -> None:
        self._label: str | None = None

    def fit(self, features: pd.DataFrame, target: pd.Series) -> "DummyClassifier":
        _ = features
        self._label = target.mode().iloc[0]
        return self

    def predict(self, features: pd.DataFrame) -> ModelResult:
        if self._label is None:
            raise ValueError("Model has not been fitted.")
        labels = pd.Series([self._label] * len(features), index=features.index)
        return ModelResult(labels=labels)
