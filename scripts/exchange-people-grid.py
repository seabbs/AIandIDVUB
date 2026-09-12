#!/usr/bin/env python3
"""Build one collaborator-grid image per group for
exchange/_partials/01b-people.qmd.

Each entry is (name, photo_path_or_None). Photos are cropped to a circle
at equal size; people with no confirmed real photo get a plain colour
tile carrying their initials instead. Output is 1600px wide, white
background, in the site palette (teal #1f6f8b, slate #4a5899, brick
#b5432f, greys).

Groups follow the work, not the institution. Sources: the GitHub API
for JuliaBayes and EpiAware membership (12 September 2026), package
DESCRIPTION and Project.toml author fields, and paper author lists, all
recorded in notes/research-collaborators.md and notes/r2-exchange-report.md.

Run with:
    uv run --with pillow scripts/exchange-people-grid.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "figures"

TEAL = (31, 111, 139)
SLATE = (74, 88, 153)
BRICK = (181, 67, 47)
GREY_TEXT = (51, 51, 51)
GREY_TILE = (150, 156, 163)
WHITE = (255, 255, 255)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

CANVAS_W = 1600
COL_GAP = 40
ROW_GAP = 30
NAME_H = 70
TOP_PAD = 40
BOTTOM_PAD = 30


def circular_crop(path, size, ring_colour):
    im = Image.open(path).convert("RGB")
    im = ImageOps.fit(im, (size, size), method=Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    ring = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(ring)
    w = 6
    rdraw.ellipse((w // 2, w // 2, size - w // 2, size - w // 2),
                  outline=ring_colour + (255,), width=w)
    out.alpha_composite(ring)
    return out


def initials(name):
    parts = [p for p in name.replace(".", "").split() if p]
    letters = [p[0] for p in parts if p[0].isupper()]
    if len(letters) >= 2:
        return (letters[0] + letters[-1]).upper()
    return name[:2].upper()


def initials_tile(name, size, colour):
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(out)
    draw.ellipse((0, 0, size, size), fill=colour + (255,))
    font = ImageFont.truetype(FONT_BOLD, int(size * 0.36))
    txt = initials(name)
    bbox = draw.textbbox((0, 0), txt, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]),
              txt, fill=WHITE, font=font)
    return out


def wrap_name(name, font, draw, max_w):
    words = name.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] > max_w and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines[:2]


def build_grid(people, ring_colour, out_path, cols=4, circle=260,
               name_size=30):
    """people: list of (name, photo_path_or_None)."""
    rows = -(-len(people) // cols)
    canvas_h = TOP_PAD + rows * (circle + 12 + NAME_H) + \
        (rows - 1) * ROW_GAP + BOTTOM_PAD
    total_cols_w = cols * circle + (cols - 1) * COL_GAP
    x0 = (CANVAS_W - total_cols_w) // 2

    canvas = Image.new("RGB", (CANVAS_W, canvas_h), WHITE)
    draw = ImageDraw.Draw(canvas)
    name_font = ImageFont.truetype(FONT_BOLD, name_size)

    for i, (name, photo) in enumerate(people):
        col, row = i % cols, i // cols
        x = x0 + col * (circle + COL_GAP)
        y = TOP_PAD + row * (circle + 12 + NAME_H + ROW_GAP)
        if photo is not None:
            tile = circular_crop(photo, circle, ring_colour)
        else:
            tile = initials_tile(name, circle, GREY_TILE)
        canvas.paste(tile, (x, y), tile)
        lines = wrap_name(name, name_font, draw, circle + 20)
        ty = y + circle + 14
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=name_font)
            tw = bbox[2] - bbox[0]
            draw.text((x + (circle - tw) / 2 - bbox[0], ty), line,
                      fill=GREY_TEXT, font=name_font)
            ty += int(name_size * 1.2)

    canvas.save(out_path, quality=92)
    print(f"wrote {out_path} ({canvas.width}x{canvas.height})")


def p(login):
    return FIGURES / f"exchange-people-{login}.jpg"


# Real-time tools and hubs: EpiNow2 and scoringutils authors.
GROUP_A = [
    ("Sebastian Funk", p("sbfnk")),
    ("James Azam", p("jamesmbaazam")),
    ("Nikos Bosse", p("nikosbosse")),
    ("Kath Sherratt", p("kathsherratt")),
    ("Hugo Gruson", p("bisaloo")),
    ("Joe Hickson", p("joehickson")),
    ("Hamada Badr", p("hsbadr")),
    ("Katelyn Gostic", p("kgostic")),
]

# Delays and nowcasting: epinowcast, epidist, primarycensored and
# baselinenowcast. Tiles where the GitHub avatar is not a photo or there
# is no login on record.
GROUP_B = [
    ("Adrian Lison", p("adrian-lison")),
    ("Kaitlyn Johnson", p("kaitejohnson")),
    ("Adam Howes", p("athowes")),
    ("Carl Pearson", p("pearsonca")),
    ("Kelly Charniga", None),
    ("Sang Woo Park", None),
    ("Thomas Ward", None),
    ("Christopher Overton", None),
]

# The Julia composable work. First row EpiAware members, the Turing.jl
# lead and the composable paper; second row JuliaBayes members. Jessica
# Cox and Penelope Yong have non-photo avatars, so tiles.
GROUP_C = [
    ("Samuel Brand", p("samuelbrand1")),
    ("Damon Bayer", p("damonbayer")),
    ("Michael DeWitt", p("medewitt")),
    ("Joseph Lemaitre", p("jcblemai")),
    ("Hong Ge", p("hong-ge")),
    ("Sandra Montes-Olivas", None),
    ("Penelope Yong", None),
    ("Peter Thestrup Waade", p("ptwaade")),
    ("Guillaume Dalle", p("gdalle")),
    ("Ryan Senne", p("rsenne")),
    ("Simon Steiger", p("simonsteiger")),
    ("Jessica Cox", None),
]


if __name__ == "__main__":
    build_grid(GROUP_A, TEAL, FIGURES / "exchange-people-grid-a.jpg")
    build_grid(GROUP_B, SLATE, FIGURES / "exchange-people-grid-b.jpg")
    build_grid(GROUP_C, BRICK, FIGURES / "exchange-people-grid-c.jpg",
               cols=6, circle=215, name_size=26)
