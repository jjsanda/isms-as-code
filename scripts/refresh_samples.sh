#!/usr/bin/env bash
# Copy a curated set of signed PDFs from a build into docs/samples/ and refresh the cover-page
# screenshots under docs/screenshots/, so the README works without running a build.
# Usage: ./scripts/refresh_samples.sh [dist-dir]
set -euo pipefail
cd "$(dirname "$0")/.."
DIST="${1:-dist}"
SAMPLES="docs/samples"
SHOTS="docs/screenshots"
mkdir -p "$SAMPLES" "$SHOTS"
rm -f "$SAMPLES"/*.pdf "$SAMPLES"/SHA256SUMS "$SAMPLES"/*.pem "$SHOTS"/*.png

pick() {
  local pattern="$1"
  local file
  file="$(ls "$DIST"/pdf/$pattern 2>/dev/null | sort -V | tail -1 || true)"
  [ -n "$file" ] && cp "$file" "$SAMPLES/"
}
pick "POL-ISMS-*.pdf"
pick "POL-ACC-*.pdf"
pick "PROC-IR-*.pdf"
pick "statement-of-applicability.pdf"
pick "isms-scope-statement.pdf"
cp "$DIST/signing-trust-anchor.pem" "$SAMPLES/"
( cd "$SAMPLES" && sha256sum *.pdf *.pem > SHA256SUMS )

if command -v pdftoppm >/dev/null 2>&1; then
  for pdf in "$SAMPLES"/POL-ACC-*.pdf "$SAMPLES"/statement-of-applicability.pdf; do
    name="$(basename "$pdf" .pdf)"
    pdftoppm -png -r 70 -f 1 -l 1 "$pdf" "$SHOTS/$name-cover"
    pdftoppm -png -r 70 -f 2 -l 2 "$pdf" "$SHOTS/$name-page2"
  done
  # pdftoppm appends the page number; normalise the names.
  for f in "$SHOTS"/*-cover-*.png; do mv "$f" "${f%-*}.png"; done 2>/dev/null || true
  for f in "$SHOTS"/*-page2-*.png; do mv "$f" "${f%-*}.png"; done 2>/dev/null || true
fi
echo "samples refreshed: $(ls "$SAMPLES" | wc -l) files, screenshots: $(ls "$SHOTS" | wc -l)"
