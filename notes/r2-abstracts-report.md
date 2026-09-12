# Report: round two abstracts and blurbs

Done 12 September 2026 on `round-2.md`. Touched: `index.qmd` card blurbs,
the four talk pages' abstracts and descriptions. Nothing committed.

## First two sentences, before and after

- Keynote. Before: "Infectious disease modelling has a long history, but
  the last ten years changed what it is asked to do during an outbreak and
  how fast. I open with that decade as I saw it." After: same first
  sentence, then "The first part is the outbreaks we worked on." 200 words,
  new order, "we" for the pandemic work, no later speakers named.
- Communication. Before: "During COVID-19 I communicated model outputs to
  three audiences. Government, through weekly estimates and reports..."
  After: "During COVID-19 we communicated...", same second sentence. Cut
  "I say what worked for each", "prose starts to sound the same", "what I
  would like us to agree on". Added other governments using the dashboard,
  the defaults line, evaluation as communication, bots filing issues on
  each other, and the closing question in his words.
- Exchange. Before: "I work at LSHTM, in CMMID, on real-time outbreak
  analysis, delay estimation and nowcasting, forecast evaluation, and the
  tools for doing them. I am part of the epiforecasts group led by
  Sebastian Funk." After: "I work at LSHTM, in CMMID. My research is on
  improving outbreak modelling through composable models, where components
  can be reused across contexts, and a workflow for modelling with multiple
  data sources." Then the groups, consulting, tools in outbreak response.
- Panel. First two unchanged; "have and have not" and "offered as a guess"
  cut from the rest.

## Three habits from his writing

1. The field's problem in the first sentence, no lead-in. "Delay
   distributions, the times between pairs of events such as symptom onset
   and laboratory confirmation, underpin infectious disease surveillance."
2. "We" plus a plain verb, then the consequence. "We instead marginalise
   over the latent primary event times, which converts the double interval
   censoring problem into a single interval censoring problem."
3. Limits stated flatly. "Yet not all available data was used." "Work
   remains to realise these potential benefits."

## For Sam

- Exchange abstract says tools are "used in outbreak response" without
  naming epidist in the DRC or Pegasus; the deck agent is verifying those.
  Out of scope and left: the communication "Around it" lines on what Poels
  and Algaba speak on, and the "The group" resources heading on exchange.

Checks: llmisms greps hit only content-bearing clauses and the bot bio;
lint clean; render clean (sandbox off) bar OJS warnings from the decks.
