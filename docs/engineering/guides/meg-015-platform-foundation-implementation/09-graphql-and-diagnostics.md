<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/09-graphql-and-diagnostics.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# 09 — GraphQL and Diagnostics

---

# GraphQL Role

GraphQL is a transport and projection surface. It is not a persistence layer.

Resolvers must call application command or query services. They must not open database connections directly.

---

# First GraphQL Surface

The first Platform GraphQL schema should cover:

| Area | Required surface |
|------|------------------|
| Auth | local sign-in, sign-out, session refresh and remote sign-in challenge status |
| Users | user list, user detail and admin-managed status |
| Permissions | roles, grants and effective permission inspection |
| Configuration | config draft, validation, activation and active version |
| Jobs | job list, job detail, job logs and retry command |
| Health | component health and degraded component detail |
| Diagnostics | support bundle request and export status |

Product media queries should wait for the relevant Module.

---

# Diagnostics Model

Every component should report:

- component identifier;
- lifecycle state;
- health status;
- degraded reason;
- last successful check;
- last failure category;
- dependency health; and
- support bundle redaction class.

Component health should be granular enough for the admin UI to show a degraded Platform without reducing the whole system to a single failed state.

---

# Local Logs

The first implementation should write local `.log` files with structured fields. Logs should include component and Module identifiers where available, but must not include personal data or secrets.

Support bundles should be fully anonymised while allowing program and Module identification for open-source issue reporting.
