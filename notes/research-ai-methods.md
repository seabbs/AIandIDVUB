# AI methods other than LLM agents in outbreak modelling: research notes

Compiled 2026-09-11 for the VUB/UAntwerp/UHasselt keynote on 2026-09-14.
Part A mines local teaching and grant material for Sam's own framing.
Part B reports only claims verified at a URL.
Paths are absolute local paths.

## A1 What nfidd teaches

nfidd has no teaching content on UDEs, PINNs, normalising flows, simulation-based inference or foundation models.
The grep for "universal differential", "UDE", "PINN", "physics-informed", "normali[sz]ing flow", "foundation model" and "deep learning" returned no hits in any nfidd course.
What it does have is a small number of framing statements about machine learning and one slide on the Google FluSight entry.

**The "two camps" framing** in `/Users/lshsa2/code/nfidd/sismid/sessions/slides/introduction-to-forecasting.qmd` (line 102) and `/Users/lshsa2/code/nfidd/sismid-forecasting/sessions/slides/introduction-to-forecasting.qmd` (line 91).
Camp A: "It's a machine learning problem! We can gather enough data to make good predictions, and we don't really have to understand the underlying processes that well."
Camp B: "We have clear theory that explains transmission of pathogens in a networked population. I don't need to confront my model's statements with data."
The slide then asks "What camp are you in?"

**The spectrum of models** in `/Users/lshsa2/code/nfidd/nfidd/sessions/slides/introduction-to-the-spectrum-of-forecasting-models.qmd` (line 146) and the sismid copy.
Machine learning sits under "Other models" next to "Expert or crowd opinion", with no elaboration.

**Course overview slide** in `/Users/lshsa2/code/nfidd/sismid-forecasting/sessions/slides/introduction-and-course-overview.qmd` (lines 241 to 244).
"Statistical and Machine Learning models" are described as "Models that don't include any epidemiological background e.g. ARIMA; also called *time-series models*", "\"Black-box\" machine learning approaches", and "Various regression-based approaches (could include some epi-relevant covariates)".

**Time series 101** in `/Users/lshsa2/code/nfidd/sismid/sessions/forecasting-models.qmd` (line 214) and `/Users/lshsa2/code/nfidd/sismid-forecasting/sessions/time-series-101.qmd` (line 218).
On the moving average term: "This is actually a common technique in more modern-day machine learning approaches too: learn from your past errors/residuals to improve your model."

**Hub playground** in `/Users/lshsa2/code/nfidd/sismid/sessions/hub-playground.qmd` (line 215) suggests "use the `fable::NNETAR()` model to build a neural network model" as an optional exercise.

**Anatomy of good forecasting models** in `/Users/lshsa2/code/nfidd/sismid-forecasting/sessions/slides/good-models.qmd` is the most reusable material.
Lines 25 to 30 set up the problem: "Predictive models either need __a lot__ of data or very good \"theory\"."
"__Data__: We sometimes have only on the order of 10 seasons of data. We'd like tens of thousands (or more)."
"__Theory__: If you could see all the eventual data, would you be able to explain why the outbreak evolved as it did? The underlying mechanics are impossibly complicated."
Lines 88 to 99 give the Google slide: "Google SAI [@martinson_prospective_2026]", "Setting: FluSight 2025/2026", "Credentials: 1st out of 39 models", "Special sauce: TreeSearch algorithm with LLM re-writing code for models; Ensembling multiple candidate models".
A footnote reads "Nick Reich acknowledges paid consulting for Google in 2025-2026."
Lines 130 to 140 close with "Squeeze all the juice out of your data" and "\"Epi-informed\" but not a lot of mechanism", noting "Most models were largely \"phenomenological\"."
The citation is in `/Users/lshsa2/code/nfidd/sismid-forecasting/nfidd.bib` (line 2) with the full arXiv abstract.

## A2 What the grants say

**EU Horizon grant vision** in `/Users/lshsa2/code/epiforecasts/eu-grant/ideas/vision.qmd` (lines 18 to 30).
"A second challenge lies in the interaction between traditional infectious disease modelling and modern AI methods."
"Traditional mechanistic models provide interpretability and encode valuable domain knowledge but are limited in their ability to learn from complex and non-standard data sources."
"Conversely, pure ML/AI approaches can discover patterns but lack the biological grounding, interpretability, and the integration of domain knowledge required for public health decision-making."
"Universal differential equations embedded within individual model components bridge the traditional-AI divide by learning residual dynamics—the unknown mechanisms that traditional approaches miss—while maintaining interpretability."
"Here, large language models serve as intelligent assistants, leveraging the well-defined component interfaces to guide practitioners through model composition and validation".
The themes note in `/Users/lshsa2/code/epiforecasts/eu-grant/ideas/themes.md` lists "universal differential equations (i.e AI) as model subcomponents for complex systems".
The call text in `/Users/lshsa2/code/epiforecasts/eu-grant/docs/work-programme.qmd` (lines 42 to 76) is the funder's framing and asks for "trustworthy and ethical AI-based tools".

