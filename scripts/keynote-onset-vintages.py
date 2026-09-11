#!/usr/bin/env python3
"""The digitised symptom-onset curve across situation report vintages.

Run with:
    uv run --with matplotlib scripts/keynote-onset-vintages.py

Reads data/onset_curve_scanned.csv from the local BVDOutbreakSize clone,
the block the agents digitised from the raster figure in each INSP
situation report, and draws weekly onset counts for a handful of report
dates. Each read sits a few percent under the total printed on the
figure, and the gap moves between vintages with the image encoding
(data/README.md in that repo records the band). Weeks the figure did not
cover in full are dropped. Writes figures/keynote-onset-vintages.png.
"""

import csv
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"

SRC = Path.home() / "code/seabbs/BVDOutbreakSize/data/onset_curve_scanned.csv"
# Report dates to draw, oldest first, so the newest is drawn on top.
VINTAGES = ["2026-07-12", "2026-07-26", "2026-08-09", "2026-08-23",
            "2026-09-06"]
COLOURS = ["#c9ccd2", "#9aa0a8", SLATE, TEAL, BRICK]

plt.rcParams.update(
    {
        "font.size": 16,
        "font.family": "sans-serif",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.axisbelow": True,
        "figure.dpi": 160,
        "text.color": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
    }
)


def load():
    daily = defaultdict(dict)
    with SRC.open() as f:
        for row in csv.DictReader(f):
            daily[row["report_date"]][date.fromisoformat(row["onset_date"])] = (
                int(row["confirmed_total"])
            )
    return daily


MONTHS = {"07": "July", "08": "August", "09": "September"}


def weekly(series):
    """Sum daily onsets into weeks starting on the Monday of each week,
    keeping only weeks the figure covered in full."""
    out = defaultdict(int)
    first, last = min(series), max(series)
    for d, n in series.items():
        monday = d - timedelta(days=d.weekday())
        if monday < first or monday + timedelta(days=6) > last:
            continue
        out[monday] += n
    weeks = sorted(out)
    return weeks, [out[w] for w in weeks]


def main():
    daily = load()
    available = sorted(daily)
    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    for vintage, colour in zip(VINTAGES, COLOURS):
        if vintage not in daily:
            raise SystemExit(f"{vintage} not in the file; have {available}")
        weeks, counts = weekly(daily[vintage])
        day, month = int(vintage[8:]), MONTHS[vintage[5:7]]
        ax.step(weeks, counts, where="post", color=colour, lw=2.4,
                label=f"report of {day} {month}")
        ax.scatter(weeks, counts, color=colour, s=22, zorder=3)
    ax.set_ylabel("Confirmed cases by onset week")
    ax.set_xlabel("Week of symptom onset")
    ax.set_title("One curve, read from five situation reports",
                 fontsize=18, pad=10)
    ax.legend(frameon=False, fontsize=13, loc="upper left")
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig("figures/keynote-onset-vintages.png", bbox_inches="tight")
    print("wrote figures/keynote-onset-vintages.png from", len(available),
          "vintages, latest", available[-1])


if __name__ == "__main__":
    main()
