# Fixing the exchange deck against `audit-exchange.md`

13 September 2026.
Every row of `notes/audit-exchange.md` is below with what was done.
Renders with only the pre-existing OJS line-number warning.
`./scripts/lint.sh` clean.
All 18 `llmisms.md` greps run over `exchange/`; the remaining hits are
alt text, code, proper nouns and his own quoted wording.
No slide overflows 1080 px and no slide uses `.smaller`.
Nothing committed.

## Every audit row

| His point | Audit status | What was done |
|---|---|---|
| 20 mins composable, links to AI, composition, UDEs, PINNs | partly | Composable is now 8 slides and the AI section 8. Added "What we want from any approach" (his JuliaCon wording and the requirements table), a UDE slide and a PINN slide |
| 10 on delays, epidist | partly | Not changed. Delays is 4 counted slides and `epidist` is still one bullet. Outside the brief I was given; see Open questions |
| 5 workflow | done | Agentic is now 5 slides, up from 4, because the brief added "Agents building methods into software" and "What else went wrong" |
| An introduction of your work and group | done | Kept, cut from 5 slides to 4 |
| epinowcast org and seminar, Clara and Fanny | partly | Names verified, see Verified below. Text unchanged |
| epiforecasts led by Seb Funk, associated with | partly | `index.qmd` now says "I am associated with the epiforecasts group" |
| CMMID | done | Unchanged |
| Mine past presentations | done | One more mined slide, "What we want from any approach" from the JuliaCon composable deck, in his corrected wording |
| A slide with collaborators, organised logically | done | Kept, regrouped onto two slides. Tools and hubs sit beside delays and nowcasting on one slide; the Julia grid moved into the composable section |
| Small group, professional not sad | done | Unchanged |
| Use we, not our group or me | done | Unchanged; no new "my group" |
| Consulting, DRC, Pegasus, LLM-friendly tools | partly | Pegasus reworded, see below |
| AI fluff sentence | done | Still absent |
| Sensible number of slides | done | 30 content slides, up from 25; see Slide count |
| Vague and LLM weird titles | partly | `04-agentic.qmd` "Being able to follow a workflow" is now "A workflow for infectious disease modelling". "A neural network as a component?" is now "Universal differential equations" |
| Overly full slides | not done | Partly fixed. `.smaller` gone from the deck. The EpiNow2 slide is down to one figure and four bullets. "Who I am" still carries bullets, a photo and a six-row table |
| Image per slide | partly | Repeated headshots dropped from both code slides. The EpiNow2 slide is down to one figure. Two slides carry two figures each, by necessity: the merged collaborator grids, and "Agents building methods into software" where the brief placed two figures |
| Refs are too long | not done | Fixed. Every attribution block in the deck is now one or two sources |
| No refs for schematics | not done | Fixed. All 11 "Drawn for this talk", `scripts/...`, "read 2026-..", grep and internal-note lines deleted |
| Quotes assigned in the text | done | Unchanged |
| "I am very excited about their potential" alone | partly | Split onto its own `## And yet {.center}` slide, in his keynote wording |
| UDEs as a slide title, define a UDE, SEIR versus UDE | partly | New "Universal differential equations" slide. Defined in a sentence, with `exchange-seir-vs-ude.png` |
| A PINN slide | not done | New "Physics-informed neural networks" slide with `exchange-pinn.png`: what they are, the diagram, epidemic uses, limitations |
| Not forecasting without a mechanism | done | Unchanged |
| No little "I am part of it" sentences | partly | `index.qmd` "I am part of the EpiAware organisation" cut; the sentence is now "The composable modelling work is in Julia, in the EpiAware organisation" |
| Every project, the whale | done | Still absent |
| Who I work with at LSHTM is not accurate | done | Unchanged |
| Who I am is missing the meta focus | done | Unchanged |
| Julia collaborators, JuliaBayes | done | Unchanged, moved into the composable section |
| Cut "Maybe nothing doing" | done | Still absent |
| Cut RL and bandits | done | Still absent |
| Network hindered parameter identification | done | Unchanged |
| Renewal as a network layer, see the composable grants | partly | Grant self-citation deleted. His keynote line on renewal versus a differential-equation PINN added |
| Agentic modelling workflows next | done | Order unchanged |
| Not "each line I have drawn" | done | Still absent |
| Workflow slides earlier, no duplication | partly | The two nine-stage slides merged into one, "A workflow for infectious disease modelling", carrying the split figure |
| Agentic tree search from the keynote | partly | All three keynote additions added: the embedded inference step as an MCMC proposal in model space, how to enforce domain knowledge, and the compute and person-power gap |
| Outbreak-specific foundation model | done | Unchanged |
| "What even is AI?" | not done | Added as the opening slide of the AI section, his list verbatim |
| "Agents building methods into software" | not done | New slide with both figures the brief named: the approaches screenshot and the epidist meta-analysis fit for Bundibugyo virus disease |
| Another slide on what went wrong | partly | New "What else went wrong" slide: forecast bugs, automatic differentiation, observation-model proposals. Figure copied from the keynote as `exchange-agent-wrong.png` |
| Model structure specified by me, review still needed | done | Unchanged |
| Acronyms in full on first use | partly | ARIMA dropped from the EpiNow2 bullets. CRAN dropped from the package table, the column is now "Downloads" and the archive is named in full beneath. MCMC expanded on the tree search slide |
| No LLM filler | done | "so it reads like `dgamma`" cut. All greps re-run |
| The abstract and the deck telling the same story | partly | `index.qmd` reordered to composable, AI, workflow, delays, and the per-strand AI promise softened to "an open question rather than a set of answers" |
| About 1.5 content slides a minute | done | 30 content slides for 20 to 25 minutes, 1.2 to 1.5 a minute |
| His 20 / 10 / 5 split | contradicts another steer | Intro and people cut from 8 slides to 5. Composable is now 8 and the AI section 8, so the 20-minute block is 16 slides against 5 for the workflow and 4 for delays |
| Slides in the wrong place | partly | "Three outbreaks, the same problems" moved to open the composable section. The deck still ends on "Less clear where AI plugs in here" |

