"""A readable view of the risk register and the criteria it is scored against."""

from __future__ import annotations

from collections import Counter

from isms_as_code.generate.common import md_header, role_title, table
from isms_as_code.loader import Repository
from isms_as_code.models import Risk

__all__ = ["render_risk_view"]


def _score(repo: Repository, likelihood: int, impact: int) -> str:
    score = likelihood * impact
    return f"{likelihood} × {impact} = {score} ({repo.criteria.band_for(score).name})"


def render_risk_view(repo: Repository, digest: str) -> str:
    criteria = repo.criteria
    risks: list[Risk] = sorted(repo.risks.risks, key=lambda r: r.id)
    out = md_header(digest)
    out += f"# Risk register — {repo.organisation.group_name}\n\n"
    out += (
        "Generated view of `isms/risk/risk-register.yaml`, scored against the criteria in "
        "`isms/risk/risk-criteria.yaml` (clauses 6.1.2, 6.1.3 and 8.2). The Statement of "
        "Applicability cites these risk ids as the justification for including controls.\n\n"
    )
    out += "## Criteria\n\n" + criteria.method.strip() + "\n\n"
    out += table(
        ["Band", "Scores", "Response", "May be retained by"],
        [
            [
                b.name,
                f"{b.min_score}–{b.max_score}",
                b.response,
                role_title(repo, b.acceptance) if b.acceptance else "never",
            ]
            for b in sorted(criteria.bands, key=lambda b: b.min_score)
        ],
    )
    out += "\n## Risks\n\n"
    out += table(
        [
            "Id",
            "Risk",
            "Owner",
            "Asset",
            "Inherent",
            "Treatment",
            "Controls",
            "Residual",
            "Status",
            "Accepted by",
            "Review",
        ],
        [
            [
                r.id,
                r.title,
                role_title(repo, r.owner),
                r.asset,
                _score(repo, r.inherent_likelihood, r.inherent_impact),
                r.treatment.value,
                ", ".join(r.controls) or "—",
                _score(repo, r.residual_likelihood, r.residual_impact),
                r.status.value,
                role_title(repo, r.accepted_by) if r.accepted_by else "—",
                r.review_date,
            ]
            for r in risks
        ],
    )
    out += "\n## Residual risk heat map\n\n"
    out += "Rows: impact (5 = severe), columns: likelihood (5 = almost certain); cells list the risks by residual score.\n\n"
    header = ["Impact \\ Likelihood"] + [
        f"{level.level} {level.label}"
        for level in sorted(criteria.likelihood, key=lambda x: x.level)
    ]
    grid: list[list[object]] = []
    for impact in sorted(criteria.impact, key=lambda x: -x.level):
        row: list[object] = [f"{impact.level} {impact.label}"]
        for likelihood in range(1, 6):
            ids = [
                r.id
                for r in risks
                if r.residual_impact == impact.level and r.residual_likelihood == likelihood
            ]
            row.append(", ".join(ids) if ids else "·")
        grid.append(row)
    out += table(header, grid)
    out += "\n## Treatment summary\n\n"
    treatments = Counter(r.treatment.value for r in risks)
    bands = Counter(criteria.band_for(r.residual_score).name for r in risks)
    out += table(
        ["Measure", "Count"],
        [
            *[[f"Treatment: {k}", v] for k, v in sorted(treatments.items())],
            *[[f"Residual band: {k}", v] for k, v in sorted(bands.items())],
        ],
    )
    return out
