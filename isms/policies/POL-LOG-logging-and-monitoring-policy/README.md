---
id: POL-LOG
title: Logging and Monitoring Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: head-of-platform
approver: isms-manager
effective_date: &id001 2026-05-04
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-05-04
controls:
- A.8.6
- A.8.15
- A.8.16
- A.8.17
clauses:
- '9.1'
applies_to:
- all
related:
- POL-IR
- POL-ACC
- POL-NET
- POL-LEG
supersedes: []
language: en
tags:
- logging
- monitoring
---

# POL-LOG — Logging and Monitoring Policy

## Purpose

Without logs PaketPort cannot detect an intrusion, reconstruct what happened to a tampered
locker, meet the NIS2 reporting deadlines or prove to an auditor that a control operates. This
policy defines what is logged, how logs are protected and retained, how they are monitored, how
clocks are kept in step so that events can be correlated, and how capacity is managed so that the
platform and the log store keep up. It treats risks R-002 and R-008 and defines the measurements
reported under clause 9.1.

## Scope

All systems of the in-scope entities that produce security-relevant events: lockers and the
fleet-management plane, the cloud backend and APIs, identity and endpoint management, network
equipment, the software pipeline, software-as-a-service tenants with audit logs, and the physical
security systems under POL-PHY.

## Policy statements

### What is logged (A.8.15)

- **LOG-1** The following event categories shall be logged by every system in scope, each event
  with timestamp (UTC), source, identity or device, action, outcome and — where applicable — the
  object affected:

| Category | Examples |
| --- | --- |
| Authentication | Logins, failures, multi-factor events, token issuance, password and key changes |
| Privileged actions | Elevation, administrative commands, break-glass use, changes to logging itself |
| Access to confidential data | Queries and exports from the customer and parcel data stores, access to restricted keys |
| Configuration and change | Infrastructure and application configuration changes, deployments, firmware roll-outs, baseline drift |
| Locker events | Door openings and closings with the authorising identity, tamper and tilt signals, power and connectivity loss, failed signature checks, firmware version changes |
| API and network | Carrier and app API calls with identity and result, firewall denies, web-filter blocks, VPN sessions |
| Security tooling | Endpoint protection detections, scanner results, mail-gateway quarantines |
| Physical | Badge events at restricted zones, alarm events |

- **LOG-2** Logs shall not contain secrets, payment data or more personal data than the event
  requires. Personal data in logs is pseudonymised where the use case allows, and the Data
  Protection Officer is consulted before a new log source is added.
- **LOG-3** All systems shall forward their logs to the central log store within five minutes of
  the event. Lockers buffer events locally and forward them on reconnection, tamper and security
  events first. A system that cannot forward logs is not production-ready, and a locker that has
  not reported for 24 hours raises an alert.
- **LOG-4** The central log store shall be append-only and tamper-evident, accessible only to the
  security operations centre and the team of the Head of Platform & SRE, administered separately
  from the systems it monitors (POL-ORG ORG-7), with its own administrative actions logged to a
  second location. Retention: 90 days searchable, twelve months in the archive tier, and logs
  tied to an incident until closure plus three years.

### Staff privacy and monitoring limits

- **LOG-5** Monitoring of staff activity shall be limited to what security and legal obligations
  require, communicated through POL-AUP AUP-16 and, at PaketPort Deutschland GmbH, governed by the
  agreement with the works council (legal register LEG-06). Logs are not used for performance
  assessment; access to logs about an identified person for a purpose other than security requires
  the approval of the HR Manager and the Data Protection Officer.

### Monitoring activities (A.8.16)

- **LOG-6** The Security Engineer shall maintain detection use cases in the central log store
  covering at least: credential attacks and impossible travel, privileged activity outside change
  windows, break-glass use, bulk exports from confidential data stores, locker tamper without a
  work order, failed firmware signature checks, configuration drift, malware detections, anomalous
  API usage and loss of logging from any source. Use cases are reviewed quarterly and after every
  S1 or S2 incident.
- **LOG-7** Alerts shall be routed to the security operations centre with a severity mapped to
  POL-IR IR-2. S1 and S2 alerts are acknowledged within 15 minutes around the clock by the on-call
  responder, S3 within four working hours and S4 within two working days. False positives are
  tuned within the review cycle, never silenced without a record.
- **LOG-8** Monitoring results — alert volumes, detection coverage, mean time to acknowledge and
  to resolve — shall be reviewed monthly by the Information Security Officer / ISMS Manager and
  reported to the Security Steering Committee.

### Clock synchronisation (A.8.17)

- **LOG-9** All systems shall synchronise their clocks with the group's time sources: the cloud
  provider's time service for the backend, the corporate time servers for the offices and the
  fleet-management plane's time service for lockers, each traced to a recognised reference.
  Permitted drift is one second for servers and five seconds for lockers; larger drift raises an
  alert, and all logs use UTC.

### Capacity management (A.8.6)

- **LOG-10** The Head of Platform & SRE shall monitor the capacity of compute, storage, network,
  the log store and the fleet-management plane against thresholds, forecast demand quarterly from
  parcel volumes and planned locker roll-outs, and plan capacity so that peak volumes, fail-over
  under POL-BC and fleet-wide firmware roll-outs can be served. Autoscaling and alerts at 70 % and
  85 % utilisation are configured; capacity incidents are handled under POL-IR.

### Measurement (clause 9.1)

- **LOG-11** The logging and monitoring platform shall produce the following measurements for the
  Security Steering Committee and the management review: detection coverage of the use cases in
  LOG-6, mean time to acknowledge and to contain, the share of systems and lockers reporting logs,
  clock-drift alerts, capacity headroom, and the security objectives of POL-ISMS ISMS-2 that
  depend on monitoring.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Head of Platform & SRE | Owns this policy, the central log store, forwarding from platform and fleet, the time sources and capacity management |
| Security Engineer | Detection use cases, tuning, severity mapping of alerts |
| Information Security Officer / ISMS Manager | Monthly review of monitoring results; measurements for the management review |
| IT Operations Lead | Log forwarding from endpoints, identity and corporate systems |
| Data Protection Officer; HR Manager | Privacy review of log sources and of access to person-related logs |
| Country Manager Germany | The works-council agreement on monitoring |

## Compliance and exceptions

Compliance is monitored through the share of in-scope systems forwarding logs (target 100 %),
integrity checks of the log store, alert handling times, clock-drift statistics and the quarterly
use-case reviews. Exceptions — a system that cannot forward a category, an older locker
generation without local buffering — follow the control exception request, approved by the Head
of Platform & SRE and the Information Security Officer / ISMS Manager, time-limited to at most
twelve months and recorded in the exception register.

## Related documents

- POL-IR — Information Security Incident Response Policy
- POL-ACC — Access Control Policy
- POL-NET — Network and Communications Security Policy
- POL-LEG — Legal, Regulatory and Privacy Compliance Policy
