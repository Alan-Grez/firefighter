"""Command-line orchestration entrypoint."""

from __future__ import annotations

import argparse
from pathlib import Path

from firefighter.io.loader import load_dataset
from firefighter.pipelines.train import run_training


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Firefighter pipeline CLI")
    parser.add_argument("--data", type=Path, required=True, help="Path to input dataset")
    parser.add_argument("--date-column", type=str, required=True)
    parser.add_argument("--target-column", type=str, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_dataset(path=args.data)
    _ = run_training(data, date_column=args.date_column, target_column=args.target_column)


if __name__ == "__main__":
    main()
