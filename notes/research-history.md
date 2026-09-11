# Research notes for the outbreak modelling intro (keynote, 14 September 2026)

Compiled 11 September 2026 from local repos and the web.
Every external claim carries a URL.
Items marked "unverified" could not be confirmed against a primary source.
First-commit dates come from `git -C <repo> log --reverse --format=%ad --date=short | head -n 1`.
Do not use `git log --reverse -n 1`, because git applies the limit before reversing and returns the newest commit.
Repository creation dates come from `gh api repos/<org>/<repo> --jq .created_at`.

## 1. Sam's own milestones

| Date | What | Source |
|---|---|---|
| 28 November 2019 | PhD thesis "Modelling BCG vaccination in the UK: What is the impact of changing policy?", University of Bristol. | https://samabbott.co.uk/thesis/ and https://research-information.bris.ac.uk/en/studentTheses/modelling-bcg-vaccination-in-the-uk/ |
| 3 or 6 January 2020 | Started at LSHTM on real-time outbreak modelling, initially cholera. | JuliaCon bio says 3 January (`~/code/seabbs/JuliaCon2026/index.qmd`); the 2023 IISA talk post says 6 January (`~/code/seabbs/seabbs.github.io/_posts/2023-01-04-iisa-data-models-and-modellers-during-a-global-pandemic/`). The two sources disagree. |
| 7 or 12 January 2020 | Switched to 2019-nCoV. | JuliaCon bio says four days after starting; the IISA post says 12 January. The two sources disagree. |
| 3 February 2020 | First author, "The transmissibility of novel Coronavirus in the early stages of the 2019-20 outbreak in Wuhan", Wellcome Open Research. | https://doi.org/10.12688/wellcomeopenres.15718.1 |
| 28 February 2020 | Second author on Hellewell et al., "Feasibility of controlling COVID-19 outbreaks by isolation of cases and contacts", Lancet Global Health. | https://doi.org/10.1016/S2214-109X(20)30074-7 |
| 11 March 2020 | Listed as a working-group investigator, not a named author, on Kucharski et al., Lancet Infectious Diseases. | https://doi.org/10.1016/S1473-3099(20)30144-4 (Europe PMC record lists Abbott S under investigators) |
| 15 March 2020 | EpiNow repository created (predecessor of EpiNow2). | `gh api repos/epiforecasts/EpiNow` |
| 21 March 2020 | epiforecasts/covid repository created, the Rt dashboard at epiforecasts.io/covid. | `gh api repos/epiforecasts/covid` |
| 2020 (v1), 8 December 2020 (v2) | First author, "Estimating the time-varying reproduction number of SARS-CoV-2 using national and subnational case counts", Wellcome Open Research. | https://doi.org/10.12688/wellcomeopenres.16006.1 and https://researchonline.lshtm.ac.uk/id/eprint/4661411/ |
| 17 June 2020 | EpiNow2 first commit, "clean copy of EpiNow". | `~/code/epiforecasts/EpiNow2`, first commit command above |
| 23 July 2020 | EpiNow2 v1.0.0 tag. | `git -C ~/code/epiforecasts/EpiNow2 for-each-ref --sort=creatordate refs/tags` |
| 1 September 2020 | EpiNow2 1.1.0, first CRAN release. | https://cran.r-project.org/src/contrib/Archive/EpiNow2/ |
| 2020 to 2022 | Weekly Rt estimates, short-term forecasts and ad hoc reports to SPI-M-O and SAGE. | Sam's own grant text, `~/code/archive/composable-grant/coapplicant_details/sam.qmd` line 89; SPI-M-O consensus statements at https://www.gov.uk/government/publications/spi-m-o-consensus-statement-on-covid-19-6-january-2021 |
| 13 January 2021 | European Covid-19 Forecast Hub repository created. | `gh api repos/european-modelling-hubs/covid19-forecast-hub-europe` |
| 29 October 2021 | epinowcast first commit; v0.0.2 tagged 1 November 2021. | `~/code/epinowcast/epinowcast` |
| 31 March 2022 | Last day of global Rt estimates on the dashboard, after more than two years. | `~/code/seabbs/seabbs.github.io/_posts/2022-03-25-rt-reflections/rt-reflections.Rmd` |
| 2022 | Co-author on Endo et al., "Heavy-tailed sexual contact networks and monkeypox epidemiology in the global outbreak, 2022", Science. | https://doi.org/10.1126/science.add4507 |
| 2 November 2022 | Co-author on the BMJ editorial "The dynamics of monkeypox transmission" (Freeman, Abbott, Kurpiel), which accompanied Ward et al. | https://doi.org/10.1136/bmj.o2504 |
| 2022 | Consultancy support to CDC and UKHSA on mpox. | Sam's grant text, `sam.qmd` line 89; self-reported, unverified externally |
| 18 October 2022 | epidist first commit; v0.0.1 tagged 29 October 2022. | `~/code/epinowcast/epidist` |
| 21 April 2023 | Co-author on Sherratt et al., European Forecast Hub ensemble evaluation, eLife. | https://doi.org/10.7554/eLife.81916 (Europe PMC lists Abbott S) |
| 2023 | Second author on Overton et al., "Nowcasting the 2022 mpox outbreak in England", PLOS Computational Biology. | https://doi.org/10.1371/journal.pcbi.1011463 |
| 5 February 2024 | CDCgov/Rt-without-renewal repository created, home of EpiAware.jl, the start of the Julia work. | `gh api repos/CDCgov/Rt-without-renewal` |
| 4 June 2024 | Earliest local EpiAware-org repo first commit (ReparameterisedDistributions.jl); CensoredDistributions.jl 24 September 2024; EpiAware/.github 30 September 2024. | `~/code/EpiAware/*`, first commit command above |
| 21 August 2024 | primarycensored first commit; v0.1.0 tagged 3 September 2024. | `~/code/epinowcast/primarycensored` |
| 19 May 2026 | BVDOutbreakSize and bdbv-linelist-analysis first commits, one day after the McCabe et al. report. | `~/code/seabbs/BVDOutbreakSize`, `~/code/epiforecasts/bdbv-linelist-analysis` |
| 10 June 2026 | WHO collaboratory call talk on the BVD outbreak size model. | `~/code/seabbs/BVDOutbreakSize/slides/bdbv_collaboratory_20260610.qmd` |
| 9 September 2026 | Latest local BVDOutbreakSize commit; 145 tags, latest release results-v1.18.0 with data to SitRep 115 (6 September). | `git -C ~/code/seabbs/BVDOutbreakSize tag`, `docs/src/news.md` |

