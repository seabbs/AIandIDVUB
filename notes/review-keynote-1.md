# Review of the keynote deck, first draft

Read on 12 September 2026 against `spec-keynote.md`, `proposal.md` section 1, `drafting-rules.md`, `style.md`, `llmisms.md` and the five research notes.
Rendered with the sandbox off, screenshotted all 29 slides at 1920 by 1080, ran every `llmisms.md` grep, ran `./scripts/lint.sh` (clean), and curl-checked six attribution URLs (all 200, the Imperial DOI 302 to Spiral).

## Findings

1. `keynote/_partials/03-agents.qmd:69` The live iframe shows the report's landing page, not an estimate, and it rendered unstyled in headless Chromium.
   Evidence: the screenshot shows raw blue links, "Skip to content", a sidebar and the title; the same URL opened directly in Playwright is fully styled, so the fault is the frame, not the site.
   Fix: point the iframe at the analysis page anchor that carries the size or $R_t$ figure, or promote the hidden fallback figure to the visible slide and drop the iframe.

2. `keynote/_partials/01-outbreaks.qmd:172-182` Slide "2026. Live" overflows the 1080 px frame and carries two figures against the spec's one figure per outbreak.
   Evidence: rendered slide height 1108 px, the attribution touches the slide number, the sitrep image is 330 px tall and its x-axis dates overlap.
   Fix: keep the September cumulative infections panel, move the sitrep page to the live outbreak slide, and put the vintage of the sitrep page (8 June) in the attribution.

3. `keynote/_partials/03-agents.qmd:144` A how-I-llm line is copied, not restated.
   Evidence: "The bottleneck is how fast I can tell whether something is right" against the source "how fast I can tell whether something is right" (`01-where-i-am.qmd:23-24`).
   Fix: restate, for example "Checking is now slower than writing".

4. `keynote/_partials/03-agents.qmd:32-33` Same fault.
   Evidence: "An agent writes most of the code I ship. About half of it gets a review from me" against "Most code I ship is written by an agent. About half of it carries a review from me".
   Fix: restate in plainer words or mark it as a quotation with its source.

5. `keynote/_partials/03-agents.qmd:175-176` Same fault.
   Evidence: "Agents built the apparatus. Data ingest, the fitting pipeline, tests, the docs site, releases" against "Agents built the apparatus: data ingest, fitting pipeline, tests, docs site, releases" (`04-drc.qmd:86-87`).
   Fix: the figure on this slide already shows what agents built, so cut the bullet to "Agents built the apparatus" or restate.

6. `keynote/_partials/05-question.qmd:9-10` and `:33`, `:37` Near copies of how-I-llm phrasing.
   Evidence: "the trust of the people who act on the numbers" against "Trust with the people who act on the numbers"; "What is ours, rather than not yet automated?" against "What is genuinely ours, rather than merely not-yet-automated?"; "Tell me what you think agents cannot do" verbatim from `how-I-llm/index.qmd:46`.
   Fix: the proposal asked for these two questions, so Sam should decide whether to own the bot phrasing or rewrite it.

7. `keynote/_partials/04-other-ai.qmd:104` The quoted line is Nick Reich's, not Sam's.
   Evidence: `git log -S` on `nfidd/sismid-forecasting/sessions/slides/good-models.qmd` shows one author, Nicholas Reich, commit f6f18f7 of 15 July 2026, and the attribution says only "the nfidd forecasting course".
   Fix: credit Reich by name in the attribution or drop the quote.

8. `scripts/keynote-schematics.py:226-247` and `keynote/_partials/04-other-ai.qmd:14` The map figure bakes in slide numbers that do not match the rendered deck.
   Evidence: the figure reads "flows, slide 17", "foundation models, slide 18", "UDEs and PINNs sit near here, slide 16"; those slides render as 24, 25 and 23.
   Fix: replace the numbers with "next slides" or the slide titles.

9. `keynote/_partials/04-other-ai.qmd:11` Structure announcement, llmisms pattern 7.
   Evidence: "The next three slides take one row each".
   Fix: delete; the figure's right-hand column already says where each row goes.

