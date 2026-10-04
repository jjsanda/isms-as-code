---
id: STD-AUTH
title: Authentication and Password Standard
type: standard
status: approved
version: 1.1.0
classification: internal
owner: security-engineer
approver: isms-manager
effective_date: &id001 2026-02-16
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-02-16
controls:
- A.5.17
- A.8.5
clauses: []
applies_to:
- all
related:
- POL-ACC
- POL-CRYP
supersedes: []
language: en
tags:
- authentication
- mfa
- passwords
---

# STD-AUTH — Authentication and Password Standard

## Purpose

This standard turns the authentication statements of POL-ACC (ACC-8, ACC-9, ACC-12 and ACC-13)
into measurable requirements for passwords, multi-factor authentication, sessions, API and
service authentication and device authentication, so that every system in scope is configured
and audited against the same numbers.

## Scope

All systems and identities of the in-scope entities: human accounts in the identity provider and
in systems that cannot federate, service accounts and API clients, break-glass accounts, and the
device identities of lockers and maintenance tablets.

## Requirements

### Account types

- **AUTH-1** Every identity shall be one of: personal account (one person), administrative
  account (a person's separate privileged identity), service account (owned by a role, used by
  software), device identity (a locker or tablet) or break-glass account (POL-ACC ACC-13).
  Identities that fit no type are not created (implements POL-ACC ACC-1).

### Passwords and passphrases (A.5.17)

- **AUTH-2** Personal and administrative accounts: minimum 14 characters, no composition rules,
  no maximum below 64 characters, checked against a breached-password list at creation and
  change, and not containing the user name or the word PaketPort. The identity provider rejects
  weak choices (implements POL-ACC ACC-9).
- **AUTH-3** Service accounts and API clients: secrets of at least 32 random characters generated
  by the secrets vault, rotated at least every twelve months and on personnel change (implements
  POL-ACC ACC-12).
- **AUTH-4** Passwords shall not expire on a schedule. They are changed when compromise is
  suspected, after break-glass use and when an administrator leaves (POL-ACC ACC-6); reuse of the
  last ten passwords is blocked.
- **AUTH-5** The approved password manager shall be used for every credential that cannot be
  federated; secrets of systems live in the secrets vault, never in browser stores, spreadsheets
  or tickets.
- **AUTH-6** Initial credentials and resets: identity shall be verified in person, by video with
  the line manager's confirmation or against the HR record before a credential is issued. Initial
  and reset credentials are one-time, valid for 24 hours and force a change at first use; helpdesk
  staff never see or set a permanent password.
- **AUTH-7** Authentication failures shall be throttled: after ten consecutive failures the
  account is locked for 15 minutes or until an administrator releases it, exponential delays apply
  to API clients, and repeated failures raise an alert under POL-LOG.

### Multi-factor authentication (A.8.5)

- **AUTH-8** Multi-factor authentication is mandatory for all remote access, all administrative
  accounts, all access to systems holding personal data, all cloud console and pipeline access,
  and all software-as-a-service tools integrated with the identity provider (implements POL-ACC
  ACC-8).
- **AUTH-9** Permitted factors: platform authenticators and hardware security keys
  (FIDO2/WebAuthn), authenticator apps with time-based codes or number matching, and smart
  cards. Phishing-resistant factors (FIDO2/WebAuthn or smart card) are mandatory for
  administrative accounts, the fleet-management plane, the signing service and the break-glass
  accounts. SMS and voice codes are not permitted for any account with privileged access and are
  phased out for all other accounts by the date in the risk treatment plan.
- **AUTH-10** Factors are enrolled during onboarding (PROC-JML) with the identity verification of
  AUTH-6; recovery codes are issued once and kept by the user in the password manager, and a lost
  factor is replaced only after re-verification. Trusted-device exemptions are limited to twelve
  hours.

### Sessions

- **AUTH-11** Idle timeouts: 15 minutes for administrative consoles, the bastion and the
  fleet-management plane; eight hours for standard sessions on managed devices; 30 minutes for
  the customer-service tooling. Re-authentication with a second factor is required for sensitive
  actions: changing authentication settings, exporting confidential data, approving a firmware
  release, retrieving a secret from the vault.
- **AUTH-12** Sessions shall be bound to the device where the platform allows, and all active
  sessions of an identity are revoked when the identity is disabled (POL-ACC ACC-6) or a factor
  is reported lost.

### API, service and device authentication

- **AUTH-13** Service-to-service and API authentication shall use OAuth 2.0 with tokens valid for
  at most one hour, or mutually authenticated TLS. Long-lived static API keys are permitted only
  for carrier integrations that cannot yet support tokens, with an expiry of at most twelve months
  and an allow-listed source.
- **AUTH-14** Lockers shall authenticate with their individual X.509 device certificate over
  mutually authenticated TLS (POL-CRYP CRYP-11). The current hardware generation keeps the private
  key in the secure element; older generations keep it in encrypted storage bound to the device,
  receive a certificate lifetime of at most one year and are monitored for cloning indicators.
  Maintenance tablets authenticate with a device certificate plus the technician's personal factors.
- **AUTH-15** Break-glass accounts shall use a random passphrase of at least 24 characters sealed
  in the key safe plus a hardware security key held by the deputy of the Head of Platform & SRE;
  both are required, and use triggers the alert and rotation of POL-ACC ACC-13.

### Logging and legacy systems

- **AUTH-16** All authentication events — successes, failures, factor changes, resets, lockouts,
  token issuance — shall be logged under POL-LOG with identity and source.
- **AUTH-17** Systems that cannot meet a requirement, such as legacy equipment without
  multi-factor support, shall be registered through the exception process of POL-ACC with
  compensating controls: network restriction to the bastion, unique local accounts, rotation of
  their credentials every 90 days and logging of every login.

## Compliance and exceptions

Compliance is measured through identity-provider reports (share of accounts with multi-factor
authentication and with phishing-resistant factors, weak-password rejections, lockouts), the
rotation report of the vault and the certificate inventory of the fleet; the results feed the
monitoring of POL-ACC. Exceptions follow AUTH-17 and the control exception request, approved by
the Security Engineer and the Information Security Officer / ISMS Manager, time-limited to at most
twelve months and recorded in the exception register.

## Related documents

- POL-ACC — Access Control Policy
- POL-CRYP — Cryptography Policy
