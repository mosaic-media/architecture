<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/03-platform-contracts.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# 03 — Platform Contracts

---

# Contract Rule

Every external dependency required by Platform application services must be represented as a Platform-owned contract before an adapter is written.

The first contracts should be small and biased toward behaviour rather than database tables or transport shapes.

---

# First Contract Set

| Contract | Purpose | First adapter |
|----------|---------|---------------|
| `UnitOfWork` | Transaction boundary for application services | PostgreSQL |
| `UserStore` | Local user persistence and lookup | PostgreSQL |
| `SessionStore` | Session persistence and revocation | PostgreSQL |
| `PermissionStore` | Role, grant and attribute lookup | PostgreSQL |
| `ConfigStore` | Configuration version persistence | PostgreSQL |
| `EventOutbox` | Commit-time event persistence | PostgreSQL |
| `EventPublisher` | Runtime event dispatch | In-process bus |
| `SecretBroker` | Secret retrieval and rotation | OS keychain or vault |
| `Clock` | Deterministic time boundary | Runtime clock |
| `IDGenerator` | Stable identity creation | Runtime generator |
| `HealthProbe` | Component readiness and degradation | Adapter-specific |

---

# Contract Shape

Contracts should pass Platform value types, not database rows.

Example shape:

```go
type UnitOfWork interface {
    WithinTx(ctx context.Context, fn func(ctx context.Context, tx Tx) error) error
}

type Tx interface {
    Users() UserStore
    Sessions() SessionStore
    Permissions() PermissionStore
    Config() ConfigStore
    Outbox() EventOutbox
}
```

This shape keeps application services independent from PostgreSQL while still making transaction ownership explicit.

---

# Error Categories

Contract errors must map into stable Platform categories:

| Category | Meaning |
|----------|---------|
| `InvalidArgument` | Request cannot be accepted as submitted |
| `Unauthenticated` | Caller has no valid session |
| `PermissionDenied` | Caller lacks required permission or attribute |
| `NotFound` | Requested resource does not exist or is not visible |
| `Conflict` | State changed or uniqueness was violated |
| `Unavailable` | Required dependency is not currently usable |
| `Internal` | Unexpected Platform or adapter failure |

Adapters may retain driver-specific errors internally, but application services and transports must see Platform categories.

---

# Compatibility Metadata

The contract package should define a version identity even before SDK generation.

```go
const ContractID = "mosaic.platform.contract"
const ContractVersion = "v1"
```

This metadata becomes the source for later SDK compatibility checks under [MIP-004 — Platform–SDK Contract Protocol](../../protocols/mip-004-platform-sdk-contract-protocol/index.md).
