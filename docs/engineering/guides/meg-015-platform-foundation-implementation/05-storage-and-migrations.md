<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/05-storage-and-migrations.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# 05 — Storage and Migrations

---

# PostgreSQL Adapter Role

PostgreSQL is the first mandatory built-in storage adapter. It is compiled into the first Platform distribution and is required for a valid local deployment.

It remains an adapter. Application services depend on Platform contracts, not PostgreSQL driver types.

---

# First Schema Areas

The first migration set should create tables for:

| Area | Required tables |
|------|-----------------|
| Identity | users, credentials, passkey credentials, recovery factors |
| Sessions | sessions, remote sign-in challenges, revoked sessions |
| Permissions | roles, grants, resource attributes, policy audit records |
| Configuration | config versions, config activations, config validation results |
| Events | event outbox, event deliveries, event checkpoints |
| Jobs | jobs, job attempts, job logs |
| Diagnostics | component health snapshots, support bundle records |
| Storage registry | object records, logical ownership, retention metadata |

Media-specific tables do not belong in the Platform foundation unless required by a first built-in infrastructure contract.

---

# Migration Strategy

Platform migrations must follow expand and contract rules:

1. additive changes ship with the application version that needs them;
2. old and new schema views coexist where rollback risk exists;
3. destructive cleanup ships later, after rollback risk has passed; and
4. a synchronous pre-migration backup is required before structural migration.

The database is not part of a Generation. Generation rollback activates an earlier executable; it does not undo data mutations.

---

# Repository Implementation

Repository methods should be written against transaction-scoped handles.

The adapter owns SQL and row mapping. It should return Platform domain types or contract DTOs. It must not leak:

- `pgx` rows;
- SQL error codes;
- table-specific structs; or
- migration tool internals.

---

# Storage Acceptance

The PostgreSQL adapter is acceptable when:

- contract tests pass against a real PostgreSQL instance;
- migration up/down or forward-only recovery behaviour is documented;
- outbox writes occur in the same transaction as state changes;
- uniqueness and concurrency failures map to Platform error categories; and
- startup can detect missing, incompatible or partially applied migrations.
