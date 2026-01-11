"""Tests for linter configuration validation.

These tests verify that Ruff and Black pass on the codebase.
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

# Get the venv bin directory to find installed tools
VENV_BIN = Path(sys.executable).parent


def test_ruff_check_passes() -> None:
    """Verify ruff check passes on API codebase."""
    ruff_path = VENV_BIN / "ruff"
    result = subprocess.run(
        [str(ruff_path), "check", "api/"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Ruff check failed: {result.stdout}{result.stderr}"


def test_black_check_passes() -> None:
    """Verify black formatting check passes on API codebase."""
    black_path = VENV_BIN / "black"
    result = subprocess.run(
        [str(black_path), "--check", "api/"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Black check failed: {result.stdout}{result.stderr}"


def test_ruff_toml_exists() -> None:
    """Verify ruff.toml configuration file exists."""
    ruff_config = PROJECT_ROOT / "ruff.toml"
    assert ruff_config.is_file(), "Missing ruff.toml configuration file"
