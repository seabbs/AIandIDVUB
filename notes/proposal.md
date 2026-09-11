# Proposal for the two talks, the panel and the exchange

Drafted 2026-09-11 from the five research notes in this directory.
Claims below point at a research note, which points at a source.
Where the note marks something unverified, this says so.
Nothing here is on a slide yet.
Sam decides what survives.
`review-1.md` is the cross-review of this file and the site; its points
are folded in here or listed in section 5.

## 0. What this room means by AI

The hosts' AI is reinforcement learning and Bayesian bandits run against
individual-based simulators (Libin, Cimpean, Reymond with Abrams and Hens),
tree-based machine learning for risk maps (Dupas), and machine learning for
surveillance at RKI's AI centre (de Schrijver).
The communication strand treats large language models as objects of audit
(Algaba, citation bias) and chatbots as channels (Poels).
See `research-workshop.md` section 3.

None of the speakers was found to have published on coding agents,
LLM-built models, or time series foundation models.
So the agentic section fills a gap rather than repeating anyone.
To the hosts, "agent" means an RL policy.
Say what you mean by it on the first slide of that section.

Two things the research corrected in the brief:

- Google's FluSight entry is not a foundation model.
  It is an LLM-guided tree search that writes and ensembles forecasting
  code (Martinson et al. 2026), and it topped the flu, COVID and RSV hubs
  prospectively in 2025/26.
  Bracher and Funk 2026 attribute the earlier retrospective gains to data
  revision leakage.
  So it belongs in the agents section, as the strongest evaluated case.
- nfidd has no material on UDEs, PINNs or flows.
  It has the "two camps" slide, the "a lot of data or very good theory"
  slide, and one slide on Google SAI.
  The UDE framing is in the EU grant vision and Nina Schmid's epinowcast
  seminar.
  See `research-ai-methods.md` A1 and A3.

Kraemer et al. 2025 (Nature) is the review this room will know.
Use its taxonomy as the shared map and place the hosts' methods and agents
on it.

## 1. Keynote: Infectious disease modelling in the age of AI

25 minutes.
Nineteen content slides are sketched below, plus plan and close.
That is about 0.8 slides a minute against the 1.5 of the JuliaCon decks.
Sections A and C are figure-led and can split into a figure slide and a
bullet slide where a point needs it, which takes the count towards 25.
Section times below sum to 22 minutes, leaving three for the plan, the
close and a question.
Pitch at statistical modelling but not LLM tooling.
Many in the room are doctoral students.

### A. Ten years of outbreaks (6 minutes, 6 slides)

The organisers asked for history and practical examples.
Keep the deep history to one strip and spend the time on the ten years.

1. **A timeline strip.** 2014 Ebola, 2020 COVID-19, 2022 mpox, 2026
   Bundibugyo.
   Bernoulli 1760, Ross 1911, Kermack and McKendrick 1927, foot and mouth
   2001, H1N1 2009 as small ticks before it.
   One figure, no bullets.
   Sources in `research-history.md` sections 2 and 3.
2. **2014, watching.** CDC projected 1.4 million cases by January 2015;
   about 21,000 had occurred.
   Camacho and Funk forecast district-level R in Sierra Leone in real
   time.
   The lesson Sam took: real-time modelling had arrived, and its
   overreach was public.
   Figure: a Funk et al. 2019 forecast panel, to be sourced.
3. **2020, doing it.** Rt daily for several thousand locations, a
   dashboard, weekly estimates to SPI-M-O.
   Figure: `example-rt.png` from the 2022 blog post.
   His line: "at least 80% but on time".
4. **What came out of it.** EpiNow2, epinowcast, scoringutils, the hubs.
   Used by CDC, and others.
   Figure: the package timeline from the JuliaCon roadmap deck.
5. **2022, mpox.** Nowcasting for UKHSA (Overton et al. 2023), and the
   BMJ editorial on Ward et al.
   Ward et al. did the delay estimates; Sam did not.
   Figure: the Overton nowcast.
