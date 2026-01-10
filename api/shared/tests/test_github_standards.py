"""Tests for GitHub Community Standards files.

Verifies that all required GitHub Community Standards files exist
and contain the expected content structure.
"""

from pathlib import Path

import pytest

# Navigate from api/shared/tests to project root
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent


class TestGitHubCommunityStandards:
    """Test suite for GitHub Community Standards compliance."""

    def test_readme_exists(self) -> None:
        """Verify README.md exists at project root."""
        readme = PROJECT_ROOT / "README.md"
        assert readme.is_file(), "Missing required file: README.md"

    def test_readme_has_required_sections(self) -> None:
        """Verify README.md contains required sections."""
        readme = PROJECT_ROOT / "README.md"
        if not readme.is_file():
            pytest.skip("README.md does not exist yet")

        content = readme.read_text()
        required_sections = [
            "# UniDash",
            "## Documentation",
            "## Quick Start",
            "## Contributing",
            "## License",
        ]
        for section in required_sections:
            assert section in content, f"README.md missing section: {section}"

    def test_contributing_exists(self) -> None:
        """Verify CONTRIBUTING.md exists at project root."""
        contributing = PROJECT_ROOT / "CONTRIBUTING.md"
        assert contributing.is_file(), "Missing required file: CONTRIBUTING.md"

    def test_contributing_has_required_sections(self) -> None:
        """Verify CONTRIBUTING.md contains required sections."""
        contributing = PROJECT_ROOT / "CONTRIBUTING.md"
        if not contributing.is_file():
            pytest.skip("CONTRIBUTING.md does not exist yet")

        content = contributing.read_text()
        required_sections = [
            "# Contributing",
            "## Development Setup",
            "## GitFlow",
            "## Conventional Commits",
            "## Code Style",
            "## Testing",
            "## Pull Request",
        ]
        for section in required_sections:
            assert section in content, f"CONTRIBUTING.md missing section: {section}"

    def test_code_of_conduct_exists(self) -> None:
        """Verify CODE_OF_CONDUCT.md exists at project root."""
        coc = PROJECT_ROOT / "CODE_OF_CONDUCT.md"
        assert coc.is_file(), "Missing required file: CODE_OF_CONDUCT.md"

    def test_code_of_conduct_is_contributor_covenant(self) -> None:
        """Verify CODE_OF_CONDUCT.md is Contributor Covenant v2.1."""
        coc = PROJECT_ROOT / "CODE_OF_CONDUCT.md"
        if not coc.is_file():
            pytest.skip("CODE_OF_CONDUCT.md does not exist yet")

        content = coc.read_text()
        assert (
            "Contributor Covenant" in content
        ), "CODE_OF_CONDUCT.md should be Contributor Covenant"
        assert "2.1" in content, "CODE_OF_CONDUCT.md should be version 2.1"

    def test_license_exists(self) -> None:
        """Verify LICENSE exists at project root."""
        license_file = PROJECT_ROOT / "LICENSE"
        assert license_file.is_file(), "Missing required file: LICENSE"

    def test_license_is_valid(self) -> None:
        """Verify LICENSE is a valid open source license (LGPL or MIT)."""
        license_file = PROJECT_ROOT / "LICENSE"
        if not license_file.is_file():
            pytest.skip("LICENSE does not exist yet")

        content = license_file.read_text()
        is_lgpl = (
            "GNU LESSER GENERAL PUBLIC LICENSE" in content
            or "GNU Lesser General Public License" in content
        )
        is_mit = "MIT License" in content
        assert is_lgpl or is_mit, "LICENSE should be LGPL or MIT"

    def test_security_exists(self) -> None:
        """Verify SECURITY.md exists at project root."""
        security = PROJECT_ROOT / "SECURITY.md"
        assert security.is_file(), "Missing required file: SECURITY.md"

    def test_security_has_required_sections(self) -> None:
        """Verify SECURITY.md contains required sections."""
        security = PROJECT_ROOT / "SECURITY.md"
        if not security.is_file():
            pytest.skip("SECURITY.md does not exist yet")

        content = security.read_text()
        required_sections = [
            "# Security Policy",
            "## Supported Versions",
            "## Reporting a Vulnerability",
        ]
        for section in required_sections:
            assert section in content, f"SECURITY.md missing section: {section}"


class TestGitHubIssueTemplates:
    """Test suite for GitHub Issue Templates."""

    def test_issue_template_directory_exists(self) -> None:
        """Verify .github/ISSUE_TEMPLATE/ directory exists."""
        issue_dir = PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE"
        assert issue_dir.is_dir(), "Missing required directory: .github/ISSUE_TEMPLATE/"

    def test_bug_report_template_exists(self) -> None:
        """Verify bug_report.yml exists."""
        bug_report = PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml"
        assert (
            bug_report.is_file()
        ), "Missing required file: .github/ISSUE_TEMPLATE/bug_report.yml"

    def test_feature_request_template_exists(self) -> None:
        """Verify feature_request.yml exists."""
        feature_request = (
            PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml"
        )
        assert (
            feature_request.is_file()
        ), "Missing required file: .github/ISSUE_TEMPLATE/feature_request.yml"

    def test_question_template_exists(self) -> None:
        """Verify question.yml exists."""
        question = PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "question.yml"
        assert (
            question.is_file()
        ), "Missing required file: .github/ISSUE_TEMPLATE/question.yml"

    def test_issue_config_exists(self) -> None:
        """Verify config.yml exists for issue templates."""
        config = PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml"
        assert (
            config.is_file()
        ), "Missing required file: .github/ISSUE_TEMPLATE/config.yml"


class TestGitHubPRTemplate:
    """Test suite for GitHub PR Template."""

    def test_pr_template_exists(self) -> None:
        """Verify PULL_REQUEST_TEMPLATE.md exists."""
        pr_template = PROJECT_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
        assert (
            pr_template.is_file()
        ), "Missing required file: .github/PULL_REQUEST_TEMPLATE.md"

    def test_pr_template_has_required_sections(self) -> None:
        """Verify PR template contains required sections."""
        pr_template = PROJECT_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
        if not pr_template.is_file():
            pytest.skip("PULL_REQUEST_TEMPLATE.md does not exist yet")

        content = pr_template.read_text()
        required_sections = [
            "## Description",
            "## Type of Change",
            "## Checklist",
        ]
        for section in required_sections:
            assert section in content, f"PR template missing section: {section}"


class TestDependabot:
    """Test suite for Dependabot configuration."""

    def test_dependabot_exists(self) -> None:
        """Verify dependabot.yml exists."""
        dependabot = PROJECT_ROOT / ".github" / "dependabot.yml"
        assert dependabot.is_file(), "Missing required file: .github/dependabot.yml"

    def test_dependabot_has_required_ecosystems(self) -> None:
        """Verify dependabot.yml configures required ecosystems."""
        dependabot = PROJECT_ROOT / ".github" / "dependabot.yml"
        if not dependabot.is_file():
            pytest.skip("dependabot.yml does not exist yet")

        content = dependabot.read_text()
        required_ecosystems = ["pip", "npm", "github-actions"]
        for ecosystem in required_ecosystems:
            assert (
                ecosystem in content
            ), f"dependabot.yml missing ecosystem: {ecosystem}"
