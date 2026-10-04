---
control: A.5.16
applicability: applicable
justification: 'Treats R-004: stale and shared identities are the most common path to unauthorised access;
  every person, service and locker needs a unique, traceable identity (NIS2 Art. 21(2)(i)).'
implementation_status: implemented
implemented_by:
- POL-ACC
owner: it-operations-lead
risks:
- R-004
evidence:
- description: Identity life-cycle tickets for joiners, movers and leavers
  location: Ticket system, queue ACCESS
  frequency: on-event
- description: Identity provider report on dormant and shared accounts
  location: Identity provider
  frequency: monthly
metrics:
- Enabled accounts without activity for 90 days (target 0)
- Shared accounts outside the break-glass set (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.16 — Identity management

## Objective

Guarantee that every identity — human, service or device — is unique, belongs to someone or something known, is created only for a valid reason and disappears when the reason ends.

## Implementation

- POL-ACC ACC-1 and ACC-4 to ACC-6 define uniqueness and the joiner, mover and leaver rules; STD-AUTH AUTH-1 defines the account types.
- PROC-JML (in draft) details the steps and the identity rules of its stage 4; device identities follow POL-CRYP CRYP-11; the IT Operations Lead reviews the monthly dormant-account report.

## Evidence

- Identity life-cycle tickets for joiners, movers and leavers — Ticket system, queue ACCESS.
- Identity provider report on dormant and shared accounts — Identity provider.

## Metrics

- Enabled accounts without activity for 90 days (target 0)
- Shared accounts outside the break-glass set (target 0)

## Common pitfalls

- Reactivating an old identity for a returning person — PROC-JML stage 4.3 issues a new one with a fresh review of rights.
- Service accounts without an owner — every one is requested by a role and reviewed with that role's access.
