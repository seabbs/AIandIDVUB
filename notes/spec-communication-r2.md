# Communication lecture, round two spec

From his notes of 12 September (`steers.md`, last long entry, second
half). His verdict: the quote format and images are good; "these are
better slides". Read `round-2.md`, `drafting-rules.md`, `style.md`,
`llmisms.md` first. This overrides `spec-communication.md` where they
differ.

Throughout: "we" for the pandemic work; short attributions; every quote
attributed to a named person in the text; images where they carry the
point, he can speak to them; no verbatim text needed to justify why a
thing is there. Content slides only count; about 30 at most for 30
minutes.

## Fixes

- There is a blank slide. Find it and remove it.
- "Other scientists" slide retitled "Collaborative forecasting hubs".
- Cut "I say what worked for each" and siblings.
- "In many cases the package is too complex" becomes "In some cases".
- Cut "What I use it for" (the keynote covers it) unless it carries the
  seabbs-review-bot slide below.
- Cut "prose that sounds the same" (he does not understand what it is
  getting at).
- "Who gets to do this" moves to the keynote (spec-keynote-r2.md, slide
  35); remove it here.
- The sitrep PDF picture belongs in the keynote; here only if a slide
  needs it.

## Section A. 2020, three audiences

- The Rt dashboard slides repeat the keynote. Do less on Rt and more on
  how results were presented: the map approach, epiforecasts.io/covid
  with a page per country and location, the use of caveats. Images from
  the live site or screenshots; `comms-shot-covid-*.png` exist.
- The public slide: other governments used the dashboard and its saved
  estimates directly or via scientists who summarised them alongside
  other evidence; the scale of checking was very hard; whether AI could
  help with that checking is a question to put.
- Two dashboard points that are currently under software move here: "the
  limits travel less well than the method", and "the limitations sat on a
  methods page that 20,000 of 1.2 million page views reached".
- "What went wrong" is great; keep.

## Section B. Software is communication

- First slide expands on why software is communication: users run the
  defaults, so the defaults are the advice; the package is the message
  that reaches the analyst; then the EpiNow2 defaults detail as now.
- A new slide on limitations in BVDOutbreakSize: the report opens with
  limitations in bullets; feedback was that this is off-putting; how we
  warn. Source `BVDOutbreakSize/README.md` and the docs. The LLM angle on
  it comes later in the deck.
- Evaluation as communication moves earlier, before AI, and expands: why
  it is communication, shared agreement and practice on evaluation, hubs
  and scoringutils as the tools. The community slide sits with it.

## Section C and D. AI and communication

He was lost by the AI-impact part; it needs more thought. What he does
want:

- Publishing prompts and steers, clear disclosure of AI usage: good, keep.
- A slide for seabbs-review-bot with its picture (GitHub avatar), what it
  does, how he acts on its reviews. Source `~/.claude/CLAUDE.md` "Review
  bot" section is his own description; `gh api users/seabbs-review-bot`
  (sandbox off if TLS fails).
- "Community in the age of robots" from the keynote moves here, with the
  emoji crowd.
- Bots talking to bots: seabbs-bot and sbfnk-bot on the same threads
  (search epiforecasts/BVDOutbreakSize and bdbv-linelist-analysis with
  `gh search issues` and `gh search prs`); issues filed on his repos by
  others' bots; issues his bots filed elsewhere. He does not like filing
  the latter and does not love receiving the former. One or two slides
  with a screenshot or short quoted exchange and URLs.
- The point he wants made: when the writer and the reader both have a
  language model, what is the person for? What value are you adding? Not
  a panel question; part of the AI-impact section. Cover people getting
  their information from LLMs: what do LLMs say about him and his work,
  and is it correct? Test it: ask two models about Sam Abbott and about
  EpiNow2 (use the Anthropic API via the claude-api skill if available,
  or record that this needs doing live) and screenshot or quote the
  answers with the errors marked. If you cannot run it, build the slide
  as a placeholder with the question and say so.
- Cut "What I would like us to agree on"; end on the value question and
  the thank you.
