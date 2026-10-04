#!/usr/bin/env python3
"""Open one GitHub issue per due review item (idempotent). Used by review-reminders.yml.

Reads the JSON produced by `isms review-due --format json` and calls the `gh` CLI. An item is
skipped when an open issue with the same title already exists, so the weekly run never spams.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

LABEL = "review-due"


def gh(*args: str) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise SystemExit(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def main(path: str) -> None:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    items = payload["items"]
    if not items:
        print("nothing due")
        return
    gh(
        "label",
        "create",
        LABEL,
        "--color",
        "D93F0B",
        "--description",
        "Document or control review is due",
        "--force",
    )
    existing = {
        issue["title"]
        for issue in json.loads(
            gh(
                "issue",
                "list",
                "--label",
                LABEL,
                "--state",
                "open",
                "--limit",
                "500",
                "--json",
                "title",
            )
        )
    }
    opened = 0
    for item in items:
        state = (
            f"overdue by {-item['days_left']} days"
            if item["overdue"]
            else f"due in {item['days_left']} days"
        )
        title = f"Review due: {item['id']} — {item['title']} ({item['due']})"
        if title in existing:
            continue
        body = (
            f"**{item['kind'].capitalize()} {item['id']}** — {item['title']}\n\n"
            f"- Owner role: `{item['owner']}`\n- Due: {item['due']} ({state})\n- As of: {payload['as_of']}\n\n"
            "Review the item, then either change it (new version + CHANGELOG entry, PROC-DOC stage 4) "
            "or record a periodic review without change (PATCH version, PROC-DOC stage 5). "
            "Control guides: update `last_assessed`, evidence and metrics.\n"
        )
        gh("issue", "create", "--title", title, "--label", LABEL, "--body", body)
        opened += 1
    print(f"opened {opened} issue(s); {len(items) - opened} already open")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "due.json")
