# Fix 1: communication lecture deck

Applied 2026-09-12 against `review-communication-1.md`, findings 1 to 14
and 16. Rendered with the sandbox off, every changed slide screenshotted at
1920 by 1080 and checked by eye. `./scripts/lint.sh` clean. Nothing committed.

1. SitRep 087 now reads "Every count about 20% low and nothing looked
   wrong", matching `data/README.md:77`. The figure labels already agreed
   with the source (assumed grid reads 70, drawn grid 87), unchanged.
2. Every how-I-llm line restated. "The brief and the corrections are mine.
   The text and the figures are the agent's"; "The first draft was close
   and wrong where it counted"; "Each steer was a call the agent did not
   make"; heading "Ten times the reading". Facts unchanged.
   **For Sam.** Proposal slide 13 named "Every steer above was a judgement I
   could make and it could not" as a quote. Restore it on slide 19 if wanted.
3. Bot account bullet now "so `git log` tells you who did most of it".
4. Iframe slide kept, slide 6 remains its static fallback.
   **For Sam.** It rendered blank in headless Chromium for the reviewer.
   Test it on the venue network before deciding to keep it.
5. Slide 4 ends the quote at "decisions" with an ellipsis. Slide 9 quotes
   one complete sentence, "However, they can be very hard to learn from,
   and though we have really tried...". Slide 13 restores "Of course".
   Every section A quote rechecked against the Rmd files; the other five
   are complete sentences, verbatim.
6. Consensus bullets follow the GOV.UK R value page ("Different modelling
   groups use different data sources", "Evidence from several models is
   considered, discussed, combined", "shown as a range"). The attribution
   quotes that text, read 2026-09-12.
7. Slide 9 states the Sherratt et al. 2023 result, 83% of case forecasts
   and 91% of death forecasts on relative WIS, cited in the attribution.
   The "missed the turns" bullet and Figure 2 are gone; Figure 4 stays.
8. "I left the press to people whose speciality it is. No training, no
   time", from the iisa post line 151.
9. how-I-llm attribution dated 2026-07-30. 10. "one of my own decks".
11. Slogan caption deleted from `digitiser()` in `scripts/comms-figures.py`
    and the figure regenerated.
12. "public health analysts" for "practitioners".
13. Slide 9 is one figure, two bullets and the quote. Slide 25 bullet 1 is
    one line, the rest two. Slide 4 splits the SPI-M-O and SAGE glosses.
    Slide 14 community bullet trimmed. WIS gloss moved to slide 9, first use.
14. Slide 17 keeps one quote, the brief for this lecture, and no figure,
    which the rules allow for a single quote. Slide 28 keeps four
    screenshots as a recap of the artefacts behind the four asks, now one
    tiled PNG, `comms-shot-recap.png`, so the grid no longer overflows.
16. New `scripts/comms-crop.py` (`uv run --with pillow`) crops the UK page
    shot to the three panels, `comms-shot-covid-uk-panels.png`, and the
    steers shot to the heading, the fifty-three paragraph and the workflow
    steers, `comms-shot-juliacon-steers-para.png`. It also builds the recap
    grid. The full screenshots stay on disk.

Also fixed: slides 14 and 18 overflowed 1080 px in my render, so the forum
and bot profile screenshots are height capped at 620 px.

Left for Sam: finding 15, the Poels hand-off, was out of scope and not
added. `comms-hub-ensemble-less-good.png` and `comms-consensus.png` are now
unused; delete if not wanted. Remaining llmisms grep hits are the quoted
point-stamp example, alt text, the GOV.UK "considered, discussed and
combined" wording, "every number" in ask 4, "for the first time" from the
GitHub reply, and his own "Agents make that worse".
