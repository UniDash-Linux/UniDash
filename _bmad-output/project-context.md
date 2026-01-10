---
project_name: 'UniDash'
user_name: 'Gabriel'
date: '2026-01-10'
sections_completed: ['technology_stack', 'language_rules', 'framework_rules', 'testing_rules', 'code_quality_rules', 'workflow_rules', 'critical_rules']
status: complete
existing_patterns_found: 12
---

# Project Context for AI Agents

_This file contains critical rules and patterns that AI agents must follow when implementing code in this project. Focus on unobvious details that agents might otherwise miss._

---

## Technology Stack & Versions

### Core Technologies

| Domain | Technology | Version | Notes |
|--------|------------|---------|-------|
| **Backend** | Python | 3.14 | EOL Oct 2030 - choix stratégique 5 ans |
| **API Framework** | FastAPI + Uvicorn | latest | Async native |
| **ORM** | SQLAlchemy 2.0 + Alembic | 2.0+ | Nouvelle API async |
| **Auth libs** | python-ldap, authlib | latest | AD/OIDC support |
| **Frontend** | Astro | 5.x | View Transitions API |
| **UI Framework** | React | 18+ | Islands architecture |
| **State Management** | Nanostores | latest | 1KB, Astro-native |
| **Data Fetching** | TanStack Query | v5+ | Cache, retry, JSON:API |
| **Animations** | CSS + Framer Motion | latest | Framer pour tiling/fenêtres |
| **Styling** | Tailwind CSS | v4 | Nouvelle architecture config |
| **UI Components** | Headless UI | latest | Accessible |
| **Database** | PostgreSQL (Patroni HA) | latest | 3 nœuds |
| **Cache** | Redis | latest | Sessions + cache |
| **Orchestration** | K3S | latest | 3 nœuds HA |
| **Reverse Proxy HTTP** | HAProxy | latest | Health checks natifs |
| **Reverse Proxy UDP** | Nginx (stream) | latest | HAProxy ne supporte pas UDP |
| **Documentation** | Astro Starlight | latest | GitHub Pages |
| **Infrastructure** | Ansible | latest | Playbooks K3S/VPN |
| **CI/CD** | GitHub Actions | - | Gratuit open source |
| **Monitoring** | Prometheus + Grafana + Loki | latest | Stack unifiée |
| **TLS K3S** | cert-manager | latest | Let's Encrypt auto |
| **TLS autres** | Certbot | latest | Proxmox, Docker, legacy |

### Critical Version Constraints

- **Python 3.14 minimum** - EOL Oct 2030, choix stratégique pour 5 ans de support
- **SQLAlchemy 2.0+** - Utiliser la nouvelle API async, pas l'ancienne API 1.x
- **Tailwind v4** - Nouvelle architecture de configuration (pas v3)
- **Astro 5+** - View Transitions API requise pour navigation fluide

## Critical Implementation Rules

### Language-Specific Rules

#### Python Rules

**Structure obligatoire (src layout PyPA) :**
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

**Packages Python :**

| API | Package | Import |
|-----|---------|--------|
| api/shared | `unidash_shared` | `from unidash_shared.types import ...` |
| api/db | `unidash_db` | `from unidash_db.models import User` |
| api/sso | `unidash_sso` | `from unidash_sso.providers import ...` |
| api/unidash | `unidash_api` | `from unidash_api.services import ...` |
| api/admin | `unidash_admin` | `from unidash_admin.api import ...` |
| api/backup | `unidash_backup` | `from unidash_backup.backends import ...` |

**Naming Python :**
- Fonctions : `snake_case` → `get_user_data()`
- Fichiers : `snake_case` → `user_service.py`
- Classes : `PascalCase` → `UserRepository`
- Packages : `snake_case` avec prefix → `unidash_db`

**Linting Python :** Ruff + Black

#### TypeScript/React Rules

**Structure frontend :**
```
web/src/
├── pages/           # Routing Astro (obligatoire)
├── features/        # Organisation par feature
│   ├── desktop/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── stores/
│   ├── store/
│   └── auth/
├── shared/          # Composants cross-feature
└── lib/             # Utilitaires purs
```

