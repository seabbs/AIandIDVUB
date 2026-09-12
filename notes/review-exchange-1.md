# Review 1: research exchange deck

Cross-review of `exchange/` against `spec-exchange.md`, 12 September 2026.
Read-only pass; nothing in the deck was changed.
Render succeeds outside the sandbox, `./scripts/lint.sh` is clean, and every slide was screenshotted at 1920 by 1080.
Most important first.

## Findings

**1. `exchange/_partials/04-delays.qmd:47-52`.**
The two-equation display is wider than the slide and the second equation is cut off at the right edge.
Measured slide width 2242 against a 1920 canvas; the render ends at "Pr(T ∈ [n, n + w" with the right-hand side missing.
Fix: stack the two equations on separate lines, or drop the second and keep the JuliaCon single-equation layout.

**2. `exchange/_partials/02-composable.qmd:185-186`.**
The code slide changes the source's sampler arguments and the attribution says only autodiff arguments and blank lines were dropped.
The approaches page has `NUTS(0.95; adtype = AutoMooncake(...)), MCMCThreads(), 100, 2`; the slide has `NUTS(), MCMCThreads(), 1000, 4`, and both comments were rewritten.
Fix: restore `100, 2` and the page's comments, or say "sampler arguments changed" in the attribution.

**3. `exchange/_partials/03-ai.qmd:50-51`.**
"Agents read them, two blind readers each" overstates what the source documents.
`BVDOutbreakSize/data/README.md:99-111` records two blind readers per vintage for the onset-figure axis reads of SitReps 104 to 114, not for every stream in every PDF.
Fix: "the onset figure is read by two blind readers per vintage".

**4. `exchange/_partials/04-delays.qmd:215`.**
"In my view neither of the first two is close" puts an opinion in his mouth that no source records.
His steer says only "less clear AI cross links"; the first-person opinion is the drafter's.
Fix: cut the sentence and keep "Tell me if you disagree", or leave the verdict for him to say aloud.

**5. `exchange/_partials/04-delays.qmd:214`.**
"Reading the line list out of a PDF is where agents already help" has no source.
BVDOutbreakSize reads aggregate situation reports from PDFs (`research-agentic.md:109-112`); the only line list, Isiro 2012, came from Rosello et al., not a PDF read by agents.
Fix: "Reading the situation report out of a PDF".

**6. `notes/draft-exchange-report.md:19-25` and `exchange/slides.qmd:20-30`.**
The drafter's own minute table sums to 25, not the 22 the spec set, and "workflow and AI 4" has become 6.
Table: who 1, composable 12, AI 3, delays 6, workflow 3.
Fix: take one minute each from the AI and workflow sections, or cut one slide, and restate the total.

**7. `exchange/_partials/03-ai.qmd` and `04-delays.qmd:207-222`, the room.**
No slide names reinforcement learning, bandits or the individual-based simulators the VUB group runs, so the questions are generic rather than to this room.
`research-workshop.md:139-145` ranks those as the hosts' working definition of AI; the amortised-inference bullet is the natural place to say "your simulators" and does not.
Fix: tie one question on each AI slide to their methods in one clause, without explaining the methods.

**8. `exchange/_partials/03-ai.qmd:7-16`.**
Five bullets, the slide overflows (1092 against 1080), and PINNs are missing although the steer and spec name them alongside UDEs.
`research-ai-methods.md` B3 has the Millevoi et al. caveats ready: deterministic, no uncertainty, poor outside the training window.
Fix: merge bullets 1 and 2, and spend the saved line on PINNs.

**9. `exchange/_partials/03-ai.qmd:47-54`.**
Bullets 1 and 2 run to four lines each on screen, against the two-line limit in `drafting-rules.md`.
Bullet 1 carries the disease, the country, the replication, the refit cadence and the release count in one breath.
Fix: split into two bullets each, or move the counts to the attribution.

**10. `exchange/_partials/04-delays.qmd:36` and `:193-194`.**
Two canonical lines were joined with ", so", the bolted-on clause he cuts most often.
JuliaCon `01-biases.qmd:44-46` has "The secondary event is recorded to the day as well" and "The probability of a daily bin is a difference of the primary-censored CDF" as separate bullets; `04-sharing.qmd:71-73` never says brms makes delays vary "so".
Fix: restore the two bullets, and rewrite the epidist line as two sentences.

