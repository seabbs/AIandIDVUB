# Fix report: keynote deck, after review 1

Written 12 September 2026 against `review-keynote-1.md`, plus the steer to mine his past decks.
An earlier pass had edited the partials and scripts but left no report, render or screenshots; this pass checked each of its changes, finished the rest, rendered, screenshotted all 30 slides plus both fallbacks at 1920 by 1080, ran `./scripts/lint.sh` (clean) and every `llmisms.md` grep.
Nothing is committed.

## Findings, what was done

1. Iframe. Root cause found: `embed-resources` inlined the remote page as a `data:` URL at render time, which stripped its CSS and the anchor. Fixed with `data-external="1"`. Pointed at `stable/summary#Headline-estimates`, not the analysis page: the analysis page is 4 MB and blocked the deck's load event for over 30 s; the summary is 26 KB, framed in under 6 s, and its headline line carries the size estimate. Fallback kept.
2. "2026. Live". One figure, the September cumulative infections panel, 712 px tall. Vintage in the attribution (release `results-1699`, 9 September, data to SitRep 115 of 6 September). Sitrep page dropped.
3. "Checking is now the slow step".
4. "Most of the code I merge is agent-written. About half went in unreviewed".
5. "Agents wrote the ingest, the fits, the tests and the release pipeline".
6. Bullets that duplicated the boxes cut; figure now says "the trust of whoever decides". Panel lines restated: "Which of this is ours, and which is only not automated yet?" and "Name something you think an agent cannot do". Sam to confirm.
7. Attribution names Nick Reich's slide and the file path.
8. Map rows labelled by topic; no slide numbers; the agents row reads "coding agents".
9. Structure announcement deleted.
10. 90% interval deleted (not in a research note). Comma thousands throughout: 6,757, 3,267, 1,371, 21,000, 2,144.
11. Renewal bullet cut to two lines, colon gone.
12. Toy seeded on the exponential solution of the recursion (Euler-Lotka rate), so no dip; `keynote-renewal.png` regenerated from the same script; the ojs cell mirrors it.
13. Log axis ticks 1, 10, 100, 1,000 with explicit domain; top margin so the axis label clears the top tick; slider labels no longer wrap (`--label-width`, `--input-width`).
14. Both tails cut.
15. Bullet restating the footer dropped.
16. Bullets dropped, diagram kept.
17. Chain figure replaced by his truncation figure (see lifts); the chain bullet returns in its place.
18. "the term you cannot write down".
19. PINN bullets cut; Millevoi caveat in the attribution; two bullets and the figure.
20. "as it happened" and "Old counts cannot fall" cut. Also trimmed to two rendered lines: the $R_t$ and SPI-M-O bullets (2020), the Google and Bracher bullets, the bot account bullet, the joint model bullet (2026). The PHEIC clause is its own bullet.
21. Stage directions moved to HTML comments.
22. Attribution is source and date only.
23. $R_t$ figure cropped to four panels at full column width (`keynote-crop.py`).
24. Grant text and GOV.UK consensus statements in the attribution.
25. "CDC used `EpiNow2` for its COVID-19 $R_t$ estimates to June 2026", with the search-snippet caveat about the method change after 1 June 2026 in the attribution.
26. Nowcasting gloss now the first bullet.
27. "a WHO emergency, a PHEIC".
28. "Recent reports get two blind reads"; attribution lists the vintages the README records: SitReps 097 to 099, 104 to 107 and 110 to 114.
29. Duplicate cut from "2026. Live".
30. Authorship labels alternate above and below the bar; "a prompt" sits clear of the loop boxes (checked in render).
31. Talk plan left as is. Sam's call.
32. Both vertical lines and the $R_t$ = 1 line explained in the attribution, with the source constants.

## Lifted from his past decks

- JuliaCon 2026 roadmap, `05-what-it-takes.qmd` ("After skynet"): the travelling bullet in his words, the three-column layout, and the seabbs-bot and sbfnk-bot avatars (`keynote-seabbs-bot.jpg`, `keynote-sbfnk-bot.jpg`) onto "How I work now". The 966 merged PRs count was July and EpiAware-only, so the figure footer carries the current totals instead.
- JuliaCon 2026 roadmap, `00-outbreak.qmd` (the DRC opener): his bullet wording on both "A live outbreak built this way" slides. Its three June figures were not lifted; the September infections and $R_t$ figures already on the slides are the same plots three months on.
- JuliaCon 2026 roadmap, `10-community.qmd`: the whole slide "Community, in the age of robots", his three bullets and the emoji crowd, as a new slide in section E before the panel question. The EpiAwareAgents bullet was left out (the research note says it does not run yet). CSS for the crowd is inline in the partial.
- how to serial interval, `02-censoring.qmd` and `fig-truncation.png` (`keynote-truncation.png`): the figure and his line "Short delays are over-represented early in an epidemic" onto "What keeps going wrong", replacing the drawn chain figure. `keynote-chain.png` and its function in `keynote-schematics.py` are now unused.
- Checked and not lifted: the hpru-ppie-kickoff dashboard and ensemble figures (the proposal names his own $R_t$ figure for 2020, and ensembles are not in this talk); the BVDOutbreakSize collaboratory figures (June vintage); nfidd has no "two camps" slide in any of its four decks (grep), and "a lot of data or very good theory" is Nick Reich's, already attributed.

## Counts

30 numbered slides: title, talk plan, five dividers, 22 content, thank you. Two hidden fallbacks.
A 6, B 3 (+1 hidden), C 6 (+1 hidden), D 4, E 3.
No slide exceeds 1080 px; tallest are "2014. Watching" at 1076 and "2020. Doing it" at 1028.

## Greps

Remaining hits are author lists and alt text (rule of three), a plain list ("evaluation, and the forecast hubs"), "every push" (README), "the first situation report", "never confirmed" (his line), "at all" (his quote), and the talk plan heading.

## Left for Sam

- The talk plan slide (31) and the two restated panel lines (6).
- The live slide needs network. Open the summary page once before the talk so it is cached; the fallback swap needs a re-render, as the HTML comment says.
- Section E is now three slides for one minute; the community slide could move to C or go.
- The community slide's third bullet says "not Julia developers", his EpiAware wording; it may want generalising for this room.
- Some bullets still render at three lines: agent definition, pull request gloss, both SitRep bullets, Camacho, UDE, OutbreakFlow, TabPFN-TS, authorship, the live slide's sitrep bullet. Each carries a fact; cutting is his call.
- If the 90% interval is wanted back, add it to `research-history.md` section 2 first (release `results-1699`, 9,749 to 19,236).
- `keynote-chain.png` can be deleted if the truncation figure stays.
