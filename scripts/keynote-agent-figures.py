#!/usr/bin/env python3
"""Figures for the agents partial of the keynote, drawn with matplotlib.

Run with:
    uv run --with matplotlib scripts/keynote-agent-figures.py

Writes, into figures/:
    keynote-agent-wrong.png   three things that went wrong beyond the
                              digitiser, from the BVDOutbreakSize record

Facts drawn: docs/src/news.md v1.15.0 (the forecast walk continued as a
fixed slope, four-week R_t 0.245 to 14.9) and v1.18.0 (gradient 21 ms
to 10 ms, pull request #656); issue #445 (Enzyme cannot differentiate
the joint model); issues #299 and #297 (bed capacity as a walk that
could only rise, one length of stay for two outcomes).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#e4e6ea"
PALE_BRICK = "#f5e6e3"

plt.rcParams.update(
    {
        "font.size": 13,
        "font.family": "sans-serif",
        "figure.dpi": 160,
        "text.color": INK,
    }
)


def panel(fig, left, width, title, what, caught):
    """A titled card with an inset axes for a small sketch."""
    ax = fig.add_axes([left, 0.0, width, 1.0])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.02, 0.03), 0.96, 0.94,
                                boxstyle="round,pad=0.01,rounding_size=0.03",
                                edgecolor=LIGHT, facecolor="white",
                                linewidth=1.6))
    ax.text(0.5, 0.905, title, ha="center", va="center", fontsize=14,
            color=BRICK, fontweight="bold")
    ax.text(0.5, 0.20, what, ha="center", va="center", fontsize=10.5,
            color=INK, linespacing=1.2)
    ax.text(0.5, 0.075, caught, ha="center", va="center", fontsize=10,
            color=GREY, style="italic")
    inset = fig.add_axes([left + 0.02 * width, 0.36, 0.96 * width, 0.46])
    inset.axis("off")
    return inset


def forecast_sketch(ax):
    h = np.linspace(0, 28, 60)
    for spread, colour, ls, text in (
            (0.11 * h, BRICK, "-", "as shipped: spread grows\nwith the horizon"),
            (0.32 * np.sqrt(h), TEAL, "-", "fixed: with its square root")):
        ax.fill_between(h, -spread, spread, color=colour, alpha=0.18)
        ax.plot(h, spread, color=colour, lw=1.6, ls=ls)
        ax.plot(h, -spread, color=colour, lw=1.6, ls=ls)
    ax.plot(h, 0 * h, color=INK, lw=1.2)
    ax.text(1, 2.6, "as shipped: spread in log $R_t$\ngrows with the horizon",
            color=BRICK, fontsize=9.5, ha="left", va="bottom")
    ax.text(27.5, -2.4, "fixed: grows with\nits square root", color=TEAL,
            fontsize=9.5, ha="right", va="top")
    ax.text(0, -3.7, "cut-off", color=GREY, fontsize=9, ha="left")
    ax.text(28, -3.7, "4 weeks", color=GREY, fontsize=9, ha="right")
    ax.set_xlim(-1, 29)
    ax.set_ylim(-4, 4)


def gradient_sketch(ax):
    ax.barh([1.0], [21], color=BRICK, height=0.55)
    ax.barh([0.0], [10], color=TEAL, height=0.55)
    ax.text(21.5, 1.0, "21 ms", va="center", fontsize=10, color=BRICK)
    ax.text(10.5, 0.0, "10 ms", va="center", fontsize=10, color=TEAL)
    ax.text(0, 1.55, "one Mooncake gradient of the joint model",
            fontsize=9.5, color=INK, va="bottom")
    ax.text(0, -0.55, "Enzyme: cannot differentiate it at all,\n"
            "open since July", fontsize=9.5, color=GREY, va="top")
    ax.set_xlim(0, 30)
    ax.set_ylim(-1.6, 2.1)


def beds_sketch(ax):
    rng = np.random.default_rng(7)
    t = np.arange(0, 16)
    up_only = np.cumsum(np.abs(rng.normal(0.35, 0.5, 16)))
    up_only -= up_only[0]
    ar = np.zeros(16)
    for i in range(1, 16):
        ar[i] = 0.75 * ar[i - 1] + rng.normal(0.25, 0.5)
    ax.step(t, up_only + 1, where="post", color=BRICK, lw=1.8)
    ax.plot(t, ar + 1.2, color=TEAL, lw=1.8)
    ax.text(0.2, up_only[-1] + 1.9, "as written: beds could only be added",
            color=BRICK, fontsize=9.5, va="bottom")
    ax.text(15.6, ar[-1] + 0.6, "fixed: a trend and\na mean-reverting\n"
            "deviation", color=TEAL, fontsize=9.5, ha="right", va="top")
    ax.text(0, -0.6, "weeks of the response", color=GREY, fontsize=9,
            va="top")
    ax.set_xlim(-0.5, 16)
    ax.set_ylim(-1.3, up_only[-1] + 3.6)


def agent_wrong():
    fig = plt.figure(figsize=(11.5, 5.0))
    w = 1 / 3
    ax = panel(fig, 0, w, "Forecasts",
               "Five defects in the one-week-ahead forecast,\n"
               "all in the published report. The $R_t$ walk was\n"
               "continued as a fixed slope, so four weeks ahead\n"
               "$R_t$ ran from 0.245 to 14.9",
               "caught by looking at a plot")
    forecast_sketch(ax)
    ax = panel(fig, w, w, "Automatic differentiation",
               "Closures boxed their captured locals, so the\n"
               "gradient paid a dictionary lookup per call site.\n"
               "Assigning each name once left the log density\n"
               "bit-identical and halved the cost",
               "caught by profiling")
    gradient_sketch(ax)
    ax = panel(fig, 2 * w, w, "Observation models",
               "Bed capacity as a random walk that could only\n"
               "rise. One length of stay for patients who died\n"
               "and patients who were discharged. Both\n"
               "replaced after a look at how the response works",
               "caught by domain knowledge")
    beds_sketch(ax)
    fig.savefig("figures/keynote-agent-wrong.png", bbox_inches="tight",
                pad_inches=0.1)
    plt.close(fig)
    print("wrote figures/keynote-agent-wrong.png")


if __name__ == "__main__":
    agent_wrong()