**Naming TypeScript :**
- Variables/fonctions : `camelCase` → `getUserData`, `userId`
- Composants React : `PascalCase` → `WindowManager.tsx`
- Nanostores : prefix `$` → `$userStore`, `$desktopState`
- Actions : `domain.verb` → `user.set`, `window.update`

**Linting TypeScript :** ESLint + Prettier + @typescript-eslint + eslint-plugin-astro

### Framework-Specific Rules

#### Astro Rules

**Architecture SPA-like Island (toutes les pages) :**
- Toutes les pages utilisent des islands React avec `client:load`
- Navigation fluide via View Transitions API (Astro 5)
- State partagé via Nanostores entre toutes les pages
- Pas de pages statiques pures - tout est interactif

**Routing :** File-based + View Transitions API (natif Astro 5)

#### React Rules (dans Astro)

**Hydration Strategy :**
- `client:load` pour tous les composants principaux (SPA-like)
- `client:visible` uniquement pour composants lourds hors viewport initial
- `client:idle` pour analytics/tracking non-critiques

**State Management Nanostores :**
```typescript
// Store definition
import { atom, map } from 'nanostores'
export const $desktopState = map<DesktopState>({...})

// Usage dans composant
import { useStore } from '@nanostores/react'
const desktop = useStore($desktopState)
```

#### FastAPI Rules

**Data Access Pattern :** Repository + Unit of Work (découplage, testabilité)

**Validation :**
- SQLAlchemy constraints (primary) - validation proche DB
- Pydantic (fallback) - validation entrée API

**Sessions :** Redis server-side (révocation immédiate, pas JWT)

#### TanStack Query Rules

**Usage standard :**
```typescript
const { data, isLoading, error } = useQuery({
  queryKey: ['users', userId],
  queryFn: () => api.users.get(userId)
})
```

**Retry :** Automatique (TanStack Query)
**Cache :** Géré par TanStack Query (per-query)

### Testing Rules

#### Test Structure

**Backend (pytest) :**
```
api/<service>/tests/
└── unidash_<service>/
    ├── unit/
    │   ├── test_models.py
    │   └── test_services.py
    └── integration/
        └── test_api.py
```

**Frontend (Vitest + Playwright) :**
```
web/tests/
├── features/
│   ├── desktop/
│   ├── store/
│   └── auth/
└── shared/
```

#### Coverage Requirements

- **Coverage : 100% blocking in CI** - Aucun merge si coverage < 100%
- Types de tests : Unit + Integration + E2E

#### Test Patterns

**Naming :**
- Fichiers Python : `test_<module>.py`
- Fichiers TypeScript : `<Component>.test.tsx`
- Fonctions : `test_<action>_<expected_result>()`

**Mocks :**
- Mocker dépendances externes (Redis, PostgreSQL) en unit tests
- Tests d'intégration avec containers (testcontainers ou docker-compose)

#### CI Integration

- pytest pour backend
- Vitest pour frontend unit tests
- Playwright pour E2E
- Tous bloquants si échec

### Code Quality & Style Rules

#### Database Naming

| Élément | Convention | Exemple |
|---------|------------|---------|
| Tables | snake_case pluriel | `users`, `app_instances` |
| Colonnes | snake_case | `user_id`, `created_at` |
| Foreign Keys | `fk_<column>` | `fk_user_id` |
| Index | `idx_<table>_<columns>` | `idx_users_email` |

#### API Naming

| Élément | Convention | Exemple |
|---------|------------|---------|
| Endpoints | pluriel | `/users`, `/apps` |
| Route params | `{param}` | `/users/{id}` |
| Query params | snake_case | `?user_id=1&sort_by=name` |

#### Format Patterns

| Élément | Convention |
|---------|------------|
| JSON field naming | snake_case |
| Dates | ISO 8601 (`2026-01-10T14:30:00Z`) |
| Null fields | Omettre (ne pas envoyer) |
| Empty arrays | `[]` (explicite) |
| Booleans | `true/false` |
| API Format | JSON:API |

