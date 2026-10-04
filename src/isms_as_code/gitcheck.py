"""`isms changelog-check`: a changed document needs a CHANGELOG entry and a version bump.

Compares the working tree with a base revision (the pull request's base in CI). For every document
folder with changes it requires that ``CHANGELOG.md`` changed too and that the front-matter version
increased; new documents only need a valid first version.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import frontmatter

from isms_as_code import layout
from isms_as_code.changelog import bump_kind

__all__ = ["changed_document_folders", "check_changelogs"]


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def changed_document_folders(root: Path, base: str) -> dict[str, set[str]]:
    """Map ``<document folder relpath>`` -> set of changed file names within it."""
    names = _git(root, "diff", "--name-only", base, "--").splitlines()
    untracked = _git(root, "ls-files", "--others", "--exclude-standard").splitlines()
    folders: dict[str, set[str]] = {}
    for name in names + untracked:
        path = Path(name)
        for relative in layout.DOCUMENT_DIRS.values():
            parts = relative.parts
            if path.parts[: len(parts)] == parts and len(path.parts) > len(parts) + 1:
                folder = Path(*path.parts[: len(parts) + 1]).as_posix()
                folders.setdefault(folder, set()).add(path.parts[len(parts) + 1])
    return folders


def _version_at(root: Path, base: str, folder: str) -> str | None:
    try:
        text = _git(root, "show", f"{base}:{folder}/{layout.DOCUMENT_FILENAME}")
    except RuntimeError:
        return None
    post = frontmatter.loads(text)
    return str(post.metadata.get("version")) if post.metadata else None


def check_changelogs(root: Path, base: str) -> list[str]:
    """Return problems; an empty list means every changed document also bumped its version and CHANGELOG."""
    problems: list[str] = []
    for folder, files in sorted(changed_document_folders(root, base).items()):
        readme = root / folder / layout.DOCUMENT_FILENAME
        if not readme.is_file():
            problems.append(f"{folder}: {layout.DOCUMENT_FILENAME} is missing")
            continue
        new_version = str(frontmatter.load(str(readme)).metadata.get("version", ""))
        old_version = _version_at(root, base, folder)
        if layout.CHANGELOG_FILENAME not in files:
            problems.append(f"{folder}: changed without a {layout.CHANGELOG_FILENAME} entry")
        if old_version is None:
            continue  # new document; the validator checks its first version
        if not new_version or bump_kind(old_version, new_version) is None:
            problems.append(
                f"{folder}: version must be bumped (base {old_version}, now {new_version or '?'})"
            )
    return problems
