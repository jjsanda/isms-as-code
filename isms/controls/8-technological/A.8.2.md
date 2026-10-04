---
control: A.8.2
applicability: applicable
justification: 'Treats R-004 and R-010: privileged access to the backend, the fleet-management plane and
  the identity provider is the most damaging access to lose or misuse; NIS2 Art. 21(2)(i).'
implementation_status: implemented
implemented_by:
- POL-ACC
owner: isms-manager
risks:
- R-004
- R-010
evidence:
- description: Privileged role assignments and quarterly review attestations
  location: Identity provider; ticket system, project ISMS-AR
  frequency: quarterly
- description: Just-in-time elevation records
  location: Privileged access tooling logs in the central log store
  frequency: continuous
- description: Break-glass use alerts and reviews
  location: Ticket system, project INC
  frequency: on-event
metrics:
- Standing (non-just-in-time) privileged assignments outside break-glass (target 0)
- Privileged access reviews completed on time (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.2 — Privileged access rights

## Objective

Keep privileged access rare, separate, temporary, strongly authenticated and watched — and have a controlled way to get it in an emergency.

## Implementation

- POL-ACC ACC-10 (separate administrative identities, just-in-time elevation, multi-factor authentication, session logging), ACC-11 (privileged utilities and production data through the bastion), ACC-13 (break-glass) and ACC-7 (quarterly reviews).
- STD-AUTH AUTH-9 (phishing-resistant factors) and AUTH-15 (break-glass credentials); logging under POL-LOG LOG-1.

## Evidence

- Privileged role assignments and quarterly review attestations — Identity provider; ticket system, project ISMS-AR.
- Just-in-time elevation records — Privileged access tooling logs in the central log store.
- Break-glass use alerts and reviews — Ticket system, project INC.

## Metrics

- Standing (non-just-in-time) privileged assignments outside break-glass (target 0)
- Privileged access reviews completed on time (target 100 %)

## Common pitfalls

- Administrators using their administrative identity for email — separate identities and the bastion.
- Standing privileges for convenience — just-in-time elevation with time limits.
