---
control: A.6.3
applicability: applicable
justification: Treats R-005 (phishing) and meets NIS2 Art. 21(2)(g) and the Art. 20 management training
  duty (LEG-01); staff and technicians (IP-07) need training that fits their role, including locker tampering
  for the field.
implementation_status: implemented
implemented_by:
- POL-HR
owner: hr-manager
risks:
- R-005
evidence:
- description: Training completion and quiz results per person and entity
  location: Training platform
  frequency: monthly
- description: Phishing simulation results
  location: Phishing simulation tool
  frequency: quarterly
- description: Role-based curricula and the management-body training record
  location: Training platform; management review minutes
  frequency: annual
metrics:
- Staff and technicians with current training (target ≥ 98 %)
- Phishing simulation click rate (target ≤ 5 %) and report rate (target ≥ 60 %)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.6.3 — Information security awareness, education and training

## Objective

Give everyone — office staff, developers, platform engineers, field technicians, managers and the management body — the knowledge and habits their role needs, and measure whether it sticks.

## Implementation

- POL-HR HR-5 to HR-9: onboarding gate, annual refresher, the role-based table, the 80 % quiz pass mark, quarterly phishing simulations, tracking with access suspension, monthly awareness.
- POL-ISMS ISMS-2 carries the objective; lessons from incidents feed the content (POL-IR IR-13).

## Evidence

- Training completion and quiz results per person and entity — Training platform.
- Phishing simulation results — Phishing simulation tool.
- Role-based curricula and the management-body training record — Training platform; management review minutes.

## Metrics

- Staff and technicians with current training (target ≥ 98 %)
- Phishing simulation click rate (target ≤ 5 %) and report rate (target ≥ 60 %)

## Common pitfalls

- One generic e-learning for all — role-based modules, with a practical one for technicians.
- Phishing simulations used to shame — targeted training, never public blame.