**UKRI pandemic grant** in `/Users/lshsa2/code/epiforecasts/ukri-pandemic-grant/submission/approach.qmd` (lines 38 and 45).
Components follow "established patterns in machine learning frameworks [@Flux.jl-2018;@innes:2018]" and the package list includes "integration packages (SciML [@SciML] for differential equations, Flux.jl [@Flux.jl-2018;@innes:2018] for neural networks)".

**UKRI reviewer feedback** in `/Users/lshsa2/code/epiforecasts/composable-workflow-grant/previous-reviews/ukri.md` (lines 93, 116).
"Also advances in AI-based methods are really transforming this field but are not mentioned - how is this going to impact the utility of this framework?"
"Although this has been an issue previously, this is changing very rapidly with both enhanced GPU capacity and AI-based methods. So this may not be pushing innovation to the extent that the applicants claim."

**Composable workflow grant (Wellcome Discovery)** in `/Users/lshsa2/code/epiforecasts/composable-workflow-grant/submission/research_vision.tex`.
Line 140 lists "neural network composition \autocite{pervez2024mechanistic,flux}" as one of the composability approaches to evaluate.
Lines 342 to 343 in the design table: "Composability with machine learning approaches" motivated by "Integration with neural networks, Gaussian processes, and other ML tools enables leveraging that expertise".
Lines 352 to 353: "Modelling language optimised for large language model assisted construction with automated validation" motivated by "Large language models may be useful for constructing models but can make errors and often do not fully capture expert knowledge".
Lines 224 to 226: "Large language models (LLMs) can generate working code for disease models but struggle with structural correctness as complexity increases \autocite{proctor2024}."
The longform note `/Users/lshsa2/code/epiforecasts/composable-workflow-grant/notes/research-vision-longform-2026-03-26.tex` (line 344) adds the risk "LLM capabilities change rapidly: the boundary we measure in year 3 may shift by year 5."

**Coefficient Giving application** in `/Users/lshsa2/code/epiforecasts/coeff-ai-composability/application/project.md`.
Line 21: "An AI system that confidently generates plausible-looking but mechanistically unsound models could be worse than no AI at all."
Line 49: Julia has "scientific machine learning methods such as Universal Differential Equations."
Lines 56 to 58 describe components as a knowledge base, as callable tools, and as part of "the AI's reasoning trace".
The feedback note `/Users/lshsa2/code/epiforecasts/coeff-ai-composability/application/feedback.md` (line 32) records "penetration in outbreak modelling is minimal" for AI experts.

**LLM composition study** in `/Users/lshsa2/code/epiforecasts/llm-epi-composition/README.md` asks "Can large language models write epidemiologically correct code for estimating the time-varying reproduction number (Rt)?" with 120 submissions.
Line 22 says results "should be interpreted as a lower bound on capability".

**HPAI challenge** in `/Users/lshsa2/code/epiforecasts/outbreak-theme/hpai-challenge/submission/model_description_phase1.md` (line 274) records a workflow that "was predominantly LLM-generated (Claude Code) following a structured 11-step modelling workflow, with human review and direction at each stage."

No grant file mentions FluSight, Google's forecasting entry, foundation models, PINNs or normalising flows.

## A3 EpiAware and epinowcast

There is no neural ODE, Lux or Flux code in any EpiAware package.
The only ML dependency is `SciMLSensitivity` in `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/Project.toml` (line 21), used for reverse-mode AD through ODE solves (`case-studies.qmd` line 1157).

