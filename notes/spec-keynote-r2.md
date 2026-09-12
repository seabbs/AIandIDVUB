# Keynote, round two spec

From his detailed notes of 12 September (`steers.md`, last long entry).
His verdict on the draft: "vague and LLM weird titles, lack of detail,
overly full slides, circular". Read `round-2.md`, `drafting-rules.md`,
`style.md` and `llmisms.md` first. This file overrides `spec-keynote.md`
and `proposal.md` section 1 where they differ.

Rules that apply throughout:

- Titles say the thing. No "watching", no "doing it", no "the other AI",
  no "fitting the unfittable". Name the outbreak, the method, the tool.
- One image per slide, and more slides rather than one compact slide
  lacking information.
- Attributions short: author, year, venue or URL. Not repository creation
  dates, not crop scripts, not "copied from". No refs at all under
  schematics drawn for this talk.
- "We" for the pandemic work.
- Reuse the JuliaCon 2026 decks' language and slides freely; he put a lot
  of work into them.
- Do not say what later speakers will cover.
- Quotes are assigned to a named person in the text, not in an aside.
- Slide budget: count content slides only; dividers, plan, title, thank
  you and hidden fallbacks are free. About 28 content slides for 25
  minutes at most.

## Plan slide

- "Ten years of outbreak modelling" (no ", from West Africa to the DRC")
- "Use of AI methods in outbreak modelling"
- "Agentic AI and outbreak modelling"
- No "Where does AI fit?" bullet.

## Section 1. Ten years of outbreak modelling

Two timeline slides to open:

1. **250 years of outbreak models.** Bernoulli 1760 to today, one figure,
   no bullets. Sources `research-history.md` section 3.
2. **My ten years.** A second timeline of the outbreaks he has modelled,
   2014 to 2026, timeline across the top and short bullets below giving
   the outbreak and the kind of modelling done. Regenerate
   `scripts/keynote-timeline.py` into two figures.

Ebola, West Africa, 2014 to 2016, three slides, one picture each:

3. **CDC's projection.** Meltzer et al. 2014: what they estimated (550,000
   to 1.4 million cases by January 2015), the method (an exponential
   growth model without intervention), what happened (about 21,000 by
   mid-January). Picture: the MMWR projection figure or the Nature news
   headline.
4. **Real-time forecasts in Sierra Leone.** Camacho et al. 2015 and Funk
   et al. 2018 and 2019: what they estimated (district-level R and
   forecasts), the method (semi-mechanistic), what happened (Funk 2019
   assessed them). Picture: `keynote-funk2019-forecasts-panel.png`.
5. **Delays from the WHO Ebola Response Team.** NEJM 2014: incubation,
   serial interval, CFR from case data. Picture: a figure from the paper
   (CC licence check; otherwise a redrawn version). Sources
   `research-history.md` section 2.

COVID-19, richer and specific, drawing on the 2023 IISA post
(`seabbs.github.io/_posts/2023-01-04-iisa-...`), the 40 minute composable
deck and the JuliaCon decks. Three or four slides:

6. **Early Wuhan estimates.** Abbott et al. 3 February 2020 and Hellewell
   et al. 2020. What we estimated, how, what happened.
7. **Real-time Rt for thousands of locations.** The dashboard figure.
   Method: EpiNow2. What happened: weekly to SPI-M-O, used by other
   governments directly or via their scientists. "We sometimes published
   nonsensical estimates" goes here, attributed to his 2022 post.
8. **What could not be done in time.** From the IISA post: variants,
   changing data, methods not reusable. This is where the JuliaCon
   composable deck's gap slides fit.
9. **The tools that came out of it.** The package timeline 2020 to 2026
   as the whole slide, no bullets. Title it for what it is, since it runs
   past COVID.

mpox 2022, two or three slides, one image each:

10. **What the outbreak was.** Global, sexual contact networks; Endo et al.
    2022 Science, heavy-tailed networks. Figure from that paper.
11. **Models from COVID could not be reused.** The composability-deck
    point. Figure from the 40 minute deck.
12. **Nowcasting for UKHSA.** Overton et al. 2023. UKHSA could not install
    other methods, so fell back on methods built on regression packages;
    state as his account unless the paper says it. No editorial, no Ward
    delays point.

Ebola disease caused by Bundibugyo virus, DRC 2026, two or three slides:

13. **The outbreak.** WHO alert 5 May, 17th DRC outbreak, PHEIC 17 May,
    counts as of DON617. The sitrep PDF page as the image.
14. **McCabe et al., and a replication the next day.** Their report of
    18 May, our replication in a few hours, then a joint renewal model
    across suspected, confirmed, deaths, exports and bed occupancy.
    The streams figure.
15. **Refit on every push.** Data pulled from the sitreps, multiple data
    sets, daily updates, 145 releases; no other regularly updated public
    model. Say only the LLM-free facts here; the agent story is section 3.

Then the modelling process, replacing "what a modeller does":

