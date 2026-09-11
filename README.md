# Modelling and AI, Brussels 2026

Talk pages and slides for the workshop *Combining Infectious Disease
Modelling and AI: Methods and Communication*, VUB, Brussels, Monday 14
September 2026, and the research exchange at the VUB AI Lab on Tuesday 15
September.

Sam Abbott, London School of Hygiene & Tropical Medicine.

Rendered: [samabbott.co.uk/AIandIDVUB](https://samabbott.co.uk/AIandIDVUB)

## The talks

| When | What | Page |
|---|---|---|
| 14 Sep, 09:00–09:30 | Keynote: Infectious disease modelling in the age of AI | `keynote/` |
| 14 Sep, 13:40–14:10 | Lecture: Science communication with and under AI | `communication/` |
| 14 Sep, 15:20–16:15 | Panel: Where do we go next? AI, communication, collaboration | `panel/` |
| 15 Sep, 09:45–10:15 | Research exchange with the VUB AI group and SIMID | `exchange/` |

## Building

Requires [Quarto](https://quarto.org/) and, optionally,
[Task](https://taskfile.dev/) and [uv](https://docs.astral.sh/uv/) for QR
codes.

```sh
task          # render the site and all decks to _site/
task preview  # live-reloading preview
task qr       # regenerate QR codes
task lint     # line length and trailing whitespace
```

## Layout

- `index.qmd` — about me and links to the talks
- `{keynote,communication,exchange}/index.qmd` — one page per talk: the
  organisers' brief as the abstract, slides link, and resources
- `{keynote,communication,exchange}/slides.qmd` — the deck, with sections in
  `_partials/`
- `panel/index.qmd` — the panel, no deck
- `prompts.qmd` — the brief that made this, and the steers that followed
- `notes/` — research notes and style guidance for the agents that draft
  the decks; `notes/style.md` and `notes/llmisms.md` first
- `figures/` — shared figures and the QR codes, one per talk page

The QR code on each deck points at that talk's page here, not at the slides.

These pages and slides are drafted by coding agents; `prompts.qmd` describes
how.
