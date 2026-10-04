---
control: A.8.27
applicability: applicable
justification: Defence in depth, least privilege, fail-secure lockers and no implicit trust between locker,
  backend and app are what keep a single flaw from becoming a fleet-wide compromise (supports R-001 and
  R-009).
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks: []
evidence:
- description: Architecture principles and reference architecture
  location: Engineering handbook; design repository
  frequency: annual
- description: Design review records
  location: Design repository; change tickets
  frequency: on-event
metrics:
- New services released without a design review against the principles (target 0)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.27 — Secure system architecture and engineering principles

## Objective

Design systems that stay safe when something fails — a locker that stops accepting commands rather than parcels, services that assume nothing about each other, updates that can be made for the product's whole life.

## Implementation

- POL-SDLC SDLC-4 lists the principles; the Security Engineer reviews designs under SDLC-3; network zoning under POL-NET NET-1; updateability under POL-VULN VULN-6.

## Evidence

- Architecture principles and reference architecture — Engineering handbook; design repository.
- Design review records — Design repository; change tickets.

## Metrics

- New services released without a design review against the principles (target 0)

## Common pitfalls

- Principles on a slide, not in reviews — design reviews check them.
- Implicit trust in the locker protocol because 'it is our device' — every call authenticated and authorised.
