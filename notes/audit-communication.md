# Audit: communication deck against his steers

Audited 13 September 2026, read only, against `notes/steers.md` in his words.
Files read in full: `communication/slides.qmd`, `communication/_partials/01-04`, `communication/index.qmd`, and the keynote partials for overlap.
`steers.md` holds no entry dated 13 September; the 13 September changes came through his direct keynote edits, which the r3 report says it propagated.
Nothing was rendered here, so "blank slide" is judged from source only.
Line references are `file:line` inside `communication/`.

## Point by point, in the order he made them

| His point | Status | Evidence | Fix |
|---|---|---|---|
| "Use we not our group or me" | done | `01-audiences.qmd:121` "beyond us", `:210` "asked us", `index.qmd:36` "we communicated"; "my group" and "our group" absent | None. |
| "Other govs ... used the dashboard and saved estimates either directly or via ... scientists ... Scale of checking was very hard ... AI help maybe?" | done | `01-audiences.qmd:115-122` "Other governments used it too", "Checking several thousand locations a day was beyond us", "Could AI do that checking?" | None. |
| "I say what worked for each ... AI filler sentence" | done | absent from deck and `index.qmd` (grep) | None. |
| "users use the defaults but we need to say that more clearly" | done | `02-software.qmd:12` "Users run the defaults, so the defaults are the advice"; `:41-42` "Every argument a user leaves alone is a decision they inherited from us" | None. |
| "second half needs to clearly bounce off and be different to the morning points not repeats" | partly | `04-under.qmd` is new material, but `03-with.qmd:37-38` repeats keynote `03-agents.qmd:25-27,43` (bot account, second login, created 23 January 2026); `01-audiences.qmd:148-149` and keynote `01-ten-years.qmd:150` both quote "nonsensical estimates" | Cut the bot-account bullet to a one-line pointer back to the morning and keep the nonsense quote in one deck only. |
| "seabbs-bot and sbfnk-bot communicating ... issues ... from others ... to others from my bots ... don't like doing the latter and don't love receiving the former" | done | `04-under.qmd:55-111`, `:93` "I do not like sending them. I do not love receiving them either" | None. |
| "end with what I would like us to agree on. not sure we need this" | done | `04-under.qmd:226-234` closes on "What is the person for?"; "agree on" absent | None. |
| "sensible number of slides ... title slides and subtitle slides don't need full time"; about 1.5 a minute | done | 24 content slides (9, 3, 5, 7 by section), 4 dividers, title, plan, thank you; 0.8 a minute for 30 minutes | None. |
| "vague and LLM weird titles"; titles that say the thing | partly | topic titles at `01-audiences.qmd:3` "Government", `02-software.qmd:68` "The epinowcast community", `03-with.qmd:33` "Making it visible", `:111` "seabbs-review-bot", `04-under.qmd:19` "Provenance" | Retitle each to its claim, for example "Government saw a range, not our estimates". |
| "overly full slides"; sparse slides, no bullet over two lines | partly | five-bullet slides at `01-audiences.qmd:62-70`, `02-software.qmd:38-45`, `03-with.qmd:115-123`, `04-under.qmd:117-125`, `:189-194`; three-line bullets at `01-audiences.qmd:9-11`, `:207-209`, `02-software.qmd:9-11`, `04-under.qmd:117-119` | Cut each to four bullets of two lines and let him speak the rest. |
| "image per slide" | done | every content slide carries a screenshot, figure, table, code block or a single quote | None. |
| "Some of the refs are way too long and over the top"; short attributions, no hedges | partly | quote lines are short (`01-audiences.qmd:19`); source blocks run five to eight lines at `02-software.qmd:24-30`, `:58-64`, `03-with.qmd:51-58`, `:130-135`, `04-under.qmd:101-109`, `:139-146`; `01-audiences.qmd:220` cites "the bmbr-guidance-grant project notes"; `03-with.qmd:133-134` adds the aside "the standing instructions my agents read" | Cut each source block to one line of links and drop the internal note and the aside. |
| "We don't need refs for schematics" | partly | `01-audiences.qmd:217-221` two-source attribution under the pairwise illustration | Keep the manuscript link only. |
| "Assign quotes to people in the text"; "No team named quote ... need attribution" | partly | every block quote names a person except `01-audiences.qmd:96-98`, attributed to "The figure captions, epiforecasts.io/covid" | Attribute to the dashboard authors by name or drop the quote and keep the bullet at `:92`. |
| "NO to these little sentences ... cut this one and similar"; no telling the audience what to think, no summarising | partly | `04-under.qmd:26` "The people we build for need to see who is behind it"; `:194` "To a reader who is not me it would sound right"; `02-software.qmd:76` "An attempt to communicate through software and the people around it"; `03-with.qmd:9-10` restates the caveats slide | Delete the four lines. |
| "Cut: Git shows who wrote what" | not done | `03-with.qmd:37-38` "so `git log` tells you who did most of it" is the same point | Cut the tail after "second GitHub login". |
| "No: ... About half went in unreviewed ... Cut review point" | contradicts another steer | `03-with.qmd:97-98` reuses the cut claim as a correction example, "'reviewed by me' became 'about half'" | His call: keep it as an example of checking, or replace with the "530 pull requests" example alone. |
| Acronyms in full on first use | partly | done for SPI-M-O, SAGE, WIS, UKHSA, CDC, ECDC, CRAN; not done for CSV `01-audiences.qmd:119`, WHO `02-software.qmd:11`, CFA `:62`, README `03-with.qmd:39`, API `:93`, "pull requests" used `:97` before its gloss `:117`, LLM in the heading `04-under.qmd:148` before "large language models" `:152`, ORCID `:190` | Expand each on first use and move the pull request gloss to `03-with.qmd:92`. |
| No LLM filler (llmisms greps) | done | see the greps section; no pattern fault in slide text | None. |
| "format of quotes is lovely here use of images is great" | done | italic name-and-year lines under each block quote kept | None. |
| "There is a blank slide" | done | no empty slide or `background-iframe` in source; r3 report says the render confirmed it; not re-rendered here | None. |
| "Rt stuff is ... a keynote repeat ... more on how we presented results i.e the map ... pages per country ... use of caveats" | done | `01-audiences.qmd:58-113` map, page per place, orange caveats; $R_t$ reduced to the gloss at `:7-8` | None. |
| "What went wrong is great" | done | `01-audiences.qmd:144-171` kept | None. |
| "Change this 'other scientists' to Collaborative forecasting hubs" | done | `01-audiences.qmd:173` | None. |
| "Software as not is communication. First slide should expand on this idea of why ... then ... epinow2 defaults" | partly | `02-software.qmd:7-8` gives one sentence of why, then a package table and who runs it; the defaults slide follows at `:34` | Add one or two bullets on why the package is the message before the table. |
| "This is really about the dashboard not software: the limits travel less well than the method" | not done | the line is absent from the deck; r3 report says it was cut as out of context; the idea survives only as `01-audiences.qmd:93-94` | Add the sentence to the caveats slide or accept the cut. |
| "In some cases: In many cases the package is too complex" | done | `02-software.qmd:13` "In some cases" | None. |
| "the limitations sat on a methods page that 20,000 of" is a dashboard point | done | `01-audiences.qmd:93-94` on the caveats slide | None. |
| "slide on lims for i.e bvdoutbreak top of report now in bullets feedback is that off putting llm point for later in the talk ... how we warn" | partly | slide at `03-with.qmd:3-31` with "How should we warn?" at `:12`; no later slide returns to warning with an LLM; the report returns at `04-under.qmd:19-53` on provenance only | Add the warning point to the LLM slides or the close, or cut the question. |
| "eval as communication needs to come earlier before we get into AI ... shared agreement practice on eval then ... tools" | done | `01-audiences.qmd:199-223` "Agreeing how to score is communication too", agreement, WIS, scoringutils, UKHSA | None. |
| "PDF picture for sitrep should be in the keynote" | done | "sitrep" absent from this deck | None. |
| "Not sure we need what i use it for as covered in earlier talk" | done | slide absent; but see the abstract row below | None here. |
| "Have a slide for seabbs-review-bot with picture" | done | `03-with.qmd:111-135` with the App page screenshot | None. |
| "the ai impact on com part lost me a bit ... needs more thought" | partly | section rebuilt at `04-under.qmd`; `:113-146` "Community, in the age of robots" never says it is about EpiAware and Julia, so "the team" `:117` and "not Julia developers" `:124` arrive cold | Add one bullet naming EpiAware, the Julia organisation, or cut the slide. |
| "publish prompts etc makes sense and is good clear on ai usage" | done | `03-with.qmd:33-86` | None. |
| "who gets to do this should be in keynote" | done | absent here; keynote `03-agents.qmd:318` | None. |
| "I don't understand what the prose that sounds the same slide is getting at" | done | absent | None. |
| "when the writer and the reader both have a language model, what is the person for? ... what value are you adding? ... not for the panel ... part of AI impact" | done | `04-under.qmd:226-234`, last content slide of Under AI, before Thank you | None. |
| "should cover people getting info from LLMs what do LLMs think about ... me and ... my work is it correct" | done | `04-under.qmd:148-224`; `:192` says both models saw his email, so the run is not clean | Rerun through the API before the talk if a clean answer matters. |
| Abstract and deck tell the same story in the same order | partly | sections 1 and 2 match `index.qmd:31-50`; `index.qmd:56` "I describe how I use coding agents" has no slide after the cut; `:55` "specific focus on agentic AI" while two Under AI slides are plain LLM answers; Bundibugyo, Checking what it wrote, review-bot, Provenance and Community have no abstract line | Reword `index.qmd:55-56` to bot account, review bot and provenance, and drop "how I use". |
| Talk plan matches the sections | partly | `slides.qmd:24-25` "With AI. A bot account, a prompt log, and a reviewer" omits the limitations slide that now opens that section | Add "limitations first" to the With AI bullet or move the slide. |

