---
title: Development Setup
description: How to set up UniDash for local development
---

## Quick Start with Docker

The easiest way to start developing is with Docker:

```bash
git clone https://github.com/UniDash-Linux/UniDash.git
cd UniDash
docker compose -f docker-compose.dev.yml up
```

This starts PostgreSQL and Redis. API and Web services are commented out until their Dockerfiles are created.

## Services

| Service     | Port | Description                 |
| ----------- | ---- | --------------------------- |
| PostgreSQL  | 5432 | Database                    |
| Redis       | 6379 | Cache and sessions          |
| api/db      | 8000 | Database API (future)       |
| api/sso     | 8001 | Authentication API (future) |
| api/unidash | 8002 | Main API (future)           |
| api/admin   | 8003 | Admin API (future)          |
| api/backup  | 8004 | Backup API (future)         |
| web         | 3000 | Astro frontend (future)     |
| docs        | 4321 | Starlight documentation     |

## Running Tests

```bash
# Python tests
docker compose -f docker-compose.dev.yml exec api pytest --cov

# Frontend tests
docker compose -f docker-compose.dev.yml exec web npm run test
```

## Code Style

Pre-commit hooks run automatically on commit. To run manually:

```bash
docker compose -f docker-compose.dev.yml exec api ruff check .
docker compose -f docker-compose.dev.yml exec web npm run lint
```
