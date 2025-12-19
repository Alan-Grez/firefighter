"""Pipeline orchestration helpers."""

from firefighter.pipelines.predict import run_prediction
from firefighter.pipelines.train import run_training

__all__ = ["run_training", "run_prediction"]
