# Review 1: communication lecture deck

Reviewed 2026-09-12 against `spec-communication.md`, `proposal.md` section 2, `drafting-rules.md`, `style.md`, `llmisms.md`, the research notes and the blog Rmd sources.
Rendered with the sandbox off and all 30 slides screenshotted at 1920 by 1080, plus the three fragment states of the prose slide.
Findings first, most important at the top, then what is fine.

## Findings

### 1. Wrong direction on the SitRep 087 misread

`communication/_partials/04-under.qmd:91-92` says "Every count came out 25% high".
The source says the opposite: "Applying the old /20 divisor to a 25-count grid undercounts every bar" and "SitRep 083's 15 May onset count reads 26, and the same figure misread through the wrong divisor came out as 8" (`BVDOutbreakSize/data/README.md:77`).
The deck's own figure agrees with the source, not the bullet: the assumed grid reads the peak as 70 and the true grid as 87, so the script read low.
Fix: "Every count came out about 20% low and nothing looked wrong", and check `scripts/comms-figures.py:117-155` labels the panels the same way.

### 2. how-I-llm phrasing copied, against the spec

The spec says "Do not use how-I-llm phrasing. Restate its facts plainly."
`03-with.qmd:59-60` "The first prompt got it most of the way, and wrong in the ways that mattered" is verbatim from `how-I-llm/_partials/09-steers.qmd:29-30`.
`03-with.qmd:61-62` "Each steer was a judgement I could make and the agent could not" is `09-steers.qmd:31` with two words changed.
`03-with.qmd:9-10` "An agent wrote the words and drew the figures" is `01-where-i-am.qmd:4` with "found the numbers" cut and "charts" swapped for "figures".
`03-with.qmd:33-34` "so git log says who did what" is `05-scale.qmd:7-8` minus "mostly".
`03-with.qmd:98` heading "Ten times the throughput" is the first half of the `05-scale.qmd:12` line.
Fix: restate each as a plain fact, for example "The first draft was close and wrong where it counted" and "Each steer was a call the agent did not make".
The proposal named the steers line as a quote, so put that one back to Sam rather than deciding.

### 3. Dropping "mostly" makes the git log claim false

`03-with.qmd:33-34` says the bot account means "git log says who did what".
The source hedged: "git log mostly tells you who did what" (`05-scale.qmd:7`), and the record shows why: 40 commits under "Sam Abbott" and 11 under "Sam" in the BVD clone, and "The 21 PRs under Sam's own account in July contain only agent-authored commits" (`research-agentic.md:133`).
Fix: restore "mostly", or say "so git log tells you who did most of it".

### 4. The live iframe rendered blank

`01-audiences.qmd:83` is the full-bleed `background-iframe` of the UK dashboard page.
After a 25 second wait in headless Chromium the slide was white apart from the slide number; the drafter's report says it took about 20 seconds.
Fix: keep the static slide 3 as the fallback it already is, and either drop the iframe slide or test it on the venue network before deciding to keep it.

### 5. Two blog quotes are not verbatim

`01-audiences.qmd:124-125` joins two sentences that are not adjacent in the source and cuts both.
The source reads "your forecast becomes part of another product, the forecast ensemble. This is a good thing as ensembles are typically more robust than forecasts from single models and in many cases give better performing forecasts. However, they can be very hard to learn from, and though we have really tried to learn more about how to forecast it has been difficult" (`surrogate-ensemble-forecast.Rmd:40`).
Dropping the middle sentence removes his positive verdict on ensembles.
`01-audiences.qmd:14-15` stops the sentence at "decisions"; the source continues "or helped inform members of the public about their individual risk" (`rt-reflections.Rmd:48`), and the source opens "That said, we don't know".
`02-software.qmd:44-45` drops the opening "Of course" (`rt-reflections.Rmd:57`).
Fix: mark cuts with an ellipsis, or quote one complete sentence per slide, which the spec's "one quote per slide" already suggests.

### 6. Consensus slide bullets have no source

`01-audiences.qmd:36-39` describes the SPI-M-O process, and the drafter's report says it is "from memory of how it worked, not from a written source".
The GOV.UK page on the slide says "Different modelling groups use different data sources to estimate these values using mathematical models that simulate the spread of infections", which is a usable source for bullet 1.
Fix: cite that page text in the attribution and cut or soften bullets 2 and 3 to what the page supports.

### 7. Ensemble readings stated as fact

`01-audiences.qmd:121-122` "The ensemble beat most single models in most countries" and "It also missed the turns the teams missed" are the drafter's readings of Figures 4 and 2, by their own account.
Sherratt et al. 2023 gives a number, that the ensemble outperformed a large majority of participating models on relative WIS, so use the paper's figure and cite it in the attribution.
Fix: quote the paper's percentage for bullet 3 and drop or source bullet 4.

### 8. "I did not talk to the press" overstates the source

`01-audiences.qmd:96-97` states it as fact.
The source is a feeling, not a record of what happened: "I personally didn't feel it was useful for me to directly interact with the public/media" (`iisa-...Rmd:151`).
Fix: "I left the press to people trained for it" or quote the line and drop the "nonsensical" quote on that slide.

### 9. Wrong date on the how-I-llm attribution

`04-under.qmd:119` gives "How I am LLM, 2026-08-10".
The deck's front matter says `date: 2026-07-30` (`how-I-llm/index.qmd:8`).
Fix: 2026-07-30.

### 10. "Decks" should be "deck"

