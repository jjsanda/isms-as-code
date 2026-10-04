"""The ISMS scope statement (clauses 4.1-4.3), generated from the context registers."""

from __future__ import annotations

from isms_as_code.generate.common import md_header, role_title, role_with_holder, table
from isms_as_code.loader import Repository

__all__ = ["render_scope"]


def render_scope(repo: Repository, digest: str) -> str:
    org = repo.organisation
    out = md_header(digest)
    out += f"# ISMS Scope Statement — {org.group_name}\n\n"
    out += table(
        ["Item", "Value"],
        [
            ["Certification target", org.certification_target],
            ["ISMS owner", role_with_holder(repo, org.isms_owner)],
            ["Management representative", role_with_holder(repo, org.management_representative)],
            ["Entities in scope", ", ".join(e.legal_name for e in org.in_scope_entities())],
            ["Sites in scope", str(len(org.in_scope_sites()))],
            [
                "Source",
                "`isms/context/organisation.yaml`, `interested-parties.yaml`, `legal-register.yaml`",
            ],
        ],
    )
    out += "\n## Purpose\n\n"
    out += (
        "This statement defines the boundaries and applicability of the information security "
        "management system (ISMS) of "
        f"{org.group_name} as required by ISO/IEC 27001:2022 clause 4.3. It is generated from the "
        "organisation register so that the scope, the entity ids used in every document's "
        "`applies_to` field and the per-entity Statements of Applicability can never drift apart.\n\n"
    )
    out += "## The organisation\n\n" + org.description.strip() + "\n\n"
    out += f"**Sector.** {org.sector}\n\n"
    out += "## External and internal issues (clause 4.1)\n\n"
    out += "### External issues\n\n" + "".join(f"- {item}\n" for item in org.external_issues)
    out += "\n### Internal issues\n\n" + "".join(f"- {item}\n" for item in org.internal_issues)
    out += "\n## Interested parties and their requirements (clause 4.2)\n\n"
    out += table(
        ["Id", "Interested party", "Kind", "Requirements", "Addressed by"],
        [
            [
                party.id,
                party.name,
                party.kind.value,
                "; ".join(party.requirements),
                ", ".join(party.addressed_by),
            ]
            for party in repo.parties.parties
        ],
    )
    out += "\n## Organisational scope — legal entities\n\n"
    out += table(
        [
            "Id",
            "Legal entity",
            "Country",
            "Role in the group",
            "Headcount",
            "NIS2 status",
            "In scope",
        ],
        [
            [
                e.id,
                e.legal_name,
                e.country,
                e.role,
                e.headcount,
                e.nis2_status.value,
                "Yes" if e.in_scope else "**No**",
            ]
            for e in org.entities
        ],
    )
    out += "\n## Physical scope — sites\n\n"
    out += table(
        ["Id", "Site", "Entity", "Location", "Kind", "Functions", "In scope"],
        [
            [
                s.id,
                s.name,
                s.entity,
                f"{s.city}, {s.country}",
                s.kind.value,
                "; ".join(s.functions),
                "Yes" if s.in_scope else "**No**",
            ]
            for s in org.sites
        ],
    )
    out += "\n## Services in scope\n\n"
    out += table(
        ["Id", "Service", "Description", "Entities", "In scope"],
        [
            [s.id, s.name, s.description, ", ".join(s.entities), "Yes" if s.in_scope else "**No**"]
            for s in org.services
        ],
    )
    out += "\n## Information systems\n\n"
    out += table(
        ["System", "Description", "Owner", "Hosted at", "Classification"],
        [
            [
                system.name,
                system.description,
                role_title(repo, system.owner),
                ", ".join(system.hosted_at),
                system.classification.value,
            ]
            for system in org.information_systems
        ],
    )
    out += "\n## Interfaces and dependencies\n\n"
    out += table(
        ["External party", "Direction", "Description", "Governed by"],
        [
            [i.party, i.direction.value, i.description, ", ".join(i.governed_by)]
            for i in org.interfaces
        ],
    )
    out += "\n## Exclusions and their justification\n\n"
    exclusions: list[list[object]] = []
    exclusions.extend([e.id, e.legal_name, e.justification] for e in org.entities if not e.in_scope)
    exclusions.extend([s.id, s.name, s.justification] for s in org.sites if not s.in_scope)
    exclusions.extend([s.id, s.name, s.justification] for s in org.services if not s.in_scope)
    if exclusions:
        out += table(["Id", "Excluded item", "Justification"], exclusions)
    else:
        out += "No entity, site or service is excluded.\n"
    out += (
        "\nThe physical infrastructure of the public cloud provider and the internal systems of "
        "carriers, suppliers and site hosts are outside the scope; the interfaces to them are "
        "listed above and governed by the documents named there.\n"
    )
    out += "\n## Applicable legal, regulatory and contractual requirements\n\n"
    out += table(
        ["Id", "Requirement", "Kind", "Applies to", "Owner"],
        [
            [
                item.id,
                item.title,
                item.kind.value,
                ", ".join(item.applies_to),
                role_title(repo, item.owner),
            ]
            for item in repo.legal.requirements
        ],
    )
    limited = [d for d in repo.approved_documents() if not d.meta.applies_to_all]
    out += "\n## Documents with limited applicability\n\n"
    if limited:
        out += table(
            ["Document", "Applies to"],
            [[f"{d.meta.id} — {d.meta.title}", ", ".join(d.meta.applies_to)] for d in limited],
        )
    else:
        out += "All approved documents apply to every entity in scope.\n"
    out += "\n## Approval\n\n"
    out += (
        f"This scope statement is approved by the {role_title(repo, org.management_representative)} "
        f"together with POL-ISMS and maintained by the {role_title(repo, org.isms_owner)}. Changes "
        "to the organisation register are reviewed through pull requests; the approval history is "
        "the version-control history of `isms/context/organisation.yaml`.\n"
    )
    return out
