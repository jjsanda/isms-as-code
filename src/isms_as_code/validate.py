"""Cross-reference, structure and lifecycle rules over a loaded :class:`Repository`.

The schema (Pydantic) guarantees each file is well-formed on its own; these rules guarantee the
*set* is consistent: every reference resolves, every control has exactly one guide, CHANGELOG and
front matter agree, retired/superseding documents point at each other, risks are treated by
applicable controls, and ownership maps to known roles. Errors block CI; warnings inform.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from isms_as_code import layout
from isms_as_code.clock import Clock
from isms_as_code.durations import Duration
from isms_as_code.ids import control_sort_key, slugify
from isms_as_code.loader import Repository
from isms_as_code.models import DocumentStatus, RiskTreatment
from isms_as_code.sections import REQUIRED_SECTIONS, outline

__all__ = ["Finding", "validate_repository", "has_errors", "count"]

Level = Literal["error", "warning"]


@dataclass(frozen=True)
class Finding:
    level: Level
    where: str
    message: str

    @property
    def is_error(self) -> bool:
        return self.level == "error"


def has_errors(findings: list[Finding]) -> bool:
    return any(finding.is_error for finding in findings)


def count(findings: list[Finding]) -> tuple[int, int]:
    """Return ``(errors, warnings)``."""
    errors = sum(1 for finding in findings if finding.is_error)
    return errors, len(findings) - errors


def validate_repository(repo: Repository, clock: Clock | None = None) -> list[Finding]:
    findings: list[Finding] = []
    _check_documents(repo, findings)
    _check_controls(repo, findings)
    _check_risks(repo, findings)
    _check_mappings(repo, findings)
    _check_context(repo, findings)
    if clock is not None:
        _check_reviews(repo, clock, findings)
    return findings


def _error(findings: list[Finding], where: str, message: str) -> None:
    findings.append(Finding("error", where, message))


def _warning(findings: list[Finding], where: str, message: str) -> None:
    findings.append(Finding("warning", where, message))


def _check_documents(repo: Repository, findings: list[Finding]) -> None:
    roles = repo.roles.by_key()
    catalogue = repo.catalogue.by_id()
    documents = repo.documents_by_id()
    entities = repo.organisation.entities_by_id()
    for document in repo.documents:
        meta = document.meta
        where = repo.relpath(document.path)

        expected_dir = repo.root / layout.DOCUMENT_DIRS[meta.type.value]
        if document.folder.parent != expected_dir:
            _error(
                findings,
                where,
                f"{meta.type.value} documents live under "
                f"{layout.DOCUMENT_DIRS[meta.type.value].as_posix()}/",
            )
        expected_folder = f"{meta.id}-{slugify(meta.title)}"
        if document.folder.name != expected_folder:
            _error(findings, where, f"folder must be named {expected_folder}")

        structure = outline(document.body)
        expected_h1 = f"{meta.id} — {meta.title}"
        if structure.h1 != (expected_h1,):
            _error(findings, where, f"document needs exactly one H1: '# {expected_h1}'")
        missing = structure.missing(REQUIRED_SECTIONS[meta.type.value])
        if missing:
            _error(findings, where, f"missing required sections: {', '.join(missing)}")

        changelog_where = repo.relpath(document.changelog_path)
        for problem in document.changelog.problems:
            _error(findings, changelog_where, problem)
        if document.changelog.entries:
            latest = document.changelog.latest
            if latest.version != meta.version:
                _error(
                    findings,
                    where,
                    f"version {meta.version} does not match the newest CHANGELOG entry "
                    f"{latest.version}",
                )
            if meta.last_reviewed is not None and meta.last_reviewed != latest.date:
                _error(
                    findings,
                    where,
                    f"last_reviewed {meta.last_reviewed} must equal the newest CHANGELOG date "
                    f"{latest.date}",
                )
            if meta.effective_date is not None and meta.effective_date < latest.date:
                _error(
                    findings,
                    where,
                    f"effective_date {meta.effective_date} precedes the approval date "
                    f"{latest.date} recorded in the CHANGELOG",
                )

        if meta.owner not in roles:
            _error(findings, where, f"owner '{meta.owner}' is not a role in roles.yaml")
        if meta.approver is not None and meta.approver not in roles:
            _error(findings, where, f"approver '{meta.approver}' is not a role in roles.yaml")
        for control_id in meta.controls:
            if control_id not in catalogue:
                _error(findings, where, f"unknown Annex A control {control_id}")
        for ref in meta.related:
            if ref not in documents:
                _error(findings, where, f"related document {ref} does not exist")
        for ref in meta.supersedes:
            target = documents.get(ref)
            if target is None:
                _error(findings, where, f"superseded document {ref} does not exist")
            elif target.meta.status is not DocumentStatus.RETIRED:
                _error(findings, where, f"{ref} is listed in supersedes but is not retired")
            elif target.meta.superseded_by != meta.id:
                _error(
                    findings,
                    where,
                    f"{ref} says it is superseded by {target.meta.superseded_by}, not {meta.id}",
                )
        if meta.superseded_by is not None:
            target = documents.get(meta.superseded_by)
            if target is None:
                _error(findings, where, f"superseded_by {meta.superseded_by} does not exist")
            elif target.meta.status is DocumentStatus.RETIRED:
                _error(findings, where, "superseded_by must point to a live document")
            elif meta.id not in target.meta.supersedes:
                _error(
                    findings,
                    where,
                    f"{meta.superseded_by} does not list {meta.id} in its supersedes field",
                )
        if not meta.applies_to_all:
            for entity_id in meta.applies_to:
                entity = entities.get(entity_id)
                if entity is None:
                    _error(findings, where, f"applies_to names unknown entity {entity_id}")
                elif not entity.in_scope:
                    _error(findings, where, f"applies_to names out-of-scope entity {entity_id}")


def _check_controls(repo: Repository, findings: list[Finding]) -> None:
    catalogue = repo.catalogue.by_id()
    guides = repo.controls_by_id()
    documents = repo.documents_by_id()
    roles = repo.roles.by_key()
    risks = repo.risks.by_id()
    entities = repo.organisation.entities_by_id()

    missing = sorted(set(catalogue) - set(guides), key=control_sort_key)
    if missing:
        _error(
            findings,
            layout.CONTROLS_DIR.as_posix(),
            f"{len(missing)} Annex A control(s) have no implementation guide: {', '.join(missing)}",
        )
    for guide in repo.controls:
        meta = guide.meta
        where = repo.relpath(guide.path)
        entry = catalogue.get(meta.control)
        if entry is None:
            _error(findings, where, f"{meta.control} is not an Annex A:2022 control")
            continue
        expected_dir = repo.root / layout.CONTROLS_DIR / layout.THEME_DIRS[entry.theme.value]
        if guide.path.parent != expected_dir:
            _error(
                findings,
                where,
                f"{meta.control} belongs under {layout.THEME_DIRS[entry.theme.value]}/",
            )
        structure = outline(guide.body)
        expected_h1 = f"{meta.control} — {entry.title}"
        if structure.h1 != (expected_h1,):
            _error(findings, where, f"guide needs exactly one H1: '# {expected_h1}'")
        missing_sections = structure.missing(REQUIRED_SECTIONS["control-guide"])
        if missing_sections:
            _error(findings, where, f"missing required sections: {', '.join(missing_sections)}")
        if meta.owner not in roles:
            _error(findings, where, f"owner '{meta.owner}' is not a role in roles.yaml")
        for document_id in meta.implemented_by:
            document = documents.get(document_id)
            if document is None:
                _error(findings, where, f"implemented_by names unknown document {document_id}")
                continue
            if meta.control not in document.meta.controls:
                _error(
                    findings,
                    where,
                    f"{document_id} is credited with {meta.control} but does not list it in "
                    "its own controls",
                )
            if document.meta.status is not DocumentStatus.APPROVED:
                _warning(
                    findings,
                    where,
                    f"{document_id} is {document.meta.status.value}; it does not yet implement "
                    f"{meta.control}",
                )
        for risk_id in meta.risks:
            if risk_id not in risks:
                _error(findings, where, f"unknown risk {risk_id}")
        for entity_id in meta.entity_overrides:
            entity = entities.get(entity_id)
            if entity is None:
                _error(findings, where, f"entity override for unknown entity {entity_id}")
            elif not entity.in_scope:
                _error(findings, where, f"entity override for out-of-scope entity {entity_id}")

    for document in repo.approved_documents():
        for control_id in document.meta.controls:
            credited = guides.get(control_id)
            if credited is not None and document.meta.id not in credited.meta.implemented_by:
                _warning(
                    findings,
                    repo.relpath(document.path),
                    f"lists {control_id} but the control guide does not credit "
                    f"{document.meta.id} in implemented_by",
                )


def _check_risks(repo: Repository, findings: list[Finding]) -> None:
    roles = repo.roles.by_key()
    guides = repo.controls_by_id()
    parties = {party.id for party in repo.parties.parties}
    legal = {item.id for item in repo.legal.requirements}
    where = layout.RISK_REGISTER.as_posix()
    for risk in repo.risks.risks:
        prefix = f"{risk.id}: "
        if risk.owner not in roles:
            _error(findings, where, prefix + f"owner '{risk.owner}' is not a role in roles.yaml")
        for control_id in risk.controls:
            guide = guides.get(control_id)
            if guide is None:
                _error(findings, where, prefix + f"unknown control {control_id}")
            elif not guide.meta.is_applicable:
                _error(
                    findings,
                    where,
                    prefix + f"{control_id} is marked not applicable and cannot treat a risk",
                )
        for party_id in risk.interested_parties:
            if party_id not in parties:
                _error(findings, where, prefix + f"unknown interested party {party_id}")
        for legal_id in risk.legal:
            if legal_id not in legal:
                _error(findings, where, prefix + f"unknown legal requirement {legal_id}")
        band = repo.criteria.band_for(risk.residual_score)
        if risk.treatment is RiskTreatment.RETAIN:
            if band.acceptance is None:
                _error(
                    findings,
                    where,
                    prefix + f"residual score {risk.residual_score} ({band.name}) may not be "
                    "retained under the risk criteria",
                )
            elif risk.accepted_by != band.acceptance:
                _error(
                    findings,
                    where,
                    prefix + f"residual risk in band '{band.name}' must be accepted by "
                    f"'{band.acceptance}', not '{risk.accepted_by}'",
                )
        if risk.accepted_by is not None and risk.accepted_by not in roles:
            _error(findings, where, prefix + f"accepted_by '{risk.accepted_by}' is not a role")


def _check_mappings(repo: Repository, findings: list[Finding]) -> None:
    guides = repo.controls_by_id()
    documents = repo.documents_by_id()
    for mapping in repo.mappings:
        where = (layout.MAPPINGS_DIR / f"{mapping.name}.yaml").as_posix()
        for requirement in mapping.requirements:
            prefix = f"{requirement.id}: "
            for control_id in requirement.controls:
                guide = guides.get(control_id)
                if guide is None:
                    _error(findings, where, prefix + f"unknown control {control_id}")
                elif not guide.meta.is_applicable:
                    _warning(
                        findings,
                        where,
                        prefix + f"{control_id} is not applicable; the requirement is not "
                        "covered by it",
                    )
            for document_id in requirement.documents:
                document = documents.get(document_id)
                if document is None:
                    _error(findings, where, prefix + f"unknown document {document_id}")
                elif document.meta.status is not DocumentStatus.APPROVED:
                    _warning(
                        findings,
                        where,
                        prefix + f"{document_id} is {document.meta.status.value}, not approved",
                    )


def _check_context(repo: Repository, findings: list[Finding]) -> None:
    roles = repo.roles.by_key()
    documents = repo.documents_by_id()
    catalogue = repo.catalogue.by_id()
    entities = repo.organisation.entities_by_id()

    where = layout.ORGANISATION.as_posix()
    for field_name in ("isms_owner", "management_representative"):
        role = getattr(repo.organisation, field_name)
        if role not in roles:
            _error(findings, where, f"{field_name} '{role}' is not a role in roles.yaml")
    for system in repo.organisation.information_systems:
        if system.owner not in roles:
            _error(findings, where, f"system '{system.name}': owner '{system.owner}' is not a role")

    where = layout.INTERESTED_PARTIES.as_posix()
    for party in repo.parties.parties:
        for ref in party.addressed_by:
            if ref not in documents and ref not in catalogue:
                _error(findings, where, f"{party.id}: addressed_by references unknown {ref}")

    where = layout.LEGAL_REGISTER.as_posix()
    for item in repo.legal.requirements:
        prefix = f"{item.id}: "
        if item.owner not in roles:
            _error(findings, where, prefix + f"owner '{item.owner}' is not a role")
        if item.applies_to != ["all"]:
            for entity_id in item.applies_to:
                if entity_id not in entities:
                    _error(findings, where, prefix + f"applies_to names unknown entity {entity_id}")
        for control_id in item.controls:
            if control_id not in catalogue:
                _error(findings, where, prefix + f"unknown control {control_id}")
        for document_id in item.documents:
            if document_id not in documents:
                _error(findings, where, prefix + f"unknown document {document_id}")


def _check_reviews(repo: Repository, clock: Clock, findings: list[Finding]) -> None:
    today = clock.today()
    for document in repo.documents:
        meta = document.meta
        if meta.status is DocumentStatus.APPROVED and meta.next_review and meta.next_review < today:
            _warning(
                findings,
                repo.relpath(document.path),
                f"review overdue: next_review was {meta.next_review}",
            )
    one_year = Duration.parse("P1Y")
    for guide in repo.controls:
        assessed = guide.meta.last_assessed
        if assessed is not None and one_year.add_to(assessed) < today:
            _warning(
                findings,
                repo.relpath(guide.path),
                f"control assessment is older than a year (last_assessed {assessed})",
            )
