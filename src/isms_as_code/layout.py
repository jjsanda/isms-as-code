"""Where things live in the repository. One place to change if the layout ever moves."""

from __future__ import annotations

from pathlib import Path

__all__ = [
    "CATALOGUE",
    "ORGANISATION",
    "ROLES",
    "INTERESTED_PARTIES",
    "LEGAL_REGISTER",
    "RISK_CRITERIA",
    "RISK_REGISTER",
    "MAPPINGS_DIR",
    "CONTROLS_DIR",
    "DOCUMENT_DIRS",
    "TEMPLATES_DIR",
    "GENERATED_DIR",
    "CODEOWNERS",
    "DOCUMENT_FILENAME",
    "CHANGELOG_FILENAME",
    "THEME_DIRS",
    "find_repo_root",
]

CATALOGUE = Path("isms/catalogue/iso27001-2022-annex-a.yaml")
ORGANISATION = Path("isms/context/organisation.yaml")
ROLES = Path("isms/context/roles.yaml")
INTERESTED_PARTIES = Path("isms/context/interested-parties.yaml")
LEGAL_REGISTER = Path("isms/context/legal-register.yaml")
RISK_CRITERIA = Path("isms/risk/risk-criteria.yaml")
RISK_REGISTER = Path("isms/risk/risk-register.yaml")
MAPPINGS_DIR = Path("isms/mappings")
CONTROLS_DIR = Path("isms/controls")
TEMPLATES_DIR = Path("isms/templates")
GENERATED_DIR = Path("generated")
CODEOWNERS = Path(".github/CODEOWNERS")
DOCUMENT_FILENAME = "README.md"
CHANGELOG_FILENAME = "CHANGELOG.md"

# Document type -> directory that holds one folder per document.
DOCUMENT_DIRS: dict[str, Path] = {
    "policy": Path("isms/policies"),
    "standard": Path("isms/standards"),
    "procedure": Path("isms/procedures"),
}

# Annex A theme -> directory that holds one control implementation guide per control.
THEME_DIRS: dict[str, str] = {
    "organizational": "5-organizational",
    "people": "6-people",
    "physical": "7-physical",
    "technological": "8-technological",
}


def find_repo_root(start: Path | None = None) -> Path:
    """Walk upwards from ``start`` (default: cwd) until a directory containing ``isms/`` is found."""
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "isms").is_dir() and (candidate / "pyproject.toml").is_file():
            return candidate
    raise FileNotFoundError(
        "not inside an isms-as-code repository (no isms/ directory found above "
        f"{current}); pass --root explicitly"
    )
