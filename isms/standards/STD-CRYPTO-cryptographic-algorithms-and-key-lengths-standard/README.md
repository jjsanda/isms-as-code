---
id: STD-CRYPTO
title: Cryptographic Algorithms and Key Lengths Standard
type: standard
status: approved
version: 1.0.0
classification: internal
owner: security-engineer
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
- POL-CRYP
- POL-SDLC
supersedes: []
language: en
tags:
- cryptography
---

# STD-CRYPTO — Cryptographic Algorithms and Key Lengths Standard

## Purpose

This standard specifies the algorithms, protocols, key lengths, lifetimes and storage rules that
implement POL-CRYP across the locker fleet, the backend, the corporate estate and the development
pipeline, so that "approved cryptography" means the same thing everywhere and can be checked by
configuration scanning.

## Scope

All cryptographic functions used by the systems and products of the in-scope entities, including
third-party components and libraries, and the requirements passed to suppliers under POL-SUP.

## Requirements

### Approved algorithms

- **CRYPTO-1** Only the following shall be used in new designs and configurations (implements
  POL-CRYP):

| Purpose | Approved | Notes |
| --- | --- | --- |
| Symmetric encryption | AES-256-GCM; ChaCha20-Poly1305 | Authenticated encryption only; AES-256-CBC permitted inside the TLS 1.2 suites below and for disk encryption with a separate integrity mechanism |
| Hashing | SHA-256, SHA-384, SHA-512, SHA-3 | |
| Message authentication | HMAC-SHA-256 or stronger; AEAD tags | |
| Digital signatures (firmware, code, documents) | Ed25519; ECDSA P-256 or P-384; RSA-PSS with 3072 bits or more for interoperability | Firmware and code signing use Ed25519 or ECDSA P-384 |
| Key agreement | X25519; ECDHE with P-256 or P-384 | Forward secrecy mandatory |
| Password hashing | Argon2id (at least 64 MiB memory, 3 iterations, parallelism 1); bcrypt with cost 12 or higher where Argon2id is unavailable | |
| Key derivation | HKDF-SHA-256 | |
| Random numbers | The platform's cryptographically secure generator; the secure element's generator on lockers | No user-space pseudo-random generators for keys |
| Transport | TLS 1.3 preferred; TLS 1.2 only with ECDHE and AEAD cipher suites | Mutual TLS for lockers and internal services |
| Secure boot | Signature verification of every stage against the firmware signing chain | |

- **CRYPTO-2** The following are forbidden in new use and shall be removed from existing systems
  by the dates in the risk treatment plan: MD5 and SHA-1 for anything security-relevant, RSA below
  2048 bits (below 3072 for new keys), DSA, 3DES, RC4, Blowfish, CBC mode without integrity
  protection, TLS 1.0 and 1.1, SSL, static RSA key exchange, export-grade suites, home-grown or
  modified algorithms, and hard-coded keys or keys derived from constants.

### Key lengths and lifetimes

- **CRYPTO-3** Keys and certificates shall meet these minimum strengths and maximum lifetimes
  (implements POL-CRYP):

| Key or certificate | Minimum strength | Maximum lifetime | Storage |
| --- | --- | --- | --- |
| Firmware signing root | ECDSA P-384 or Ed25519 | 10 years, offline | Hardware security module, dual control |
| Firmware signing intermediate | ECDSA P-384 or Ed25519 | 2 years | Signing service backed by the key management service |
| Code and container signing keys | Ed25519 or ECDSA P-256 | 1 year | Key management integration of the pipeline |
| Device certificate authority | ECDSA P-384 | 10 years | Key management service, hardware-backed |
| Locker device certificates | ECDSA P-256 | 2 years; 1 year for generations without a secure element | Secure element or encrypted device storage |
| Public TLS certificates (app, carrier APIs) | ECDSA P-256 or RSA 3072 | 13 months | Cloud certificate service |
| Internal service certificates | ECDSA P-256 | 90 days, automated renewal | Internal certificate authority |
| Data-encryption keys (databases, storage, backups) | AES-256 | Rotated yearly, old data re-wrapped | Key management service, customer-managed |
| Secrets of service accounts and API clients | 32 random characters | 12 months | Secrets vault |
| VPN and zero-trust gateway keys | ECDSA P-256 | 1 year | Gateway key store |
| Disk-encryption keys on endpoints | AES-256 | Life of the device | Hardware-backed key store, escrow in device management |

- **CRYPTO-4** Keys shall serve one purpose only — signing, encryption or authentication — and
  shall never be shared between environments or entities; test and lab keys are distinct and are
  rejected by production (POL-SDLC SDLC-8).

### Key storage and handling

- **CRYPTO-5** Root and certificate-authority keys shall reside in a hardware security module or
  the hardware-backed tier of the key management service, application secrets in the secrets
  vault and device keys in the locker's secure element. Keys are never stored in source code,
  container images, configuration files, tickets, chat or email, and the pipeline's secret
  scanner blocks commits containing key material.
- **CRYPTO-6** Private keys shall not be exported from their storage except in the escrow cases
  of POL-CRYP CRYP-9, performed under dual control and logged.

### Protocol configuration

- **CRYPTO-7** TLS endpoints shall be configured to the current platform hardening baseline under
  POL-VULN: TLS 1.3 enabled, TLS 1.2 limited to the approved suites, compression disabled, HSTS
  of at least one year on public endpoints, complete certificate chains and OCSP stapling where
  supported. Locker connections require client certificates and reject renegotiation.
- **CRYPTO-8** Cryptographic libraries shall be the platform's maintained implementations or one
  of a short list approved by the Security Engineer, kept current under POL-VULN; applications
  shall not implement primitives themselves (POL-CRYP CRYP-13).

### Agility and review

- **CRYPTO-9** Every system shall be able to change algorithms and rotate keys without redesign:
  configurable cipher suites, versioned key identifiers in protocols and stored data, and firmware
  able to accept a new signing chain through a signed transition update. The Security Engineer
  reviews this standard annually against current guidance from recognised bodies and maintains a
  watch item on post-quantum algorithms, with a plan to introduce hybrid key agreement for
  locker-to-backend TLS and for long-lived signatures once the platform libraries support the
  standardised schemes.

## Compliance and exceptions

Compliance is checked through configuration scanning of TLS endpoints and key management settings
under POL-VULN, the key inventory review under POL-CRYP and the pipeline's secret scanning.
Exceptions — a carrier that supports only an older cipher suite, a locker generation that cannot
run a required algorithm — follow the control exception request, approved by the Security Engineer
and the Information Security Officer / ISMS Manager, accompanied by compensating controls,
time-limited to at most twelve months and recorded in the exception register.

## Related documents

- POL-CRYP — Cryptography Policy
- POL-SDLC — Secure Development and Change Management Policy
