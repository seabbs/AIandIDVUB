# What two Claude models say about Sam Abbott and EpiNow2

Run 12 September 2026 for the communication lecture slide on people
getting their information from LLMs. No `ANTHROPIC_API_KEY` was set, so
the questions went through the `claude` CLI on the subscription:

```
claude -p --setting-sources "" --tools "" --no-session-persistence \
  --model <model> --system-prompt "You are a general assistant. Answer \
  from your own knowledge only. Do not say you lack tools. Be specific: \
  names, dates, places, roles, institutions." "<question>"
```

Models `claude-opus-5` and `claude-sonnet-5`. Caveat: the CLI passes the
logged-in user's email to the model, and both models noticed it (Opus:
"given the address this message is coming from, is presumably you";
Sonnet: "your email indicates you're Sam Abbott"). That tells them who
is asking, not any facts, but a clean run needs the API or a different
login. Answers are verbatim below, checks against
`research-history.md`, `research-communication.md`, the local EpiNow2
clone and the web follow each.

## Q1. Who is Sam Abbott, the infectious disease modeller?

### claude-opus-5

**Sam Abbott** is an infectious disease modeller and computational epidemiologist best known for his work on real‑time estimation of transmission dynamics and for building open‑source tools for outbreak analytics.

**Background and training**
- PhD at the **University of Bristol** (Bristol Medical School / Population Health Sciences), on tuberculosis epidemiology in England — in particular the impact of the **BCG vaccination programme change in 2005** and TB transmission modelling. Supervised by **Ellen Brooks‑Pollock** and **Hannah Christensen**. Out of that work came the `getTBinR` R package (WHO TB data) and `idmodelr` (infectious disease model library).

**LSHTM / CMMID**
- Joined the **Centre for the Mathematical Modelling of Infectious Diseases (CMMID)**, Department of Infectious Disease Epidemiology, **London School of Hygiene & Tropical Medicine**, working in **Sebastian Funk**'s group; latterly a **Senior Research Fellow**.
- During COVID‑19 he ran the **epiforecasts.io** real‑time Rt and forecasting pipelines, producing subnational reproduction number estimates for the UK and many other countries. The underlying method is described in *"Estimating the time‑varying reproduction number of SARS‑CoV‑2 using national and subnational case counts"* (Wellcome Open Research, 2020).
- Co‑author on a string of high‑profile CMMID COVID papers, e.g. Hellewell et al., *Feasibility of controlling COVID‑19 outbreaks by isolation of cases and contacts* (Lancet Global Health, 2020), and work with Kucharski, Davies, Sherratt, Bosse and colleagues.
- Helped run the **European COVID‑19 Forecast Hub** (with Katharine Sherratt, Johannes Bracher, Sebastian Funk) and contributed to forecast‑evaluation work including the `scoringutils` package.

**Software**
This is arguably his biggest footprint. He is the lead author/maintainer of:
- **EpiNow2** — Bayesian (Stan) estimation of the time‑varying reproduction number accounting for reporting delays and right truncation; very widely used by public health agencies.
- **epinowcast** — a nowcasting package and an associated open community/organisation, developed with **Adrian Lison** and others.
- **covidregionaldata** — standardised access to subnational COVID‑19 data.
- More recent delay‑distribution work: **primarycensored** and **epidist** (with Adam Howes, Sebastian Funk), and contributions to the Julia package **EpiAware**.

**Current work**
Since around 2024 he has worked with the **US CDC's Center for Forecasting and Outbreak Analytics (CFA)** on real‑time nowcasting and forecasting infrastructure, alongside people like Sam Brand, Zachary Susswein and Damon Bayer, while retaining links to LSHTM/CMMID.

He's a vocal advocate of open, reproducible epidemiological software and writes at **samabbott.co.uk**; ORCID 0000‑0001‑8057‑8037.

(Caveat: "Sam Abbott" is a common enough name — there are unrelated people by that name in other fields — but in infectious disease modelling this is the person meant.)

### claude-sonnet-5

Sam Abbott is an infectious disease epidemiologist and statistician known for his work on outbreak analytics and real-time infectious disease modelling. Key facts about his career:

