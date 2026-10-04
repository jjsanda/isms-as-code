---
control: A.8.5
applicability: applicable
justification: 'Treats R-004 and R-005: multi-factor and phishing-resistant authentication is the most
  effective control against credential attacks; required by the insurer (LEG-08, IP-10) and NIS2 Art.
  21(2)(j).'
implementation_status: implemented
implemented_by:
- POL-ACC
- STD-AUTH
owner: security-engineer
risks:
- R-004
- R-005
evidence:
- description: Identity provider multi-factor coverage and factor-type report
  location: Identity provider
  frequency: monthly
- description: Authentication configuration per system checked against STD-AUTH
  location: Configuration-drift monitoring
  frequency: continuous
- description: Authentication event logs
  location: Central log store
  frequency: continuous
metrics:
- Accounts in scope of ACC-8 protected by multi-factor authentication (target 100 %)
- Privileged accounts using phishing-resistant factors (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.5 — Secure authentication

## Objective

Authenticate people, services and devices in a way that resists phishing, replay and brute force — multi-factor for people, tokens or mutual TLS for services, certificates for lockers.

## Implementation

- POL-ACC ACC-8 and ACC-9 set the rules; STD-AUTH AUTH-8 to AUTH-15 make them measurable: where multi-factor authentication is mandatory, permitted and phishing-resistant factors, enrolment, sessions, API and device authentication, break-glass.
- The identity provider enforces the rules for federated systems; legacy systems are registered and compensated under AUTH-17.

## Evidence

- Identity provider multi-factor coverage and factor-type report — Identity provider.
- Authentication configuration per system checked against STD-AUTH — Configuration-drift monitoring.
- Authentication event logs — Central log store.

## Metrics

- Accounts in scope of ACC-8 protected by multi-factor authentication (target 100 %)
- Privileged accounts using phishing-resistant factors (target 100 %)

## Common pitfalls

- Multi-factor authentication everywhere except the one legacy console attackers find — AUTH-17 registers and compensates legacy systems.
- SMS codes counted as a second factor for administrators — AUTH-9 forbids it.
