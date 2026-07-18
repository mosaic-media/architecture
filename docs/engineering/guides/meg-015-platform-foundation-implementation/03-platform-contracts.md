<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/03-platform-contracts.md
Document: MEG-015
Status: Draft
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
| `CredentialStore` | Password, passkey and recovery-factor persistence and lookup | PostgreSQL |
| `PermissionStore` | Role, grant and attribute lookup | PostgreSQL |
| `ConfigStore` | Configuration version persistence | PostgreSQL |
| `EventOutbox` | Commit-time event persistence | PostgreSQL |
| `EventPublisher` | Runtime event dispatch | In-process bus |
| `SecretBroker` | Secret retrieval and rotation | OS keychain or vault |
| `Clock` | Deterministic time boundary | Runtime clock |
| `IDGenerator` | Stable identity creation | Runtime generator |
| `HealthProbe` | Component readiness and degradation | Adapter-specific |

The first contract set is a starting point, not a ceiling. A later slice may reveal a genuine external dependency the original set did not anticipate; when that happens, add the contract rather than forcing the dependency through an existing one, and record why in this table. `CredentialStore` was added this way: the Identity, sessions and policy slice needed durable password, passkey and recovery-factor persistence per [07 — Identity, Policy and Sessions](07-identity-policy-and-sessions.md)'s Local Identity Scope, and no existing contract's purpose covered it.

---

# Contract Shape

Contracts should pass Platform value types, not database rows.

Store access is uniform. A transaction scope must not enumerate a fixed list of stores. Every store — Core Platform or capability — is resolved the same way, so nothing is privileged by being named on the transaction handle and adding a store never edits it.

Example shape:

```go
type UnitOfWork interface {
    WithinTx(ctx context.Context, fn func(ctx context.Context, tx Tx) error) error
}

// Tx marks a transaction scope. It intentionally exposes no fixed accessor
// list: Core Platform stores and capability stores are resolved identically,
// so adding a store never edits this interface.
type Tx interface {
    // sealed: carries the live transaction handle, no store accessors
    transaction()
}

// Store resolves a store contract bound to tx. The type parameter keeps the
// call site fully typed with no assertion. It is a package function rather
// than a Tx method because Go methods cannot take type parameters.
func Store[T any](tx Tx) (T, error)
```

A command that would previously have called `tx.Users()` obtains the same contract with `Store[UserStore](tx)`, and the outbox with `Store[EventOutbox](tx)` — fully typed, no assertion.

Storage itself is a port. A `StorageAdapter` provides the `UnitOfWork` and binds each resolved store to the live transaction, so the built-in PostgreSQL adapter can be replaced — for example by SQLite — without changing a call site. This keeps application services independent from any single engine, makes transaction ownership explicit, and lets the store set grow as new Platform bounded contexts appear without a central interface becoming a closed list that every addition must edit.

---

# Storage Extensibility Boundary

Uniform resolution is not an invitation for capabilities to own private schema.

Capabilities persist through Platform-owned storage contracts exposed by the SDK. They do not define their own tables, modify Core Platform schema or open parallel databases, per [MIP-005 — Module Adapter Contract Protocol](../../protocols/mip-005-module-adapter-contract-protocol/index.md). The Platform owns a deliberately content-agnostic object model, so a new content capability maps onto existing storage rather than extending it.

Store resolution stays uniform so that Core Platform bounded contexts and first-party capabilities participate in a transaction identically — not so that external Modules can inject storage. This preserves the architectural equality of built-in and Module-delivered capabilities required by [MEG-006 — Module Platform](../meg-006-module-platform/index.md) without granting any store a private path into the transaction boundary.

The reasoning behind this shape, and the alternatives rejected, are recorded in [MAD-001 — Transactional Store Extensibility](../../architecture/mad-001-transactional-store-extensibility/index.md).

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