## 2. Outbreak timeline 2014 to 2026

### Ebola, West Africa, 2014 to 2016 (others' work, before Sam entered the field)

- WHO was notified of the Guinea outbreak on 23 March 2014 and declared a PHEIC on 8 August 2014.
- WHO Ebola Response Team, NEJM, 23 September 2014, reported 4507 cases by 14 September, CFR 70.8 percent, and forward projections. https://doi.org/10.1056/NEJMoa1411100
- Meltzer et al., MMWR, September 2014, projected 550,000 reported cases, 1.4 million corrected for under-reporting, in Liberia and Sierra Leone by 20 January 2015 without further intervention. https://www.cdc.gov/mmwr/preview/mmwrhtml/su6303a1.htm
- Around 21,000 cases had occurred by mid-January 2015; the debate ran in Butler, Nature 2014, "Models overestimate Ebola cases" (https://www.nature.com/articles/515018a) and Rivers, Nature 2014, "Ebola: models do more than forecast" (https://pubmed.ncbi.nlm.nih.gov/25428492/); CDC's own account is at https://www.cdc.gov/mmwr/volumes/65/su/su6503a12.htm
- Camacho et al., PLOS Currents Outbreaks, 10 February 2015, estimated district-level R in Sierra Leone in real time and forecast cases to March 2015. https://currents.plos.org/outbreaks/article/temporal-changes-in-ebola-transmission-in-sierra-leone-and-implications-for-control-requirements-a-real-time-modelling-study/
- Funk et al., Epidemics, 2018 (online December 2016), described the semi-mechanistic model used for the real-time Sierra Leone forecasts. https://doi.org/10.1016/j.epidem.2016.11.003
- Funk et al., PLOS Computational Biology, 2019, assessed those real-time forecasts against what happened in Western Area, Sierra Leone. https://doi.org/10.1371/journal.pcbi.1006785
- Sam was not an author on any of these; Funk, Camacho, Kucharski and Edmunds became his colleagues at LSHTM from January 2020.

### COVID-19, 2020 to 2023 (Sam's own work, alongside others')

- Others: Imai et al., Imperial Report 2, 22 January 2020, estimated 4000 cases (1000 to 9700) in Wuhan by 18 January. https://spiral.imperial.ac.uk/entities/publication/c8551280-787c-40c4-89e1-a261117c6579
- Sam's own: Abbott et al., Wellcome Open Research, 3 February 2020, scenario analysis of early Wuhan transmissibility. https://doi.org/10.12688/wellcomeopenres.15718.1
- Sam's own: Hellewell, Abbott et al., Lancet Global Health, 28 February 2020, feasibility of control by isolation and contact tracing. https://doi.org/10.1016/S2214-109X(20)30074-7
- Others, with Sam in the working group: Kucharski et al., Lancet Infectious Diseases, 11 March 2020, on Wuhan transmission dynamics. https://doi.org/10.1016/S1473-3099(20)30144-4
- The CMMID COVID-19 working group page lists the group and its outputs. https://cmmid.github.io/groups/ncov-group.html and https://cmmid.github.io/topics/covid19/
- Sam's own: Abbott et al., Wellcome Open Research, 2020, national and subnational Rt estimates, the method behind the dashboard and EpiNow2. https://doi.org/10.12688/wellcomeopenres.16006.1
- Sam's own: EpiNow2 on CRAN from 1 September 2020. https://cran.r-project.org/package=EpiNow2
- Sam's own: weekly estimates to SPI-M-O; consensus statements are on GOV.UK. https://www.gov.uk/government/publications/spi-m-o-consensus-statement-on-covid-19-6-january-2021
- Others, with Sam as a named author: Sherratt et al., eLife, 21 April 2023, ensemble of the European Covid-19 Forecast Hub across 32 countries from March 2021; the ensemble beat 83 percent of case forecasts and 91 percent of death forecasts by relative WIS. https://doi.org/10.7554/eLife.81916
- Sam's account of the pandemic years, by year, is in the 2023 IISA post (data, models, modellers), at `~/code/seabbs/seabbs.github.io/_posts/2023-01-04-iisa-data-models-and-modellers-during-a-global-pandemic/`.

### mpox, 2022 and 2024

- WHO declared the multi-country monkeypox outbreak a PHEIC on 23 July 2022, with more than 16,000 cases in 75 countries. https://www.who.int/news-room/speeches/item/who-director-general-s-statement-on-the-press-conference-following-IHR-emergency-committee-regarding-the-multi--country-outbreak-of-monkeypox--23-july-2022
- Others: Ward et al., BMJ, 2 November 2022, UK contact tracing study; mean incubation 7.6 to 7.8 days, mean serial interval 8.0 to 9.5 days, with evidence of presymptomatic transmission. https://doi.org/10.1136/bmj-2022-073153
- Sam is not an author on Ward et al. (Europe PMC author string: Ward T, Christie R, Paton RS, Cumming F, Overton CE).
- Sam's own: the BMJ editorial accompanying Ward et al., Freeman, Abbott, Kurpiel, "The dynamics of monkeypox transmission". https://doi.org/10.1136/bmj.o2504
- Sam's own: Endo et al., Science, 2022, heavy-tailed sexual contact networks and the 2022 outbreak. https://doi.org/10.1126/science.add4507
- Sam's own: Overton, Abbott et al., PLOS Computational Biology, 2023, nowcasting the 2022 mpox outbreak in England for UKHSA. https://doi.org/10.1371/journal.pcbi.1011463
- Sam's own: Murayama, Pearson, Abbott et al., Journal of Infectious Diseases, 2024, accumulation of immunity in heavy-tailed networks. https://doi.org/10.1093/infdis/jiad254
- Sam's own: consultancy to CDC and UKHSA in 2022 (self-reported in grant text, `sam.qmd` line 89; unverified externally).
- Others: WHO declared the clade Ib upsurge in DRC and neighbouring countries a PHEIC on 14 August 2024, with more than 15,600 cases and 537 deaths reported that year. https://www.who.int/news/item/14-08-2024-who-director-general-declares-mpox-outbreak-a-public-health-emergency-of-international-concern
- No local evidence of Sam's own work on clade Ib in 2024 was found in `~/code`.

### Ebola disease caused by Bundibugyo virus, DRC and Uganda, 2026 (Sam's own live work)

- WHO was alerted on 5 May 2026 to a high-mortality illness in Mongbwalu health zone, Ituri; DRC declared its 17th Ebola outbreak on 15 May; the Director-General declared a PHEIC on 17 May. https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602
- The first Uganda import was admitted in Kampala on 11 May and died on 14 May. https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602
- Others: McCabe et al., Imperial College London, 18 May 2026, estimated outbreak size from Uganda exports and from deaths; updated 20 May (400 to 900 cases); Lancet Infectious Diseases correspondence 9 June 2026. https://doi.org/10.25560/130007 and https://doi.org/10.1016/S1473-3099(26)00299-9
- Others: Chamla et al., Lancet Infectious Diseases, 25 June 2026, stochastic SEIRD projection of confirmed cases. https://doi.org/10.1016/S1473-3099(26)00320-8
- Sam's own: BVDOutbreakSize, first commit 19 May 2026, replicates McCabe et al. then extends it to a joint renewal model fitted to INSP situation report streams, digitised onset curves and Uganda exports; refit on every push with 145 tagged releases by 9 September. https://epiforecasts.io/BVDOutbreakSize/stable/ and https://github.com/epiforecasts/BVDOutbreakSize
- Sam's own: bdbv-linelist-analysis with Sebastian Funk, delay distributions and CFR from the 2012 Isiro line list (n = 52) of Rosello et al. 2015. https://epiforecasts.io/bdbv-linelist-analysis/dev and https://doi.org/10.7554/eLife.09015
- Status as of 7 September 2026 (WHO DON617, published 10 September): 6757 confirmed cases and 3267 deaths in DRC, CFR 48.3 percent; 20 confirmed cases and 2 deaths in Uganda; six provinces and 61 health zones; 963 new confirmed cases since the 28 August update. https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON617
- The same WHO update states that evidence is insufficient to support programmatic use of Ervebo for BVD, with 2007 people vaccinated under research protocols by 6 September. https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON617
- Local cross-check: INSP SitRep 115 (report date 6 September) gives 6686 confirmed cases, 3226 confirmed deaths, 819 in isolation, 1563 recovered (`~/code/seabbs/BVDOutbreakSize/data/insp_sitrep_scanned.csv`).
- WHO describes this as the largest Ebola disease outbreak recorded in DRC and the second BVD outbreak there after 2012. https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON616

## 3. Deep history anchors (one slide)

- 1760: Daniel Bernoulli read his smallpox inoculation memoir to the Paris Academy on 30 April 1760 (published 1766); see Dietz and Heesterbeek 2002. https://doi.org/10.1016/S0025-5564(02)00122-0
- 1911: Ronald Ross, The Prevention of Malaria, second edition, gave a differential equation model with a mosquito density threshold. https://archive.org/details/pr00eventionofmalarossrich and https://doi.org/10.1371/journal.ppat.1002588
- 1927: Kermack and McKendrick, "A contribution to the mathematical theory of epidemics", Proceedings of the Royal Society A. https://doi.org/10.1098/rspa.1927.0118
- 1991: Anderson and May, Infectious Diseases of Humans: Dynamics and Control, Oxford University Press. https://academic.oup.com/book/53038
- 2001: UK foot-and-mouth epidemic modelled in real time; Ferguson, Donnelly and Anderson, Science (https://doi.org/10.1126/science.1061020) and Keeling et al., Science (https://doi.org/10.1126/science.1065973).
- 2009: Fraser et al., Science, 11 May 2009 online, early assessment of pandemic H1N1 with the WHO Rapid Pandemic Assessment Collaboration. https://doi.org/10.1126/science.1176062

## 4. Candidate figures on disk

All paths are absolute under `/Users/lshsa2/code/`.

- `seabbs/JuliaCon2026/figures/bvd-insp-sitreps.png`: an INSP situation report page in French (used 13 August 2026 slides).
- `seabbs/JuliaCon2026/figures/bvd-outbreak-streams.png`: posterior cumulative infections per data stream and joint fit, data as of 7 June 2026.
- `seabbs/JuliaCon2026/figures/bvd-rt-over-time.png`: Rt trajectories, data as of 7 June 2026.
- `seabbs/JuliaCon2026/figures/bvd-generative-process.svg` and `seabbs/JuliaCon2026/figures/fig-bvd-model.png`: model schematics, vintage-independent.
- `seabbs/BVDOutbreakSize/slides/figures/`: `generative-process.svg`, `outbreak_streams.png`, `rt-over-time.png`, `size-trajectory.png`, `validation-mccabe.png`, `validation-ppc.png`, `validation-earlier.png`, `insp_sitreps.png`, all from the 10 June 2026 talk.
- `seabbs/how-I-llm/figures/rt-over-time.png`: Rt fit to 29 June 2026 data, with an attribution caveat; `seabbs/how-I-llm/figures/bvd-authorship.png`: commit authorship chart (390 commits, 291 bot, 29 July 2026).
- `seabbs/seabbs.github.io/_posts/2022-03-25-rt-reflections/example-rt.png`: an example Rt estimate from the COVID-19 dashboard.
- `seabbs/JuliaCon2026/figures/composable-epinow2-results.png` and `composable-epinow2-model.png`: EpiNow2 output and model figures.
- `seabbs/JuliaCon2026/figures/workflow-schematic.png`: the nine-step infectious disease modelling workflow.
- `seabbs/JuliaCon2026/figures/delays-fit.png`, `delays-right-truncation.png`, `delays-double-censoring.png`: delay estimation figures.
- Note from `seabbs/JuliaCon2026/notes/bvd.md`: the BVDOutbreakSize `output/` folder is a stale 20 May cache; current figures live in the GitHub Release and the live site, so download from https://github.com/epiforecasts/BVDOutbreakSize/releases/latest for a September vintage.
- Local BVD figures on disk are all June or July vintages; the numbers on them have moved (Rt and size estimates changed materially through the summer, per `docs/src/news.md`).

## 5. Numbers Sam has stated publicly

| Claim | Where stated | Status |
|---|---|---|
| Dashboard "used by over a million people" | JuliaCon 2026 bio, `seabbs/JuliaCon2026/index.qmd` | Partly verified. The March 2022 blog post gives just over 500 thousand unique users since April 2020 and 1.2 million page views; the January 2023 IISA post says the platform "ended the pandemic with > 1 million unique users". The two figures differ; the bio's phrasing matches page views or the later unique-user count. |
| Tools "used by upwards of 30 public health agencies" | JuliaCon 2026 bio | Unverified. No list of 30 agencies was found in `~/code`. Grant text names WHO, ECDC, CDC, MSF, RKI and UKHSA. |
| Weekly estimates to UK government advisory bodies (SPI-M-O, SAGE) | JuliaCon bio; grant text `archive/composable-grant/coapplicant_details/sam.qmd` line 89 | Self-reported; SPI-M-O consensus statements exist on GOV.UK but do not name contributors individually. |
| Rt estimated daily for "several thousand" or "4k+" locations | 2022 rt-reflections post; 2023 IISA post | Self-reported, consistent across the two posts. |
| EpiNow2 58,073 CRAN downloads, 141 stars; epinowcast 67 stars; primarycensored 11,294 downloads | `seabbs/JuliaCon2026/roadmap/_partials/04-r.qmd`, dated 11 to 13 August 2026 | Verified at the time from cranlogs and the GitHub API; GitHub API on 11 September 2026 gives EpiNow2 140 stars, epinowcast 67. |
| BVDOutbreakSize about 35,000 lines of Julia; 442 commits with 78 percent from bot identities as of 8 August 2026 | `seabbs/JuliaCon2026/roadmap/_partials/00-outbreak.qmd`; `notes/bvd.md` | Verified locally on those dates; counts have grown since. |
| "Six years of trying this in R and Stan" | `04-r.qmd` | Consistent with EpiNow first commit March 2020. |
| Start dates 3 January 2020 and switch to nCoV four days later | JuliaCon bio | Contradicted by the 2023 IISA post (6 January and 12 January). Pick one and say which source. |
| Worked "~18 hours a day for about 6 months" in 2020 | 2023 IISA post | Self-reported. |

## Gaps

- Sam's Google Scholar could not be fetched; authorship was checked through Europe PMC records instead.
- The Lancet, PubMed and Wellcome Open Research pages returned 403 or cookie walls; DOIs are given and dates come from Europe PMC or search summaries.
- No authorship or code for 2024 clade Ib mpox work was found locally.
- The exact first publication date of the subnational Rt paper (v1) was not confirmed; Europe PMC dates v2 to 8 December 2020.
