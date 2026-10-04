---
control: A.5.17
applicability: applicable
justification: 'Treats R-004: weak, reused or shared credentials are the cheapest attack; the standard
  fixes lengths, screening, issuance and reset rules (NIS2 Art. 21(2)(j); insurer condition LEG-08).'
implementation_status: implemented
implemented_by:
- POL-ACC
- STD-AUTH
owner: security-engineer
risks:
- R-004
evidence:
- description: Identity provider password-policy configuration and weak-password rejections
  location: Identity provider
  frequency: continuous
- description: Secrets vault rotation report
  location: Secrets vault
  frequency: quarterly
- description: Reset and initial-credential tickets with identity verification
  location: Ticket system, queue ACCESS
  frequency: on-event
metrics:
- Service secrets older than twelve months (target 0)
- Credential resets without recorded identity verification (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.17 — Authentication information

## Objective

Ensure that passwords, secrets and recovery information are strong, personal, issued and reset safely, stored only where they belong and rotated when they may have been exposed.

## Implementation

- POL-ACC ACC-9 sets the user duties; STD-AUTH AUTH-2 to AUTH-7 set the measurable rules: length, breach screening, no scheduled expiry, password manager, verified resets, throttling.
- Secrets live in the vault (POL-CRYP CRYP-4); authentication events are logged under POL-LOG LOG-1.

## Evidence

- Identity provider password-policy configuration and weak-password rejections — Identity provider.
- Secrets vault rotation report — Secrets vault.
- Reset and initial-credential tickets with identity verification — Ticket system, queue ACCESS.

## Metrics

- Service secrets older than twelve months (target 0)
- Credential resets without recorded identity verification (target 0)

## Common pitfalls

- Forced periodic password changes that drive people to patterns — PaketPort screens against breach lists instead.
- Helpdesk resets by phone without verification — AUTH-6 requires identity verification and one-time credentials.
