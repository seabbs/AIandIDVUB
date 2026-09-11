# Review 1: proposal and scaffold

Cross-review of `notes/proposal.md` and the site, 11 September 2026.
Read-only pass; nothing was changed.
Most important first.

## Findings

**1. `index.qmd:124-126`.**
The new bio sentence reinstates a claim he corrected by commit.
Site: "Most of the code I now ship is written by coding agents and reviewed by me".
His corrected line (`how-I-llm` commit 8c7e834, `01-where-i-am.qmd:18-19`): "Most code I ship is written by an agent. About half of it carries a review from me".
The sentence also carries a bolted-on ", and I am trying to work out what that means" and a rule of three ("built, checked and shared").
Changing the Julia sentence is acceptable, since the block is labelled bot-drafted and Julia is off-topic here, but this replacement reads as an LLM-ism and is false by his own count.
Fix: use his two sentences verbatim, or drop the sentence.

**2. `notes/proposal.md:178` and `:182-271`.**
The lecture minutes sum to 30 with nothing left for the plan slide, the close, or questions in a 30 minute slot.
Sections: 8 + 5 + 7 + 7 + 3 = 30.
Fix: cut two minutes from A and one from D, or state that the slot has no questions.

**3. `notes/proposal.md:46` and `:178`.**
The stated slide counts do not match the slides enumerated.
"about 24 content slides" against 19 numbered keynote slides; "about 26 content slides" against 22 numbered lecture slides.
Both decks then run at about 0.75 slides a minute, half the house rate in `style.md` ("About 1.5 slides a minute").
Fix: correct the counts, and either add slides or say each slide will hold more than the style allows.

**4. `notes/proposal.md:326-327`.**
The proposal admits its own timing is wrong.
"Cut to three ... if section C runs long, which it will."
Fix: retime section C now rather than deferring the cut to the day.

**5. `index.qmd:110`, `:116-117`, `:121`.**
The site publishes three claims the research marks contradicted or unverified.
"3rd of January 2020" (research-history: IISA post says 6 January); "used by over a million people" (research-history: "Partly verified"); "upwards of 30 public health agencies" (research-history: "Unverified. No list of 30 agencies was found").
The proposal puts the first two to Sam in section 5, but the site carries them already.
Fix: either keep the JuliaCon bio verbatim and label it "My JuliaCon 2026 bio", or fix the three claims and label it as his current bio.

**6. `index.qmd:98`.**
"My conference bio" implies a bio was submitted to these organisers, and the brief shows none.
JuliaCon said "My submitted conference bio" and the steers confirm it was submitted there.
Fix: relabel as the JuliaCon bio or as "About me".

**7. `communication/index.qmd:36-37` and `panel/index.qmd:26`.**
The abstract block is labelled "The organisers' request" but carries bullets that are not in the request.
"Karolien Poels speaks before ... and Andres Algaba after, on the same title from the AI side" is from the programme, and "from the AI side" is invented.
"Closing remarks follow at 16:15" is from the programme, not the ask.
Fix: move programme facts out of the `.abstract` block into the session meta or a "Around it" line, and drop "from the AI side".

**8. `notes/proposal.md:17-18`, `:21`, `:4`.**
Three absolutes the research does not support.
"Nobody on the programme has published on coding agents" against research-workshop "No speaker was found to have published".
"The word 'agent' means an RL policy to half the room" has no source.
"Every claim below points at a research note" is false given the two lines above.
Fix: "None of the speakers was found to have published", drop "half the room", drop "Every".

**9. `notes/proposal.md:136`.**
A quote is garbled into a sentence that does not parse.
"Who pays, and who can do this work at all, is narrowing" against the source (`11-governance.qmd:13`): "Who can do this work at all is narrowing. Agents make that worse".
Fix: quote the source as two sentences.

**10. `notes/proposal.md:76-77`.**
The mpox slide credits him with "Delays and the serial interval" when the research shows others did that.
research-history: "Sam is not an author on Ward et al."; his mpox record is the BMJ editorial, Endo et al., and the Overton nowcast.
Fix: "Nowcasting for UKHSA, and the editorial on Ward et al.", with the figure being the Overton nowcast.

**11. `notes/proposal.md:206-207`.**
Ottawa and the Philippines are stated as fact but the research did not verify them.
research-communication: Philippines chapter "paywalled, so quote not verified directly"; Ottawa "not fetched".
Fix: keep CDC (CFA page and MMWR, both fetched) and drop or mark the other two.

**12. `notes/proposal.md:158-160`.**
"worse at turning points, which is where decisions are made" has no quoted source.
It comes from the note author's synthesis in research-ai-methods "What a modeller might say", not from a paper quote; CAPE reports alert sensitivity and Jafari reports that a mixture did best.
Fix: cite a paper with a turning-point result or soften to "less is known about peaks".

**13. `notes/proposal.md:242-243`.**
"Fifty-three steers" was a mid-build count.
JuliaCon `prompts.qmd`: "fifty-three so far and the build is not finished".
Fix: recount from `JuliaCon2026/notes/steers.md` before it goes on a slide.

