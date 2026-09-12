# Report: formal prompts and abstracts

Done 12 September 2026 on the steer to make the prompts more formal and less
confusing, and the abstracts more formal but steered by what the organisers
said. Nothing committed.

## What changed

- `prompts.qmd`. Same structure. Every prompt and steer rewritten as full
  first-person sentences, spelling and grammar fixed, one judgement per
  sentence, nothing added or dropped in substance. Two bracketed entries
  mark what Sam forwarded rather than said. The two latest steers are in.
  The intro and "How it was built" say an agent rewrote these on his steer.
- `keynote/index.qmd`. Bulleted brief replaced by a 205 word abstract: the
  ten years of outbreaks, agents and the other AI on a shared map, the open
  question. Organisers' ask kept in prose below it.
- `communication/index.qmd`. 214 word abstract: three audiences in 2020,
  software as a fourth channel, with and under AI, what he would like us
  to agree on. Organisers' ask below.
- `panel/index.qmd`. Heading "The panel", three sentences on the panel and
  what he brings, his guess marked as a guess. Organisers' ask below.
- `exchange/index.qmd`. 214 word abstract: him, CMMID, epiforecasts led by
  Sebastian Funk, the epinowcast community, then composable modelling,
  delays and the workflow with AI as questions. Organisers' ask below,
  including that there is no theme.
- `index.qmd`. Only the exchange card blurb changed, adding the group intro.

## Judgement calls

- "not clear cross over is i.e realtime modelling" became "The cross-over
  is not clear-cut, but it is real-time modelling and evaluating it",
  keeping his hedge. "CMMID ..." kept as the fragment.
- Abstracts carry no counts. Each claim traces to `proposal.md` or the
  research notes. "Note that you can use less powerful agents" lost its
  "Note that" opener.

Checks: `quarto render` clean (sandbox off); `scripts/lint.sh` clean for
these six files, failing only on `keynote/_partials/03-agents.qmd:68`,
another agent's file; the `llmisms.md` greps hit only his wording and lists.
