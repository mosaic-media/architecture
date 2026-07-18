<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/11-test-gates.md
Document: MEG-015
Status: Draft
-->

# 11 — Test Gates

---

# Required Gates

Each implementation slice should introduce its own tests before the next dependent slice begins.

| Gate | Required evidence |
|------|-------------------|
| Contract compile gate | Core contracts compile without adapters |
| Import boundary gate | Modules and transports cannot import private Platform internals |
| Application service gate | Commands enforce validation, authentication, policy and transactions |
| PostgreSQL contract gate | Adapter passes shared contract tests against real PostgreSQL |
| Migration gate | Fresh install and upgrade path are tested |
| Outbox gate | State change and event append commit atomically |
| Policy gate | Denied actions cannot mutate state |
| GraphQL gate | Resolvers call services rather than database packages |
| Diagnostics gate | Health and support bundle redaction are verified |
| Supervisor gate | Candidate process exposes readiness, liveness and shutdown behaviour |

---

# Test Shape

Contract tests should be reusable. The PostgreSQL adapter should pass the same behavioural tests that a future storage adapter would need to pass.

Integration tests may require local PostgreSQL. Unit tests for application services should run without PostgreSQL by using contract fakes.

---

# Acceptance Baseline

Before the Platform foundation is considered build-ready for SDK extraction:

- `go test ./...` must pass;
- adapter contract tests must pass against PostgreSQL;
- migration tests must run from an empty database;
- import boundary checks must pass;
- GraphQL resolver tests must prove service routing; and
- Supervisor health probes must pass against a running Platform process.
