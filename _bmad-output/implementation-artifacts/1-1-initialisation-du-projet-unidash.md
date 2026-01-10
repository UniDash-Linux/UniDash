# Story 1.1: Initialisation du Projet UniDash

Status: ready-for-dev

## Story

As a **développeur**,
I want **une structure de projet initialisée avec les outils de développement**,
So that **je puisse commencer le développement avec les bonnes pratiques**.

## Acceptance Criteria

1. **Given** un repository git vide
   **When** le script d'initialisation est exécuté
   **Then** la structure de répertoires est créée selon project-context.md

2. **And** les fichiers pyproject.toml sont configurés pour chaque API

3. **And** les linters (Ruff, Black, ESLint, Prettier) sont configurés

4. **And** les hooks pre-commit sont installés

5. **And** le workflow CI GitHub Actions de base est créé

6. **And** les tests de validation de structure passent à 100%

## Tasks / Subtasks (TDD - Test First)

### Phase 1: Setup Test Infrastructure

- [ ] **Task 1: Créer infrastructure de tests** (Prerequis)
  - [ ] 1.1 Créer `pyproject.toml` racine minimal avec pytest + pytest-cov
  - [ ] 1.2 Créer dossier `tests/` à la racine
  - [ ] 1.3 Créer `tests/conftest.py` avec fixtures de base

### Phase 2: TDD - Structure de Répertoires

