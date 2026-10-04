"""Review-due reporting: which documents and control assessments are due or overdue on a given day."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date, timedelta

from isms_as_code.durations import Duration
from isms_as_code.loader import Repository
from isms_as_code.models import DocumentStatus

__all__ = ["DueItem", "due_items", "render_due_table", "render_due_markdown", "render_due_json"]

ASSESSMENT_CYCLE = Duration.parse("P1Y")


@dataclass(frozen=True)
class DueItem:
    kind: str
    id: str
    title: str
    owner: str
    due: date
    days_left: int

    @property
    def overdue(self) -> bool:
        return self.days_left < 0


def due_items(repo: Repository, today: date, within_days: int) -> list[DueItem]:
    horizon = today + timedelta(days=within_days)
    catalogue = repo.catalogue.by_id()
    items: list[DueItem] = []
    for document in repo.documents:
        meta = document.meta
        if meta.status is not DocumentStatus.APPROVED or meta.next_review is None:
            continue
        if meta.next_review <= horizon:
            items.append(
                DueItem(
                    "document",
                    meta.id,
                    meta.title,
                    meta.owner,
                    meta.next_review,
                    (meta.next_review - today).days,
                )
            )
    for guide in repo.controls:
        guide_meta = guide.meta
        assessed = guide_meta.last_assessed
        due = ASSESSMENT_CYCLE.add_to(assessed) if assessed else today
        if due <= horizon:
            control = guide_meta.control
            title = catalogue[control].title if control in catalogue else control
            items.append(
                DueItem("control", control, title, guide_meta.owner, due, (due - today).days)
            )
    return sorted(items, key=lambda item: (item.due, item.kind, item.id))


def render_due_table(items: list[DueItem], repo: Repository) -> str:
    if not items:
        return "Nothing is due within the requested window.\n"
    roles = repo.roles.by_key()
    width = max(len(item.id) for item in items)
    lines = [f"{'DUE':<11} {'ID':<{width}}  {'STATE':<9} OWNER — TITLE"]
    for item in items:
        state = f"{-item.days_left}d late" if item.overdue else f"in {item.days_left}d"
        owner = roles[item.owner].title if item.owner in roles else item.owner
        lines.append(
            f"{item.due.isoformat():<11} {item.id:<{width}}  {state:<9} {owner} — {item.title}"
        )
    return "\n".join(lines) + "\n"


def render_due_markdown(items: list[DueItem], repo: Repository, today: date) -> str:
    roles = repo.roles.by_key()
    out = f"# Reviews due as of {today.isoformat()}\n\n"
    if not items:
        return out + "Nothing is due within the requested window.\n"
    out += "| Due | Kind | Id | Title | Owner | State |\n| --- | --- | --- | --- | --- | --- |\n"
    for item in items:
        state = (
            f"**overdue by {-item.days_left} days**"
            if item.overdue
            else f"in {item.days_left} days"
        )
        owner = roles[item.owner].title if item.owner in roles else item.owner
        out += f"| {item.due} | {item.kind} | {item.id} | {item.title} | {owner} | {state} |\n"
    return out


def render_due_json(items: list[DueItem], today: date) -> str:
    payload = {
        "as_of": today.isoformat(),
        "items": [
            {**asdict(item), "due": item.due.isoformat(), "overdue": item.overdue} for item in items
        ],
    }
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"
