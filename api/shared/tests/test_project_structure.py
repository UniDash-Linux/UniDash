"""Tests for project directory structure validation.

These tests verify that the UniDash project structure follows
the architecture defined in architecture.md.
"""

from pathlib import Path

import pytest

# Remonter de api/shared/tests vers la racine du projet
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

# Infrastructure directories
INFRA_DIRS = [
    "infra/ansible/playbooks",
    "infra/ansible/inventory",
    "infra/k8s/manifests",
    "infra/k8s/helm",
]

# API directories with src layout PyPA
API_DIRS = [
    "api/shared/src/unidash_shared",
    "api/shared/tests/unidash_shared",
    "api/db/src/unidash_db",
    "api/db/tests/unidash_db",
    "api/sso/src/unidash_sso",
    "api/sso/tests/unidash_sso",
    "api/unidash/src/unidash_api",
    "api/unidash/tests/unidash_api",
    "api/admin/src/unidash_admin",
    "api/admin/tests/unidash_admin",
    "api/backup/src/unidash_backup",
    "api/backup/tests/unidash_backup",
]

# Web frontend directories
WEB_DIRS = [
    "web/src/pages",
    "web/src/features",
    "web/src/shared",
    "web/src/lib",
]

# Documentation directories
DOCS_DIRS = [
    "docs/src/content/docs",
]

# GitHub workflows directory
GITHUB_DIRS = [
    ".github/workflows",
]

# All required directories
ALL_REQUIRED_DIRS = INFRA_DIRS + API_DIRS + WEB_DIRS + DOCS_DIRS + GITHUB_DIRS


@pytest.mark.parametrize("directory", INFRA_DIRS)
def test_infra_directories_exist(directory: str) -> None:
    """Verify infrastructure directories exist."""
    path = PROJECT_ROOT / directory
    assert path.is_dir(), f"Missing infrastructure directory: {directory}"


@pytest.mark.parametrize("directory", API_DIRS)
def test_api_directories_exist(directory: str) -> None:
    """Verify API directories with src layout exist."""
    path = PROJECT_ROOT / directory
    assert path.is_dir(), f"Missing API directory: {directory}"


@pytest.mark.parametrize("directory", WEB_DIRS)
def test_web_directories_exist(directory: str) -> None:
    """Verify web frontend directories exist."""
    path = PROJECT_ROOT / directory
    assert path.is_dir(), f"Missing web directory: {directory}"


@pytest.mark.parametrize("directory", DOCS_DIRS)
def test_docs_directory_exists(directory: str) -> None:
    """Verify documentation directories exist."""
    path = PROJECT_ROOT / directory
    assert path.is_dir(), f"Missing docs directory: {directory}"


@pytest.mark.parametrize("directory", GITHUB_DIRS)
def test_github_workflows_directory_exists(directory: str) -> None:
    """Verify GitHub workflows directory exists."""
    path = PROJECT_ROOT / directory
    assert path.is_dir(), f"Missing GitHub directory: {directory}"
