"""Tests for documentation enforcement configuration.

Verifies that Ruff docstring rules, ESLint JSDoc rules,
and CodeRabbit AI configuration are properly set up.
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent


class TestRuffDocstringRules:
    """Test suite for Ruff docstring configuration."""

    def test_ruff_toml_exists(self) -> None:
        """Verify ruff.toml exists at project root."""
        ruff_toml = PROJECT_ROOT / "ruff.toml"
        assert ruff_toml.is_file(), "Missing required file: ruff.toml"

    def test_ruff_docstring_rules_enabled(self) -> None:
        """Verify Ruff D rules are enabled for docstrings."""
        ruff_toml = PROJECT_ROOT / "ruff.toml"
        assert ruff_toml.is_file(), "Missing required file: ruff.toml"
        content = ruff_toml.read_text()
        assert (
            '"D"' in content or "'D'" in content
        ), "ruff.toml should enable D rules for docstrings"

    def test_ruff_pydocstyle_convention(self) -> None:
        """Verify Ruff uses Google style docstrings."""
        ruff_toml = PROJECT_ROOT / "ruff.toml"
        assert ruff_toml.is_file(), "Missing required file: ruff.toml"
        content = ruff_toml.read_text()
        assert (
            "google" in content.lower()
        ), "ruff.toml should use google convention for docstrings"


class TestESLintJSDocRules:
    """Test suite for ESLint JSDoc configuration."""

    def test_eslint_config_exists(self) -> None:
        """Verify eslint.config.js exists in web directory."""
        eslint_config = PROJECT_ROOT / "web" / "eslint.config.js"
        assert eslint_config.is_file(), "Missing required file: web/eslint.config.js"

    def test_eslint_jsdoc_plugin_installed(self) -> None:
        """Verify eslint-plugin-jsdoc is in package.json."""
        package_json = PROJECT_ROOT / "web" / "package.json"
        assert package_json.is_file(), "Missing required file: web/package.json"
        content = json.loads(package_json.read_text())
        dev_deps = content.get("devDependencies", {})
        assert (
            "eslint-plugin-jsdoc" in dev_deps
        ), "eslint-plugin-jsdoc should be in devDependencies"

    def test_eslint_jsdoc_rules_configured(self) -> None:
        """Verify JSDoc rules are configured in eslint.config.js."""
        eslint_config = PROJECT_ROOT / "web" / "eslint.config.js"
        assert eslint_config.is_file(), "Missing required file: web/eslint.config.js"
        content = eslint_config.read_text()
        assert "jsdoc" in content, "eslint.config.js should configure jsdoc plugin"


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
        assert (
            workflow.is_file()
        ), "Missing required file: .github/workflows/docs-check.yml"
        content = workflow.read_text()
        assert "api/" in content, "docs-check.yml should check api/ directory"
        assert "docs/" in content, "docs-check.yml should check docs/ directory"


class TestCodeRabbitConfig:
    """Test suite for CodeRabbit AI configuration."""

    def test_coderabbit_config_exists(self) -> None:
        """Verify .coderabbit.yaml exists at project root."""
        coderabbit = PROJECT_ROOT / ".coderabbit.yaml"
        assert coderabbit.is_file(), "Missing required file: .coderabbit.yaml"

    def test_coderabbit_language_english(self) -> None:
        """Verify CodeRabbit is configured for English reviews."""
        coderabbit = PROJECT_ROOT / ".coderabbit.yaml"
        assert coderabbit.is_file(), "Missing required file: .coderabbit.yaml"
        content = coderabbit.read_text()
        assert (
            "english" in content.lower() or "en" in content.lower()
        ), ".coderabbit.yaml should configure English language"
