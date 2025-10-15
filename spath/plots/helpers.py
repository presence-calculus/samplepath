# -*- coding: utf-8 -*-
# Copyright (c) 2025 Krishna Kumar
# SPDX-License-Identifier: MIT
from typing import Optional, Tuple, Sequence, List

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def add_caption(fig: Figure, text: str) -> None:
    """Add a caption below the x-axis."""
    fig.subplots_adjust(bottom=0.28)
    fig.text(
        0.5,
        0.005,
        text,
        ha="center",
        va="bottom",
        fontsize=9,
    )


def format_date_axis(ax: Axes, unit: str = "timestamp") -> None:
    """Format the x-axis for dates if possible."""
    ax.set_xlabel(f"Date ({unit})")
    try:
        ax.figure.autofmt_xdate()
    except Exception:
        pass


def format_axis(ax: Axes, title: str, unit: str, ylabel: str) -> None:
    """Set axis labels, title, and legend with date formatting."""
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.legend()
    format_date_axis(ax, unit=unit)


def format_fig(caption: Optional[str], fig: Figure) -> None:
    """Finalize figure with optional caption and layout adjustment."""
    fig.tight_layout()
    if caption:
        add_caption(fig, caption)


def format_and_save(
    fig: Figure,
    ax: Axes,
    title: str,
    ylabel: str,
    unit: str,
    caption: Optional[str],
    out_path: str,
) -> None:
    """Format the axis, add optional caption, save the figure, and close it."""
    format_axis(ax, title, unit, ylabel)
    format_fig(caption, fig)
    fig.savefig(out_path)
    plt.close(fig)


def init_fig_ax(figsize: Tuple[float, float] = (10.0, 3.4)) -> Tuple[Figure, Axes]:
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


def plot_series(
    ax: Axes,
    times: Sequence[pd.Timestamp],
    values: Sequence[float],
    label: str,
    style: str = "line",
    where: str = "post",
) -> None:
    if style == "step":
        ax.step(times, values, where=where, label=label)
    else:
        ax.plot(times, values, label=label)


def draw_series_chart(
    times: Sequence[pd.Timestamp],
    values: Sequence[float],
    title: str,
    ylabel: str,
    out_path: str,
    unit: str = "timestamp",
    caption: Optional[str] = None,
    style: str = "line",
    figsize: Tuple[float, float] = (10.0, 3.4),
) -> None:
    fig, ax = init_fig_ax(figsize=figsize)
    plot_series(ax, times, values, label=ylabel, style=style)
    format_and_save(fig, ax, title, ylabel, unit, caption, out_path)


def draw_line_chart(
    times: List[pd.Timestamp],
    values: np.ndarray,
    title: str,
    ylabel: str,
    out_path: str,
    unit: str = "timestamp",
    caption: Optional[str] = None,
) -> None:
    draw_series_chart(
        times, values, title, ylabel, out_path, unit=unit, caption=caption, style="line"
    )


def draw_step_chart(
    times: List[pd.Timestamp],
    values: np.ndarray,
    title: str,
    ylabel: str,
    out_path: str,
    unit: str = "timestamp",
    caption: Optional[str] = None,
) -> None:
    draw_series_chart(
        times, values, title, ylabel, out_path, unit=unit, caption=caption, style="step"
    )
