---
control: A.6.1
applicability: applicable
justification: People with privileged access, access to personal data, firmware signing rights or field
  access to lockers need proportionate screening within the limits of local labour law (LEG-06); supports
  R-010.
implementation_status: implemented
implemented_by:
- POL-HR
owner: hr-manager
risks: []
evidence:
- description: Screening records per hire and role
  location: HR system (restricted)
  frequency: on-event
- description: Subcontractor screening confirmations
  location: Supplier register
  frequency: on-event
metrics:
- New hires in sensitive roles with completed screening before access (target 100 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.6.1 — Screening

## Objective

Check, proportionately and lawfully, that the people PaketPort trusts with its systems, data and lockers are who they say they are and have the background the role requires.

## Implementation

- POL-HR HR-1 (proportionate checks, criminal-record certificates where permitted for sensitive roles, national limits per LEG-06) and HR-2 (subcontractors screened by their employer, confirmed under POL-SUP).
- PROC-JML stage 1.1 (in draft) gates account creation on the HR record that carries the screening result.

## Evidence

- Screening records per hire and role — HR system (restricted).
- Subcontractor screening confirmations — Supplier register.

## Metrics

- New hires in sensitive roles with completed screening before access (target 100 %)

## Common pitfalls

- One screening rule for three countries — the Country Manager Germany and the Site Lead Brno apply local law.
- Subcontractor technicians never screened — HR-2 requires written confirmation before access.
