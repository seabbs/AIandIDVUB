#!/usr/bin/env bash
# Regenerate the QR codes that appear on each deck's plan and closing slides.
# Each QR points at the talk's page on this site, not at the slides.
set -euo pipefail

cd "$(dirname "$0")"

BASE="https://samabbott.co.uk/AIandIDVUB"

for talk in keynote communication exchange; do
  uvx --from segno segno \
    --output "qr-${talk}.png" \
    --scale 10 --border 2 --error H \
    --dark "#333333" --light "#ffffff" \
    "${BASE}/${talk}/"
done
