---
control: A.8.7
applicability: applicable
justification: Endpoints, servers and the mail gateway are exposed to malware daily, and ransomware in
  production would threaten the service; the insurer requires endpoint protection (LEG-08); NIS2 Art.
  21(2)(g).
implementation_status: implemented
implemented_by:
- POL-VULN
owner: security-engineer
risks: []
evidence:
- description: Endpoint detection and response coverage report
  location: Security tooling console
  frequency: monthly
- description: Mail gateway and web filter block statistics
  location: Gateway consoles; central log store
  frequency: monthly
- description: Locker integrity measures (signed images, read-only root, boot integrity)
  location: Firmware build configuration; fleet-management plane
  frequency: continuous
metrics:
- Endpoints and servers with active protection (target 100 %)
- Unexplained boot integrity failures on lockers (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.7 — Protection against malware

## Objective

Prevent, detect and respond to malware on endpoints, servers and the mail and web channels, and make the locker fleet resistant by design.

## Implementation

- POL-VULN VULN-7: endpoint detection and response, mail filtering, web filtering, locker design with signed images, read-only root file systems and boot integrity; POL-AUP AUP-9 and AUP-11 (software catalogue and web filter); POL-NET NET-10.
- Detections are handled under POL-IR; users have no administrator rights to disable protection (POL-AUP AUP-4).

## Evidence

- Endpoint detection and response coverage report — Security tooling console.
- Mail gateway and web filter block statistics — Gateway consoles; central log store.
- Locker integrity measures (signed images, read-only root, boot integrity) — Firmware build configuration; fleet-management plane.

## Metrics

- Endpoints and servers with active protection (target 100 %)
- Unexplained boot integrity failures on lockers (target 0)

## Common pitfalls

- Protection disabled by local administrators — users have no administrator rights.
- Servers excluded from detection tooling for performance — coverage is 100 % with tuned policies.
