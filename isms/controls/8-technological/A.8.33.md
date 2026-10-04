---
control: A.8.33
applicability: applicable
justification: Real consumer data in test systems would extend the breach surface to every developer laptop
  and lab unit (supports R-009); masked or synthetic test data removes it.
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks: []
evidence:
- description: Test data generation and masking configuration
  location: Test data repository
  frequency: on-event
- description: Checks for production data in non-production stores
  location: Data-leakage monitoring; spot checks
  frequency: quarterly
metrics:
- Production personal data found in test environments (target 0)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.33 — Test information

## Objective

Ensure that the data used to test firmware, backend and app is realistic enough to be useful and fake or masked enough to be harmless.

## Implementation

- POL-SDLC SDLC-8 (masked or synthetic data only) with POL-CLS CLS-12 (masking) and POL-ACC ACC-15; the Brno lab uses synthetic parcel flows and test certificates; DPO exceptions are time-limited.

## Evidence

- Test data generation and masking configuration — Test data repository.
- Checks for production data in non-production stores — Data-leakage monitoring; spot checks.

## Metrics

- Production personal data found in test environments (target 0)

## Common pitfalls

- A 'one-time' production copy that lives for years — exceptions expire and checks run quarterly.
- Test data that accidentally contains real addresses — synthetic generators, not edited exports.
