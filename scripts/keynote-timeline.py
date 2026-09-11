#!/usr/bin/env python3
"""Timeline strips for the keynote.

Run with:
    uv run --with matplotlib scripts/keynote-timeline.py

Writes figures/keynote-timeline.png (outbreaks, 1760 to 2026) and
figures/keynote-packages.png (software, 2020 to 2026). Dates come from
notes/research-history.md sections 1 to 3, and from
`git log --reverse --format=%ad --date=short | head -n 1` in the local
clones for scoringutils (2020-02-14) and baselinenowcast (2026-04-13).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#d5d8de"

plt.rcParams.update(
    {
        "font.size": 16,
        "font.family": "sans-serif",
        "figure.dpi": 160,
        "text.color": INK,
    }
)

# Deep history, drawn as small ticks on a compressed left axis.
DEEP = [
    (1760, "Bernoulli\nsmallpox"),
    (1911, "Ross\nmalaria"),
    (1927, "Kermack and\nMcKendrick"),
    (2001, "Foot and\nmouth"),
    (2009, "H1N1"),
]

# The ten years, drawn large on the right. Colour marks whose work it was.
TEN = [
    (2014, "Ebola\nWest Africa", "watching", GREY),
    (2020, "COVID-19", "doing it", TEAL),
    (2022, "mpox", "nowcasting", TEAL),
    (2026, "Ebola disease,\nBundibugyo virus\nDRC", "live", TEAL),
]


def timeline():
    fig, (ax_l, ax_r) = plt.subplots(
        1,
        2,
        figsize=(14, 4.2),
        gridspec_kw={"width_ratios": [1.15, 2.0], "wspace": 0.04},
    )
    for ax in (ax_l, ax_r):
        ax.set_ylim(-1.4, 2.0)
        ax.axis("off")

    # Left: compressed deep history.
    ax_l.set_xlim(1740, 2012)
    ax_l.plot([1740, 2012], [0, 0], color=LIGHT, lw=3, zorder=1)
    for i, (year, label) in enumerate(DEEP):
        ax_l.plot([year, year], [-0.12, 0.12], color=GREY, lw=2)
        y = 0.35 if i % 2 == 0 else -0.45
        va = "bottom" if i % 2 == 0 else "top"
        ax_l.text(
            year,
            y,
            f"{year}\n{label}",
            ha="center",
            va=va,
            fontsize=11.5,
            color=GREY,
            linespacing=1.15,
        )

    # Right: the ten years, expanded.
    ax_r.set_xlim(2012.4, 2027.8)
    ax_r.plot([2012.4, 2027.8], [0, 0], color=LIGHT, lw=3, zorder=1)
    for year, label, verb, colour in TEN:
        ax_r.scatter([year], [0], s=420, color=colour, zorder=3)
        ax_r.text(
            year,
            0.42,
            f"{year}",
            ha="center",
            va="bottom",
            fontsize=20,
            fontweight="bold",
            color=colour,
        )
        ax_r.text(
            year,
            -0.42,
            label,
            ha="center",
            va="top",
            fontsize=13.5,
            color=INK,
            linespacing=1.15,
        )
        ax_r.text(
            year,
            1.35 if year == 2022 else 0.98,
            verb,
            ha="center",
            va="bottom",
            fontsize=12.5,
            style="italic",
            color=colour,
        )

    # Axis break marks between the two panels.
    for ax, x in ((ax_l, 2012), (ax_r, 2012.4)):
        ax.plot([x - 0.6, x + 0.6], [-0.18, 0.18], color=GREY, lw=1.6)

    handles = [
        Line2D([], [], marker="o", ls="", color=GREY, ms=13,
               label="others' work"),
        Line2D([], [], marker="o", ls="", color=TEAL, ms=13,
               label="my work"),
    ]
    ax_l.legend(
        handles=handles,
        loc="upper left",
        frameon=False,
        fontsize=12.5,
        handletextpad=0.4,
    )
    fig.savefig("figures/keynote-timeline.png", bbox_inches="tight")


# Software, with the first-commit or repo-creation month as the anchor.
PACKAGES = [
    ("2020-02", "scoringutils\nforecast scoring", 1.45, TEAL),
    ("2020-03", "EpiNow and the $R_t$ dashboard\nepiforecasts.io/covid",
     -1.45, TEAL),
    ("2020-06", "EpiNow2\non CRAN from Sep 2020", 0.7, TEAL),
    ("2021-01", "European COVID-19\nForecast Hub, with ECDC", -0.7, SLATE),
    ("2021-10", "epinowcast\nnowcasting", 1.2, TEAL),
    ("2022-10", "epidist\ndelay estimation", -1.0, TEAL),
    ("2024-02", "EpiAware.jl\nwith CDC", 1.2, SLATE),
    ("2024-08", "primarycensored\ncensored delays", -1.0, TEAL),
    ("2026-04", "baselinenowcast", 1.2, TEAL),
    ("2026-05", "BVDOutbreakSize\nlive report", -1.0, BRICK),
]


def ym(s):
    y, m = s.split("-")
    return int(y) + (int(m) - 0.5) / 12


def packages():
    fig, ax = plt.subplots(figsize=(14, 4.6))
    ax.set_xlim(2019.7, 2027.0)
    ax.set_ylim(-1.9, 1.9)
    ax.axis("off")
    ax.plot([2019.7, 2027.0], [0, 0], color=LIGHT, lw=3, zorder=1)
    for year in range(2020, 2027):
        ax.plot([year, year], [-0.08, 0.08], color=GREY, lw=1.5)
        ax.text(year, -0.2, str(year), ha="center", va="top", fontsize=13,
                color=GREY)
    for when, name, h, colour in PACKAGES:
        x = ym(when)
        ax.plot([x, x], [0, h], color=colour, lw=1.6, zorder=2)
        ax.scatter([x], [0], s=90, color=colour, zorder=3)
        va = "bottom" if h > 0 else "top"
        y = h + (0.06 if h > 0 else -0.06)
        ax.text(x, y, name, ha="center", va=va, fontsize=12.5, color=colour,
                linespacing=1.15)
    fig.savefig("figures/keynote-packages.png", bbox_inches="tight")


if __name__ == "__main__":
    timeline()
    packages()
    print("wrote figures/keynote-timeline.png, figures/keynote-packages.png")
