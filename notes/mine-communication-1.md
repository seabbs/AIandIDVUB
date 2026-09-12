# Mine 1: communication lecture deck

Applied 2026-09-12 to the steer "heavily mine past presentations of mine
for images, complete slides and sections". Slide count unchanged at 21
content slides plus plan, iframe and close. Rendered with the sandbox off,
each changed slide screenshotted at 1920 by 1080 from the print layout and
checked by eye. `./scripts/lint.sh` clean. Nothing committed.

| Slide | Lifted | From | Replaced |
|---|---|---|---|
| 8 The limits travel less well | R packages table, "All of them are used by public health departments, including CDC, UKHSA, RKI, ECDC and WHO", "In many cases the package is too complex for anyone else to use" | JuliaCon2026 `roadmap/_partials/04-r.qmd` | Drawn schematic `comms-pipeline.png` |
| 9 Community as the channel | Emoji crowd and the robot bullets, "Nobody from outside the team has committed since February", "the other party on an issue is usually one of my robots. Answering a robot is dispiriting", "Do 🤖 shut down collaboration?" | JuliaCon2026 `roadmap/_partials/10-community.qmd` | Forum screenshot and the "too complex" bullet, which moved to slide 8 |
| 11 What I use it for | SitRep page `comms-bvd-insp-sitreps.png`; "I was travelling for summer schools, teaching and workshops, so decided to have a go with agents" | BVDOutbreakSize `slides/figures/insp_sitreps.png`; JuliaCon2026 `roadmap/_partials/05-what-it-takes.qmd` | Quote-only right column, brief now sits under the bullets; "The brief for this lecture is on the right" |
| 12 Making it visible | Disclosure on the WHO call limitations slide, "model and analysis drafted with an LLM under human oversight" | BVDOutbreakSize `slides/bdbv_collaboratory_20260610.qmd` | README-only disclosure bullet |
| 17 Provenance | "need to be able to trust it, and to see who is behind it" | JuliaCon2026 `roadmap/_partials/11-governance.qmd` | Nothing, added as a third bullet |
| 19 Who gets to do this | "🐋 Every project I have worked on has ended up with one person doing most of it", "Here the whale is me and a subscription", 🌍 line | JuliaCon2026 `roadmap/_partials/11-governance.qmd` | Two plain bullets |

The robot bullets were about EpiAware, so slide 9 names it as the Julia
successor before them. "Since February" carries his 2026-08-12 check in
the attribution and was not rechecked.

Considered and rejected:

- `bot-prs-by-month.png` from the roadmap deck. The current figure is the
  same figure extended to September with the same styling, and the
  bullets cite the September total. Attribution now names the source.
- "Before skynet" and "After skynet" as slides. The funding bullets are
  JuliaCon-specific. Only the travelling line was taken.
- hpru-ppie-kickoff respicast multi and ensemble figures for slide 5. The
  spec asks for the Sherratt et al. hub figure, which already comes from
  that deck's figures and carries the 83% and 91%.
- hpru-ppie-kickoff human forecasting challenge. No slide in the running
  order is about the public forecasting, and adding one would go over the
  count.
- The SitRep page on slide 18 in place of the digitiser schematic. The
  schematic carries the 20 versus 25 grid story; the SitRep now sits on
  slide 11 instead.
- "Governance, what do users want" as a whole slide. Only the trust line
  fits; the rest is about Julia reliability.
- nfidd forecast-evaluation and ensembles slides. Authored by Funk, Reich
  and Ray by the git log and figure credits, not his.
- how-to-serial-interval figures. All delay and censoring figures, nothing
  on communication.
- fellowships decks. Text only, no figures, and the packages line
  duplicates the roadmap table.

Left for Sam: `comms-pipeline.png` and its `pipeline()` function in
`scripts/comms-figures.py` are now unused, delete if not wanted. Slide 9
now reaches into 2026 inside the "Software is communication" section,
which was 2020 to 2023; move the robot bullets to section D if that jars.
