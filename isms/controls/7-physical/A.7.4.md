---
control: A.7.4
applicability: applicable
justification: 'Treats R-001: tamper detection on lockers and intrusion detection at the head office and
  the depot turn a physical attack into an alert the security operations centre can act on (IP-03). Partially
  implemented: older locker generations lack enclosure sensors and are scheduled for retrofit.'
implementation_status: partially-implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks:
- R-001
evidence:
- description: Intrusion detection and camera coverage documentation
  location: Facilities documentation
  frequency: annual
- description: Tamper alert statistics and their reconciliation
  location: Fleet-management plane; SOC dashboards
  frequency: monthly
- description: Retrofit plan for sensor-less locker generations
  location: Risk treatment plan, ticket system project ISMS-RTP
  frequency: quarterly
metrics:
- Lockers with enclosure tamper sensors reporting to the SOC (target 100 %, currently below because of
  older generations)
- Tamper alerts triaged within the POL-IR deadlines (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.4 — Physical security monitoring

## Objective

Detect physical intrusion and tampering — at the offices, the depot, the lab and every locker — quickly enough to respond before data or parcels are lost.

## Implementation

- POL-PHY PHY-7 (intrusion detection and cameras, SOC and alarm receiving service, 30-day retention) and PHY-8 (locker sensors alerting when no work order matches, retrofit plan, interim inspections); alerts follow POL-LOG LOG-6 and POL-IR.
- Partially implemented: the retrofit of the oldest generation runs through 2027 under the treatment plan.

## Evidence

- Intrusion detection and camera coverage documentation — Facilities documentation.
- Tamper alert statistics and their reconciliation — Fleet-management plane; SOC dashboards.
- Retrofit plan for sensor-less locker generations — Risk treatment plan, ticket system project ISMS-RTP.

## Metrics

- Lockers with enclosure tamper sensors reporting to the SOC (target 100 %, currently below because of older generations)
- Tamper alerts triaged within the POL-IR deadlines (target 100 %)

## Common pitfalls

- Alerts nobody watches outside office hours — the SOC and the alarm service cover 24/7.
- Sensor gaps unknown — the sensor-less generations are listed in the risk register with interim inspections.
