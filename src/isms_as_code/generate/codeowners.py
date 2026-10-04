"""CODEOWNERS generated from document ownership: review routing derives from the documents."""

from __future__ import annotations

from isms_as_code import layout
from isms_as_code.generate.common import hash_header
from isms_as_code.loader import Repository

__all__ = ["render_codeowners"]


def _handles(repo: Repository, *keys: str | None) -> str:
    roles = repo.roles.by_key()
    handles: list[str] = []
    for key in keys:
        if key is None:
            continue
        handle = roles[key].github
        if handle not in handles:
            handles.append(handle)
    return " ".join(handles)


def render_codeowners(repo: Repository, digest: str) -> str:
    roles = repo.roles.by_key()
    isms = repo.organisation.isms_owner
    top = repo.organisation.management_representative
    out = hash_header(digest, "the ownership metadata of the ISMS documents")
    out += (
        "#\n"
        "# Every controlled document names an owner role and an approver role in its front matter;\n"
        "# roles map to GitHub handles or teams in isms/context/roles.yaml. Pull requests that touch a\n"
        "# document are therefore routed to exactly the roles that must review and approve it\n"
        "# (PROC-DOC, stage 3). Control guides route to the control owner and the ISMS owner.\n"
        "#\n# Role -> handle:\n"
    )
    for role in repo.roles.roles:
        out += f"#   {role.key:<28} {role.github}  ({role.title})\n"
    out += "\n# Default: the ISMS owner reviews everything not listed below.\n"
    out += f"*  {_handles(repo, isms)}\n\n"
    out += "# Tooling, workflows and the generated artefacts.\n"
    for path in (
        "/src/",
        "/tests/",
        "/scripts/",
        "/.github/",
        "/generated/",
        "/pyproject.toml",
        "/Makefile",
    ):
        out += f"{path}  {_handles(repo, isms)}\n"
    out += "\n# Registers and catalogue: the ISMS owner and top management.\n"
    for path in (
        "/isms/catalogue/",
        "/isms/context/",
        "/isms/risk/",
        "/isms/mappings/",
        "/isms/templates/",
    ):
        out += f"{path}  {_handles(repo, isms, top)}\n"
    out += "\n# Controlled documents: owner role and approver role.\n"
    for document in sorted(repo.documents, key=lambda d: d.meta.id):
        folder = "/" + repo.relpath(document.folder) + "/"
        approver = document.meta.approver
        out += f"# {document.meta.id}: owner {document.meta.owner}"
        out += f", approver {approver}\n" if approver else "\n"
        out += f"{folder}  {_handles(repo, document.meta.owner, approver)}\n"
    out += "\n# Control implementation guides: control owner and the ISMS owner.\n"
    for guide in sorted(repo.controls, key=lambda g: repo.relpath(g.path)):
        owner = guide.meta.owner
        if owner not in roles:
            continue
        out += f"/{repo.relpath(guide.path)}  {_handles(repo, owner, isms)}\n"
    assert layout.CODEOWNERS.name == "CODEOWNERS"
    return out