`04-under.qmd:7` says "Three edits from my own decks".
All three commits, `4897ba8`, `a865fe2` and `bdd0a34`, are in one repository, `how-to-serial-interval`.
Fix: "one of my own decks".

### 11. Slogan and negative parallelism baked into a figure

The digitiser figure carries the caption "Same pixels, two answers. Caught by the reporting triangle, not by eye" (`scripts/comms-figures.py`, rendered on slide 25).
That is pattern 4 and pattern 6 from `llmisms.md`, and it repeats bullet 4 on the same slide.
Fix: delete the caption from the figure.

### 12. Banned word

`02-software.qmd:64-65` "public health practitioners" is on the author's own banned list in `CLAUDE.md` and in `llmisms.md` pattern 10; the grep missed the plural.
Fix: "public health analysts", or quote the grant text if the exact phrase matters.

### 13. Slides too busy

Slide 9 "Other scientists" (`01-audiences.qmd:114-144`) has four bullets, a quote and two stacked figures, renders 1104 px tall against a 1080 px slide, and the country labels on Figure 4 are unreadable.
Fix: one figure, two bullets, and the quote.
Slide 25 "Confident, plausible, wrong" (`04-under.qmd:86-94`) has four bullets each rendering three lines, twelve lines of text beside the figure.
Fix: cut bullet 1 to one line and let the figure carry SitRep 087.
Slide 4 "Government" bullet 2 (`01-audiences.qmd:9-11`) renders four lines, glossing SPI-M-O and SAGE in one bullet.
Fix: split the glosses or move one to the attribution.
Slide 14 "Community" bullet 1 (`02-software.qmd:64-66`) renders four lines.
Fix: drop "a forum, a monthly seminar since May 2023, a contribution ladder" since bullet 2 and the screenshot carry them.

### 14. Slides thin or without a visual

Slide 17 "What I use it for" (`03-with.qmd:3-27`) has no figure; the right column is two quote blocks.
The rules allow no visual only for a code slide or a single quote.
Fix: one quote, or add the prompts page screenshot already used on slide 28.
Slide 28 "Four things" (`05-asks.qmd:14-22`) shows four screenshots at about 500 px wide, none legible; they work as thumbnails only if the audience remembers them.
Fix: fine if intended as a recap of artefacts, otherwise two larger shots.

### 15. No hand-off to Poels

The spec allows one line handing each neighbour their topic and proposal slide 16 names both.
`04-under.qmd:9` hands detection and citation bias to Algaba; nothing hands chatbots as channels to Poels, who has already spoken.
Fix: optional, one line on slide 4 or slide 8, or leave it.

### 16. Screenshot legibility

Slide 6 "The public" (`01-audiences.qmd:71`) shows a report-style figure with a paragraph caption at about 6 px text; the caption reads as noise.
Slide 19 steers screenshot (`03-with.qmd:64`) is unreadable at slide size, and the "fifty-three" it is there to show cannot be seen.
Fix: crop the UK page to the three panels, and crop the steers page to the "There are fifty-three so far" paragraph.

## Fine as is

- Running order follows proposal section 2 slides 1 to 21 with 22 content slides, A 7 including the iframe, B 4, C 5, D 4, E 2, and no summary slide.
- Section A quotes are verbatim where checked in full: `rt-reflections.Rmd:63` and `:71`, `iisa-...Rmd:132` and `:150`, one quote per slide.
- Ottawa and the Philippines are absent; Poels' and Algaba's topics are not covered.
- Steers recount: `JuliaCon2026/notes/steers.md` has 130 blank-line-separated blockquote blocks, last commit `755f1f1` on 2026-08-14, and `prompts.qmd:172` says fifty-three; the slide matches both.
- "at least 13.5% of 2024 PubMed abstracts" matches `research-communication.md:180`; "114 claims, 67 changed" matches `research-agentic.md:44` and commit `8c7e834` exists; "530 became 353" matches `1fceb9a`; "712 of 1,371" matches `research-agentic.md:45`.
- Bot counts on slide 21 (2,144; 85.5%; 11.9%; monthly bars) match `research-agentic.md:197-203`; BVD counts (497 commits, 333 of 425, author table) match `:205-218`; the README disclosure quote is verbatim (`README.md:50-51`).
- The three before and after pairs match `llmisms.md` examples for patterns 2, 3 and 1, the commit hashes resolve, and the fragments reveal in order.
- SitRep 081 numbers match `data/README.md:75`.
- EpiNow2 1.1.0 is dated 2020-09-01 in the CRAN archive; the `epinow()` call matches `EpiNow2/vignettes/EpiNow2.Rmd:93-100` minus the verbose line; Wisconsin "first time ever, reported data on a Sunday" is sbfnk's reply on issue 171.
- The bio quote is Sam's own words (`JuliaCon2026/index.qmd:80-83`); "too complex for anyone else to use" and "Agents make that worse" are from the corrected roadmap deck.
- The drafter's swap of `uk-rt-dashboard.png` to the consensus slide is right: the image is the GOV.UK "Latest R and growth rate for England" panel, not the epiforecasts dashboard.
- `./scripts/lint.sh` is clean; the four long lines in `05-asks.qmd:15-21` carry link targets and are exempt.
- Of nine attribution URLs curled, seven returned 200; Science Advances and CDC returned 403 to curl, which is bot blocking rather than a dead link.
- The remaining `llmisms.md` grep hits are quoted source or sourced facts, as the drafter's report says.
- Other rendered slides fit within 1080 px with no overflow; the code slide and the two single-quote slides are sparse by design.
