#!/usr/bin/env -S uv run --with matplotlib --script
"""Draw the figures for the communication deck.

Run with:
    ./scripts/comms-figures.py

Counts are written in here with their sources so the figures can be rebuilt
without re-querying anything.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "figures"

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#d9dce1"

plt.rcParams.update(
    {
        "font.size": 18,
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


def bot_prs():
    """seabbs-bot pull requests opened per month in 2026.

    Source: GitHub search API, total_count per month, run 2026-09-11 and
    recorded in notes/research-agentic.md section 5. September is to the
    11th.
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    prs = [17, 92, 78, 61, 124, 531, 744, 399, 98]
    fig, ax = plt.subplots(figsize=(10, 4.8))
    colours = [TEAL] * len(prs)
    colours[-1] = LIGHT
    ax.bar(months, prs, color=colours, width=0.68)
    for m, v in zip(months, prs):
        ax.text(m, v + 14, f"{v}", ha="center", va="bottom", fontsize=16)
    ax.text(
        "Sep", 98 + 70, "to 11th", ha="center", fontsize=13, color=GREY
    )
    ax.set_ylabel("Pull requests opened")
    ax.set_ylim(0, max(prs) * 1.2)
    ax.set_title("seabbs-bot pull requests per month, 2026", pad=14)
    ax.tick_params(length=0)
    fig.text(
        0.99,
        0.01,
        "2,144 total · 85.5% merged · 11.9% closed unmerged",
        ha="right",
        fontsize=14,
        color=GREY,
    )
    fig.tight_layout()
    fig.savefig(OUT / "comms-bot-prs-by-month.png", bbox_inches="tight")
    plt.close(fig)


def consensus():
    """Several groups' interval estimates and the one range that is published.

    Schematic. The intervals are illustrative and carry no data.
    """
    groups = [(0.85, 1.10), (0.90, 1.20), (0.80, 1.05), (0.95, 1.25),
              (0.88, 1.15), (0.92, 1.30)]
    fig, ax = plt.subplots(figsize=(10, 4.8))
    for i, (lo, hi) in enumerate(groups):
        y = len(groups) - i
        ax.plot([lo, hi], [y, y], color=SLATE, lw=6, solid_capstyle="round",
                alpha=0.85)
        ax.plot((lo + hi) / 2, y, "o", color=SLATE, ms=9)
        ax.text(0.62, y, f"Group {i + 1}", va="center", ha="left",
                fontsize=15, color=GREY)
    ax.axhline(0.35, color=LIGHT, lw=1)
    ax.plot([0.9, 1.2], [-0.4, -0.4], color=BRICK, lw=14,
            solid_capstyle="round")
    ax.text(0.62, -0.4, "Consensus", va="center", ha="left", fontsize=17,
            color=BRICK, weight="bold")
    ax.text(1.05, -1.05, "one range, no point estimate",
            ha="center", fontsize=14, color=GREY)
    ax.axvline(1.0, color=GREY, lw=1, ls="--")
    ax.text(1.01, len(groups) + 0.6, "R = 1", ha="left", color=GREY,
            fontsize=14)
    ax.set_xlim(0.6, 1.4)
    ax.set_ylim(-1.4, len(groups) + 1)
    ax.set_yticks([])
    ax.set_xticks([0.8, 1.0, 1.2])
    ax.set_xlabel("Reproduction number, schematic")
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "comms-consensus.png", bbox_inches="tight")
    plt.close(fig)


