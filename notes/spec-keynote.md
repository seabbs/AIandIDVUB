# Spec: keynote, Infectious disease modelling in the age of AI

Monday 14 September 2026, 09:00–09:30, 25 minutes of talking.
Mixed room of infectious disease and AI researchers, many doctoral
students, some with no modelling background.
Abrams and Libin follow with a methods overview, then three case studies.

The running order is `proposal.md` section 1, slides 1 to 19, with section
times A 6, B 2, C 8, D 5, E 1.
Build that.
Where the proposal says "Figure:" build or copy that figure.
Where it says "Option:" decide and say why in your report.

## Steers that override the proposal

- The Google point is LLM-guided tree search writing forecasting models
  (Martinson et al. 2026), not a foundation model. It lives in section C,
  slide 13, and gets its own figure or a one-line schematic of the loop:
  propose model, fit, score, keep, rewrite. Bracher and Funk 2026 in the
  attribution.
- Pictures and interactives. Section A is one figure per outbreak.
  Candidates for interactives: the timeline strip with a hover or
  fragment reveal per outbreak; an `{ojs}` slider showing how a renewal
  process turns infections and a generation interval into cases, for slide
  7; the live BVDOutbreakSize report in an iframe for slide 11, with a
  static fallback. Pick two.
- Sparse slides. Section A slides may be a figure and one line.

## Sources by section

- A: `research-history.md` sections 2 to 5 for every date and count;
  figure paths in its section 4 and in `research-communication.md`
  section 7. The mpox slide credits Overton et al. 2023 and the BMJ
  editorial, not Ward et al.
- B: `research-communication.md` section 2 for "nonsensical estimates";
  `research-workshop.md` section 4 for Bagaforo et al. 2026.
- C: `research-agentic.md` throughout, section 5 for the counts. Rebuild
  the bot PRs per month figure from the monthly counts there.
- D: `research-ai-methods.md` B2 to B4 and the caveats list;
  `research-workshop.md` section 4 for Kraemer et al. 2025.
- E: `research-agentic.md` section 6 for the questions.

## Do not

- Explain reinforcement learning, bandits or STRIDE.
- State the LSHTM start date, the million users or the 30 agencies; the
  bio carries them and they are under review.
- Write a summary slide.
