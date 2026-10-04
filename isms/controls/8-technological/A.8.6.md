---
control: A.8.6
applicability: applicable
justification: 'Treats R-011: the API must absorb peaks and attacks, and fleet-wide firmware roll-outs
  must not starve the management plane; capacity planning keeps the service available. Partially implemented:
  monitoring and autoscaling exist, quarterly forecasting from parcel volumes is being introduced.'
implementation_status: partially-implemented
implemented_by:
- POL-LOG
owner: head-of-platform
risks:
- R-011
evidence:
- description: Capacity dashboards and threshold alerts
  location: Monitoring platform
  frequency: continuous
- description: Quarterly capacity forecast
  location: Steering committee pack
  frequency: quarterly
metrics:
- Capacity incidents per quarter (target 0)
- Capacity forecasts produced per quarter (target 1)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.6 — Capacity management

## Objective

Make sure compute, storage, network, the log store and the fleet-management plane have the headroom for normal peaks, fail-over and fleet-wide updates — and know before they run out.

## Implementation

- POL-LOG LOG-10: monitoring, thresholds at 70 % and 85 %, autoscaling, quarterly forecasting, roll-out capacity; POL-BC BC-7 (reserves in the secondary region); POL-NET NET-3 (rate limiting).
- Partially implemented: the forecasting step is new and will produce its first full-year view in the next cycle.

## Evidence

- Capacity dashboards and threshold alerts — Monitoring platform.
- Quarterly capacity forecast — Steering committee pack.

## Metrics

- Capacity incidents per quarter (target 0)
- Capacity forecasts produced per quarter (target 1)

## Common pitfalls

- Autoscaling assumed to solve everything — quotas, the log store and the fleet plane need planning.
- Roll-outs scheduled at peak parcel hours — roll-out windows consider capacity.
