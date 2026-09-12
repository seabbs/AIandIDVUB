#!/usr/bin/env python3
"""Box-and-arrow schematics for the keynote, drawn with matplotlib.

Run with:
    uv run --with matplotlib scripts/keynote-schematics.py

Writes, into figures/:
    keynote-loop.png         what a modeller does during an outbreak
    keynote-chain.png        chained models that lose uncertainty
    keynote-agent.png        what I mean by an agent
    keynote-sai-loop.png     LLM-guided tree search, Martinson et al. 2026
    keynote-map.png          Kraemer et al. 2025, Table 1, with markers
    keynote-ude.png          an SEIR model with one term learned
    keynote-sbi.png          simulation-based inference with a flow
    keynote-foundation.png   a time series foundation model, zero-shot
    keynote-renewal.png      static fallback for the renewal slider
    keynote-who.png          who does what, my guess
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.ticker import NullFormatter

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#e4e6ea"
PALE_TEAL = "#e3eef2"
PALE_SLATE = "#e6e8f2"
PALE_BRICK = "#f5e6e3"

plt.rcParams.update(
    {
        "font.size": 15,
        "font.family": "sans-serif",
        "figure.dpi": 160,
        "text.color": INK,
    }
)


def canvas(w=10, h=5.2, xlim=(0, 10), ylim=(0, 5.2)):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, colour=TEAL, fill=None, fs=14, lw=2,
        weight="normal", style="round,pad=0.02,rounding_size=0.12",
        text_colour=None):
    patch = FancyBboxPatch((x, y), w, h, boxstyle=style,
                           edgecolor=colour, facecolor=fill or "white",
                           linewidth=lw, zorder=2)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=text_colour or colour, fontweight=weight, zorder=3,
            linespacing=1.15)


def arrow(ax, p, q, colour=GREY, lw=2, style="-|>", rad=0.0, ls="-"):
    a = FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=18,
                        color=colour, linewidth=lw, zorder=1,
                        connectionstyle=f"arc3,rad={rad}", linestyle=ls)
    ax.add_patch(a)


def label(ax, x, y, text, colour=GREY, fs=12, ha="center", va="center",
          style="normal", weight="normal"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=colour,
            style=style, fontweight=weight, linespacing=1.15, zorder=3)


def save(fig, name):
    fig.savefig(f"figures/{name}", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote figures/" + name)


# 1. The loop -----------------------------------------------------------

def loop():
    fig, ax = canvas(10, 4.6, ylim=(0, 4.6))
    steps = [
        ("Data arrive", "cases, deaths,\ntests, by report date"),
        ("Delays", "infection to onset,\nonset to report"),
        ("Infections and $R_t$", "a renewal process\nruns backwards"),
        ("Forecasts and\nscenarios", "runs forwards"),
    ]
    xs = [0.1, 2.65, 5.2, 7.75]
    for x, (head, sub) in zip(xs, steps):
        box(ax, x, 2.0, 2.25, 1.3, head, colour=TEAL, fill=PALE_TEAL, fs=13,
            weight="bold")
        label(ax, x + 1.125, 3.45, sub, fs=11.5, va="bottom")
    for x0, x1 in zip(xs[:-1], xs[1:]):
        arrow(ax, (x0 + 2.25, 2.65), (x1, 2.65), colour=TEAL, lw=2.2)
    # The decision, and the return.
    box(ax, 3.95, 0.15, 2.1, 0.75, "A decision", colour=BRICK,
        fill=PALE_BRICK, fs=14, weight="bold")
    arrow(ax, (8.875, 2.0), (8.875, 0.52), colour=BRICK, lw=2, style="-")
    arrow(ax, (8.875, 0.52), (6.05, 0.52), colour=BRICK, lw=2)
    arrow(ax, (3.95, 0.52), (1.225, 0.52), colour=BRICK, lw=2, style="-")
    arrow(ax, (1.225, 0.52), (1.225, 2.0), colour=BRICK, lw=2)
    label(ax, 2.6, 0.78, "new data, next week", colour=BRICK, fs=11.5,
          style="italic")
    save(fig, "keynote-loop.png")


# 2. Chained models that lose uncertainty -------------------------------

def bell(ax, cx, cy, w, h, colour, alpha=1.0, lw=2):
    x = np.linspace(-2.6, 2.6, 120)
    y = np.exp(-x ** 2 / 2)
    ax.plot(cx + x * w / 5.2, cy + y * h, color=colour, lw=lw, alpha=alpha,
            zorder=3)
    ax.fill_between(cx + x * w / 5.2, cy, cy + y * h, color=colour,
                    alpha=0.15 * alpha, zorder=2)


def chain():
    fig, ax = canvas(10, 4.6, ylim=(0, 4.6))
    stages = ["Delay\ndistribution", "$R_t$", "Forecast"]
    xs = [0.3, 3.8, 7.3]
    for x, s in zip(xs, stages):
        box(ax, x, 2.6, 2.4, 1.6, "", colour=TEAL, fill="white")
        bell(ax, x + 1.2, 2.75, 1.8, 1.0, TEAL)
        label(ax, x + 1.2, 4.42, s, colour=TEAL, fs=14, weight="bold",
              va="bottom")
    for x0, x1 in zip(xs[:-1], xs[1:]):
        # What travels: one number.
        arrow(ax, (x0 + 2.4, 3.4), (x1, 3.4), colour=BRICK, lw=2.2)
        ax.plot([x0 + 2.4 + 0.55, x0 + 2.4 + 0.55], [3.25, 3.55],
                color=BRICK, lw=3, zorder=4)
        label(ax, x0 + 2.4 + 0.55, 3.72, "the mean", colour=BRICK, fs=11.5,
              style="italic")
    # Below: what the last stage should have looked like.
    bell(ax, 8.5, 0.55, 3.0, 1.1, GREY, alpha=0.9)
    bell(ax, 8.5, 0.55, 1.8, 1.1, TEAL)
    ax.plot([7.0, 7.35], [0.3, 0.3], color=TEAL, lw=3)
    label(ax, 7.45, 0.3, "reported", colour=TEAL, fs=11, ha="left")
    ax.plot([8.45, 8.8], [0.3, 0.3], color=GREY, lw=3)
    label(ax, 8.9, 0.3, "should carry", colour=GREY, fs=11, ha="left")
    label(ax, 0.3, 1.2, "Each stage is fitted on its own.\n"
          "Only a point estimate is passed on.\n"
          "The interval at the end is too narrow.",
          colour=INK, fs=13, ha="left")
    save(fig, "keynote-chain.png")


# 3. What I mean by an agent ------------------------------------------

def agent():
    fig, ax = canvas(11, 5.0, xlim=(0, 11), ylim=(0, 5.0))
    # People at the ends.
    box(ax, 0.05, 1.7, 1.85, 1.6, "You\n\nthe task, and\nwhat counts\nas right",
        colour=BRICK, fill=PALE_BRICK, fs=12)
    box(ax, 8.9, 1.7, 2.0, 1.6,
        "You\n\nread the pull\nrequest, merge\nor send it back",
        colour=BRICK, fill=PALE_BRICK, fs=12.5)
    # The loop in the middle.
    cx, cy, r = 5.6, 2.5, 1.6
    nodes = [
        ("Read the files\nand the docs", 90),
        ("Write or\nchange code", 0),
        ("Run it.\nTests, lint, render", -90),
        ("Check passed?", 180),
    ]
    for text, deg in nodes:
        t = np.deg2rad(deg)
        x, y = cx + r * np.cos(t), cy + r * np.sin(t)
        colour = SLATE if deg != 180 else TEAL
        box(ax, x - 0.95, y - 0.42, 1.9, 0.84, text, colour=colour,
            fill=PALE_SLATE if deg != 180 else PALE_TEAL, fs=11)
    # Arrows around the loop, clockwise.
    arcs = [((6.4, 4.05), (7.2, 2.92)), ((7.2, 2.08), (6.4, 0.95)),
            ((4.8, 0.95), (4.0, 2.08)), ((4.0, 2.92), (4.8, 4.05))]
    for p, q in arcs:
        arrow(ax, p, q, colour=SLATE, lw=2, rad=-0.35)
    label(ax, 3.75, 3.85, "no, again", colour=SLATE, fs=11, style="italic",
          ha="right")
    label(ax, 5.6, 2.5, "a language\nmodel\nwith tools", colour=GREY,
          fs=10.5, style="italic")
    arrow(ax, (1.9, 2.5), (3.05, 2.5), colour=BRICK, lw=2)
    label(ax, 2.45, 2.8, "a prompt", colour=BRICK, fs=10, style="italic")
    arrow(ax, (8.15, 2.5), (8.9, 2.5), colour=TEAL, lw=2.2)
    label(ax, 8.52, 2.78, "yes", colour=TEAL, fs=11, style="italic")
    save(fig, "keynote-agent.png")


# 4. LLM-guided tree search ----------------------------------------------

def sai_loop():
    fig, ax = canvas(10, 4.8, ylim=(0, 4.8))
    steps = ["Propose a\nforecasting model", "Write the code",
             "Fit and forecast", "Score against\nheld-out weeks",
             "Keep the best,\nrewrite the rest"]
    xs = [0.1, 2.1, 4.1, 6.1, 8.1]
    for x, s in zip(xs, steps):
        colour = SLATE if "Score" not in s else TEAL
        box(ax, x, 2.6, 1.8, 1.2, s, colour=colour,
            fill=PALE_SLATE if colour == SLATE else PALE_TEAL, fs=11)
    for x0, x1 in zip(xs[:-1], xs[1:]):
        arrow(ax, (x0 + 1.8, 3.2), (x1, 3.2), colour=SLATE, lw=2)
    arrow(ax, (9.0, 2.6), (9.0, 1.5), colour=SLATE, lw=2, style="-")
    arrow(ax, (9.0, 1.5), (1.0, 1.5), colour=SLATE, lw=2, style="-")
    arrow(ax, (1.0, 1.5), (1.0, 2.6), colour=SLATE, lw=2)
    label(ax, 5.0, 1.72, "a tree of candidate models, many rounds",
          colour=SLATE, fs=12, style="italic")
    label(ax, 5.0, 0.75,
          "The language model writes the code at each node.\n"
          "An ensemble of the surviving models is what gets submitted.",
          colour=INK, fs=12.5)
    label(ax, 5.0, 4.3, "Propose, fit, score, keep, rewrite", colour=INK,
          fs=15, weight="bold")
    save(fig, "keynote-sai-loop.png")


# 5. The Kraemer et al. map ---------------------------------------------

ROWS = [
    ("Inference of epidemiological\nparameters",
     "generative Bayesian and\nsurrogate models", SLATE,
     "flows and simulation-based inference"),
    ("Epidemic forecasting\nand nowcasting",
     "time series foundation models\nand ensembles", SLATE,
     "time series foundation models"),
    ("Scenario modelling",
     "compartmental and mechanistic\nmodels, RL agent-based models",
     TEAL, "the hosts, next two talks"),
    ("Understanding disease\nspread mechanisms",
     "graph neural networks,\ngraph foundation models", SLATE,
     "UDEs and PINNs sit near here"),
    ("Infectious disease\nsurveillance",
     "active learning,\nBayesian optimisation", None, ""),
    ("Risk prediction", "multimodal AI", None, ""),
    ("Pathogen genome analysis", "protein language models", None, ""),
    ("Public health\ndecision making",
     "Markov decision processes,\nreinforcement learning", TEAL,
     "the hosts, next two talks"),
    ("Building and checking\nthe model itself", "not in the table",
     BRICK, "coding agents"),
]


def kraemer_map():
    n = len(ROWS)
    fig, ax = canvas(11.5, 7.6, xlim=(0, 11.5), ylim=(0, 7.6))
    top, rowh = 7.15, 0.72
    label(ax, 0.2, top + 0.15, "Task", colour=GREY, fs=12, ha="left",
          weight="bold")
    label(ax, 3.7, top + 0.15, "AI method named for it", colour=GREY, fs=12,
          ha="left", weight="bold")
    label(ax, 7.9, top + 0.15, "Where this talk puts it", colour=GREY, fs=12,
          ha="left", weight="bold")
    for i, (task, method, colour, note) in enumerate(ROWS):
        y = top - (i + 1) * rowh
        edge = colour or LIGHT
        fill = {TEAL: PALE_TEAL, SLATE: PALE_SLATE, BRICK: PALE_BRICK}.get(
            colour, "white")
        ax.add_patch(FancyBboxPatch((0.1, y - 0.3), 7.3, 0.6,
                                    boxstyle="round,pad=0.02,rounding_size=0.08",
                                    edgecolor=edge, facecolor=fill,
                                    linewidth=1.6, zorder=1))
        tc = INK if colour is None else colour
        label(ax, 0.2, y, task, colour=tc, fs=11.5, ha="left",
              weight="bold" if colour else "normal")
        label(ax, 3.7, y, method, colour=tc if colour else GREY, fs=11,
              ha="left")
        if note:
            label(ax, 7.9, y, note, colour=colour, fs=11.5, ha="left",
                  style="italic")
    save(fig, "keynote-map.png")


# 6. An SEIR model with one term learned -----------------------------------

def nn_glyph(ax, cx, cy, colour=BRICK, scale=1.0):
    layers = [3, 4, 2]
    xs = [cx - 0.45 * scale, cx, cx + 0.45 * scale]
    pts = []
    for x, n in zip(xs, layers):
        ys = [cy + (i - (n - 1) / 2) * 0.22 * scale for i in range(n)]
        pts.append([(x, y) for y in ys])
    for a, b in zip(pts[:-1], pts[1:]):
        for (x0, y0) in a:
            for (x1, y1) in b:
                ax.plot([x0, x1], [y0, y1], color=colour, lw=0.7, alpha=0.6,
                        zorder=2)
    for layer in pts:
        for (x, y) in layer:
            ax.scatter([x], [y], s=28 * scale, color=colour, zorder=3)


def ude():
    fig, ax = canvas(10, 4.4, ylim=(0, 4.4))
    comps = ["S", "E", "I", "R"]
    xs = [0.5, 3.0, 5.5, 8.0]
    for x, c in zip(xs, comps):
        box(ax, x, 2.4, 1.4, 1.1, c, colour=TEAL, fill=PALE_TEAL, fs=22,
            weight="bold")
    for x0, x1 in zip(xs[:-1], xs[1:]):
        arrow(ax, (x0 + 1.4, 2.95), (x1, 2.95), colour=TEAL, lw=2.2)
    label(ax, 4.55, 3.15, r"$\sigma$", colour=TEAL, fs=15)
    label(ax, 7.05, 3.15, r"$\gamma$", colour=TEAL, fs=15)
    # The learned term.
    ax.add_patch(FancyBboxPatch((1.15, 0.35), 2.2, 1.4,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                edgecolor=BRICK, facecolor=PALE_BRICK,
                                linewidth=2, zorder=1))
    nn_glyph(ax, 2.25, 1.05, scale=1.0)
    label(ax, 2.25, 1.62, r"$\beta(t) = \mathrm{NN}(t,\ \ldots)$",
          colour=BRICK, fs=13)
    arrow(ax, (2.45, 1.75), (2.45, 2.85), colour=BRICK, lw=2)
    label(ax, 4.0, 1.05,
          "The transmission rate is the term\nyou cannot write down.\n"
          "Behaviour, season, policy.",
          colour=INK, fs=12.5, ha="left")
    label(ax, 5.0, 4.1, "Written down: the S, E, I, R structure.  "
          "Learned: one rate.", colour=GREY, fs=12.5, style="italic")
    save(fig, "keynote-ude.png")


# 7. Simulation-based inference with a flow -----------------------------

def sbi():
    fig, ax = canvas(10, 4.6, ylim=(0, 4.6))
    box(ax, 0.2, 2.3, 2.2, 1.4,
        "Simulator\n\nSEIR, agent-based,\nanything you can run",
        colour=TEAL, fill=PALE_TEAL, fs=11.5)
    box(ax, 3.3, 2.3, 2.2, 1.4,
        "Many simulated\npairs\n\n$(\\theta_i,\\ y_i)$",
        colour=SLATE, fill=PALE_SLATE, fs=11.5)
    box(ax, 6.4, 2.3, 2.2, 1.4,
        "A network learns\n$p(\\theta \\mid y)$\n\nnormalising flow",
        colour=BRICK, fill=PALE_BRICK, fs=11.5)
    arrow(ax, (2.4, 3.0), (3.3, 3.0), colour=GREY, lw=2)
    arrow(ax, (5.5, 3.0), (6.4, 3.0), colour=GREY, lw=2)
    label(ax, 2.85, 3.25, "draw $\\theta$,\nrun", colour=GREY, fs=10.5)
    label(ax, 5.95, 3.25, "train\nonce", colour=GREY, fs=10.5)
    # Then: observed data in, posterior out.
    box(ax, 3.3, 0.3, 2.2, 1.0, "Observed data $y_{obs}$", colour=INK,
        fill="white", fs=11.5)
    arrow(ax, (5.5, 0.8), (7.5, 0.8), colour=GREY, lw=2, style="-")
    arrow(ax, (7.5, 0.8), (7.5, 2.3), colour=GREY, lw=2)
    bell(ax, 9.3, 0.5, 1.2, 0.9, BRICK)
    label(ax, 9.3, 0.25, "posterior, in seconds", colour=BRICK, fs=10.5)
    arrow(ax, (8.6, 3.0), (9.3, 3.0), colour=BRICK, lw=2, style="-")
    arrow(ax, (9.3, 3.0), (9.3, 1.5), colour=BRICK, lw=2)
    label(ax, 0.25, 1.0, "No likelihood needed.\nThe cost moves to\n"
          "training, paid once.", colour=INK, fs=12, ha="left")
    label(ax, 5.0, 4.3, "Fit models you could not write a likelihood for",
          colour=INK, fs=14, weight="bold")
    save(fig, "keynote-sbi.png")


# 8. A time series foundation model, zero-shot ------------------------------

def foundation():
    rng = np.random.default_rng(3)
    fig, ax = canvas(10, 4.6, ylim=(0, 4.6))
    # Left: a stack of many series.
    for i in range(7):
        y0 = 0.55 + i * 0.5
        x = np.linspace(0.3, 2.6, 60)
        y = y0 + 0.16 * np.sin(x * rng.uniform(2, 6) + rng.uniform(0, 6)) \
            + 0.05 * rng.standard_normal(60).cumsum() / 4
        ax.plot(x, y, color=GREY, lw=1.4, alpha=0.9)
    label(ax, 1.45, 4.25, "Many series, many domains\nretail, energy, "
          "traffic, weather", colour=GREY, fs=11.5)
    arrow(ax, (2.7, 2.3), (3.8, 2.3), colour=GREY, lw=2)
    label(ax, 3.25, 2.55, "pre-train", colour=GREY, fs=10.5)
    box(ax, 3.8, 1.5, 2.1, 1.6, "One pretrained\nmodel\n\na transformer",
        colour=SLATE, fill=PALE_SLATE, fs=12)
    arrow(ax, (5.9, 2.3), (7.0, 2.3), colour=SLATE, lw=2)
    label(ax, 6.45, 2.55, "zero-shot", colour=SLATE, fs=10.5)
    # Right: one epidemic series with a forecast fan.
    x = np.linspace(7.1, 8.6, 40)
    y = 1.4 + 1.2 * np.exp(-((x - 8.0) / 0.6) ** 2) + 0.05 * rng.standard_normal(40)
    ax.plot(x, y, color=TEAL, lw=2.2)
    xf = np.linspace(8.6, 9.7, 20)
    med = 1.4 + 1.2 * np.exp(-((xf - 8.0) / 0.6) ** 2)
    spread = np.linspace(0.05, 0.6, 20)
    ax.fill_between(xf, med - spread, med + spread, color=BRICK, alpha=0.2)
    ax.fill_between(xf, med - spread / 2, med + spread / 2, color=BRICK,
                    alpha=0.3)
    ax.plot(xf, med, color=BRICK, lw=2)
    ax.plot([8.6, 8.6], [0.9, 3.0], color=GREY, lw=1, ls="--")
    label(ax, 8.3, 3.55, "Your series in.\nA forecast out.\nNo mechanism "
          "anywhere.", colour=INK, fs=12)
    label(ax, 8.6, 0.7, "today", colour=GREY, fs=10.5)
    save(fig, "keynote-foundation.png")


# 9. Static fallback for the renewal slider ----------------------------------

def renewal_curve(r, gen_mean=5.0, days=60):
    """Infections from a renewal process with constant R and a gamma-like
    discrete generation interval with the given mean. The seed is the
    exponential solution of the recursion itself, ten on day 0, so the
    series is a straight line on a log scale from the first day rather
    than dipping while a flat seed runs out. Mirrors the ojs cell in
    keynote/_partials/02-modeller.qmd."""
    k = 4.0
    theta = gen_mean / k
    support = 24
    s = np.arange(1, support + 1)
    g = s ** (k - 1) * np.exp(-s / theta)
    g /= g.sum()
    # Growth rate from the Euler-Lotka equation R * sum g_s exp(-rate s) = 1.
    lo, hi = -2.0, 2.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if r * np.sum(g * np.exp(-mid * s)) > 1:
            lo = mid
        else:
            hi = mid
    rate = (lo + hi) / 2
    inf = np.zeros(support + days)
    inf[:support] = 10 * np.exp(rate * (np.arange(support) - support + 1))
    for t in range(support, support + days):
        past = inf[t - support:t][::-1]
        inf[t] = r * np.sum(past * g)
    return inf[support - 1:], g


def renewal():
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1, 2.4]})
    for ax in (ax1, ax2):
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.grid(alpha=0.25)
        ax.set_axisbelow(True)
    _, g = renewal_curve(1.0)
    ax1.bar(np.arange(1, len(g) + 1), g, color=SLATE, width=0.8)
    ax1.set_xlim(0, 20)
    ax1.set_title("Generation interval", fontsize=13)
    ax1.set_xlabel("days since infection")
    for r, colour in ((0.8, TEAL), (1.0, GREY), (1.3, BRICK)):
        inf, _ = renewal_curve(r)
        ax2.plot(inf, color=colour, lw=2.4, label=f"$R$ = {r}")
    ax2.set_yscale("log")
    ymax = max(renewal_curve(1.3)[0].max(), 10.0)
    lo, hi = 1, 10 ** int(np.ceil(np.log10(ymax * 1.5)))
    ax2.set_ylim(lo, hi)
    ticks = [10 ** i for i in range(int(np.log10(lo)), int(np.log10(hi)) + 1)]
    ax2.set_yticks(ticks)
    ax2.set_yticklabels([f"{t:,}" for t in ticks])
    ax2.yaxis.set_minor_formatter(NullFormatter())
    ax2.axhline(10, color=GREY, lw=1, ls="--")
    ax2.set_title("Infections per day", fontsize=13)
    ax2.set_xlabel("day")
    ax2.legend(frameon=False, fontsize=12)
    fig.suptitle(
        r"$I_t = R_t \sum_s I_{t-s}\, g_s$. Today's infections are "
        r"$R_t$ times a weighted sum of recent ones",
        fontsize=12.5, y=1.02)
    fig.tight_layout()
    save(fig, "keynote-renewal.png")


# 10. Who does what, my guess --------------------------------------------

def who():
    fig, ax = canvas(10, 4.0, ylim=(0, 4.0))
    cols = [
        ("Agents", "build and check\n\ndata ingest, pipelines,\ntests, "
         "docs, releases,\nreading French PDFs", SLATE, PALE_SLATE),
        ("The mechanism", "stays the object\n\ninfections, delays,\n"
         "$R_t$, ascertainment.\nThe thing being\nestimated", TEAL,
         PALE_TEAL),
        ("People", "keep\n\nthe question,\nfitness for use,\nthe trust of "
         "whoever\ndecides", BRICK, PALE_BRICK),
    ]
    xs = [0.3, 3.55, 6.8]
    for x, (head, body, colour, fill) in zip(xs, cols):
        ax.add_patch(FancyBboxPatch((x, 0.3), 2.9, 3.4,
                                    boxstyle="round,pad=0.02,rounding_size=0.12",
                                    edgecolor=colour, facecolor=fill,
                                    linewidth=2, zorder=1))
        label(ax, x + 1.45, 3.3, head, colour=colour, fs=17, weight="bold")
        label(ax, x + 1.45, 1.75, body, colour=INK, fs=12.5)
    save(fig, "keynote-who.png")


if __name__ == "__main__":
    loop()
    chain()
    agent()
    sai_loop()
    kraemer_map()
    ude()
    sbi()
    foundation()
    renewal()
    who()