6. **2026, live.** Ebola disease caused by Bundibugyo virus, DRC.
   6757 confirmed cases and 3267 deaths by 7 September (WHO DON617).
   Figure: the French sitrep page and the per-stream posterior.
   This slide is the bridge to section C.

Two facts to settle before any slide: start date at LSHTM is 3 January in
the bio and 6 January in the 2023 blog post, and "30 public health
agencies" has no list behind it.
See `research-history.md` section 5.

### B. What a modeller does during an outbreak (2 minutes, 2 slides)

7. **The loop.** Data in, delays, infections and Rt, forecasts and
   scenarios, a decision, new data.
   Figure: a four-box version drawn for a non-modeller, not the
   nine-stage schematic.
   Say what a renewal process is in one line here.
   One slide only, since Lecture 1 covers the methods.
8. **What keeps going wrong.** Biased delays.
   Chained models that lose uncertainty.
   Everything bespoke, so slow to adapt.
   "We sometimes published nonsensical estimates" (2022 blog).
   Option: the Belgian scoping review this room co-wrote found half of
   105 COVID-19 models had no behaviour component (Bagaforo et al.
   2026), which is a gap they already accept.
   Stop here and hand to Abrams and Libin.

### C. Agents (8 minutes, 6 slides, the section most likely to run long)

Gloss on first use, one line each: pull request, bot account, git log,
reporting triangle.
The room has statistical modelling, not LLM tooling.

9. **What I mean by an agent.** A language model that reads files, runs
   code, opens pull requests and loops until a check passes.
   Not an RL policy.
   Not a chatbot.
   One schematic.
10. **How I work now.** Most code I ship is written by an agent.
    About half carries a review from me.
    My job moved from typing to specifying and checking.
    Figure: bot pull requests per month, rebuilt with the September
    counts (Jun 531, Jul 744, Aug 399; 2144 total, 85.5% merged).
    Source: `research-agentic.md` section 5.
11. **A live outbreak built this way.** Replication of McCabe et al. in a
    few hours the next day.
    Refit on every push, 145 releases since 20 May.
    The situation reports are French PDFs and agents read them.
    333 of 425 pull requests by the bot.
    Figure: sitrep page beside the streams posterior.
12. **What was hard to check.** SitRep 081: JPEG compression hid the tick
    marks and the digitiser undercounted by 54%.
    SitRep 087: the y-axis changed from steps of 20 to 25 and was caught
    only because it broke the reporting triangle invariant.
    "The failure mode is confident, plausible, wrong."
    Figure: the raster onset curve.
13. **What changes.** Review is the bottleneck.
    Components with their own checks give the agent something to test
    against.
    Google's SAI is an agent writing forecasting models, and it topped
    the three CDC hubs in 2025/26.
    Attribution: Martinson et al. 2026; Bracher and Funk 2026 on the
    retrospective claim.
14. **What does not change.** Agents did not choose the model, decide
    what the lower bound meant, or judge whether the ascertainment
    assumption held.
    "Who can do this work at all is narrowing. Agents make that worse."
    "I do not have a defence for this."

### D. The other AI (5 minutes, 4 slides)

15. **A map.** Kraemer et al. 2025 taxonomy as a figure.
    Mark where the hosts' RL sits, where agents sit, where the next three
    slides sit.
    Do not explain RL or bandits; Abrams, Libin and Cimpean will.
16. **Learn the part of the mechanism you do not know.** Universal
    differential equations and PINNs.
    A neural network for the term you cannot write down.
    Caveat from Philipps et al. 2025: the network soaks up identifiability
    and fitted mechanistic parameters may not mean what they did.
    Figure: SEIR box diagram with one box replaced by a network.
17. **Fit models you could not fit.** Normalising flows and
    simulation-based inference.
    OutbreakFlow on early German COVID-19; neural posterior estimation on
    the 2014 Sierra Leone SEIR.
    Caveat from Jang et al. 2026: non-identifiability comes from the
    simulator and more simulation does not fix it.
