#!/usr/bin/env -S uv run --with matplotlib python
"""The nine workflow stages as a column, with what stayed with people on
the left and what agents did on BVDOutbreakSize on the right.

Stage names follow the workflow paper (Abbott et al.). Labels come from
the BVDOutbreakSize README and data/README.md. A vertical layout keeps
every label on one or two lines at a size that reads from the back of
the room when the figure fills a 60 per cent column at 1920 by 1080.

Output: figures/exchange-workflow-split.png
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.use("Agg")

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
GREY = "#6b6b6b"

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(exist_ok=True)

STAGES = [
    "Research questions",
    "Process DAG",
    "Data source selection",
    "Observation DAG",
    "Modularise DAGs",
    "Inference choices",
    "Model implementation",
    "Specification and validation",
    "Data integration",
]

# (stage index from 0, label). Left of the column: people. Right: agents.
PEOPLE = [
    (0, "choosing the question"),
    (1, "which model"),
    (3, "what the genetic\nlower bound means"),
    (7, "does ascertainment hold"),
    (8, "which streams to trust"),
]
AGENTS = [
    (2, "reading French PDF sitreps"),
    (3, "digitising the onset curve"),
    (6, "fitting pipeline,\nreleases, docs"),
    (7, "tests, recovery checks"),
    (8, "sensitivity analyses,\nfigures"),
]

BOX_L, BOX_R = 3.1, 6.9
ROW = 1.0
TOP = 8.9


def main():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.1, 10)
    ax.axis("off")

    ax.text(BOX_L - 0.3, 9.6, "stayed with people", ha="right",
            va="center", fontsize=15, color=BRICK, fontweight="bold")
    ax.text(BOX_R + 0.3, 9.6, "agents did, on BVDOutbreakSize",
            ha="left", va="center", fontsize=15, color=TEAL,
            fontweight="bold")

    for i, name in enumerate(STAGES):
        y = TOP - i * ROW
        ax.add_patch(
            FancyBboxPatch(
                (BOX_L, y - 0.36), BOX_R - BOX_L, 0.72,
                boxstyle="round,pad=0.01,rounding_size=0.1",
                linewidth=0, facecolor=SLATE,
            )
        )
        ax.text(BOX_L + 0.22, y, str(i + 1), ha="left", va="center",
                fontsize=13, color="white", fontweight="bold")
        ax.text(BOX_L + 0.62, y, name, ha="left", va="center",
                fontsize=12, color="white")
        if i < len(STAGES) - 1:
            ax.annotate("", xy=(5, y - ROW + 0.4), xytext=(5, y - 0.38),
                        arrowprops=dict(arrowstyle="-|>", color=GREY,
                                        lw=1.2))

    for i, label in PEOPLE:
        y = TOP - i * ROW
        ax.plot([BOX_L - 0.22, BOX_L - 0.04], [y, y], color=BRICK, lw=1.6)
        ax.text(BOX_L - 0.32, y, label, ha="right", va="center",
                fontsize=13, color=BRICK, linespacing=1.1)

    for i, label in AGENTS:
        y = TOP - i * ROW
        ax.plot([BOX_R + 0.04, BOX_R + 0.22], [y, y], color=TEAL, lw=1.6)
        ax.text(BOX_R + 0.32, y, label, ha="left", va="center",
                fontsize=13, color=TEAL, linespacing=1.1)

    fig.tight_layout()
    fig.savefig(OUT / "exchange-workflow-split.png", bbox_inches="tight",
                facecolor="white")


if __name__ == "__main__":
    main()
