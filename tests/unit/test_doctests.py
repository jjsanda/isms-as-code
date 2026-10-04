from __future__ import annotations

import doctest
import importlib

import pytest

pytestmark = pytest.mark.unit

MODULES = [
    "isms_as_code.clock",
    "isms_as_code.ids",
    "isms_as_code.durations",
    "isms_as_code.sections",
    "isms_as_code.changelog",
    "isms_as_code.integrity",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_doctests(name: str) -> None:
    result = doctest.testmod(importlib.import_module(name))
    assert result.failed == 0
    assert result.attempted > 0
