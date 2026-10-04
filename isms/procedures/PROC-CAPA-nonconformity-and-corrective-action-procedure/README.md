---
id: PROC-CAPA
title: Nonconformity and Corrective Action Procedure
type: procedure
status: approved
version: 1.0.0
classification: internal
owner: isms-manager
approver: managing-director
effective_date: &id001 2026-03-30
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-03-30
controls:
- A.5.36
clauses:
- '10.1'
- '10.2'
applies_to:
- all
related:
- PROC-AUDIT
- PROC-MR
- PROC-IR
- PROC-DOC
supersedes: []
language: en
tags:
- corrective-action
---

# PROC-CAPA — Nonconformity and Corrective Action Procedure

## Purpose

This procedure defines how PaketPort reacts to nonconformities, removes their causes so that they
do not recur, verifies that the actions worked and turns lessons into continual improvement of
the ISMS (clauses 10.1 and 10.2), including how compliance with the ISMS's own policies, rules
and standards is checked (A.5.36).

## Scope

All nonconformities of the ISMS in any entity: failures to meet a requirement of ISO/IEC
27001:2022, of a PaketPort policy, standard or procedure, or of a legal or contractual
requirement, whatever their source.

## Procedure

### 1. Sources and detection

1. Nonconformities and improvement opportunities come from internal and certification audits
   (PROC-AUDIT), incidents and post-incident reviews (POL-IR), monitoring and metrics (POL-LOG),
   the compliance checks of step 2, exceptions that expire or are breached, complaints from
   customers, carriers or authorities, supplier reviews, the management review (PROC-MR) and
   proposals from staff through the improvement form.
2. Compliance with policies, rules and standards (A.5.36) is checked through automated checks —
   `isms validate`, configuration-drift monitoring under POL-VULN, identity-provider reports under
   STD-AUTH, endpoint compliance under POL-AUP — through quarterly spot checks by the Information
   Security Officer / ISMS Manager of two controls per theme across the entities, and through the
   owners' periodic reviews of their documents and controls. Every failed check is recorded as a
   nonconformity or an observation.

### 2. Recording

1. Every nonconformity is recorded within five working days of detection in the ticket system,
   project ISMS-CAPA, with the id `CAPA-nnn`, the source, a description with evidence, the
   requirement breached, the affected entity, the detection date and an owner role.
2. Classification: **major** (a systematic failure, or a breach that endangers the outcomes of
   the ISMS, legal compliance or the certificate), **minor** (an isolated lapse) or
   **observation** (a weakness or improvement opportunity without a breach).

### 3. Immediate correction

1. The owner contains and corrects the immediate effect — restores the control, closes the gap,
   informs affected parties — within two working days for majors and ten for minors, and records
   the correction. Incidents follow POL-IR and PROC-IR for containment; the CAPA addresses the
   cause.

### 4. Root-cause analysis

1. For every major, and for minors that recur within twelve months, the owner performs a
   root-cause analysis with the Information Security Officer / ISMS Manager using the five-whys
   method or a cause-and-effect diagram, examining process, people, technology and supplier
   causes, and checks whether similar nonconformities exist elsewhere — other entities, other
   systems, other locker generations.

### 5. Corrective action plan

1. The owner proposes actions that remove the cause, with deadlines and resources: for majors a
   plan within ten working days and closure within 90 days; for minors closure within 180 days;
   observations are decided within 30 days (act, or accept with reasons).
2. Actions that change documents go through PROC-DOC; actions that change the risk picture
   update the register under PROC-RISK; actions needing budget beyond the owner's authority go to
   the Security Steering Committee.

### 6. Effectiveness check

1. After implementation the Information Security Officer / ISMS Manager — or the Internal Audit
   Lead for audit findings — verifies effectiveness with evidence: the control operates, the
   metric has moved, no recurrence over an agreed observation period, typically one quarter. The
   result is recorded; an ineffective action reopens the CAPA with a revised analysis.

### 7. Closure and reporting

1. Closure is approved by the Information Security Officer / ISMS Manager for minors and
   observations and by the Managing Director for majors. Open majors and overdue actions are
   reported at every Security Steering Committee, and the CAPA statistics at the management review.
2. Twice a year the Information Security Officer / ISMS Manager analyses trends — recurring
   causes, entities, control themes — and proposes systemic improvements.

### 8. Continual improvement (clause 10.1)

1. Improvement opportunities that are not nonconformities — staff proposals, audit and review
   suggestions, new technology, the opportunities recorded under PROC-RISK — are entered in the
   continual improvement register (project ISMS-CAPA, type "improvement"), evaluated quarterly
   by the steering committee for benefit and effort, and either scheduled with an owner or closed
   with reasons. Implemented improvements are reported at the management review.

## Records

| Record | Where it is kept | Retention | Owner |
| --- | --- | --- | --- |
| Nonconformity records (CAPA-nnn) with analysis, actions and evidence | Ticket system, project ISMS-CAPA | Life of the ISMS plus 3 years | Information Security Officer / ISMS Manager |
| Compliance check results and spot checks | Ticket system, project ISMS-CAPA; automated check reports in the pipeline | 3 years | Information Security Officer / ISMS Manager |
| Effectiveness verifications | Ticket system, attached to the CAPA | Life of the ISMS plus 3 years | Verifier |
| Trend analyses | Steering committee pack | 3 years | Information Security Officer / ISMS Manager |
| Continual improvement register | Ticket system, project ISMS-CAPA | 3 years after closure | Information Security Officer / ISMS Manager |

## Related documents

- PROC-AUDIT — Internal Audit Procedure
- PROC-MR — Management Review Procedure
- PROC-IR — Incident Response and NIS2 Reporting Procedure
- PROC-DOC — Document Control Procedure
