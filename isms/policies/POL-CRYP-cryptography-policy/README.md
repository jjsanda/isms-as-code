---
id: POL-CRYP
title: Cryptography Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: head-of-platform
approver: isms-manager
effective_date: &id001 2026-02-01
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-02-01
controls:
- A.8.24
clauses: []
applies_to:
- all
related:
- STD-CRYPTO
- POL-ACC
- POL-NET
- POL-SDLC
- POL-BC
supersedes: []
language: en
tags:
- cryptography
- keys
---

# POL-CRYP — Cryptography Policy

## Purpose

Cryptography protects PaketPort's data in transit between lockers, backend, apps and carriers,
its data at rest in the cloud and on devices, and the integrity of the firmware that runs on
street-sited hardware. This policy states where cryptography is mandatory and how keys and
certificates are managed through their life; the algorithms, key lengths and lifetimes are
specified in STD-CRYPTO.

## Scope

All systems and entities in scope: the locker fleet and its firmware, the fleet-management and
OTA signing service, the cloud backend and data stores, corporate endpoints and software-as-a-
service tools, backups, and the software development tool chain. It applies to everyone who
designs, operates or uses cryptographic functions, and to suppliers whose contracts reference it.

## Policy statements

### Where cryptography is mandatory

- **CRYP-1** Data in transit shall be encrypted and authenticated: mutually authenticated TLS
  between lockers and the backend, TLS for the customer app and the carrier APIs, an encrypted
  channel for every administrative access, and encrypted connections between backend components
  across network zones (POL-NET).
- **CRYP-2** Data at rest shall be encrypted: databases, object storage and backups in the cloud
  (POL-BC), the storage of lockers and maintenance tablets, and the disks of laptops and phones.
  Confidential and restricted information shall never be stored unencrypted on removable media.
- **CRYP-3** Firmware and software releases shall be digitally signed. Lockers verify the
  signature before installing an image (secure boot and signed OTA), and the build pipeline signs
  container images and release artefacts so that only signed code reaches production (POL-SDLC).
- **CRYP-4** Secrets — API keys, passwords, tokens, private keys — shall be stored in the secrets
  vault or the key management service, never in source code, configuration files, images, tickets
  or chat (POL-ACC ACC-12).

### Key management

- **CRYP-5** Every key and certificate shall have an owner role, a documented purpose, a defined
  lifetime and a rotation plan, recorded in the key inventory maintained by the Head of
  Platform & SRE. Keys are classified restricted under POL-CLS.
- **CRYP-6** Keys shall be generated in the key management service, in a hardware security module
  or in the secure element of the locker controller, using the algorithms and random sources
  approved in STD-CRYPTO. Keys generated on a laptop or copied between systems by hand are
  prohibited.
- **CRYP-7** The firmware signing root key shall be kept offline in a hardware security module
  under dual control: two named custodians — the Head of Platform & SRE and the Software
  Engineering Lead, each with a deputy — are required to sign an intermediate or to recover the
  root. Day-to-day firmware signing uses an intermediate key in the signing service, restricted
  to the release role (POL-ACC ACC-16).
- **CRYP-8** Keys shall be rotated at the lifetimes in STD-CRYPTO, immediately on suspected
  compromise, and when a custodian or a person with knowledge of a secret leaves (PROC-JML).
  Rotation is tested under change management so that lockers in the field are never locked out.
- **CRYP-9** Keys shall be backed up or escrowed only where their loss would make data or devices
  unrecoverable — data-encryption keys and the firmware root — using the controlled backup of the
  key management service or a sealed offline copy under dual control; escrow copies are listed in
  the key inventory.
- **CRYP-10** Revoked, expired or superseded keys shall be destroyed in the key management service
  or the hardware security module and the destruction recorded. Keys that protected archived
  records are kept in escrow for the retention period of those records (POL-LEG).

### Certificates

- **CRYP-11** Every locker shall hold an individual device certificate issued by PaketPort's
  device certificate authority, bound to the controller's secure element where the hardware
  generation supports it. Certificates are issued during provisioning in the Vienna depot, renewed
  automatically through the fleet-management plane before expiry, and revoked on decommissioning,
  theft or compromise (POL-CLS CLS-11).
- **CRYP-12** Public-facing certificates for the customer app and the carrier APIs shall come from
  a publicly trusted certificate authority and renew automatically; internal services use the
  internal certificate authority. Expiry is monitored with alerts 30 and 7 days ahead under POL-LOG.

### Use and design

- **CRYP-13** Only the algorithms, protocols, key lengths and libraries approved in STD-CRYPTO
  shall be used. Designing or implementing cryptographic primitives in-house is prohibited, and
  cryptography in the locker product shall meet the product-security requirements of the Cyber
  Resilience Act tracked in the legal register.
- **CRYP-14** Suspected or confirmed compromise of a key or certificate shall be reported and
  handled as an incident under POL-IR and PROC-IR, including revocation, rotation and an
  assessment of the affected data and devices.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Head of Platform & SRE | Owns this policy, the key inventory, the key management service and the device and internal certificate authorities; first root custodian |
| Software Engineering Lead | Code and firmware signing in the pipeline; second root custodian |
| Security Engineer | Owns STD-CRYPTO; reviews cryptographic design in projects |
| Information Security Officer / ISMS Manager | Approves exceptions; confirms rotation and custody evidence at audits |
| IT Operations Lead | Disk encryption and certificate deployment on corporate devices |
| All staff | Keep secrets in the vault; report suspected compromise |

## Compliance and exceptions

Compliance is monitored through the quarterly key inventory review, certificate expiry monitoring,
the rotation log, the share of lockers holding a valid individual certificate (target 100 %) and
pipeline evidence of signed releases. Exceptions — for example an older locker generation without
a secure element — shall be requested through a control exception request, approved by the Head
of Platform & SRE and the Information Security Officer / ISMS Manager, accompanied by compensating
controls such as shorter certificate lifetimes and additional monitoring, time-limited to at most
twelve months and recorded in the exception register.

## Related documents

- STD-CRYPTO — Cryptographic Algorithms and Key Lengths Standard
- POL-ACC — Access Control Policy
- POL-NET — Network and Communications Security Policy
- POL-SDLC — Secure Development and Change Management Policy
- POL-BC — Business Continuity & Backup Policy
