# Keynote partial 2, acting on his edits of 13 September

File: `keynote/_partials/02-ai-methods.qmd`. Also `scripts/keynote-schematics.py`, `figures/keynote-renewal-layer.png` (redrawn), `figures/keynote-pinn.png` (new). Nothing committed.

## Each TODO

- **What even is AI?** His list as written. Spacing after "i.e." fixed on two lines. Nothing else touched.
- **My view / And yet.** Kept as his two slides, attribution line under each.
- **Kraemer map.** His shortened alt text kept.
- **UDEs.** Definition bullet added (a differential equation with one or more terms a neural network, fitted jointly with the mechanistic parameters, Rackauckas et al. 2020). The "keep the compartments" bullet cut. "2020c" fixed. Philipps et al. 2025 is now a link to PMC12398592. Charlotte Holt and "most exciting where" bullets kept, tidied. Limitation bullet added: reporting not modelled, no comparison with a simple statistical or semi-mechanistic model as in Funk et al. 2019 (PLOS Comput Biol, the Ebola forecasts already in section 1). Funk 2019 added to the attribution.
  - Source check. The Rackauckas et al. 2020 paper (arXiv:2001.04385, v4 text read via pdftotext) has no epidemic example; "spatial epidemiology" appears once as a reaction-diffusion benchmark. The epidemic UDE with Rackauckas as author is Dandekar, Rackauckas and Barbastathis 2020, Patterns 1(9):100145, PMC7671652: a neural network for quarantine strength in an SIR model fitted to case counts from 70 countries (abstract via Europe PMC). The slide cites that paper for "applied to epidemics" and the limitation bullet describes it. Full text was behind a 403, so the "reporting not modelled, no statistical comparison" reading rests on the abstract and my knowledge of the paper. Please check.
- **PINNs.** Built from his outline: what they are (Raissi, Perdikaris and Karniadakis 2019, J Comput Phys, via Crossref), a schematic drawn by `pinn()` in the schematics script (time in, network, state and beta out, data loss and physics loss summed), epidemic uses (Kharazmi et al. 2021, Nat Comput Sci 1:744, via Crossref; research note B3 for the four locations), fitting to challenging data (Millevoi, Pasetto and Ferronato 2024, PLOS Comput Biol, doi 10.1371/journal.pcbi.1012387, cases and admissions jointly, fetched from PMC), applied successfully (Rama et al. 2026, arXiv:2506.03897, Italian influenza, competitive on the weighted interval score, fetched), limitations (deterministic, no uncertainty; extrapolation beyond the training window, both Millevoi et al.).
- **Renewal as a layer.** His bullets kept, PINN spelled out, $R_t$ glossed. Added the advantages against a PINN on an ODE (time-varying parameters natural to a renewal process; discrete time matches the data). Repository is SamuelBrand1/RenewalExamples; the `conv` branch has `RenewalCell`, a Lux.jl recurrent cell for the renewal equation, and `delay_conv`, a delay as a convolution layer, so the schematic boxes now say "a recurrent cell" and "a convolution over the delay". Gradient arrows and the backward label removed; two side notes on time-varying $R_t$ and discrete time added. One-line grant attribution restored, repository cited by URL.
- **AI-driven inference.** His three bullets kept, acronyms spelled (MCMC, SMC, ABC), "ID" expanded, merged "offer an alternative" with the simulate bullet.
- **Foundation models.** "What kind of model?" answered: transformers, attention-based; TimesFM decoder-only, Chronos T5 (research note B2). His prospective question kept as a bullet. The outbreak-specific foundation model line is now a quote under the columns with "Sam Abbott, September 2026" in slate, as on the My view slide. It fits at 1080 (slide height 915).
- **RL.** Title kept with his parenthetical. Added what it is, one sentence on how it differs from optimal control with JuMP, and his "how does it differ" left as an open question. PPO spelled out. Bullets otherwise his. Fits (height 1043).
- **Patterns.** Acronyms spelled on first use (UDE, SIR, PINN, MCMC, SMC, PPO, ECDC in full). Quotes attributed in text. Divs balance (6 `::::` pairs, 25 `:::` pairs).

## Layout

Six slides carry five or six of his bullets, which overflowed at the default size. They use Quarto's `{.smaller}` slide class with a 42/58 column split. All section 2 slides render under 1080 px in `keynote-shots.py`; no overflow flagged.

## Checks

Rendered with the sandbox off. The six fenced-div warnings in the render come from `03-agents.qmd` ("Digitising from figures" slide), not this partial. `./scripts/lint.sh` clean for this file (remaining hits are in `03-agents.qmd`). llmisms greps: only author lists and alt text hit; two rewrites made (alt text "which", "best actions" to "optimal actions").

## Slide count

Section 2 now 10 content slides (two are single quotes), up two from his additions.
