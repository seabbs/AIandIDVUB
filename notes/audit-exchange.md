# Audit: exchange deck against his steers

Audited 13 September 2026 against `notes/steers.md` (no 13 September entries exist there) and his keynote edits in `02ca043`.
Read `exchange/slides.qmd`, all six partials and `exchange/index.qmd` in full.
Status is what the source shows, not what the round reports claim.
Line references are to `exchange/_partials/` unless a path is given.

| His point | Status | Evidence | Fix |
|---|---|---|---|
| "20 mins on composable EpiAware modelling and potential links to AI ... composition, UDEs, PINNs" | partly | `02-composable.qmd` has 5 slides, `03-ai.qmd` 4; UDEs and PINNs share one bullet at `03-ai.qmd:24-26` | Add the UDE definition and PINN slide his keynote edit asked for, and give composable at least the design considerations slide back. |
| "10 on recent delays work and i.e. epidist, less clear AI cross links" | partly | `05-delays.qmd` has 4 counted slides; epidist is one bullet at 200-201; the AI line is at 205-206 | Give epidist and the DRC use a slide or accept the cut and say so. |
| "5 workflow chat and where AI sits" | done | `04-agentic.qmd` 4 slides, workflow figure at 5 | None. |
| Organiser: "an introduction of your work and group" | done | `01-who.qmd:1-170`, five slides | None. |
| "epinowcast org and seminar (loose forum, users, Clara and Fanny organising)" | partly | `01-who.qmd:144-147` names "Clara Brigitta and Fanny Bergström"; no hit for either surname anywhere in `~/code/epinowcast/epinowcast.github.io`, which `spec-exchange.md:99-101` said to check before use | Verify the surnames with him or revert to first names as he gave them. |
| "epiforecasts led by Seb Funk which I am associated with" | partly | `01-who.qmd:138-139` fine; `index.qmd:34` says "I work in the epiforecasts group" | Change the abstract to "associated with" or "part of". |
| "CMMID" | done | `01-who.qmd:5-6` in full | None. |
| "heavily mine past presentations for images, complete slides and sections" | done | ONS cascade, structure figure and EpiNow2 replication from the 40 minute deck (`02-composable.qmd:21,45,190`); delays figures and divider from JuliaCon (`05-delays.qmd:29,43`); RespiCast from the HPRU deck (`01-who.qmd:159`) | None. |
| "a slide with collaborators ... organised in some logical way" | done | `01b-people.qmd` three grids by kind of work | None. |
| "Group is small due to lack of funding success is maybe an opener ... professional and not sad" | done | `01-who.qmd:7-12` "A small group", "Tools in wide use. The use has not turned into funding" | None, though the last clause is the closest to sad and he should read it. |
| "Use we not our group or me" | done | No "my group" or "our group" in `exchange/`; "me" only for his own code at `01b-people.qmd:23`, `04-agentic.qmd:21` | None. |
| "time consulting with US CDC collabs, UKHSA, state and local PH ... epidist use by the DRC response team ... Pegasus multiple teams used various tools ... easy for LLM to use tools" | partly | `01-who.qmd:98-110` covers each; but 107 "Several teams used the tools in Exercise Pegasus" claims his tools, while the only written source (his os4ls grant, per `r2-exchange-report.md:40`) says "Epiverse tools" and he said "various tools" | Reword to "various tools, including ours" or drop "the tools". |
| "AI fluff sentence: For some of these the answer at the moment may be nothing" | done | Absent from `exchange/` | None. |
| "sensible number of slides ... title slides and subtitle slides don't need full time" | done | 25 content slides, 6 dividers, 1 uncounted, plus plan and thank you | None. |
| "vague and LLM weird titles" | partly | `04-agentic.qmd:3` "Being able to follow a workflow" names nothing; the rest say the thing | Retitle to "A workflow for infectious disease modelling". |
| "overly full slides" | not done | `02-composable.qmd:165-198` four dense bullets, a callout, two figures and a four line attribution; `03-ai.qmd:96` and `04-agentic.qmd:87` need `.smaller` to fit; `01-who.qmd:1-38` bullets plus photo plus six row table | Cut each to three or four bullets and one figure, drop `.smaller`. |
| "image per slide" | partly | `05-delays.qmd:169` code only; `02-composable.qmd:165` two figures; his headshot appears on four slides (`01-who.qmd:14`, `02-composable.qmd:102,155`, grid a) | One figure on the EpiNow2 slide, drop the repeated headshots. |
| "Some of the refs are way too long and over the top" | not done | `01-who.qmd:124-130` six sources; `03-ai.qmd:112-118` six sources; `01-who.qmd:150-156` five sources plus a second attribution block | Keep one or two sources per slide. |
| "We don't need refs for schematics in this talk" | not done | "Drawn for this talk, `scripts/...`" at `03-ai.qmd:54,91,137`, `04-agentic.qmd:45,124`, `01-who.qmd:64`; process notes at `01b-people.qmd:36`, `03-ai.qmd:40`, `01-who.qmd:18-19`, `02-composable.qmd:90` | Delete every script, grep, notes and "read 2026-..." provenance line. |
| "Assign quotes to people in the text not in asides" | done | `03-ai.qmd:13`, `03-ai.qmd:130-133`, `01-who.qmd:148` | None. |
| "I am very excited about their potential on a slide after that again alone" | partly | `03-ai.qmd:16-18` is a fragment on the "My view" slide; his `02ca043` keynote edit made "And yet" its own slide | Split into a second slide as in the keynote. |
| "UDEs should be a slide title ... traditional semi-mech SEIR model and a UDE version ingesting lots of data sources" and `02ca043` "actually define what a UDE is" | partly | `03-ai.qmd:20` titled "A neural network as a component?"; UDE defined in one clause at 24-26; schematic is renewal not SEIR | Title it UDEs, define it in a sentence, keep the renewal schematic if he prefers. |
| `02ca043` new PINN slide ("What they are, diagram, epi uses, limitations") | not done | PINN is one word at `03-ai.qmd:24-25` and one bullet at 65 | Add a PINN slide or say the keynote carries it. |
| "Not to forecast without a mech.. Foundation time series models" | done | `03-ai.qmd:96` | None. |
| "NO to these little sentences: I am part of it cut this one and similar" | partly | Deck clean; `index.qmd:38-39` "I am part of the EpiAware organisation"; `r3-exchange-report.md` calls the page out of scope | Cut or rephrase in the abstract. |
| "Every project I have worked on ... the whale is me and a subscription cut" | done | Absent | None. |
| "Who I work with, at LSHTM and epiforecasts isn't super accurate" | done | `01b-people.qmd:3,21,40` grouped by work | None. |
| "Who I am is missing the meta focus on composability, outbreak modelling improvements and workflow ... more than one slide on research interests" | done | `01-who.qmd:67-96` three bold leads; `01-who.qmd:40-53` outbreaks | None. |
| "Who I work with in Julia no Jason Asher ... look at JuliaBayes org" | done | `01b-people.qmd:48-53` no Asher; JuliaBayes API today lists BJMCox, gdalle, nsiccha, penelopeysm, PTWaade, rsenne, simonsteiger; six shown, `nsiccha` omitted for having no name; EpiAware members Brand, Bayer, DeWitt, Funk all present | Ask him whether Nikolas Siccha belongs on the grid. |
| "Cut: Maybe nothing doing there at the moment" | done | Absent | None. |
| "Reinforcement learning and bandits on individual-based simulators ... environment" | done | Absent | None. |
| "the network consistently hindered parameter id ... Could also use nn for fitting to lots of data sources i.e pinn like stuff" | done | `03-ai.qmd:29-30` observation side network | None. |
| "Renewal as a nn layer should have a slide I think see the composable grants" | partly | Slide at `03-ai.qmd:61-94` in his keynote wording; attribution 77-78 still cites "the 2026 Wellcome Discovery application", which `02ca043` deleted from the keynote | Drop the grant self-citation. |
| "Agentic modelling workflows is the next one I think" | done | `04-agentic.qmd` follows `03-ai.qmd` | None. |
| "Not to this: Each line I have drawn between the two columns has moved within months" | done | Absent | None. |
| "the workflow slides section is actually quite good so maybe we remove that earlier and don't dup in the bit about bvdoutbreak" | partly | `04-agentic.qmd:5` shows the nine stages, `04-agentic.qmd:34` shows the same nine stages again as the split; 22 and 64-65 both make the "people judged, review still needed" point | Merge slides 1 and 2 of the section, or drop the repeated bullet. |
| "Should have the agentic tree search as a slide from the keynote" | partly | `04-agentic.qmd:87-127` present; his `02ca043` additions "embedded inference step (MCMC proposal in model space)", "how to enforce domain knowledge" and the compute and person power gap are absent | Add those three lines from the keynote. |
| "outbreak specific foundation model as a project I would love to be involved in ... changing data over time" | done | `03-ai.qmd:96-140`, quote at 130-133 | None. |
| `02ca043` "What even is AI?" | not done | AI section opens on "My view" at `03-ai.qmd:3` with no definition of what counts as AI | Add the list slide before "My view" or accept the omission the round 3 report chose. |
| `02ca043` "Agents building methods into software" (EpiAware two approaches, epidist meta-analysis model in days, epidelays porting, analytic integrals) | not done | `04-agentic.qmd` covers the DRC model only, in a deck whose main section is composable software | Add the slide; it is the most relevant of his keynote additions to this deck. |
| `02ca043` "another slide on what went wrong" and earlier "something on dangers i.e. eval cite the Bracher Funk paper" | partly | Bracher and Funk at `04-agentic.qmd:100-101`; no agent failure slide | Add one slide on forecast bugs, AD performance and odd observation model proposals. |
| `02ca043` "Model structure and approaches specified by me at a high level", "review still needed to keep the agents in check" | done | `04-agentic.qmd:20-21,64-65` | None. |
| Acronyms in full on first use | partly | CMMID, CDC, UKHSA, DRC, ONS, ECDC, UDE, PINN, AR, LLM, RSV, CDF done; SPI-M-O glossed not expanded `01-who.qmd:43`; ARIMA `02-composable.qmd:169` and CRAN `01-who.qmd:23` not expanded | Expand ARIMA and CRAN or drop them. |
| No LLM filler (`llmisms.md` greps) | done | All 18 greps run; no faults; "Talk plan" appears in six of his own decks; the double integral line is his SI wording; one candidate benefit tail at `05-delays.qmd:199` "so it reads like `dgamma`" | Cut that tail. |
| The abstract and the deck telling the same story | partly | `index.qmd:44-55` orders composable, delays, workflow and promises an AI question per strand including delays; deck runs composable, AI, agentic, delays with one delays bullet | Reorder the abstract to match and soften the per strand promise. |
| About 1.5 content slides a minute for 20 to 25 minutes | done | 25 content slides, 1.0 to 1.25 a minute | None. |
| His 20 / 10 / 5 split | contradicts another steer | Intro and people 8 slides, composable 5, AI 4, agentic 4, delays 4; the "bit" on the group is now the largest block and composable the smallest he asked for | Cut the intro to five slides and return two to composable. |
| Slides in the wrong place, read as a listener | partly | `01-who.qmd:40` argues for composability then three intro slides intervene before `02-composable.qmd`; `01-who.qmd:134` introduces epiforecasts after `01-who.qmd:98` shows its tools in use; the deck ends at `05-delays.qmd:205` on "Less clear where AI plugs in here" | Move the outbreaks slide to open the composable section, move the groups slide before the tools slide, end on a foundation model or thank you line. |

## Counts

Done 24, partly 17, not done 6, contradicts another steer 1.

## Five most important gaps

1. Provenance and long attributions on about ten slides, against two explicit steers and the pattern of his own keynote edits.
2. Overfull slides, two of them only fitting with `.smaller`.
3. The time split has inverted, with the group intro at 8 slides and composable at 5.
4. His keynote content for this deck is not propagated: "Agents building methods into software", a PINN slide, a UDE definition, "What even is AI?", and the tree search additions.
5. Unverified names and claims on the intro slides: the seminar organisers' surnames, "the tools" in Exercise Pegasus, and "I work in the epiforecasts group" on the page.
