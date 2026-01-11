---
title: Architecture Overview
description: UniDash system architecture and design decisions
---

## System Architecture

UniDash follows a microservices architecture with separated APIs:

| Component   | Description                                |
| ----------- | ------------------------------------------ |
| api/db      | Database access layer (ClusterIP internal) |
| api/sso     | Authentication and OIDC provider           |
| api/unidash | Main business logic API                    |
| api/admin   | Administration API (VPN Admin only)        |
| api/backup  | Backup service (ClusterIP internal)        |
| web         | Astro frontend with React islands          |

## Technology Stack

- **Backend**: Python 3.13, FastAPI, SQLAlchemy 2.0
- **Frontend**: Astro 5, React, Tailwind CSS v4
- **Database**: PostgreSQL 17 with Patroni HA
- **Cache**: Redis 7
- **Orchestration**: K3S

See the [Architecture Decision Document](https://github.com/UniDash-Linux/UniDash/blob/main/_bmad-output/planning-artifacts/architecture.md) for detailed decisions.
