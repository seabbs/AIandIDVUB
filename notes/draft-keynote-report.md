# Draft report: keynote deck

Written 11 September 2026 after drafting `keynote/_partials/*.qmd`.
Nothing is committed.
`quarto render keynote/slides.qmd` succeeds (with the sandbox off, as the
rules predict), `./scripts/lint.sh` is clean, and the `llmisms.md` greps
over `keynote/_partials` return only hits judged not to be faults (listed
below).

## What was built

Five partials, following `proposal.md` section 1 slides 1 to 19 in order
with the steers in `spec-keynote.md`.

| Partial | Slides | Content |
|---|---|---|
| `01-outbreaks.qmd` | 6 | timeline strip; 2014; 2020; what came out of it; 2022; 2026 |
| `02-modeller.qmd` | 3 visible, 1 hidden | the loop; the renewal slider; what keeps going wrong |
| `03-agents.qmd` | 6 visible, 1 hidden | what an agent is; how I work; live outbreak; hard to check; what changes; what does not |
| `04-other-ai.qmd` | 4 | map; UDEs and PINNs; flows and SBI; foundation models |
| `05-question.qmd` | 2 | my guess; the question |

Rendered deck: 29 numbered slides.
Title, talk plan, five section dividers, 21 content slides, thank you.
Two further slides carry `{visibility="hidden"}` as static fallbacks for
the interactives and do not count.
Content slides against the proposal's 19: the renewal slider is an extra
slide (spec asked for it), and the question is split from "my guess" as a
single-quote slide.
At 25 minutes that is about 0.85 content slides a minute.

### Interactives, two as the spec asked

1. **Renewal process slider**, `02-modeller.qmd`. An `{ojs}` cell with
   `Inputs.range` for $R$ and the generation interval mean, driving a
   `Plot.plot` of infections per day on a log scale. Renders and responds
   in the rendered deck. Observable Plot is loaded from a CDN at run time,
   so a room with no network gets an empty column. Fallback: the next
   slide, same heading, `keynote-renewal.png`, marked
   `{visibility="hidden"}`. Swap the `visibility` attribute between the
   two slides to switch.
2. **Live BVDOutbreakSize report**, `03-agents.qmd`, an `<iframe>` of
   https://epiforecasts.io/BVDOutbreakSize/stable/ in the 60% column.
   In a headless screenshot the page loaded but unstyled (raw links and
   headings), which is either the site's JavaScript not finishing in the
   screenshot window or a framing restriction. **Check this in a real
   browser before the talk.** Fallback: hidden slide with
   `keynote-bvd-rt-sep.png`, the $R_t$ figure from release `results-1699`.

The third candidate, a fragment reveal on the timeline, was not built.

### Options decided

- Slide 8 "Option: the Belgian scoping review". Included as the one
  callout on the slide: "Half of the 105 Belgian COVID-19 models reviewed
  by Bagaforo et al. 2026 had no behaviour component." It is a fact this
  room co-wrote and it hands to Abrams. Source `research-workshop.md`
  section 2 (Bagaforo, Dupas, Abrams, Dellicour and Hens 2026,
  doi:10.1186/s13690-026-01959-3).
- Slide 5 credits Overton et al. 2023 and the BMJ editorial, and says
  Ward et al. did the delay estimates, as the spec requires.
- Slide 13 carries the Google point as LLM-guided tree search, with its
  own loop schematic and Bracher and Funk in the attribution.
- The proposal's "Figure: sitrep page beside the streams posterior" for
  slide 11 became the live iframe (spec steer), and the sitrep page moved
  to slide 6 beside the September cumulative infections figure. The June
  per-stream posterior on disk was not used because its numbers are three
  months stale.
- Section A slide 6 uses the WHO DON617 counts (6757, 3267) in the
  bullets and the model's 90% interval (9,700 to 19,200) rounded.

### Glosses on first use

$R$ (slide 2), $R_t$ (slide 3), SPI-M-O (slide 3), nowcasting (slide 4),
UKHSA (slide 5), renewal process and generation interval (slides 7 and
7b), pull request (slide 9), bot account (slide 10).
SAGE and WIS are not used.
"Reporting triangle" is avoided; slide 12 says "counts on twelve-week-old
dates fell. Old counts cannot fall" instead.

## Figures

### Made, with scripts in `scripts/`

| Figure | Script | Notes |
|---|---|---|
| `keynote-timeline.png` | `keynote-timeline.py` | broken axis, deep history compressed left, four outbreaks right, colour marks mine from others' |
| `keynote-packages.png` | `keynote-timeline.py` | first-commit or repo-creation month per package |
| `keynote-bot-prs.png` | `keynote-counts.py` | Jan to Sep 2026, Sep to the 11th in grey |
| `keynote-bvd-authorship.png` | `keynote-counts.py` | 497 commits by identity |
| `keynote-onset-vintages.png` | `keynote-onset-vintages.py` | reads `data/onset_curve_scanned.csv` from the local BVDOutbreakSize clone; weekly onsets for five report dates |
| `keynote-loop.png`, `-chain.png`, `-agent.png`, `-sai-loop.png`, `-map.png`, `-ude.png`, `-sbi.png`, `-foundation.png`, `-renewal.png`, `-who.png` | `keynote-schematics.py` | matplotlib box diagrams in the site palette |
| `keynote-funk2019-forecasts-panel.png`, `keynote-bvd-infections-sep-panel.png` | `keynote-crop.py` | crops of the two files below |

