#!/usr/bin/env -S uv run --with matplotlib python
"""The nine workflow stages, with what agents did on BVDOutbreakSize placed
under them, and what stayed with people placed above.

Stage names follow the workflow paper (Abbott et al.). The placement of the
two lists is an interpretation of Sam's own statements in how-I-llm and the
BVDOutbreakSize README; see notes/draft-exchange-report.md.

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
    "Research\nquestions",
    "Process\nDAG",
    "Data source\nselection",
    "Observation\nDAG",
    "Modularise\nDAGs",
    "Inference\nchoices",
    "Model\nimplementation",
    "Specification\nand validation",
    "Data\nintegration",
]

# (stage index from 0, label). Above the strip: people. Below: agents.
PEOPLE = [
    (0, "choosing the question"),
    (1, "which model"),
    (3, "what the genetic\nlower bound means"),
    (7, "does ascertainment\nhold"),
    (8, "which streams\nto trust"),
]
AGENTS = [
    (2, "reading French\nPDF sitreps"),
    (3, "digitising the\nonset curve"),
    (6, "fitting pipeline,\nreleases, docs"),
    (7, "tests, recovery\nchecks"),
    (8, "sensitivity\nanalyses, figures"),
]


def main():
    fig, ax = plt.subplots(figsize=(15, 6.4), dpi=200)
    ax.set_xlim(-0.2, 9.2)
    ax.set_ylim(-3.2, 3.2)
    ax.axis("off")

    for i, name in enumerate(STAGES):
        ax.add_patch(
            FancyBboxPatch(
                (i + 0.05, -0.55), 0.9, 1.1,
                boxstyle="round,pad=0.01,rounding_size=0.08",
                linewidth=0, facecolor=SLATE,
            )
        )
        ax.text(i + 0.5, 0.28, str(i + 1), ha="center", va="center",
                fontsize=13, color="white", fontweight="bold")
        ax.text(i + 0.5, -0.17, name, ha="center", va="center",
                fontsize=10.5, color="white")
        if i < 8:
            ax.annotate("", xy=(i + 1.05, 0), xytext=(i + 0.95, 0),
                        arrowprops=dict(arrowstyle="-|>", color=GREY,
                                        lw=1.2))

    for i, label in PEOPLE:
        ax.plot([i + 0.5, i + 0.5], [0.6, 1.25], color=BRICK, lw=1.4)
        ax.text(i + 0.5, 1.35, label, ha="center", va="bottom",
                fontsize=11, color=BRICK)

    for i, label in AGENTS:
        ax.plot([i + 0.5, i + 0.5], [-0.6, -1.25], color=TEAL, lw=1.4)
        ax.text(i + 0.5, -1.35, label, ha="center", va="top",
                fontsize=11, color=TEAL)

    ax.text(-0.15, 2.7, "stayed with people", ha="left", va="center",
            fontsize=14, color=BRICK, fontweight="bold")
    ax.text(-0.15, -2.75, "agents did, on BVDOutbreakSize", ha="left",
            va="center", fontsize=14, color=TEAL, fontweight="bold")

    fig.tight_layout()
    fig.savefig(OUT / "exchange-workflow-split.png", bbox_inches="tight",
                facecolor="white")


if __name__ == "__main__":
    main()
