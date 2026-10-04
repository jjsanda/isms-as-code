---
id: PROC-AUDIT
title: Internal Audit Procedure
type: procedure
status: approved
version: 1.0.0
classification: internal
owner: internal-audit-lead
approver: managing-director
effective_date: &id001 2026-03-16
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-03-16
controls:
- A.5.35
- A.8.34
clauses:
- '9.2'
applies_to:
- all
related:
- PROC-CAPA
- PROC-MR
- PROC-DOC
- POL-ISMS
supersedes: []
language: en
tags:
- audit
---

# PROC-AUDIT — Internal Audit Procedure

## Purpose

This procedure defines how PaketPort plans, performs and follows up internal audits of the ISMS,
so that the Managing Director knows from an independent source whether the ISMS conforms to
ISO/IEC 27001:2022 and to PaketPort's own requirements and whether it is effectively implemented
(clause 9.2; independent review A.5.35), and how audit testing is performed without harming
production (A.8.34).

## Scope

All clauses of ISO/IEC 27001:2022, all applicable Annex A controls, all ISMS documents and all
three in-scope entities and their sites, including the compliance of suppliers and subcontractors
with contractual requirements where PaketPort holds audit rights.

## Procedure

### 1. The audit programme

1. The Internal Audit Lead maintains a three-year audit programme that covers every clause, every
   applicable control and every entity at least once, with higher frequency for higher-risk areas
   — the fleet-management plane, access control, incident response, tier 1 suppliers — and for
   areas with previous findings.
2. The annual audit plan — audits, scope, criteria, dates, auditors — is derived from the
   programme and the risk register, approved by the Managing Director in the first quarter and
   published to the auditees.
3. Certification and surveillance audits by the certification body and customer audits by
   carriers are scheduled in the same calendar; their findings enter PROC-CAPA like internal ones.

### 2. Auditors, independence and competence

1. Auditors are independent of the area they audit: the Internal Audit Lead does not audit the
   work of the ISMS function itself, auditors from one entity audit another where possible, and
   external specialists are engaged for technical depth (cloud configuration, firmware, review of
   penetration tests).
2. Auditors hold a recognised auditing qualification or have completed the internal auditor
   training and shadowed two audits; competence records are kept under POL-HR HR-13.

### 3. Planning an audit

1. At least four weeks before an audit the auditor issues the audit plan: objective, scope
   (entity, sites, processes, controls), criteria (the clauses of the standard, the ISMS
   documents, legal and contractual requirements), method, schedule, participants and evidence
   requests.
2. Evidence is requested through the repository wherever possible: the current Statement of
   Applicability, the control guides with their `evidence` lists, the generated registers and the
   version-control history of the documents. Sampling sizes are defined in the plan.

### 4. Conducting the audit

1. Opening meeting with the auditee's owner roles; interviews; review of documents and records;
   observation of processes (a locker provisioning in the Vienna depot, a firmware release, an
   access review); and technical testing where the plan provides for it.
2. Protection of systems during audit testing (A.8.34): auditors use read-only accounts issued
   for the audit period; any scan, query or test against production or the locker fleet requires
   the written approval of the Head of Platform & SRE and an agreed window; tests that could
   affect availability run against staging or the Brno lab; audit working papers are classified
   confidential and contain no copies of personal data beyond the sample; audit accounts are
   removed at closure.
3. Findings are discussed with the auditee before the closing meeting so that the facts are agreed.

### 5. Findings

1. Each finding is classified as a **major nonconformity** (a requirement is not met in a way
   that endangers the outcomes of the ISMS, or a systematic failure), a **minor nonconformity**
   (an isolated lapse), an **observation** (a weakness that could become a nonconformity) or an
   **opportunity for improvement**.
2. Each finding states the requirement, the evidence, the gap and the affected entity, and names
   the owner role.

### 6. Reporting

1. The audit report is issued within ten working days of the closing meeting to the auditee
   owners, the Information Security Officer / ISMS Manager and the Managing Director and filed in
   the audit record; the summary is presented at the next Security Steering Committee and at the
   management review.

### 7. Follow-up

1. Nonconformities and observations are entered in PROC-CAPA within five working days. The
   auditor verifies the effectiveness of corrective actions for major nonconformities within the
   PROC-CAPA deadline and for minor ones at the next audit of the area.

### 8. Independent review (A.5.35)

1. In addition to the internal audits, the ISMS is reviewed at least every three years by an
   external party — a consultancy or the certification body's pre-assessment — covering
   governance, the suitability of the control set and the effectiveness of the ISMS as a whole.
   The results are handled like audit findings.

## Records

| Record | Where it is kept | Retention | Owner |
| --- | --- | --- | --- |
| Audit programme and annual plans | ISMS records area; approval in the management review minutes | Life of the ISMS plus 3 years | Internal Audit Lead |
| Audit plans, working papers, evidence samples | Ticket system, project ISMS-AUDIT (confidential) | Three audit cycles | Internal Audit Lead |
| Audit reports | Ticket system, project ISMS-AUDIT; summary in the steering committee pack | Life of the ISMS plus 3 years | Internal Audit Lead |
| Auditor competence records | HR system | Duration of the role plus 3 years | HR Manager |
| Approvals for testing against production | Ticket system, project ISMS-AUDIT | 3 years | Head of Platform & SRE |

## Related documents

- PROC-CAPA — Nonconformity and Corrective Action Procedure
- PROC-MR — Management Review Procedure
- PROC-DOC — Document Control Procedure
- POL-ISMS — Information Security Policy