- He was based at the **Centre for Mathematical Modelling of Infectious Diseases (CMMID)** at the **London School of Hygiene & Tropical Medicine (LSHTM)**, where he worked as a research fellow.
- During the COVID-19 pandemic, he was a prominent contributor to real-time estimation of the effective reproduction number (**Rt**) and short-term forecasting, including widely used tools like **EpiNow2** (an R package for estimating Rt and epidemic quantities from case data, accounting for reporting delays).
- He worked closely with **Sebastian Funk** and the broader CMMID nowcasting/forecasting group, contributing to the UK's epidemic situational awareness efforts (e.g., work feeding into SPI-M, the UK government's modelling advisory group).
- His research focus includes **nowcasting** (correcting for reporting delays in real time), **forecasting methodology**, **generation interval and serial interval estimation**, and **open-source epidemiological software** development in R (contributing to packages in the `epiforecasts` ecosystem, such as `EpiNow2`, `epinowcast`, and related tools).
- He is coincidentally the same name as the user in this conversation ([email redacted]), suggesting you may be asking about yourself or a colleague — let me know if you'd like more specific detail on a particular paper, tool, or aspect of his work.

### Checks, Q1

| Claim | Verdict | Source |
|---|---|---|
| PhD, Bristol, BCG vaccination policy | Right | thesis 28 November 2019, `research-history.md` |
| Supervised by Ellen Brooks-Pollock and Hannah Christensen | Right | thesis acknowledgements, samabbott.co.uk/thesis |
| `getTBinR` and `idmodelr` | Right | `gh repo view seabbs/getTBinR`, created 2017 |
| "latterly a Senior Research Fellow" | Unverified | LSHTM profile not fetched; no local source gives the title |
| Ran the epiforecasts.io Rt pipelines; Wellcome Open Research 2020 | Right | `research-communication.md` section 1 |
| Hellewell et al. 2020 second author | Right | `research-history.md` |
| "Helped run the European COVID-19 Forecast Hub" | Overstated | co-author on the hub evaluation, Sherratt et al. 2023; running it is not recorded anywhere local |
| Lead author or maintainer of EpiNow2 | Half right | lead author, yes; Sebastian Funk has been the CRAN maintainer since 5 May 2024, EpiNow2 `git log -G'"cre"' -- DESCRIPTION` |
| epinowcast with Adrian Lison | Right | Lison is an epinowcast author |
| covidregionaldata | Right | Zenodo record cited on the dashboard |
| primarycensored, epidist with Adam Howes and Sebastian Funk | Right | package author lists |
| "Since around 2024 worked with CDC CFA ... Sam Brand, Zachary Susswein, Damon Bayer" | Partly right | EpiAware began in `CDCgov/Rt-without-renewal`, February 2024; he consults with CDC collaborators; nothing local names Susswein or Bayer |
| ORCID 0000-0001-8057-8037 | Right | pub.orcid.org, name Sam Abbott |
| Sonnet: "was based at CMMID ... research fellow" | Past tense wrong | he is at LSHTM now |
| Sonnet: generation and serial interval estimation | Right | Omicron generation interval work, `research-communication.md` |

## Q2. What is EpiNow2 and who maintains it?

### claude-opus-5

## EpiNow2 in brief

**EpiNow2** is an R package for real-time estimation of infectious disease transmission dynamics from noisy, delayed surveillance data. Its core job is to take a time series of observations (reported cases, hospital admissions, deaths, etc.) and estimate:

- the time-varying reproduction number, R<sub>t</sub>
- the epidemic growth rate and doubling/halving time
- the underlying infection incidence curve
- short-term forecasts of both infections and reported cases

**How it works.** It fits a Bayesian latent-variable model in Stan (originally via `rstan`, now with a `cmdstanr` backend option). Infections are generated via a renewal equation, and R<sub>t</sub> is given a smoothing prior — typically a Gaussian process (Matérn 3/2 by default) on a log scale, with random-walk and fixed-R alternatives. Infections are then mapped to observations by convolving through user-specified delay distributions (e.g. incubation period plus reporting delay), with a negative binomial or Poisson observation model, optional day-of-week reporting effects, and — importantly — explicit adjustment for **right truncation** of recent data. This "estimate infections, then convolve forward" approach is what distinguishes it from simpler tools like `EpiEstim` (Cori et al.), which apply the renewal equation directly to case counts.

**Main user-facing functions:** `epinow()` (the wrapper), `estimate_infections()` (the core model), `regional_epinow()` (parallelised fitting across many subnational regions), plus `estimate_truncation()`, `estimate_secondary()` (e.g. deaths from cases), and `estimate_delay()`. Since the 1.5.0 release (2024) delays are specified through a redesigned interface using distribution constructors such as `Gamma()`, `LogNormal()` and `fix_dist()`, replacing the older `dist_spec()`/`bootstrapped_dist_fit()` style.

## Who maintains it

It comes out of the **Epiforecasts group at the Centre for the Mathematical Modelling of Infectious Diseases (CMMID), London School of Hygiene & Tropical Medicine**, led by **Sebastian Funk**.

