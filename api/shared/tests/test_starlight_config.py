"""Tests for Starlight documentation configuration.

Verifies that Starlight is properly configured with
structure, sidebar, and community links.
"""

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent


class TestStarlightStructure:
    """Test suite for Starlight documentation structure."""

    def test_docs_directory_exists(self) -> None:
        """Verify docs/ directory exists."""
        docs_dir = PROJECT_ROOT / "docs"
        assert docs_dir.is_dir(), "Missing required directory: docs/"

    def test_astro_config_exists(self) -> None:
        """Verify astro.config.mjs exists in docs."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        assert config.is_file(), "Missing required file: docs/astro.config.mjs"

    def test_getting_started_directory_exists(self) -> None:
        """Verify getting-started documentation section exists."""
        section = PROJECT_ROOT / "docs" / "src" / "content" / "docs" / "getting-started"
        assert section.is_dir(), "Missing docs section: getting-started/"

    def test_architecture_directory_exists(self) -> None:
        """Verify architecture documentation section exists."""
        section = PROJECT_ROOT / "docs" / "src" / "content" / "docs" / "architecture"
        assert section.is_dir(), "Missing docs section: architecture/"

    def test_api_directory_exists(self) -> None:
        """Verify API documentation section exists."""
        section = PROJECT_ROOT / "docs" / "src" / "content" / "docs" / "api"
        assert section.is_dir(), "Missing docs section: api/"

    def test_deployment_directory_exists(self) -> None:
        """Verify deployment documentation section exists."""
        section = PROJECT_ROOT / "docs" / "src" / "content" / "docs" / "deployment"
        assert section.is_dir(), "Missing docs section: deployment/"

    def test_development_directory_exists(self) -> None:
        """Verify development documentation section exists."""
        section = PROJECT_ROOT / "docs" / "src" / "content" / "docs" / "development"
        assert section.is_dir(), "Missing docs section: development/"


class TestStarlightSidebar:
    """Test suite for Starlight sidebar configuration."""

    def test_sidebar_has_getting_started(self) -> None:
        """Verify sidebar includes Getting Started section."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert (
            "Getting Started" in content
        ), "Sidebar should include Getting Started section"

    def test_sidebar_has_architecture(self) -> None:
        """Verify sidebar includes Architecture section."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert "Architecture" in content, "Sidebar should include Architecture section"

    def test_sidebar_has_api_reference(self) -> None:
        """Verify sidebar includes API Reference section."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert "API" in content, "Sidebar should include API Reference section"

    def test_sidebar_has_deployment(self) -> None:
        """Verify sidebar includes Deployment section."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert "Deployment" in content, "Sidebar should include Deployment section"

    def test_sidebar_has_development(self) -> None:
        """Verify sidebar includes Development section."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert "Development" in content, "Sidebar should include Development section"

    def test_sidebar_has_community_links(self) -> None:
        """Verify sidebar includes Community links section."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert "Community" in content, "Sidebar should include Community section"
        assert (
            "CONTRIBUTING" in content
        ), "Community section should link to CONTRIBUTING.md"


class TestTypeDocConfiguration:
    """Test suite for starlight-typedoc configuration."""

    def test_typedoc_plugin_installed(self) -> None:
        """Verify starlight-typedoc is in package.json dependencies."""
        package_json = PROJECT_ROOT / "docs" / "package.json"
        if not package_json.is_file():
            pytest.skip("package.json does not exist yet")

        import json

        data = json.loads(package_json.read_text())
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        assert "starlight-typedoc" in deps, "starlight-typedoc should be installed"

    def test_typedoc_config_points_to_web_src(self) -> None:
        """Verify TypeDoc config references web/src for TypeScript files."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert (
            "../web/src" in content
        ), "TypeDoc should reference ../web/src for TypeScript files"

    def test_typedoc_has_conditional_loading(self) -> None:
        """Verify TypeDoc plugin loads conditionally based on file existence."""
        config = PROJECT_ROOT / "docs" / "astro.config.mjs"
        if not config.is_file():
            pytest.skip("astro.config.mjs does not exist yet")

        content = config.read_text()
        assert (
            "hasTypeScriptFiles" in content
        ), "Should have hasTypeScriptFiles function for conditional loading"
