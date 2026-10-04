---
control: A.8.28
applicability: applicable
justification: 'Treats R-009: injection, memory errors in firmware and leaked secrets are coding defects;
  a coding standard with automated checks and four-eyes review prevents them (LEG-03; NIS2 Art. 21(2)(e)).'
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks:
- R-009
evidence:
- description: Coding standard per language
  location: Engineering handbook
  frequency: annual
- description: 'Pipeline results: static analysis, dependency and secret scanning, review coverage'
  location: Pipeline
  frequency: continuous
metrics:
- Merges with open critical or high static-analysis findings (target 0)
- Changes merged without a second reviewer (target 0)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.28 — Secure coding

## Objective

Write code that does not introduce the classic vulnerabilities — in firmware, backend and app — and catch the ones that slip through before they reach production.

## Implementation

- POL-SDLC SDLC-5 (standard, linters and static analysis, approved cryptographic libraries, no secrets, four-eyes, merge blocking) and SDLC-6 (components); developer training under POL-HR HR-6; secret scanning under STD-CRYPTO CRYPTO-5.

## Evidence

- Coding standard per language — Engineering handbook.
- Pipeline results: static analysis, dependency and secret scanning, review coverage — Pipeline.

## Metrics

- Merges with open critical or high static-analysis findings (target 0)
- Changes merged without a second reviewer (target 0)

## Common pitfalls

- Tools that can be skipped with a flag — the pipeline blocks merges.
- Firmware written in memory-unsafe languages without safe-handling rules — the standard addresses firmware explicitly.