18. **Forecast without a mechanism.** Time series foundation models
    zero-shot.
    Strong short-term accuracy on sparse or irregular data (Kalahasti et
    al. 2025); TabPFN-TS zero-shot rivalled the ECDC RespiCast ensemble
    (Wang, Li and Perra 2026).
    Less is reported about peaks and turning points, so say so rather
    than claim they fail there.
    Sources: Kalahasti et al. 2025, Wang, Li and Perra 2026, Jafari et al.
    2026.
    The nfidd line fits here: "a lot of data or very good theory".

### E. Where does AI fit? (1 minute, 1 slide)

19. **My guess, marked as a guess.** Agents build and check.
    Mechanism stays the object.
    People keep the question, the judgement of fitness for use, and the
    trust of the people who act on the numbers.
    Then the question to the room, which becomes the panel question.

## 2. Lecture: Science communication with and under AI

30 minutes.
Twenty-one content slides are sketched below, plus plan and close.
Section times sum to 27 minutes, leaving three for the plan and close.
Gloss on first use: SPI-M-O, SAGE, UKHSA, WIS, pull request, bot
account.
Poels covers risk communication and chatbots.
Algaba covers LLMs as citation-biased scientific actors.
So this lecture is about communicating model outputs when both the writer
and the reader have a language model, told through 2020.
Sources: `research-communication.md` throughout.

### A. Three audiences in 2020 (7 minutes, 6 slides)

1. **Government.** Weekly Rt, forecasts and ad hoc reports to SPI-M-O and
   SAGE.
   Consensus statements on GOV.UK, unattributed.
   "We don't know whether any of this gave any policy maker any useful
   information that helped them make better decisions."
   Figure: a SPI-M-O consensus statement page.
2. **What the consensus process did.** Joint statements carry the shared
   view and lose the detail.
   His 2023 line: joint statements stop the incentive to be first out and
   cut corners.
3. **The public.** The dashboard.
   Just over 500,000 unique users and 1.2 million page views by March
   2022, of which 20,000 were for the methods page.
   Figure: `uk-rt-dashboard.png`.
4. **What went wrong.** "Because we did not have the capacity to manually
   inspect the data and estimates on a daily basis we sometimes published
   nonsensical estimates."
   Rules he wrote down afterwards: be as open as possible, state
   limitations first, no point estimates.
   And: "I personally didn't feel it was useful for me to directly
   interact with the public/media."
5. **Other scientists.** Forecast hubs.
   "Your forecast becomes part of another product, the forecast ensemble.
   However, they can be very hard to learn from."
   Figure: `hub-ensemble-good.png` and `hub-ensemble-less-good.png`.
6. **Where it mattered.** "Probably our most useful contributions were in
   the UK where we knew the data and interacted directly and frequently
   with policy makers."

### B. Software is communication (4 minutes, 4 slides)

7. **Defaults are advice.** EpiNow2 on CRAN since September 2020.
   CDC used it for nowcasts and Rt (CFA page and MMWR 2024).
   Ottawa Public Health and the Philippines platform are in his adoption
   file but were not fetched, so verify before use.
   Defaults are decisions the user inherits.
8. **The limits travel less well than the method.** "This can cause issues
   if the limitations of the method are poorly communicated" (2022).
9. **Community as the channel.** epinowcast: over 50 researchers and
   practitioners, 31 seminars since May 2023, a forum, a contribution
   ladder.
   "Community >> methods or models alone" and "why efforts in this
   direction keep failing" (2023).
   Later: "in many cases the package is too complex for anyone else to
   use."
10. **Evaluation as communication.** scoringutils, pairwise comparison so
    teams can be compared with missing forecasts.
    UKHSA asked for guidance on evaluation.

### C. With AI (6 minutes, 5 slides)

11. **What I use it for.** Drafting, review, reading French PDFs, these
    slides.
    "I wrote the argument and almost none of the words."
12. **Making it visible.** A bot account, so git log says who did what.
    A disclosure line in the BVDOutbreakSize README.
    A prompts page with the brief and the steers.
    The bot-written bio and its "suspiciously high opinion of me".
