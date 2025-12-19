"""Plotting helpers for dashboards and reports."""

from __future__ import annotations

from typing import Iterable

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def heatmap(data: pd.DataFrame, x: str, y: str, value: str) -> go.Figure:
    """Create a heatmap figure."""

    return px.density_heatmap(data, x=x, y=y, z=value, color_continuous_scale="YlOrRd")


def spider(values: Iterable[float], categories: Iterable[str], title: str = "Radar") -> go.Figure:
    """Create a radar/spider plot."""

    figure = go.Figure(
        data=[
            go.Scatterpolar(r=list(values), theta=list(categories), fill="toself")
        ]
    )
    figure.update_layout(title=title)
    return figure
