# -*- coding: utf-8 -*-
# Copyright (c) 2025 Krishna Kumar
# SPDX-License-Identifier: MIT
from __future__ import annotations

from typing import List

from spath.plots.advanced import plot_advanced_charts
from spath.plots.convergence import plot_convergence_charts
from spath.plots.core import plot_core_flow_metrics_charts
from spath.plots.misc import plot_misc_charts
from spath.plots.stability import plot_stability_charts





# ---- MISC CHARTS

# ---- MAIN Driver -----

def produce_all_charts(df,  args, filter_result, metrics, empirical_metrics, out_dir):
    written: List[str] = []
    # create plots
    written += plot_core_flow_metrics_charts(df, args, filter_result, metrics, out_dir)
    written += plot_convergence_charts(df, args, filter_result, metrics, empirical_metrics, out_dir)
    written += plot_stability_charts(df, args, filter_result, metrics, out_dir)
    written += plot_advanced_charts(df, args, filter_result, metrics, out_dir)
    written += plot_misc_charts(df, args, filter_result, metrics, out_dir)
    return written


