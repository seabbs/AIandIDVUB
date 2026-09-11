# Draft report: research exchange deck

Written 2026-09-11 after the first full draft of `exchange/`.
Built for 22 minutes against `spec-exchange.md`.
Nothing is committed.

## What I built

Deck title, on `slides.qmd` and as the `index.qmd` subtitle:
*Composable infectious disease modelling, and where AI might plug in*.

The six placeholder partials are gone.
Five partials replace them, in the spec's running order:

| Partial | Divider | Content slides | Minutes |
|---|---|---|---|
| `01-who.qmd` | none | 1 | 1 |
| `02-composable.qmd` | Composable infectious disease modelling | 9 | 12 |
| `03-ai.qmd` | Where AI might plug in | 2 | 3 |
| `04-delays.qmd` | Recent delays work | 5, one uncounted | 6 |
| `05-workflow.qmd` | The workflow | 2 | 3 |

Rendered deck: 26 slides.
Title, plan, four dividers, 18 counted content slides, one uncounted
static fallback, thank you.
That is about 0.8 counted content slides a minute, under the 1.5 of the
JuliaCon decks, because the spec's minute budget was tight and the
composable section carries two code slides and a replication slide that
each need time.

Both `quarto render exchange/slides.qmd` and `quarto render
exchange/index.qmd` succeed (outside the sandbox; inside it fails with
"unrecognized architecture" as the rules predict).
`./scripts/lint.sh` is clean for `exchange/`.
It prints `awk: can't open file` for the five deleted partials because
they are still in the git index; `git rm` at commit time clears that.
The lint failures it reports in `communication/_partials/01-audiences.qmd`
are not mine.

## Running order, slide by slide

1. Talk plan and QR. Plan bullets rewritten to the five sections.
2. Who I am and what the group does. Four bullets glossing $R_t$ and
   nowcasting on first use, photo, and the keynote's timeline strip
   beneath, copied as `exchange-timeline.png` once the keynote agent had
   made it.
3. Composable. Whitty and Cramer (JuliaCon `00-gap.qmd`, wording kept);
   chaining, the ONS cascade (JuliaCon `01-options.qmd`, one bullet
   cut); joint modelling, Lison (JuliaCon `01-options.qmd`, mpox bullet
   cut); what is composable modelling (JuliaCon `01b-composable.qmd`,
   Figure 1); what we want from any approach (JuliaCon
   `02-composable.qmd`, third bullet swapped, see below); two
   approaches (epiaware.org/approaches wording); `ComposableTuringIDModels.jl`
   with the approaches page's `renewal_model.jl`; `ComposedDistributions.jl`
   with the approaches page's `composed_delays.jl`; the `EpiNow2`
   replication (JuliaCon `04-case-study.qmd`, attribution shortened to
   fit).
4. Where AI might plug in. A neural network as a component, with a
   drawn figure and the Philipps et al. caveats, ending in "What would
   you put in the slot?"; agents building and checking the parts, with
   the BVDOutbreakSize facts, ending in "What would convince you a part
   an agent built is right?".
5. Delays. An epidemiological delay (JuliaCon `00-delay.qmd`, verbatim);
   both events recorded to the day (primary and secondary censoring
   merged onto one slide with the double censoring figure and both
   equations); right truncation as the one interactive, an `{ojs}`
   slider moving the cutoff; the static fallback "A mean of 3.9 days
   instead of 5.9" as an uncounted slide straight after; three
   packages, one likelihood (the `CensoredDistributions.jl` model from
   JuliaCon `05-julia.qmd` with one bullet each for `primarycensored`,
   `epidist` and the Julia package); less clear where AI plugs in here,
   two questions marked as his uncertainty.
6. Workflow. The schematic (JuliaCon `02a-workflow.qmd`); where AI sits,
   with a drawn strip of the nine stages.
7. Thank you and QR. Links updated to the approaches page, the two
   Julia packages, the three delay packages and BVDOutbreakSize.

## What I cut from the 35 minute steer to reach 22

His steer was 20 on composable, 10 on delays, 5 on workflow.

**Composable, 20 to 12.** Kept the Whitty framing, one chaining slide,
one joint slide, the definition, the design considerations, the two
approaches with code, and one replication.
Cut from the 40 minute deck and the JuliaCon cut: the COVID (Birrell),
mpox (Endo), viral load (Hay) and multi-model gap slides, apart from
the Cramer bullets which sit on the Whitty slide; PPLs reduce effort;
the $R_t$ ecosystem and $R_t$ research slides; epinowcast's limits; the
"this pattern repeats" slide; the ARIMA, Mishra and Chatzilena case
studies; the struct, `as_turing_model` and `as_turing_submodel`
internals; "Some fun bits and bobs"; the Turing.jl backend slide and
the small teams slide; "Where we are" and the `Distributions.jl`
slide; "Is Julia the place for this work?".
The design considerations went from twelve rows to three bullets with
Table 1 as the figure.

