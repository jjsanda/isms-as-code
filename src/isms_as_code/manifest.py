"""SHA-256 manifest over the build output (``dist/SHA256SUMS``), in the ``sha256sum -c`` format."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from isms_as_code.integrity import sha256_file

__all__ = ["MANIFEST_NAME", "write_manifest", "verify_manifest", "collect_outputs"]

MANIFEST_NAME = "SHA256SUMS"


def collect_outputs(dist: Path) -> list[Path]:
    """Every file under ``dist`` except the manifest itself, sorted by relative path."""
    return sorted(
        (p for p in dist.rglob("*") if p.is_file() and p.name != MANIFEST_NAME),
        key=lambda p: p.relative_to(dist).as_posix(),
    )


def write_manifest(dist: Path, paths: Iterable[Path] | None = None) -> Path:
    files = list(paths) if paths is not None else collect_outputs(dist)
    lines = [f"{sha256_file(path)}  {path.relative_to(dist).as_posix()}" for path in files]
    manifest = dist / MANIFEST_NAME
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return manifest


def verify_manifest(dist: Path) -> list[str]:
    """Return problems (missing files, mismatching hashes, unlisted files); empty means intact."""
    manifest = dist / MANIFEST_NAME
    if not manifest.is_file():
        return [f"{MANIFEST_NAME} is missing"]
    problems: list[str] = []
    listed: set[str] = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, _, relative = line.partition("  ")
        listed.add(relative)
        path = dist / relative
        if not path.is_file():
            problems.append(f"{relative}: listed in the manifest but missing")
        elif sha256_file(path) != digest:
            problems.append(
                f"{relative}: hash mismatch (file changed after the manifest was written)"
            )
    for path in collect_outputs(dist):
        relative = path.relative_to(dist).as_posix()
        if relative not in listed:
            problems.append(f"{relative}: present but not listed in the manifest")
    return problems
