---
title: Deployment Guide
description: How to deploy UniDash in production
---

## Deployment Modes

UniDash supports two deployment modes:

| Mode       | Internet Access   | VPN Required       |
| ---------- | ----------------- | ------------------ |
| Homelab    | Web + API exposed | Admin only         |
| Enterprise | Nothing exposed   | All access via VPN |

## Prerequisites

- K3S cluster (3 nodes recommended for HA)
- PostgreSQL 17 with Patroni
- Redis 7
- Valid TLS certificates (Let's Encrypt via cert-manager)

## Quick Deploy

```bash
# Clone repository
git clone https://github.com/UniDash-Linux/UniDash.git
cd UniDash

# Run Ansible playbook
cd infra/ansible
ansible-playbook -i inventory/production.yml playbooks/k3s-install.yml
```

## Configuration

See [Getting Started](/getting-started/installation) for detailed setup instructions.
