# Draft report: communication lecture deck

Written 2026-09-11 by the drafting agent for `communication/slides.qmd`.
Nothing is committed.

## What was built

The five partials in `communication/_partials/` now carry the deck laid out
in `proposal.md` section 2, slides 1 to 21, with the steers from
`spec-communication.md`.
The `# Title` dividers were kept and no partial was renamed, so
`slides.qmd` and the talk plan are unchanged.

Slide count: 30 in the rendered deck.
That is the plan slide, five dividers, 22 content slides, one full-bleed
live iframe, and the thank you slide.
The 22 content slides against 27 minutes of section time is about 0.8 a
minute, under the 1.5 of the JuliaCon decks, which suits a lecture with
two single-quote slides and a live page.

### A. Three audiences in 2020 (7 slides including the iframe)

1. Government. GOV.UK screenshot of the 17 September 2020 SPI-M-O consensus
   statement page. Quote: "We don't know whether any of this gave any
   policy maker any useful information that helped them make better
   decisions."
2. What the consensus process did. The GOV.UK "Latest R range for England
   1.0 to 1.2" panel (`uk-rt-dashboard.png`, see the note on that figure
   below). Quote: "If results are presented individually this can get
   lost and it incentivises being first out (and maybe therefore cutting
   corners)."
3. The public. Screenshot of the epiforecasts UK page at the Rt figure,
   estimates frozen 2022-03-26.
4. Live iframe of the same UK page, `background-iframe` with
   `background-interactive`. Slide 3 is its static fallback.
5. What went wrong. Screenshot of `epiforecasts/covid#171`, the Wisconsin
   Rt of 9.1 issue and Seb's reply. Quote: "Because we did not have the
   capacity to manually inspect the data and estimates on a daily basis we
   sometimes published nonsensical estimates."
6. Other scientists. Figures 4 and 2 of Sherratt et al. 2023, eLife.
   Quote: "Your forecast becomes part of another product, the forecast
   ensemble. However, they can be very hard to learn from."
7. Where it mattered. Single quote slide, the "most useful contributions
   were in the UK" line.

### B. Software is communication (4 slides)

8. Defaults are advice. The `epinow()` call from the EpiNow2 vignette as a
   code slide.
9. The limits travel less well than the method. Drawn pipeline schematic.
   Quote: "This can cause issues if the limitations of the method are
   poorly communicated."
10. Community as the channel. Forum screenshot. Quote: "Trying to build a
    community of practice as community >> methods or models alone."
11. Evaluation as communication. The scoringutils pairwise comparison
    figure.

### C. With AI (5 slides)

12. What I use it for. His two briefs for this project as quote blocks,
    from `prompts.qmd`.
13. Making it visible. seabbs-bot GitHub profile screenshot.
14. The steering is the work. JuliaCon prompts page at the steers section.
15. Checking what it wrote. Drawn 114 claims bar.
16. Ten times the throughput. Bot pull requests per month, rebuilt.

### D. Under AI (4 slides)

17. Prose that sounds the same. Three before and after pairs from
    `llmisms.md` as fragments, before in grey and after in teal. One line
    hands detection and citation bias to Algaba.
18. Provenance. The BVD README disclosure line as the quote, `git log`
    author counts as the code block.
19. Confident, plausible, wrong. Drawn digitiser schematic, SitReps 081 and
    087.
20. Who gets to do this. Single quote slide plus two lines.

### E. What I would like us to agree on (2 slides)

21. Four things. Four asks with a 2 by 2 grid of the artefacts already
    shown.
22. For the panel. "When the writer and the reader both have a language
    model, what is the person for?" in the `.send-help` style.

## Interactives

- The live UK dashboard as a full-bleed background iframe after the static
  public slide. In headless Chromium it took about 20 seconds to load, so
  give it a moment or skip it if the room has no network.
- Fragment reveals on the three before and after pairs.

## Numbers and their sources

