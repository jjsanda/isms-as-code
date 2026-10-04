---
control: A.8.20
applicability: applicable
justification: 'Treats R-011 and supports R-001 and R-004: the APIs face the internet and the lockers
  connect over untrusted networks; firewalls, denial-of-service protection, authenticated remote access
  and mutual TLS are the backbone (NIS2 Art. 21(2)(j)).'
implementation_status: implemented
implemented_by:
- POL-NET
owner: head-of-platform
risks:
- R-011
evidence:
- description: Firewall and cloud network rule sets with owners and review dates
  location: Network configuration repository
  frequency: semi-annual
- description: Web application firewall and denial-of-service protection configuration and event statistics
  location: Gateway consoles; central log store
  frequency: monthly
- description: Device gateway certificate enforcement logs
  location: Fleet-management plane; central log store
  frequency: continuous
metrics:
- Firewall rules past their review date (target 0)
- Locker connections accepted without a valid certificate (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.20 — Networks security

## Objective

Protect PaketPort's networks and the traffic on them — from the internet to the API, from the street to the backend, from home to the office — against intrusion, interception and denial of service.

## Implementation

- POL-NET NET-3 (default deny, web application firewall, denial-of-service protection), NET-4 (remote access), NET-5 (locker uplinks with mutual TLS), NET-6 (wireless, equipment hardening) and NET-7 (intrusion detection); encryption under POL-CRYP CRYP-1; monitoring under POL-LOG.

## Evidence

- Firewall and cloud network rule sets with owners and review dates — Network configuration repository.
- Web application firewall and denial-of-service protection configuration and event statistics — Gateway consoles; central log store.
- Device gateway certificate enforcement logs — Fleet-management plane; central log store.

## Metrics

- Firewall rules past their review date (target 0)
- Locker connections accepted without a valid certificate (target 0)

## Common pitfalls

- Rules added for a migration and never removed — every rule has an owner and a review date.
- Trusting the cellular provider's private access point name as security — mutual TLS regardless of the carrier network.
