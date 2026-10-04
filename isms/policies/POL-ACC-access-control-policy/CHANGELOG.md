# Changelog

All notable changes to this document are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the rules in PROC-DOC.
The newest entry is the document's current version and its date is the approval date.

## [2.0.0] - 2026-08-20

### Changed

- ACC-8: the factors used for privileged access and for the fleet-management plane shall be
  phishing-resistant, and SMS and voice codes are withdrawn as a factor for every account. A new
  obligation following the phishing risk R-005 and the insurer's conditions (LEG-08); effective
  2026-09-01 to allow communication and factor enrolment.

## [1.3.0] - 2025-10-15

### Added

- ACC-10: just-in-time elevation for privileged access with session logging to the central log store.
- ACC-13: break-glass accounts — sealed, monitored, alerting on use, reviewed within one working day.

### Changed

- ACC-7: reviews of privileged access moved from every six months to quarterly following the
  internal audit finding on dormant administrator accounts.

## [1.2.0] - 2025-04-07

### Added

- ACC-14: third-party and subcontractor access, covering the field-service subcontractors of
  PaketPort Deutschland GmbH with personal accounts on the maintenance tooling only.

### Changed

- ACC-12: locker edge devices now require per-device identities and mutually authenticated TLS.

## [1.1.0] - 2024-11-18

### Changed

- ACC-6: leaver access is disabled by the end of the last working day instead of within 48 hours.
- ACC-8: multi-factor authentication extended from remote and privileged access to all systems
  holding personal data.

## [1.0.0] - 2024-04-02

### Added

- Initial approved version.
