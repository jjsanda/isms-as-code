---
control: A.8.8
applicability: applicable
justification: 'Treats R-007 and R-009: unpatched lockers, backend services and dependencies are the likeliest
  entry point; the Cyber Resilience Act (LEG-03) and NIS2 Art. 21(2)(e) require vulnerability handling
  with deadlines and disclosure.'
implementation_status: implemented
implemented_by:
- POL-VULN
owner: security-engineer
risks:
- R-007
- R-009
evidence:
- description: Vulnerability scan results and remediation tracking with deadlines
  location: Vulnerability tracker
  frequency: weekly
- description: Coordinated disclosure policy and security.txt
  location: Public website
  frequency: annual
- description: Risk acceptances for missed deadlines
  location: Ticket system, project ISMS-RISK
  frequency: on-event
metrics:
- Critical vulnerabilities on internet-facing systems remediated within 14 days (target 100 %; POL-ISMS
  ISMS-2)
- Scan coverage of the asset inventory (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.8.8 — Management of technical vulnerabilities

## Objective

Find vulnerabilities in the fleet, the platform and the corporate estate before attackers do, fix them within defined deadlines, and handle external reports responsibly.

## Implementation

- POL-VULN VULN-1 (scanning programme), VULN-2 (sources and the disclosure channel), VULN-3 and VULN-4 (deadline table, exceptions), VULN-5 and VULN-6 (fleet patching and support periods).
- POL-SDLC SDLC-6 scans dependencies on every build; emergency patches go through SDLC-9 emergency changes.

## Evidence

- Vulnerability scan results and remediation tracking with deadlines — Vulnerability tracker.
- Coordinated disclosure policy and security.txt — Public website.
- Risk acceptances for missed deadlines — Ticket system, project ISMS-RISK.

## Metrics

- Critical vulnerabilities on internet-facing systems remediated within 14 days (target 100 %; POL-ISMS ISMS-2)
- Scan coverage of the asset inventory (target 100 %)

## Common pitfalls

- Scanning what is easy rather than what is exposed — the inventory drives coverage, including the fleet.
- Deadlines measured from ticket creation instead of fix availability — VULN-3 defines the start.
