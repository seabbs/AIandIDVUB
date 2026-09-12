#!/usr/bin/env -S uv run --with matplotlib python
"""Draw a composable Turing model with a neural network in one slot.

Three parts in a row, as on epiaware.org/approaches/composable-turing-models:
a prior model for R_t, an infection model, and an observation model. The
prior slot is drawn twice, once holding an AR process and once holding a
neural network, with a swap arrow between them. A third candidate sits
under the observation model: a network that maps the same latent
infections to several data streams at once, in the manner of a
physics-informed network, with the renewal process as the physics.

Output: figures/exchange-nn-component.png
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

matplotlib.use("Agg")

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
GREY = "#6b6b6b"
LIGHT = "#f2f2f2"

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(exist_ok=True)


def box(ax, x, y, w, h, title, body, colour, lw=2.0, fill=LIGHT):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=lw, edgecolor=colour, facecolor=fill,
        )
    )
    ax.text(x + w / 2, y + h - 0.16, title, ha="center", va="top",
            fontsize=15, fontweight="bold", color=colour)
    ax.text(x + w / 2, y + 0.16, body, ha="center", va="bottom",
            fontsize=11.5, color="#222222", family="monospace")


def arrow(ax, x0, y0, x1, y1, colour=GREY, style="-|>", lw=1.8):
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0), (x1, y1), arrowstyle=style, mutation_scale=18,
            linewidth=lw, color=colour, shrinkA=2, shrinkB=2,
        )
    )


def network(ax, cx, cy, colour):
    """A small three layer network glyph centred at (cx, cy)."""
    layers = [3, 4, 2]
    xs = [cx - 0.42, cx, cx + 0.42]
    nodes = []
    for lx, n in zip(xs, layers):
        ys = [cy + (i - (n - 1) / 2) * 0.22 for i in range(n)]
        nodes.append([(lx, y) for y in ys])
        for y in ys:
            ax.add_patch(plt.Circle((lx, y), 0.055, color=colour, zorder=3))
    for a, b in zip(nodes[:-1], nodes[1:]):
        for (x0, y0) in a:
            for (x1, y1) in b:
                ax.plot([x0, x1], [y0, y1], color=colour, lw=0.7,
                        alpha=0.6, zorder=2)


def ar_glyph(ax, cx, cy, colour):
    """A short autoregressive path."""
    import math
    import random
    random.seed(4)
    xs = [cx - 0.5 + i * 0.1 for i in range(11)]
    y = 0.0
    ys = []
    for _ in xs:
        y = 0.8 * y + random.gauss(0, 0.12)
        ys.append(cy + y)
    ax.plot(xs, ys, color=colour, lw=2.2, zorder=3)
    ax.plot([cx - 0.55, cx + 0.55], [cy, cy], color=GREY, lw=0.8, ls=":")
    _ = math


def main():
    fig, ax = plt.subplots(figsize=(13, 6.2), dpi=200)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.2)
    ax.axis("off")

    # Infection and observation models, and the data.
    box(ax, 5.0, 2.1, 3.1, 2.0, "infection model",
        "Renewal(;\n  generation_time,\n  rt = ▢)", TEAL)
    box(ax, 8.9, 2.1, 3.1, 2.0, "observation model",
        "LatentDelay(\n  Ascertainment(\n    NegativeBinomialError()))",
        TEAL)
    ax.text(12.6, 3.1, "cases", ha="center", va="center", fontsize=14,
            color="#222222")
    arrow(ax, 8.1, 3.1, 8.9, 3.1)
    arrow(ax, 12.0, 3.1, 12.35, 3.1)
    ax.text(8.5, 3.35, r"$I_t$", ha="center", va="bottom", fontsize=14,
            color=GREY)
    ax.text(12.18, 3.35, r"$y_t$", ha="center", va="bottom", fontsize=14,
            color=GREY)

    # A third candidate: one network from the latent infections to
    # several data streams at once, physics-informed, the renewal
    # process being the physics.
    box(ax, 8.6, 0.15, 4.2, 1.75, "observation model, a question",
        "network($I_t$) → several streams", BRICK, fill="#fbf1ef")
    network(ax, 9.9, 1.0, BRICK)
    for i, stream in enumerate(("cases", "deaths", "wastewater")):
        y = 1.42 - i * 0.4
        arrow(ax, 10.45, y, 11.1, y, BRICK, lw=1.2)
        ax.text(11.15, y, stream, ha="left", va="center", fontsize=10.5,
                color="#222222")
    arrow(ax, 9.4, 2.1, 9.4, 1.9, GREY, style="<|-|>", lw=1.4)
    ax.text(9.15, 2.0, "swap", ha="right", va="center", fontsize=12,
            color=GREY, style="italic")

    # Two candidates for the prior slot.
    box(ax, 0.4, 3.6, 3.8, 2.2, "prior model for $R_t$, today",
        "AR(; ϵ_t = HierarchicalNormal())", SLATE)
    ar_glyph(ax, 2.3, 4.75, SLATE)

    box(ax, 0.4, 0.4, 3.8, 2.2, "prior model for $R_t$, a question",
        "network(covariates) → log $R_t$", BRICK, fill="#fbf1ef")
    network(ax, 2.3, 1.55, BRICK)

    # Both feed the same slot.
    arrow(ax, 4.2, 4.7, 5.0, 3.35, SLATE)
    arrow(ax, 4.2, 1.5, 5.0, 2.85, BRICK)
    ax.text(4.6, 3.1, "same\nslot", ha="center", va="center", fontsize=12,
            color=GREY, style="italic")

    # Swap arrow between the two candidates.
    arrow(ax, 2.3, 3.6, 2.3, 2.6, GREY, style="<|-|>", lw=1.4)
    ax.text(2.55, 3.1, "swap", ha="left", va="center", fontsize=12,
            color=GREY, style="italic")

    fig.tight_layout()
    fig.savefig(OUT / "exchange-nn-component.png", bbox_inches="tight",
                facecolor="white")


if __name__ == "__main__":
    main()
