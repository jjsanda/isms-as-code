---
control: A.5.3
applicability: applicable
justification: Treats R-010 (insider misuse of privileged access) by separating development from release
  signing, request from approval, and operation from audit; a small team makes technically enforced and
  compensating controls essential.
implementation_status: implemented
implemented_by:
- POL-ORG
owner: isms-manager
risks:
- R-010
evidence:
- description: Segregation matrix and register of duty conflicts with compensating controls
  location: Ticket system, project ISMS-SOD; quarterly steering committee pack
  frequency: quarterly
- description: Pipeline and repository settings enforcing author ≠ approver and the separate release role
  location: Source control platform; pipeline configuration
  frequency: continuous
- description: Four-eyes records for conflicting duties
  location: Pull requests and change tickets
  frequency: on-event
metrics:
- Recorded duty conflicts without a compensating control (target 0)
- Changes merged or released by their own author (target 0)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.3 — Segregation of duties

## Objective

Prevent one person from being able to introduce, approve and deploy a harmful change, or to grant themselves access unnoticed — across the pipeline, the fleet-management plane and the identity provider.

## Implementation

- POL-ORG ORG-7 lists the duty pairs that must be separated and ORG-8 the compensating controls where the team is too small to separate them.
- Branch protection prevents authors from approving their own pull requests; the signing service is restricted to the release role (POL-ACC ACC-16, POL-CRYP CRYP-7); access approval and administration are separated in the ACCESS queue (POL-ACC ACC-3).
- The Internal Audit Lead is independent of operations (PROC-AUDIT stage 2); conflicts are confirmed quarterly at the steering committee.

## Evidence

- Segregation matrix and register of duty conflicts with compensating controls — Ticket system, project ISMS-SOD; quarterly steering committee pack.
- Pipeline and repository settings enforcing author ≠ approver and the separate release role — Source control platform; pipeline configuration.
- Four-eyes records for conflicting duties — Pull requests and change tickets.

## Metrics

- Recorded duty conflicts without a compensating control (target 0)
- Changes merged or released by their own author (target 0)

## Common pitfalls

- Treating segregation as an organisation-chart exercise while the pipeline still lets one person merge and release — PaketPort enforces it technically.
- Break-glass use that bypasses segregation without review — every use triggers an alert and a review within one working day (POL-ACC ACC-13).
