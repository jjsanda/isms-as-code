from __future__ import annotations

from pathlib import Path

import pytest

from isms_as_code.integrity import (
    canonical_json,
    sha256_file,
    sha256_text,
    source_digest,
    write_json,
)

pytestmark = pytest.mark.unit


def test_canonical_json_sorts_keys_and_keeps_unicode() -> None:
    assert canonical_json({"b": 1, "a": "ü"}) == '{\n  "a": "ü",\n  "b": 1\n}\n'


def test_write_json_and_hashes(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "out.json"
    write_json(path, {"x": [1, 2]})
    assert sha256_file(path) == sha256_text(path.read_text(encoding="utf-8"))


def test_source_digest_is_order_independent_and_content_sensitive(tmp_path: Path) -> None:
    a = tmp_path / "a.txt"
    b = tmp_path / "sub" / "b.txt"
    b.parent.mkdir()
    a.write_text("A", encoding="utf-8")
    b.write_text("B", encoding="utf-8")
    first = source_digest([a, b], tmp_path)
    assert source_digest([b, a, a], tmp_path) == first
    b.write_text("B2", encoding="utf-8")
    assert source_digest([a, b], tmp_path) != first