`/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/index.qmd` (line 177) has the design row "Composability with machine learning (ML) approaches" citing `[@philipps2025ude]`, the Philipps, Schmid and Hasenauer UDE review.
The 40 minute talk `/Users/lshsa2/code/EpiAware/ComposableProbabilisticIDModels/presentations/40min/index.qmd` (line 682) lists "SciML ecosystem for ODEs, neural networks, and other scientific computing tools" as a reason for Julia.
`/Users/lshsa2/code/EpiAware/epiaware.github.io/index.qmd` (line 44) describes SciML as "Differential equations, sensitivity analysis, and scientific machine learning."
`/Users/lshsa2/code/EpiAware/JuliaForIDM/index.qmd` (lines 175 to 176) lists two candidate case studies: "Neural ODEs: SEIR w/ AR + NN interaction terms" pointing at HybridDynamicModels.jl, and "UDEs SEIR with NN on multiple datasets" pointing at the Heliyon paper in B3.

epinowcast hosted Nina Schmid's seminar on 2026-03-04, `/Users/lshsa2/code/epinowcast/epinowcast.github.io/seminars/2026-03-04-nina-schmid/index.qmd`.
Its abstract says UDEs "face challenges in efficient and reliable training due to stiff dynamics and noisy, sparse data, as well as in ensuring the interpretability of the mechanistic model parameters" and describes an SEIR UDE "to link wastewater viral loads to case counts while learning time-varying parameters via neural networks".
Matthew Shin's 2024 seminar page describes his interests as "scientific machine learning (SciML)".
The STLT reporting delays guide (`/Users/lshsa2/code/epinowcast/GuideToSTLTReportingDelays/methods/reporting-delays.qmd`, line 116) notes that nowcasting as regression admits "gradient-boosted trees, neural networks, and other machine learning approaches".

JuliaCon 2026 partial `/Users/lshsa2/code/seabbs/JuliaCon2026/composable/_partials/06-direction.qmd` (lines 76 to 84) contrasts "JAX has one automatic differentiation system, and everything is written against it" with "We are trying to support seven automatic differentiation configurations in CI".
No partial mentions PyRenew or ML-friendly components by name.

## B1 Google in the CDC hubs

