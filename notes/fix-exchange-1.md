# Fix 1: research exchange deck

Applied `review-exchange-1.md` and the two 12 September steers (no theme, so introduce the group; mine past decks first) to `exchange/`.
Nothing is committed.
`quarto render` of `slides.qmd` and `index.qmd` succeeds outside the sandbox, `./scripts/lint.sh` is clean for `exchange/`, and every slide was screenshotted at 1920 by 1080 with a playwright script; none overflows the canvas.

## Findings, in the review's order

1. Equations stacked as two displays on "Both events are recorded to the day".
2. `ComposableTuringIDModels.jl` code is the page's `renewal_model.jl` with `NUTS(0.95)` and `100, 2`, comments as on the page. The attribution lists every change: `Mooncake` dropped from the `using` line, the `using ADTypes` line, the `adtype` argument and "(Mooncake AD)" dropped, `sample` call reflowed to two lines. `ComposedDistributions.jl` matches the page with only the three inspection calls and their comment dropped, checked against both pages today. `exchange/exchange.css` lifts the code block height cap.
3. "Two blind reads per vintage of the onset chart", with "SitReps 104 to 114" in the attribution, which is what `data/README.md:99-111` documents.
4. and 5. "In my view neither of the first two is close" and the PDF line list claim cut; the slide says agents read the situation reports.
6. Deck at 22 minutes on the new budget, table below.
7. Network slide ends "Reinforcement learning and bandits on individual-based simulators. Could a composable component be the environment?" Agents slide ends "Could agents build and check the simulators you learn against?" Questions only.
8. Network slide is four bullets: UDEs and PINNs together, one Philipps caveat, "No neural network code in any EpiAware package. Maybe nothing doing there at the moment" verbatim, the room question. Millevoi et al. 2024 in the attribution as the PINN source.
9. Agents slide rewritten as five two-line bullets in a 56 per cent column. The refit cadence, the 18 May date and "145 releases" left the bullets; the date is in the attribution.
10. and 11. The canonical censoring bullets restored as four bullets, the `epidist` line is two sentences, "Adding a new application means defining only the novel parts" restored.
12. `scripts/exchange-workflow-split.py` redrawn as a vertical column with 13pt labels, about 20px on screen; figure regenerated from the script today. Bullets 1 and 2 cut to one line.
13. Who slide: timeline at 55 per cent. EpiNow2: left column 48 per cent, results figure 520px.
14. Attributions carry sources only. The slider setup ("Continuous `LogNormal(1.6, 0.6)` delays, every primary event at day zero") is a bullet; its attribution points at the JuliaCon delays talk.
15. "Less clear where AI plugs in here" slide cut. One line on "Three packages, one likelihood": "Less clear where AI plugs in here. A learned delay distribution? Amortised inference trained on your simulators?"
16. "Two approaches" slide cut. Photos sit under the bullets on the two code slides.
17. `# Unfortunately, biases` divider restored. The double-integral line is back as the canonical callout-note.
18. `index.qmd`: "five talks and two introductions". Description now opens with the group.
19. Counts corrected below.

## Steer 1: three group slides

- **Who I am.** LSHTM and CMMID spelled out, $R_t$ and nowcasting glossed, evaluation. Photo and the keynote timeline strip. The tools bullet moved to the table on slide three.
- **epiforecasts.** Led by Sebastian Funk, I am part of it, the cross-over is real-time modelling and evaluating it (his steer, restated). `EpiNow2`, `scoringutils`, `epinowcast`, the European COVID-19 Forecast Hub (repository created 13 January 2021, `research-history.md`) and RespiCast. SPI-M-O glossed; source `sam.qmd:89` via `research-history.md`.
- **epinowcast, the community.** The package table and his two lines lifted whole from the JuliaCon roadmap; forum with over 50 members (`research-communication.md` section 3); monthly seminar since May 2023, 31 entries; "Community >> methods or models alone" (IISA post, 2023).
- Surnames verified: `seminars.qmd` names Sam Abbott, Fanny Bergström and Clara Brigitta as the people to contact about organising, in commit `20be2ff` (24 June 2026) on branch `add-2026-06-03-bvd-outbreak` of `epinowcast.github.io`. `main` still names Kelly Charniga, so the page is stale rather than contradicting him.

## Steer 2: lifted from his past decks

| Slide | Source deck and file |
|---|---|
| epiforecasts, figure | HPRU PPIE kick-off (Funk, Abbott, Cori, September 2025), `slides.qmd:52-56`, `figures/respicast-multi.png` copied as `exchange-respicast-multi.png` |
| epinowcast, table and two bullets | JuliaCon 2026 roadmap, `_partials/04-r.qmd:5-25`, "Six years of trying this in R and Stan" |
| Whitty, ONS, "What is composable modelling?", the two code slides, EpiNow2 | JuliaCon 2026 composable `00-gap`, `01-options`, `01b-composable`, `04-case-study`; epiaware.org approaches pages (already lifted in the draft) |
| Delay definition, censoring, truncation, fallback, Julia model | JuliaCon 2026 delays `00-delay`, `01-biases`, `05-julia` (already lifted) |
| Workflow schematic | JuliaCon 2026 roadmap `04-r.qmd:29-39` (already lifted) |

## Slides cut

- "Analysing all data and processes together" (Lison) merged into the ONS slide.
- "Two approaches, and they interoperate" (finding 16).
- "Less clear where AI plugs in here" (finding 15).
- "What we want from any approach", to pay for the two new group slides.

## Final count

25 counted slides plus one uncounted static fallback, 26 sections.
Title, plan, three group slides, five dividers, 14 content slides, the fallback, thank you.

| Section | Content slides | Minutes |
|---|---|---|
| Who I am and the groups | 3 | 4 |
| Composable, with the two AI slides | 6 + 2 | 10 |
| Delays | 4, plus the uncounted fallback | 5 |
| Workflow and AI | 2 | 3 |
| Total | 17 | 22 |

## Left for Sam

- The room questions on the network and agents slides are the drafter's framing; check the wording lands. "Amortised inference trained on your simulators?" may overreach.
- "Led by Sebastian Funk. I am part of it" and the cross-over line restate his steer; no public page says who leads epiforecasts.
- The organiser surnames come from an unmerged branch of the epinowcast site. Merge it or drop the surnames.
- The design considerations slide is gone; the Interoperability bullet naming machine learning went with it.
