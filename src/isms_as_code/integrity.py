"""Hashing and canonical serialisation helpers.

The generators stamp every output with a *source digest* -- a SHA-256 over the sorted relative
paths and contents of the inputs they consumed -- instead of a timestamp. The digest only changes
when an input changes, so re-running ``isms generate`` on an unchanged tree is byte-identical and
CI can diff the committed outputs against a fresh run.

>>> sha256_bytes(b"")
'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

__all__ = [
    "sha256_bytes",
    "sha256_text",
    "sha256_file",
    "canonical_json",
    "write_json",
    "source_digest",
]


def sha256_bytes(data: bytes) -> str:
    """Hex SHA-256 of raw bytes."""
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    """Hex SHA-256 of a string encoded as UTF-8."""
    return sha256_bytes(text.encode("utf-8"))


def sha256_file(path: Path) -> str:
    """Hex SHA-256 of a file's contents."""
    return sha256_bytes(Path(path).read_bytes())


def canonical_json(obj: Any) -> str:
    """Deterministic JSON text: sorted keys, UTF-8, 2-space indent, trailing newline."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, indent=2) + "\n"


def write_json(path: Path, obj: Any) -> None:
    """Write ``obj`` as canonical JSON to ``path`` (parent dirs are created)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json(obj), encoding="utf-8")


def source_digest(paths: Iterable[Path], root: Path) -> str:
    """SHA-256 over ``(relative path, sha256(content))`` pairs in sorted path order."""
    digest = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.relative_to(root).as_posix()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(sha256_file(path).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()