**Delays, 10 to 6.** Kept the definition, the two biases, the software
and the AI question.
Cut the `fitdistrplus` internals, the Stan duplication table, the
`integrate_1d` failure and `ode_rk45` recast, Stan vendoring, the
`brms` regex, the autodiff backend table, the downloads and dependants
slide, and "In my view the Julia version is better".
Primary and secondary censoring share one slide.

**Workflow and AI, 5 to 4.** Two slides.
The bot pull requests per month chart, the money and access slides and
the community slides from how-I-llm are not here; the keynote carries
that material the day before.

## Every number, with its source

| Number or date | Slide | Source |
|---|---|---|
| Tuesday 15 September 2026, 09:45, Pleinlaan 9 | plan | `exchange-programme.md` |
| Timeline dates 1760 to 2026 | who | `keynote-timeline.png`, drawn by the keynote agent from `research-history.md` sections 1 to 3 |
| 4M+ swabs, 150K households, £500M+, April 2020 to March 2023 | ONS cascade | JuliaCon `composable/_partials/01-options.qmd`, from the Abbott and Funk 2022 introduction |
| Cramer 2022, Whitty 2015, Lison 2024, Abbott and Funk 2022 DOIs | composable | JuliaCon composable partials |
| Six themes, twelve requirements | design considerations | Table 1 of the paper; `epiaware.org/approaches` lists twelve |
| Photos read 2026-08-13 | two approaches | JuliaCon `03-approach.qmd`, `06-direction.qmd` |
| Approaches page read 2026-09-11 | two approaches, code slides | fetched today |
| ~3 hours, no new components | EpiNow2 | 40 minute deck and JuliaCon `04-case-study.qmd` |
| Italy, February to June 2020 | EpiNow2 | JuliaCon `04-case-study.qmd` |
| Philipps et al. 2025 quotes | network component | `research-ai-methods.md` B3, PMC12398592 |
| No Lux or Flux code in EpiAware | network component | `research-ai-methods.md` A3, and my own grep over `~/code/EpiAware` excluding worktrees and `_site`, 2026-09-11 |
| McCabe et al. report of 18 May, replicated in a few hours the next day | agents | JuliaCon `roadmap/_partials/00-outbreak.qmd`; repo created 2026-05-19 per `gh repo view` |
| 145 releases, newest 2026-09-09 | agents | `research-agentic.md` section 5, `gh release list` |
| 333 of 425 pull requests by the bot | agents | `research-agentic.md` section 5, GitHub search API |
| Two blind readers | agents | `BVDOutbreakSize/data/README.md:99-111` |
| SitRep 087, y axis steps 20 to 25, caught by the reporting-triangle invariant | agents | `BVDOutbreakSize/data/README.md:77` |
| Outbreak size figure is a June 2026 fit | agents | `research-agentic.md` section 4 |
| `LogNormal(1.6, 0.6)`, mean 5.9; 3.9 at day 7, 5.3 at day 14 | truncation fallback | JuliaCon `delays/_partials/01-biases.qmd`, `scripts/delays-right-truncation.jl`, `CensoredDistributions.jl` v0.2.22 |
| Mean seen 4.1 at day 7 on the slider | truncation interactive | computed live in the `{ojs}` cell, continuous delays; the attribution says why it differs from 3.9 |
| `CensoredDistributions.jl` model, v0.2.22 | software | JuliaCon `delays/_partials/05-julia.qmd`, `README.md:67-81` |
| Closed forms for gamma, lognormal, Weibull | software | JuliaCon `delays/_partials/01-biases.qmd`, `02-software.qmd` |
| NEJM correspondence used `epidist`, doi:10.1056/NEJMc2608070 | software | JuliaCon `delays/_partials/06-adoption.qmd` |
| Jang, Candan and Chowell 2026; Radev et al. 2021 | AI in delays | `research-ai-methods.md` B4 |
| Nine workflow stages | workflow strip | `a-workflow-for-infectious-disease-modelling/main.tex` subsection titles |
| Agents wrote ingest, pipeline, tests, docs, releases, sensitivity analyses; did not pick the model, the lower bound meaning, the ascertainment judgement | where AI sits | `research-agentic.md` section 1, how-I-llm `04-drc.qmd`, restated in plain words |

