"""Tests for GitHub Actions CI workflows.

These tests verify that CI workflow files exist and are valid.
"""

from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
WORKFLOWS_DIR = PROJECT_ROOT / ".github" / "workflows"


def test_ci_python_workflow_exists() -> None:
    """Verify Python CI workflow exists."""
    workflow_path = WORKFLOWS_DIR / "ci-python.yml"
    assert workflow_path.is_file(), "Missing .github/workflows/ci-python.yml"


def test_ci_web_workflow_exists() -> None:
    """Verify Web CI workflow exists."""
    workflow_path = WORKFLOWS_DIR / "ci-web.yml"
    assert workflow_path.is_file(), "Missing .github/workflows/ci-web.yml"


def test_docs_deploy_workflow_exists() -> None:
    """Verify docs deploy workflow exists."""
    workflow_path = WORKFLOWS_DIR / "docs-deploy.yml"
    assert workflow_path.is_file(), "Missing .github/workflows/docs-deploy.yml"


def test_workflows_valid_yaml() -> None:
    """Verify all workflow files are valid YAML."""
    assert WORKFLOWS_DIR.is_dir(), "Missing .github/workflows directory"

    for workflow_file in WORKFLOWS_DIR.glob("*.yml"):
        with open(workflow_file) as f:
            config = yaml.safe_load(f)
            assert config is not None, f"Empty workflow: {workflow_file.name}"
            assert (
                "on" in config or True in config
            ), f"Missing 'on' trigger in {workflow_file.name}"


def test_ci_python_runs_linters() -> None:
    """Verify Python CI workflow runs ruff and black linters."""
    workflow_path = WORKFLOWS_DIR / "ci-python.yml"
    content = workflow_path.read_text()
    assert "ruff check" in content, "ci-python.yml should run ruff check"
    assert "black --check" in content, "ci-python.yml should run black --check"


def test_ci_python_runs_coverage() -> None:
    """Verify Python CI workflow runs tests with coverage."""
    workflow_path = WORKFLOWS_DIR / "ci-python.yml"
    content = workflow_path.read_text()
    assert "--cov" in content, "ci-python.yml should run tests with coverage"
    assert (
        "cov-fail-under" in content
    ), "ci-python.yml should enforce coverage threshold"


def test_ci_web_runs_linters() -> None:
    """Verify Web CI workflow runs ESLint and Prettier."""
    workflow_path = WORKFLOWS_DIR / "ci-web.yml"
    content = workflow_path.read_text()
    assert "npm run lint" in content, "ci-web.yml should run ESLint"
    assert "prettier" in content, "ci-web.yml should run Prettier"


def test_ci_web_runs_coverage() -> None:
    """Verify Web CI workflow runs tests with coverage."""
    workflow_path = WORKFLOWS_DIR / "ci-web.yml"
    content = workflow_path.read_text()
    assert "test:coverage" in content, "ci-web.yml should run tests with coverage"


def test_codeql_workflow_exists() -> None:
    """Verify CodeQL security workflow exists."""
    workflow_path = WORKFLOWS_DIR / "codeql.yml"
    assert workflow_path.is_file(), "Missing .github/workflows/codeql.yml"


def test_codeql_scans_both_languages() -> None:
    """Verify CodeQL scans Python and JavaScript/TypeScript."""
    workflow_path = WORKFLOWS_DIR / "codeql.yml"
    content = workflow_path.read_text()
    assert "python" in content, "codeql.yml should scan Python"
    assert "javascript-typescript" in content, "codeql.yml should scan JS/TS"
