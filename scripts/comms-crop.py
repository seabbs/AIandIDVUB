#!/usr/bin/env -S uv run --with pillow --script
"""Crop two screenshots from scripts/comms-shots.py to the part each slide
is about, and tile four of them as the recap grid on the asks slide.

Run with:
    ./scripts/comms-crop.py

Reads figures/comms-shot-covid-uk.png and
figures/comms-shot-juliacon-steers.png as taken on 2026-09-11 at 1440 by
1000 CSS pixels and device scale 1.5, and writes the cropped files the
deck uses. The full screenshots stay on disk.
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
]

for src, dst, *box in CROPS:
    im = Image.open(FIGURES / f"{src}.png")
    out = FIGURES / f"{dst}.png"
    im.crop(tuple(box)).save(out)
    print(out, im.crop(tuple(box)).size)

# The recap grid. Each shot is scaled to TILE and laid out two by two.
TILE = (1080, 750)
GUTTER = 40
RECAP = [
    "comms-shot-juliacon-prompts",
    "comms-shot-seabbs-bot",
    "comms-shot-spimo-statement",
    "comms-shot-covid-issue-171",
]
w, h = TILE
grid = Image.new(
    "RGB", (2 * w + GUTTER, 2 * h + GUTTER), "white"
)
for i, name in enumerate(RECAP):
    im = Image.open(FIGURES / f"{name}.png").convert("RGB")
    im.thumbnail(TILE, Image.LANCZOS)
    x = (i % 2) * (w + GUTTER)
    y = (i // 2) * (h + GUTTER)
    grid.paste(im, (x, y))
out = FIGURES / "comms-shot-recap.png"
grid.save(out)
print(out, grid.size)
