#!/usr/bin/env -S uv run --with matplotlib python
"""Schematics drawn for the research exchange deck, round two.

Writes, into figures/:
    exchange-renewal-layer.png       the renewal equation as a network layer
    exchange-tree-search.png         an agent searching over models as a tree
    exchange-foundation-outbreak.png an outbreak foundation model fed vintages
    exchange-public-health-use.png   where the tools have been used

Palette follows the site: teal #1f6f8b, slate #4a5899, brick #b5432f, greys.
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

matplotlib.use("Agg")

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#e4e6ea"
PALE_TEAL = "#e3eef2"
PALE_SLATE = "#e6e8f2"
PALE_BRICK = "#f5e6e3"

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.size": 15,
    "font.family": "sans-serif",
    "figure.dpi": 170,
    "text.color": INK,
})


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, colour=TEAL, fill=None, fs=13, lw=2,
        weight="normal", text_colour=None, family=None):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
        edgecolor=colour, facecolor=fill or "white", linewidth=lw,
        zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=text_colour or colour, fontweight=weight,
            zorder=3, linespacing=1.15, family=family)


def arrow(ax, p, q, colour=GREY, lw=2, style="-|>", rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(
        p, q, arrowstyle=style, mutation_scale=18, color=colour,
        linewidth=lw, zorder=1, connectionstyle=f"arc3,rad={rad}",
        linestyle=ls, shrinkA=2, shrinkB=2))


def label(ax, x, y, text, colour=GREY, fs=12, ha="center", va="center",
          style="normal", weight="normal"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=colour,
            style=style, fontweight=weight, linespacing=1.2, zorder=3)


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", pad_inches=0.15,
                facecolor="white")
    plt.close(fig)
    print("wrote figures/" + name)


# 1. Renewal as a neural network layer --------------------------------------

def renewal_layer():
    fig, ax = canvas(11, 6.6)
    # The equation, left.
    label(ax, 0.2, 5.9, "The renewal equation", colour=INK, fs=16,
          ha="left", weight="bold")
    label(ax, 0.2, 5.15,
          r"$I_t = R_t \sum_{s \geq 1} I_{t-s}\, g_s$",
          colour=INK, fs=22, ha="left")
    label(ax, 0.2, 4.25,
          "A convolution of past infections with a\n"
          "fixed kernel $g$, the generation interval,\n"
          "scaled by $R_t$",
          colour=INK, fs=12.5, ha="left")
    label(ax, 0.2, 3.1,
          "Written as layers, every step has a\n"
          "gradient. The stack trains with the\n"
          "deep learning tools, or samples by\n"
          "Hamiltonian Monte Carlo",
          colour=INK, fs=12.5, ha="left")
    label(ax, 0.2, 1.95,
          "The layers are the same parts as the\n"
          "composable Turing model. A network\n"
          "can sit in any of them",
          colour=INK, fs=12.5, ha="left")

    # The layer stack, right, top to bottom.
    x, w, h = 6.0, 4.4, 0.86
    layers = [
        ("inputs", "time, covariates, past $I$", GREY, "white"),
        ("$R_t$ layer", "AR process, or a small network", SLATE,
         PALE_SLATE),
        ("renewal layer", r"conv1d(kernel $= g$) $\times\ R_t$", TEAL,
         PALE_TEAL),
        ("delay layer", "conv1d(kernel = reporting delay)", TEAL,
         PALE_TEAL),
        ("ascertainment layer", r"$\times\ p_t$, day of week", TEAL,
         PALE_TEAL),
        ("likelihood", "negative binomial on cases", BRICK, PALE_BRICK),
    ]
    ys = [5.6 - i * 1.08 for i in range(len(layers))]
    for (head, sub, colour, fill), y in zip(layers, ys):
        box(ax, x, y, w, h, "", colour=colour, fill=fill)
        ax.text(x + 0.18, y + h - 0.16, head, ha="left", va="top",
                fontsize=13, color=colour, fontweight="bold", zorder=3)
        ax.text(x + 0.18, y + 0.14, sub, ha="left", va="bottom",
                fontsize=11, color=INK, zorder=3, family="monospace")
    for y0, y1 in zip(ys[:-1], ys[1:]):
        arrow(ax, (x + w / 2, y0), (x + w / 2, y1 + h), colour=GREY,
              lw=1.8)
    # A bracket marking the mechanistic layers.
    yb0, yb1 = ys[4], ys[2] + h
    ax.plot([x + w + 0.25] * 2, [yb0, yb1], color=TEAL, lw=2)
    label(ax, x + w + 0.4, (yb0 + yb1) / 2,
          "fixed\nby the\nepidemiology", colour=TEAL, fs=11, ha="left")
    ax.plot([x - 0.25] * 2, [ys[1], ys[1] + h], color=SLATE, lw=2)
    label(ax, x - 0.4, ys[1] + h / 2, "learned", colour=SLATE, fs=11,
          ha="right")
    save(fig, "exchange-renewal-layer.png")


# 2. Agents searching over models as a tree -------------------------------

def tree_search():
    fig, ax = canvas(12, 7.0)
    bw, bh = 2.05, 0.78

    def node(cx, cy, text, kept=True, root=False, leaf=False):
        if root:
            colour, fill = INK, "white"
        elif leaf:
            colour, fill = BRICK, PALE_BRICK
        elif kept:
            colour, fill = TEAL, PALE_TEAL
        else:
            colour, fill = GREY, "white"
        box(ax, cx - bw / 2, cy - bh / 2, bw, bh, text, colour=colour,
            fill=fill, fs=11.5, weight="bold" if (root or leaf) else
            "normal", lw=2 if kept or root or leaf else 1.4)
        return (cx, cy)

    def edge(p, q, kept=True):
        arrow(ax, (p[0], p[1] - bh / 2), (q[0], q[1] + bh / 2),
              colour=TEAL if kept else GREY, lw=2 if kept else 1.3,
              ls="-" if kept else (0, (3, 3)))

    root = node(6.0, 6.3,
                "Task: forecast admissions\nScore: held-out weeks",
                root=True)
    l1 = [
        node(1.6, 4.7, "ARIMA on\nadmissions", kept=False),
        node(4.5, 4.7, "renewal,\nAR $R_t$"),
        node(7.5, 4.7, "renewal,\nweekly $R_t$"),
        node(10.4, 4.7, "GAM on\ntime", kept=False),
    ]
    for n, k in zip(l1, (False, True, True, False)):
        edge(root, n, kept=k)
    l2 = [
        node(3.0, 3.1, "+ reporting\ndelay"),
        node(5.3, 3.1, "+ spline $R_t$", kept=False),
        node(7.5, 3.1, "+ day of\nweek"),
        node(9.8, 3.1, "+ wastewater\nstream"),
    ]
    edge(l1[1], l2[0]); edge(l1[1], l2[1], kept=False)
    edge(l1[2], l2[2]); edge(l1[2], l2[3])
    leaf = node(6.4, 1.4, "ensemble of the survivors\nis what gets submitted",
                leaf=True)
    for n in (l2[0], l2[2], l2[3]):
        arrow(ax, (n[0], n[1] - bh / 2), (leaf[0], leaf[1] + bh / 2),
              colour=BRICK, lw=1.8)

    # Side labels.
    label(ax, 0.15, 5.5, "propose", colour=SLATE, fs=12, ha="left",
          style="italic")
    label(ax, 0.15, 3.9, "write the code,\nfit, score,\nexpand the best",
          colour=SLATE, fs=12, ha="left", style="italic")
    label(ax, 0.15, 2.25, "many rounds", colour=SLATE, fs=12, ha="left",
          style="italic")
    # Legend.
    box(ax, 9.3, 0.55, 0.35, 0.3, "", colour=TEAL, fill=PALE_TEAL, lw=1.6)
    label(ax, 9.8, 0.7, "kept and expanded", colour=INK, fs=11, ha="left")
    box(ax, 9.3, 0.1, 0.35, 0.3, "", colour=GREY, fill="white", lw=1.2)
    label(ax, 9.8, 0.25, "scored worse, dropped", colour=INK, fs=11,
          ha="left")
    label(ax, 0.15, 0.4,
          "The language model writes the code at every node",
          colour=INK, fs=12.5, ha="left")
    save(fig, "exchange-tree-search.png")


# 3. An outbreak foundation model fed data vintages -------------------------

def foundation_outbreak():
    rng = np.random.default_rng(7)
    fig, ax = canvas(12, 6.2)

    # Left: the same outbreak as seen on three dates.
    x0, y0, pw, ph = 0.4, 2.6, 4.6, 2.9
    ax.plot([x0, x0 + pw], [y0, y0], color=GREY, lw=1)
    ax.plot([x0, x0], [y0, y0 + ph], color=GREY, lw=1)
    weeks = np.linspace(0, 1, 60)
    true = 2.3 * np.exp(-((weeks - 0.75) / 0.32) ** 2)
    cuts = [0.42, 0.68, 1.0]
    cols = [LIGHT, GREY, TEAL]
    for cut, col, k in zip(cuts, cols, (0, 1, 2)):
        m = weeks <= cut
        y = true[m].copy()
        # Earlier vintages sit lower, and dip at their own end.
        y *= 0.78 + 0.11 * k
        tail = np.clip((weeks[m] - (cut - 0.12)) / 0.12, 0, 1)
        y *= 1 - 0.55 * tail
        y += 0.03 * rng.standard_normal(m.sum())
        ax.plot(x0 + weeks[m] * pw, y0 + y, color=col, lw=2.4, zorder=3)
        name = ("May", "July", "September")[k]
        if k == 2:
            peak = int(np.argmax(y))
            label(ax, x0 + weeks[m][peak] * pw + 0.12, y0 + y[peak] + 0.02,
                  name, colour=col, fs=10, ha="left", va="bottom")
        else:
            label(ax, x0 + cut * pw + 0.08, y0 + y[-1] + 0.02, name,
                  colour=GREY, fs=10, ha="left")
    # A step where the case definition changed.
    xs = x0 + 0.55 * pw
    ax.plot([xs, xs], [y0, y0 + ph], color=BRICK, lw=1.2, ls="--")
    label(ax, xs + 0.05, y0 + ph - 0.1, "case definition\nchanged",
          colour=BRICK, fs=10, ha="left", va="top")
    label(ax, x0, y0 + ph + 0.15, "The same outbreak, as it looked on "
          "three dates", colour=INK, fs=12.5, ha="left", weight="bold")
    label(ax, x0 + pw, y0 - 0.22, "week of onset", colour=GREY, fs=10.5,
          ha="right", va="top")

    # Streams that start and stop.
    gy = 1.55
    label(ax, x0, gy + 0.55, "Streams start and stop", colour=INK,
          fs=12.5, ha="left", weight="bold")
    streams = [("confirmed cases", 0.0, 1.0, TEAL),
               ("deaths", 0.05, 1.0, TEAL),
               ("suspected, daily", 0.0, 0.62, GREY),
               ("treatment-centre beds", 0.2, 0.58, GREY)]
    for i, (name, a, b, col) in enumerate(streams):
        yy = gy - i * 0.32
        ax.plot([x0 + a * pw, x0 + b * pw], [yy, yy], color=col, lw=6,
                solid_capstyle="butt")
        label(ax, x0 + b * pw + 0.1, yy, name, colour=col, fs=10,
              ha="left")

    # Middle: what goes in.
    arrow(ax, (5.3, 3.3), (6.3, 3.3), colour=SLATE, lw=2.2)
    label(ax, 5.8, 3.75, "every vintage,\nevery stream,\nwith its date",
          colour=SLATE, fs=10.5)
    box(ax, 6.3, 2.2, 2.6, 2.2,
        "an outbreak\nfoundation model\n\npretrained on outbreaks\nas they "
        "were seen\nat the time",
        colour=SLATE, fill=PALE_SLATE, fs=11.5)
    arrow(ax, (8.9, 3.3), (9.7, 3.3), colour=SLATE, lw=2.2)

    # Right: nowcast and forecast on the latest vintage.
    rx, ry, rw, rh = 9.7, 2.3, 2.1, 2.0
    ax.plot([rx, rx + rw], [ry, ry], color=GREY, lw=1)
    xr = np.linspace(0, 0.62, 30)
    yr = 1.5 * np.exp(-((xr - 0.55) / 0.3) ** 2)
    ax.plot(rx + xr * rw, ry + yr, color=TEAL, lw=2.2)
    xf = np.linspace(0.62, 1.0, 20)
    med = 1.5 * np.exp(-((xf - 0.55) / 0.3) ** 2)
    sp = np.linspace(0.05, 0.5, 20)
    ax.fill_between(rx + xf * rw, ry + med - sp, ry + med + sp,
                    color=BRICK, alpha=0.2)
    ax.plot(rx + xf * rw, ry + med, color=BRICK, lw=2)
    ax.plot([rx + 0.62 * rw] * 2, [ry, ry + rh], color=GREY, lw=1, ls="--")
    label(ax, rx + rw / 2, ry + rh + 0.15, "nowcast and forecast",
          colour=BRICK, fs=11.5)
    label(ax, rx + 0.62 * rw, ry - 0.2, "today", colour=GREY, fs=10,
          va="top")
    label(ax, 8.9, 1.1,
          "The hard part is the input.\nOutbreak data change after the "
          "fact, and a model\ntrained on the final curves has never seen "
          "that.",
          colour=INK, fs=12.5)
    save(fig, "exchange-foundation-outbreak.png")


# 4. Where the tools have been used -----------------------------------------

ROWS = [
    ("US CDC, Center for Forecasting\nand Outbreak Analytics",
     "EpiNow2 for nowcasts and $R_t$.\nEpiAware.jl built together",
     "2024 to 2026", TEAL),
    ("UKHSA",
     "mpox nowcasting. Norovirus nowcasts.\nExercise Pegasus",
     "2022 to 2025", TEAL),
    ("DRC, INSP and INRB, Kinshasa",
     "epidist delay estimates in the NEJM\ncorrespondence on Bundibugyo "
     "virus", "August 2026", BRICK),
    ("ECDC",
     "European COVID-19 Forecast Hub,\nnow RespiCast. scoringutils",
     "2021 on", SLATE),
    ("Ottawa Public Health",
     "EpiNow2 short-term projections", "", TEAL),
    ("Philippines, FASSSTER",
     "EpiNow2 for local and regional $R_t$", "", TEAL),
    ("South Africa, NICD and SACEMA",
     "EpiNow2 on clinical and\nwastewater data", "2025", TEAL),
]


def public_health_use():
    n = len(ROWS)
    rowh = 0.86
    fig, ax = canvas(11.5, 0.7 + n * rowh)
    top = 0.2 + n * rowh
    label(ax, 0.3, top + 0.25, "Where", colour=GREY, fs=12, ha="left",
          weight="bold")
    label(ax, 4.55, top + 0.25, "What", colour=GREY, fs=12, ha="left",
          weight="bold")
    label(ax, 9.6, top + 0.25, "When", colour=GREY, fs=12, ha="left",
          weight="bold")
    for i, (where, what, when, colour) in enumerate(ROWS):
        y = top - (i + 1) * rowh + rowh / 2
        ax.add_patch(FancyBboxPatch(
            (0.15, y - rowh / 2 + 0.06), 11.2, rowh - 0.12,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            edgecolor=LIGHT, facecolor="white", linewidth=1.4, zorder=1))
        ax.plot([0.15, 0.15], [y - rowh / 2 + 0.1, y + rowh / 2 - 0.1],
                color=colour, lw=5, solid_capstyle="butt", zorder=2)
        label(ax, 0.4, y, where, colour=INK, fs=12, ha="left",
              weight="bold")
        label(ax, 4.55, y, what, colour=INK, fs=11.5, ha="left")
        label(ax, 9.6, y, when, colour=GREY, fs=11.5, ha="left")
    save(fig, "exchange-public-health-use.png")


if __name__ == "__main__":
    renewal_layer()
    tree_search()
    foundation_outbreak()
    public_health_use()
