# Open questions for Sam

Everything the agent rounds could not settle, in one place, so the round
reports can be deleted.
Written 13 September 2026, after the audit and fix passes on all three
decks.

## Decide before the day

**EpiDelays on the exchange stage.**
The "Agents building methods into software" slide names a UHasselt
package rewired onto the `primarycensored` likelihood.
UHasselt is half the SIMID group in the room, the package is Oswaldo
Gressani's, and the pull request from the bot has been open since April.
It is the most direct bridge to that audience, and it is also a public
comment on an unmerged pull request of his.

**The bio on the home page.**
`index.qmd:118-123` carries the JuliaCon text verbatim, including a
dashboard "used by over a million" people and "upwards of 30 public
health agencies".
Neither number was verified by the research pass.

**The two live iframes.**
The BVDOutbreakSize summary page in the keynote and the UK dashboard in
the lecture both need a test on venue wifi.
Both have static fallbacks.

**Slide counts.**
Keynote 39 content slides, exchange 31, communication 24.
Sam is auditing density himself.

## Facts to confirm

**UKHSA and nowcasting.**
Overton, Abbott et al. 2023 gives the reason as permissions on UKHSA's
managed IT systems, not installation.
The slide says install.

**Clara Brigitta.**
`epinowcast.github.io/seminars.qmd:19` names Fanny Bergström and Clara
Brigitta as the seminar organisers, so the names are sourced, but
"Clara Brigitta" reads like two given names.

**The epidist meta-analysis figure.**
`figures/exchange-epidist-meta-bdbv.png` could not be traced to a local
repo, because `bdbv-linelist-analysis` is not cloned on this machine.

**The Endo et al. mpox figure** in the keynote is a Science figure
reused from the JuliaCon deck, not CC BY.

**The language model answers** in the communication deck were collected
through the CLI, which passed Sam's email address to the models, so the
run was not blind.
Rerun through the API if a clean answer matters.

## Wording he may want back

**"The workflow is what kept it reviewable"**, his own sentence from
`02ca043`, was lost when three of his lines were merged into
`keynote/_partials/03-agents.qmd:163-164`.
The surviving bullet makes the same point in other words.

**"About half"** at `communication/_partials/03-with.qmd:92`.
He cut this claim from the keynote.
It survives here as the example of a claim that checking caught and
corrected, which is that slide's point.

**Rackauckas et al. 2020c** is now cited as 2020 at
`keynote/_partials/02-ai-methods.qmd:75`.

## Loose ends

**Charlotte Holt** is named on a UDE slide in both the keynote and the
exchange deck with no photo; her GitHub account has no name or activity.

**The four exchange figures** (`exchange-seir-vs-ude`, `exchange-pinn`,
`exchange-epiaware-approaches`, `exchange-epidist-meta-bdbv`) arrived
without a drawing script, so they cannot be regenerated.

**The initials tiles** on the collaborator grids stand in for people
whose GitHub avatars are not faces.
Drop a photo into `figures/` as `exchange-people-<name>.jpg` to replace
one.
