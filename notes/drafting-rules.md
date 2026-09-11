# Drafting rules for the decks

Read in this order before writing a slide: `style.md`, `llmisms.md`,
`tone-precedent.md`, `proposal.md`, the spec for your deck, then the
research notes it cites.

## What a slide is

- `##` heading that says the thing, not the topic. Wry where he would be.
- Two columns, about 40/60. Three or four short bullets on one side, one
  figure, schematic, code block or interactive on the other.
- The figure explains. The bullets say what the figure cannot.
- One `::: {.attribution}` block for sources only: paper, repo, URL, date
  read. No asides, no cross-references, no commentary.
- At most one callout, one sentence, and only when it carries a fact.
- No sub-bullets. No bullet longer than two lines.
- Section dividers are `# Title` slides with nothing else on them.

## Pictures and interactives

He asked for pictures, schematics and interactives, and sparse text.

- Every content slide has a visual unless it is a code slide or a single
  quote.
- Reuse first. The research notes list figures on disk with paths. Copy
  what you use into `figures/` with your deck's prefix, for example
  `keynote-bvd-streams.png`, and record the source path in the
  attribution.
- Draw what does not exist. Timelines, loops, box diagrams, before and
  after pairs. Write a script in `scripts/` (Python with matplotlib via
  `uv run --with matplotlib`, or hand-written SVG) so it can be regenerated.
  Match the site palette: teal `#1f6f8b`, slate `#4a5899`, brick `#b5432f`,
  greys. No mermaid box-and-arrow diagrams; he called them weak.
- Interactives, one to three per deck, only where they earn it. Options
  that work in Quarto revealjs: an `{ojs}` cell with an `Inputs.range`
  slider driving a Plot (for example a renewal process or a delay being
  censored); an `<iframe>` of a live site (the BVDOutbreakSize report at
  https://epiforecasts.io/BVDOutbreakSize/stable/, the COVID dashboard at
  https://epiforecasts.io/covid/); a revealjs `fragment` reveal on a
  before and after figure. Every interactive needs a static fallback
  figure in the same partial in case the room has no network.
- Alt text on every image.

## Words

- Where the research marks a line as **[Sam's words]**, use it verbatim.
- Lines from `how-I-llm` carry his facts in bot phrasing. Restate the fact
  plainly. Do not copy the phrasing.
- Every number and date comes from a research note with a source, and the
  source goes in the attribution. No number without one.
- Gloss on first use, one line each, for a room of statisticians and AI
  researchers: $R_t$, nowcasting, renewal process, pull request, bot
  account, SPI-M-O, SAGE, UKHSA, WIS.
- Run the greps in `llmisms.md` over your partials before you finish and
  fix every hit that is a fault.
- UK English. Under 80 characters a line except link targets and headings.
  No trailing whitespace. `./scripts/lint.sh` must pass.

## Mechanics

- Write into the existing `_partials/*.qmd` files for your deck, replacing
  the HTML comment. Keep the `#` divider slide. You may add or rename
  partials; if you do, update the `{{< include >}}` list in `slides.qmd`
  and the talk plan bullets to match.
- Edit only your deck's directory, `figures/` files with your prefix,
  `scripts/` files with your prefix, and your report in `notes/`.
- Render with `quarto render <deck>/slides.qmd`. If it fails with
  "unrecognized architecture" the sandbox blocked it; retry with the
  sandbox disabled.
- Do not commit or push. The orchestrator does.
- When done, write `notes/draft-<deck>-report.md`: what you built, slide
  count, every number with its source, figures made or copied, what you
  were unsure about, and anything in the spec you could not do.