- [ ] **Task 2: TESTS - Structure de répertoires** (AC: #1, #6) 🔴 RED
  - [ ] 2.1 Créer `tests/test_project_structure.py`
  - [ ] 2.2 Écrire test `test_infra_directories_exist()` - doit FAIL
  - [ ] 2.3 Écrire test `test_api_directories_exist()` - doit FAIL
  - [ ] 2.4 Écrire test `test_web_directories_exist()` - doit FAIL
  - [ ] 2.5 Écrire test `test_docs_directory_exists()` - doit FAIL
  - [ ] 2.6 Écrire test `test_github_workflows_directory_exists()` - doit FAIL
  - [ ] 2.7 Vérifier: `pytest tests/test_project_structure.py` → FAIL (tous les tests rouges)

- [ ] **Task 3: IMPL - Structure de répertoires** (AC: #1) 🟢 GREEN
  - [ ] 3.1 Créer `infra/ansible/playbooks/` et `infra/ansible/inventory/`
  - [ ] 3.2 Créer `infra/k8s/manifests/` et `infra/k8s/helm/`
  - [ ] 3.3 Créer `api/shared/`, `api/db/`, `api/sso/`, `api/unidash/`, `api/admin/`, `api/backup/`
  - [ ] 3.4 Créer `web/src/pages/`, `web/src/features/`, `web/src/shared/`, `web/src/lib/`
  - [ ] 3.5 Créer `docs/src/content/docs/`
  - [ ] 3.6 Créer `.github/workflows/`
  - [ ] 3.7 Vérifier: `pytest tests/test_project_structure.py` → PASS (tous les tests verts)

### Phase 3: TDD - Packages Python

- [ ] **Task 4: TESTS - Packages Python** (AC: #2, #6) 🔴 RED
  - [ ] 4.1 Créer `tests/test_python_packages.py`
  - [ ] 4.2 Écrire test `test_unidash_shared_importable()` - doit FAIL
  - [ ] 4.3 Écrire test `test_unidash_db_importable()` - doit FAIL
  - [ ] 4.4 Écrire test `test_unidash_sso_importable()` - doit FAIL
  - [ ] 4.5 Écrire test `test_unidash_api_importable()` - doit FAIL
  - [ ] 4.6 Écrire test `test_unidash_admin_importable()` - doit FAIL
  - [ ] 4.7 Écrire test `test_unidash_backup_importable()` - doit FAIL
  - [ ] 4.8 Écrire test `test_pyproject_toml_valid()` pour chaque API - doit FAIL
  - [ ] 4.9 Vérifier: `pytest tests/test_python_packages.py` → FAIL

- [ ] **Task 5: IMPL - Packages Python** (AC: #2) 🟢 GREEN
  - [ ] 5.1 Créer `api/shared/pyproject.toml` + `src/unidash_shared/__init__.py`
  - [ ] 5.2 Créer `api/db/pyproject.toml` + `src/unidash_db/__init__.py`
  - [ ] 5.3 Créer `api/sso/pyproject.toml` + `src/unidash_sso/__init__.py`
  - [ ] 5.4 Créer `api/unidash/pyproject.toml` + `src/unidash_api/__init__.py`
  - [ ] 5.5 Créer `api/admin/pyproject.toml` + `src/unidash_admin/__init__.py`
  - [ ] 5.6 Créer `api/backup/pyproject.toml` + `src/unidash_backup/__init__.py`
  - [ ] 5.7 Créer structure src layout PyPA complète pour chaque API
  - [ ] 5.8 `pip install -e api/shared api/db api/sso api/unidash api/admin api/backup`
  - [ ] 5.9 Vérifier: `pytest tests/test_python_packages.py` → PASS

### Phase 4: TDD - Linters

- [ ] **Task 6: TESTS - Configuration Linters** (AC: #3, #6) 🔴 RED
  - [ ] 6.1 Créer `tests/test_linters.py`
  - [ ] 6.2 Écrire test `test_ruff_check_passes()` - doit FAIL (ruff pas configuré)
  - [ ] 6.3 Écrire test `test_black_check_passes()` - doit FAIL
  - [ ] 6.4 Vérifier: `pytest tests/test_linters.py` → FAIL

- [ ] **Task 7: IMPL - Configuration Linters Python** (AC: #3) 🟢 GREEN
  - [ ] 7.1 Ajouter config Ruff dans `pyproject.toml` racine
  - [ ] 7.2 Ajouter config Black dans `pyproject.toml` racine
  - [ ] 7.3 Vérifier: `pytest tests/test_linters.py` → PASS

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
  - [ ] 10.1 Ajouter `tests/test_precommit.py`
  - [ ] 10.2 Écrire test `test_precommit_config_exists()` - doit FAIL
  - [ ] 10.3 Écrire test `test_precommit_runs_successfully()` - doit FAIL
  - [ ] 10.4 Vérifier: `pytest tests/test_precommit.py` → FAIL

- [ ] **Task 11: IMPL - Pre-commit hooks** (AC: #4) 🟢 GREEN
  - [ ] 11.1 Créer `.pre-commit-config.yaml`
  - [ ] 11.2 `pip install pre-commit && pre-commit install`
  - [ ] 11.3 Vérifier: `pytest tests/test_precommit.py` → PASS

### Phase 7: TDD - CI GitHub Actions

- [ ] **Task 12: TESTS - GitHub Actions** (AC: #5, #6) 🔴 RED
  - [ ] 12.1 Ajouter `tests/test_ci_workflows.py`
  - [ ] 12.2 Écrire test `test_ci_python_workflow_exists()` - doit FAIL
  - [ ] 12.3 Écrire test `test_ci_web_workflow_exists()` - doit FAIL
  - [ ] 12.4 Écrire test `test_docs_deploy_workflow_exists()` - doit FAIL
  - [ ] 12.5 Écrire test `test_workflows_valid_yaml()` - doit FAIL
  - [ ] 12.6 Vérifier: `pytest tests/test_ci_workflows.py` → FAIL

- [ ] **Task 13: IMPL - GitHub Actions** (AC: #5) 🟢 GREEN
  - [ ] 13.1 Créer `.github/workflows/ci-python.yml` avec coverage 100%
  - [ ] 13.2 Créer `.github/workflows/ci-web.yml` avec coverage 100%
  - [ ] 13.3 Créer `.github/workflows/docs-deploy.yml`
  - [ ] 13.4 Vérifier: `pytest tests/test_ci_workflows.py` → PASS

### Phase 8: Documentation Starlight

- [ ] **Task 14: Initialiser Documentation Starlight** (AC: #1)
  - [ ] 14.1 Exécuter `npm create astro@latest docs -- --template starlight --typescript strict`
  - [ ] 14.2 Configurer `astro.config.mjs` pour GitHub Pages

### Phase 9: Validation Finale

- [ ] **Task 15: Coverage Final 100%** (AC: #6)
  - [ ] 15.1 Exécuter `pytest --cov --cov-report=term-missing --cov-fail-under=100`
  - [ ] 15.2 Exécuter `cd web && npm run test:coverage`
  - [ ] 15.3 Vérifier tous les tests passent
  - [ ] 15.4 Commit initial: `feat(init): initialize project structure with TDD`

## Dev Notes

### CRITICAL: TDD Workflow (Test First)

**Cycle Red-Green-Refactor:**
1. 🔴 **RED**: Écrire le test qui échoue
2. 🟢 **GREEN**: Écrire le code minimal pour faire passer le test
3. 🔄 **REFACTOR**: Améliorer le code en gardant les tests verts

**Règle AR9**: Coverage 100% blocking in CI - Aucun merge si coverage < 100%

### Test Examples

```python
# tests/test_project_structure.py
import os
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

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


# tests/test_python_packages.py
import pytest
import subprocess
import sys

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


# tests/test_linters.py
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

def test_ruff_check_passes() -> None:
    """Verify ruff check passes on codebase."""
    result = subprocess.run(
        ["ruff", "check", "."],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Ruff check failed: {result.stdout}"

def test_black_check_passes() -> None:
    """Verify black formatting check passes."""
    result = subprocess.run(
        ["black", "--check", "."],
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

_To be filled by dev agent_

### Completion Notes List

_To be filled during implementation_

### File List

_To be filled during implementation_
