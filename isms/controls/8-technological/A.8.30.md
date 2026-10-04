---
control: A.8.30
applicability: applicable
justification: 'Treats R-006: code written by an external developer enters PaketPort''s products; contracts,
  access limits, testing before acceptance and no production data keep it to the same standard (LEG-03
  for product components; NIS2 Art. 21(2)(d)).'
implementation_status: implemented
implemented_by:
- POL-SUP
owner: head-of-procurement
risks:
- R-006
evidence:
- description: Contracts with outsourced developers including the security terms
  location: Contract files; supplier register
  frequency: on-event
- description: Acceptance test and code review records for delivered code
  location: Pipeline; change tickets
  frequency: on-event
metrics:
- Outsourced deliveries merged without review and scanning (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.30 — Outsourced development

## Objective

Make sure software developed outside PaketPort — for example parts of the customer app — meets the same security standard as internal code, and that PaketPort owns and controls it.

## Implementation

- POL-SUP SUP-14 (contract requirements: POL-SDLC practices, ownership, testing, no production data, access under POL-ACC ACC-14, review before merge) and POL-SDLC SDLC-13; supplier assessment under SUP-2.

## Evidence

- Contracts with outsourced developers including the security terms — Contract files; supplier register.
- Acceptance test and code review records for delivered code — Pipeline; change tickets.

## Metrics

- Outsourced deliveries merged without review and scanning (target 0)

## Common pitfalls

- External developers with standing repository write access — access sponsored, time-limited and review-gated.
- Accepting deliveries on functionality alone — security tests are acceptance criteria.
