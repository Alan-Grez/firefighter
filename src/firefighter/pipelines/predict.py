"""Prediction pipeline orchestration."""

from __future__ import annotations

import pandas as pd

from firefighter.models.base import BaseClassifier, ModelResult


def run_prediction(model: BaseClassifier, features: pd.DataFrame) -> ModelResult:
    """Run model inference for a prepared feature set."""

    return model.predict(features)
