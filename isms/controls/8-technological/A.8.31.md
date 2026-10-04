---
control: A.8.31
applicability: applicable
justification: Separate development, test, staging and production with separate credentials and no production
  data stop a test mistake or a compromised developer account from reaching the fleet or consumer data
  (supports R-009 and R-004).
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks: []
evidence:
- description: Environment architecture with separate accounts, keys and network zones
  location: Platform documentation
  frequency: annual
- description: Access configuration showing no standing developer access to production
  location: Identity provider; cloud IAM
  frequency: semi-annual
metrics:
- Production credentials or data found in non-production environments (target 0)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.31 — Separation of development, test and production environments

## Objective

Keep the places where software is built and tested apart from the place where it serves customers — technically, not just by convention.

## Implementation

- POL-SDLC SDLC-8 (separate environments, credentials, keys and zones; no standing production access; masked data; lab test certificates rejected); POL-NET NET-1 zones; POL-CLS CLS-12 masking; STD-CRYPTO CRYPTO-4 distinct keys.

## Evidence

- Environment architecture with separate accounts, keys and network zones — Platform documentation.
- Access configuration showing no standing developer access to production — Identity provider; cloud IAM.

## Metrics

- Production credentials or data found in non-production environments (target 0)

## Common pitfalls

- Staging that shares a database with production — separate data stores and credentials.
- Developers debugging in production with standing access — just-in-time access under POL-ACC ACC-10.