**14. `notes/proposal.md:264-266` and `:257`.**
Two lecture slides step onto the next speakers.
D17 "What a dashboard means when the reader asks a chatbot about it" is Poels' territory (research-workshop: "chatbots and generative AI as communication channels").
D16 Kobak on LLM vocabulary sits beside Algaba's detection work (Mobini et al. 2026).
Fix: keep D16 to his own before and after pairs and hand D17 to Poels in one line.

**15. `notes/proposal.md:89-92`.**
"The loop" borders Lecture 1, "Approaches to Infectious Disease Modelling ... Mathematical, Statistical, and AI Perspectives".
Fix: keep it to one slide drawn for the non-modeller, as the proposal already suggests, and say so on the slide.

**16. `notes/proposal.md:113-125`, `:184`, `:230-231`.**
The proposal assumes tooling and UK acronyms the room lacks.
"pull requests", "bot account", "git log", "reporting triangle invariant", "SPI-M-O", "SAGE", "UKHSA", "WIS" appear without a gloss, while research-workshop says "pitch at a level that assumes statistical modelling but not LLM tooling".
Fix: one line each on first use, as `style.md` already requires for $R_t$ and nowcasting.

**17. `notes/proposal.md`, missing.**
The research offers a hook this room co-wrote and the proposal does not use it.
research-workshop: "The behaviour gap in the Belgian scoping review is a hook this room already accepts" (Bagaforo et al. 2026, half of 105 models included behaviour).
Fix: consider it for keynote slide 8 or 16.

**18. `prompts.qmd:69-70`.**
The clean-up splits one judgement into two.
Original: "agentic model compostioon i.e Google foerecating success with flusight?"; cleaned: "agentic model composition, Google's forecasting success with FluSight."
The "i.e." made Google an example of agentic composition, and the question mark is gone.
Fix: "agentic model composition, i.e. Google's forecasting success with FluSight?"

**19. `index.qmd:40-41`, `:56-57`; `keynote/slides.qmd:23-28`; `communication/slides.qmd:23-27`.**
The site encodes the proposal's structure before Sam has chosen it.
The brief asked for "slides with their titles and qr codes etc in place but not at this stage content", and the proposal says "Sam decides what survives".
Fix: fine if he accepts the outline; otherwise the card blurbs and plan bullets need to change with it.

**20. `keynote/index.qmd`, `communication/index.qmd`, `index.qmd`.**
No link to the public workshop page, where JuliaCon linked each pretalx session.
research-workshop: https://www.simid.be/events/workshop2026/.
Fix: add a "Workshop page" button beside "Slides".

**21. Style hits in `notes/proposal.md`.**
`:128` "which is the composability argument" is a bolted-on clause (pattern 2).
`:275-276` "matter more, not less" is negative parallelism (pattern 6).
`:257` "Everything sounds the same" is a universal against Kobak's "at least 13.5%" (pattern 13).
`:208-209` "Every default is a modelling decision someone else now makes" has no source (pattern 13).
Fix: delete the tail, state the positive, replace the universals with the measured share.

**22. `communication/slides.qmd:26`.**
"prose that all sounds the same" repeats the universal above on a slide.
Fix: "prose that sounds the same".

## Fine as is

Structure matches JuliaCon: `_quarto.yml`, `index.qmd`, `prompts.qmd`, one directory per talk with `index.qmd`, `slides.qmd` and `_partials/`, plus `panel/` for a session that has no deck.
The partials carry a `#` title and an HTML comment only, so there is no slide content.
Talk plan and Thank you slides carry the QR code; the three QR files differ from the JuliaCon ones and are timestamped 14:32 today, and `make_qr.sh` points at the three talk pages, though no decoder was available to confirm the payload.
`prompts.qmd` and `notes/steers.md` at HEAD agree on four steers.
The organisers' ask appears as bullets in `.abstract` blocks on all four pages, faithful to the brief apart from finding 7.
Talk plan slides have JuliaCon precedent.
Numbers checked and matching the research: DON617 6757 and 3267; bot PRs Jun 531, Jul 744, Aug 399, 2144 total, 85.5% merged; 145 releases; 333 of 425; SitRep 081 54% and 087 steps 20 to 25; 500,000, 1.2 million and 20,000; 31 seminars; 114 claims and 67 changed; Kobak 13.5%.
The Google SAI correction is supported by Martinson et al. 2026 and Bracher and Funk 2026, and moving it to the agents section follows.
"Not an RL policy. Not a chatbot." is a contrast the room actually holds, so it passes pattern 6.
The exchange "where we might work together" bullets fit Libin's RL and Cimpean's fairness work.
`llmisms.md` greps over the `*.qmd` files return no point-stamps, morals, adjectives, metaphors, hedges, benefit tails or em dashes.
`./scripts/lint.sh`: "lint: clean", exit 0.
Quarto was not run here; the site rendered cleanly earlier per the orchestrator.
