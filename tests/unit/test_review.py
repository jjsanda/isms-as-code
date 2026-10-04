from __future__ import annotations

import json
from datetime import date

import pytest

from isms_as_code.loader import load_repository
from isms_as_code.review import due_items, render_due_json, render_due_markdown, render_due_table
from tests.conftest import RepoBuilder

pytestmark = pytest.mark.unit


def test_due_items_window_and_overdue(builder: RepoBuilder) -> None:
    builder.add_control("A.6.1", last_assessed=date(2025, 1, 1))
    builder.add_control("A.6.2", last_assessed=None)
    repo = load_repository(builder.root)
    today = date(2026, 8, 20)
    items = due_items(repo, today, 0)
    assert [(i.kind, i.id, i.days_left) for i in items] == [
        ("control", "A.6.1", -231),
        ("control", "A.6.2", 0),
    ]
    assert items[0].overdue and not items[1].overdue
    wide = due_items(repo, today, 400)
    assert ("document", "POL-TEST") in {(i.kind, i.id) for i in wide}
    doc = next(i for i in wide if i.kind == "document")
    assert doc.due == date(2027, 1, 10) and doc.days_left == 143
    assert "A.5.15" in {
        i.id for i in wide
    }  # assessed 2026-06-01 -> due 2027-06-01, within 400 days


def test_renderers(builder: RepoBuilder) -> None:
    repo = load_repository(builder.root)
    today = date(2026, 8, 20)
    assert render_due_table([], repo).startswith("Nothing is due")
    assert "Nothing is due" in render_due_markdown([], repo, today)
    builder.add_control("A.6.1", last_assessed=date(2025, 1, 1))
    repo = load_repository(builder.root)
    items = due_items(repo, today, 0)
    table = render_due_table(items, repo)
    assert "231d late" in table and "ISMS Manager" in table
    markdown = render_due_markdown(items, repo, today)
    assert "**overdue by 231 days**" in markdown
    payload = json.loads(render_due_json(items, today))
    assert payload["as_of"] == "2026-08-20" and payload["items"][0]["overdue"] is True
