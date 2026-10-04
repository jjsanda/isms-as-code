---
control: A.8.26
applicability: applicable
justification: 'Treats R-009: without explicit requirements for authentication, authorisation, input validation,
  cryptography and logging, features ship insecure; the locker product''s essential requirements under
  the Cyber Resilience Act must be documented.'
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks:
- R-009
evidence:
- description: Security requirements per product and feature
  location: Requirements tracker
  frequency: on-event
- description: Threat models for new services and protocol changes
  location: Design repository
  frequency: on-event
metrics:
- Features touching personal data or the locker protocol released without a threat model (target 0)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.26 — Application security requirements

## Objective

State what 'secure' means for each product and feature before building it, derived from data classification, law, contracts, risk and the product's regulatory requirements.

## Implementation

- POL-SDLC SDLC-2 (requirement sources and topics) and SDLC-3 (threat modelling triggers); inputs from POL-CLS, POL-LEG, PROC-RISK and the carrier agreements; privacy by design under POL-LEG LEG-14.

## Evidence

- Security requirements per product and feature — Requirements tracker.
- Threat models for new services and protocol changes — Design repository.

## Metrics

- Features touching personal data or the locker protocol released without a threat model (target 0)

## Common pitfalls

- Requirements copied from a generic checklist — they are derived from PaketPort's data, law and risks.
- Threat models done once and never updated — protocol changes trigger a new one.
