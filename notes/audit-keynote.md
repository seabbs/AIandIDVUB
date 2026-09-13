# Audit of the keynote deck against every steer

Audited 13 September 2026 at commit `3efb99e`, which landed during the audit and is the state reported here.
Sources: `steers.md` in full, `git show 02ca043`, the three k-reports, `spec-keynote-r2.md`, `round-2.md`, the three partials, `slides.qmd` and `index.qmd`.
Line numbers are for the partials as they stand after `3efb99e`.
Read only, apart from this file.

## Point by point, in the order he made them

| His point | Status | Evidence | Fix |
|---|---|---|---|
| Blurb: "10 years of outbreak modelling, integration of AI ... agentic AI" | done | `index.qmd:5-6` uses his three phrases | none |
| Order: outbreaks, then AI methods, then agentic AI | done | `slides.qmd:23-25`, dividers `01:1`, `02:1`, `03:1` | none |
| "Abstract is good but text a little AI" | partly | `index.qmd:31-32` "where real-time modelling arrived in public view" is the line he called "ick" on the slide | Cut "where real-time modelling arrived in public view" from the abstract. |
| "Use we not our group or me" | done | `01:112-119` "We started", "we were estimating"; no "our group" or "my group" in the deck | none |
| "we don't know what later speakers cover ... can include a slide on reinf" | done | RL slide `02:235`; no claim about hosts; `index.qmd:63-64` names the next speakers without saying what they cover | none |
| "the 10 mins on ai methods so link back to the points raised about outbreaks" | partly | UDE `02:64-65`, inference `02:160-161`, foundation `02:204-205` link back; PINN, renewal layer and RL slides do not | Add one bullet on each of `02:86`, `02:122`, `02:235` naming the section 1 problem it answers. |
| "charlotte holt get photo from github" | partly | named at `02:62-63`, no photo; k2 does not report verifying the login | Verify the `charlotteholt` login via epiforecasts membership and add the photo, or leave as name only and say so. |
| "sensible number of slides" | partly | 37 content slides for 25 minutes is 1.48 a minute, at the ceiling and above the spec's 28 to 30 | Cut or merge about seven content slides, see gaps below. |
| "Remove: , from West Africa to the DRC" | done | `slides.qmd:23` | none |
| "the other AI ... to Use of AI methods"; no "where does AI fit" bullet | done | `slides.qmd:24`; bullet absent | none |
| "250 years of outbreak models as a first slide then a second timeline ... timeline at top and short bullets below" | done | `01:3-42` | none |
| "we don't need watching in the title" | partly | title `01:44` clean; "Watched from a PhD" survives at `01:32` and as the label in `figures/keynote-timeline-ten-years.png` | Cut "Watched from a PhD on tuberculosis vaccination" from the bullet and the figure label; he can say it. |
| "No to real time modelling had arrived point ick" | partly | absent from the deck; present in `index.qmd:31-32` | As above. |
| "2 slides on this each with a pic cdc rojk on one and funk work on other" | not done | one slide `01:44-76` holds Meltzer and Funk with the Funk figure only; no CDC image | Split into a Meltzer slide with the MMWR projection figure and a Funk slide with the forecast panel. |
| "coherent points i.e what they estimated, method, what happened" | done | `01:48-57` gives all three for both studies | none |
| "Add a third for ebola response group WHO NEJM delay estimation" | done | `01:78-106` | none |
| "Some of the refs are way too long and over the top" | partly | `01:128-133` (repository creation date), `01:182-186` and `01:214-218` (release ids), `03:301-308` eight lines carrying facts, `01:266-267` names a plotting script | Cut attributions to author, year, venue or URL; move the Google SAI facts into bullets or drop them. |
| "Covid 19 pandemic doing it etc is too on the nose" | done | titles `01:108`, `01:138`, `01:169` | none |
| "lot of slides from elsewhere on covid ... could be richer/more specific" | partly | four COVID slides; the ONS cascade figure is lifted; no whole slide reused from the IISA post or the 40 minute deck | Lift one gap slide from the composable deck for the variants point. |
| "what came out of it slide ... could just be the timeline and not the bullets" | done | `01:200-212`, `01:275-287`, no bullets | none |
| "It goes up to 2026 though so its not really COVID" | done | split into 2020 to 2021 and 2022 to 2026 per his TODO | none |
| "Mpox slide also has a bad title" | done | `01:214` | none |
| "Doesn't have a bullet on what the mpox outbreak was" | done | `01:218-220` | none |
| "doesn't use the composability slide ideas i.e. models from covid couldn't be used" | partly | one bullet `01:226-227`; the spec's own slide with the 40 minute deck figure was not built | Add the composability slide or accept the bullet. |
| "doesn't include points about contact networks" | done | `01:221-225` | none |
| "UKHSA ... couldn't use other methods due to installation issues" | partly | `01:256-257` now states it as fact; `3efb99e` cut "As I recall it", which the spec kept because it is his recollection not the paper's | Restore a two-word hedge or confirm with him that the paper says it. |
| "Editorial point ... ward delays point does nothing" | done | absent | none |
| "a few slides for mpox ... image per slide" | partly | two slides, one image each | Add the composability slide above and it is three. |
| "DRC Ebola bad title doesn't explain early outbreak" | done | `01:289-315` | none |
| "doesn't capture mccabe and rep of it in a few hours" | done | `01:317-342`; repeated at `03:158-159` | Cut the repeat from `03:158-159`. |
| "pulling data from sitrep and automation multiple datasets no other regularly update public models" | done | `01:344-370` | none |
| "What a modeller does is a bit superficial ... look at a workflow for infectious disease" | done | `01:405-427`, delays sit in the joint model, renewal not assumed | none |
| "The renewal process by hand slide adds nothing" | done | no `{ojs}` or slider in the deck | none |
| "focus on truncation is a bit shit ... High level lack of reuse ..." | done | `01:429-453` his four points | none |
| "we sometimes publish nonsensical could go in the covid reflection" | done | `01:150` attributed | none |
| "We don't need not and RL policy blah bullet in what is an agent" | done | `03:7-8` | none |
| "This point means nothing: write the task and what counts as right" | partly | bullet gone; `figures/keynote-agent-1.png` still says "You, the task, and what counts as right", alt `03:12` | Relabel the left box in `scripts/keynote-agent-figures.py` to "You, a prompt" and redraw. |
| "We don't need refs for schematics in this talk" | partly | loop `03:11-18` has none; tree `03:271-274` still carries a source line | Delete `03:271-274`. |
| "agentic loop diagram misses the agent review and iteration loops ... build it up" | done | agent-1, agent-2 `03:138-142`, agent-3 | none |
| "so decided to have a go" to "a very focussed go" | done | `03:24-25` | none |
| "All code I have produced ... agent written. Cut review point" | done | `03:26-27` his line | none |
| "Cut: Git shows who wrote what" | done | absent | none |
| "use agents to generate tasks from specs and conversations. Review at different levels" | done | `03:28-30`; he cut "like working with students" himself in `02ca043` | none |
| "We don't need copied from Julia.onc.. blah" | done | no "from my ... deck" or "as used in" left after `3efb99e` | none |
| "we can use more lang etc from them" (JuliaCon decks) | partly | Endo and ONS figures lifted; no wording traceable to the JuliaCon decks | Lift the gap and chaining wording from the composable deck for `01:169`. |
| "For the bvdoutbreak we already intro'd that so here we talk about the LLM agent usage" | done | `03:94-185` | none |
| "a few slides on this data ingestion process, onset digitisation" | done | `03:94-121`, `03:187-214` | none |
| "Model dev, model performance dev ... two versions kept in sync. Review the repo" | done | `03:123-152`, PR #155 cited | none |
| "agents let us go wide ... Need to ref the modelling workflow ... include that workflow" | done | `03:154-185`, workflow figure with agent tags | none |
| "Not to what as hard to check ... Digitising from figures" | done | `03:187` | none |
| "image of the sitrep PDF on the sitrep digitisation slide" | done | `03:109` page 3, `03:201` the raster | none |
| "Onsets changing aren't just a digitisation thing ... nowcasting problem" | contradicts another steer | he deleted this bullet in `02ca043` and wrote a Julia and Python cross-check bullet instead; `3efb99e` reversed both, `03:105-106` | Put back to him: his 12 September note wants the nowcasting bullet, his 13 September edit removed it. |
| "own slide for agent use with images ... dangers ... bracher funk ... infra still needed" | done | `03:278-311` | none |
| "Schematic for the tree idea could be more tree like ... ebola ad-hoc then google" | done | `03:249-311`; `keynote-agent-3.png` is a tree | none |
| "What does not change slide doesn't make sense ... before this agent tree" | done | replaced by `03:154`, before `03:249` | none |
| "community in the age of robots ... communication talk" | done | absent from the keynote | none |
| "Not the other AI. use of AI in past, present and future outbreak modelling" | done | `02:1` | none |
| "Open with the kramer table with the addition of the build and checking and forward link" | done | `keynote-map.png` has the brick row "Building and checking the model, agentic AI, the third part of this talk"; slide `02:37` follows his three added slides | none |
| "Don't try and guess the hosts ... no need for the bullets" | done | `02:37-46` no bullets | none |
| "table task, Kramer et al., In this talk as columns" | done | figure header row | none |
| "Udes should be a slide title ... semi mech random seir model and a ude version" | done | `02:48`, figure `02:68-72` | none |
| "just call it PINNs and then have another one for AI driven inference refs and images of what others are doing" | partly | titles `02:86`, `02:154`; inference has the OutbreakFlow figure; PINN has a drawn schematic, not others' work | Swap or add a figure from Kharazmi 2021 or Millevoi 2024 on the PINN slide. |
| "Non-identifiability comes from the simulator" | done | absent | none |
| "no to forecast without a mech.. Foundation time series models" | done | `02:190` | none |
| "Assign quotes to people in the text" | done | `01:150`, `02:23-24`, `02:231-233`, `03:320-321`; the "Predictive models" quote is gone | none |
| "my view ... after the subtitle slide before the table, then I am very excited" | done | `02:14-35` in the order he set in `02ca043` | none |
| "Not sure the where does AI fit is adding anything" | done | absent | none |
| "Remove: For the panel / Which of this is ours / Name something" | done | absent | none |
| "NO to these little sentences: I am part of it cut" | done | `03:315-317` | none |
| Commit: "Found that they were...." | done | `01:55-57` from Funk et al. 2019 | none |
| Commit: "TODO get the ref in properly" (Park 2024) | done | `01:85-86`, `01:101-102` | none |
| Commit: "TODO: Is this a forecast from there model?" | done | `01:87-88` labelled their forecast, 14,383 credited to CDC MMWR `01:103` | none |
| Commit: "Software widely used" and "In 2022 I wrote:" | done | `01:148-150` | none |
| Commit: "tools from the pandemic, then tools after" | done | `01:200`, `01:275` | none |
| Commit: mpox "more than one bullet point ... pheic in full ... don't need who highest alert" | done | `01:218-220` | none |
| Commit: Endo "depletion of high risk ... behaviour change ... heavy tailed" | done | `01:223-225`, Murayama et al. 2024 cited | none |
| Commit: "Nowcasting for UKHSA TODO spell out" | done | `01:247` | none |
| Commit: "What even is AI?" list | done | `02:3-12` verbatim, no image, "claude code" lower case as typed | Confirm he wants it as a slide rather than a note; capitalise Claude Code. |
| Commit: UDE "define what a UDE is ... flag limitations ... link to their paper" | done | `02:52-61` | none |
| Commit: PINN outline of six items | done | `02:86-120` covers all six | none |
| Commit: renewal "advantages vs PINN", "clean up schematic no need to focus on grads" | done | `02:132-133`; figure has no gradient arrows | none |
| Commit: his deletion of the grant attribution under the renewal schematic | contradicts another steer | k2 restored a one-line version, now `02:146` | Delete `02:146` as he did. |
| Commit: foundation "What kind of model? TODO", prospective question, "make this a quote" | done | `02:195-196`, `02:204-205`, `02:226-233` | none |
| Commit: RL "TODO: What is it", "how does it differ from JUMP", question left in | done | `02:239-244`; JuMP itself no longer named after `3efb99e` | none |
| Commit: RL title "(I don't know anything about this)" | done | `02:235`, 83 characters | Ask whether the parenthetical is for the room or a note to self. |
| Commit: "Agents building methods into software" outline, question "don't try to answer" | done | `03:62-92`, question kept at `03:69-70` | none |
| Commit: "model model" typo | done | `03:94` | none |
| Commit: "Bayesian workflow TODO: Needs two refs" | done | `03:180-182` | none |
| Commit: "TODO another slide on what went wrong ... Need a picture" | done | `03:216-247` with `keynote-agent-wrong.png` | none |
| Commit: "TODO check it topped the leaderboard" | done | `03:286-287`; k3 read page 4, first of 43, 12 and 4 | none |
| Commit: "What happens when the VC funding dries up" | done | `03:327` | none |
| General: sparse slides | partly | no slide overflows 1080 px, but 13 content slides carry five or six bullets and four sit above 1000 px (mpox 1031, data 1036, what else 1017, Google SAI 1045) | Cut each five or six bullet slide to four. |
| General: one image per slide | partly | `01:44` shares one figure between two studies; `02:3` has none | See the Ebola split. |
| General: acronyms in full on first use | partly | PHEIC and BVD first appear unexpanded at `01:19-20`; UKHSA at `01:35` before `01:247`; SEIR at `02:167` never expanded; INRB-UMIE `03:100`; SAI `03:278` | Expand each at first use or drop it from the attribution. |
| General: quotes attributed in the text | done | as above | none |
| General: no LLM filler, no telling the audience what to think | done | the named sentences are gone; `01:89` "The models on the following slides lean on delay estimates like these" is a structure announcement he kept | none |
| General: titles say the thing | done | all bar the RL parenthetical | none |
| General: no statement of what later speakers cover | done | none in deck or abstract | none |
| General: abstract and deck tell the same story in the same order | partly | order matches; `index.qmd:42-43` lists UDEs, flows, foundation models and RL but not PINNs or the renewal layer; abstract omits how he works, the software slide, Google SAI and who gets to do this | Add PINNs and the renewal layer to the abstract's list and one clause on the Google search and access. |
| General: past decks mined | done | Endo figure, ONS cascade, bot PR chart, streams figure lifted | none |

