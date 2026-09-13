#!/usr/bin/env python3
"""Timeline strips for the keynote.

Run with:
    uv run --with matplotlib scripts/keynote-timeline.py

Writes four figures into figures/:
    keynote-timeline-centuries.png   outbreak models, Bernoulli 1760 to 2026
    keynote-timeline-ten-years.png   the outbreaks I have worked on, 2014 on
    keynote-packages-pandemic.png    software from the pandemic, 2020 to 2021
    keynote-packages-since.png       software since, 2022 to 2026

Dates come from notes/research-history.md sections 1 to 3. Package dates
are first commits or repository creation months, from the local clones and
the GitHub API; scoringutils (2020-02-14) and baselinenowcast (2026-04-13)
from `git log --reverse --format=%ad --date=short | head -n 1`.
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


# 1. Two and a half centuries -----------------------------------------------

# (year, label, colour). Grey for others' work, teal where I was involved.
# (year, label, colour, label height). Heights keep neighbours apart.
DEEP = [
    (1760, "Bernoulli\nsmallpox inoculation", GREY, 0.32),
    (1911, "Ross\nmalaria threshold", GREY, -0.32),
    (1927, "Kermack and\nMcKendrick, SIR", GREY, 0.32),
    (1991, "Anderson and May\nInfectious Diseases\nof Humans", GREY, -1.15),
]

RECENT = [
    (2001, "Foot and mouth\nreal-time fitting", GREY, 0.32),
    (2009, "H1N1\nearly assessment", GREY, -0.32),
    (2014, "Ebola\nWest Africa", GREY, 0.32),
    (2020, "COVID-19", TEAL, -0.32),
    (2022, "mpox", TEAL, 0.32),
    (2026, "Ebola disease,\nBundibugyo virus", TEAL, -1.15),
]


def centuries():
    fig, (ax_l, ax_r) = plt.subplots(
        1,
        2,
        figsize=(14, 4.4),
        gridspec_kw={"width_ratios": [1.0, 1.6], "wspace": 0.03},
    )
    for ax in (ax_l, ax_r):
        ax.set_ylim(-2.2, 1.7)
        ax.axis("off")

    ax_l.set_xlim(1745, 1997)
    ax_l.plot([1745, 1997], [0, 0], color=LIGHT, lw=3, zorder=1)
    for year, text, colour, h in DEEP:
        ax_l.scatter([year], [0], s=160, color=colour, zorder=3)
        ax_l.plot([year, year], [0, h], color=LIGHT, lw=1.2, zorder=0)
        ax_l.text(
            year, h, f"{year}\n{text}",
            ha="center", va="bottom" if h > 0 else "top", fontsize=12.5,
            color=colour, linespacing=1.15,
        )

    ax_r.set_xlim(1997.5, 2030.5)
    ax_r.plot([1997.5, 2030.5], [0, 0], color=LIGHT, lw=3, zorder=1)
    for year, text, colour, h in RECENT:
        ax_r.scatter([year], [0], s=160 if colour == GREY else 320,
                     color=colour, zorder=3)
        ax_r.plot([year, year], [0, h], color=LIGHT, lw=1.2, zorder=0)
        ax_r.text(
            year, h, f"{year}\n{text}",
            ha="center", va="bottom" if h > 0 else "top", fontsize=12.5,
            color=colour, linespacing=1.15,
            fontweight="bold" if colour == TEAL else "normal",
        )

    # Axis break between the panels.
    for ax, x in ((ax_l, 1997), (ax_r, 1997.5)):
        ax.plot([x - 0.9, x + 0.9], [-0.16, 0.16], color=GREY, lw=1.6)

    handles = [
        Line2D([], [], marker="o", ls="", color=GREY, ms=11,
               label="others' work"),
        Line2D([], [], marker="o", ls="", color=TEAL, ms=13,
               label="work I was part of"),
    ]
    ax_r.legend(handles=handles, loc="upper right", frameon=False,
                fontsize=12.5, handletextpad=0.4)
    fig.savefig("figures/keynote-timeline-centuries.png", bbox_inches="tight")
    plt.close(fig)
    print("wrote figures/keynote-timeline-centuries.png")


# 2. My ten years -----------------------------------------------------------

# (start, end, label, colour, height). Spans are drawn as bars, points as
# dots. Heights alternate to keep the labels apart.
TEN = [
    (2014.2, 2016.0, "Ebola, West Africa\nwatched from a PhD", GREY, 1.0),
    (2020.0, 2020.2, "Wuhan\nearly estimates", TEAL, -0.9),
    (2020.25, 2022.25, "$R_t$ dashboard\nand SPI-M-O", TEAL, 1.0),
    (2020.9, 2021.6, "Variants\nAlpha, Delta", SLATE, -1.9),
    (2022.4, 2022.9, "mpox\nnowcasting, networks", TEAL, 1.9),
    (2026.37, 2026.75, "Ebola disease,\nBundibugyo virus\njoint model, live",
     BRICK, -0.9),
]


def ten_years():
    fig, ax = plt.subplots(figsize=(14, 4.4))
    ax.set_xlim(2013.3, 2027.6)
    ax.set_ylim(-3.0, 2.9)
    ax.axis("off")
    ax.plot([2013.3, 2027.6], [0, 0], color=LIGHT, lw=3, zorder=1)
    for year in range(2014, 2027):
        ax.plot([year, year], [-0.08, 0.08], color=GREY, lw=1.4)
        ax.text(year, -0.2, str(year), ha="center", va="top", fontsize=12,
                color=GREY)
    for start, end, text, colour, h in TEN:
        mid = (start + end) / 2
        if end - start > 0.3:
            ax.plot([start, end], [0, 0], color=colour, lw=9,
                    solid_capstyle="butt", zorder=2)
        else:
            ax.scatter([mid], [0], s=220, color=colour, zorder=3)
        ax.plot([mid, mid], [0.12 if h > 0 else -0.35, h], color=colour,
                lw=1.4, zorder=2)
        ax.text(mid, h + (0.06 if h > 0 else -0.06), text, ha="center",
                va="bottom" if h > 0 else "top", fontsize=12.5,
                color=colour, linespacing=1.15,
                fontweight="bold" if colour != GREY else "normal")
    fig.savefig("figures/keynote-timeline-ten-years.png", bbox_inches="tight")
    plt.close(fig)
    print("wrote figures/keynote-timeline-ten-years.png")


# 3. Software ----------------------------------------------------------------

# Two strips: the tools that came out of the pandemic, then the tools since
# (mpox onwards). (month, label, label height, colour).
PANDEMIC = [
    ("2020-02", "scoringutils\nforecast scoring", 1.35, TEAL),
    ("2020-03", "EpiNow and the $R_t$ dashboard\nepiforecasts.io/covid",
     -1.0, TEAL),
    ("2020-06", "EpiNow2\non CRAN from Sep 2020", 0.45, TEAL),
    ("2021-01", "European COVID-19\nForecast Hub, with ECDC", -1.0, SLATE),
    ("2021-10", "epinowcast\nnowcasting", 1.2, TEAL),
]

SINCE = [
    ("2022-10", "epidist\ndelay estimation", 1.2, TEAL),
    ("2024-02", "EpiAware.jl\nwith CDC", -1.0, SLATE),
    ("2024-08", "primarycensored\ncensored delays", 1.2, TEAL),
    ("2026-04", "baselinenowcast", -1.0, TEAL),
    ("2026-05", "BVDOutbreakSize\nlive report", 1.2, BRICK),
]


def ym(s):
    y, m = s.split("-")
    return int(y) + (int(m) - 0.5) / 12


def packages(items, years, xlim, out):
    lo, hi = xlim
    fig, ax = plt.subplots(figsize=(14, 4.6))
    ax.set_xlim(lo, hi)
    ax.set_ylim(-1.9, 1.9)
    ax.axis("off")
    ax.plot([lo, hi], [0, 0], color=LIGHT, lw=3, zorder=1)
    for year in years:
        ax.plot([year, year], [-0.08, 0.08], color=GREY, lw=1.5)
        ax.text(year, -0.2, str(year), ha="center", va="top", fontsize=13,
                color=GREY)
    for when, name, h, colour in items:
        x = ym(when)
        ax.plot([x, x], [0.1 if h > 0 else -0.35, h], color=colour, lw=1.6,
                zorder=2)
        ax.scatter([x], [0], s=90, color=colour, zorder=3)
        va = "bottom" if h > 0 else "top"
        y = h + (0.06 if h > 0 else -0.06)
        ax.text(x, y, name, ha="center", va=va, fontsize=12.5, color=colour,
                linespacing=1.15)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    centuries()
    ten_years()
    packages(PANDEMIC, range(2020, 2023), (2019.8, 2022.2),
             "figures/keynote-packages-pandemic.png")
    packages(SINCE, range(2022, 2027), (2021.7, 2026.9),
             "figures/keynote-packages-since.png")