def digitiser():
    """The same bars read against a 20-step grid and a 25-step grid.

    Schematic of the SitRep 087 misread recorded in BVDOutbreakSize
    data/README.md. Bar heights are illustrative.
    """
    heights = [12, 30, 55, 70, 62, 41, 25]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax, step, title, colour in (
        (axes[0], 20, "Grid the script assumed", TEAL),
        (axes[1], 25, "Grid SitRep 087 drew", BRICK),
    ):
        ax.bar(range(len(heights)), heights, color=colour, width=0.7)
        ax.set_ylim(0, 84)
        ax.set_yticks(range(0, 81, 20))
        ax.set_yticklabels([str(int(t * step / 20)) for t in range(0, 81, 20)])
        ax.set_xticks([])
        ax.set_title(title, fontsize=17)
        ax.grid(axis="y", alpha=0.5)
        ax.grid(axis="x", visible=False)
        peak = max(heights)
        ax.annotate(
            f"peak read as {int(peak * step / 20)}",
            xy=(heights.index(peak), peak),
            xytext=(heights.index(peak) + 1.6, peak + 6),
            fontsize=15,
            color=colour,
            arrowprops={"arrowstyle": "-", "color": colour},
        )
    axes[0].set_ylabel("Cases per day")
    fig.tight_layout()
    fig.savefig(OUT / "comms-digitiser.png", bbox_inches="tight")
    plt.close(fig)


def box(ax, x, y, w, h, text, colour, fs=16, fc="white"):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            fc=fc, ec=colour, lw=2.5,
        )
    )
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=INK)


def arrow(ax, x0, y0, x1, y1, colour=GREY, ls="-"):
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0), (x1, y1),
            arrowstyle="-|>", mutation_scale=22, lw=2.2,
            color=colour, ls=ls,
        )
    )


def pipeline():
    """Estimates travel downstream. The limitations mostly do not."""
    fig, ax = plt.subplots(figsize=(11, 4.4))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.4)
    ax.axis("off")
    box(ax, 0.3, 2.3, 2.6, 1.3, "Model\nEpiNow2", TEAL)
    box(ax, 4.2, 2.3, 2.6, 1.3, "Estimates\nCSV on GitHub", TEAL)
    box(ax, 8.1, 2.3, 2.6, 1.3, "Other papers\nother models", TEAL)
    arrow(ax, 2.95, 2.95, 4.15, 2.95, TEAL)
    arrow(ax, 6.85, 2.95, 8.05, 2.95, TEAL)
    box(ax, 0.3, 0.3, 2.6, 1.3, "Limitations\nmethods page", BRICK, fs=15)
    arrow(ax, 2.95, 0.95, 4.15, 0.95, BRICK, ls="--")
    ax.text(5.5, 0.95, "?", ha="center", va="center", fontsize=30,
            color=BRICK, weight="bold")
    arrow(ax, 6.85, 0.95, 8.05, 0.95, LIGHT, ls="--")
    ax.text(9.4, 0.95, "rarely arrive", ha="center", va="center",
            fontsize=15, color=GREY)
    fig.tight_layout()
    fig.savefig(OUT / "comms-pipeline.png", bbox_inches="tight")
    plt.close(fig)


def claims():
    """Claims a second agent workflow extracted from a deck, and how many
    needed changing.

    Source: how-I-llm commit 8c7e834, 114 claims tested, 67 changed;
    recorded in notes/research-agentic.md section 1.
    """
    fig, ax = plt.subplots(figsize=(10, 2.8))
    ax.barh(0, 67, color=BRICK, height=0.55, label="changed 67")
    ax.barh(0, 114 - 67, left=67, color=LIGHT, height=0.55,
            label="stood 47")
    ax.text(67 / 2, 0, "67 changed", ha="center", va="center",
            color="white", fontsize=18, weight="bold")
    ax.text(67 + 47 / 2, 0, "47 stood", ha="center", va="center",
            color=INK, fontsize=18)
    ax.set_xlim(0, 114)
    ax.set_yticks([])
    ax.set_xticks([0, 114])
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_title("114 claims in one deck, checked against git and GitHub",
                 fontsize=17, pad=12)
    fig.tight_layout()
    fig.savefig(OUT / "comms-claims.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    for f in (bot_prs, consensus, digitiser, pipeline, claims):
        f()
    print("wrote figures/comms-*.png")