## Numbers

Every number on a slide traces to `research-history.md`, `research-agentic.md` or a k-report, with these exceptions.
The incubation mean of 11.4 days and serial interval mean of 15.3 days in the delays figure and its alt text (`01:93-96`) are not in any note.
They match the NEJM paper but should be recorded in `research-history.md`.
"Software widely used by researchers and public health agencies worldwide" (`01:148-149`) is his line and carries no number.

## Reading it as a listener

"The tools since, 2022 to 2026" (`01:275`) shows the BVDOutbreakSize lollipop before the outbreak is introduced at `01:289`.
The McCabe replication in a few hours is said at `01:325` and again at `03:158-159`.
Section 2 opens with three text slides before any figure, and ends on the bolded negative finding of the RL review rather than on "I am very excited".
"Agents building methods into software" (`03:62`) sits between his working pattern and the Bundibugyo data slide with nothing to bridge the jump from general software to the outbreak.
The foundation model quote sits under two columns of five bullets (`02:226-233`), so the slide carries two ideas.

## llmisms greps

Zero hits for point-stamp, moral, negative parallelism, overclaimed identity, persuasive adjectives, room flattery, hedges, benefit tail, structural metaphor and maxim.
Bolted-on clause: three hits, all alt text or attribution, not faults.
Rule of three: about thirty hits, all author lists, alt text or data lists; `03:24` "summer schools, teaching and workshops" is his own line.
Colon gloss: `01:150`, his quote line.
Metadiscourse: "## Talk plan" (`slides.qmd:19`), a free slide.
Absolutes: 17 hits; `03:26` is his line, `03:99`, `03:160` and `03:198` are repo README claims, `01:162` is verified by the release count.
Promise tail: `03:187` "Digitising from figures, and what went wrong" is the exact shape he cuts.
Fix: retitle to "Digitising the onset curve".

## Render

`quarto render keynote/slides.qmd` needed the sandbox off ("unrecognized architecture") and completed with zero fenced-div warnings.
The rendered deck has 43 slides: title, talk plan, 3 dividers, 37 content slides and thank you.
The hidden static fallback is dropped from the HTML as intended.
No slide exceeds 1080 px at 1920 by 1080; tallest is Google SAI at 1045.
`./scripts/lint.sh` is clean; the RL heading at `02:235` is 83 characters and exempt as a heading.

## Counts

Done 73, partly 20, not done 1, contradicts another steer 2.

## The five most important gaps

1. Ebola West Africa is one slide with one figure where he asked for two, a CDC picture on one and Funk on the other.
2. Thirty-seven content slides sit at the 1.5 a minute ceiling, and thirteen carry five or six bullets, which is the "overly full" he complained of.
3. Two of his 13 September decisions were reversed without asking: the nowcasting bullet replaced his cross-check bullet, and the grant attribution he deleted came back; the UKHSA hedge was also cut.
4. The agent loop figure still says "the task, and what counts as right" and the tree schematic still carries a source line, both things he said to remove.
5. The abstract keeps "where real-time modelling arrived in public view" and does not list PINNs or the renewal layer, so it and the deck do not tell the same story.
