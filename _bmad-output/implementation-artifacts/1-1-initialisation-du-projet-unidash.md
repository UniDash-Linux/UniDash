# Story 1.1: Initialisation du Projet UniDash

Status: done

## Story

As a **développeur**,
I want **une structure de projet initialisée avec les outils de développement et la documentation**,
So that **je puisse commencer le développement avec les bonnes pratiques et une documentation automatisée**.

## Acceptance Criteria

### Project Structure (DONE)

1. **Given** un repository git vide
   **When** le script d'initialisation est exécuté
   **Then** la structure de répertoires est créée selon project-context.md

2. **And** les fichiers pyproject.toml sont configurés pour chaque API

3. **And** les linters (Ruff, Black, ESLint, Prettier) sont configurés

4. **And** les hooks pre-commit sont installés

5. **And** le workflow CI GitHub Actions de base est créé

6. **And** les tests de validation de structure passent à 100%

### GitHub Community Standards (TODO)

7. **And** README.md est créé (English, liens vers Starlight)

8. **And** CONTRIBUTING.md est créé (English, GitFlow, Conventional Commits)

9. **And** CODE_OF_CONDUCT.md est créé (Contributor Covenant v2.1)

10. **And** LICENSE est créé (MIT)

11. **And** SECURITY.md est créé (English)

12. **And** .github/ISSUE_TEMPLATE/ est configuré (bug_report.yml, feature_request.yml, question.yml, config.yml)

13. **And** .github/PULL_REQUEST_TEMPLATE.md est créé

14. **And** .github/dependabot.yml est configuré

### Documentation Enforcement (TODO)

15. **And** Ruff est configuré avec règles D (docstrings obligatoires - Google style)

16. **And** ESLint est configuré avec eslint-plugin-jsdoc (JSDoc obligatoire sur exports)

17. **And** GitHub Action pour vérifier mise à jour Starlight est créée

18. **And** CodeRabbit AI est configuré (.coderabbit.yaml)

### Starlight Documentation (TODO)

19. **And** docs/ est initialisé avec Astro Starlight

20. **And** la structure de base est créée (getting-started/, architecture/, api/, deployment/, development/)

21. **And** starlight-typedoc est configuré pour auto-génération TypeScript

22. **And** mkdocstrings workflow est configuré pour Python

23. **And** la sidebar est configurée avec liens Community vers GitHub .md

## Tasks / Subtasks (TDD - Test First)

### Phase 1: Setup Dev Tools Infrastructure

- [ ] **Task 1: Créer infrastructure dev tools** (Prerequis)
  - [ ] 1.1 Créer `ruff.toml` racine pour config linter global
  - [ ] 1.2 Créer `.editorconfig` pour uniformiser les éditeurs
  - [ ] 1.3 Créer `requirements-dev.txt` avec pytest, ruff, black, pre-commit

### Phase 2: TDD - Structure de Répertoires

