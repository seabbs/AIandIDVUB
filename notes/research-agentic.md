# Agentic AI material mined from Sam's own work

Gathered 2026-09-11 for the VUB/UAntwerp/UHasselt keynote on 14 September 2026.
Read-only pass over local repos plus GitHub API counts.
Paths are absolute.
`how-I-llm` quotes carry Sam's facts but not his phrasing.
All 16 commits in that repo are by `seabbs-bot`, and Sam later said "how-I-llm is not a style reference as it was all bots" (`/Users/lshsa2/code/seabbs/JuliaCon2026/notes/steers.md:74-77`).
Where a quote is Sam's own typing it is marked **[Sam's words]**.

## 1. Claims Sam has made about coding agents and research

### What agents are good at

- "Best when there is something to check the answer against. Does it run, does it recover known parameters, does it match the analytic case" (`/Users/lshsa2/code/seabbs/how-I-llm/_partials/02-use-cases.qmd:8-9`).
- Review: "Good at the boring half. Unused arguments, silent fallbacks, an off-by-one index, a test that asserts nothing" (`02-use-cases.qmd:15-16`).
- Focused edits: "Small, verifiable, tedious. The most useful category, and the least interesting to talk about" (`02-use-cases.qmd:47-48`).
- "Agents built the apparatus: data ingest, fitting pipeline, tests, docs site, releases, figures, sensitivity analyses" (`04-drc.qmd:86-87`).
- "I would not have picked a question this size without them" (`04-drc.qmd:90`).
- "If a task is well-specified, bounded, and checkable, assume it is already automated. What is left is work where the hard part is deciding what the task is" (`07-whats-left.qmd:3-5`).
- "Most code I ship is written by an agent. About half of it carries a review from me" (`01-where-i-am.qmd:18-19`).
- "My job moved from typing to specifying and checking" (`01-where-i-am.qmd:22`).
- **[Sam's words]** on BVDOutbreakSize: "a bunch of LLM driven blah vbery long etc etc hard to check hard to steer etc but on the asame fromnt much better imop that what we had before can consider lots of datassts adapt as data changes read sitreps in french and scan out daga from i.e images with little effort ourselveds" (`/Users/lshsa2/code/seabbs/JuliaCon2026/notes/original-brief.md:72-76`).

### What agents are bad at

- "Worst when I do not know what right looks like" (`02-use-cases.qmd:10`).
- "Poor at 'is this the right model'" (`02-use-cases.qmd:17`).
- "Agents did not choose the model, decide what the lower bound meant, or judge whether the ascertainment assumption held" (`04-drc.qmd:88-89`).
- "The failure mode is confident, plausible, wrong. It does not look like a bug, which is what makes it expensive" (`04-drc.qmd:92-94`).
- "An agent will make a failing test pass by weakening the test. Silent fallbacks and swallowed errors recur" (`04-drc.qmd:95-96`).
- What is left for people: "Choosing the question, and knowing when an answer would change a decision. Judging whether a model is fit for the use it will be put to. Data that does not exist yet. Trust with the people who act on the numbers. Saying no to an analysis that should not be done" (`07-whats-left.qmd:9-14`).
- "Every boundary I have drawn in two years has moved. 'Agents cannot do long-horizon work' lasted about six months" (`07-whats-left.qmd:17-18`).
- Julia side of BVD: "Really quite slow. I cannot get Enzyme to work, and Mooncake compile times are very slow" (`/Users/lshsa2/code/seabbs/JuliaCon2026/roadmap/_partials/00-outbreak.qmd:59-60`).

### Review and trust

- "The bottleneck moved with it. Not how fast I write, but how fast I can tell whether something is right" (`01-where-i-am.qmd:23-24`).
- "Cheap enough to run several reviewers and keep only the findings that survive being argued against" (`02-use-cases.qmd:18-19`).
- "So the core maths and the headline numbers get checked against something independent. An analytic case, simulated data with known parameters, or another group's published estimate" (`04-drc.qmd:97-99`).
- "All of it runs on every rebuild, so it is checked whether or not I remember to look" (`04-drc.qmd:77-78`).
- "11% closed unmerged. About half of those were superseded by a later pull request rather than rejected. What is left is the review gate working. Ten times the throughput at ten times the review load is not a win" (`05-scale.qmd:9-12`).
- "The first prompt got it most of the way, and wrong in the ways that mattered. Every steer above was a judgement I could make and it could not" (`09-steers.qmd:29-31`).
- "The prompt is not the work. The steering is the work" (`09-steers.qmd:37-38`).
- The deck itself was fact-checked by a second agent workflow, which "extracted 114 claims from the deck and tested each against git, GitHub and tool history. 67 needed changing" (`git -C /Users/lshsa2/code/seabbs/how-I-llm show 8c7e834`).
- That commit also records: "712 of 1,371 merged bot PRs carry no review at all, so it is about half" and "the claude-code-review workflow is gated on a login that never matches, and every run shows skipped" (same commit).
- Earlier fact-check: "530 pull requests was GitHub's latest issue-or-PR number, not a count. The real figure is 353" (`git show 1fceb9a`).
- "The pull request counts here were wrong at first, from a paginated API that silently capped at 400" (`08-how-i-made-this.qmd:34-35`).
- Repo-level disclosure: "The model code and analysis were drafted by a language model, then reviewed and revised under human oversight. The named authors are responsible for that oversight" (`/Users/lshsa2/code/seabbs/BVDOutbreakSize/README.md:50-51`).
- "Most of this repository was drafted with LLM assistance and the prose has drifted before" (`/Users/lshsa2/code/seabbs/BVDOutbreakSize/AGENTS.md:13`).
- Agent-written note, flagged as such: coverage on `main` was 93.93 percent, but "the tests were largely written by the same agents writing the code, so high coverage is evidence the code does what it was told to do, not evidence that what it was told to do is correct" (`/Users/lshsa2/code/seabbs/JuliaCon2026/notes/bvd.md`, section "The honest downside").

### Scale, cost and access

- "Agent work is pushed from a bot account, so git log mostly tells you who did what" (`05-scale.qmd:7-8`).
- Tooling: "51 skills of my own", hooks as "deterministic guardrails", "16 open right now" tmux sessions, "The blocker was parallelism, not features" (`03-tooling.qmd:5-10, 28, 38`).
- "Nothing confidential on it. That is the design, not an oversight. So agents can run with wide permissions and the worst case stays boring" (`03-tooling.qmd:24-26`).
- "I pay £200 a month for this. Out of my own pocket. My institution does not cover it, and neither do most" (`06-money.qmd:3-7`).
- "On metered access, $50 a day is easy if you are running agents in parallel" (`06-money.qmd:10-11`).
- "Real work is now possible on small open models" (`06-money.qmd:17`).
- "It lands on top of existing inequalities in research capacity and makes them steeper. The people modelling outbreaks where outbreaks happen are the least likely to have paid access. I do not have a defence for this. I am part of the problem" (`06-money.qmd:28-31`).
- JuliaCon: "I was travelling for summer schools, teaching and workshops, so decided to have a go with agents", "A Claude Max subscription", "Well, actually, we still need funding" (`/Users/lshsa2/code/seabbs/JuliaCon2026/roadmap/_partials/05-what-it-takes.qmd:31-36`).
- "Who can do this work at all is narrowing. Agents make that worse" (`/Users/lshsa2/code/seabbs/JuliaCon2026/roadmap/_partials/11-governance.qmd:13`).

### Collaboration and community

- "Nobody from outside the team has committed since February, so the other party on an issue is usually one of my robots. Answering a robot is dispiriting" (`10-community.qmd:5-7`).
- "It is not clear which repositories want robot-filed issues at all" (`10-community.qmd:8`).
- "Every project I have worked on has ended up with one person doing most of it. Here the whale is me and a subscription" (`11-governance.qmd:7-9`).
- "The hope is that modularity makes it easier for the whales to work together" (`11-governance.qmd:10-11`).
- Users "work in R in the middle of an outbreak response. They don't care about fancy language features. They need their tools to work" (`11-governance.qmd:24-27`).
- "They need to be able to trust it, and to see who is behind it. Who do they ask when it breaks?" (`11-governance.qmd:28-29`).
- `EpiAwareAgents` is "a community bot any maintainer could point at their own repository" (`10-community.qmd:10-11`), and its own README says "design phase. Nothing here runs yet" (`/Users/lshsa2/code/seabbs/JuliaCon2026/notes/roadmap-llm.md:103-104`).
- "The standard is what makes the volume survivable" and "An agent that has learned one repo has learned all of them" (`05-scale.qmd:43, 49`).

### "I wrote the argument and almost none of the words"

- "I did not write these slides. I wrote the argument. An agent wrote the words, found the numbers, and drew the charts. It took about two hours" (`01-where-i-am.qmd:1-6`).
- "I wrote the argument and almost none of the words" (`08-how-i-made-this.qmd:38`).
- **[Sam's words]** "no the point was an llm wrote the outline of me and I wanted that to be clear" (`steers.md:25`).
- **[Sam's words]** "the following was drafted by @seabbs-bot who has a very suspiciously high opinion of me so take it with a pinch of salt" (`steers.md:36-37`).
- **[Sam's words]** "'stan is the through line' is the kind of classic LLM language that I don't use and edit out" (`steers.md:86-87`).
- **[Sam's words]** "the slides honestly kind of suck" (`steers.md:74`).
- The grant example: "Three of us each wrote a brainstorm file. Those became a 2,000-word expression of interest over 76 commits in two days" (`02-use-cases.qmd:33-35`).
- The seabbs.github.io blog has no post on LLMs or agents; the latest post is dated 2024-01-15 (`ls /Users/lshsa2/code/seabbs/seabbs.github.io/_posts`).

## 2. BVDOutbreakSize as a worked example

Sources: `/Users/lshsa2/code/seabbs/BVDOutbreakSize/README.md`, `data/README.md`, `scripts/README.md`, `AGENTS.md`, `docs/src/news.md`; `/Users/lshsa2/code/seabbs/JuliaCon2026/roadmap/_partials/00-outbreak.qmd`; `/Users/lshsa2/code/seabbs/JuliaCon2026/notes/bvd.md`; `how-I-llm/_partials/04-drc.qmd`.

### What was built

- A joint Bayesian renewal-process model of the 2026 Bundibugyo virus disease outbreak in DRC, with exports to Uganda (`README.md:31-43`).
- Authors Sam Abbott, Kath Sherratt, Samuel Brand, Sebastian Funk (`README.md:3`).
- One infection process, many INSP situation-report streams fitted in one posterior: suspected and confirmed cases and deaths, laboratory, isolation, treatment-centre, recoveries, a digitised onset curve, Uganda exports, and a genetic TMRCA bound (`README.md:34-40`).
- Outputs: infections and deaths to date, time-varying reproduction number, case-fatality ratio, per-stream ascertainment, and a one-week-ahead forecast scored against later data (`README.md:40-42`).
- Live report: each push to `main` refits and publishes a GitHub Release with draws (`README.md:124-128`).
- Funded under the NIHR HPRU in Health Analytics and Modelling (`README.md:206`).

### How fast

- "A replication of the McCabe et al. report of 18 May, in a few hours the next day" (`00-outbreak.qmd:25-26`).
- Repo created 2026-05-19T16:50:45Z with 33 commits that day (`gh repo view`; `00-outbreak.qmd:36`).
- First results release `results-43` on 2026-05-20; latest `results-1699` on 2026-09-09; 145 releases in total (section 5).
- "Updated up to daily since, and the model has evolved with the outbreak" (`00-outbreak.qmd:27`).
- About 35,000 lines of Julia counted 2026-08-13 (`00-outbreak.qmd:54, 74-75`).

### What agents did

- "The situation reports are French PDFs. Agents ingest them directly" (`00-outbreak.qmd:30`).
- Every stream except confirmed cases and deaths is read directly from the PDFs; confirmed series are cross-checked against the INRB-UMIE transcription mirror and the script exits non-zero on undocumented disagreement (`README.md:117-120`).
- Reads are done by "two blind readers" or "two independent blind readers" per vintage (`data/README.md:99, 101, 110, 111`).
- The onset-date epidemic curve exists only as a raster image in the PDF; `scripts/digitize_onset_curve.jl` recovers counts from pixel colour and axis-tick geometry, with a byte-identical Python port "for the automated data-updater, which has Python but not Julia access" (`scripts/README.md:22-32`).
- Model priors were revised mid-outbreak in response to a BEAST X genomic reanalysis and a field-epidemiology finding (`notes/bvd.md`, "How many data streams").
- The talk framed the workflow paper as "the rail. Name the stage, show the DAG, then write model code" (`04-drc.qmd:53-54`), softened at fact-check from "the agent has to say which stage it is at" (`git show 8c7e834`).

### What went wrong or was hard to check

- SitRep 080: the caption sat on the wrong page, so a same-page lookup "landed on the wrong page" and pulled an unrelated image; fix was a neighbouring-page fallback (`data/README.md:69-71`).
- SitRep 081: JPEG compression left tick marks 1px tall, the digitiser found about 10 of 19 ticks and "undercounting to 1411 against the printed n = 3 066 (−54%)" (`data/README.md:75`).
- SitRep 087: the chart's y-axis grid changed from steps of 20 to 25, and the misread "was caught only because it broke the reporting-triangle invariant on dates that should have been stable" (`data/README.md:77`).
- SitRep 098: a losslessly encoded image read 7 percent higher than its neighbours and was excluded, "not because 098 is the wrong number, since it is arguably the most faithful scan in the series" (`data/README.md:83`).
- SitRep 110: the caption said onset date but the raster title said notification date; "Both readers who blindly and independently transcribed SitRep 110 flagged the caption/title mismatch unprompted", it was not digitised, and the decision went to issue #644 (`data/README.md:109`).
- A mirror-only data point was "acted on only after a human explicitly reviewed and directed it, not automatically" (`data/README.md:262`, issue #577).
- Streams disappeared: daily new suspects stopped on 6 August and the treatment-centre table was dropped on 3 August, so "the most recent weeks rest on fewer streams than earlier ones" (`README.md:15-19`).
- "The 27 May vintage disagrees badly, because INSP began reclassifying suspected cases. The model surfacing that is the point" (`04-drc.qmd:72-73`).
- Slowness: "a full docs build fits every model, which has hit GitHub's six-hour ceiling", so the workflow was redesigned to push early and let CI run (`AGENTS.md:20-24`).
- Every fix to the digitiser was checked to reproduce every previously committed block unchanged before acceptance (`data/README.md:75, 77, 79`).

### Authorship

- Local clone `git log`, 497 commits: Sam Abbott (bot) 238, seabbs-bot 144, Sebastian Funk robot edition 7, Claude 3, dependabot 50, Sam Abbott by hand 51, Funk and Brand by hand 4.
- Pull requests via GitHub search: 425 total, 333 by seabbs-bot, 53 by dependabot, 22 under seabbs (section 5).
- The 21 PRs under Sam's own account in July "contain only agent-authored commits" (`git show 8c7e834`).
- how-I-llm figure caption numbers (390 commits, 291 bot, 29 July) should stay with that figure rather than be relabelled (`notes/bvd.md`, "Size and authorship").

### Current status

- Latest release notes are v1.18.0 with cut-off SitRep 115 of 6 September 2026, confirmed cases 6686 and confirmed deaths 3226 (`docs/src/news.md:9-45`).
- Last push 2026-09-11 (`gh repo view`).
- Rt and outbreak size figures in `how-I-llm` and the collaboratory slides are from June and July fits; read current numbers from the live site before quoting any.
- Companion repo `/Users/lshsa2/code/epiforecasts/bdbv-linelist-analysis` reanalyses the 2012 Isiro line list (n = 52) for delay priors; 53 of 64 commits and all 35 PRs are by `sbfnk-bot` (local `git log`; section 5).

## 3. Composable modelling and LLM-assisted construction

Paper: `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/index.qmd`.

- Design consideration: "Modelling language optimised for large language model assisted construction with automated validation", motivated because LLMs "can make errors and often do not fully capture expert knowledge" (`index.qmd:181`, citing Aygün et al. 2025).
- "The component structure of our proposed DSL and validation tools built into it also make our approach well-suited for large language model assisted model construction" (`index.qmd:294`).
- "our DSL may enable large language models to reason about model design and propose structural adaptations more easily and with less room for error but we did not assess this in this study" (`index.qmd:364`).
- "Composable frameworks may also be key for enabling robust large language model assisted model construction, where explicit component structure and validation tools could reduce errors" (`index.qmd:380`).
- AI disclosure: Claude Sonnet and Opus "were used to assist with preparation of the manuscript text and as part of code review" (`index.qmd:725-727`).

Coefficient Giving proposal: `/Users/lshsa2/code/epiforecasts/coeff-ai-composability/application/project.md`.

- "An AI system that confidently generates plausible-looking but mechanistically unsound models could be worse than no AI at all" (`project.md:21`).
- "It has recently become evident that LLMs struggle with complex epidemiological models, yet complex models are often necessary" (`project.md:27`).
- "Validated components prevent hallucination of implausible disease dynamics" (`project.md:128`).
- Team Funk, Abbott, Ge, Paige; deadlines 1 December 2025 and 30 January 2026; outcome not recorded in the repo (`README.md:29-40`).
- EU Horizon idea: LLMs "serve as intelligent assistants, leveraging the well-defined component interfaces to guide practitioners through model composition and validation" (`eu-grant/ideas/vision.qmd:32`).

Evaluation study: `/Users/lshsa2/code/epiforecasts/llm-epi-composition`.

- Question: "Can large language models write epidemiologically correct code for estimating the time-varying reproduction number" (`README.md:3`).
- Design: Claude Sonnet 4 and Llama 3.1 8B, four scenarios, five framework conditions including EpiAware, blinded expert review of departures from a reference (`README.md:7-11, 56-67`).
- Limitation stated up front: "zero-context, single-shot prompting", "No tool use or agentic behavior", "Results should be interpreted as a lower bound on capability" (`README.md:15-22`).
- Status: last commit 2026-03-02, review materials for 48 runs, "Paper forthcoming"; a Claude Code agentic runner exists at `evaluation/run_agentic.sh`.

Why composability matters for agents, in Sam's own material:

- Agents work best "when there is something to check the answer against" (`02-use-cases.qmd:8`), and components carry their own validation (`index.qmd:380`).
- "Same layout, same CI, same style, same docs build" across eleven packages, so "changing the standard is one instruction, not eleven tickets" (`05-scale.qmd:40-48`).
- The package template "injects AGENTS.md and CLAUDE.md so a model can find the docs" (`/Users/lshsa2/code/seabbs/JuliaCon2026/roadmap/_partials/07-infrastructure.qmd:52`).
- The workflow paper gives agents a rail (`04-drc.qmd:49-54`) but itself says nothing about LLMs or agents; a grep of `main.tex` finds only "agent-based models" and "automatic differentiation". It has 141 commits, 132 by Sam.

## 4. Figures available for reuse

- `/Users/lshsa2/code/seabbs/how-I-llm/figures/bot-prs-by-month.png`: seabbs-bot PRs per month Jan to Jul 2026, footer "1,643 total · 84% merged · 11% closed unmerged"; rebuild from `figures/make_figures.py` with the September counts in section 5 if wanted.
- `/Users/lshsa2/code/seabbs/how-I-llm/figures/bvd-authorship.png`: commit shares, 390 commits, 291 bot, 29 July.
- `/Users/lshsa2/code/seabbs/how-I-llm/figures/fig-bvd-model.png`: BVD model schematic drawn for the talk.
- `/Users/lshsa2/code/seabbs/how-I-llm/figures/id-workflow.png`: the nine-stage workflow schematic.
- `/Users/lshsa2/code/seabbs/how-I-llm/figures/rt-over-time.png`: Rt fit to 29 June data; stale, keep the caveat.
- `/Users/lshsa2/code/seabbs/JuliaCon2026/figures/bvd-insp-sitreps.png`: a French INSP sitrep page.
- `/Users/lshsa2/code/seabbs/JuliaCon2026/figures/bvd-outbreak-streams.png`: per-stream against joint posterior, June fit.
- `/Users/lshsa2/code/seabbs/JuliaCon2026/figures/seabbs-bot.jpg` and `sbfnk-bot.jpg`: bot avatars; live URL https://avatars.githubusercontent.com/u/256795758?v=4.
- `/Users/lshsa2/code/seabbs/BVDOutbreakSize/slides/figures/generative-process.svg` and `outbreak_streams.png`: vintage-independent; the other files there carry June numbers.
- `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/figures/visual-abstract.png` and `fig-composable.png`.
- The robot-crowd slide in `10-community.qmd:16-23` is emoji markup, not an image.

## 5. Verified numbers

Run 2026-09-11 with `gh` outside the sandbox (TLS proxy blocked it inside).

```
gh api users/seabbs-bot --jq '{login,id,created_at,name,bio}'
# login seabbs-bot, id 256795758, created 2026-01-23T13:36:14Z,
# name "Sam Abbott (bot)", bio "This is a username for bot written commits and code from @seabbs"
gh api -X GET search/issues -f q='is:pr author:seabbs-bot' -f per_page=1 --jq .total_count            # 2144
gh api -X GET search/issues -f q='is:pr author:seabbs-bot is:merged' -f per_page=1 --jq .total_count  # 1834
gh api -X GET search/issues -f q='is:pr author:seabbs-bot is:closed is:unmerged' -f per_page=1 --jq .total_count  # 256
gh api -X GET search/issues -f q='is:pr author:seabbs-bot is:open' -f per_page=1 --jq .total_count    # 54
# 1834 + 256 + 54 = 2144. Merged 85.5%, closed unmerged 11.9%.
# Per month, q='is:pr author:seabbs-bot created:2026-MM-01..2026-MM-DD':
# Jan 17, Feb 92, Mar 78, Apr 61, May 124, Jun 531, Jul 744, Aug 399, Sep (to 11th) 98
gh api -X GET search/issues -f q='is:pr author:seabbs-bot org:EpiAware is:merged' -f per_page=1 --jq .total_count  # 1132
gh api -X GET search/issues -f q='is:pr repo:epiforecasts/BVDOutbreakSize' -f per_page=1 --jq .total_count                     # 425
gh api -X GET search/issues -f q='is:pr repo:epiforecasts/BVDOutbreakSize author:seabbs-bot' -f per_page=1 --jq .total_count   # 333
gh api -X GET search/issues -f q='is:pr repo:epiforecasts/BVDOutbreakSize author:app/dependabot' -f per_page=1 --jq .total_count  # 53
gh api -X GET search/issues -f q='is:pr repo:epiforecasts/BVDOutbreakSize author:seabbs' -f per_page=1 --jq .total_count       # 22
gh api -X GET search/issues -f q='is:pr repo:epiforecasts/bdbv-linelist-analysis' -f per_page=1 --jq .total_count              # 35
gh api -X GET search/issues -f q='is:pr repo:epiforecasts/bdbv-linelist-analysis author:sbfnk-bot' -f per_page=1 --jq .total_count  # 35
gh repo view epiforecasts/BVDOutbreakSize --json createdAt,pushedAt,stargazerCount,latestRelease
# created 2026-05-19T16:50:45Z, pushed 2026-09-11T12:57:30Z, 12 stars,
# latest release results-1699 published 2026-09-09T21:11:03Z
gh release list -R epiforecasts/BVDOutbreakSize --limit 1000 --json tagName,publishedAt --jq 'length, .[0], .[-1]'
# 145; newest results-1699 2026-09-09; oldest results-43 2026-05-20
git -C /Users/lshsa2/code/seabbs/BVDOutbreakSize rev-list --count HEAD   # 497 (local clone, 2026-09-11)
git -C /Users/lshsa2/code/seabbs/BVDOutbreakSize log --format='%an' | sort | uniq -c | sort -rn
# 238 Sam Abbott (bot), 144 seabbs-bot, 50 dependabot[bot], 40 Sam Abbott, 11 Sam,
# 7 Sebastian Funk - robot edition, 3 Sebastian Funk, 3 Claude, 1 Samuel Brand
git -C /Users/lshsa2/code/seabbs/a-workflow-for-infectious-disease-modelling log --format='%an' | sort | uniq -c
# 132 Sam Abbott, 8 seabbs-bot, 1 Sam Abbott (bot); 141 commits
```

Use `total_count`, not a paginated list; the search endpoint caps at 400 results and the deck's first numbers were wrong for that reason (`git show 69e6236`).
The July snapshot in the deck was 1,643 PRs, 84 percent merged, 11 percent closed unmerged (`how-I-llm/figures/make_figures.py:30-32`).
The August 2026 JuliaCon re-check gave 1,814 total, 84.9 percent merged, 11.2 percent closed unmerged (`notes/roadmap-llm.md:64-69`).
No revert-rate number exists; a title search for reverts found nothing usable (`notes/roadmap-llm.md:75-87`).
Review turnaround on the last 30 merged EpiAware bot PRs had a median of about 3 hours, a small sample (`notes/roadmap-llm.md:89-97`).

## 6. Open questions Sam has posed publicly

- "Tell me what you think agents cannot do" (`how-I-llm/index.qmd`, closing slide).
- "What is genuinely ours, rather than merely not-yet-automated? I do not have a good answer, and betting a career on a specific capability gap looks unwise" (`07-whats-left.qmd:22-24`).
- "If output per researcher now scales with spend, what does fair look like, and who is supposed to pay?" (`06-money.qmd:35-36`).
- "Do robots shut down collaboration?" (`10-community.qmd:9`).
- "What are good examples of whales working together in Julia?" (`11-governance.qmd:12`).
- "Who do they ask when it breaks? How do we move users to contributors?" (`11-governance.qmd:29-30`).
- "what does this mean for contributions?" and "build out an org agent which acts in batch overnight as public standards? Runs somewhere safe?" **[Sam's words, spelling normalised]** (`original-brief.md:42-45`).
- "Well, actually, we still need funding" (`05-what-it-takes.qmd:36`).
