# Round 2: communication lecture deck

Applied 12 September 2026 against `spec-communication-r2.md`. Rendered
with the sandbox off, every slide screenshotted at 1920 by 1080, no
overflow. `./scripts/lint.sh` clean. The llmisms greps leave only fact
lists (agency and author names) and literal uses. Nothing committed;
`05-asks.qmd` is removed and staged as deleted.

## Running order

24 content slides, 4 dividers, plus title, plan and thank you.

- **2020, three audiences** (8). Government · What the consensus process
  did · The public. A map, then a page for each place · The caveats sat
  in the captions · Other governments used it too · What went wrong ·
  Collaborative forecasting hubs · Where it mattered.
- **Software is communication** (5). The package is the message ·
  Defaults are advice · Limitations first · Evaluation as communication ·
  Community as the channel.
- **With AI** (4). Making it visible · The steering is the work ·
  Checking what it wrote · seabbs-review-bot.
- **Under AI** (7). Provenance · Bots talking to bots · Issues nobody
  asked for · Community, in the age of robots · What an LLM says about
  EpiNow2 · What an LLM says about me · the value question as the close.

## Moved, added, cut

- The blank slide was the background-iframe of the live UK page. Removed.
- "The limits travel less well" and the 20,000 of 1.2 million page views
  moved from software to the caveats slide; the "poorly communicated"
  quote to the other-governments slide, with "could AI do that checking?".
- New: The package is the message, Limitations first (live BVD report),
  seabbs-review-bot, Bots talking to bots, Issues nobody asked for, two
  LLM slides, the close. Community in the age of robots copied verbatim
  from the JuliaCon roadmap deck. The public is now map, caveats, table.
- Cut: What I use it for, Ten times the reading, Prose that sounds the
  same, Confident plausible wrong (the keynote has the digitiser), Who
  gets to do this (to the keynote), What I would like us to agree on, For
  the panel. "Other scientists" retitled; "In some cases"; "we" for the
  pandemic work; every quote carries a short italic attribution in text.

## Bot-to-bot evidence

- BVDOutbreakSize#443: sbfnk-bot 20 and 21 July, seabbs-bot closed it 4
  August with commit e556e69; #438 same pattern.
  https://github.com/epiforecasts/BVDOutbreakSize/issues/443
- sbfnk-bot filed 11 EpiNow2 issues in 2026, including #1475 (Rt prior
  Jacobian, fixed in #1478). https://github.com/epiforecasts/EpiNow2/issues/1475
- seabbs-bot outside his orgs: 91 issues. nfidd/sismid-nowcasting#30
  ("Done"), chalk-lab/Mooncake.jl#1241, LuxDL/DocumenterVitepress.jl#375,
  MilesCranmer/AirspeedVelocity.jl#158, 12 on mfiidd/mfiidd this month.
  The 22 on adrian-lison/blueprint-biosecurity-grant-application are
  private and not shown; his reply there, "I imagine @sbfnk won't get to
  this", could be spoken.
- seabbs-review-bot: App created 17 August 2026, 213 PRs reviewed.

## LLM answers

No API key, so `claude -p` with no tools for Opus 5 and Sonnet 5;
answers and a claim-by-claim check in `notes/llm-answers.md`. Both name
Sam as EpiNow2 maintainer; Sebastian Funk has been CRAN maintainer since
5 May 2024. Opus adds three contributors not in `DESCRIPTION` and
`fix_dist()`, removed in 1.9.0. Caveat: the CLI passed his email and both
models noticed; the slide says so. A clean run needs the API.

## For Sam

- His own account, unverified: the "off-putting" feedback on the BVD
  limitations, and the UKHSA guidance request.
- Unused figures, delete if not wanted: `comms-bot-prs-by-month.png`,
  `comms-bvd-insp-sitreps.png`, `comms-digitiser.png`,
  `comms-shot-recap.png`, `comms-shot-juliacon-prompts.png`.
- `communication/index.qmd` still has "I say what worked for each"; the
  abstracts agent owns it.
