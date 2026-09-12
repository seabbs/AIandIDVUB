# Fix 1: research exchange deck

Applied `review-exchange-1.md` to `exchange/` on 12 September 2026, in two passes.
Nothing is committed.
`quarto render` of `slides.qmd` and `index.qmd` succeeds outside the sandbox, `./scripts/lint.sh` is clean, and every slide was screenshotted at 1920 by 1080 with a playwright script; none overflows the canvas (tallest is the workflow schematic at 1080, next the EpiNow2 slide at 1070).

## Findings, in the review's order

1. Equations stacked as two displays on "Both events are recorded to the day". Slide is 1044 tall.
2. `ComposableTuringIDModels.jl` code is the page's `renewal_model.jl` with `NUTS(0.95)` and `100, 2`, comments as on the page. The attribution lists every change: `Mooncake` dropped from the `using` line, the `using ADTypes` line, the `adtype` argument and "(Mooncake AD)" dropped, `sample` call reflowed from three lines to two. `ComposedDistributions.jl` matches the page with only the three inspection calls and their comment dropped, checked against the page today. `exchange/exchange.css` lifts the code block height cap so all 20 lines show.
3. "Two blind reads per vintage of the onset chart", with "SitReps 104 to 114" in the attribution, which is what `data/README.md:99-111` documents.
4. "In my view neither of the first two is close" cut with its slide (15).
5. The PDF line list claim cut. The slide now says agents read the situation reports.
6. Deck at 22 minutes, table below.
7. Network slide ends "Reinforcement learning and bandits on individual-based simulators. Could a composable component be the environment?" Agents slide ends "Could agents build and check the simulators you learn against?" Questions only. Source: `research-workshop.md` sections 2 and 5.
8. Network slide is four bullets: UDEs and PINNs named together, one Philipps caveat (`consistently hindered parameter identifiability`), "No neural network code in any EpiAware package. Maybe nothing doing there at the moment" verbatim, the room question. Millevoi et al. 2024 in the attribution as the PINN source. 920 tall.
9. Agents slide rewritten as five two-line bullets in a 56 per cent column. "Refit on every push since", the 18 May date and "145 releases" left the bullets; the date and repository creation day are in the attribution.
10. The two canonical secondary-censoring bullets restored, and the primary bullet split back into its two canonical bullets. The `epidist` line is two sentences.
11. "Adding a new application means defining only the novel parts" restored.
12. `scripts/exchange-workflow-split.py` redrawn as a vertical column of nine stages with 13pt labels on a 10 inch canvas, about 20px on screen; figure regenerated from the script today. Bullets 1 and 2 cut to one line pointing at it.
13. Who slide: timeline at 55 per cent, 1050 tall. EpiNow2: left column 48 per cent, results figure 520px, 1070 tall.
14. Attributions carry sources only. The slider's setup ("Continuous `LogNormal(1.6, 0.6)` delays, every primary event at day zero") is now a bullet and its attribution points at the JuliaCon delays talk. "Static fallback", "from the keynote the day before" and "my reading of" are gone.
15. "Less clear where AI plugs in here" slide cut. One line on "Three packages, one likelihood": "Less clear where AI plugs in here. A learned delay distribution? Amortised inference trained on your simulators?" Jang and Radev citations went with the slide.
16. "Two approaches" slide cut. Photos sit under the bullets on the two code slides, as in the JuliaCon decks.
17. `# Unfortunately, biases` divider restored before "Both events are recorded to the day". The double-integral line is back as the canonical callout-note under that slide.
18. `index.qmd`: "five talks and two introductions".
19. Counts corrected below.

Beyond the review: the merged ONS and Lison slide is four bullets, "Uncertainty from earlier estimates approximated at each step" cut as the one that overlapped the Lison bullet.

## Slides cut to reach 22 minutes

- "Analysing all data and processes together" (Lison) merged into the ONS slide as "Analysing data and processes separately, or all together".
- "Two approaches, and they interoperate" (finding 16).
- "Less clear where AI plugs in here" (finding 15).

## Final count

24 counted slides plus one uncounted static fallback, 25 sections.
Title, plan, who, five dividers, 15 content slides, the fallback, thank you.

| Section | Content slides | Minutes |
|---|---|---|
| Composable | 7 | 9 |
| Where AI might plug in | 2 | 3 |
| Delays | 4, plus the uncounted fallback | 6 |
| Workflow | 2 | 4 |
| Total | 15 | 22 |

Plan and who take about one minute on top, so 23 spoken minutes in a 20 to 25 minute slot.

## llmisms greps

Remaining hits are canonical wording ("timely, rigorous, and collaborative", "Current approaches struggle", the ONS colon, "which is typically more complicated to evaluate", "so it reads like `dgamma`"), alt text, citations, the slider setup line, and `## Talk plan`, which the spec keeps.

## Left for Sam

- The room questions on the network and agents slides are the drafter's framing of the hook the spec asked for; check the wording lands.
- "Amortised inference trained on your simulators?" ties their individual-based models to simulation-based inference. Cut if it overreaches.
- Bullets on the ONS, network and delay slides run to three lines at their column widths; the wording is canonical, so I trimmed by whole bullets only.
- `exchange/exchange.css` is new and lifts the code block height cap for this deck only.
