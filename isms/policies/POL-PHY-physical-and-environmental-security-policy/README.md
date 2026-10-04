---
id: POL-PHY
title: Physical and Environmental Security Policy
type: policy
status: approved
version: 1.0.0
classification: internal
owner: facilities-lead
approver: isms-manager
effective_date: &id001 2026-04-01
last_reviewed: *id001
review_cycle: P1Y
next_review: 2027-04-01
controls:
- A.7.1
- A.7.2
- A.7.3
- A.7.4
- A.7.5
- A.7.6
- A.7.8
- A.7.9
- A.7.11
- A.7.12
- A.7.13
- A.7.14
clauses: []
applies_to:
- all
related:
- POL-CLS
- POL-ACC
- POL-BC
- POL-SUP
supersedes: []
language: en
tags:
- physical
- lockers
- sites
---

# POL-PHY — Physical and Environmental Security Policy

## Purpose

PaketPort's most exposed assets stand on public streets. This policy sets the physical and
environmental security rules for the offices in Vienna, Munich and Brno, the Vienna depot, the
Brno test lab and — as a zone of its own — the locker enclosures in the field, so that people,
equipment and information are protected against unauthorised access, damage and interference.
It treats risk R-001 together with POL-CRYP and POL-VULN.

## Scope

All sites of the in-scope entities, the locker estates in Austria and Germany, equipment in
transit and in vehicles, and everyone who enters PaketPort premises or works on lockers,
including visitors, suppliers, site hosts' staff and subcontractors.

## Policy statements

### Security zones and perimeters (A.7.1)

- **PHY-1** Every site shall be divided into zones with a defined perimeter and entry rule:

| Zone | Where | Entry |
| --- | --- | --- |
| Public | Reception areas, public street around lockers | Open |
| Office | Work areas in Vienna, Munich and Brno | Badge; visitors escorted and logged |
| Restricted | Server and network rooms, the security operations centre, the depot's secure cage, the Brno lab's key-handling room | Badge with named authorisation, two-factor at the server room, access log reviewed monthly |
| Field | The locker enclosure and its controller compartment | Technician badge plus tablet authorisation per visit; door and enclosure sensors |

- **PHY-2** Perimeters of office and restricted zones shall be solid (walls, doors, windows with
  locks or sensors) with no unmonitored openings; restricted zones have no external windows or
  have them alarmed.

### Physical entry (A.7.2)

- **PHY-3** Access to office and restricted zones shall be by personal badge, granted by the
  Facilities & Physical Security Lead on the request of the line manager, reviewed quarterly for
  restricted zones and semi-annually otherwise, and removed through PROC-JML. Badges are never
  lent; tailgating is prohibited and reported.
- **PHY-4** Visitors shall be pre-registered, identified at reception, logged with host, purpose
  and times, issued a visible visitor badge and escorted at all times; visitor logs are retained
  for twelve months. Suppliers' technicians working in restricted zones are escorted or work under
  camera supervision with a named PaketPort contact.
- **PHY-5** Locker enclosures shall open only with the technician's badge in combination with a
  per-visit authorisation issued through the fleet-management plane to the maintenance tablet;
  every opening is logged with the technician identity and reconciled against the work order.

### Securing offices, rooms and facilities (A.7.3)

- **PHY-6** Restricted rooms shall not be signposted as such, shall be locked at all times, and
  shall hold only the equipment and material they exist for; keys and master keys are kept in the
  key safe with a key register maintained by the Facilities & Physical Security Lead.

### Physical security monitoring (A.7.4)

- **PHY-7** The Vienna head office, the depot and the Brno lab shall be protected by intrusion
  detection and cameras covering entrances and restricted zones, monitored by the security
  operations centre and the alarm receiving service outside office hours; recordings are retained
  for 30 days and classified confidential.
- **PHY-8** Lockers shall report door openings, enclosure tamper, tilt and power events to the
  fleet-management plane, which raises an alert to the security operations centre when an event
  has no matching work order. Older locker generations without enclosure sensors are listed in
  the risk register and prioritised for retrofit; until then they receive more frequent site
  inspections.

### Protecting against physical and environmental threats (A.7.5)

- **PHY-9** Server rooms and the depot's secure cage shall have fire detection and suppression,
  water leak detection, temperature and humidity monitoring and be located away from flood-prone
  areas; the Brno lab shall have fire protection suitable for battery-powered test units.
