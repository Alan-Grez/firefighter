"""Model interfaces and implementations."""

from firefighter.models.base import BaseClassifier, ModelResult
from firefighter.models.classifier import DummyClassifier

__all__ = ["BaseClassifier", "ModelResult", "DummyClassifier"]
