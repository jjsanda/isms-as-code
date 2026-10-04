---
id: PROC-MR
title: Management Review Procedure
type: procedure
status: approved
version: 1.0.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: &id001 2026-03-16
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-03-16
controls: []
clauses:
- '6.2'
- '7.1'
- '9.1'
- '9.3'
applies_to:
- all
related:
- POL-ISMS
- PROC-RISK
- PROC-AUDIT
- PROC-CAPA
- POL-LEG
supersedes: []
language: en
tags:
- management-review
---

# PROC-MR — Management Review Procedure

## Purpose

This procedure defines how top management reviews the ISMS so that it remains suitable, adequate
and effective (clause 9.3), how the security objectives are set and tracked (clause 6.2), how
resources are decided (clause 7.1) and which measurements feed the review (clause 9.1).

## Scope

The ISMS of all in-scope entities: the annual management review and the quarterly Security
Steering Committee (POL-ORG ORG-3), which prepares the review and tracks its decisions.

## Procedure

### 1. Schedule and participants

1. The management review takes place once a year in the last quarter, after the annual risk
   assessment (PROC-RISK) and the internal audit cycle (PROC-AUDIT), and additionally after a
   major incident, a significant change of scope or a failed certification audit.
2. The Managing Director chairs; the Information Security Officer / ISMS Manager prepares and
   records. Participants: Head of Platform & SRE, IT Operations Lead, Software Engineering Lead,
   Head of Procurement, HR Manager, Facilities & Physical Security Lead, Data Protection Officer,
   Internal Audit Lead, Country Manager Germany and Site Lead Brno. Absent participants provide
   written input.

### 2. Measurement inputs (clause 9.1)

1. The Information Security Officer / ISMS Manager collects the measurements through the year
   from their sources:

| Measurement | Source | Frequency |
| --- | --- | --- |
| Security objectives of POL-ISMS ISMS-2 (late reports, training, remediation, restore tests, MFA coverage, reviews on time) | Reporting under POL-HR, POL-VULN, POL-BC, POL-ACC and POL-LOG; `isms review-due` | Quarterly |
| Control implementation status and SoA changes | Generated Statement of Applicability | Quarterly |
| Incident statistics and reporting-deadline compliance | POL-IR IR-14 | Quarterly |
| Risk posture: open treatments, residual risk by band, accepted risks due for re-confirmation | Risk register and treatment plan | Quarterly |
| Audit findings and corrective-action status | PROC-AUDIT, PROC-CAPA | Quarterly |
| Monitoring and capacity measurements | POL-LOG LOG-11 | Monthly |
| Supplier review status | POL-SUP SUP-8 | Annually |
| Document and control review status | Generated document register | Quarterly |

### 3. Preparation

1. Ten working days before the review the Information Security Officer / ISMS Manager circulates
   the review pack covering every required input: the status of actions from previous reviews;
   changes in external and internal issues, in interested-party needs and in the legal register
   (confirmed with the Data Protection Officer under POL-LEG LEG-2); feedback on performance —
   nonconformities and corrective actions, the measurements above, audit results and the
   fulfilment of objectives; feedback from interested parties (carriers, customers, authorities,
   staff); the results of the risk assessment and the status of the treatment plan; opportunities
   for continual improvement; resource needs; and the NIS2 governance items (registration status,
   management-body training, reporting duties, incidents reported).
2. The Country Manager Germany and the Site Lead Brno contribute an entity section: local
   incidents, exceptions, audits, authority contacts and resource needs.

### 4. The review meeting

1. Agenda: (1) actions from the last review; (2) context and legal changes; (3) performance and
   objectives; (4) incidents and reporting; (5) risks and treatment; (6) audits and corrective
   actions; (7) suppliers; (8) entity reports; (9) improvement opportunities; (10) decisions.
2. Decisions and outputs are recorded for each item: decisions on continual improvement; changes
   needed to the ISMS (scope, policies, controls, risk criteria); resource decisions (budget,
   staff, tools); the security objectives for the next cycle with measures, targets and owners,
   updated in POL-ISMS ISMS-2 through PROC-DOC; acceptance or rejection of residual risks put
   forward under PROC-RISK; and any escalation to the shareholders.

### 5. Minutes and follow-up

1. Minutes are issued within five working days, approved by the Managing Director and classified
   internal. Decisions become tickets in the ticket system (project ISMS-MR) with owner and
   deadline and are tracked at every Security Steering Committee until closed.
2. Document changes resulting from the review are made through pull requests under PROC-DOC
   within the decided deadlines.

### 6. Resources (clause 7.1)

1. The review confirms the resources for the ISMS for the coming year — the ISMS budget line of
   POL-ORG ORG-2, the staffing of the security function and the operations centre, the training
   budget, tooling and external support — and records any gap, with its accepted consequence, in
   the risk register.

## Records

| Record | Where it is kept | Retention | Owner |
| --- | --- | --- | --- |
| Review pack | Ticket system, project ISMS-MR | Life of the ISMS plus 3 years | Information Security Officer / ISMS Manager |
| Minutes and decisions | Ticket system, project ISMS-MR; approved copy in the ISMS records area | Life of the ISMS plus 3 years | Managing Director |
| Action tracking | Ticket system, project ISMS-MR | Until closure plus 3 years | Action owners |
| Measurement data | Reporting dashboards; quarterly snapshots attached to the steering committee pack | 3 years | Information Security Officer / ISMS Manager |
| Objectives | POL-ISMS ISMS-2 (version-controlled) | Life of the ISMS | Managing Director |

## Related documents

- POL-ISMS — Information Security Policy
- PROC-RISK — Risk Assessment and Treatment Procedure
- PROC-AUDIT — Internal Audit Procedure
- PROC-CAPA — Nonconformity and Corrective Action Procedure
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