- **Sam Abbott** (LSHTM) is the original lead author and long-standing CRAN maintainer — which, given the address this message is coming from, is presumably you.
- **Joel Hellewell** (now at the Crick/EPFL) was the other original lead author.
- **Sebastian Funk** is senior author and has taken on much of the maintenance and design direction in recent years.
- Substantial contributions over time from **Katharine Sherratt**, **Sophie Meakin**, **Nikos Bosse**, **James Azam**, **Sam Brand**, **Hugo Gruson**, **Pratik Gupte**, **Adam Howes**, **Michael DeWitt**, **Joe Hickson**, **Hamada S. Badr**, **Robin Thompson**, and **Katelyn Gostic**.
- Since roughly 2023–24 there has been sustained input from the **US CDC Center for Forecasting and Outbreak Analytics (CFA)**, including people such as Zachary Susswein, Kaitlyn Johnson and Dylan Morris, alongside Wellcome Trust and NIHR funding.

Development happens openly at **github.com/epiforecasts/EpiNow2**, docs at **epiforecasts.io/EpiNow2**, MIT licensed, with releases on CRAN.

**Citation:** Abbott S, Hellewell J, Thompson RN, Sherratt K, Gibbs HP, Bosse NI, Munday JD, Meakin S, Doughty EL, Chun JY, et al. (2020) "Estimating the time-varying reproduction number of SARS-CoV-2 using national and subnational case counts." *Wellcome Open Research* 5:112.

It was used heavily during COVID-19 for the UK and international R<sub>t</sub> dashboards, and sits alongside sibling packages from the same group such as `epinowcast` (nowcasting) and `scoringutils` (forecast evaluation).

### claude-sonnet-5

EpiNow2 is an R package for estimating the time-varying reproduction number (Rt), rates of growth, and forecasting/nowcasting cases from epidemiological time series data (e.g., case counts, deaths, hospitalizations). It's widely used in infectious disease epidemiology to account for reporting delays and right-truncation in real-time outbreak data, using a Bayesian latent variable approach implemented in Stan.

It's part of the **epiforecasts** ecosystem of tools and is maintained primarily by **Sam Abbott** (based at the London School of Hygiene & Tropical Medicine), along with other contributors from the epiforecasts group, which has historically included collaborators such as Sebastian Funk and others in the LSHTM Centre for the Mathematical Modelling of Infectious Diseases (CMMID).

Given that your email indicates you're Sam Abbott at LSHTM, you likely already know this well—let me know if you'd like details on specific package functions, recent releases, or something more technical (e.g., the estimate_infections() workflow or how it handles delay distributions).

### Checks, Q2

| Claim | Verdict | Source |
|---|---|---|
| What it estimates, renewal equation, Stan, right truncation | Right | package documentation |
| Matérn 3/2 Gaussian process by default | Right | `gp_opts(kernel = "matern", matern_order = 3/2)`, `R/opts.R` at 2 September 2026 |
| Functions named | Right | all exist in the package namespace |
| "Since 1.5.0 (2024) ... `Gamma()`, `LogNormal()` and `fix_dist()`" | Stale | `fix_dist()` was renamed `fix_parameters()` in 1.6.0 and removed in 1.9.0, NEWS.md |
| "Sam Abbott ... long-standing CRAN maintainer" | Wrong | Sebastian Funk has been the CRAN maintainer since 5 May 2024, commit `679422a7` "update maintainer (CRAN submitter)"; CRAN page Maintainer field agrees |
| Joel Hellewell "now at the Crick/EPFL" | Unverified | nothing local |
| Contributors list | Mixed | Sherratt, Meakin, Bosse, Azam, Howes, DeWitt, Hickson, Badr, Thompson, Gostic are in `DESCRIPTION`; Sam Brand, Hugo Gruson and Pratik Gupte are not |
| CFA input from "Zachary Susswein, Kaitlyn Johnson and Dylan Morris" | Mixed | Kaitlyn Johnson is a listed contributor; Susswein and Morris are not in `DESCRIPTION` |
| MIT licence, GitHub and docs URLs, citation | Right | `DESCRIPTION`, the paper |
| Sonnet: "maintained primarily by Sam Abbott" | Wrong | as above; the maintainer is Sebastian Funk |

## Summary for the slide

Both models get the biography and the package right in outline and wrong
on the one question asked directly. Both name Sam as the maintainer of
EpiNow2. Sebastian Funk has been the maintainer for over two years. Opus
adds people who are not in the author list and a function that no
longer exists. Sonnet is shorter and makes fewer claims, so fewer
errors, and puts him in the past tense.