## Flow, read as a listener

Section 1 runs 2020 to 2022 in order and closes on the "Where it mattered" quote, which reads well.
Section 2 moves to the packages and the 2023 community without a jump.
The Bundibugyo limitations slide now sits at `03-with.qmd:3`, the first content slide after the "With AI" divider, per commit c41c9cb "the Bundibugyo limitations slide opens the second half".
The r3 report still places it after "What went wrong", and the r2 report placed it in Software, so the file has moved since the last report.
In its current place it does not read: the divider promises AI, the slide has no AI in it, its second bullet refers back to the dashboard two sections earlier, and "How should we warn?" is never answered.
The same report then returns at `04-under.qmd:19` "Provenance" in the next section with no link between the two slides.
The cleanest fix is to return it to Software after "Defaults are advice" as the r2 spec had it, or to keep it here and add the disclosure line so the AI link is on the slide.
"Community, in the age of robots" at `04-under.qmd:113` jumps to EpiAware and Julia without saying so, and "since February" has no year.
The two LLM slides and the close read well in sequence.

## llmisms greps

All eighteen greps were run over `communication/*.qmd` and `_partials/*.qmd`.
Pattern 2 hits are alt text at `03-with.qmd:23,76,128` and the attribution tail at `02-software.qmd:63` "and the CFA $R_t$ page's change of method", which is commentary and should go.
Pattern 5 hits are author lists, agency lists and the abstract's own "methods, assumptions and defaults"; not faults.
Pattern 8 hit `02-software.qmd:77` introduces a quote; not a fault.
Pattern 10 hit is the literal "Comprehensive R Archive Network"; not a fault.
Pattern 11 hit is the Talk plan slide, kept by house convention across all three decks.
Pattern 13 hits are "every analyst" from the abstract, "the first time" as fact, the title "Issues nobody asked for", and his own JuliaCon line; not faults.
Pattern 16 hit `04-under.qmd:62` "the thread" is literal.
Pattern 17 hits `index.qmd:6` and `slides.qmd:30` "and what the person is for" name the closing question; not faults.
No em dashes, no long lines, no trailing whitespace.
Faults the greps miss are in the table: the `git log` tail, the four telling sentences, and the long attributions.

## Counts

Done 25, partly 14, not done 2, contradicts another steer 1, of 42 points.

## The five most important gaps

1. The Bundibugyo limitations slide opens "With AI" with no AI content, and its "how we warn" LLM point never lands.
2. The abstract promises "how I use coding agents" and an agentic focus the deck no longer has, and the talk plan omits the limitations slide.
3. The second half still repeats the keynote's bot-account slide and the nonsense-estimates quote, and reuses the "about half unreviewed" point he cut from the keynote.
4. Source attributions of five to eight lines, an internal project note cited on a public slide, and unexpanded CSV, WHO, ORCID and API with "pull request" glossed after its first use.
5. "Community, in the age of robots" arrives without naming EpiAware, and five slides carry five bullets under topic titles such as "Government" and "Provenance".
