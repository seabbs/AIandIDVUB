# Mining report: keynote deck

Against the 12 September steer to mine past decks for images and slides.

## Lifted

| Slide | Lifted | From | Replaced |
|---|---|---|---|
| How I work now | Bullet "I was travelling for summer schools, teaching and workshops, so decided to have a go with agents"; `seabbs-bot.jpg` and `sbfnk-bot.jpg` avatars as a third column | JuliaCon 2026 roadmap, `_partials/05-what-it-takes.qmd` and `figures/{seabbs-bot,sbfnk-bot}.jpg` | Generic opening bullet; text-only 40/60 layout |
| What keeps going wrong | Figure and its caption's first line ("condition on being observed") | how-to-serial-interval, `_partials/02-censoring.qmd` and `figures/fig-truncation.png` | Freshly-drawn `keynote-chain.png` bell-curve diagram |
| A live outbreak built this way (both) | Bullet wording tightened to his phrasing: "A replication of the McCabe et al. report of 18 May, in a few hours the next day"; "Agents ingest them directly" | JuliaCon 2026 roadmap, `_partials/00-outbreak.qmd` | Looser paraphrase of the same facts |

All three copies verified byte-identical to source. Render, 1920x1080
screenshots of the three changed slides, `./scripts/lint.sh`, and the
`llmisms.md` greps all clean; no new hits beyond ones already accepted
in `fix-keynote-1.md`.

## Considered and rejected

- JuliaCon "Where does Julia come in" (`01-need.qmd`): Julia-vs-R
  implementation detail; off-topic for this room and this deck's
  brief, which stays at the modelling level.
- JuliaCon "Six years of trying this in R and Stan" table (`04-r.qmd`):
  the keynote's own `keynote-packages.png` timeline already covers more
  packages, extends to 2026, and is a schematic rather than a table,
  which the style guide prefers.
- JuliaCon "Community, in the age of robots" (`10-community.qmd`): a
  different argument (open-source erosion) from section E's
  forward-looking close; would append, not swap.
- BVDOutbreakSize collaboratory (10 June, joint authorship with
  Sherratt, Brand and Funk): `generative-process.svg` and
  `validation-mccabe.png` fit a methods slide, but section C is about
  the agent workflow, not model methodology; the McCabe comparison is
  already the live iframe per the spec's steer. The three-panel
  sitrep/streams/Rt opener is June vintage, superseded by the
  deck's September-vintage figures.
- hpru-ppie-kickoff: dashboard and ensemble figures belong to the
  communication lecture (`proposal.md` section 2), not this deck.
  `germany_early.png`, `germany_historical.png` and `mechanism*.png`
  are unused orphans in that repo with no caption or context to source
  them safely.
- nfidd "a lot of data or very good theory": already attributed to
  Nick Reich in the prior pass; confirmed by `git log` (author
  Nicholas Reich), left as is.
- Other how-to-serial-interval figures (contact interval, secondary
  and double censoring): no other slide's claim matches their
  specific content.
