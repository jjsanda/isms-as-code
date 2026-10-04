---
control: A.8.25
applicability: applicable
justification: 'Treats R-009: security built into the requirements, design, coding, testing and release
  of firmware, backend and app; required for the locker product by the Cyber Resilience Act (LEG-03) and
  by NIS2 Art. 21(2)(e).'
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks:
- R-009
evidence:
- description: Life-cycle definition with security gates
  location: Engineering handbook in the repository
  frequency: annual
- description: Gate records per release (requirements, threat model, tests, approvals)
  location: Pipeline and change tickets
  frequency: on-event
metrics:
- Releases with all life-cycle gates recorded (target 100 %)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.25 — Secure development life cycle

## Objective

Make security a built-in property of how PaketPort develops software, from the first requirement to the signed release and the support period in the field.

## Implementation

- POL-SDLC SDLC-1 defines the phases and links to SDLC-2 to SDLC-13; the Security Engineer reviews the life cycle annually; Cyber Resilience Act documentation under SDLC-13.
- Not applicable at PaketPort Deutschland GmbH, which performs no development.

## Evidence

- Life-cycle definition with security gates — Engineering handbook in the repository.
- Gate records per release (requirements, threat model, tests, approvals) — Pipeline and change tickets.

## Metrics

- Releases with all life-cycle gates recorded (target 100 %)

## Common pitfalls

- A life cycle that exists only for the backend — firmware and the app follow the same gates.
- Security activities done by the security team alone — developers own them, with review.