10. `keynote/_partials/01-outbreaks.qmd:166-168` The 90% interval is not in any research note and the number formatting is inconsistent.
    Evidence: "between 9,700 and 19,200" beside "6757 confirmed cases and 3267 deaths"; the drafter's report says the interval came from a release bundle downloaded that day.
    Fix: add the interval and its source to `research-history.md` section 2, and use one thousands convention on the slide.

11. `keynote/_partials/02-modeller.qmd:11-13` The renewal bullet runs to five rendered lines and uses a colon gloss.
    Evidence: "A renewal process: today's infections are $R_t$ times a weighted sum of recent infections, weighted by the generation interval. Run it backwards to estimate, forwards to forecast".
    Fix: cut to "Today's infections are $R_t$ times a weighted sum of recent infections" and let the next slide carry the rest.

12. `keynote/_partials/02-modeller.qmd:63-70` and `figures/keynote-renewal.png` The toy dips below its seed before growing.
    Evidence: both the slider and the fallback show infections falling from 10 to about 8 at day 5 for every $R$, because the seed is five days but the generation interval spans 24.
    Fix: seed for as long as the generation interval support, or start the plot at the end of the seed.

13. `keynote/_partials/02-modeller.qmd:42-86` The slider's log axis stops labelling at 100 while the line runs to about 1000.
    Evidence: the screenshot shows ticks 9 to 100 and the line leaving the top of the gridded area.
    Fix: set an explicit y domain or use Plot's `ticks` option for the log scale.

14. `keynote/_partials/03-agents.qmd:34-36` Two bolted-on tails on one slide.
    Evidence: "a second GitHub login, so the history says who wrote what" and "specifying and checking, with little typing".
    Fix: full stop after "login", then "The history says who wrote what"; delete ", with little typing".

15. `keynote/_partials/03-agents.qmd:37-38` and `:41-45` The bullet restates the figure footer.
    Evidence: "2144 pull requests since January. 85.5% merged, 11.9% closed without merging" duplicates "2,144 total, 85.5% merged, 11.9% closed unmerged" printed under the bars.
    Fix: drop the bullet or drop the footer.

16. `keynote/_partials/05-question.qmd:7-20` The diagram restates the bullets word for word.
    Evidence: the three boxes read "build and check", "stays the object", "keep the question, fitness for use, the trust of those who act on the numbers".
    Fix: keep either the bullets or the boxes, not both.

17. `keynote/_partials/02-modeller.qmd:137-141` The chain figure restates bullet two.
    Evidence: figure text "Only a point estimate is passed on. The interval at the end is too narrow." against the bullet "Chained models pass on a point estimate. The interval at the end is too narrow".
    Fix: remove the sentences from the figure and keep the picture.

18. `scripts/keynote-schematics.py` (UDE figure) An absolute inside the figure text.
    Evidence: "The transmission rate is the term nobody can write down."
    Fix: "the term you cannot write down" or delete the sentence.

19. `keynote/_partials/04-other-ai.qmd:35-42` Busiest slide in the deck.
    Evidence: four bullets of two to three rendered lines each plus a figure with three lines of caption prose.
    Fix: cut the PINN definition bullet, which the drafter admits has no research source, and move the Millevoi caveat to the attribution.

20. `keynote/_partials/03-agents.qmd:116-120` and `01-outbreaks.qmd:33-38` Bullets over two lines.
    Evidence: the SitRep 087 bullet renders at four lines, the Camacho bullet at four.
    Fix: cut "Old counts cannot fall" (the previous sentence implies it) and cut "as it happened" from the Camacho bullet.

21. `keynote/_partials/02-modeller.qmd:112-116` and `03-agents.qmd:102-106` Attribution blocks carry stage directions.
    Evidence: "Shown only if the room has no network: swap `visibility` between the two slides."
    Fix: move the instruction to an HTML comment; Quarto drops hidden slides from the HTML entirely, so the swap needs a re-render anyway.

22. `keynote/_partials/05-question.qmd:23-25` Attribution carries commentary.
    Evidence: "A guess. The moving line is from how I LLM, where a claim that agents could not do long-horizon work lasted about six months".
    Fix: keep the source link and date only; the heading already says it is a guess.

23. `keynote/_partials/01-outbreaks.qmd:73` The $R_t$ figure is too small to read.
    Evidence: six panels occupy about half the column width with axis text under 10 px at 1920 wide.
    Fix: crop to two panels, or set `width="100%"` and let the height follow.

