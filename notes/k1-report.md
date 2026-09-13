# Keynote partial 1, his TODOs of 13 September

File: `keynote/_partials/01-ten-years.qmd`. Not committed.

## What I did, TODO by TODO

- **"Found that they were...."** Completed from Funk et al. 2019, PLOS Comput Biol (doi:10.1371/journal.pcbi.1006785). The abstract: good calibration one and two weeks ahead, increasingly unreliable further out; the results give 12 percent overestimation at one week rising to 44 percent at five. Bullet now says calibrated at one and two weeks, overestimating from three weeks with the bias growing with horizon.
- **Park et al. 2024 reference.** Park, Akhmetzhanov, Charniga, ... Abbott, "Estimating epidemiological delay distributions for infectious diseases", medRxiv, doi:10.1101/2024.01.12.24301247. In the attribution. The related PLOS Comput Biol paper (Charniga et al. 2024, doi:10.1371/journal.pcbi.1012520) has Park as second author, so the medRxiv one is his "Sang Woo Park et al.".
- **20,000 by 2 November.** A model forecast. NEJM sentence: "Assuming no change in the control measures for this epidemic, by November 2, 2014, the cumulative reported numbers of confirmed and probable cases are predicted to be ... exceeding 20,000 in total." Now labelled "Their forecast" with the condition. Set against what happened: 14,383 cases reported by 11 November, from CDC MMWR 63(46), 1130 (mm6346a6). The WHO situation report of 5 November was behind a 403, so I used the CDC figure and date.
- **Tools split.** One slide is now two: "The tools that came out of the pandemic, 2020 to 2021" (scoringutils, EpiNow and the dashboard, EpiNow2, European Forecast Hub, epinowcast) after the variants slide, and "The tools since, 2022 to 2026" (epidist, EpiAware.jl, primarycensored, baselinenowcast, BVDOutbreakSize) after the UKHSA nowcasting slide. `scripts/keynote-timeline.py` now writes `keynote-packages-pandemic.png` and `keynote-packages-since.png`; `keynote-packages.png` deleted. One content slide added to the count.
- **mpox.** Five bullets. PHEIC spelt in full, "WHO's highest alert" dropped, the case count its own bullet. Endo et al. bullet now states what the paper found (heavy-tailed partnership distribution explains sustained growth among men who have sex with men, from the Science abstract). A "Why it turned over" bullet gives his account: depletion of the high-activity core, counter-argument behaviour change, both sides agreed on heavy-tailed networks. Murayama, Pearson, Abbott et al. 2024, J Infect Dis (doi:10.1093/infdis/jiad254) added to the attribution as the depletion paper. Reuse bullet as he wrote it, fixed from a broken sub-bullet to a bullet.
- **UKHSA title.** "Nowcasting for the UK Health Security Agency"; the bullet gloss shortened to "for UKHSA".
- **Headings.** His four kept. "Ebola, West Africa" without the full stop and with a blank line after it.
- **Patterns propagated.** Bold lead words on the Ebola, delays, Wuhan, variants, mpox and UKHSA bullets. His quote line kept as written. Spelt out on first use: US Centers for Disease Control and Prevention, Office for National Statistics, Democratic Republic of the Congo. His "Software widely used ..." line kept, double space and full stop removed.

## Checks

- `quarto render keynote/slides.qmd` runs (sandbox off). This partial rendered alone gives zero fenced-div warnings and its fences balance (43 `:::`, 13 `::::`). The six warnings in the full render come from `02-ai-methods.qmd` or `03-agents.qmd`, not touched.
- Screenshots at 1920x1080 in `_shots/keynote/06.png` to `15.png`. No slide in this section overflows; mpox is the tallest at 1031 px. Slides 25, 28, 29, 37, 38 and 40 in the other partials overflow.
- `./scripts/lint.sh` reports nothing in this partial. Its failures are all in the other two partials.
- llmisms greps: the rule-of-three grep hits are author lists and data streams; the colon hit is his quote line. Nothing changed.

## Follow-up

- The case fatality box in `keynote-ebola-delays.png` clipped its text. Widened the box and moved the percentage to the second line in `scripts/keynote-schematics.py`, regenerated that figure only, re-rendered and checked slide 7 at 1920x1080.
