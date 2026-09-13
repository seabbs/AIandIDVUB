# Keynote partial 3, acting on his TODOs

13 September 2026, against commit `02ca043`. Rendered with zero fenced-div warnings (all six came from the TODO line glued to the `::::` on the digitising slide). All 12 section slides screenshotted at 1920 by 1080, none over 1080 (tallest the data slide at 1036, unchanged). `./scripts/lint.sh` clean. Every `llmisms.md` grep run; remaining hits are attribution lines, alt text and verified counts. Nothing committed.

## TODOs and half-written lines

- **What I mean by an agent.** Kept his single line only. Both deleted bullets stay deleted.
- **How I am working.** Kept his bullets. Sebastian Funk line made grammatical; evidence added to the attribution, `sbfnk-bot` pull request #656 in BVDOutbreakSize merged 8 September 2026 (`gh pr view`). His cut of the JuliaCon layout credit kept.
- **Agents building methods into software (new slide).** Two approaches from epiaware.org/approaches, screenshotted by `scripts/keynote-epiaware-shot.py` into `figures/keynote-epiaware-approaches.png`. The modelling-language question left as a question. epidist meta model: pull request #620, opened 26 August, merged 4 September 2026, so "about a week". EpiDelays: Oswaldo Gressani's UHasselt package, 36 `seabbs-bot` commits on 13 and 14 April 2026 wiring `primarycensored` in as the likelihood (`git log` of the fork; upstream pull request #3 still open, so "open" in the attribution). primarycensored generalised gamma: pull request #334 by `seabbs-bot`, merged 10 September 2026; gamma, lognormal and Weibull by Samuel Brand in 2024 (`NEWS.md`).
- **The data.** "model model" typo fixed. INSP in full. His bullets kept, merged to five. Julia reference digitiser and byte-identical Python port from `scripts/README.md`; two blind readers from `data/README.md`.
- **The model.** Two versions in tandem verified: pull request #155 replaced the integral model with the renewal model, opened 31 May, 100 commits, merged 9 June 2026, while `main` kept moving (perf commits #145, #152). Added to the attribution. His deletion of "log density bit-identical" kept.
- **What agents made possible.** Two workflow refs added: Gelman et al. 2020 arXiv:2011.01808 and the Abbott et al. workflow page. "In a few hours" from the JuliaCon outbreak slide and the repo created 19 May with `results-43` on 20 May. His nine bullets cut to five to fit; "5+" became "the sitrep streams" since README lists nine.
- **What else went wrong (new slide, his TODO).** Forecasts: five defects in v1.15.0 `news.md`, four-week $R_t$ 0.245 to 14.9, his issue #606. Autodiff: Enzyme issue #445 open since 20 July; boxed closures halved the Mooncake gradient 21 to 10 ms, pull request #656 and v1.18.0 news. Observation models: his issues #299 (bed capacity as a rise-only walk) and #297 (one length of stay for died and discharged). Drawn as `figures/keynote-agent-wrong.png` by `scripts/keynote-agent-figures.py`.
- **Digitising.** TODO line removed; nothing else changed.
- **Search over models.** His bullets kept, tidied. His deleted "the score is the thing that can be gamed" also removed from the tree figure (`keynote-schematics.py`, `agent_3` redrawn only).
- **Google SAI.** Leaderboard checked in the paper, page 4: first of 43 eligible FluSight, 12 COVIDHub and 4 RSVHub submissions; Bracher and Funk say the same. His "mutates and composes" bullet: prompts came in three families, adaptations of hub models, recombinations of pairs, and unconstrained searches, so stated as "most candidates adapt or recombine models already in the hubs". 207,500 candidates from 142 prompts, page 2. His compute line flagged as his guess. LLM and RSV in full; CDC was spelled out in partial 1.
- **Who gets to do this.** Quote in quotation marks with "Sam Abbott, how I LLM, July 2026" beneath, as on his "My view" slide. His deletion of "I am part of the problem" kept. VC spelled out.

## For Sam

- INRB-UMIE is not expanded; I could not verify what UMIE stands for.
- The EpiDelays pull request to Gressani's repo has been open since April. Worth a word before naming a UHasselt colleague on stage.
- The Google SAI slide is at 1045 px, the tightest in the section.