## Figures

Copied from `/Users/lshsa2/code/seabbs/JuliaCon2026/figures/` with the
`exchange-` prefix: `composable-whitty.png`, `composable-ons-cascade.jpg`,
`composable-lison.png`, `composable-structure.png`,
`composable-requirements.png`, `composable-epinow2-model.png`,
`composable-epinow2-results.png`, `delays-natural-history.png`,
`delays-double-censoring.png`, `delays-right-truncation.png`,
`workflow-schematic.png`, `bvd-outbreak-streams.png`, `samuel-brand.jpg`.
`sam-abbott.jpg` and `seabbs-bot.jpg` were already in `figures/`.
`exchange-timeline.png` is a copy of the keynote's `keynote-timeline.png`
(`scripts/keynote-timeline.py`, dates from `research-history.md`).

Drawn, both in the site palette:

- `scripts/exchange-nn-component.py` makes `figures/exchange-nn-component.png`.
  The three parts of a composable Turing model with the `rt` slot drawn
  twice, once holding an AR process and once a small network, and a
  swap arrow.
- `scripts/exchange-workflow-split.py` makes `figures/exchange-workflow-split.png`.
  The nine stages as a strip, his "agents did" list below and his
  "stayed with people" list above.

Interactive: one, the right truncation slider, with the static figure on
the next slide as fallback.
The keynote had not made a renewal slider when I looked, so I built the
delay one the rules suggest.

## llmisms greps

Run over `exchange/`.
One hit of mine fixed: a bolted-on clause on the composed distributions
slide, split into two sentences.
Remaining hits are his own wording carried over ("timely, rigorous, and
collaborative", "Current approaches struggle", the colon glosses on the
ONS and Lison slides, "which is typically more complicated to
evaluate", "so it reads like `dgamma`"), attribution lines, alt text,
verified numbers, and `## Talk plan`, which the spec keeps.

## What I was unsure about

- **The who slide reuses the keynote's timeline strip.** It is a copy
  of `figures/keynote-timeline.png` taken 2026-09-11; if the keynote
  agent redraws it, recopy. The alt text describes the copy I saw.
- **"Less clear where AI plugs in here" has no figure.** Four question
  bullets at full width. His asks slides in the serial interval deck
  are bullets only, so I left it, but it is the one slide that breaks
  the visual rule.
- **Interactive plus fallback is two slides on one point.** The
  fallback is `{visibility="uncounted"}` and directly follows the
  slider, so it is there if the room has no network. If that reads as a
  repeat, drop the fallback to after the close.
- **The third design consideration.** The JuliaCon cut used Uncertainty,
  Model structure and Workflow. For this room I swapped Workflow for
  Interoperability, since its wording names machine learning and ODEs
  (40 minute deck). Easy to revert.
- **The network slide framing is mine.** "The `rt` slot could hold a
  network" and the `network(covariates) → log R_t` label in the figure
  are my framing of what a UDE-like component would be here. His own
  material only has the EU grant vision sentence on UDEs and "maybe
  nothing doing there at the moment", which is on the slide verbatim.
- **The workflow strip placement is mine.** Stage names are the
  paper's; which of his lists sits under which stage is my reading of
  the BVDOutbreakSize README and data notes. The attribution says so.
- **"Two blind readers each."** `data/README.md` says two blind readers
  per vintage for the digitised onset curve and mirror cross-checks for
  confirmed series. Worth a read before it stays.
- **"Each line I have drawn between the two columns has moved within
  months."** A restatement of "Every boundary I have drawn in two years
  has moved. 'Agents cannot do long-horizon work' lasted about six
  months" from how-I-llm, which is bot phrasing of his fact.
- **The NEJM correspondence has no author on the slide.** The delays
  deck gave only the DOI; I did not fetch the paper.
- **The room's theme is still unknown.** The organiser has not replied.

## Outside my scope, for the orchestrator

- The root `index.qmd` exchange card still says "Background, research
  group, and current work" as its subtitle and the two-line blurb still
  describes the old plan. I did not edit it.
- The five deleted partials need `git rm` so the lint script stops
  warning.
- `communication/_partials/01-audiences.qmd` fails the 80 character
  lint on six lines.

## Anything in the spec I could not do

Nothing was blocked.
The composed distribution slider was the spec's first suggestion for the
interactive; I chose the truncation slider instead because it has a
correct static twin already in his delays deck and a one-line mechanism
to show.
