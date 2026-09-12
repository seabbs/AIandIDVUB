#!/usr/bin/env bash
# Fetch GitHub avatars for the collaborator slides in exchange/_partials/
# 01b-people.qmd. Source of names and logins: notes/research-collaborators.md.
set -euo pipefail

cd "$(dirname "$0")/.."

logins=(
  sbfnk jamesmbaazam nikosbosse kathsherratt Bisaloo joeHickson medewitt
  hsbadr
  adrian-lison kaitejohnson athowes pearsonca kcharniga parksw3 TimTaylor
  SamuelBrand1 damonbayer jcblemai jasonasher
)

for login in "${logins[@]}"; do
  lower=$(echo "$login" | tr '[:upper:]' '[:lower:]')
  out="figures/exchange-people-${lower}.jpg"
  echo "fetching $login -> $out"
  curl -sL -o "$out" "https://github.com/${login}.png?size=400"
done
