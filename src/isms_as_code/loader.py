"""Load the whole repository into validated objects, collecting every problem in one pass.

The loader is deliberately greedy about errors: a broken front matter in one policy must not hide
a broken YAML register elsewhere, so every file is parsed and validated and the problems are
reported together as one :class:`LoaderError`. Cross-reference rules (does ``POL-ACC`` exist? is
``A.5.15`` in the catalogue?) live in :mod:`isms_as_code.validate`, which works on the loaded
:class:`Repository`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter
import yaml
from pydantic import BaseModel, ValidationError

from isms_as_code import layout
from isms_as_code.changelog import Changelog, parse_changelog
from isms_as_code.models import (
    Catalogue,
    ControlGuideMeta,
    DocumentMeta,
    DocumentStatus,
    InterestedPartyRegister,
    LegalRegister,
    Mapping,
    Organisation,
    RiskCriteria,
    RiskRegister,
    RoleRegister,
)

__all__ = ["Document", "ControlGuide", "Repository", "LoaderError", "load_repository"]


class LoaderError(Exception):
    """Raised when one or more repository files fail to parse or validate."""

    def __init__(self, errors: list[str]) -> None:
        self.errors = errors
        joined = "\n  - ".join(errors)
        super().__init__(f"{len(errors)} problem(s) loading the repository:\n  - {joined}")


@dataclass(frozen=True)
class Document:
    """A controlled document: front matter, Markdown body, location and its CHANGELOG."""

    meta: DocumentMeta
    body: str
    path: Path
    changelog: Changelog

    @property
    def folder(self) -> Path:
        return self.path.parent

    @property
    def changelog_path(self) -> Path:
        return self.folder / layout.CHANGELOG_FILENAME


@dataclass(frozen=True)
class ControlGuide:
    """An Annex A control implementation guide: front matter plus Markdown body."""

    meta: ControlGuideMeta
    body: str
    path: Path


@dataclass(frozen=True)
class Repository:
    root: Path
    catalogue: Catalogue
    organisation: Organisation
    roles: RoleRegister
    parties: InterestedPartyRegister
    legal: LegalRegister
    criteria: RiskCriteria
    risks: RiskRegister
    mappings: tuple[Mapping, ...]
    documents: tuple[Document, ...]
    controls: tuple[ControlGuide, ...]

    def relpath(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def documents_by_id(self) -> dict[str, Document]:
        return {document.meta.id: document for document in self.documents}

    def controls_by_id(self) -> dict[str, ControlGuide]:
        return {guide.meta.control: guide for guide in self.controls}

    def document(self, document_id: str) -> Document:
        return self.documents_by_id()[document_id]

    def control(self, control_id: str) -> ControlGuide:
        return self.controls_by_id()[control_id]

    def approved_documents(self) -> list[Document]:
        return [d for d in self.documents if d.meta.status is DocumentStatus.APPROVED]

    def source_paths(self) -> list[Path]:
        """Every input file the generators depend on (used for the source digest)."""
        paths = [
            self.root / layout.CATALOGUE,
            self.root / layout.ORGANISATION,
            self.root / layout.ROLES,
            self.root / layout.INTERESTED_PARTIES,
            self.root / layout.LEGAL_REGISTER,
            self.root / layout.RISK_CRITERIA,
            self.root / layout.RISK_REGISTER,
        ]
        paths.extend(sorted((self.root / layout.MAPPINGS_DIR).glob("*.yaml")))
        for document in self.documents:
            paths.append(document.path)
            paths.append(document.changelog_path)
        paths.extend(guide.path for guide in self.controls)
        return paths


def _rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _format_validation_error(exc: ValidationError, where: str) -> list[str]:
    messages: list[str] = []
    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"])
        message = str(error["msg"])
        if message.startswith("Value error, "):
            message = message[len("Value error, ") :]
        messages.append(f"{where}: {location}: {message}" if location else f"{where}: {message}")
    return messages


def _read_yaml(path: Path, root: Path, errors: list[str]) -> Any:
    if not path.is_file():
        errors.append(f"{_rel(path, root)}: file not found")
        return None
    try:
        with path.open(encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        errors.append(f"{_rel(path, root)}: invalid YAML: {exc}")
        return None
    if data is None:
        errors.append(f"{_rel(path, root)}: file is empty")
        return None
    return data


def _load_model[TModel: BaseModel](
    path: Path, model: type[TModel], root: Path, errors: list[str]
) -> TModel | None:
    raw = _read_yaml(path, root, errors)
    if raw is None:
        return None
    try:
        return model.model_validate(raw)
    except ValidationError as exc:
        errors.extend(_format_validation_error(exc, _rel(path, root)))
        return None


def _read_front_matter(path: Path, root: Path, errors: list[str]) -> tuple[Any, str] | None:
    if not path.is_file():
        errors.append(f"{_rel(path, root)}: file not found")
        return None
    try:
        post = frontmatter.load(str(path))
    except yaml.YAMLError as exc:
        errors.append(f"{_rel(path, root)}: invalid YAML front matter: {exc}")
        return None
    if not post.metadata:
        errors.append(f"{_rel(path, root)}: no YAML front matter found")
        return None
    return post.metadata, str(post.content)


def _load_documents(root: Path, errors: list[str]) -> list[Document]:
    documents: list[Document] = []
    seen: dict[str, Path] = {}
    for type_name, relative in layout.DOCUMENT_DIRS.items():
        directory = root / relative
        if not directory.is_dir():
            errors.append(f"{relative.as_posix()}: directory for {type_name} documents not found")
            continue
        for folder in sorted(p for p in directory.iterdir() if p.is_dir()):
            path = folder / layout.DOCUMENT_FILENAME
            parsed = _read_front_matter(path, root, errors)
            if parsed is None:
                continue
            metadata, body = parsed
            try:
                meta = DocumentMeta.model_validate(metadata)
            except ValidationError as exc:
                errors.extend(_format_validation_error(exc, _rel(path, root)))
                continue
            if meta.id in seen:
                errors.append(
                    f"{_rel(path, root)}: duplicate document id {meta.id} "
                    f"(also in {_rel(seen[meta.id], root)})"
                )
                continue
            seen[meta.id] = path
            changelog_path = folder / layout.CHANGELOG_FILENAME
            if not changelog_path.is_file():
                errors.append(f"{_rel(changelog_path, root)}: every document needs a CHANGELOG.md")
                changelog = Changelog((), ("CHANGELOG.md missing",))
            else:
                changelog = parse_changelog(changelog_path.read_text(encoding="utf-8"))
            documents.append(Document(meta=meta, body=body, path=path, changelog=changelog))
    return documents


def _load_controls(root: Path, errors: list[str]) -> list[ControlGuide]:
    guides: list[ControlGuide] = []
    seen: dict[str, Path] = {}
    base = root / layout.CONTROLS_DIR
    if not base.is_dir():
        errors.append(f"{layout.CONTROLS_DIR.as_posix()}: directory not found")
        return guides
    for theme_dir in layout.THEME_DIRS.values():
        directory = base / theme_dir
        if not directory.is_dir():
            errors.append(f"{_rel(directory, root)}: theme directory not found")
            continue
        for path in sorted(directory.glob("*.md")):
            parsed = _read_front_matter(path, root, errors)
            if parsed is None:
                continue
            metadata, body = parsed
            try:
                meta = ControlGuideMeta.model_validate(metadata)
            except ValidationError as exc:
                errors.extend(_format_validation_error(exc, _rel(path, root)))
                continue
            if path.name != f"{meta.control}.md":
                errors.append(f"{_rel(path, root)}: file must be named {meta.control}.md")
                continue
            if meta.control in seen:
                errors.append(
                    f"{_rel(path, root)}: duplicate guide for {meta.control} "
                    f"(also {_rel(seen[meta.control], root)})"
                )
                continue
            seen[meta.control] = path
            guides.append(ControlGuide(meta=meta, body=body, path=path))
    return guides


def _load_mappings(root: Path, errors: list[str]) -> list[Mapping]:
    mappings: list[Mapping] = []
    directory = root / layout.MAPPINGS_DIR
    if not directory.is_dir():
        errors.append(f"{layout.MAPPINGS_DIR.as_posix()}: directory not found")
        return mappings
    for path in sorted(directory.glob("*.yaml")):
        mapping = _load_model(path, Mapping, root, errors)
        if mapping is None:
            continue
        if mapping.name != path.stem:
            errors.append(
                f"{_rel(path, root)}: mapping name {mapping.name!r} must equal the file stem"
            )
            continue
        mappings.append(mapping)
    return mappings


def load_repository(root: Path) -> Repository:
    """Load and schema-validate every file under ``root``; raise :class:`LoaderError` on problems."""
    root = root.resolve()
    errors: list[str] = []
    catalogue = _load_model(root / layout.CATALOGUE, Catalogue, root, errors)
    organisation = _load_model(root / layout.ORGANISATION, Organisation, root, errors)
    roles = _load_model(root / layout.ROLES, RoleRegister, root, errors)
    parties = _load_model(root / layout.INTERESTED_PARTIES, InterestedPartyRegister, root, errors)
    legal = _load_model(root / layout.LEGAL_REGISTER, LegalRegister, root, errors)
    criteria = _load_model(root / layout.RISK_CRITERIA, RiskCriteria, root, errors)
    risks = _load_model(root / layout.RISK_REGISTER, RiskRegister, root, errors)
    mappings = _load_mappings(root, errors)
    documents = _load_documents(root, errors)
    controls = _load_controls(root, errors)
    if errors:
        raise LoaderError(errors)
    assert catalogue and organisation and roles and parties and legal and criteria and risks
    return Repository(
        root=root,
        catalogue=catalogue,
        organisation=organisation,
        roles=roles,
        parties=parties,
        legal=legal,
        criteria=criteria,
        risks=risks,
        mappings=tuple(mappings),
        documents=tuple(documents),
        controls=tuple(controls),
    )
