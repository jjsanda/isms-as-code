---
control: A.8.23
applicability: applicable
justification: 'Treats R-005: malicious and phishing sites deliver credential theft and malware; filtering
  on all managed devices, including field laptops, blocks them early (NIS2 Art. 21(2)(g)). Partially implemented:
  office and VPN traffic is filtered, always-on filtering for field-service tablets is being rolled out.'
implementation_status: partially-implemented
implemented_by:
- POL-AUP
- POL-NET
owner: head-of-platform
risks:
- R-005
evidence:
- description: Web filter policy and category configuration
  location: Web filter console
  frequency: semi-annual
- description: Block statistics and exception requests
  location: Web filter console; ticket system
  frequency: monthly
metrics:
- Managed devices with the filter enforced wherever they are (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.23 — Web filtering

## Objective

Stop users — in the office, at home, in the field — from reaching malicious, phishing and unnecessarily risky websites, and log what was blocked.

## Implementation

- POL-NET NET-10 (filter on all managed endpoints, threat-intelligence categories, logging, exception approval) and NET-11 (production egress allow-lists); POL-AUP AUP-11 (user rules, no circumvention); intelligence from POL-IR IR-15.
- Partially implemented: the tablet roll-out is in the risk treatment plan.

## Evidence

- Web filter policy and category configuration — Web filter console.
- Block statistics and exception requests — Web filter console; ticket system.

## Metrics

- Managed devices with the filter enforced wherever they are (target 100 %)

## Common pitfalls

- Filtering only behind the office firewall — the filter travels with the device.
- Overblocking that pushes people to personal devices — quick exception handling through the ticket system.
