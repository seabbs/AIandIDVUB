# Keynote, round two report

Written 12 September 2026 against `spec-keynote-r2.md`. Rendered, all 38 slides screenshotted at 1920 by 1080 with `scripts/keynote-shots.py` (none over 1080 px; tallest is "the data" at 1036), `./scripts/lint.sh` clean, every `llmisms.md` grep run. Nothing committed.

## Running order

Title, talk plan (three bullets as specified), thank you: free. Three dividers: free. One hidden fallback, under "Refit on every push". 32 content slides.

1. Ten years of outbreak modelling (divider), 16 content. Two and a half centuries; My ten years; Ebola, West Africa (CDC's 1.4 million and the Sierra Leone forecasts, merged); Delays from the WHO Ebola Response Team; Early Wuhan estimates; Real-time $R_t$ for thousands of locations; What could not be done in time; The tools that came out of it, 2020 to 2026; mpox 2022, heavy-tailed networks (with the "COVID models could not be reused" bullet); Nowcasting for UKHSA; Ebola disease caused by Bundibugyo virus, DRC, 2026; McCabe et al. and a replication; Refit on every push (live iframe, hidden fallback); How an outbreak gets modelled; What keeps going wrong.
2. Use of AI in past, present and future outbreak modelling (divider), 8 content. His view alone; the Kraemer map with the added row; UDEs; Renewal as a neural network layer; AI-driven inference; Foundation time series models; Reinforcement learning for control; "I am very excited about their potential" alone.
3. Agentic AI and outbreak modelling (divider), 8 content. What I mean by an agent; How I work now; the data; the model; What agents made possible; Digitising from figures, and what went wrong; Agents that search over models; Google SAI in the CDC hubs; Who gets to do this.

## Cut to reach budget

Spec listed 35. Cut slide 21 (PINNs) outright; Kharazmi, Millevoi and Rama are not in the deck. Merged 3 and 4 into one Ebola slide on the Funk 2019 figure, as the spec allowed. Folded slide 11 into slide 10, since the 40 minute deck already makes the "could not be reused" point on the Endo figure. Result 32, of which two are single-sentence quotes. The renewal slider and its fallback went with the spec. Also cut: "What does not change", "Where does AI fit", "For the panel", the community slide.

## Verified BVD facts, with sources

- 333 of 425 pull requests from `seabbs-bot`; 145 releases, `results-43` (20 May) to `results-1699` (9 September): GitHub API, 11 September, `research-agentic.md` section 5.
- Every stream except confirmed cases and deaths read from the PDFs; those two cross-checked against the INRB-UMIE mirror; script exits on undocumented disagreement: `README.md:117-120`, `data/README.md:22-23`.
- Two blind readers per recent vintage: `data/README.md` notes for SitReps 097 to 115.
- Digitiser from pixel colour and tick geometry; Julia script with a byte-identical Python port, parity test added (#629 in `docs/src/news.md`), divergence found and flagged (issue #594, `data/README.md:85`).
- SitRep 081 (10 of 19 ticks, minus 54%), 087 (grid 20 to 25, caught by the reporting-triangle invariant), 098 (lossless image, about 7% high, excluded): `data/README.md:75-83`, issue #594.
- Onset reporting triangle fitted as a nowcast: commit `e2328e76`, 27 July 2026.
- Performance: 19 commits with "perf" in the subject, 17 by "Sam Abbott (bot)", 1 `seabbs-bot`, 1 "Sebastian Funk - robot edition"; issue #444 (bot) records a null result from a micro-optimisation review; PR #656 (`sbfnk-bot`, merged 8 September) removed boxed closures, "roughly halves the gradient", log density bit-identical.
- "Two versions kept in sync": the exports-only and deaths-only composers reproduce McCabe Methods 1 and 2 from the same building-block submodels as `bvd_joint`; the analysis page's "Imperial report sense check" compares them with all three published McCabe versions on every build (`docs/src/analysis.md` sections "Top-level composers" and "Imperial report sense check"; `README.md:166-168`). Stated as "share submodels" and "every release refits the analogues". Nothing in the repo describes two separate model codebases.
- Streams that stopped: daily new suspects 6 August, treatment-centre table 3 August (`README.md:15-19`).
- "Agents proposed patches as issues": open `patch model` issues #666, #668, #669 by `seabbs-bot`, 11 September. Forecast scoring in `src/scoring.jl` and `scripts/score_releases.jl`.

## Charlotte Holt

`gh api users/charlotteholt`: account created 19 September 2019, no name, no bio, no public repositories, not a public member of epiforecasts, zero commits or issues in the org by that login. Unverifiable, so named only, no photo.

## Figures

Drawn (`scripts/keynote-timeline.py`, `scripts/keynote-schematics.py`, no refs beneath them): timeline-centuries, timeline-ten-years, packages, ebola-delays (means and CFR from the NEJM abstract), workflow, workflow-agents, map, seir-vs-ude, renewal-layer, foundation, rl-loop, agent-1, agent-2, agent-3. `keynote-shots.py` is new; `keynote-counts.py` lost the authorship figure.

Downloaded, all CC BY or public: Abbott 2020 WOR figure 2 (CC BY, via PMC); OutbreakFlow figure 1 (PLOS, CC BY); Funk 2019 and Overton 2023 panels kept (PLOS, CC BY); SitRep 087 page 1, page 3 and its embedded onset raster from insp.cd (a government situation report, cited); arXiv abstract page screenshot for Martinson et al.; BVD per-stream fit panel from release `results-1699` (`site.zip`). Meltzer's MMWR figure 1 was downloaded (US government work) but is unused after the merge; not kept.

Reused from his decks: Endo 2022 figure (Science, licence not CC; it is the file from his JuliaCon composable deck), ONS cascade (Abbott and Funk 2022), June per-stream size figure from the collaboratory talk, bot avatars, bot PRs chart.

Not used: Hellewell 2020 (CC BY-NC-ND), Pinotti 2025 and Kharazmi (licence unknown), Bolshov PRISMA (dull), WHO ERT NEJM figures (redrawn as estimands).

## For Sam

- 32 content slides for 25 minutes is over 30. Easiest further cuts: RL, or merge "the outbreak" into "McCabe".
- The Endo figure is a Science figure; say if you want it described instead.
- Slide 11 "UKHSA could not install other methods" is your account, marked "as I recall it".
- Renewal-as-a-layer: neither grant uses that phrase. The attribution cites the ML composability design row and the EU note's UDEs-in-components line.
- WHO ERT slide draws only means; the abstract gives no spreads.
- Live iframe still needs network; open the summary page once before the talk.
- Old figures deleted: chain, loop, sai-loop, who, renewal, agent, sbi, ude, timeline, authorship, truncation, June sitrep, infections and Rt September panels.
