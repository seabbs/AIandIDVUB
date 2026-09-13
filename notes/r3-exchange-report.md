# Exchange, round three report

His 12 September exchange notes, checked point by point against the deck, and his 13 September keynote edits (`02ca043`) propagated. Nothing committed. Renders clean apart from the pre-existing OJS line-number warning, lint clean, llmisms greps clean, every slide screenshotted at 1920x1080 with no overflow.

## His feedback points

| Point | Status |
|---|---|
| No "I am part of it" and similar little sentences | Done in r2, checked. Only the abstract on `index.qmd` says "I am part of", and that file was out of scope |
| No whale line | Done in r2, checked |
| "Who I work with, at LSHTM and epiforecasts" not accurate | Done in r2, regrouped by work; kept |
| Who I am missing the meta focus; more than one research slide | Done now. New "What I work on" slide with bold leads for composability, improving outbreak modelling and the multi-source workflow, replacing "Joint models from reusable parts". Opener, outbreaks timeline, tools in use and community slides carry the rest |
| Julia group, no Jason Asher, check JuliaBayes | Done in r2, checked |
| Cut "Maybe nothing doing" | Done in r2, checked |
| Cut RL and bandits line | Done in r2, checked |
| Cut "consistently hindered", keep schematic, add NN for many data sources | Done in r2; slide now also carries his "most exciting where many hard to model data sets" line |
| Renewal as a NN layer slide | Done in r2; now in his keynote wording, see below |
| Agentic modelling workflows next | Done in r2, order kept |
| Cut "moved within months" | Done in r2, checked |
| Workflow slides earlier, no duplication in the BVD part | Done in r2; BVD slide now carries his keynote facts instead |
| Tree search slide from the keynote | Done in r2; rewritten to his keynote wording |
| Outbreak foundation model as a project | Done in r2; his line now a highlighted quote per his keynote TODO |
| Cut the VUB and SIMID sentence | Done in r2, checked |
| Consulting, epidist in the DRC, Pegasus, LLM-friendly tools | Done in r2; bullets split and bold leads added |
| Opener: small group, little funding, professional | Done in r2; kept |
| epinowcast seminar organisers | Not done in r2. Now names Clara Brigitta and Fanny Bergström |
| No "my group" | None in the deck |
| Sensible slide count | 25 content slides |

## Propagated from his keynote edits

- "My view" quote slide opens the AI section, with "And yet. I am very excited about their potential." as a fragment on the same slide. "What even is AI?" left out to hold the slide budget; add if wanted.
- Renewal layer slide uses his bullets: specialised PINN, autoregressive transformation, can be thought of as a layer, stacked with other layers, "Not seen this used in research yet. Proposed in Samuel Brand's RenewalExamples repository" (repo verified to exist; the layer idea is his statement, not found in its README). Schematic no longer mentions gradients. His advantages-versus-ODE-PINN TODO is unresolved in the keynote, so not added.
- Tree search: his ad hoc versus systematic framing, "matched or beat" the hub ensembles (the arXiv abstract says "consistently matched or outperformed"; "topped" dropped per his TODO), "earlier claimed" gain, mutates and composes existing models, hubs, data, target and review still people's work.
- Foundation model: "how do these methods hold up when data change" and the project line as a quote with his name.
- BVD slide: McCabe replication over a few hours, five streams plus exports and a genomic bound, two blind reads, digitiser cross-checked in a second language, checks on every rebuild, infrastructure and review still needed.
- Style: acronyms spelt out on first use (CMMID, CDC, UKHSA, DRC, ONS, ECDC, NEJM, UDE, PINN, AR, LLM, RSV, CDF), bold lead words, compact bullets split, quotes in quotation marks with his name ("community >> methods or models alone", IISA 2023 post).
- Timeline figure replaced by the keynote's centuries version, dropping the "watching" and "doing it" labels he objected to.
- The tree search and foundation model slides use revealjs `.smaller` to fit at 1080 without cutting his facts.

## Counts

25 content slides, 6 dividers, plus title, plan, thank you and one uncounted fallback. 34 counted sections. New script `scripts/exchange-shots.py` walks fragments and uncounted slides.
