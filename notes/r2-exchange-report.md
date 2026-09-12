# Exchange, round two report

Applied `spec-exchange-r2.md` to `exchange/`. Nothing committed. Renders,
lint clean, llmisms greps run, every slide screenshotted at 1920x1080.

## Running order

24 content slides, 6 dividers, plus title, plan, thank you and one
uncounted fallback. 33 counted sections.

| Section | Content | Slides |
|---|---:|---|
| Who I am | 5 | Who I am (opener, package table); Three outbreaks, the same problems (timeline); Joint models from reusable parts (workflow paper figure 6); Where the tools get used (drawn table); epiforecasts and the epinowcast community |
| Who I work with (divider) | 3 | Real-time tools and the hubs; Delays and nowcasting; The Julia composable work |
| Composable (divider) | 5 | ONS cascade; What is composable; two code slides; EpiNow2 replication |
| Where AI might plug in (divider) | 3 | A neural network as a component (now with the many-streams network); Renewal as a neural network layer; An outbreak-specific foundation model |
| Agentic modelling workflows (divider) | 4 | Workflow schematic; Where the agents sat on the DRC model; Agents building and checking the parts; Agents that search over models |
| Recent delays work (two dividers) | 4 | Delay; both events censored; truncation slider (fallback uncounted); Three packages, one likelihood |

## Added and cut

Added: research-interest slides 2 to 4, renewal layer, foundation model,
tree search, three regrouped grids. New figures in
`scripts/exchange-schematics.py`; `exchange-nn-component.py` gained the
observation-side network; the Lego figure is the workflow paper's figure 6.

Cut whole slides: "Timely, rigorous, and collaborative evidence" (Whitty),
the separate "epiforecasts" slide (merged into the community slide). Cut
lines: "I am part of it", the whale, "Maybe nothing doing", RL and bandits,
"consistently hindered", "moved within months", the VUB and SIMID sentence,
the Philipps quote, the NEJM line on the packages slide (moved to slide 4).

## Verification

- epidist in the DRC. No epidist issue mentions the DRC or a response
  team. Crossref: the NEJM correspondence (doi 10.1056/NEJMc2608070,
  6 August 2026) is by Akilimali et al., INSP and INRB Kinshasa with
  Northeastern and Oxford. That it used epidist rests on his JuliaCon 2026
  delays deck, not on the paper itself. Stated as INSP and INRB use.
- Pegasus. Written down once, in his os4ls grant text: "Epiverse tools were
  used in Exercise Pegasus, the 2025 national pandemic exercise". The bmbr
  outline cites it as personal communication. "Several teams" is his
  account and the attribution says so, as does the US state and local line.
- Julia group. JuliaBayes members via the API: BJMCox, gdalle, nsiccha,
  penelopeysm, PTWaade, rsenne, seabbs, simonsteiger; org created 7 April
  2026; its Turing.jl is a fork, so the slide says "tools around Turing.jl".
  EpiAware members: damonbayer, medewitt, SamuelBrand1, sbfnk, seabbs.
  Jason Asher removed. nsiccha left out (no name on GitHub or in any
  Project.toml). Hong Ge is not a JuliaBayes member; included as Turing
  lead and paper co-author.

## For Sam

- "One small internal grant held as principal investigator" is from the
  fellowship decks. "The use has not turned into funding" is your steer.
  Consulting with US state and local public health has no written source.
- The tree search slide says the DRC search was by hand with agents writing
  variants; check that matches what happened.
- Penelope Yong and Jessica Cox have non-photo avatars, so tiles.
