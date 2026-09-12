# Round 2: his notes from reading the site, made actionable

Source: `steers.md`, the two entries dated 12 September after the
collaborators steer. Read `drafting-rules.md`, `style.md` and `llmisms.md`
again before touching anything; he has asked for the reminder.

## Slide budget, for every deck

- Title, plan, section dividers, thank you and hidden fallbacks take no
  time. Count content slides only.
- About 1.5 content slides a minute is the ceiling, from his past decks.
  Keynote 25 minutes: at most about 30 content slides, fewer is fine.
  Lecture 30 minutes: at most about 35. Exchange 22 minutes: at most 25.
- Report the count of content slides and dividers separately.

## Voice, for every deck and page

- "We", not "our group" and not "me", for the pandemic work. It was not
  his group.
- No AI filler sentences. Two he named: "I say what worked for each" and
  "For some of these the answer at the moment may be nothing, and I would
  like to hear where the VUB and SIMID groups see it differently". Cut
  both and anything shaped like them.
- Do not say what later speakers will cover. We do not know. A slide on
  reinforcement learning or similar is fine.
- Writing samples to match, for the abstracts: the composable paper
  `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/index.qmd`,
  the primarycensored paper `/Users/lshsa2/code/epinowcast/primarycensored-paper`
  (or wherever the paper text is under `/Users/lshsa2/code/epinowcast/`),
  and the composable grants
  `/Users/lshsa2/code/epiforecasts/composable-workflow-grant/submission/`
  and `/Users/lshsa2/code/archive/composable-grant/`.

## Home page and talk pages

- Keynote blurb becomes, in substance: ten years of outbreak modelling,
  integration of AI and outbreak modelling, agentic AI and outbreak
  modelling. Use those three phrases.
- Exchange blurb and abstract: not "my group". He has collaborators and is
  attached to other groups and virtual groups (epiforecasts, CMMID, the
  epinowcast community, EpiAware).
- Abstracts: keep the substance, cut fluff such as "I open with the decade
  as I saw it", and tune the prose against the writing samples above.
  Prompts page is good; leave it.

## Keynote

New order, which he proposed and I accept:

1. Overview of outbreak modelling and the outbreaks, focused on work he
   was involved with. Sources beyond the current partials: the 2023 IISA
   post at `/Users/lshsa2/code/seabbs/seabbs.github.io/_posts/2023-01-04-iisa-data-models-and-modellers-during-a-global-pandemic/`
   (the pandemic years narrative), the case for composability decks at
   `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/presentations/{20min,40min}/`
   and the JuliaCon composable deck (the gap, chaining versus joint
   models). "Why am I so late" refers to that material; grep "late" in
   those decks.
2. AI methods and their use in outbreak settings. Use has been minimal, and
   say so. Each method links back to a point raised in section 1 (biased
   delays, chained models, slow to adapt, behaviour). Include a slide on
   reinforcement learning for control alongside UDEs, flows and foundation
   models. Add Charlotte Holt, epiforecasts PhD student, working on UDEs
   to recover behavioural change in outbreaks to improve forecasts; GitHub
   login appears to be `charlotteholt` (no name or bio on the profile, so
   verify it is her via epiforecasts org membership or a repo before using
   the photo; if unverifiable, name only).
3. Agentic AI and its potential. The current agents section, then the open
   question.

Remove any line that says what Abrams, Libin, the case studies, Poels or
Algaba will cover. Rewrite the plan slide and the home page blurb to match.

## Communication lecture

- The public slide: other governments used the dashboard and its saved
  estimates, directly or via scientists who summarised them alongside
  other evidence. The scale of checking was very hard. Whether AI could
  help with that checking is a question worth putting.
- Cut "I say what worked for each" and any sibling.
- Say the defaults point more clearly: users run the defaults, so the
  defaults are the advice.
- The second half (with AI, under AI) must bounce off the morning keynote
  and not repeat it. Material to mine: GitHub issues where seabbs-bot and
  sbfnk-bot talk to each other, issues filed on his repos by other people's
  bots, and issues his bots filed on other people's repos. He does not
  like filing the latter and does not love receiving the former. Use `gh`
  (sandbox off if TLS fails): `gh search issues --author seabbs-bot`,
  `gh search issues --commenter sbfnk-bot --author seabbs-bot`,
  `gh api search/issues -f q='org:epinowcast author:app/...'` and read a
  few threads. Quote sparingly, with URLs.
- The closing "What I would like us to agree on" may go. He is not sure he
  wants to force the discussion. Replace with a short close that puts one
  or two questions, or end on the last content slide and the thank you.

## Exchange

- Opener, professional not sad: a small group with little grant success,
  many collaborations, tools in wide use. Use of methods and software is
  not well linked to funding. Facts from `research-communication.md`
  section 3 and the package table.
- A slide on consulting and public health use: time consulting with US
  CDC collaborators, UKHSA, and state and local public health in the US;
  the aim to extend to other countries' public health departments; tools
  used in outbreaks, including recent epidist use by the DRC response team
  (verify in `/Users/lshsa2/code/epinowcast/epidist` issues or the BVD
  repo, else state as his report); the all-nation Pegasus pandemic
  preparedness exercise where multiple teams used various tools (verify
  what is written down locally, grep "Pegasus" under `~/code`; else state
  as his report); the aim to move to more flexible, extensible tools that
  are easy for LLMs to use.
- Cut "For some of these the answer at the moment may be nothing, and I
  would like to hear where the VUB and SIMID groups see it differently".
- "My group" nowhere.
