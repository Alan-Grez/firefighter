"""Project settings and default paths."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Centralized settings for paths, keys, and parameters."""

    project_root: Path = Path(__file__).resolve().parents[3]
    data_dir: Path = project_root / "data_2020"
    raw_data_dir: Path = data_dir / "raw"
    processed_data_dir: Path = data_dir / "processed"
    model_dir: Path = project_root / "models"
    figures_dir: Path = project_root / "images"

    geocoding_api_key: str = ""
    temporal_window_days: int = 30
    random_state: int = 42
