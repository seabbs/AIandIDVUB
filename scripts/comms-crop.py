#!/usr/bin/env -S uv run --with pillow --script
"""Crop screenshots from scripts/comms-shots.py to the part each slide is
about.

Run with:
    ./scripts/comms-crop.py

Reads figures/comms-shot-*.png as taken on 2026-09-11 to 2026-09-13 at
1440 by 1000 CSS pixels and device scale 1.5, and writes the cropped files
the deck uses. The full screenshots stay on disk.
"""

from pathlib import Path

from PIL import Image

FIGURES = Path(__file__).resolve().parent.parent / "figures"

# (source, target, left, top, right, bottom) in image pixels.
CROPS = [
    # The three panels of the UK page figure, title to legend, caption off.
    ("comms-shot-covid-uk", "comms-shot-covid-uk-panels", 540, 30, 1560, 1120),
    # "The steers" heading, the "fifty-three so far" paragraph and the
    # workflow steers beneath it, table of contents off.
    ("comms-shot-juliacon-steers", "comms-shot-juliacon-steers-para",
     200, 120, 1600, 890),
    # The global page: the data date lines, the map and its legend.
    ("comms-shot-covid-global-map", "comms-shot-covid-map",
     410, 710, 1748, 1440),
    # The global page: the per-country table with its word categories.
    ("comms-shot-covid-global-table", "comms-shot-covid-table",
     410, 735, 1750, 1500),
    # The GitHub App page: name, avatar and description.
    ("comms-shot-review-bot-app", "comms-shot-review-bot",
     356, 150, 1836, 690),
    # BVDOutbreakSize issue 443: the end of sbfnk-bot's evidence and
    # seabbs-bot's closing comment.
    ("comms-shot-bvd-issue-443", "comms-shot-bots-443",
     157, 324, 1528, 1172),
    # sismid-nowcasting issue 30: the bot's request and the one-word reply.
    ("comms-shot-sismid-issue-30", "comms-shot-sismid-30",
     150, 300, 1535, 918),
    # Enzyme.jl issues by seabbs-bot: the search box and the seven issues.
    ("comms-shot-enzyme-issues", "comms-shot-enzyme",
     420, 380, 2125, 1360),
    # The live BVD report: the Limitations heading and first bullets.
    ("comms-shot-bvd-limitations", "comms-shot-bvd-limits",
     560, 735, 1620, 1500),
]

for src, dst, *box in CROPS:
    im = Image.open(FIGURES / f"{src}.png")
    out = FIGURES / f"{dst}.png"
    im.crop(tuple(box)).save(out)
    print(out, im.crop(tuple(box)).size)
