"""Training pipeline orchestration."""

from __future__ import annotations

import pandas as pd

from firefighter.features.builder import build_temporal_window, encode_categoricals
from firefighter.models.classifier import DummyClassifier


def run_training(data: pd.DataFrame, date_column: str, target_column: str) -> DummyClassifier:
    """Run the model training pipeline."""

    windowed = build_temporal_window(data, date_column=date_column, window_days=30)
    features = encode_categoricals(windowed.drop(columns=[target_column]), columns=[])
    target = windowed[target_column]
    model = DummyClassifier()
    return model.fit(features, target)
