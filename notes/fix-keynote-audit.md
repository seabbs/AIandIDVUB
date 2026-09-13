# Acting on the keynote audit

Worked 13 September 2026 from `notes/audit-keynote.md`, against the deck at
`e6962b5`.
Changed `keynote/_partials/*.qmd` and `scripts/keynote-schematics.py`, and
redrew `figures/keynote-agent-1.png`.
Not committed.
Line numbers are for the files as they now stand.

## A. Reversals of his own edits, undone

### The sitrep data slide, his Julia and Python cross-check bullet

`03-agents.qmd:104-105`.
In `02ca043` he deleted the nowcasting bullet and wrote:

> These are cross checked again using multiple agents and using digistiers
> written in both Python and Julia.

`3efb99e` deleted that and put the nowcasting bullet back.
His bullet is restored as "These are cross-checked again by several agents,
and by digitisers written in both Python and Julia".

The nowcasting point is kept as well, at `03:106-107`, because it is also his
(12 September note) and the brief said not to cut bullets for density.
It no longer displaces his line, and its bolted-on tail is gone: "That is a
nowcasting problem, and it is in the model" is now "That nowcasting problem is
in the model".

### The grant attribution under the renewal-layer schematic

`02-ai-methods.qmd:145-149`.
He deleted three lines of grant attribution in `02ca043`.
A later commit restored a one-line version, "The composable modelling grant,
Abbott, Funk et al. 2026".
Deleted again.
The attribution is now Samuel Brand's repository and Pervez et al. 2024.

### Other lines of his that later commits overwrote

I checked every line he added or changed in `02ca043` against the current
files.
Two more are not as he left them.

1. `02-ai-methods.qmd:75`. He wrote "Rackauckas et al. 2020c"; it now reads
   "Rackauckas et al. 2020".
   Left as 2020, because there is no 2020a or 2020b in the deck for the
   suffix to distinguish, so it reads as a stray citekey letter.
   Say the word and I will put the c back.
2. `03-agents.qmd:167-168`. His sentence "The workflow is what kept it
   reviewable" was dropped when three of his sentences were merged into one
   bullet.
   His other two sentences on that bullet survive.
   Left out, as it is a moral tacked on the end of the bullet, but it is his
   line and it is your call.

Everything else of his survives, including the "What even is AI?" list, the
"My view" and "And yet" quote slides in his order, the RL title parenthetical,
all the TODO answers, and "Who gets to do this".

## B. Mechanical fixes

### The agent loop figure

`scripts/keynote-schematics.py:451`, in `agent_1()`.
The left box read "You / the task, and what counts as right".
It now reads "You, a prompt".
The arrow's separate italic "a prompt" label was removed, since the box now
carries the words.
`figures/keynote-agent-1.png` redrawn; alt text at `03-agents.qmd:12-15`
matches.

Note: the figure lives in `keynote-schematics.py`, not
`keynote-agent-figures.py` as the brief said.
`keynote-agent-figures.py` only draws `keynote-agent-wrong.png`.

### Source line under the tree schematic

Deleted, at what was `03-agents.qmd:271-274`.
The loop and tree schematics now both carry no attribution.

### Over-long attributions, cut to author, year, venue or URL

| Slide | File | Was | Now |
|---|---|---|---|
| Early Wuhan estimates | `01:154-157` | four lines ending "EpiNow repository created 15 March 2020" | figure credit, Hellewell et al., the blog post |
| Refit on every push | `01:388-390` | three lines with `results-43` to `results-1699` | "[BVDOutbreakSize], live · release counts from the GitHub API, 11 September 2026" |
| Refit on every push, hidden fallback | `01:419-421` | four lines with the same release ids | release and date, then the API |
| What keeps going wrong | `01:468-470` | named `data/onset_curve_scanned.csv` and `scripts/keynote-onset-vintages.py` | "[BVDOutbreakSize], read 11 September 2026" |
| Google tree search | `03:297-302` | eight lines carrying facts | three authors-and-URL lines |

Two facts from the Google attribution moved into bullets rather than being
dropped: "142 prompts in three families" onto `03:279-280`, and the ranking
"first of 43 eligible FluSight, 12 COVID-19 and 4 RSV submissions" onto
`03:281-283`.

### Acronyms

| Acronym | Where | What I did |
|---|---|---|
| PHEIC | `01:19-20`, the first-slide attribution | dropped from the attribution; the timeline entries are now "mpox, WHO, 23 July 2022" and "Bundibugyo virus, [WHO DON602], 17 May 2026". First body use, `01:242-243` on the mpox slide, already spells it out, and `01:319` follows it |
| BVD | same attribution | gone with the above. Only `BVDOutbreakSize`, a repository name, is left |
| UKHSA | `01:35` | expanded to "the UK Health Security Agency (UKHSA)" at first use. The later title and bullets can now use the short form |
| SEIR | `02:166` | "an SEIR model, SIR plus an exposed class". SIR itself is spelled out on the UDE slide, which comes first |
| INRB-UMIE | `03:99`, `03:119` | dropped from the bullet, which now reads "Where a public transcription has the same series". Kept in the attribution as a source name. I could not verify what UMIE stands for, and neither could the earlier research pass (`notes/k3-report.md:21`) |
| SAI | `03:272` | dropped from the title, which is now "Google's tree search topped the CDC forecast hubs". The team folders `Google_SAI-*` stay in the attribution |

### Retitle

`03-agents.qmd:186`.
"Digitising from figures, and what went wrong" is now "Digitising the onset
curve".
The promise tail is the shape you cut.

### The duplicate McCabe replication

Section 1 keeps it, at `01:347` ("We replicated it on 19 May, in a few
hours").
Section 3's repeat at `03:158-159` is gone.
Your following sentence survives, merged into one bullet at `03:159-160`:
"Issues with the McCabe et al. Imperial College report were addressed, and
every stream they had used was fitted jointly".
This is the one place where I cut a line you wrote in `02ca043`, because the
brief was explicit that the repeat goes and the section 1 version stays.

## C. The UKHSA installation bullet

Left as fact at `01:280-281`, with no hedge, as instructed.

The cited paper does support it.
Overton, Abbott et al. 2023, PLOS Computational Biology, says the permissions
needed on the managed IT systems UKHSA used for the mpox data meant Bayesian
nowcasting packages could not be used, and that generalised additive models
in `mgcv` were chosen because they were easy to implement and efficient to
run, with computational tractability and reliability vital to delivering
weekly.

So the claim is the paper's, not only your recollection.
The one word that is not quite the paper's is "install": the paper gives
permissions on a managed system as the reason.
If you want it exact, "UKHSA could not run Bayesian nowcasting packages on the
systems holding the data" is what the paper says.

## Checks

`quarto render keynote/slides.qmd` completes with no warnings.
`./scripts/lint.sh` is clean.

## Left for you

- Whether "Rackauckas et al. 2020c" should keep its c (`02:75`).
- Whether "The workflow is what kept it reviewable" should come back
  (`03:167`).
- The centre italic "a language model with tools" in `keynote-agent-1.png`
  overlaps the "Write or change code" box. This predates my change and the
  label comes from `inner_loop()`, which `keynote-agent-2.png` also uses, so
  fixing it moves two figures. Out of the scope I was given.
- Everything else in the audit that was not in my scope: slide count and
  density, the Ebola figure split, the abstract line "where real-time
  modelling arrived in public view", the Charlotte Holt photo, and
  "Watched from a PhD on tuberculosis vaccination".
