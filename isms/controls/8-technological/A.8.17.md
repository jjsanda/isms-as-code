---
control: A.8.17
applicability: applicable
justification: 'Treats R-008: correlating events across lockers, backend and identity provider during
  an investigation requires synchronised clocks, and timelines reported to authorities must be accurate.'
implementation_status: implemented
implemented_by:
- POL-LOG
owner: head-of-platform
risks:
- R-008
evidence:
- description: Time source configuration per platform
  location: Platform and fleet configuration
  frequency: annual
- description: Clock drift alerts
  location: Monitoring platform
  frequency: continuous
metrics:
- Systems or lockers with drift beyond tolerance at month end (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.17 — Clock synchronization

## Objective

Keep all clocks — servers, network equipment, endpoints, lockers — synchronised with trusted sources so that logs line up and timelines hold.

## Implementation

- POL-LOG LOG-9: time sources per platform, drift tolerance of one second for servers and five for lockers, alerts, UTC in logs; lockers synchronise through the fleet-management plane; baselines under POL-VULN VULN-8 include the time settings.

## Evidence

- Time source configuration per platform — Platform and fleet configuration.
- Clock drift alerts — Monitoring platform.

## Metrics

- Systems or lockers with drift beyond tolerance at month end (target 0)

## Common pitfalls

- Lockers with drifting real-time clocks after power loss — resynchronisation on reconnection with alerting.
- Mixed time zones in logs — UTC everywhere.
