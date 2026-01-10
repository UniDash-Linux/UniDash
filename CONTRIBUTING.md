# Contributing to UniDash

Thank you for your interest in contributing to UniDash! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Development Setup](#development-setup)
- [GitFlow Workflow](#gitflow)
- [Conventional Commits](#conventional-commits)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a welcoming and inclusive community.

## Development Setup

### Prerequisites

- Python 3.14+
- Node.js 20+
- Git

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/OWNER/UniDash.git
cd UniDash

# Create Python virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or: .venv\Scripts\activate  # Windows

# Install development dependencies
pip install -r requirements-dev.txt
pip install -e "api/shared[dev]" -e "api/db[dev]" -e "api/sso[dev]" \
            -e "api/unidash[dev]" -e "api/admin[dev]" -e "api/backup[dev]"

# Install pre-commit hooks
pre-commit install

# Install frontend dependencies
cd web && npm install && cd ..

# Install documentation dependencies
cd docs && npm install && cd ..
```

For more details, see the [Development Guide](https://OWNER.github.io/UniDash/development/setup/).

## GitFlow

We use GitFlow branching strategy:

```
main          ← Production, always stable
develop       ← Integration branch
feature/*     ← New features (from develop)
release/*     ← Release preparation (from develop)
hotfix/*      ← Urgent fixes (from main)
bugfix/*      ← Bug fixes (from develop)
```

### Branch Naming

- `feature/<short-description>` - New features
- `bugfix/<short-description>` - Bug fixes
- `hotfix/<short-description>` - Urgent production fixes
- `release/<version>` - Release preparation

### Workflow

1. Create a feature branch from `develop`
2. Make your changes
3. Open a Pull Request to `develop`
4. After review and CI passes, merge

**Important Rules:**
- Never commit directly to `main` or `develop`
- All changes must go through Pull Requests
- Squash merge for features (clean history)
- Merge commit for releases and hotfixes (traceability)

## Conventional Commits

All commit messages must follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Code refactoring |
| `test` | Adding/modifying tests |
| `chore` | Maintenance, dependencies, CI |

### Examples

```bash
feat(desktop): add window tiling support
fix(auth): handle expired session gracefully
docs(api): update OpenAPI descriptions
test(store): add integration tests for app installation
chore(deps): update FastAPI to 0.110.0
```

## Code Style

### Python

- **Linters**: Ruff + Black
- **Style**: Google style docstrings
- **Config**: `ruff.toml` at project root

```bash
# Check code style
ruff check api/
black --check api/

# Auto-fix issues
ruff check --fix api/
black api/
```

### TypeScript/React

- **Linters**: ESLint + Prettier
- **Style**: JSDoc on all exports
- **Config**: `eslint.config.js` in `web/`

```bash
cd web
npm run lint        # Check
npm run lint:fix    # Auto-fix
npm run format      # Prettier
```

### Naming Conventions

| Language | Element | Convention | Example |
|----------|---------|------------|---------|
| Python | Functions | snake_case | `get_user_data()` |
| Python | Classes | PascalCase | `UserRepository` |
| Python | Files | snake_case | `user_service.py` |
| TypeScript | Functions | camelCase | `getUserData()` |
| TypeScript | Components | PascalCase | `WindowManager.tsx` |
| TypeScript | Stores | $prefix | `$userStore` |

## Testing

### Test-Driven Development (TDD)

We follow TDD principles:

1. **Red**: Write a failing test
2. **Green**: Write minimal code to pass
3. **Refactor**: Improve while keeping tests green

### Coverage Requirements

**100% coverage is required for all code.** CI will block merges if coverage drops below 100%.

### Running Tests

```bash
# Python tests
pytest api/ --cov --cov-fail-under=100

# Frontend tests
cd web && npm run test:coverage

# Documentation tests
cd docs && npm run test
```

### Test Structure

```
api/<service>/tests/
└── unidash_<service>/
    ├── unit/
    │   ├── test_models.py
    │   └── test_services.py
    └── integration/
        └── test_api.py

web/tests/
├── features/
│   ├── desktop/
│   ├── store/
│   └── auth/
└── shared/
```

## Documentation

### Continuous Documentation Policy

Documentation is part of each feature, not a separate task:

1. **Each PR must include documentation updates** where applicable
2. **Language**: English only for all documentation
3. **Docstrings**: Required on all public functions/classes
4. **JSDoc**: Required on all exported functions/classes

### Documentation Structure

| Change Type | Documentation Location |
|-------------|----------------------|
| API endpoint | `docs/api/` |
| Architecture | `docs/architecture/` |
| Infrastructure | `docs/deployment/` |
| User feature | `docs/getting-started/` |

### Building Documentation

```bash
cd docs
npm run dev     # Development server
npm run build   # Production build
```

## Pull Request

### Before Submitting

1. Ensure all tests pass
2. Ensure 100% code coverage
3. Run linters without errors
4. Update documentation if needed
5. Follow commit message conventions

### PR Template

Your PR should include:

- Clear description of changes
- Link to related issue (if any)
- Type of change (feature, fix, etc.)
- Testing checklist
- Documentation updates

### Review Process

1. Open PR against `develop` branch
2. Automated CI checks must pass
3. At least 1 reviewer must approve
4. CodeRabbit AI provides advisory comments
5. Squash merge after approval

### CI Checks

All PRs must pass:

- Python tests with 100% coverage
- Frontend tests with 100% coverage
- Ruff + Black (Python linting)
- ESLint + Prettier (TypeScript linting)
- Documentation requirements check

---

Thank you for contributing to UniDash!