### Copied or downloaded

| Figure | Source | Licence or note |
|---|---|---|
| `keynote-funk2019-forecasts.png` | https://doi.org/10.1371/journal.pcbi.1006785.g002, Fig 2 of Funk et al. 2019 | CC-BY 4.0; panel B cropped for the slide |
| `keynote-overton2023-historical.png` | https://doi.org/10.1371/journal.pcbi.1011463.g007, Fig 7 of Overton, Abbott et al. 2023 | CC-BY 4.0 |
| `keynote-example-rt.png` | `seabbs/seabbs.github.io/_posts/2022-03-25-rt-reflections/example-rt.png` | his own; transparent background, renders fine on white |
| `keynote-bvd-sitrep.png` | `seabbs/JuliaCon2026/figures/bvd-insp-sitreps.png` | INSP SitRep 25 page, 8 June 2026 |
| `keynote-bvd-infections-sep.png`, `keynote-bvd-rt-sep.png` | `site.zip` asset of BVDOutbreakSize release `results-1699` (9 September 2026), files `assets/infections.*.png` and `assets/rt.*.png` on the analysis page | September vintage, data to SitRep 115 of 6 September |

Not used: `how-I-llm/figures/bot-prs-by-month.png` (rebuilt instead),
`bvd-authorship.png` (rebuilt), the June `bvd-outbreak-streams.png`
(stale), `workflow-schematic.png` (proposal asked for a four-box loop for
a non-modeller instead of the nine-stage schematic).

## Every number, with its source

Section A

- 1760, 1911, 1927, 2001, 2009: `research-history.md` section 3.
- 23 March 2014 (WHO notified), 23 July 2022 (mpox PHEIC), 17 May 2026
  (BVD PHEIC): `research-history.md` section 2.
- 1.4 million by 20 January 2015: Meltzer et al. MMWR 2014, section 2.
- About 21,000 by mid January 2015: section 2, CDC MMWR su6503a12.
- "several thousand locations": 2022 rt-reflections post, section 5 and
  `research-communication.md` section 2.
- Dashboard repo created 21 March 2020, last global estimates 31 March
  2022: section 1. The slide says "spring 2020 to March 2022".
- First commits: scoringutils 2020-02-14 and baselinenowcast 2026-04-13
  from `git log --reverse` on the local clones (run today); EpiNow repo
  15 March 2020, covid repo 21 March 2020, EpiNow2 17 June 2020, CRAN
  1 September 2020, European hub 13 January 2021, epinowcast 29 October
  2021, epidist 18 October 2022, Rt-without-renewal 5 February 2024,
  primarycensored 21 August 2024, BVDOutbreakSize 19 May 2026: section 1.
- CDC use of EpiNow2: CDC CFA nowcasting page and MMWR 21 November 2024,
  `research-communication.md` section 3.
- 15 May declaration, 17 May PHEIC: WHO DON602.
- 6757 confirmed cases, 3267 deaths by 7 September: WHO DON617.
- 9,700 to 19,200 infections: the 90% interval 9749 to 19236 for `C_T` in
  the analysis page of release `results-1699` (site bundle downloaded
  today), rounded on the slide.

Section B

- 105 models, half with no behaviour component: Bagaforo et al. 2026,
  `research-workshop.md`.
- "We sometimes published nonsensical estimates": 2022 post,
  `research-communication.md` section 2.
- The slider's shape 4 gamma, five seed days of ten infections: my
  choices for the toy, stated in the attribution.

Section C

- Bot PRs per month Jan 17, Feb 92, Mar 78, Apr 61, May 124, Jun 531,
  Jul 744, Aug 399, Sep 98 to the 11th; 2144 total, 1834 merged (85.5%),
  256 closed unmerged (11.9%): `research-agentic.md` section 5.
- seabbs-bot created 23 January 2026: section 5.
- 712 of 1371 merged bot PRs without review: how-I-llm commit 8c7e834,
  `research-agentic.md` section 1.
- McCabe et al. 18 May; replication next day; repo created 2026-05-19
  with 33 commits: section 2.
- 145 releases, `results-43` 2026-05-20 to `results-1699` 2026-09-09:
  section 5.
- 333 of 425 PRs by the bot: section 5. Four authors: section 2.
- Two blind readers: `data/README.md`, section 2.
- SitRep 081 54% under, one pixel ticks; SitRep 087 grid 20 to 25,
  caught by a fall on twelve-week-old dates: `data/README.md` in
  BVDOutbreakSize (read directly today, lines quoted in
  `research-agentic.md` section 2).
- "each read sits a few percent under the printed total": the README's
  band of −5.0% to +1.6% over SitReps 059 to 083 and −3.8% to −9.3% for
  087 to 089.
