---
control: A.7.11
applicability: applicable
justification: Power and connectivity failures at the head office, the SOC or a locker site interrupt
  the service; uninterruptible power and safe locker behaviour on power loss protect availability (supports
  R-003 and R-011).
implementation_status: implemented
implemented_by:
- POL-PHY
owner: facilities-lead
risks: []
evidence:
- description: UPS and generator test records
  location: Facilities records
  frequency: quarterly
- description: Locker power-loss behaviour test results
  location: Brno lab test records
  frequency: on-event
metrics:
- UPS tests passed per year (target 4 of 4)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.7.11 — Supporting utilities

## Objective

Keep the utilities the service depends on — power, cooling, connectivity — reliable, monitored and able to fail safely.

## Implementation

- POL-PHY PHY-15 (UPS for head office, SOC, depot and lab; redundant uplinks) and PHY-16 (locker behaviour on loss, site-host obligations); redundancy under POL-BC BC-13; power events monitored under POL-LOG LOG-1.

## Evidence

- UPS and generator test records — Facilities records.
- Locker power-loss behaviour test results — Brno lab test records.

## Metrics

- UPS tests passed per year (target 4 of 4)

## Common pitfalls

- UPS never tested under load — quarterly tests.
- Site hosts cutting power for renovations without notice — the site agreement requires notification.
