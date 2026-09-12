# Spec: research exchange, Tuesday 15 September 2026

09:45–10:15 at the AI Experience Centre, Pleinlaan 9, Brussels.
Present for 20 to 25 minutes, questions after.
10 to 15 people onsite from the VUB AI group (reinforcement learning,
bandits, fairness, individual-based simulators) and the UHasselt and
UAntwerp SIMID group (statistical and mechanistic modelling), plus people
online over Teams.
Details in `exchange-programme.md`.

## His steer, verbatim apart from spelling

> I might like 20 minutes on composable EpiAware modelling and potential
> links to AI approaches as they might think of them, i.e. using
> composition, UDEs, PINNs, maybe nothing doing there at the moment. Ten on
> recent delays work and epidist, less clear AI cross links. Maybe five on
> the workflow and where AI sits. Not sure. Review and come up with a first
> version after cross review.

That is 35 minutes for a 20 to 25 minute slot.
Build for 22 minutes: composable 12, delays 6, workflow and AI 4.
Say in your report what you cut to get there.

## Running order

Retitle the deck. Working title: "Composable infectious disease
modelling, and where AI might plug in". Update `slides.qmd` title, the
plan bullets, the partials list, and `index.qmd` subtitle and description
to match.

1. Plan and QR (exists).
2. **Who I am and what the group does.** One slide. Real-time outbreak
   analysis, delays and nowcasting, evaluation, tools. The timeline strip
   from the keynote if it exists in `figures/`, else a one-line list.
3. **Composable EpiAware modelling** (12 minutes, about 9 slides).
   Source: `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/presentations/40min/index.qmd`
   is canonical and his voice; the JuliaCon composable deck at
   `/Users/lshsa2/code/seabbs/JuliaCon2026/composable/` is the 15 minute
   cut he corrected, so its wording is safe. Remix, do not rewrite.
   The gap (timely, rigorous, collaborative), chaining versus joint
   models, what composable means, the two approaches from
   https://epiaware.org/approaches/ (composable Turing models, composed
   distributions) with a code example each, one replication figure, and
   the design considerations compressed to the three that matter here.
   Then **where AI might plug in**, two slides: a neural network as a
   component (UDEs, PINNs) with the Philipps et al. 2025 caveats and his
   line "maybe nothing doing there at the moment" as the honest status;
   agents building and checking components, with the BVDOutbreakSize
   facts from `research-agentic.md`. Frame as questions to this room.
4. **Recent delays work** (6 minutes, about 4 slides). primarycensored,
   epidist, CensoredDistributions.jl. Source: the JuliaCon delays deck
   `/Users/lshsa2/code/seabbs/JuliaCon2026/delays/` and its figures
   (`delays-double-censoring.png`, `delays-right-truncation.png`,
   `delays-fit.png`). What an epidemiological delay is, the two biases,
   the software, and one line on where AI could help (learned delay
   distributions? amortised inference?) marked as his uncertainty.
5. **The workflow, and where AI sits** (4 minutes, 2 slides). The
   workflow schematic (`JuliaCon2026/figures/workflow-schematic.png`),
   which stages agents do and which stay with people, from
   `research-agentic.md` section 1.
6. Thank you and QR (exists).

## Pictures and interactives

Reuse the JuliaCon and 40 minute deck figures; copy into `figures/` with
the `exchange-` prefix. One interactive at most; the composed
distribution or the renewal `{ojs}` slider if the keynote made one.

## Sources

`research-ai-methods.md` A2, A3, B3 for UDEs and PINNs;
`research-agentic.md` for agents and BVDOutbreakSize;
`research-workshop.md` section 2 for what this room works on;
`/Users/lshsa2/code/seabbs/JuliaCon2026/notes/spec-composable.md` and
`notes/style-juliacon.md` here for what he cut from the composable deck.

## Update, 12 September: no theme, so introduce the group

The organiser confirmed there is no theme; each group introduces itself
and shares some work.
His steer, spelling normalised:

> Our day 2 needs a bit on my epinowcast org and seminar (loose forum,
> users, Clara and Fanny organising the seminar), epiforecasts led by Seb
> Funk which I am associated with, the cross-over is real-time modelling
> and evaluating it. CMMID ...

Expand "Who I am and what the group does" from one slide to three, and
take the two minutes from the composable section:

1. **Me.** LSHTM, CMMID. Real-time outbreak analysis, delays and
   nowcasting, evaluation, tools. The timeline strip.
2. **epiforecasts.** Led by Sebastian Funk; I am part of it. The shared
   ground is real-time modelling and evaluating it. Name the packages
   (EpiNow2, scoringutils, epinowcast) and the hubs. Source:
   `research-communication.md` section 3, `research-history.md` section 1.
3. **epinowcast, the community.** Packages, a loose forum with users, a
   monthly seminar organised by Clara and Fanny. Verify their surnames
   and roles from `/Users/lshsa2/code/epinowcast/epinowcast.github.io`
   (seminars, meetings, or team pages) before putting them on a slide;
   if not verifiable, first names only as he gave them. Counts from
   `research-communication.md` section 3 (31 seminars since May 2023,
   over 50 members per grant text). His lines "community >> methods or
   models alone" and "too complex for anyone else to use" are available.

New budget: who and group 4, composable 10, delays 5, workflow and AI 3,
total 22.
