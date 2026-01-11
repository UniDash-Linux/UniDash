"""Tests for documentation enforcement configuration.

Verifies that Ruff docstring rules, ESLint JSDoc rules,
and CodeRabbit AI configuration are properly set up.
"""

import json
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent


@pytest.fixture
def ruff_toml_content() -> str:
    """Read ruff.toml content once for all tests."""
    ruff_toml = PROJECT_ROOT / "ruff.toml"
    assert ruff_toml.is_file(), "Missing required file: ruff.toml"
    return ruff_toml.read_text()


@pytest.fixture
def eslint_config_content() -> str:
    """Read eslint.config.js content once for all tests."""
    eslint_config = PROJECT_ROOT / "web" / "eslint.config.js"
    assert eslint_config.is_file(), "Missing required file: web/eslint.config.js"
    return eslint_config.read_text()


@pytest.fixture
def coderabbit_content() -> str:
    """Read .coderabbit.yaml content once for all tests."""
    coderabbit = PROJECT_ROOT / ".coderabbit.yaml"
    assert coderabbit.is_file(), "Missing required file: .coderabbit.yaml"
    return coderabbit.read_text()


class TestRuffDocstringRules:
    """Test suite for Ruff docstring configuration."""

    def test_ruff_docstring_rules_enabled(self, ruff_toml_content: str) -> None:
        """Verify Ruff D rules are enabled for docstrings."""
        assert (
            '"D"' in ruff_toml_content or "'D'" in ruff_toml_content
        ), "ruff.toml should enable D rules for docstrings"

    def test_ruff_pydocstyle_convention(self, ruff_toml_content: str) -> None:
        """Verify Ruff uses Google style docstrings."""
        assert (
            "google" in ruff_toml_content.lower()
        ), "ruff.toml should use google convention for docstrings"


class TestESLintJSDocRules:
    """Test suite for ESLint JSDoc configuration."""

    def test_eslint_jsdoc_plugin_installed(self) -> None:
        """Verify eslint-plugin-jsdoc is in package.json."""
        package_json = PROJECT_ROOT / "web" / "package.json"
        assert package_json.is_file(), "Missing required file: web/package.json"
        content = json.loads(package_json.read_text())
        dev_deps = content.get("devDependencies", {})
        assert (
            "eslint-plugin-jsdoc" in dev_deps
        ), "eslint-plugin-jsdoc should be in devDependencies"

    def test_eslint_jsdoc_rules_configured(self, eslint_config_content: str) -> None:
        """Verify JSDoc rules are configured in eslint.config.js."""
        assert (
            "jsdoc" in eslint_config_content
        ), "eslint.config.js should configure jsdoc plugin"


class TestDocsCheckWorkflow:
    """Test suite for documentation check GitHub workflow."""

    def test_docs_check_workflow_exists(self) -> None:
        """Verify docs-check.yml workflow exists."""
        workflow = PROJECT_ROOT / ".github" / "workflows" / "docs-check.yml"
        assert (
            workflow.is_file()
        ), "Missing required file: .github/workflows/docs-check.yml"

    def test_docs_check_workflow_validates_api_docs(self) -> None:
        """Verify workflow checks api/ changes require docs/api/ updates."""
        workflow = PROJECT_ROOT / ".github" / "workflows" / "docs-check.yml"
        content = workflow.read_text()
        assert "api/" in content, "docs-check.yml should check api/ directory"
        assert "docs/" in content, "docs-check.yml should check docs/ directory"


class TestCodeRabbitConfig:
    """Test suite for CodeRabbit AI configuration."""

    def test_coderabbit_language_english(self, coderabbit_content: str) -> None:
        """Verify CodeRabbit is configured for English reviews."""
        assert (
            "english" in coderabbit_content.lower()
            or "en" in coderabbit_content.lower()
        ), ".coderabbit.yaml should configure English language"