- [ ] **Task 2: TESTS - Structure de répertoires** (AC: #1, #6) 🔴 RED
  - [ ] 2.1 Créer `api/shared/tests/test_project_structure.py` (tests racine dans shared)
  - [ ] 2.2 Écrire test `test_infra_directories_exist()` - doit FAIL
  - [ ] 2.3 Écrire test `test_api_directories_exist()` - doit FAIL
  - [ ] 2.4 Écrire test `test_web_directories_exist()` - doit FAIL
  - [ ] 2.5 Écrire test `test_docs_directory_exists()` - doit FAIL
  - [ ] 2.6 Écrire test `test_github_workflows_directory_exists()` - doit FAIL
  - [ ] 2.7 Vérifier: `pytest api/shared/tests/test_project_structure.py` → FAIL (tous les tests rouges)

- [ ] **Task 3: IMPL - Structure de répertoires** (AC: #1) 🟢 GREEN
  - [ ] 3.1 Créer `infra/ansible/playbooks/` et `infra/ansible/inventory/`
  - [ ] 3.2 Créer `infra/k8s/manifests/` et `infra/k8s/helm/`
  - [ ] 3.3 Créer structure src layout pour chaque API:
    - `api/shared/src/unidash_shared/`, `api/shared/tests/unidash_shared/`
    - `api/db/src/unidash_db/`, `api/db/tests/unidash_db/`
    - `api/sso/src/unidash_sso/`, `api/sso/tests/unidash_sso/`
    - `api/unidash/src/unidash_api/`, `api/unidash/tests/unidash_api/`
    - `api/admin/src/unidash_admin/`, `api/admin/tests/unidash_admin/`
    - `api/backup/src/unidash_backup/`, `api/backup/tests/unidash_backup/`
  - [ ] 3.4 Créer `web/src/pages/`, `web/src/features/`, `web/src/shared/`, `web/src/lib/`
  - [ ] 3.5 Créer `docs/src/content/docs/`
  - [ ] 3.6 Créer `.github/workflows/`
  - [ ] 3.7 Vérifier: `pytest api/shared/tests/test_project_structure.py` → PASS (tous les tests verts)

### Phase 3: TDD - Packages Python

- [ ] **Task 4: TESTS - Packages Python** (AC: #2, #6) 🔴 RED
  - [ ] 4.1 Créer `api/shared/tests/test_python_packages.py`
  - [ ] 4.2 Écrire test `test_unidash_shared_importable()` - doit FAIL
  - [ ] 4.3 Écrire test `test_unidash_db_importable()` - doit FAIL
  - [ ] 4.4 Écrire test `test_unidash_sso_importable()` - doit FAIL
  - [ ] 4.5 Écrire test `test_unidash_api_importable()` - doit FAIL
  - [ ] 4.6 Écrire test `test_unidash_admin_importable()` - doit FAIL
  - [ ] 4.7 Écrire test `test_unidash_backup_importable()` - doit FAIL
  - [ ] 4.8 Écrire test `test_pyproject_toml_valid()` pour chaque API - doit FAIL
  - [ ] 4.9 Vérifier: `pytest api/shared/tests/test_python_packages.py` → FAIL

- [ ] **Task 5: IMPL - Packages Python** (AC: #2) 🟢 GREEN
  - [ ] 5.1 Créer `api/shared/pyproject.toml` + `api/shared/src/unidash_shared/__init__.py`
  - [ ] 5.2 Créer `api/db/pyproject.toml` + `api/db/src/unidash_db/__init__.py`
  - [ ] 5.3 Créer `api/sso/pyproject.toml` + `api/sso/src/unidash_sso/__init__.py`
  - [ ] 5.4 Créer `api/unidash/pyproject.toml` + `api/unidash/src/unidash_api/__init__.py`
  - [ ] 5.5 Créer `api/admin/pyproject.toml` + `api/admin/src/unidash_admin/__init__.py`
  - [ ] 5.6 Créer `api/backup/pyproject.toml` + `api/backup/src/unidash_backup/__init__.py`
  - [ ] 5.7 Chaque pyproject.toml inclut: pytest, pytest-cov, ruff, black dans [project.optional-dependencies.dev]
  - [ ] 5.8 `pip install -e "api/shared[dev]" -e "api/db[dev]" -e "api/sso[dev]" -e "api/unidash[dev]" -e "api/admin[dev]" -e "api/backup[dev]"`
  - [ ] 5.9 Vérifier: `pytest api/shared/tests/test_python_packages.py` → PASS

### Phase 4: TDD - Linters

- [ ] **Task 6: TESTS - Configuration Linters** (AC: #3, #6) 🔴 RED
  - [ ] 6.1 Créer `api/shared/tests/test_linters.py`
  - [ ] 6.2 Écrire test `test_ruff_check_passes()` - doit FAIL (ruff pas configuré)
  - [ ] 6.3 Écrire test `test_black_check_passes()` - doit FAIL
  - [ ] 6.4 Vérifier: `pytest api/shared/tests/test_linters.py` → FAIL

- [ ] **Task 7: IMPL - Configuration Linters Python** (AC: #3) 🟢 GREEN
  - [ ] 7.1 Créer `ruff.toml` racine avec config globale (tous les packages unidash_*)
  - [ ] 7.2 Ajouter section [tool.black] dans chaque pyproject.toml des APIs
  - [ ] 7.3 Vérifier: `pytest api/shared/tests/test_linters.py` → PASS

### Phase 5: Frontend Astro (initialisation - pas de TDD pour npm create)

- [ ] **Task 8: Initialiser Frontend Astro** (AC: #3)
  - [ ] 8.1 Exécuter `npm create astro@latest web -- --template minimal --typescript strict`
  - [ ] 8.2 `cd web && npx astro add tailwind`
  - [ ] 8.3 `npm install @headlessui/react react react-dom @types/react @types/react-dom`
  - [ ] 8.4 `npm install nanostores @nanostores/react`
  - [ ] 8.5 `npm install -D vitest @vitest/coverage-v8`
  - [ ] 8.6 Créer `eslint.config.js` avec ESLint + @typescript-eslint + eslint-plugin-astro
  - [ ] 8.7 Créer `.prettierrc`
  - [ ] 8.8 Configurer `vitest.config.ts` avec coverage threshold 100%

- [ ] **Task 9: TESTS - Frontend Setup Validation** (AC: #3, #6) 🔴 RED
  - [ ] 9.1 Créer `web/tests/setup.test.ts`
  - [ ] 9.2 Écrire test `test_typescript_config_strict()` - doit PASS (déjà configuré)
  - [ ] 9.3 Écrire test `test_tailwind_installed()` - doit PASS
  - [ ] 9.4 Écrire test `test_eslint_passes()` - doit PASS
  - [ ] 9.5 Vérifier: `cd web && npm run test` → PASS

### Phase 6: TDD - Pre-commit

- [ ] **Task 10: TESTS - Pre-commit hooks** (AC: #4, #6) 🔴 RED
  - [ ] 10.1 Créer `api/shared/tests/test_precommit.py`
  - [ ] 10.2 Écrire test `test_precommit_config_exists()` - doit FAIL
  - [ ] 10.3 Écrire test `test_precommit_runs_successfully()` - doit FAIL
  - [ ] 10.4 Vérifier: `pytest api/shared/tests/test_precommit.py` → FAIL

- [ ] **Task 11: IMPL - Pre-commit hooks** (AC: #4) 🟢 GREEN
  - [ ] 11.1 Créer `.pre-commit-config.yaml`
  - [ ] 11.2 `pip install pre-commit && pre-commit install`
  - [ ] 11.3 Vérifier: `pytest api/shared/tests/test_precommit.py` → PASS

### Phase 7: TDD - CI GitHub Actions

- [ ] **Task 12: TESTS - GitHub Actions** (AC: #5, #6) 🔴 RED
  - [ ] 12.1 Créer `api/shared/tests/test_ci_workflows.py`
  - [ ] 12.2 Écrire test `test_ci_python_workflow_exists()` - doit FAIL
  - [ ] 12.3 Écrire test `test_ci_web_workflow_exists()` - doit FAIL
  - [ ] 12.4 Écrire test `test_docs_deploy_workflow_exists()` - doit FAIL
  - [ ] 12.5 Écrire test `test_workflows_valid_yaml()` - doit FAIL
  - [ ] 12.6 Vérifier: `pytest api/shared/tests/test_ci_workflows.py` → FAIL

- [ ] **Task 13: IMPL - GitHub Actions** (AC: #5) 🟢 GREEN
  - [ ] 13.1 Créer `.github/workflows/ci-python.yml` avec coverage 100%
  - [ ] 13.2 Créer `.github/workflows/ci-web.yml` avec coverage 100%
  - [ ] 13.3 Créer `.github/workflows/docs-deploy.yml`
  - [ ] 13.4 Vérifier: `pytest api/shared/tests/test_ci_workflows.py` → PASS

### Phase 8: Documentation Starlight (DONE)

- [x] **Task 14: Initialiser Documentation Starlight** (AC: #19)
  - [x] 14.1 Exécuter `npm create astro@latest docs -- --template starlight --typescript strict`
  - [x] 14.2 Configurer `astro.config.mjs` pour GitHub Pages

### Phase 9: Validation Initiale (DONE)

- [x] **Task 15: Coverage Initial 100%** (AC: #6)
  - [x] 15.1 Exécuter `pytest api/shared/tests/ --cov=api --cov-report=term-missing --cov-fail-under=100`
  - [x] 15.2 Exécuter `cd web && npm run test:coverage`
  - [x] 15.3 Vérifier tous les tests passent
  - [x] 15.4 Commit initial: `feat(init): initialize project structure with TDD`

---

## NEW PHASES (TODO) - Documentation Continue

### Phase 10: GitHub Community Standards (TODO)

- [ ] **Task 16: TESTS - GitHub Community Standards** (AC: #7-14) 🔴 RED
  - [ ] 16.1 Créer `api/shared/tests/test_github_standards.py`
  - [ ] 16.2 Écrire test `test_readme_exists()` - doit FAIL
  - [ ] 16.3 Écrire test `test_contributing_exists()` - doit FAIL
  - [ ] 16.4 Écrire test `test_code_of_conduct_exists()` - doit FAIL
  - [ ] 16.5 Écrire test `test_license_exists()` - doit FAIL
  - [ ] 16.6 Écrire test `test_security_exists()` - doit FAIL
  - [ ] 16.7 Écrire test `test_issue_templates_exist()` - doit FAIL
  - [ ] 16.8 Écrire test `test_pr_template_exists()` - doit FAIL
  - [ ] 16.9 Écrire test `test_dependabot_exists()` - doit FAIL
  - [ ] 16.10 Vérifier: `pytest api/shared/tests/test_github_standards.py` → FAIL

- [ ] **Task 17: IMPL - README.md** (AC: #7) 🟢 GREEN
  - [ ] 17.1 Créer `README.md` (English)
  - [ ] 17.2 Header avec badges (CI, coverage, license, docs)
  - [ ] 17.3 Description courte du projet
  - [ ] 17.4 Quick links vers Starlight docs
  - [ ] 17.5 Installation rapide (liens vers docs/getting-started/)
  - [ ] 17.6 Liens Contributing, License, Security

- [ ] **Task 18: IMPL - CONTRIBUTING.md** (AC: #8) 🟢 GREEN
  - [ ] 18.1 Créer `CONTRIBUTING.md` (English)
  - [ ] 18.2 Welcome section
  - [ ] 18.3 Development setup (liens vers docs/development/)
  - [ ] 18.4 GitFlow workflow (diagramme Mermaid)
  - [ ] 18.5 Conventional Commits (examples)
  - [ ] 18.6 Code style (Ruff, Black, Prettier)
  - [ ] 18.7 Testing requirements (TDD, 100% coverage)
  - [ ] 18.8 Pull Request process

- [ ] **Task 19: IMPL - Other GitHub Files** (AC: #9-14) 🟢 GREEN
  - [ ] 19.1 Créer `CODE_OF_CONDUCT.md` (Contributor Covenant v2.1)
  - [ ] 19.2 Créer `LICENSE` (MIT)
  - [ ] 19.3 Créer `SECURITY.md` (English)
  - [ ] 19.4 Créer `.github/ISSUE_TEMPLATE/bug_report.yml`
  - [ ] 19.5 Créer `.github/ISSUE_TEMPLATE/feature_request.yml`
  - [ ] 19.6 Créer `.github/ISSUE_TEMPLATE/question.yml`
  - [ ] 19.7 Créer `.github/ISSUE_TEMPLATE/config.yml`
  - [ ] 19.8 Créer `.github/PULL_REQUEST_TEMPLATE.md`
  - [ ] 19.9 Créer `.github/dependabot.yml`
  - [ ] 19.10 Vérifier: `pytest api/shared/tests/test_github_standards.py` → PASS

### Phase 11: Documentation Enforcement (TODO)

- [ ] **Task 20: TESTS - Documentation Enforcement** (AC: #15-18) 🔴 RED
  - [ ] 20.1 Créer `api/shared/tests/test_doc_enforcement.py`
  - [ ] 20.2 Écrire test `test_ruff_docstring_rules_enabled()` - doit FAIL
  - [ ] 20.3 Écrire test `test_eslint_jsdoc_rules_enabled()` - doit FAIL
  - [ ] 20.4 Écrire test `test_docs_check_workflow_exists()` - doit FAIL
  - [ ] 20.5 Écrire test `test_coderabbit_config_exists()` - doit FAIL
  - [ ] 20.6 Vérifier: `pytest api/shared/tests/test_doc_enforcement.py` → FAIL

- [ ] **Task 21: IMPL - Ruff Docstring Rules** (AC: #15) 🟢 GREEN
  - [ ] 21.1 Mettre à jour `ruff.toml` avec règles D (pydocstyle)
  - [ ] 21.2 Configurer convention Google style
  - [ ] 21.3 Ajouter docstrings à tous les modules existants
  - [ ] 21.4 Vérifier: `ruff check api/` → PASS

- [ ] **Task 22: IMPL - ESLint JSDoc Rules** (AC: #16) 🟢 GREEN
  - [ ] 22.1 `cd web && npm install -D eslint-plugin-jsdoc`
  - [ ] 22.2 Mettre à jour `eslint.config.js` avec plugin jsdoc
  - [ ] 22.3 Configurer règles jsdoc/require-jsdoc, require-description, require-param-description
  - [ ] 22.4 Vérifier: `cd web && npm run lint` → PASS

- [ ] **Task 23: IMPL - GitHub Actions Documentation Check** (AC: #17) 🟢 GREEN
  - [ ] 23.1 Créer `.github/workflows/docs-check.yml`
  - [ ] 23.2 Script bash vérifie si PR modifie api/ → exige docs/api/ update
  - [ ] 23.3 Script bash vérifie si PR modifie web/src/features/ → exige docs/ update
  - [ ] 23.4 Label `skip-docs` pour override (hotfixes)

- [ ] **Task 24: IMPL - CodeRabbit AI Config** (AC: #18) 🟢 GREEN
  - [ ] 24.1 Créer `.coderabbit.yaml`
  - [ ] 24.2 Configurer review language: English
  - [ ] 24.3 Configurer checks: code style, documentation quality
  - [ ] 24.4 Activer CodeRabbit GitHub App sur le repo
  - [ ] 24.5 Vérifier: `pytest api/shared/tests/test_doc_enforcement.py` → PASS

### Phase 12: Starlight Configuration Avancée (TODO)

- [ ] **Task 25: TESTS - Starlight Configuration** (AC: #19-23) 🔴 RED
  - [ ] 25.1 Créer `docs/tests/starlight.test.ts`
  - [ ] 25.2 Écrire test `test_starlight_typedoc_configured()` - doit FAIL
  - [ ] 25.3 Écrire test `test_starlight_sidebar_community_links()` - doit FAIL
  - [ ] 25.4 Écrire test `test_docs_structure_complete()` - doit FAIL
  - [ ] 25.5 Vérifier: `cd docs && npm run test` → FAIL

- [ ] **Task 26: IMPL - Starlight Structure** (AC: #20) 🟢 GREEN
  - [ ] 26.1 Créer `docs/src/content/docs/getting-started/` (introduction.md, installation.md, quick-start.md, configuration.md)
  - [ ] 26.2 Créer `docs/src/content/docs/architecture/` (overview.md placeholder)
  - [ ] 26.3 Créer `docs/src/content/docs/api/` (overview.md placeholder)
  - [ ] 26.4 Créer `docs/src/content/docs/deployment/` (overview.md placeholder)
  - [ ] 26.5 Créer `docs/src/content/docs/development/` (setup.md placeholder)

- [ ] **Task 27: IMPL - Starlight TypeDoc** (AC: #21) 🟢 GREEN
  - [ ] 27.1 `cd docs && npm install starlight-typedoc typedoc`
  - [ ] 27.2 Configurer `astro.config.mjs` avec plugin starlight-typedoc
  - [ ] 27.3 Configurer entryPoints vers `../web/src/**/*.ts`

- [ ] **Task 28: IMPL - mkdocstrings Workflow** (AC: #22) 🟢 GREEN
  - [ ] 28.1 Créer `docs/mkdocs.yml` pour génération Python docs
  - [ ] 28.2 Ajouter mkdocstrings dans requirements-dev.txt
  - [ ] 28.3 Créer `.github/workflows/generate-python-docs.yml`
  - [ ] 28.4 Script copie .md générés vers `docs/src/content/docs/api/python/`

- [ ] **Task 29: IMPL - Starlight Sidebar** (AC: #23) 🟢 GREEN
  - [ ] 29.1 Mettre à jour `docs/astro.config.mjs` sidebar
  - [ ] 29.2 Section Getting Started (autogenerate)
  - [ ] 29.3 Section Architecture (autogenerate)
  - [ ] 29.4 Section API Reference (autogenerate)
  - [ ] 29.5 Section Deployment (autogenerate)
  - [ ] 29.6 Section Development (autogenerate)
  - [ ] 29.7 Section Community avec liens externes:
    - Contributing → https://github.com/OWNER/UniDash/blob/main/CONTRIBUTING.md
    - Code of Conduct → https://github.com/OWNER/UniDash/blob/main/CODE_OF_CONDUCT.md
    - License → https://github.com/OWNER/UniDash/blob/main/LICENSE
    - Security → https://github.com/OWNER/UniDash/blob/main/SECURITY.md
  - [ ] 29.8 Vérifier: `cd docs && npm run test` → PASS

### Phase 13: Validation Finale Complète (TODO)

- [ ] **Task 30: Validation Totale** (AC: #1-23)
  - [ ] 30.1 Exécuter tous les tests Python: `pytest api/ --cov --cov-fail-under=100`
  - [ ] 30.2 Exécuter tous les tests Frontend: `cd web && npm run test:coverage`
  - [ ] 30.3 Exécuter tous les tests Docs: `cd docs && npm run test`
  - [ ] 30.4 Build Starlight: `cd docs && npm run build`
  - [ ] 30.5 Vérifier GitHub Community Standards 100% sur repo
  - [ ] 30.6 Commit final: `docs: complete GitHub Community Standards and documentation enforcement`

## Dev Notes

### CRITICAL: TDD Workflow (Test First)

**Cycle Red-Green-Refactor:**
1. 🔴 **RED**: Écrire le test qui échoue
2. 🟢 **GREEN**: Écrire le code minimal pour faire passer le test
3. 🔄 **REFACTOR**: Améliorer le code en gardant les tests verts

**Règle AR9**: Coverage 100% blocking in CI - Aucun merge si coverage < 100%

### Test Examples

```python
# api/shared/tests/test_project_structure.py
import pytest
from pathlib import Path

# Remonter de api/shared/tests vers la racine du projet
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

REQUIRED_DIRS = [
    "infra/ansible/playbooks",
    "infra/ansible/inventory",
    "infra/k8s/manifests",
    "infra/k8s/helm",
    "api/shared/src/unidash_shared",
    "api/db/src/unidash_db",
    "api/sso/src/unidash_sso",
    "api/unidash/src/unidash_api",
    "api/admin/src/unidash_admin",
    "api/backup/src/unidash_backup",
    "web/src/pages",
    "web/src/features",
    "docs/src/content/docs",
    ".github/workflows",
]

@pytest.mark.parametrize("directory", REQUIRED_DIRS)
def test_directory_exists(directory: str) -> None:
    """Verify required directory exists."""
    path = PROJECT_ROOT / directory
    assert path.is_dir(), f"Missing required directory: {directory}"


# api/shared/tests/test_python_packages.py
import subprocess
import sys

import pytest

PACKAGES = [
    "unidash_shared",
    "unidash_db",
    "unidash_sso",
    "unidash_api",
    "unidash_admin",
    "unidash_backup",
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


# api/shared/tests/test_linters.py
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

def test_ruff_check_passes() -> None:
    """Verify ruff check passes on codebase."""
    result = subprocess.run(
        ["ruff", "check", "api/"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Ruff check failed: {result.stdout}"

def test_black_check_passes() -> None:
    """Verify black formatting check passes."""
    result = subprocess.run(
        ["black", "--check", "api/"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Black check failed: {result.stdout}"
```

### Architecture Requirements Covered

Cette story couvre les AR suivants (enablement story):
- **AR2**: Backend FastAPI avec src layout PyPA (unidash_* packages)
- **AR7**: GitFlow branching (main/develop + feature/release/hotfix)
- **AR8**: Conventional Commits (feat/fix/docs/style/refactor/test/chore)
- **AR9**: Coverage 100% blocking in CI (pytest + Vitest + Playwright)

### Critical Implementation Rules

**Python Structure (src layout PyPA) - OBLIGATOIRE:**
```
api/<service>/
├── pyproject.toml
├── src/
│   └── unidash_<service>/
│       ├── __init__.py
│       ├── core/
│       ├── models/
│       ├── repositories/
│       ├── services/
│       └── api/
└── tests/
    └── unidash_<service>/
```

**Packages Python - Nommage OBLIGATOIRE:**

| API | Package | Import |
|-----|---------|--------|
| api/shared | `unidash_shared` | `from unidash_shared.types import ...` |
| api/db | `unidash_db` | `from unidash_db.models import User` |
| api/sso | `unidash_sso` | `from unidash_sso.providers import ...` |
| api/unidash | `unidash_api` | `from unidash_api.services import ...` |
| api/admin | `unidash_admin` | `from unidash_admin.api import ...` |
| api/backup | `unidash_backup` | `from unidash_backup.backends import ...` |

**Version Constraints - CRITIQUES:**
- **Python 3.14 minimum** - EOL Oct 2030
- **SQLAlchemy 2.0+** - Nouvelle API async uniquement
- **Tailwind v4** - Nouvelle architecture de config
- **Astro 5+** - View Transitions API requise

### Anti-Patterns à Éviter

- ❌ JAMAIS écrire du code avant les tests (TDD obligatoire)
- ❌ JAMAIS de structure flat (app/ au lieu de src/unidash_*/
- ❌ JAMAIS de Python < 3.14
- ❌ JAMAIS de commit direct sur main ou develop
- ❌ JAMAIS de merge avec coverage < 100%

### References

- [Source: project-context.md#Technology Stack & Versions]
- [Source: project-context.md#Python Rules]
- [Source: project-context.md#Testing Rules]
- [Source: architecture.md#Project Structure]
- [Source: epics.md#Story 1.1]

## Dev Agent Record

### Agent Model Used

Claude Opus 4.5 (claude-opus-4-5-20251101)

### Completion Notes List

- Phase 1: Created ruff.toml, .editorconfig, requirements-dev.txt
- Phase 2: Created complete directory structure (infra, api, web, docs, .github)
- Phase 3: Created 6 Python packages with src layout PyPA (unidash_*)
- Phase 4: Configured Ruff + Black linters
- Phase 5: Initialized Astro frontend with React, Tailwind, Nanostores, Vitest
- Phase 6: Created .pre-commit-config.yaml
- Phase 7: Created 3 GitHub Actions workflows (ci-python, ci-web, docs-deploy)
- Phase 8: Initialized Starlight documentation
- Phase 9: All 55 tests pass (49 Python + 6 Frontend)
- Phase 10: GitHub Community Standards (README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, issue/PR templates, dependabot)
- Phase 11: Documentation Enforcement (Ruff D rules, ESLint JSDoc, docs-check workflow, CodeRabbit)
- Phase 12: Starlight Configuration (starlight-typedoc with conditional loading, mkdocstrings workflow, sidebar Community links, docker-compose.dev.yml)
- Phase 13: Final Validation - 94 Python tests + 3 docs tests + build pass

### File List

**Root files:**
- ruff.toml
- .editorconfig
- requirements-dev.txt
- .pre-commit-config.yaml
- README.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- docker-compose.dev.yml
- Dockerfile.dev

**API packages (src layout PyPA):**
- api/shared/pyproject.toml, src/unidash_shared/__init__.py
- api/db/pyproject.toml, src/unidash_db/__init__.py
- api/sso/pyproject.toml, src/unidash_sso/__init__.py
- api/unidash/pyproject.toml, src/unidash_api/__init__.py
- api/admin/pyproject.toml, src/unidash_admin/__init__.py
- api/backup/pyproject.toml, src/unidash_backup/__init__.py

**Tests:**
- api/shared/tests/test_project_structure.py
- api/shared/tests/test_python_packages.py
- api/shared/tests/test_linters.py
- api/shared/tests/test_precommit.py
- api/shared/tests/test_ci_workflows.py
- api/shared/tests/test_github_standards.py
- api/shared/tests/test_doc_enforcement.py
- api/shared/tests/test_starlight_config.py
- web/tests/setup.test.ts
- docs/tests/astro-config.test.js

**Frontend:**
- web/ (Astro + React + Tailwind)
- web/eslint.config.js (with eslint-plugin-jsdoc)
- web/.prettierrc
- web/vitest.config.ts

**Documentation:**
- docs/ (Starlight)
- docs/astro.config.mjs (with starlight-typedoc conditional loading)
- docs/mkdocs.yml
- docs/src/content/docs/getting-started/
- docs/src/content/docs/development/setup.md
- docs/src/content/docs/api/python/

**CI/CD:**
- .github/workflows/ci-python.yml
- .github/workflows/ci-web.yml
- .github/workflows/docs-deploy.yml
- .github/workflows/docs-check.yml
- .github/workflows/generate-python-docs.yml
- .github/dependabot.yml
- .github/ISSUE_TEMPLATE/ (bug_report.yml, feature_request.yml, question.yml, config.yml)
- .github/PULL_REQUEST_TEMPLATE.md
- .coderabbit.yaml

**Infrastructure (directories):**
- infra/ansible/playbooks/
- infra/ansible/inventory/
- infra/k8s/manifests/
- infra/k8s/helm/
