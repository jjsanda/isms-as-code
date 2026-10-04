---
control: A.8.21
applicability: applicable
justification: 'Treats R-011: connectivity, cellular data and content-delivery services are bought in;
  their security features and service levels must be specified and monitored (LEG-05 carrier API commitments,
  IP-02).'
implementation_status: implemented
implemented_by:
- POL-NET
owner: head-of-platform
risks:
- R-011
evidence:
- description: Network service contracts with security requirements and service levels
  location: Supplier register; contract files
  frequency: annual
- description: Service performance and security event reports
  location: Monitoring platform; supplier reviews
  frequency: monthly
metrics:
- Network service providers reviewed in the last twelve months (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.21 — Security of network services

## Objective

Make sure the network services PaketPort relies on — internet uplinks, cellular data for lockers, content delivery, cloud networking — deliver the security features and availability the service needs.

## Implementation

- POL-NET NET-8 (contractual requirements, monitoring, annual review under POL-SUP) and NET-9 (documentation); carrier API availability commitments under POL-SUP SUP-4; redundancy under POL-BC BC-13.

## Evidence

- Network service contracts with security requirements and service levels — Supplier register; contract files.
- Service performance and security event reports — Monitoring platform; supplier reviews.

## Metrics

- Network service providers reviewed in the last twelve months (target 100 %)

## Common pitfalls

- Service levels agreed without security features — NET-8 names encryption, private access point names, denial-of-service protection and logging.
- Provider incidents learned from the news — notification clauses under POL-SUP SUP-3.