#### Communication Patterns

| Domaine | Convention | Exemple |
|---------|------------|---------|
| Events | `domain.action` | `user.created` |
| Event payload | Flat | `{user_id, email}` |
| Actions | `domain.verb` | `user.set`, `window.update` |
| Logs | Structured JSON | Parseable Loki |
| Log levels | DEBUG/INFO/WARN/ERROR | Standard |

#### Enforcement

- ESLint + Prettier (frontend)
- Ruff + Black (backend)
- CI bloque si patterns non respectés

### Development Workflow Rules

#### Continuous Documentation Policy

**Principe fondamental :** La documentation fait partie intégrante de chaque feature, pas un effort séparé.

**Langue obligatoire :** English only pour :
- Code comments
- Docstrings (Python)
- JSDoc (TypeScript)
- Starlight documentation
- Commit messages
- PR descriptions

**Règles obligatoires :**

1. **Chaque story inclut sa documentation**
   - Starlight docs mises à jour dans la même PR que le code
   - Pas de merge sans documentation correspondante
   - La documentation est un critère d'acceptation

2. **GitHub Community Standards (one-time setup)**
   - README.md, CONTRIBUTING.md, etc. créés avec la première story (1-1)
   - Mis à jour au besoin par les stories suivantes

3. **Documentation par layer**

| Layer | Où documenter | Quand |
|-------|---------------|-------|
| API endpoints | Starlight `docs/api/` + OpenAPI auto | Avec chaque endpoint |
| Architecture | Starlight `docs/architecture/` | Avec chaque composant majeur |
| Deployment | Starlight `docs/deployment/` | Avec chaque infra change |
| User guide | Starlight `docs/getting-started/` | Avec chaque feature user-facing |

4. **Format de documentation**
   - Starlight (docs/) = source unique de vérité
   - README.md racine = résumé + liens vers Starlight
   - Code comments = pourquoi, pas quoi

5. **Acceptance Criteria standard**
   - Chaque story doit inclure: `Documentation Starlight mise à jour si applicable`

#### Documentation Enforcement (CI/CD)

**Automated checks in GitHub Actions (all blocking) :**

1. **Docstring coverage (Python - Ruff)**
   - Ruff rules: `D100-D107` (pydocstyle) - docstrings required
   - Config: `pyproject.toml` with `select = ["D"]`
   - 100% coverage on public functions/classes/modules

2. **JSDoc coverage (TypeScript - ESLint)**
   - Plugin: `eslint-plugin-jsdoc`
   - Rules: `jsdoc/require-jsdoc` on exports
   - 100% coverage on exported functions/classes

3. **Starlight documentation check**
   - Custom GitHub Action script checks if PR modifies:
     - `api/` → requires `docs/api/` update
     - `web/src/features/` → requires `docs/getting-started/` or `docs/architecture/` update
     - `infra/` → requires `docs/deployment/` update
   - Can be overridden with `skip-docs` label (hotfixes only)

4. **AI Code Review**
   - Tool: CodeRabbit AI (free for open source, unlimited PRs)
   - Alternative: Sourcery (free for open source Python)
   - Checks: code style, documentation quality, potential bugs
   - Advisory comments on PR (non-blocking)
   - Setup: Add `.coderabbit.yaml` config + enable GitHub App

5. **Auto-generated API docs (Starlight integration)**

   **TypeScript → Starlight (native):**
   - Plugin: `starlight-typedoc` (official Starlight plugin)
   - Reads JSDoc from TypeScript source → generates pages in Starlight
   - Config in `astro.config.mjs`:
     ```js
     import starlightTypeDoc from 'starlight-typedoc'
     integrations: [
       starlight({
         plugins: [starlightTypeDoc({ entryPoints: ['../web/src/**/*.ts'] })]
       })
     ]
     ```

   **Python → Starlight (via mkdocstrings):**
   - Tool: `mkdocstrings` with `mkdocs-material` theme
   - Generates Markdown from Python docstrings
   - CI workflow copies generated `.md` files to `docs/src/content/docs/api/python/`
   - Alternative: `sphinx` + `sphinx-markdown-builder` for more control

   **Workflow:**
   - On merge to `develop`: CI generates docs, commits to `docs/api/reference/`
   - Pages auto-update on next Starlight build