| Number | Slide | Source |
|---|---|---|
| Weekly Rt, forecasts, ad hoc reports to SPI-M-O and SAGE | 1 | `research-communication.md` s1, grant bio `sam.qmd:89` |
| April 2020 to 31 March 2022 | 3 | rt-reflections 2022, line 31 |
| several thousand locations | 3 | rt-reflections, line 4 |
| just over 500,000 unique users, 1.2 million page views | 3 | rt-reflections, line 46 |
| 20,000 page views for methods | 3, 9 | rt-reflections, line 46 |
| Wisconsin, first Sunday report, 17 October 2021 | 5 | epiforecasts/covid#171, sbfnk reply |
| US, European, German and Polish hubs | 6 | surrogate-ensemble-forecast 2022, line 40 |
| EpiNow2 on CRAN since 1 September 2020 | 8 | CRAN archive, 1.1.0 dated 2020-09-01, fetched 2026-09-11 |
| CDC used EpiNow2 for nowcasts and Rt | 8 | CDC CFA page updated 2026-01-30; MMWR 2024-11-21 |
| over 50 researchers and practitioners | 10 | composable workflow grant `abbott.md:127` |
| 31 seminars May 2023 to May 2026 | 10 | `epinowcast.github.io/seminars/` count |
| "too complex for anyone else to use" | 10 | JuliaCon roadmap `04-r.qmd:22-25` |
| UKHSA asked for evaluation guidance | 11 | `bmbr-guidance-grant/CLAUDE.md:21-30` |
| seabbs-bot created 2026-01-23 | 13 | `gh api users/seabbs-bot` in `research-agentic.md` s5 |
| 130 steers by 14 August 2026 | 14 | recount of `JuliaCon2026/notes/steers.md`, 130 blank-line-separated blocks starting with `>`; last commit `755f1f1` 2026-08-14 |
| fifty-three mid-build | 14 | `JuliaCon2026/prompts.qmd:172` |
| 114 claims, 67 changed | 15 | how-I-llm commit `8c7e834` |
| 530 became 353 | 15 | how-I-llm commit `1fceb9a` |
| 712 of 1,371 merged bot PRs no review | 15 | how-I-llm commit `8c7e834` |
| Jan 17, Feb 92, Mar 78, Apr 61, May 124, Jun 531, Jul 744, Aug 399, Sep 98 | 16 | GitHub search API per month, `research-agentic.md` s5 |
| 2,144 total, 85.5% merged, 11.9% closed unmerged | 16 | same |
| about half of closed unmerged superseded | 16 | how-I-llm `05-scale.qmd:9-12` via commit `8c7e834` |
| at least 13.5% of 2024 PubMed abstracts | 17 | Kobak et al. 2025, Science Advances |
| 497 commits; 238, 144, 50, 40, 11, 7, 3, 3, 1 by author | 18 | local `git log` 2026-09-11, `research-agentic.md` s5 |
| 333 of 425 pull requests | 18 | GitHub search API, `research-agentic.md` s5 |
| four named authors | 18 | BVDOutbreakSize README line 3 |
| SitRep 081: about 10 of 19 ticks, 1,411 vs 3,066, 54% low | 19 | BVDOutbreakSize `data/README.md:75` |
| SitRep 087: grid 20 to 25, caught by reporting triangle | 19 | `data/README.md:77` |
| £200 a month | 20 | how-I-llm `06-money.qmd:3-7` |

## Figures

Copied, with source path in the attribution:

- `figures/comms-uk-rt-dashboard.png` from
  `hpru-ppie-kickoff/figures/uk-rt-dashboard.png`.
- `figures/comms-hub-ensemble-good.png` and
  `comms-hub-ensemble-less-good.png` from `hpru-ppie-kickoff/figures/`.
  These are Figures 4 and 2 of Sherratt et al. 2023, eLife 12:e81916,
  identified from the embedded captions.
- `figures/comms-pairwise-illustration.png` from
  `epiforecasts/scoringutils/man/figures/pairwise-illustration.png`.

Drawn by `scripts/comms-figures.py` (`uv run --with matplotlib`), site
palette:

