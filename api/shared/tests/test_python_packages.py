"""Tests for Python package importability and configuration.

These tests verify that all UniDash Python packages can be imported
and have valid pyproject.toml configurations.
"""

import subprocess
import sys
from pathlib import Path

import pytest

# Remonter de api/shared/tests vers la racine du projet
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

PACKAGES = [
    "unidash_shared",
    "unidash_db",
    "unidash_sso",
    "unidash_api",
    "unidash_admin",
    "unidash_backup",
]

API_DIRS = [
    "api/shared",
    "api/db",
    "api/sso",
    "api/unidash",
    "api/admin",
    "api/backup",
]


@pytest.mark.parametrize("package", PACKAGES)
def test_package_importable(package: str) -> None:
    """Verify each package can be imported."""
    result = subprocess.run(
        [sys.executable, "-c", f"import {package}"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Cannot import {package}: {result.stderr}"


@pytest.mark.parametrize("api_dir", API_DIRS)
def test_pyproject_toml_exists(api_dir: str) -> None:
    """Verify each API has a pyproject.toml file."""
    pyproject_path = PROJECT_ROOT / api_dir / "pyproject.toml"
    assert pyproject_path.is_file(), f"Missing pyproject.toml in {api_dir}"


@pytest.mark.parametrize("api_dir", API_DIRS)
def test_pyproject_toml_valid(api_dir: str) -> None:
    """Verify each pyproject.toml is valid TOML."""
    import tomllib

    pyproject_path = PROJECT_ROOT / api_dir / "pyproject.toml"
    if not pyproject_path.is_file():
        pytest.skip(f"pyproject.toml not found in {api_dir}")

    with open(pyproject_path, "rb") as f:
        config = tomllib.load(f)

    # Verify required sections
    assert "project" in config, f"Missing [project] section in {api_dir}/pyproject.toml"
    assert (
        "name" in config["project"]
    ), f"Missing project name in {api_dir}/pyproject.toml"
    assert (
        "requires-python" in config["project"]
    ), f"Missing requires-python in {api_dir}/pyproject.toml"
