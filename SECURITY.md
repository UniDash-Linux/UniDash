# Security Policy

## Supported Versions

We release patches for security issues in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security issue, please report it by sending an email to <pikatsuto@gmail.com>.

Please include the following information:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the issue
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue

We will acknowledge receipt of your report within 48 hours and provide a more detailed response within 7 days.

## Security Measures

UniDash implements the following security measures:

- All communications are encrypted (HTTPS, VPN)
- Passwords are stored with secure hashing (argon2)
- Sessions expire after 24h of inactivity
- Cluster access is restricted to VPN or local network
- Each app runs in its isolated namespace

## Disclosure Policy

When we receive a security report, we will:

1. Confirm the issue and determine affected versions
2. Audit code to find similar issues
3. Prepare fixes for all supported versions
4. Release patches as quickly as possible
