---
title: Python API Reference
description: Auto-generated Python API documentation from docstrings
---

## Python Packages

UniDash backend is organized into six Python packages:

| Package                    | Description                             |
| -------------------------- | --------------------------------------- |
| [unidash_shared](./shared) | Shared types, exceptions, and utilities |
| [unidash_db](./db)         | Database models and repositories        |
| [unidash_sso](./sso)       | Authentication and OIDC provider        |
| [unidash_api](./unidash)   | Main business logic API                 |
| [unidash_admin](./admin)   | Administration API                      |
| [unidash_backup](./backup) | Backup service API                      |

## Documentation Style

All Python code uses Google-style docstrings, enforced by Ruff D rules.

```python
def example_function(param1: str, param2: int) -> bool:
    """Short description of the function.

    Longer description if needed, explaining the purpose
    and behavior of the function.

    Args:
        param1: Description of first parameter.
        param2: Description of second parameter.

    Returns:
        Description of return value.

    Raises:
        ValueError: When param2 is negative.
    """
    pass
```
