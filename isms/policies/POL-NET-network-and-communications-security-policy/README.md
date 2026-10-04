---
id: POL-NET
title: Network and Communications Security Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: head-of-platform
approver: isms-manager
effective_date: &id001 2026-05-18
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-05-18
controls:
- A.8.20
- A.8.21
- A.8.22
- A.8.23
clauses: []
applies_to:
- all
related:
- POL-CRYP
- POL-ACC
- POL-LOG
- POL-SUP
supersedes: []
language: en
tags:
- network
---

# POL-NET — Network and Communications Security Policy

## Purpose

Lockers talk to the backend over networks PaketPort does not own, carriers and customers reach
the platform over the internet, and staff work from offices, homes and vehicles. This policy
defines how networks are segregated, protected and monitored, what PaketPort requires of the
network services it buys, and how web access is filtered. It treats risk R-011 and supports the
treatment of R-001 and R-004.

## Scope

All networks and network services used by the in-scope entities: the cloud networks of the
backend and the management plane, the office networks in Vienna, Munich and Brno, the Brno lab
network, remote access, the locker uplinks, and the connectivity and content-delivery services
bought from providers.

## Policy statements

### Network zones and segregation (A.8.22)

- **NET-1** Networks shall be divided into zones with controlled interfaces:

| Zone | Contents | Trust assumptions |
| --- | --- | --- |
| Production | Backend services, data stores, carrier and app APIs | Reachable only through the API gateway and the bastion; no direct internet egress except through controlled proxies |
| Management plane | Fleet management, OTA signing service, logging, identity | Reachable only from the bastion with privileged access under POL-ACC; the signing service additionally restricted to the release role |
| Corporate | Office networks, endpoints, software-as-a-service access | Separate from production; guest and visitor wireless isolated |
| Locker estate | Every locker uplink | Untrusted: each locker authenticates individually (POL-CRYP CRYP-11) and reaches only the device endpoints of the backend |
| Lab | Brno test lab and pre-production lockers | Isolated from production; test certificates rejected by production |
| Development and test | Non-production environments | Separate credentials and no production data (POL-SDLC SDLC-8) |

- **NET-2** Traffic between zones shall be denied by default and allowed only through documented
  rules with an owner, a purpose and a review date. Rules are reviewed semi-annually and removed
  when no longer needed; lateral movement inside production is limited by network policies
  between services.

### Network security (A.8.20)

- **NET-3** All zone boundaries shall be protected by firewalls or cloud network controls in
  default-deny configuration. The public APIs sit behind a web application firewall and
  distributed-denial-of-service protection with rate limiting, and the backend autoscales within
  the capacity limits of POL-LOG LOG-10.
- **NET-4** Remote access to corporate and production resources shall use the zero-trust gateway
  or the VPN with multi-factor authentication (POL-ACC ACC-8) from managed devices only;
  administrative access additionally passes through the bastion with session recording (ACC-11).
- **NET-5** Locker uplinks — wired or cellular — shall use a private access point name or a VPN
  to the device gateway, and every connection is protected by mutually authenticated TLS under
  POL-CRYP. A locker whose certificate is revoked or expired is refused at the gateway and flagged
  in the fleet-management plane.
- **NET-6** Office wireless shall use enterprise authentication tied to the identity provider;
  guest wireless is isolated from all PaketPort networks. Network equipment is hardened under
  POL-VULN, administered only from the management network with individual accounts, and its
  configuration is backed up under POL-BC.
- **NET-7** Intrusion detection and flow logging shall be active at zone boundaries, the API
  gateway and the device gateway, feeding the central log store and the detection use cases of
  POL-LOG.

### Security of network services (A.8.21)

- **NET-8** Contracts for connectivity, cellular data for lockers, content delivery and cloud
  network services shall specify the security features required (encryption, private access
  point names, denial-of-service protection, logging), service levels and incident notification
  under POL-SUP. The Head of Platform & SRE monitors service performance and security events and
  reviews the providers at the annual supplier review.
- **NET-9** Network documentation — zone diagrams, address plans, firewall rule sets — is
  classified confidential (POL-CLS), kept in the repository and updated through change management
  before a change goes live.

### Web filtering (A.8.23)

- **NET-10** Web access from managed endpoints, including field-service laptops and tablets, shall
  pass through the web filter wherever the device is. The filter blocks malicious and phishing
  sites using threat intelligence under POL-IR and the categories listed in POL-AUP AUP-11,
  inspects downloads for malware and logs blocks to the central log store; category changes and
  work-justified exceptions are requested through the ticket system and approved by the IT
  Operations Lead.
- **NET-11** Egress from production and the management plane shall be restricted to the
  destinations the services need — carrier endpoints, cloud services, update repositories —
  through allow-lists on the egress proxies; lockers reach only the device gateway.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Head of Platform & SRE | Owns this policy, the cloud and device networks, the gateways, the firewall rules and the provider contracts for network services |
| IT Operations Lead | Office networks, wireless, remote access, the web filter and endpoints |
| Security Engineer | Rule reviews, intrusion-detection content, hardening baselines for network equipment |
| Software Engineering Lead | Network policies between services; the locker protocol |
| Site Lead Brno | Isolation of the lab network |
| Information Security Officer / ISMS Manager | Approves exceptions; reviews the rule-review evidence |

## Compliance and exceptions

Compliance is monitored through the semi-annual firewall rule reviews, the share of lockers
connecting through the device gateway with valid certificates (target 100 %), web-filter and
intrusion-detection statistics and the providers' service reports. Exceptions — a temporary
direct connection for a migration, a site host's uplink that cannot carry the VPN — follow the
control exception request, approved by the Head of Platform & SRE and the Information Security
Officer / ISMS Manager, compensated, time-limited to at most twelve months and recorded in the
exception register.

## Related documents

- POL-CRYP — Cryptography Policy
- POL-ACC — Access Control Policy
- POL-LOG — Logging and Monitoring Policy
- POL-SUP — Supplier & Cloud Security Policy