- **PHY-10** Locker sites shall be assessed during the site survey for flooding, vehicle impact,
  vandalism risk and lighting; enclosures shall meet the weather and impact ratings in the
  product specification and shall be anchored according to the installation standard.

### Working in secure areas (A.7.6)

- **PHY-11** Work in restricted zones shall be authorised in advance, performed by at least two
  people for the server room and the key-handling room, and recorded. Photography, personal
  devices and unaccompanied visitors are not permitted there; restricted zones are left locked
  and alarmed when unattended.

### Equipment siting and protection (A.7.8)

- **PHY-12** Servers and network equipment shall be installed in locked racks with cable
  management, environmental monitoring and uninterruptible power; screens and printers handling
  confidential information shall be positioned so that they cannot be viewed from public areas.
- **PHY-13** Lockers shall be installed so that the controller compartment faces away from public
  reach, cables enter through protected conduits, and the enclosure cannot be removed without
  tools and without triggering the tamper sensors.

### Security of assets off-premises (A.7.9)

- **PHY-14** Laptops, tablets, tools, spare parts and locker units outside PaketPort premises
  shall be kept under the personal control of the holder or locked away; they shall not be left
  visible in vehicles or left in vehicles overnight. Devices follow POL-AUP and, when approved,
  POL-REM; locker units in transit travel in tamper-evident packaging with a handover record
  under POL-CLS.

### Supporting utilities (A.7.11)

- **PHY-15** Head office, the security operations centre, the depot and the Brno lab shall have
  uninterruptible power sized for an orderly shutdown and, for the operations centre, for
  continued operation until the generator or the fail-over under POL-BC takes over; redundant
  internet uplinks from different providers serve the head office and the operations centre.
- **PHY-16** Lockers shall protect transactions in progress on power loss and shall report loss
  of power and of connectivity; site hosts are contractually required to keep the agreed power
  supply and to notify planned outages.

### Cabling security (A.7.12)

- **PHY-17** Power and network cabling in PaketPort premises shall run in protected conduits,
  separated from public areas and from each other where interference is possible; patch panels
  and cabinets are locked and documented. Cabling at locker sites is concealed and the uplink is
  treated as untrusted under POL-NET regardless of who provides it.

### Equipment maintenance (A.7.13)

- **PHY-18** Equipment shall be maintained according to the manufacturer's schedule by authorised
  technicians; maintenance of servers and network equipment is recorded in the change log, and
  maintenance of lockers in the fleet-management plane with the work order, the parts replaced and
  the technician. Equipment leaving a site for repair is wiped or its storage removed under POL-CLS.

### Secure disposal and re-use (A.7.14)

- **PHY-19** Before disposal, re-use or return to a supplier, all storage in equipment shall be
  wiped with a verified method or physically destroyed, and a certificate of destruction retained.
  Decommissioned lockers are returned to the Vienna depot or the Munich store, their storage wiped,
  their certificates revoked and their keys removed before the enclosure is scrapped or re-used.

## Roles and responsibilities

| Role | Responsibility |
| --- | --- |
| Facilities & Physical Security Lead | Owns this policy; zones, badges, visitor management, monitoring, utilities, disposal at all sites |
| Head of Platform & SRE | Tamper alerting in the fleet-management plane; locker power and connectivity behaviour |
| Country Manager Germany | Applies the policy at the Munich office, the German estate and with German site hosts |
| Site Lead Brno | Applies the policy at the Brno lab |
| Field technicians | Follow site and enclosure rules, report tamper and damage |
| Information Security Officer / ISMS Manager | Reviews access logs and monitoring results; approves exceptions |

## Compliance and exceptions

Compliance is monitored through badge access reviews, visitor logs, the monthly review of
restricted-zone logs, tamper-alert statistics and their reconciliation, site inspection records
and destruction certificates. Exceptions — for example a temporary site without anchoring or a
locker generation without sensors — shall be requested through a control exception request,
approved by the Facilities & Physical Security Lead and the Information Security Officer / ISMS
Manager, accompanied by compensating controls, time-limited to at most twelve months and
recorded in the exception register.

## Related documents

- POL-CLS — Asset Management and Information Classification Policy
- POL-ACC — Access Control Policy
- POL-BC — Business Continuity & Backup Policy
- POL-SUP — Supplier & Cloud Security Policy
