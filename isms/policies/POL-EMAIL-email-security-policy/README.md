---
id: POL-EMAIL
title: Email Security Policy
type: policy
status: retired
version: 1.1.0
classification: internal
owner: it-operations-lead
approver: isms-manager
effective_date: &id001 2024-06-03
last_reviewed: *id001
review_cycle: P1Y
next_review: 2025-06-03
retired_date: 2026-03-10
controls:
- A.5.14
- A.8.7
clauses: []
applies_to:
- all
related:
- POL-AUP
supersedes: []
superseded_by: POL-AUP
language: en
tags:
- email
---

# POL-EMAIL — Email Security Policy

> **Retired on 2026-03-10.** This policy was superseded by POL-AUP — Acceptable Use Policy, which
> now contains the email, messaging and information-transfer rules. It is kept for reference only
> and no longer applies.

## Purpose

This policy defined how email was to be used and protected at PaketPort Systems GmbH so that
messages could not become a channel for data loss, phishing or malware.

## Scope

All mailboxes, mail gateways and users of PaketPort Systems GmbH. The policy predates the German
and Czech entities and was never extended to them; POL-AUP covers the whole group.

## Policy statements

### Use of email (A.5.14)

- **EMAIL-1** Only the corporate mail service shall be used for PaketPort business; private mail
  accounts shall not be used for work, and automatic forwarding to external addresses is prohibited.
- **EMAIL-2** Confidential information shall be sent externally only encrypted, with the password
  communicated through a different channel; restricted information shall not be sent by email.
- **EMAIL-3** Messages from external senders are marked by the gateway. Users shall not open
  unexpected attachments or follow links that ask for credentials, and shall report suspicious
  messages to the security mailbox without forwarding them.

### Protection of the mail service (A.8.7)

- **EMAIL-4** The mail gateway shall scan all inbound and outbound messages and attachments for
  malware, block executable attachments and quarantine suspicious content for review by the IT
  Operations Lead.
- **EMAIL-5** Mailboxes are protected by the authentication rules of the access control policy;
  access to another person's mailbox requires the approval of the line manager and of the
  Information Security Officer / ISMS Manager and is logged.
- **EMAIL-6** Mail retention follows the records schedule; mailboxes of leavers are archived and
  removed under the leaver process.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| IT Operations Lead | Owned the policy; operated the mail gateway and the quarantine |
| Information Security Officer / ISMS Manager | Handled reported phishing and mailbox-access approvals |
| All users | Followed the rules and reported suspicious messages |

## Compliance and exceptions

Compliance was monitored through gateway statistics and phishing reports. No exception remains in
force: the document is retired, and every rule still needed lives in POL-AUP.

## Related documents

- POL-AUP — Acceptable Use Policy
