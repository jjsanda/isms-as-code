---
control: A.8.13
applicability: applicable
justification: 'Treats R-003: ransomware or a region failure must not destroy the only copy; the insurer
  (LEG-08, IP-10) and NIS2 Art. 21(2)(c) require tested, isolated backups.'
implementation_status: implemented
implemented_by:
- POL-BC
owner: head-of-platform
risks:
- R-003
evidence:
- description: Backup job monitoring and success reports
  location: Backup console; monitoring platform
  frequency: daily
- description: Quarterly restore test records against RTO and RPO
  location: Ticket system, project ISMS-EXERCISE
  frequency: quarterly
- description: Isolation and immutability configuration
  location: Backup configuration; drift monitoring
  frequency: continuous
metrics:
- Successful quarterly restore tests (target 4 of 4; POL-ISMS ISMS-2)
- Backup sets without an isolated copy (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.13 — Information backup

## Objective

Keep encrypted, isolated, tested copies of everything PaketPort would need to rebuild — databases, fleet data, code, logs, configuration — and prove regularly that they restore within the targets.

## Implementation

- POL-BC BC-9 (scope and frequency), BC-10 (encryption, secondary region, immutable copy, retention), BC-11 (restore tests) and BC-12 (locker data never the only copy); encryption keys under POL-CRYP; failed tests go to PROC-CAPA.

## Evidence

- Backup job monitoring and success reports — Backup console; monitoring platform.
- Quarterly restore test records against RTO and RPO — Ticket system, project ISMS-EXERCISE.
- Isolation and immutability configuration — Backup configuration; drift monitoring.

## Metrics

- Successful quarterly restore tests (target 4 of 4; POL-ISMS ISMS-2)
- Backup sets without an isolated copy (target 0)

## Common pitfalls

- Backups deletable with production credentials — the isolated copy uses separate credentials.
- Restore tests on a toy data set — tests restore production-scale data into isolation.
