---
id: POL-BC
title: Business Continuity & Backup Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: head-of-platform
approver: isms-manager
effective_date: &id001 2026-01-20
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-01-20
controls:
- A.5.29
- A.5.30
- A.8.13
- A.8.14
clauses: []
applies_to:
- all
related:
- POL-IR
- POL-CRYP
- POL-PHY
- PROC-IR
supersedes: []
language: en
tags:
- continuity
- backup
---

# POL-BC — Business Continuity & Backup Policy

## Purpose

People must be able to collect their parcels and carriers must be able to hand them over even
while the backend is disrupted, and PaketPort must be able to restore its data and services within
agreed targets after an outage, an attack or a region failure. This policy sets the continuity
requirements for the locker service and the platform, the backup rules that make recovery
possible, the redundancy required, and the rule that security is not switched off in a crisis.
It treats risks R-003 and R-011.

## Scope

All in-scope entities and the services, systems and sites that deliver the locker service and the
corporate functions behind it — the locker fleet, the cloud backend and data stores, the
fleet-management plane, carrier integrations, corporate identity and IT — and the suppliers they
depend on.

## Policy statements

### Continuity requirements

- **BC-1** The Head of Platform & SRE shall maintain the business impact analysis that sets the
  recovery time objective (RTO) and recovery point objective (RPO) of each service. The current
  targets are:

| Service | Continuity requirement | RTO | RPO |
| --- | --- | --- | --- |
| Parcel deposit and collection at lockers | Lockers keep accepting deposits and handing over parcels offline, buffering transactions locally for at least 72 hours and reconciling on reconnection | offline-capable | 0 (local buffer) |
| Cloud backend (customer app, routing engine) | Fail-over to the secondary region | 4 hours | 1 hour |
| Carrier APIs | Fail over with the backend; carriers informed of degraded modes | 4 hours | 1 hour |
| Fleet-management plane and OTA | Restored after the backend; no updates during an incident | 8 hours | 4 hours |
| Corporate identity and IT | Redundant identity provider; email and collaboration as software-as-a-service | 24 hours | 24 hours |
| Vienna depot provisioning | Provisioning possible from the Munich store with cached images | 5 working days | — |

- **BC-2** Continuity plans shall exist for the loss of the primary cloud region, the loss of the
  fleet-management plane, the loss of connectivity to the locker estate, the loss of the Vienna
  head office or depot, the unavailability of key staff (risk R-013) and a major supplier
  failure. Each plan names the roles, the invocation decision, the steps, the communication and
  the return to normal.

### Information security during disruption (A.5.29)

- **BC-3** Security controls shall remain in force during disruption and recovery: access control
  and multi-factor authentication (POL-ACC), logging to the central store (POL-LOG), encryption
  (POL-CRYP) and change control. Emergency access uses the break-glass accounts of POL-ACC
  ACC-13, never shared credentials or disabled controls.
- **BC-4** Recovery environments — the secondary region, restored systems, temporary workplaces —
  shall meet the production baselines before they carry live data. Deviations accepted under time
  pressure are recorded in the incident ticket and closed within ten working days after the
  return to normal.
- **BC-5** Lockers operating offline shall keep enforcing their local security functions: signed
  firmware only, encrypted local storage, tamper detection, and no administrative access without
  the device certificate chain.

### ICT readiness for business continuity (A.5.30)

- **BC-6** The backend shall run across at least two availability zones in the primary region with
  continuous replication to a secondary EU region. Fail-over shall be automated where possible and
  rehearsed at least twice a year, once unannounced; results, gaps and actions are recorded and
  reported to the Security Steering Committee.
- **BC-7** Runbooks for fail-over, restore and the return to the primary region shall be kept in
  the repository, versioned and tested together with the exercises; capacity reserves in the
  secondary region shall cover peak parcel volume.
- **BC-8** Continuity plans and runbooks shall be reviewed annually, after every exercise, after
  every S1 or S2 incident and after significant changes to the platform or the estate.

### Backup (A.8.13)

- **BC-9** The following shall be backed up: production databases and object storage
  (continuously, point-in-time), fleet-management data including locker configurations and
  certificate records (hourly), source repositories and build configurations (daily), the central
  log store (daily, to the archive tier), corporate software-as-a-service data (daily through the
  providers' export functions) and the infrastructure-as-code configuration (on every change).
- **BC-10** Backups shall be encrypted (POL-CRYP) and stored in the secondary region, and at
  least one copy shall be immutable or logically isolated with separate credentials so that
  production administrators and ransomware cannot delete or alter it. Retention: 35 days of daily
  backups, twelve months of monthly backups, longer where the records schedule in POL-LEG requires.
- **BC-11** Restores shall be tested at least quarterly for the production databases and the
  fleet-management data against the RTO and RPO in BC-1, and at least annually for every other
  backup set, by restoring into an isolated environment. Results are recorded; failures are
  treated under PROC-CAPA.
- **BC-12** Lockers never hold the only copy of data for longer than their local buffer:
  transactions are reconciled to the backend on reconnection, and locker configurations are
  recoverable from the fleet-management plane so that a replaced controller can be provisioned
  without data loss.

### Redundancy (A.8.14)

- **BC-13** Production services shall have no single point of failure within a region (redundant
  instances, load balancing, multi-zone data stores). Lockers shall have redundant connectivity —
  a wired uplink with cellular fall-back, or dual cellular — and enough local power protection to
  complete the current transaction and shut down safely. Critical spare parts are stocked at the
  Vienna depot and the Munich store.

### Crisis management and communication

- **BC-14** The decision to invoke a continuity plan is taken by the Head of Platform & SRE for a
  technical fail-over and by the Managing Director for a crisis affecting the group.
  Communication with customers, carriers, site hosts, authorities and the insurer follows POL-IR
  and PROC-IR, including the degraded-mode notices agreed with carriers.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Head of Platform & SRE | Owns this policy, the impact analysis, the continuity plans, backups, fail-over and restore tests |
| Managing Director | Invokes crisis management; approves external communication |
| Information Security Officer / ISMS Manager | Confirms that security is maintained during disruption; reviews exercise results; incident coordination |
| IT Operations Lead | Corporate IT continuity and software-as-a-service backups |
| Software Engineering Lead | Offline behaviour of the locker firmware; repository backups |
| Facilities & Physical Security Lead | Site-level plans for the head office, the depot and the Brno lab under POL-PHY |
| Country Manager Germany | Field-service continuity and the Munich spare-parts store |

## Compliance and exceptions

Compliance is monitored through the exercise and restore-test records against the RTO and RPO
(objective in POL-ISMS ISMS-2: four successful quarterly restore tests per year), backup
monitoring, and the immutability and isolation checks in the configuration-drift monitoring.
Exceptions — for example a backup set that cannot yet be isolated — follow the control exception
request, approved by the Head of Platform & SRE and the Information Security Officer / ISMS
Manager, time-limited to at most twelve months and recorded in the exception register.

## Related documents

- POL-IR — Information Security Incident Response Policy
- POL-CRYP — Cryptography Policy
- POL-PHY — Physical and Environmental Security Policy
- PROC-IR — Incident Response and NIS2 Reporting Procedure
