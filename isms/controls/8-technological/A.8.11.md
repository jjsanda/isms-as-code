---
control: A.8.11
applicability: applicable
justification: 'Treats R-009: development, test and analytics should never expose real consumer data;
  masking and synthetic data remove the exposure. Planned: the rule exists in POL-CLS, the masking tooling
  for all data stores is being built under the risk treatment plan.'
implementation_status: planned
implemented_by:
- POL-CLS
owner: software-engineering-lead
risks:
- R-009
evidence:
- description: Masking rules and synthetic data sets per data store
  location: Data platform repository
  frequency: on-event
metrics:
- Non-production environments with verified masked or synthetic data (target 100 % by the treatment plan
  date)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.11 — Data masking

## Objective

Make sure that the people who build and test PaketPort's software and the analysts who study parcel flows work with masked or synthetic data, not with real consumers' details.

## Implementation

- POL-CLS CLS-12 (masking outside production, DPO exceptions) and POL-SDLC SDLC-8 (no production data in test); POL-ACC ACC-15 restricts access meanwhile.
- Planned: automated masking pipelines for the remaining data stores are in the risk treatment plan with a named owner and deadline.

## Evidence

- Masking rules and synthetic data sets per data store — Data platform repository.

## Metrics

- Non-production environments with verified masked or synthetic data (target 100 % by the treatment plan date)

## Common pitfalls

- Masking that preserves enough to re-identify — pseudonymisation reviewed by the DPO.
- Exceptions that become permanent — time-limited under the exception process.
