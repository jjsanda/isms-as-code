---
control: A.8.29
applicability: applicable
justification: 'Treats R-009: static and dynamic testing, hardware-in-the-loop firmware tests and annual
  penetration tests find what reviews miss before attackers do.'
implementation_status: implemented
implemented_by:
- POL-SDLC
owner: software-engineering-lead
risks:
- R-009
evidence:
- description: Test results per release (static, dynamic, security and hardware-in-the-loop tests)
  location: Pipeline; Brno lab records
  frequency: on-event
- description: Penetration test reports and remediation
  location: Ticket system, project ISMS-PT (restricted)
  frequency: annual
metrics:
- Internet-facing systems and the locker product penetration-tested in the last twelve months (target
  100 %)
- High findings from tests remediated within the POL-VULN deadlines (target 100 %)
entity_overrides:
  ENT-DE:
    applicability: not-applicable
    justification: PaketPort Deutschland GmbH performs no software development; the control is met for
      the group by PaketPort Systems GmbH and PaketPort Software s.r.o.
last_assessed: 2026-06-15
---

# A.8.29 — Security testing in development and acceptance

## Objective

Test the security of firmware, backend and app systematically — in the pipeline, in the Brno lab and by independent testers — and act on what is found.

## Implementation

- POL-SDLC SDLC-7 (tests before release, hardware-in-the-loop in the lab, annual independent penetration tests); findings under POL-VULN VULN-3; test information under SDLC-8; production protections during testing under PROC-AUDIT stage 4.2.

## Evidence

- Test results per release (static, dynamic, security and hardware-in-the-loop tests) — Pipeline; Brno lab records.
- Penetration test reports and remediation — Ticket system, project ISMS-PT (restricted).

## Metrics

- Internet-facing systems and the locker product penetration-tested in the last twelve months (target 100 %)
- High findings from tests remediated within the POL-VULN deadlines (target 100 %)

## Common pitfalls

- Penetration tests scoped to the website only — the locker product and the APIs are in scope.
- Findings fixed without retest — retest is part of closure.