- Google's entry is an LLM-guided tree search that writes forecasting code, not a time series foundation model. Martinson, Brenner, Plomecka, Williams, Reich and Shamsi, "Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search", arXiv 2026-05-15. https://arxiv.org/abs/2605.16238
- The abstract states a "fully prospective, real-time evaluation during the 2025-2026 US respiratory season" for influenza, COVID-19 and RSV, with an ensemble that "consistently matched or outperformed" the CDC hub ensembles, and that "optimizing log-scale distance metrics prevents reward hacking". Same URL.
- Team folders exist in all three hubs: `Google_SAI-FluEns` and `Google_SAI-FluBoostQR` in FluSight (https://github.com/cdcepi/FluSight-forecast-hub/tree/main/model-output), `Google_SAI-Ensemble` in the COVID hub (https://github.com/CDCgov/covid19-forecast-hub/tree/main/model-output), and `Google_SAI-RSVEns` in the RSV hub (https://github.com/CDCgov/rsv-forecast-hub/tree/main/model-output).
- Bracher and Funk, "Information leakage from data revisions in retrospective forecasts", arXiv 2026-08-06, analyse the earlier Google retrospective study and attribute its reported 11 percent improvement over the CDC ensemble to failure to account for data revisions. https://arxiv.org/html/2608.05883
- The same paper notes the follow-up "Google SAI Ensemble competed under real-time conditions during the 2025/26 season" and "was found to top the leader board for all three diseases considered". Same URL.
- Google's TimesFM-3 blog (2026-08-31) does not mention epidemics, influenza, FluSight or the CDC. https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/
- No Google Research blog post on the FluSight entry was found in search.
- The nfidd slide's "1st out of 39 models" ranking could not be verified at a URL beyond the two arXiv papers above.

## B2 Time series foundation models in epidemic forecasting

- TimesFM (Google): decoder-only pretrained forecaster, ICML 2024. https://github.com/google-research/timesfm
- Chronos (Amazon): tokenises series and trains T5-family models, 20M to 710M parameters. https://arxiv.org/abs/2403.07815
- Moirai (Salesforce): masked encoder trained on LOTSA, over 27 billion observations. https://arxiv.org/abs/2402.02592
- Lag-Llama: decoder-only transformer using lags as covariates, described as the first open-source time series foundation model. https://arxiv.org/abs/2310.08278
- Zero-shot evaluation on epidemics: "Foundation time series models for forecasting and policy evaluation in infectious disease epidemics", medRxiv 2025-02-25, tested TimesFM, Lag-Llama, Chronos, TimeGPT and TabPFN-TS on influenza, RSV, chickenpox and dengue and reports strong short-term accuracy and gains on limited or irregular data. https://www.medrxiv.org/content/10.1101/2025.02.24.25322795v1
- Wang, Li and Perra, "From naive to foundation: benchmarking models for epidemic forecasting", medRxiv 2026-05-11, found TabPFN-TS zero-shot "consistently outperform[ed] all other individual architectures" on ILI in nine European countries and often rivalled the ECDC RespiCast ensemble. https://www.medrxiv.org/content/10.64898/2026.05.11.26352889v1.full
- Jafari et al., "Understanding Key Features of Time Series Foundation Models from Epidemic Forecasting", arXiv 2026-06-17, found a mixture of pretrained forecasters did best on US influenza and that "language model-based time series methods underperformed" numerical forecasters. https://arxiv.org/abs/2606.19560
- HFMD comparison in Frontiers in Public Health 2025: ARIMA matched Moirai at one step ahead, TimesFM led at five and ten steps. https://pmc.ncbi.nlm.nih.gov/articles/PMC12507834/
- Epidemiology-specific pretraining: CAPE (Liu et al., KDD 2026) pretrains on synthetic compartmental simulations plus surveillance data and reports higher alert sensitivity than Moirai across 17 diseases zero-shot. https://pmc.ncbi.nlm.nih.gov/articles/PMC13464487/
- Perspective: "Toward AI foundation models for epidemics: Promise, challenges, and paths forward", PNAS 2026-03-31, asks whether a single pretrained model can capture shared dynamics across pathogens. https://www.pnas.org/doi/10.1073/pnas.2526192123 (abstract only via search; page blocked)
- PandemicLLM (Du et al., Nature Computational Science 2025) reformulates forecasting as text reasoning over policy, genomic and case data for 50 US states over 19 months. https://arxiv.org/abs/2404.06962

## B3 UDEs and PINNs in epidemic models

- Rackauckas et al., "Universal Differential Equations for Scientific Machine Learning", arXiv 2020, v4 2021, defines UDEs as "the unifying framework connecting the ecosystem". https://arxiv.org/abs/2001.04385
- Philipps, Schmid and Hasenauer, npj Systems Biology and Applications 2025, review UDEs and report that "noise and limited data significantly degrade performance", "the over-parametrised ANN component consistently hindered parameter identifiability", stiff dynamics need specialised solvers, and fitted mechanistic parameters "did not match the published values". https://pmc.ncbi.nlm.nih.gov/articles/PMC12398592/
- Applied UDE: "Predicting Covid-19 pandemic waves with biologically and behaviorally informed universal differential equations", Heliyon 2024, couples behaviour and disease dynamics to predict second waves. https://www.sciencedirect.com/science/article/pii/S240584402401394X
- Applied PINN: Millevoi, Pasetto and Ferronato, PLoS Computational Biology 2024, estimate time-varying transmission in an SIR model on Italian COVID-19 data and note "The deterministic nature of PINN does not provide a quantification of uncertainty" and that predictions outside the training window can be "extremely far" from data. https://pmc.ncbi.nlm.nih.gov/articles/PMC11407682/
- Applied PINN: Kharazmi et al., Nature Computational Science 2021, use PINNs for time-dependent parameters in SIR variants on New York City, Rhode Island, Michigan and Italy, with an explicit identifiability analysis. https://www.medrxiv.org/content/10.1101/2021.04.05.21254919v1.full
- Applied PINN for forecasting: Rama et al., "Forecasting Seasonal Influenza Epidemics with Physics-Informed Neural Networks", arXiv 2025 revised 2026, competitive on weighted interval score but "coverage metrics highlight room for improvement in uncertainty calibration". https://arxiv.org/abs/2506.03897

## B4 Normalising flows and simulation-based inference

- Radev et al., "OutbreakFlow", PLoS Computational Biology 2021, train an invertible network on simulations from an epidemic model then infer generation time, undetected fraction and reporting delays for early COVID-19 in Germany. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009472
- Pinotti et al., "Simulation based-inference of epidemiological and phylodynamic models via Neural Posterior Estimation", bioRxiv 2025-11-28, fit an SEIR model to 2014 Sierra Leone Ebola data and a birth-death phylodynamic model, and note NPE's "limited application in infectious disease epidemiology". https://www.biorxiv.org/content/10.1101/2025.11.25.690436v1
- Wieland et al., "Assessment of simulation-based inference methods for stochastic compartmental models", arXiv 2025 revised 2026, compare particle MCMC with conditional normalising flows on SIS, SIR and two-variant SEIR models. https://arxiv.org/abs/2512.02528
- Jang, Candan and Chowell, PLoS Computational Biology 2026, compare ABC, NPE, NPE-LSTM and preconditioned NPE and find that "additional simulations alone cannot resolve non-identifiability when multiple parameter combinations produce indistinguishable epidemic trajectories". https://pmc.ncbi.nlm.nih.gov/articles/PMC13252848/

## B5 LLM agents for epidemic modelling and forecasting

- Martinson et al. 2026 (B1) is the strongest evaluated case: prospective, multi-pathogen, hub-submitted. https://arxiv.org/abs/2605.16238
- Samaei et al., "EpidemIQs: Prompt-to-Paper LLM Agents for Epidemic Modeling and Analysis", arXiv 2025 revised 2026, report a 79 percent task success rate, about 870K tokens and 1.57 US dollars per study, judged by LLM-as-judge and human review. https://arxiv.org/abs/2510.00024
- Lu et al., "EpiEvolve: Self-Evolving Agents for Streaming Pandemic Forecasting under Regime Shifts", arXiv 2026-06-03, report 0.629 accuracy on COVID-19 hospitalisation trend classes against 0.561 for a static backbone and 0.325 for the CDC ensemble, and a recovery lag after regime shifts cut from five weeks to two. https://arxiv.org/abs/2606.05513
- Chae et al., "Auditable Context-Aware HFMD Forecasting with Structured LLM Agents", arXiv 2025 revised 2026, two-agent system with 90 percent interval coverage between 0.85 and 1.00 on Hong Kong and Lishui data. https://arxiv.org/abs/2511.23276
- "Integrating adaptive human behavior into epidemic models with large language models", arXiv 2026, reports LLM-generated contact matrices beating mobility-derived ones for short-term forecasts. https://arxiv.org/abs/2608.29535 (abstract via search only)
- Sam's own framing on the limits is in A2: LLMs "struggle with structural correctness as complexity increases" and an unsound model "could be worse than no AI at all".

## B6 Reinforcement learning for epidemic control

- Libin, Moonens, Verstraeten, Perez-Sanjines, Hens, Lemey and Nowé, "Deep reinforcement learning for large-scale epidemic control", arXiv 2020, ECML PKDD 2020 proceedings, learn school closure policies with PPO on a 379-district meta-population influenza model of Great Britain. https://arxiv.org/abs/2003.13676 and https://link.springer.com/chapter/10.1007/978-3-030-67670-4_10
- Reymond, Hayes, Willem, Rădulescu, Abrams, Roijers, Howley, Mannion, Hens, Nowé and Libin, "Exploring the Pareto front of multi-objective COVID-19 mitigation policies using reinforcement learning", arXiv 2022, extend Pareto Conditioned Networks to continuous actions on a Belgian stochastic compartmental model. https://arxiv.org/abs/2204.05027
- Bolshov and Chumachenko, "Reinforcement learning for policymaking in epidemic control: A scoping review", PLoS One 2026, include 13 studies from 2014 to 2025 and identify gaps in benchmarking, economic cost modelling, uncertainty quantification and "limited prospective validation or real-world deployment testing". https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0351176

## What a modeller might say about each

- Google in the hubs: the win is real and prospective, but the method is an LLM writing statistical models, and the earlier retrospective gain was attributable to data revision leakage (Bracher and Funk 2026).
- Time series foundation models: they do well zero-shot at one to four weeks with sparse data, and worse at turning points and peaks, which is where decisions are made (CAPE, Jafari et al.).
- Foundation models for epidemics: the PNAS perspective is a question, not a result, and CAPE's pretraining corpus is largely simulated compartmental models.
- UDEs: the neural part soaks up misspecification but also soaks up identifiability, and fitted mechanistic parameters may not mean what they did (Philipps et al. 2025).
- PINNs: they estimate time-varying rates from noisy data but are deterministic by default and extrapolate poorly outside the training window (Millevoi et al. 2024).
- Normalising flows and SBI: amortised inference makes agent-based and stochastic models fittable, but non-identifiability is inherited from the simulator and no amount of simulation fixes it (Jang et al. 2026).
- LLM agents: evaluations range from hub-submitted forecasts to LLM-as-judge on 79 percent task success, so read the evaluation before the headline.
- RL for control: policies beat heuristic baselines inside the simulator, and the scoping review finds almost no prospective or real-world validation.
- Sam's own line from the grants: the boundary between where AI assists and where expert input is required moves every year, so frame claims around structure and validation rather than model performance.
