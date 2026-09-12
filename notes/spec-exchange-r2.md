# Exchange, round two spec

From his notes of 12 September (`steers.md`, last long entry, the part
after "act on the other decks"). Read `round-2.md` (Exchange section),
`drafting-rules.md`, `style.md`, `llmisms.md` first. Overrides
`spec-exchange.md` where they differ. Content slides only; about 25 at
most for 22 minutes.

## Cuts

- "I am part of it" and similar little sentences.
- The whale line ("Every project I have worked on has ended up with one
  person doing most of it"). Not related to this talk.
- "Maybe nothing doing there at the moment."
- "Reinforcement learning and bandits on individual-based simulators.
  Could a composable component be the environment?"
- "The network consistently hindered parameter identifiability" (keep the
  network-in-a-slot schematic; the idea is nice).
- "Each line I have drawn between the two columns has moved within months."
- "For some of these the answer at the moment may be nothing, and I would
  like to hear where the VUB and SIMID groups see it differently."
- "My group" anywhere.

## Who I am: more, and about the research

Two or three slides on research interests, not one. Research more, from
the composable paper and grants, the workflow paper, `epiaware.org`, and
`research-communication.md`:

- The meta focus: composability, improving outbreak modelling, a workflow
  for modelling with multiple data sources. Not over-focused on
  nowcasting.
- Consulting and public health use: time consulting with US CDC
  collaborators, UKHSA, state and local public health in the US; the aim
  to extend to other countries' public health departments; tools used in
  outbreak response, including recent epidist use by the DRC response team
  (verify in `epinowcast/epidist` and BVD repos; else his report); the
  all-nation Pegasus pandemic preparedness exercise where multiple teams
  used various tools (grep "Pegasus" under `~/code`; else his report);
  the aim: flexible, extensible tools that are easy for LLMs to use.
- The professional opener from `round-2.md`: small group, little grant
  success, many collaborations, tools in wide use.

## Who I work with

- "At LSHTM and epiforecasts" is not accurate for recent work. Regroup by
  what the work is (real-time tools and hubs; delays and nowcasting; the
  Julia composable work; public health agencies), and check against
  `research-collaborators.md` and recent commits.
- Julia group: no Jason Asher. Check the JuliaBayes organisation
  (`gh api orgs/JuliaBayes/members`, `gh api orgs/JuliaBayes/repos`) and
  EpiAware for the right names.

## Composable, AI, workflow

- Add "Renewal as a neural network layer" as a slide, from the composable
  grants. Add NN fitting to many data sources (PINN-like) to the
  network-in-a-slot slide.
- "Agentic modelling workflows" is the next section after the AI-methods
  slides. The workflow slides are good: move them earlier and do not
  duplicate them in the BVD part. Include the agentic tree search slide
  from the keynote as part of the workflow.
- A slide on an outbreak-specific foundation model as a project he would
  love to be involved in; the key is getting the changing data over time
  into the model.
