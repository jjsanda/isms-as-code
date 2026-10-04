---
control: A.5.15
applicability: applicable
justification: >-
  Treats R-004 (unauthorised access via weak authentication or stale accounts) and R-010 (insider
  misuse of privileged access). Required by NIS2 Art. 21(2)(i) (LEG-01), by the cyber insurance
  conditions (LEG-08) and by the security annex of the carrier agreements (IP-02).
implementation_status: implemented
implemented_by: [POL-ACC]
owner: isms-manager
risks: [R-004, R-010]
evidence:
  - description: Access control matrices per system (roles to permissions), reviewed semi-annually
    location: Identity provider role catalogue and cloud IAM export, attached to the review ticket
    frequency: semi-annual
  - description: Access requests with line-manager and system-owner approval
    location: Ticket system, queue ACCESS
    frequency: on-event
  - description: Quarterly privileged access review attestations with the list of removed rights
    location: Ticket system, project ISMS-AR
    frequency: quarterly
metrics:
  - Share of in-scope systems with a documented access control matrix (target 100 %)
  - Access rights found in a review without a documented approval (target 0 per quarter)
entity_overrides: {}
last_assessed: 2026-06-15
---

# A.5.15 — Access control

## Objective

Make sure that every person, service and device gets exactly the access its role needs to
PaketPort's information and systems — the cloud backend, the fleet-management plane, corporate IT
and the locker devices — and nothing more, on the basis of rules that are written down, approved by
the system owner and checked at regular intervals.

## Implementation

- POL-ACC ACC-1 to ACC-3 set the rules: unique identities, least privilege and need-to-know,
  role-based assignment and default deny. ACC-15 ties information access to the classification
  scheme of POL-CLS, and ACC-14 confines external parties to the systems their contract requires.
- The rules are enforced as role catalogues in the group identity provider for corporate IT and
  software-as-a-service tools, as IAM policies in the cloud platform for the backend, and as device
  certificates and device groups in the fleet-management plane for the lockers. Production data
  stores are reachable only through application roles and the bastion with session recording.
- Requests, approvals and reviews run through the ticket system (queue ACCESS). The
  joiner-mover-leaver steps are being formalised in PROC-JML, which is in draft; until it is
  approved the IT Operations Lead's checklist applies.
- Entity differences: PaketPort Deutschland GmbH uses the group identity provider without local
  exceptions; its field-service subcontractors reach only the maintenance tooling, each technician
  with a personal account sponsored by the Country Manager Germany. PaketPort Software s.r.o. has no
  standing production access; production debugging is granted just in time under ACC-10.

## Evidence

- Access control matrices: the identity provider role catalogue, the cloud IAM policy export and
  the fleet device groups, attached to the semi-annual review ticket.
- Approved access requests with line-manager and system-owner approval in the ticket system,
  queue ACCESS.
- Quarterly privileged access review attestations and the list of removed rights in the ticket
  system, project ISMS-AR.

## Metrics

- Share of in-scope systems with a documented access control matrix (target 100 %; last
  assessment 100 %).
- Access rights found in a review without a documented approval (target 0 per quarter; last
  quarter 2, both removed within the ten-day deadline of ACC-7).

## Common pitfalls

- Role catalogues that drift from reality because exceptions are granted directly in a system.
  PaketPort routes every grant through the ticket system and reconciles the catalogue against the
  live configuration at each review.
- Subcontractor accounts that outlive the contract. Sponsorship and expiry dates under ACC-14 make
  every external account time-limited, and the Country Manager Germany confirms removal at contract end.
- Treating devices as second-class identities. Locker edge devices carry per-device certificates
  and appear in the same access control matrix as people and services.