13. **The steering is the work.** The JuliaCon prompts page counted
    fifty-three steers mid-build; recount from its `notes/steers.md`
    before this goes on a slide.
    "Every steer above was a judgement I could make and it could not."
14. **Checking what it wrote.** A second workflow extracted 114 claims
    from a deck and 67 needed changing.
    One count was really a pull request number.
15. **Ten times the throughput.** "Ten times the throughput at ten times
    the review load is not a win."
    Figure: bot PRs per month.

### D. Under AI (7 minutes, 4 slides)

16. **Prose that sounds the same.** Three before and after pairs from
    `llmisms.md`: the bolted-on clause, the moral, the point-stamp.
    His own edits, not a detection study; Algaba covers detection and
    citation bias next, and Poels covers chatbots as channels.
    Kobak et al. 2025 (at least 13.5% of 2024 PubMed abstracts) as the
    attribution line only.
17. **Provenance.** Who is accountable for a number an agent produced.
    The BVD README line: "The named authors are responsible for that
    oversight."
18. **Confident, plausible, wrong.** The SitRep digitiser stories, told
    from the communication side: the error that reached a plot before a
    check caught it.
19. **Who gets to do this.** "The people modelling outbreaks where
    outbreaks happen are the least likely to have paid access.
    I do not have a defence for this. I am part of the problem."

### E. What I would like us to agree on (3 minutes, 2 slides)

20. Publish the prompts and steers with the code.
    Disclose agent authorship the way we disclose funding.
    Joint statements and hubs matter more when writing is cheap.
    Keep a named person behind every number.
21. The question for the panel.

## 3. Research exchange, 15 September

Half a day shared with the VUB AI Lab and SIMID, so probably 30 to 40
minutes with discussion.
Informal, mostly reused slides.

- Who I am. The timeline strip from the keynote.
- What the group works on. Real-time outbreak analysis, delays and
  nowcasting, forecast evaluation, tooling.
  Name the people.
- epinowcast and EpiAware. R and Julia, community and org.
- Composable models. The approaches page and the two approaches, with
  the three replications.
- The live outbreak. Reuse keynote slides 11 and 12 with more detail on
  the model.
- Working with agents. Reuse the tooling slides from how I LLM, facts
  only, rephrased.
- Where we might work together.
  RL for control needs transmission models with honest uncertainty; a
  composable component could be the environment.
  Agents that build simulators; who checks them.
  Fairness in allocation needs the same delays and ascertainment we
  model.
  Evaluation of learned policies against hub-style prospective tests,
  which the RL scoping review says is missing.

## 4. Panel: likely questions and his lines

- What is AI good for in an outbreak?
  Building and checking the apparatus.
  Not choosing the model.
- Will AI replace modellers?
  "Every boundary I have drawn in two years has moved."
  "What is genuinely ours, rather than merely not-yet-automated?"
- Trust.
  Bot accounts, disclosure lines, prompts pages, hubs.
- Equity.
  "I am part of the problem."
- Communication.
  "No point estimates!"
  Joint statements.
  "Answering a robot is dispiriting."

## 5. Decisions for Sam

1. Keynote section C is the one at risk of running long.
   If it does in rehearsal, cut keynote slide 17 (flows) rather than
   anything in A or C.
2. Google SAI moves from "other AI" to "agents".
   Agree?
3. Start date: 3 January or 6 January 2020.
4. "30 public health agencies": keep as "used by public health agencies
   including CDC" unless a list exists.
5. The lecture leans on the 2022 and 2023 blog posts for his own words.
   They are his, but four years old.
   Say which still hold.
6. The exchange deck is the lowest priority and could be assembled from
   the other two on the day.
7. The home page carries the JuliaCon 2026 bio verbatim, labelled as
   such.
   It says 3 January 2020, over a million people, and upwards of 30
   agencies.
   The research supports the first two only partly and the third not at
   all (`research-history.md` section 5).
   Keep, correct, or replace with a plain about-me.