**11. `exchange/_partials/02-composable.qmd:200-201`.**
"Changing an assumption means swapping one part for another" replaces a line the canonical decks already have.
JuliaCon `03-approach.qmd:11` and the 40 minute deck line 657: "Adding a new application means defining only the novel parts".
Fix: use the original.

**12. `exchange/_partials/05-workflow.qmd:20-24` and `:36-43`.**
The strip's labels render at about ten pixels on a 1920 canvas and bullets 1 and 2 read the same labels out.
On screen the stage names and the brick and teal labels are illegible past the front row; the right column is two thirds empty below the strip.
Fix: redraw the strip taller with larger labels, and cut bullets 1 and 2 to one line pointing at it.

**13. `exchange/_partials/01-who.qmd` and `02-composable.qmd:270-276`.**
Two more slides overflow the 1080 canvas: who at 1139 and EpiNow2 at 1130.
The who attribution sits on the footer bar; the EpiNow2 results figure is 560px under a 260px graph plus a callout and a three-line attribution.
Fix: shrink the timeline to 60 per cent and the results figure to 500px, or drop the who slide's photo attribution.

**14. `exchange/_partials/04-delays.qmd:76-80`, `:144-148`, `01-who.qmd:34-37`, `05-workflow.qmd:45-49`.**
Four attribution blocks carry commentary rather than sources.
"Continuous delays, so the numbers differ slightly from the daily-window figure on the next slide"; "Static fallback for the slider on the previous slide"; "from the keynote the day before"; "the placement of the labels is my reading of".
Fix: keep the source, delete the aside, and promote the continuous-versus-daily point to a bullet if it must be said.

**15. `exchange/_partials/04-delays.qmd:207-222`.**
The spec asked for "one line on where AI could help" in the delays section and got a full-width four-bullet slide with no visual.
It is the only content slide without a figure, and two of its bullets are two lines long.
Fix: cut to two question bullets on the "Three packages" slide, or add the `fig-truncation.png` diagram and keep it to three lines.

**16. `exchange/_partials/02-composable.qmd:152-163`.**
The 60 per cent column of the "Two approaches" slide holds three headshots and nothing else.
In JuliaCon the photos sat under bullets on slides that had a figure or code as the main visual.
Fix: move the photos under the bullets and put the approaches page's two-piece schematic, or the code, on the right.

**17. `exchange/_partials/04-delays.qmd:1`.**
His wry divider "Unfortunately, biases" (JuliaCon `01-biases.qmd:1`) is gone and the deck runs from definition into censoring with no beat.
`style-juliacon.md` says these titles stay exactly as written.
Fix: use it as the heading of the "Both events" slide, or as a second divider.

**18. `exchange/index.qmd:31`.**
"Seven talks from 09:00 to 12:00" miscounts the programme.
`exchange-programme.md` lists five talks and two group introductions.
Fix: "five talks and two introductions".

**19. `notes/draft-exchange-report.md:22` and `:28`.**
The report's counts are off by one.
The delays partial holds six slides (five counted plus the uncounted fallback), so the deck is 27 sections and 26 counted, not 26 in total.
Fix: correct the table.

## Fine as is

- Running order, retitling, `index.qmd` subtitle and description, and the root index card all match the spec.
- The cut from 35 to 22 minutes is explained slide by slide in the report and is defensible.
- "Maybe nothing doing there at the moment" is on the slide verbatim.
- Whitty, ONS, Lison, "What is composable modelling?", the EpiNow2 slide and the delay definition are the JuliaCon wording, trimmed by whole bullets only.
- The Interoperability swap on "What we want" uses the 40 minute deck's own lines (`index.qmd:533-540`).
- The composed distributions code matches the approaches page with only the inspection calls dropped, as the attribution says.
- Philipps quotes, Jang and Radev citations, 145 releases, 333 of 425 pull requests, SitRep 087, the McCabe date and the LogNormal(1.6, 0.6) numbers all trace to their stated sources.
- Both callouts are canonical and one sentence each.
- The slider works, its static fallback follows as an uncounted slide, and the choice of a truncation slider over the spec's two options is explained.
- The keynote now has a renewal slider (`keynote/_partials/02-modeller.qmd:42`), so the report's "had not made one" note is stale but the choice still stands.
- llmisms grep hits beyond findings 10 and 11 are canonical wording, citations, alt text or `## Talk plan`, which the spec keeps.
- Lint is clean and no line exceeds 80 characters outside link targets.
