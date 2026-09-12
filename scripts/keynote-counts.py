#!/usr/bin/env python3
"""Count charts for the keynote agents section.

Run with:
    uv run --with matplotlib scripts/keynote-counts.py

Writes figures/keynote-bot-prs.png and figures/keynote-bvd-authorship.png.
Counts are recorded here so the figures rebuild without re-querying.
Sources: notes/research-agentic.md section 5, run 2026-09-11 with
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

# seabbs-bot pull requests opened per month, 2026. September is to the 11th.
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
PRS = [17, 92, 78, 61, 124, 531, 744, 399, 98]
TOTAL, MERGED, UNMERGED = 2144, 1834, 256


def bot_prs():
    fig, ax = plt.subplots(figsize=(10, 4.8))
    colours = [TEAL] * len(PRS)
    colours[-1] = LIGHT
    ax.bar(MONTHS, PRS, color=colours, width=0.68,
           edgecolor=[TEAL] * 8 + [GREY], linewidth=1.2)
    for m, v in zip(MONTHS, PRS):
        ax.text(m, v + 14, f"{v:,}", ha="center", va="bottom", fontsize=15)
    ax.text(MONTHS[-1], PRS[-1] + 70, "to 11 Sep", ha="center",
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


# BVDOutbreakSize commits by author identity, local clone, 2026-09-11.
# Bot identities: Sam Abbott (bot) 238, seabbs-bot 144,
# Sebastian Funk robot edition 7, Claude 3.
# By hand: Sam Abbott 40, Sam 11, Sebastian Funk 3, Samuel Brand 1.
AUTHORS = [
    ("Agent, from bot identities", 392, TEAL),
    ("Dependabot", 50, LIGHT),
    ("By hand", 55, BRICK),
]


def authorship():
    fig, ax = plt.subplots(figsize=(10, 3.3))
    total = sum(c for _, c, _ in AUTHORS)
    left = 0
    for i, (label, count, colour) in enumerate(AUTHORS):
        share = round(100 * count / total)
        ax.barh(0, count, left=left, color=colour, height=0.55)
        text_colour = "white" if colour != LIGHT else INK
        if count / total > 0.15:
            ax.text(left + count / 2, 0, f"{label}\n{count} ({share}%)",
                    ha="center", va="center", color=text_colour,
                    fontsize=14, linespacing=1.15)
        else:
            # Narrow segments take turns above and below the bar so their
            # labels do not run into each other.
            above = (i % 2 == 0)
            ax.text(left + count / 2, 0.38 if above else -0.38,
                    f"{label}\n{count} ({share}%)", ha="center",
                    va="bottom" if above else "top", color=INK,
                    fontsize=12, linespacing=1.1)
        left += count
    ax.set_xlim(0, total)
    ax.set_ylim(-1.0, 1.0)
    ax.axis("off")
    ax.set_title(f"BVDOutbreakSize: {total} commits, 19 May to 11 September",
                 fontsize=18, pad=8)
    fig.tight_layout()
    fig.savefig("figures/keynote-bvd-authorship.png", bbox_inches="tight")


if __name__ == "__main__":
    bot_prs()
    authorship()
    print("wrote figures/keynote-bot-prs.png, "
          "figures/keynote-bvd-authorship.png")
