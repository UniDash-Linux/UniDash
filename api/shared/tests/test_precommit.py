"""Tests for pre-commit hook configuration.

These tests verify that pre-commit is properly configured.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent


def test_precommit_config_exists() -> None:
    """Verify .pre-commit-config.yaml exists."""
    config_path = PROJECT_ROOT / ".pre-commit-config.yaml"
    assert config_path.is_file(), "Missing .pre-commit-config.yaml"


def test_precommit_config_valid() -> None:
    """Verify pre-commit config is valid YAML."""
    import yaml

    config_path = PROJECT_ROOT / ".pre-commit-config.yaml"
    assert config_path.is_file(), "Missing .pre-commit-config.yaml"

    with open(config_path) as f:
        config = yaml.safe_load(f)

    assert "repos" in config, "Missing 'repos' section in pre-commit config"
    assert len(config["repos"]) > 0, "No hooks configured in pre-commit"