24. `keynote/_partials/01-outbreaks.qmd:68-69` A claim without its source in the attribution.
    Evidence: "Weekly estimates and forecasts to SPI-M-O" rests on grant text (`research-history.md` section 1), which the attribution does not cite.
    Fix: add the grant text or the GOV.UK consensus statements to the attribution.

25. `keynote/_partials/01-outbreaks.qmd:102` Tense outruns the source.
    Evidence: "Used by public health agencies, including CDC" is present tense, and `research-communication.md` section 3 records that the CDC $R_t$ page no longer mentions EpiNow2 after June 2026.
    Fix: "Used by CDC for its COVID-19 nowcasts to 2026" or past tense.

26. `keynote/_partials/01-outbreaks.qmd:98-101` The nowcasting gloss comes after the first use.
    Evidence: bullet one says "`epinowcast` for nowcasting" and bullet two defines the word; the timeline figure on slide 3 also labels 2022 "nowcasting".
    Fix: swap the two bullets.

27. `keynote/_partials/01-outbreaks.qmd:163-164` PHEIC is not glossed.
    Evidence: "a PHEIC on 17 May" with no expansion anywhere in the deck.
    Fix: "a WHO emergency, a PHEIC, on 17 May".

28. `keynote/_partials/03-agents.qmd:64-65` A universal the README supports only for the vintages it describes.
    Evidence: "two blind reads per report" against README notes of "two blind readers" for SitReps 104 to 106 and 110.
    Fix: "two blind reads on each new report" or check the README covers every vintage.

29. `keynote/_partials/01-outbreaks.qmd:169` and `03-agents.qmd:64` The same fact appears twice.
    Evidence: "The situation reports are PDFs, in French, most days" and "The situation reports are French PDFs. Agents read them".
    Fix: keep the second, cut the first.

30. `scripts/keynote-counts.py` and `scripts/keynote-schematics.py` Labels collide in two figures.
    Evidence: the authorship bar reads "DependabotBy hand", and in the agent loop "a prompt" sits under the "Check passed?" box.
    Fix: put the two small bar labels above and below the bar, and move the loop labels clear of the boxes.

31. `keynote/slides.qmd:19-31` The talk plan slide is the agenda that `llmisms.md` pattern 11 cuts.
    Evidence: five bullets that announce the five sections.
    Fix: Sam's call; the drafter was told not to touch it.

32. `keynote/_partials/03-agents.qmd:96-100` The fallback $R_t$ figure has two unexplained vertical lines.
    Evidence: a dashed line near 17 May and a dotted line near 7 June with no legend; the alt text names only one.
    Fix: say what both lines mark in the attribution.

## Fine as is

- Spec fidelity: proposal order followed, 21 content slides plus two hidden fallbacks, Google as LLM-guided tree search on slide 13 with its own loop figure and Bracher and Funk in the attribution, no RL or bandit explanation, no start date, no million users, no 30 agencies, no summary slide.
- The mpox slide credits Overton et al. 2023 and the BMJ editorial, names Ward et al. as the authors of the delay estimates, and Kucharski is not claimed.
- Section times hold: A 6 slides, B 3, C 6, D 4, E 2, about 0.85 content slides a minute.
- Glosses land for $R$, $R_t$, SPI-M-O, UKHSA, renewal process, generation interval, pull request and bot account.
- The eight Kraemer et al. Table 1 rows on the map match the PMC text, checked today.
- Every date and count in sections A, C and D that I traced sits in a research note with a URL, except the two items above.
- Verbatim lines that are Sam's own writing are exact: "at least 80% but on time", "We sometimes published nonsensical estimates", "In many cases the package is too complex for anyone else to use", "Who can do this work at all is narrowing. Agents make that worse".
- "Not an RL policy. Not a chatbot" names the belief this room holds, so the contrast earns its place.
- "I do not have a defence for this. I am part of the problem" is on the `llmisms.md` survivor list.
- The remaining grep hits are author lists, alt text, "Refit on every push" and "topped all three", each backed by a source.
- The ojs slider renders and responds; Observable Plot loads from a CDN, so the fallback is needed for a room without network.
- Lint is clean and no slide other than "2026. Live" and the iframe slide exceeds 1080 px.
