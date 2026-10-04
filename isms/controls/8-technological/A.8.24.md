---
control: A.8.24
applicability: applicable
justification: 'Treats R-001 and R-009: mutual TLS and signed firmware protect the lockers, encryption
  at rest and in transit protects consumer data; NIS2 Art. 21(2)(h) and the Cyber Resilience Act require
  managed cryptography.'
implementation_status: implemented
implemented_by:
- POL-CRYP
- STD-CRYPTO
owner: head-of-platform
risks:
- R-001
- R-009
evidence:
- description: Key inventory with owners, lifetimes and rotation records
  location: Key management service; key inventory
  frequency: quarterly
- description: TLS and key-management configuration scans against STD-CRYPTO
  location: Configuration-drift monitoring
  frequency: continuous
- description: Locker certificate status
  location: Fleet-management plane
  frequency: continuous
- description: Dual-control records for the firmware signing root
  location: Key ceremony records (restricted)
  frequency: on-event
metrics:
- Lockers with a valid individual certificate (target 100 %)
- Keys past their maximum lifetime (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.24 — Use of cryptography

## Objective

Use cryptography correctly and consistently — the right algorithms, keys managed through their life, certificates renewed before they expire, signing keys under dual control — across fleet, platform and corporate estate.

## Implementation

- POL-CRYP CRYP-1 to CRYP-14 (where cryptography is mandatory, key life cycle, custodians, certificates, design rules, compromise handling) and STD-CRYPTO CRYPTO-1 to CRYPTO-9 (algorithms, lifetimes, storage, protocol configuration, agility).
- Provisioning issues device certificates (CRYP-11); compromise of a key is an incident (CRYP-14).

## Evidence

- Key inventory with owners, lifetimes and rotation records — Key management service; key inventory.
- TLS and key-management configuration scans against STD-CRYPTO — Configuration-drift monitoring.
- Locker certificate status — Fleet-management plane.
- Dual-control records for the firmware signing root — Key ceremony records (restricted).

## Metrics

- Lockers with a valid individual certificate (target 100 %)
- Keys past their maximum lifetime (target 0)

## Common pitfalls

- Keys in code or images — the secret scanner blocks them (STD-CRYPTO CRYPTO-5).
- Certificates expiring in the field — automated renewal through the fleet plane with 30- and 7-day alerts.
