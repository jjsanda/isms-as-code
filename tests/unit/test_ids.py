from __future__ import annotations

import pytest

from isms_as_code.ids import control_sort_key, semver_key, slugify

pytestmark = pytest.mark.unit


def test_control_sort_key_orders_numerically() -> None:
    ids = ["A.5.10", "A.5.9", "A.8.1", "A.6.2"]
    assert sorted(ids, key=control_sort_key) == ["A.5.9", "A.5.10", "A.6.2", "A.8.1"]


def test_control_sort_key_rejects_garbage() -> None:
    with pytest.raises(ValueError):
        control_sort_key("POL-ACC")


def test_semver_key() -> None:
    assert semver_key("1.10.0") > semver_key("1.9.3")
    assert semver_key("2.0.0") > semver_key("1.99.99")


@pytest.mark.parametrize(
    ("text", "slug"),
    [
        ("Access Control Policy", "access-control-policy"),
        ("Supplier & Cloud Security Policy", "supplier-cloud-security-policy"),
        ("Kryptographie — Schlüsselverwaltung", "kryptographie-schlusselverwaltung"),
        ("  HR  Security   ", "hr-security"),
    ],
)
def test_slugify(text: str, slug: str) -> None:
    assert slugify(text) == slug