- `comms-bot-prs-by-month.png`, September counts, September bar greyed and
  marked "to 11th".
- `comms-pipeline.png`, model to estimates to other papers with the
  limitations arrow fading.
- `comms-digitiser.png`, the same bars on a 20-step and a 25-step axis.
- `comms-claims.png`, 114 claims, 67 changed.
- `comms-consensus.png`, six illustrative intervals and one consensus
  band. Drawn for slide 2 and then replaced by the real GOV.UK panel. Left
  on disk as an alternative; delete if not wanted.

Screenshots by `scripts/comms-shots.py` (playwright, needs the sandbox
off to launch Chromium), all taken 2026-09-11:

- `comms-shot-spimo-statement.png`, GOV.UK, cookie banner dismissed.
- `comms-shot-covid-issue-171.png`, GitHub issue.
- `comms-shot-covid-uk.png`, epiforecasts UK page scrolled to the Rt
  figure.
- `comms-shot-epinowcast-forum.png`.
- `comms-shot-seabbs-bot.png`.
- `comms-shot-juliacon-prompts.png` and `comms-shot-juliacon-steers.png`.

## Checks run

- `quarto render communication/slides.qmd` succeeds with the sandbox off.
- `./scripts/lint.sh` is clean. It prints awk errors for exchange partials
  that another agent had not yet created at the time; not mine.
- All 18 `llmisms.md` greps run over `communication/_partials`. Remaining
  hits are quoted source (the point-stamp "before" example, his brief), a
  factual list of hubs, the ask "a named person behind every number", the
  sourced "for the first time" from the GitHub reply, and his own line
  "Agents make that worse".
- Every attribution URL returned 200 on 2026-09-11.
- Every slide screenshotted at 1920 by 1080 and checked by eye.

## What I was unsure about

- `uk-rt-dashboard.png` is not the epiforecasts dashboard. It is the
  GOV.UK "Latest R and growth rate for England" panel. The spec named it
  for the public slide; I moved it to the consensus slide, where it shows
  the published range with no point estimate, and screenshotted the real
  epiforecasts UK page for the public slide. Check you are happy with the
  swap.
- The consensus slide bullets ("each group sent its own estimate", "one
  range went out") describe the SPI-M-O process from memory of how it
  worked, not from a written source. The quote beneath is sourced.
- "Ten times the output needs ten times the reading" restates the
  how-I-llm line "Ten times the throughput at ten times the review load is
  not a win" in plain words, as the rules ask. Say if you want the
  original.
- "I wrote the argument and almost none of the words" is how-I-llm
  phrasing, so slide 12 says "I wrote the brief and the corrections. An
  agent wrote the words and drew the figures" instead.
- The "who gets to do this" quote and the £200 line are from how-I-llm,
  which is bot phrasing. `llmisms.md` lists the first as an admission that
  survives every pass, and the proposal names it for this slide, so it is
  quoted as written.
- The "community too complex for anyone else to use" verdict is quoted
  from the JuliaCon roadmap deck, which is post-correction and so his.
- CDC's Rt page no longer mentions EpiNow2 and a search snippet reports a
  switch to a hierarchical GAM after 1 June 2026. Not on the slide; the
  attribution dates the CFA page and the MMWR.
- The UKHSA evaluation request is sourced only to a project `CLAUDE.md`.
  The attribution says "project notes". Drop the bullet if that is too
  thin.
- The Kobak et al. figure is attribution only, as the proposal asked, and
  Algaba is handed detection in one line.
- Slide 6 says "The ensemble beat most single models in most countries",
  read off Figure 4, and "It also missed the turns the teams missed", read
  off Figure 2. Both are readings of the figures rather than lines from
  the paper.

## What I could not do

- Nothing in the spec was left out. Ottawa and the Philippines are not
  mentioned, as instructed.
- The iframe slide renders blank for the first 20 seconds or so in
  headless Chromium and I could not test it on a projector. The static
  slide before it is the fallback.