- Google topped the three CDC hubs in 2025/26; 11% retrospective gain
  attributed to data revision leakage: Martinson et al. 2026 and Bracher
  and Funk 2026, `research-ai-methods.md` B1.
- 497 commits, 392 bot (238 + 144 + 7 + 3), 50 Dependabot, 55 by hand
  (40 + 11 + 3 + 1): `git log` counts in section 5.
- Quotes: "Who can do this work at all is narrowing. Agents make that
  worse" (roadmap deck, his edited words); "I do not have a defence for
  this. I am part of the problem" (how-I-llm, listed in `llmisms.md` as
  a survivor).

Section D

- Kraemer et al. 2025, Nature 638, 623 to 635, Table 1 tasks and methods:
  fetched today from PMC11987553. The eight rows on the map are that
  table's rows, paraphrased for space. The ninth row and the markers are
  mine.
- Philipps et al. 2025 "did not match the published values", Millevoi et
  al. 2024 deterministic and poor extrapolation: `research-ai-methods.md`
  B3.
- OutbreakFlow, Pinotti et al. 2014 Sierra Leone SEIR, Jang et al.
  "additional simulations alone cannot resolve": B4.
- Kalahasti et al. 2025, Wang, Li and Perra 2026 (TabPFN-TS, nine
  countries, RespiCast), Jafari et al. 2026: B2.
- "a lot of data or very good theory": nfidd `good-models.qmd`, A1.

Section E

- "long-horizon work lasted about six months": how-I-llm
  `07-whats-left.qmd`, `research-agentic.md` section 1.

## llmisms grep hits left in place, and why

- Pattern 5 (rule of three): author lists, alt text, and "falling, flat
  and rising" for $R$ below, at and above one. Load-bearing.
- Pattern 8 (colon gloss): "A renewal process: today's infections are..."
  and "Nowcasting: estimating what has...". Both are definitions where
  the right-hand side is the substance.
- Pattern 13 (absolutes): "Refit on every push" (the README says each
  push refits), "topped all three" (Bracher and Funk), "Most infections
  are never confirmed" (a measured share, and his own line), "Who can do
  this work at all" (his quote).
- Pattern 6: "Not an RL policy. Not a chatbot" kept, as review-1 judged
  it a contrast the room holds.

Fixed after the greps: a bolted-on "which they cannot" (now two
sentences), "Every line I have drawn" (now "The lines I have drawn"),
"always look like a fall" (now "look like a fall"), and "this room" on the
map slide and figure (now "the hosts").

## Restated rather than copied from how-I-llm

Per the rules, these facts appear in plain words rather than that deck's
phrasing: "confident, plausible, wrong" became "Wrong answers look like
right ones. Nothing crashes"; "My job moved from typing to specifying and
checking" became "The job is now specifying and checking, with little
typing"; "Agents did not choose the model..." became "Choosing the
model... stayed with the authors"; "Every boundary I have drawn in two
years has moved" became "The lines I have drawn between the columns have
moved since I drew them".
Two how-I-llm lines are quoted verbatim in quotation marks because the
proposal asks for them and `llmisms.md` lists one as a survivor: "I do
not have a defence for this. I am part of the problem".

## Unsure about

- **The onset vintages figure** (slide 12). The five reads do not stack
  as a reporting triangle should: the 6 September read sits below the
  July and August reads on June onset weeks. That is the digitiser's
  JPEG bias moving between vintages, documented in `data/README.md`, and
  the attribution says so. It is honest, and it illustrates the noise
  the checks see through, but it is not the tidy "later sits above
  earlier" picture. If he wants the raster itself, the SitRep PDFs are
  not in the repo and would need fetching from insp.cd.
- **The iframe** rendering unstyled in a headless browser. See above.
- **Slide 6 wording** "The situation reports are PDFs, in French, most
  days". The README says reports are "up to daily"; "most days" is my
  reading of 115 SitReps between 18 May and 6 September.
- **The PINN one-liner** on slide 16, "fits the network to the data, with
  the equations as a penalty", is the standard definition and not from a
  research note.
- **The PLOS figure downloads** carry no caption text on the image; the
  attribution names figure, panel, paper and licence.
- **"A public dashboard from spring 2020"**: the repo was created 21
  March 2020 and the 2022 post says "since April 2020". "Spring" covers
  both.
- **Timeline heading** "Two and a half centuries of models, then ten
  years of outbreaks" is a contrast with content in both halves, not a
  promise tail, but it is long.

## Not done

- No fragment-reveal interactive on the timeline (spec said pick two;
  the slider and the iframe were picked).
- The bio numbers (start date, million users, 30 agencies) do not
  appear, as the spec forbids.
- No summary slide, as the spec forbids.
- `slides.qmd` and the talk plan were not changed; the five partials keep
  their names.
- Link targets in the attributions were checked with `curl` today. The
  epinowcast seminars index URL returned 404, so the slide 16 attribution
  links the seminar page itself, which returns 200.
- `./scripts/lint.sh` prints awk errors for five `exchange/_partials/*.qmd`
  files that git tracks but that are absent from the working tree. Not
  this deck's files; left alone.
