# Collaborator slides build report

New partial `exchange/_partials/01b-people.qmd`, 3 slides, included
after `01-who.qmd`. Grids built by `scripts/exchange-people-grid.py`
(Pillow) from avatars fetched by `scripts/exchange-people.sh`. Source
for every name and order: `research-collaborators.md`, groups (a),
(b), (c).

## Slide 1, LSHTM and epiforecasts (lines 14-22, all photos)

Sebastian Funk, James Azam, Nikos Bosse, Kath Sherratt, Hugo Gruson,
Joe Hickson, Michael DeWitt, Hamada Badr.
Skipped: Katelyn Gostic, Joel Hellewell (lines 23-24), and the
"Others, minor" row of 15 names at 1-4 commits each (line 25).

## Slide 2, the epinowcast community (lines 31-48, 4 photos, 4 tiles)

Photos: Adrian Lison, Kaitlyn Johnson, Adam Howes, Carl Pearson.
Tiles: Kelly Charniga, Sang Woo Park, Tim Taylor, Thomas Ward (UKHSA,
no GitHub login given).
Skipped: 11 minor or paper-only names (lines 36-51) and the seminar
speakers (line 52, attendees, not collaborators). Hannah Choi and
Nicholas Davies excluded, already confirmed identicons in the note.

## Slide 3, the Julia side (lines 58-67, 4 photos, 4 tiles)

Photos: Samuel Brand, Damon Bayer, Joseph Lemaitre, Jason Asher.
Tiles: Hong Ge, Sandra Montes-Olivas, Simon Frost, Anne Cori, none
with a GitHub login in the note.
Kaitlyn Johnson and Michael DeWitt are also group (c) (lines 60, 64)
but appear once each, on slides 1 and 2, not twice. Skipped: Katelyn
Gostic, Beau Bruce, Zachary Susswein, Dylan Morris, Eric Rescorla
(lines 68-72, all minor).

Identicons and non-photos, fetched but unused, kept as an audit
trail: Kelly Charniga and Sang Woo Park are GitHub identicons,
confirmed by eye; Tim Taylor's avatar is a real photo, of a buffalo,
so treated as no photo.

## Trimming for the 22 minute budget

The new slides add about a minute. Sebastian Funk was the only name
truly repeated, already pictured on the `epiforecasts` slide, so I
dropped that photo there and pointed its attribution at the new
slide. `epinowcast, the community` names Fanny Bergström and Clara
Brigitta, neither in `research-collaborators.md`, so left as is.
Updated the talk plan bullet.

## For Sam to check

- Name spellings taken as given: Hamada Badr, Sang Woo Park, Joseph
  Lemaitre.
- Samuel Brand's photo now appears here and on the composable slide
  (`02-composable.qmd:131`), maybe one photo too many.
- Thomas Ward and Tim Taylor have no confirmed photo. Worth a tile,
  or cut.

Checks: lint clean, all 18 `llmisms.md` greps clean on the new
partial, deck renders, and all 4 changed slides screenshot correctly
at 1920x1080.