## Figures placed

All four were opened and checked by eye before anything was written about
them. All four show what their slide needs.

- `exchange-seir-vs-ude.png`. A semi-mechanistic stochastic SEIR with a
  random-walk transmission rate beside a UDE version whose rate is a
  network fed by mobility, surveys, policy, weather and wastewater. On
  the new "Universal differential equations" slide.
- `exchange-pinn.png`. Time into a network, out come the state and the
  transmission rate, into a data loss and a physics loss that sum to one
  training loss. On the new "Physics-informed neural networks" slide.
- `exchange-epiaware-approaches.png`. The approaches section of
  epiaware.org, two cards. On "Agents building methods into software".
- `exchange-epidist-meta-bdbv.png`. Onset-to-death delay densities, the
  meta-analysis model at population level, a re-analysis of the line
  list and the Rosello 2015 study-level estimate against the delay as
  reported. On the same slide.

Copied in: `exchange-agent-wrong.png`, the keynote's
`keynote-agent-wrong.png`, for the new "What else went wrong" slide.

Dropped from the deck: `exchange-composable-epinow2-model.png`, so the
EpiNow2 slide carries one figure.

Brought back into use: `exchange-composable-requirements.png` and
`exchange-people-grid-c.jpg`.

## Verified

- **The seminar organisers.** The audit says neither surname appears in a
  real source. It does.
  `~/code/epinowcast/epinowcast.github.io/seminars.qmd:19` asks people to
  contact "Sam Abbott, Fanny Bergström, or Clara Brigitta", with
  `fanny.bergstrom@maths.ox.ac.uk` and `clara.brigitta@lshtm.ac.uk`. The
  slide text is unchanged. Worth a look by him: "Clara Brigitta" reads
  like two given names, and that is exactly what the page carries.
- **Exercise Pegasus.** "Several teams used the tools in Exercise
  Pegasus" is now "Several teams used various tools in Exercise Pegasus,
  the UK's 2025 national pandemic exercise". No claim that the tools were
  ours, which the only written source (the os4ls grant text, "Epiverse
  tools were used in Exercise Pegasus") does not support.

## Slide count

25 content slides before, 30 now, plus six dividers, the title, the talk
plan, the thank you and one uncounted fallback.

Added: "What we want from any approach", the Julia collaborator grid
moved in from the people block, "What even is AI?", "And yet",
"Universal differential equations" and "A neural network in the slots of
a composable model" where there was one slide, "Physics-informed neural
networks", "Agents building methods into software", "What else went
wrong".

Removed: one collaborator slide, by putting the tools grid and the
delays grid side by side; one nine-stage workflow slide, by merging the
two.

The blocks now run intro 5, composable 8, AI 8, agentic 5, delays 4 plus
one uncounted.

## Open questions for him

- **`EpiDelays` on stage.** The slide names a UHasselt package rewired
  onto the `primarycensored` likelihood. UHasselt is half of the SIMID
  group in the room, the package is Oswaldo Gressani's, and per
  `notes/k3-report.md` the pull request to his repository has been open
  since April. Kept because it is his keynote content and it is the most
  direct bridge to this audience, but he should decide before the day.
- **The epidist meta-analysis figure.** `bdbv-linelist-analysis` is not
  cloned on this machine, so the figure's content was checked by eye and
  its legend read, but I could not confirm it was produced by the epidist
  meta model in pull request #620. The attribution points at the public
  report.
- **No scripts for four figures.** `exchange-seir-vs-ude.png`,
  `exchange-pinn.png`, `exchange-epiaware-approaches.png` and
  `exchange-epidist-meta-bdbv.png` arrived in `e6962b5` with no entry in
  `scripts/`, so they cannot be regenerated. The keynote equivalents can
  be, from `scripts/keynote-schematics.py` and
  `scripts/keynote-epiaware-shot.py`.
- **ARIMA in a figure.** Dropped from the EpiNow2 bullets, but
  `exchange-tree-search.png` still labels a node "ARIMA on admissions".
  Changing that means re-running `scripts/exchange-schematics.py`.
- **Two rows left alone** because they were outside the brief. `epidist`
  and the DRC use still have no delays slide, and the deck still ends on
  "Less clear where AI plugs in here" rather than on the foundation model
  or a thank-you line.
- **"Who I am" is still the fullest slide** in the deck: four bullets, a
  photo and a six-row table. Cutting the table would fix it, at the cost
  of the only evidence for "tools in wide use".
