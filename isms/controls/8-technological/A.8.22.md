---
control: A.8.22
applicability: applicable
justification: Production, the management plane, corporate IT, the lab and the untrusted locker estate
  must not share trust; segregation limits the blast radius of a compromised locker, laptop or test unit
  (supports R-001 and R-004; NIS2 Art. 21(2)(j)).
implementation_status: implemented
implemented_by:
- POL-NET
owner: head-of-platform
risks: []
evidence:
- description: Zone model and network diagrams
  location: Network documentation (confidential)
  frequency: annual
- description: Inter-zone rule reviews
  location: Network configuration repository; ticket system, project ISMS-NET
  frequency: semi-annual
- description: Lab isolation tests
  location: Brno lab test records
  frequency: annual
metrics:
- Inter-zone flows without a documented rule (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.22 — Segregation of networks

## Objective

Keep network zones apart so that a compromise in one — a tampered locker, a phished laptop, a pre-production unit in Brno — cannot reach the backend, the management plane or the signing service.

## Implementation

- POL-NET NET-1 (zone table and trust assumptions) and NET-2 (default deny between zones, documented rules, service-level network policies); test certificates are rejected by production (POL-SDLC SDLC-8); egress allow-lists under NET-11.

## Evidence

- Zone model and network diagrams — Network documentation (confidential).
- Inter-zone rule reviews — Network configuration repository; ticket system, project ISMS-NET.
- Lab isolation tests — Brno lab test records.

## Metrics

- Inter-zone flows without a documented rule (target 0)

## Common pitfalls

- Flat networks that grew with the company — zones enforced in the cloud and the offices with documented rules.
- The lab connected to production 'for a quick test' — isolation tests and rejected test certificates.
