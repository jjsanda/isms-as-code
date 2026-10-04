---
control: A.5.28
applicability: applicable
justification: 'Treats R-008: evidence that can stand up before authorities, insurers and courts requires
  disciplined collection with chain of custody; locker controllers are physical evidence that travels.'
implementation_status: implemented
implemented_by:
- POL-IR
- PROC-IR
owner: isms-manager
risks:
- R-008
evidence:
- description: Evidence log with chain-of-custody records
  location: Incident evidence store (restricted)
  frequency: on-event
- description: Forensic toolkit and collection procedure
  location: Incident response runbook repository
  frequency: annual
metrics:
- Evidence items with a complete chain-of-custody record (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.28 — Collection of evidence

## Objective

Collect, preserve and hand over evidence — logs, images, devices — in a way that keeps it complete, unaltered and attributable, so that it can be relied on in regulatory, contractual or criminal proceedings.

## Implementation

- POL-IR IR-12 defines what is collected, how it is classified and how long it is kept; PROC-IR stage 5 has the Security Engineer secure evidence before changes, with hashes, the evidence log, physical custody in the key-handling room and legal hold under POL-LEG.
- The tamper-evident central log store (POL-LOG LOG-4) supports admissibility of exported logs.

## Evidence

- Evidence log with chain-of-custody records — Incident evidence store (restricted).
- Forensic toolkit and collection procedure — Incident response runbook repository.

## Metrics

- Evidence items with a complete chain-of-custody record (target 100 %)

## Common pitfalls

- Evidence collected by whoever is nearest — the Security Engineer owns collection and the log records every handover.
- Logs overwritten before export — LOG-4 retention and the immediate export in stage 5.