**Tools configuration :**

```toml
# pyproject.toml - Ruff docstring rules
[tool.ruff.lint]
select = [
  "D",     # pydocstyle - docstrings
  "E",     # pycodestyle errors
  "F",     # pyflakes
  "I",     # isort
]

[tool.ruff.lint.pydocstyle]
convention = "google"  # Google style docstrings
```

```json
// .eslintrc.json - JSDoc rules
{
  "plugins": ["jsdoc"],
  "extends": ["plugin:jsdoc/recommended"],
  "rules": {
    "jsdoc/require-jsdoc": ["error", {
      "publicOnly": true,
      "require": {
        "FunctionDeclaration": true,
        "MethodDefinition": true,
        "ClassDeclaration": true,
        "ArrowFunctionExpression": true
      }
    }],
    "jsdoc/require-description": "error",
    "jsdoc/require-param-description": "error",
    "jsdoc/require-returns-description": "error"
  }
}
```

#### GitFlow Branching Strategy

**Branches principales :**
- `main` - Production, toujours stable et déployable
- `develop` - Intégration, base pour les features

**Branches de support :**
- `feature/<nom>` - Nouvelles fonctionnalités (depuis `develop`)
- `release/<version>` - Préparation release (depuis `develop`)
- `hotfix/<nom>` - Correctifs urgents (depuis `main`)

**Flow standard :**
```
feature/xxx → develop → release/x.y.z → main
                                      ↓
                               tag vx.y.z
```

**Règles strictes :**
- JAMAIS de commit direct sur `main` ou `develop`
- Merge via Pull Request uniquement
- Squash merge pour features (historique propre)
- Merge commit pour releases et hotfixes (traçabilité)

#### Commit Messages

**Format Conventional Commits :**
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types autorisés :**
- `feat` - Nouvelle fonctionnalité
- `fix` - Correction de bug
- `docs` - Documentation uniquement
- `style` - Formatting, pas de changement de code
- `refactor` - Refactoring sans changement de comportement
- `test` - Ajout/modification de tests
- `chore` - Maintenance, dépendances, CI

**Exemples :**
```
feat(desktop): add window tiling support
fix(auth): handle expired session gracefully
docs(api): update OpenAPI descriptions
```

#### Pull Request Requirements

- Description claire du changement
- Lien vers issue/story si applicable
- Tests passent (100% coverage)
- Review par au moins 1 personne
- Pas de conflits avec branche cible

### Critical Don't-Miss Rules

#### Anti-Patterns à éviter

**Architecture :**
- JAMAIS exposer API-DB ou API-Backup sur Internet (ClusterIP uniquement)
- JAMAIS de JWT - utiliser sessions Redis server-side
- JAMAIS de commit direct sur `main` ou `develop`

**Sécurité :**
- JAMAIS stocker de secrets en DB non chiffrés (utiliser python-cryptography)
- JAMAIS logger de données sensibles (tokens, passwords, PSK)
- JAMAIS de self-signed certificates en production

**Code :**
- JAMAIS d'API SQLAlchemy 1.x (utiliser 2.0+ async)
- JAMAIS de Tailwind v3 config (utiliser v4)
- JAMAIS de pages Astro sans `client:load` (architecture SPA-like)

#### Edge Cases critiques

- Sessions expirées : Gérer gracieusement côté frontend (redirect login)
- Apps sans OIDC : Utiliser Proxy Auth (headers injectés par reverse proxy)
- Multi-tenant : Isolation par namespace K8S, pas par DB schema

#### Process Patterns

| Domaine | Pattern |
|---------|---------|
| Error boundary | Global + par feature critique |
| Loading state | TanStack Query (per-query) |
| Validation | Client-side first, server valide toujours |
| Notifications | Store centralisé `$notifications` |

---

_Document généré le 2026-01-10 pour UniDash. Ce fichier doit être lu par tous les agents IA avant toute implémentation._
