#!/usr/bin/env python3
"""Crop reused figures to the panel the slide needs.

Run with:
    uv run --with pillow scripts/keynote-crop.py

Inputs are the files as downloaded or copied into figures/. Outputs sit
beside them with a -panel suffix, so the originals stay for the record.

- keynote-funk2019-forecasts.png: Fig 2 of Funk et al. 2019, PLOS Comput
  Biol, CC-BY 4.0, downloaded from
  https://doi.org/10.1371/journal.pcbi.1006785.g002. Panel B only.
- keynote-bvd-infections-sep.png: the cumulative infections figure from
  the BVDOutbreakSize release results-1699 site bundle (analysis page,
  "Joint model estimates", data to 6 September 2026). Top row only.
- keynote-example-rt.png: the six-panel Rt example from the 25 March 2022
  rt-reflections post at samabbott.co.uk. Top two rows, four panels, so
  the axis text is legible in a 60% column; the shared y-axis title on
  the far left is cropped away with them.
"""

from PIL import Image

CROPS = {
    # (left, top, right, bottom) as fractions of width and height.
    "keynote-funk2019-forecasts.png": (
        "keynote-funk2019-forecasts-panel.png", (0.505, 0.0, 1.0, 1.0)),
    "keynote-bvd-infections-sep.png": (
        "keynote-bvd-infections-sep-panel.png", (0.0, 0.0, 1.0, 0.345)),
    "keynote-example-rt.png": (
        "keynote-example-rt-panel.png", (0.041, 0.0, 1.0, 0.592)),
}

for src, (dst, frac) in CROPS.items():
    im = Image.open(f"figures/{src}")
    w, h = im.size
    box = (int(frac[0] * w), int(frac[1] * h), int(frac[2] * w),
           int(frac[3] * h))
    im.crop(box).save(f"figures/{dst}")
    print("wrote figures/" + dst, im.crop(box).size)