16. **How an outbreak gets modelled.** From the workflow paper
    (`a-workflow-for-infectious-disease-modelling`), tailored to
    outbreaks: question, data, model, fit, check, report, iterate. Not
    "delays first then renewal"; delays can sit in a joint model, and it
    need not be a renewal model. Renewal as one example if helpful.
    Figure: the workflow schematic. Cut the renewal slider slide.
17. **What keeps going wrong.** High level: methods not reused; methods
    not flexible enough to match the data sources; data sources changing
    over time; evaluation and understanding what works. No truncation
    focus.

## Section 2. Use of AI methods in outbreak modelling

Divider title: "Use of AI in past, present and future outbreak modelling".

18. **His view, alone on a slide, attributed to him.** Cleaned up: "Many
    of these approaches are under-explored and not well integrated with
    the rapidly evolving, noisy, sparse data settings I have worked in. I
    am not aware of any real-world operational use so far, and I am mostly
    not convinced by the evaluations."
19. **The map.** Kraemer et al. 2025 table with a row added for building
    and checking models, columns: Task, Kraemer et al., In this talk.
    The added row forward-links to section 3. No bullets about the hosts.
20. **Universal differential equations.** A schematic of a
    semi-mechanistic stochastic SEIR on the left and a UDE version
    ingesting many data sources on the right. Charlotte Holt,
    epiforecasts PhD student, UDEs to recover behavioural change to
    improve forecasts (verify her GitHub `charlotteholt` via epiforecasts
    membership; photo only if verified). Philipps et al. 2025 in the
    attribution. No "consistently hindered" line.
21. **Physics-informed neural networks.** Titled so. Also NN for fitting
    to many data sources. Refs and an image of what others are doing
    (Kharazmi 2021, Millevoi 2024, Rama 2026).
22. **Renewal as a neural network layer.** From the composable grants
    (`composable-workflow-grant/submission/research_vision.tex` and
    `eu-grant/ideas/vision.qmd`); schematic.
23. **AI-driven inference.** Normalising flows and simulation-based
    inference: OutbreakFlow 2021, Pinotti 2025, Jang 2026, with images of
    their figures where licensed. Cut the "non-identifiability" line.
24. **Foundation time series models.** Titled so. Kalahasti 2025, Wang,
    Li and Perra 2026, Jafari 2026, CAPE. One line: an outbreak-specific
    foundation model that handles data changing over time is a project he
    would like to be involved in.
25. **Reinforcement learning for control.** Libin et al. 2020, Reymond et
    al. 2024, the 2026 scoping review. As literature, not as what the
    hosts will present.
26. **"I am very excited about their potential."** Alone on a slide,
    attributed to him.

Each of 20 to 25 links back to a problem from slide 17 in one bullet.

## Section 3. Agentic AI and outbreak modelling

27. **What I mean by an agent.** Loop schematic. No "not an RL policy",
    no "write the task and what counts as right", no refs under the
    schematic. Build the diagram up across slides 27, 30 and 33: loop,
    then review and iteration loops, then the tree.
28. **How I work now.** "All code I have produced in the last six months
    has been agent written." Cut the review percentage, cut "git shows
    who wrote what". Bot avatars stay. Change "so decided to have a go" to
    a very focused go. Add: agents generate tasks from specs and
    conversations; review at different levels, sometimes all the code,
    sometimes the outcome, like working with students. Bot PRs per month
    figure.
29. **Agents in the Bundibugyo model: data.** Sitrep PDF ingestion with
    the PDF image, two blind reads, onset curve digitisation; and the
    nowcasting problem behind changing onsets, which is modelled.
30. **Agents in the Bundibugyo model: the model.** Model development,
    performance work (automated review for speed-ups), two versions of the
    model kept in sync by agents. Verify in the BVDOutbreakSize repo
    (`git log`, issues, `AGENTS.md`, `docs/`) before stating.
31. **What agents made possible.** Going wide: synthesis across many data
    streams and many checks and debugging that would not otherwise be
    possible, following the workflow (schematic from slide 16). Then
    the limits that still hold: agents did not choose the model or judge
    ascertainment; infrastructure and review still needed. Replaces
    "what does not change".
32. **Digitising from figures, and what went wrong.** SitRep 081 and 087,
    with the raster image. Replaces "what was hard to check".
33. **Agents that search over models.** Tree schematic, more tree-like.
    What we did for Ebola as an ad-hoc version; then
34. **Google SAI in the CDC hubs.** Own slide with image and facts:
    LLM-guided tree search, prospective 2025/26 result, Bracher and Funk
    2026 on the retrospective claim and the evaluation dangers, less
    epidemiological domain knowledge, non-agent infrastructure and review
    still needed.
35. **Who gets to do this.** Moved here from the communication deck.
    "I do not have a defence for this. I am part of the problem."

Cut: "Where does AI fit" section, "For the panel" slide, the two panel
questions. The "Community in the age of robots" slide moves to the
communication deck. End on slide 35 and the thank you.

That is 35 content slides, over budget. Merge 3 and 4 into one Ebola
slide only if needed; prefer cutting 21 or 25 to reach 30. Report what
was cut.
