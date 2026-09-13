#!/usr/bin/env python3
"""Count charts for the keynote agents section.

Run with:
    uv run --with matplotlib scripts/keynote-counts.py

Writes figures/keynote-bot-prs.png.
Counts are recorded here so the figures rebuild without re-querying.
Sources: notes/research-agentic.md section 5, rerun 2026-09-13 with
`gh api search/issues ... --jq .total_count` per month, and
`git -C ~/code/seabbs/BVDOutbreakSize log --format='%an' | sort | uniq -c`
on the local clone the same day (497 commits).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#d5d8de"

plt.rcParams.update(
    {
        "font.size": 17,
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

# seabbs-bot pull requests opened per month, 2026. September is to the 13th.
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
PRS = [17, 92, 78, 61, 124, 531, 744, 399, 119]
TOTAL, MERGED, UNMERGED = 2165, 1844, 257


def bot_prs():
    fig, ax = plt.subplots(figsize=(10, 4.8))
    colours = [TEAL] * len(PRS)
    colours[-1] = LIGHT
    ax.bar(MONTHS, PRS, color=colours, width=0.68,
           edgecolor=[TEAL] * 8 + [GREY], linewidth=1.2)
    for m, v in zip(MONTHS, PRS):
        ax.text(m, v + 14, f"{v:,}", ha="center", va="bottom", fontsize=15)
    ax.text(MONTHS[-1], PRS[-1] + 70, "to 13 Sep", ha="center",
            va="bottom", fontsize=12, color=GREY)
    ax.set_ylabel("Pull requests opened")
    ax.set_ylim(0, max(PRS) * 1.18)
    ax.set_title("seabbs-bot pull requests per month, 2026", fontsize=19,
                 pad=12)
    ax.tick_params(length=0)
    fig.text(
        0.99,
        0.01,
        f"{TOTAL:,} total · {100 * MERGED / TOTAL:.1f}% merged · "
        f"{100 * UNMERGED / TOTAL:.1f}% closed unmerged",
        ha="right",
        fontsize=13,
        color=GREY,
    )
    fig.tight_layout()
    fig.savefig("figures/keynote-bot-prs.png", bbox_inches="tight")


if __name__ == "__main__":
    bot_prs()
    print("wrote figures/keynote-bot-prs.png")
