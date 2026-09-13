#!/usr/bin/env python3
"""Schematics for the keynote, drawn with matplotlib.

Run with:
    uv run --with matplotlib scripts/keynote-schematics.py

Writes, into figures/:
    keynote-ebola-delays.png     the WHO Ebola Response Team estimands, 2014
    keynote-workflow.png         how an outbreak gets modelled
    keynote-workflow-agents.png  the same, marked with what agents did
    keynote-map.png              Kraemer et al. 2025, Table 1, plus one row
    keynote-seir-vs-ude.png      a semi-mechanistic SEIR beside a UDE
    keynote-renewal-layer.png    a renewal process as a network layer
    keynote-pinn.png             a physics-informed neural network
    keynote-foundation.png       a time series foundation model, zero-shot
    keynote-rl-loop.png          reinforcement learning for control
    keynote-agent-1.png          an agent: the inner loop
    keynote-agent-2.png          plus review agents and the task loop
    keynote-agent-3.png          plus a tree of candidate models
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

TEAL = "#1f6f8b"
SLATE = "#4a5899"
BRICK = "#b5432f"
INK = "#2b2b2b"
GREY = "#8a8f98"
LIGHT = "#e4e6ea"
PALE_TEAL = "#e3eef2"
PALE_SLATE = "#e6e8f2"
PALE_BRICK = "#f5e6e3"
PALE = {TEAL: PALE_TEAL, SLATE: PALE_SLATE, BRICK: PALE_BRICK, GREY: "white",
        INK: "white"}

plt.rcParams.update(
    {
        "font.size": 15,
        "font.family": "sans-serif",
        "figure.dpi": 160,
        "text.color": INK,
    }
)


def canvas(w=10, h=5.2, xlim=None, ylim=None):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*(xlim or (0, w)))
    ax.set_ylim(*(ylim or (0, h)))
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, colour=TEAL, fill=None, fs=14, lw=2,
        weight="normal", text_colour=None, ls="-", spacing=1.15):
    patch = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=0.02,rounding_size=0.12",
                           edgecolor=colour, facecolor=fill or PALE[colour],
                           linewidth=lw, zorder=2, linestyle=ls)
    ax.add_patch(patch)
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fs, color=text_colour or colour, fontweight=weight,
                zorder=3, linespacing=spacing)


def arrow(ax, p, q, colour=GREY, lw=2, style="-|>", rad=0.0, ls="-",
          scale=18):
    a = FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=scale,
                        color=colour, linewidth=lw, zorder=1,
                        connectionstyle=f"arc3,rad={rad}", linestyle=ls)
    ax.add_patch(a)


def label(ax, x, y, text, colour=GREY, fs=12, ha="center", va="center",
          style="normal", weight="normal", rotation=0):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=colour,
            style=style, fontweight=weight, linespacing=1.15, zorder=3,
            rotation=rotation)


def nn_glyph(ax, cx, cy, colour=BRICK, scale=1.0, layers=(3, 4, 2)):
    xs = [cx + (i - (len(layers) - 1) / 2) * 0.45 * scale
          for i in range(len(layers))]
    pts = []
    for x, n in zip(xs, layers):
        ys = [cy + (i - (n - 1) / 2) * 0.22 * scale for i in range(n)]
        pts.append([(x, y) for y in ys])
    for a, b in zip(pts[:-1], pts[1:]):
        for (x0, y0) in a:
            for (x1, y1) in b:
                ax.plot([x0, x1], [y0, y1], color=colour, lw=0.7, alpha=0.6,
                        zorder=3)
    for layer in pts:
        for (x, y) in layer:
            ax.scatter([x], [y], s=26 * scale, color=colour, zorder=4)


def save(fig, name):
    fig.savefig(f"figures/{name}", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote figures/" + name)


# 1. The WHO Ebola Response Team estimands ----------------------------------

def ebola_delays():
    """Means from the NEJM abstract, 23 September 2014. No shapes drawn,
    since the abstract gives only the means."""
    fig, ax = canvas(10.4, 3.6)
    y = 2.1
    events = [(0.6, "Infection"), (4.2, "Symptom onset"),
              (8.6, "Onset of the\nnext case")]
    ax.plot([0.6, 9.4], [y, y], color=LIGHT, lw=3, zorder=1)
    for x, t in events:
        ax.scatter([x], [y], s=260, color=TEAL, zorder=3)
        label(ax, x, y + 0.45, t, colour=TEAL, fs=13.5, weight="bold",
              va="bottom")
    arrow(ax, (0.75, y - 0.55), (4.05, y - 0.55), colour=SLATE, lw=2.2,
          style="<|-|>")
    label(ax, 2.4, y - 0.95, "incubation period\nmean 11.4 days", colour=SLATE,
          fs=13, va="top")
    arrow(ax, (4.35, y - 0.55), (8.45, y - 0.55), colour=SLATE, lw=2.2,
          style="<|-|>")
    label(ax, 6.4, y - 0.95, "serial interval, onset to onset\nmean 15.3 days",
          colour=SLATE, fs=13, va="top")
    box(ax, 8.25, 0.7, 2.05, 0.7, "case fatality\n70.8% (69 to 73)",
        colour=BRICK, fs=11.5)
    label(ax, 5.0, 0.28, "4,507 probable and confirmed cases by 14 September "
          "2014, from case investigation forms", colour=GREY, fs=11.5)
    save(fig, "keynote-ebola-delays.png")


# 2. How an outbreak gets modelled --------------------------------------------

STEPS = [
    ("Question", "how big, how fast,\nis it slowing"),
    ("Data", "sitreps, line lists,\nexports, beds"),
    ("Model", "process, observation,\ndelays inside it"),
    ("Fit", "MCMC, autodiff,\nconvergence"),
    ("Check", "predictive checks,\nothers' estimates"),
    ("Report", "estimates, caveats,\na date"),
]

AGENT_TAGS = [
    ("people", BRICK),
    ("agents read\nand digitise", SLATE),
    ("people choose,\nagents write", BRICK),
    ("agents,\nevery push", SLATE),
    ("agents run,\npeople judge", BRICK),
    ("agents draft,\npeople sign", BRICK),
]


def workflow(tags=None, name="keynote-workflow.png"):
    fig, ax = canvas(12, 4.8)
    xs = [0.15 + i * 1.97 for i in range(6)]
    for i, (x, (head, sub)) in enumerate(zip(xs, STEPS)):
        box(ax, x, 2.3, 1.55, 0.95, head, colour=TEAL, fs=14, weight="bold")
        label(ax, x + 0.775, 2.15, sub, colour=INK, fs=10.5, va="top")
        if tags:
            text, colour = tags[i]
            label(ax, x + 0.775, 3.42, text, colour=colour, fs=10.5,
                  style="italic", weight="bold", va="bottom")
    for x0, x1 in zip(xs[:-1], xs[1:]):
        arrow(ax, (x0 + 1.55, 2.775), (x1, 2.775), colour=TEAL, lw=2.2)
    # Iterate: the report brings new data and a new question.
    arrow(ax, (xs[-1] + 0.775, 1.35), (xs[-1] + 0.775, 0.75), colour=BRICK,
          lw=2, style="-")
    arrow(ax, (xs[-1] + 0.775, 0.75), (xs[0] + 0.775, 0.75), colour=BRICK,
          lw=2, style="-")
    arrow(ax, (xs[0] + 0.775, 0.75), (xs[0] + 0.775, 1.4), colour=BRICK,
          lw=2)
    label(ax, 6.0, 0.95, "iterate: new data tomorrow, a new question "
          "next week, a model that failed a check", colour=BRICK, fs=12,
          style="italic")
    if not tags:
        # Back arrows from Fit and Check to Model.
        for i in (3, 4):
            arrow(ax, (xs[i] + 0.5, 3.28), (xs[2] + 1.1, 3.28), colour=GREY,
                  lw=1.4, rad=0.3, ls="--")
        label(ax, 6.0, 4.35, "back to the model when a fit fails or a check "
              "disagrees", colour=GREY, fs=10.5, style="italic")
    save(fig, name)


# 3. The Kraemer et al. map --------------------------------------------------

ROWS = [
    ("Inference of epidemiological\nparameters",
     "generative Bayesian and\nsurrogate models", SLATE,
     "flows and simulation-based inference"),
    ("Epidemic forecasting\nand nowcasting",
     "time series foundation models\nand ensembles", SLATE,
     "foundation time series models"),
    ("Scenario modelling",
     "compartmental and mechanistic\nmodels, RL agent-based models",
     SLATE, "reinforcement learning for control"),
    ("Understanding disease\nspread mechanisms",
     "graph neural networks,\ngraph foundation models", SLATE,
     "UDEs, renewal as a layer"),
    ("Infectious disease\nsurveillance",
     "active learning,\nBayesian optimisation", None, ""),
    ("Risk prediction", "multimodal AI", None, ""),
    ("Pathogen genome analysis", "protein language models", None, ""),
    ("Public health\ndecision making",
     "Markov decision processes,\nreinforcement learning", SLATE,
     "reinforcement learning for control"),
    ("Building and checking\nthe model", "not in the table",
     BRICK, "agentic AI, the third part of this talk"),
]


def kraemer_map():
    fig, ax = canvas(12.2, 7.6)
    top, rowh = 7.15, 0.72
    for x, t in ((0.2, "Task"), (3.7, "Kraemer et al. 2025"),
                 (7.6, "In this talk")):
        label(ax, x, top + 0.15, t, colour=GREY, fs=12.5, ha="left",
              weight="bold")
    for i, (task, method, colour, note) in enumerate(ROWS):
        y = top - (i + 1) * rowh
        edge = colour or LIGHT
        fill = PALE.get(colour, "white") if colour else "white"
        ax.add_patch(FancyBboxPatch((0.1, y - 0.3), 11.9, 0.6,
                                    boxstyle="round,pad=0.02,rounding_size=0.08",
                                    edgecolor=edge, facecolor=fill,
                                    linewidth=1.6, zorder=1))
        tc = INK if colour is None else colour
        label(ax, 0.2, y, task, colour=tc, fs=11.5, ha="left",
              weight="bold" if colour else "normal")
        label(ax, 3.7, y, method, colour=tc if colour else GREY, fs=11,
              ha="left")
        if note:
            label(ax, 7.6, y, note, colour=colour, fs=11.5, ha="left",
                  style="italic")
    save(fig, "keynote-map.png")


# 4. A semi-mechanistic SEIR beside a UDE ----------------------------------

def seir(ax, x0, y0, colour=TEAL):
    xs = [x0 + i * 1.15 for i in range(4)]
    for x, c in zip(xs, "SEIR"):
        box(ax, x, y0, 0.8, 0.7, c, colour=colour, fs=17, weight="bold")
    for xa, xb in zip(xs[:-1], xs[1:]):
        arrow(ax, (xa + 0.8, y0 + 0.35), (xb, y0 + 0.35), colour=colour,
              lw=2)
    return xs


def seir_vs_ude():
    fig, ax = canvas(12, 5.6)
    # Left: semi-mechanistic, stochastic.
    label(ax, 2.9, 5.25, "Semi-mechanistic stochastic SEIR", colour=TEAL,
          fs=14, weight="bold")
    xs = seir(ax, 0.6, 3.2)
    label(ax, xs[0] + 0.98, 3.75, r"$\beta_t$", colour=TEAL, fs=14)
    box(ax, 0.9, 1.55, 2.2, 0.8, r"$\log \beta_t$ a random walk",
        colour=SLATE, fs=11.5)
    arrow(ax, (2.0, 2.35), (xs[0] + 0.98, 3.2), colour=SLATE, lw=1.8)
    box(ax, 3.6, 1.55, 1.9, 0.8, "cases", colour=GREY, fs=12)
    arrow(ax, (xs[2] + 0.4, 3.2), (4.55, 2.35), colour=GREY, lw=1.8)
    label(ax, 2.9, 0.85, "the rate is free to move, and one stream "
          "constrains it", colour=INK, fs=11.5)
    # Divider.
    ax.plot([6.0, 6.0], [0.5, 5.4], color=LIGHT, lw=2)
    # Right: the UDE.
    label(ax, 9.0, 5.25, "Universal differential equation", colour=BRICK,
          fs=14, weight="bold")
    xs = seir(ax, 6.5, 3.2)
    label(ax, xs[0] + 0.98, 3.75, r"$\beta_t$", colour=TEAL, fs=14)
    box(ax, 6.75, 1.3, 2.5, 1.1, "", colour=BRICK)
    nn_glyph(ax, 7.6, 1.85, scale=0.9)
    label(ax, 8.55, 1.85, r"$\beta_t = \mathrm{NN}(\cdot)$", colour=BRICK,
          fs=12)
    arrow(ax, (8.0, 2.4), (xs[0] + 0.98, 3.2), colour=BRICK, lw=1.8)
    inputs = ["mobility", "surveys", "policy", "weather", "wastewater"]
    for i, t in enumerate(inputs):
        yy = 2.45 - i * 0.42
        box(ax, 9.75, yy - 0.16, 1.6, 0.34, t, colour=GREY, fs=10.5)
        arrow(ax, (9.75, yy + 0.01), (9.27, 1.85), colour=GREY, lw=1.2)
    box(ax, 8.9, 4.15, 2.0, 0.7, "cases, deaths, admissions",
        colour=GREY, fs=10.5)
    arrow(ax, (xs[2] + 0.4, 3.9), (9.6, 4.15), colour=GREY, lw=1.6)
    label(ax, 9.0, 0.35, "the same compartments; the rate is learned "
          "from many sources", colour=INK, fs=11.5)
    save(fig, "keynote-seir-vs-ude.png")


# 5. Renewal as a network layer ----------------------------------------------

def renewal_layer():
    fig, ax = canvas(11, 6.0)
    x0, w, h = 2.6, 5.8, 0.72
    layers = [
        (5.0, "Inputs to $R_t$\nbehaviour data, mobility, policy, a random "
         "walk", GREY, 1.15),
        (3.9, r"$R_t$ layer" + "\na network, a spline, or a random walk",
         SLATE, 1.15),
        (2.8, "Renewal layer, a recurrent cell\n"
         "$I_t = R_t \\sum_s I_{t-s}\\, g_s$", TEAL, 1.6),
        (1.7, "Observation layers, a convolution over the delay\n"
         "ascertainment, noise", TEAL, 1.15),
        (0.6, "Data streams\ncases, deaths, onsets, exports, beds", GREY,
         1.15),
    ]
    for y, text, colour, spacing in layers:
        box(ax, x0, y - h / 2, w, h, text, colour=colour, fs=11.5,
            spacing=spacing)
    for (ya, *_), (yb, *_) in zip(layers[:-1], layers[1:]):
        arrow(ax, (x0 + w / 2, ya - h / 2), (x0 + w / 2, yb + h / 2),
              colour=INK, lw=2)
    label(ax, 1.25, 5.1, "swap a layer,\nkeep the rest", colour=SLATE,
          fs=12.5)
    label(ax, 1.25, 2.8, "$R_t$ varies in time\nby construction",
          colour=TEAL, fs=12.5)
    label(ax, 9.75, 2.8, "discrete time,\nlike the data", colour=TEAL,
          fs=12.5)
    label(ax, 9.75, 0.7, "add a stream,\nadd a layer", colour=TEAL, fs=12.5)
    save(fig, "keynote-renewal-layer.png")


# 5b. A physics-informed neural network ------------------------------------

def pinn():
    fig, ax = canvas(11, 5.2)
    box(ax, 0.2, 2.35, 1.1, 0.7, "time $t$", colour=GREY, fs=12)
    arrow(ax, (1.3, 2.7), (1.9, 2.7), colour=GREY, lw=2)
    box(ax, 1.9, 1.75, 2.4, 1.9, "", colour=BRICK)
    nn_glyph(ax, 3.1, 2.95, scale=1.1, layers=(1, 4, 4, 3))
    label(ax, 3.1, 2.05, "neural network", colour=BRICK, fs=11.5)
    box(ax, 4.9, 3.05, 2.0, 0.8, "$S(t),\\; I(t),\\; R(t)$", colour=TEAL,
        fs=12.5)
    box(ax, 4.9, 1.65, 2.0, 0.8, r"$\beta(t)$", colour=SLATE, fs=12.5)
    arrow(ax, (4.3, 3.05), (4.9, 3.45), colour=TEAL, lw=1.8)
    arrow(ax, (4.3, 2.35), (4.9, 2.05), colour=SLATE, lw=1.8)
    # Two losses.
    box(ax, 7.6, 3.45, 2.7, 1.05, "Data loss\nmisfit to reported cases",
        colour=TEAL, fs=11)
    box(ax, 7.6, 1.15, 2.7, 1.25, "Physics loss\nresidual of\n"
        r"$\dot S = -\beta S I / N$, ...", colour=SLATE, fs=11)
    arrow(ax, (6.9, 3.6), (7.6, 3.85), colour=TEAL, lw=1.8)
    arrow(ax, (6.9, 3.25), (7.6, 2.3), colour=TEAL, lw=1.4)
    arrow(ax, (6.9, 2.05), (7.6, 1.85), colour=SLATE, lw=1.8)
    label(ax, 7.75, 2.9, "autodiff gives $\\dot S, \\dot I, \\dot R$",
          colour=GREY, fs=9.5, ha="left")
    box(ax, 7.85, 0.15, 2.2, 0.6, "one loss, summed", colour=BRICK, fs=11,
        weight="bold")
    arrow(ax, (8.95, 1.15), (8.95, 0.75), colour=BRICK, lw=1.8)
    arrow(ax, (10.3, 3.97), (10.6, 3.97), colour=BRICK, lw=1.4, style="-")
    arrow(ax, (10.6, 3.97), (10.6, 0.45), colour=BRICK, lw=1.4, style="-")
    arrow(ax, (10.6, 0.45), (10.05, 0.45), colour=BRICK, lw=1.4)
    label(ax, 8.95, 4.85, "the data pull the fit, the equation holds it "
          "to the model", colour=INK, fs=11.5)
    label(ax, 3.1, 0.6, "trained on both losses at once,\nnetwork weights "
          "and $\\beta(t)$ together", colour=GREY, fs=11, style="italic")
    save(fig, "keynote-pinn.png")


# 6. A time series foundation model, zero-shot -------------------------------

def foundation():
    rng = np.random.default_rng(3)
    fig, ax = canvas(10, 4.6)
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
        colour=SLATE, fs=12)
    arrow(ax, (5.9, 2.3), (7.0, 2.3), colour=SLATE, lw=2)
    label(ax, 6.45, 2.55, "zero-shot", colour=SLATE, fs=10.5)
    x = np.linspace(7.1, 8.6, 40)
    y = 1.4 + 1.2 * np.exp(-((x - 8.0) / 0.6) ** 2) \
        + 0.05 * rng.standard_normal(40)
    ax.plot(x, y, color=TEAL, lw=2.2)
    xf = np.linspace(8.6, 9.7, 20)
    med = 1.4 + 1.2 * np.exp(-((xf - 8.0) / 0.6) ** 2)
    spread = np.linspace(0.05, 0.6, 20)
    ax.fill_between(xf, med - spread, med + spread, color=BRICK, alpha=0.2)
    ax.fill_between(xf, med - spread / 2, med + spread / 2, color=BRICK,
                    alpha=0.3)
    ax.plot(xf, med, color=BRICK, lw=2)
    ax.plot([8.6, 8.6], [0.9, 3.0], color=GREY, lw=1, ls="--")
    label(ax, 8.3, 3.55, "Your series in.\nA forecast out.\nNo fitting.",
          colour=INK, fs=12)
    label(ax, 8.6, 0.7, "today", colour=GREY, fs=10.5)
    save(fig, "keynote-foundation.png")


# 7. Reinforcement learning for control --------------------------------------

def rl_loop():
    fig, ax = canvas(10, 4.2)
    box(ax, 0.4, 1.4, 2.8, 1.5, "Policy\n\na network mapping the\nstate to "
        "an action", colour=SLATE, fs=12)
    box(ax, 6.6, 1.4, 3.0, 1.5, "Simulator\n\na meta-population or\n"
        "individual-based model", colour=TEAL, fs=12)
    arrow(ax, (3.2, 2.55), (6.6, 2.55), colour=SLATE, lw=2.2)
    label(ax, 4.9, 2.7, "action: close schools,\nallocate vaccine",
          colour=SLATE, fs=11.5, style="italic", va="bottom")
    arrow(ax, (6.6, 1.75), (3.2, 1.75), colour=TEAL, lw=2.2)
    label(ax, 4.9, 1.45, "state: cases by district, beds\n"
          "reward: cases averted minus cost", colour=TEAL, fs=11.5,
          style="italic", va="top")
    label(ax, 5.0, 3.85, "Learn a policy by trial and error against a "
          "model, then hope the model was right", colour=INK, fs=12.5)
    label(ax, 5.0, 0.35, "the simulator is the whole world the policy "
          "ever sees", colour=GREY, fs=11.5, style="italic")
    save(fig, "keynote-rl-loop.png")


# 8. Agents, built up over three figures --------------------------------------

def inner_loop(ax, cx, cy, r=1.35, fs=10.5):
    nodes = [("Read the files\nand the docs", 90), ("Write or\nchange code", 0),
             ("Run it.\nTests, render", -90), ("Check passed?", 180)]
    for text, deg in nodes:
        t = np.deg2rad(deg)
        x, y = cx + r * np.cos(t), cy + r * np.sin(t)
        colour = TEAL if deg == 180 else SLATE
        box(ax, x - 0.8, y - 0.36, 1.6, 0.72, text, colour=colour, fs=fs)
    d = 0.62 * r
    arcs = [((cx + 0.5, cy + r - 0.36), (cx + r - 0.2, cy + 0.36)),
            ((cx + r - 0.2, cy - 0.36), (cx + 0.5, cy - r + 0.36)),
            ((cx - 0.5, cy - r + 0.36), (cx - r + 0.2, cy - 0.36)),
            ((cx - r + 0.2, cy + 0.36), (cx - 0.5, cy + r - 0.36))]
    for p, q in arcs:
        arrow(ax, p, q, colour=SLATE, lw=1.8, rad=-0.35)
    label(ax, cx, cy, "a language\nmodel with\ntools", colour=GREY, fs=9.5,
          style="italic")
    label(ax, cx - r + 0.1, cy + 0.85, "no, again", colour=SLATE, fs=9.5,
          style="italic", ha="right")
    return d


def agent_1():
    fig, ax = canvas(11, 4.6)
    box(ax, 0.1, 1.85, 1.9, 0.9, "You,\na prompt", colour=BRICK, fs=12.5)
    inner_loop(ax, 5.3, 2.3, r=1.3)
    arrow(ax, (2.0, 2.3), (3.2, 2.3), colour=BRICK, lw=2)
    box(ax, 8.3, 1.75, 1.3, 1.1, "Pull\nrequest", colour=TEAL, fs=11.5)
    arrow(ax, (7.4, 2.3), (8.3, 2.3), colour=TEAL, lw=2)
    label(ax, 7.85, 2.55, "yes", colour=TEAL, fs=10, style="italic")
    box(ax, 9.8, 1.55, 1.15, 1.5, "You\n\nread it,\nmerge or\nsend back",
        colour=BRICK, fs=11)
    arrow(ax, (9.6, 2.3), (9.8, 2.3), colour=BRICK, lw=2)
    save(fig, "keynote-agent-1.png")


def agent_2():
    fig, ax = canvas(11, 6.2)
    # Top: where tasks come from.
    box(ax, 0.1, 4.7, 2.6, 1.1, "A spec, or a\nconversation with me",
        colour=BRICK, fs=11.5)
    box(ax, 3.4, 4.7, 2.4, 1.1, "Agents write\nthe tasks", colour=SLATE,
        fs=11.5)
    arrow(ax, (2.7, 5.25), (3.4, 5.25), colour=BRICK, lw=2)
    arrow(ax, (4.6, 4.7), (4.6, 3.75), colour=SLATE, lw=2)
    label(ax, 4.95, 4.25, "one task each", colour=SLATE, fs=10,
          style="italic", ha="left")
    # Middle: the inner loop.
    inner_loop(ax, 4.6, 2.3, r=1.3, fs=10)
    box(ax, 7.3, 1.75, 1.35, 1.1, "Pull\nrequest", colour=TEAL, fs=11.5)
    arrow(ax, (6.7, 2.3), (7.3, 2.3), colour=TEAL, lw=2)
    # Review agents feed findings back.
    box(ax, 7.05, 0.15, 1.85, 0.95, "Review agents\nseveral, argued",
        colour=SLATE, fs=10.5)
    arrow(ax, (7.975, 1.75), (7.975, 1.1), colour=SLATE, lw=1.8)
    arrow(ax, (7.05, 0.62), (4.6, 0.62), colour=SLATE, lw=1.8, style="-")
    arrow(ax, (4.6, 0.62), (4.6, 0.95), colour=SLATE, lw=1.8)
    label(ax, 5.8, 0.38, "findings, back into the loop", colour=SLATE,
          fs=10, style="italic", va="top")
    # Me, at a level I choose.
    box(ax, 9.3, 1.55, 1.6, 1.5, "Me\n\nall the code,\nor only the\noutcome",
        colour=BRICK, fs=11)
    arrow(ax, (8.65, 2.3), (9.3, 2.3), colour=BRICK, lw=2)
    # Merge runs CI, which refits and raises new tasks.
    box(ax, 9.05, 4.7, 1.9, 1.1, "Merge. CI refits,\npublishes a release",
        colour=TEAL, fs=10.5)
    arrow(ax, (10.1, 3.05), (10.1, 4.7), colour=TEAL, lw=1.8)
    arrow(ax, (9.05, 5.25), (5.8, 5.25), colour=TEAL, lw=1.8, ls="--")
    label(ax, 7.4, 5.92, "what broke, what moved: new tasks", colour=TEAL,
          fs=10, style="italic", va="bottom")
    save(fig, "keynote-agent-2.png")


def agent_3():
    fig, ax = canvas(11, 6.4)
    label(ax, 5.5, 6.1, "One task: make the model better on a held-out "
          "week", colour=INK, fs=13, weight="bold")
    # Root.
    root = (5.5, 5.1)
    box(ax, root[0] - 1.0, root[1] - 0.35, 2.0, 0.7, "the current model",
        colour=TEAL, fs=11.5)
    # Level 1: three candidates proposed by an agent.
    l1 = [(1.9, "add a stream"), (5.5, "change the\ndelay prior"),
          (9.1, "split $R_t$\nby province")]
    l1_status = [SLATE, GREY, SLATE]
    for (x, t), colour in zip(l1, l1_status):
        arrow(ax, (root[0], root[1] - 0.35), (x, 3.95), colour=colour, lw=1.6)
        box(ax, x - 0.95, 3.25, 1.9, 0.7, t, colour=colour, fs=10.5)
        label(ax, x + 1.05, 3.6, "score", colour=colour, fs=9, ha="left",
              style="italic")
    label(ax, 6.7, 5.1, "an agent proposes candidates,\none loop each, "
          "fit and score", colour=SLATE, fs=10.5, style="italic", ha="left")
    # Level 2 under the two survivors.
    l2 = {1.9: [(0.7, "beds"), (1.9, "exports"), (3.1, "onsets")],
          9.1: [(7.9, "shared\nwalk"), (9.1, "per\nprovince"),
                (10.3, "distance\nkernel")]}
    keep = {(1.9, 3.1), (9.1, 9.1)}
    for px, kids in l2.items():
        for x, t in kids:
            colour = TEAL if (px, x) in keep else GREY
            arrow(ax, (px, 3.25), (x, 2.2), colour=colour, lw=1.4)
            box(ax, x - 0.55, 1.55, 1.1, 0.65, t, colour=colour, fs=9.5)
    # Level 3: the two kept branches meet.
    for x in (3.1, 9.1):
        arrow(ax, (x, 1.55), (5.5 if x < 5 else 6.2, 0.75), colour=TEAL,
              lw=1.6)
    box(ax, 4.55, 0.1, 2.6, 0.65, "keep the best, branch again",
        colour=TEAL, fs=10.5, weight="bold")
    label(ax, 1.0, 0.42, "grey: tried, scored,\ndropped", colour=GREY,
          fs=10, style="italic")
    save(fig, "keynote-agent-3.png")


if __name__ == "__main__":
    ebola_delays()
    workflow()
    workflow(tags=AGENT_TAGS, name="keynote-workflow-agents.png")
    kraemer_map()
    seir_vs_ude()
    renewal_layer()
    pinn()
    foundation()
    rl_loop()
    agent_1()
    agent_2()
    agent_3()
