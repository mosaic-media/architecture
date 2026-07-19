# Architecture

How Mosaic is built. This document describes the system as it exists in `mosaic-platform` — 175 Go files, ~17,650 lines — not a system that is planned. Where it describes something unbuilt, it says so.

Read this before changing anything. For what Mosaic is and why, see [MOSAIC.md](index.md). For what is being built next, see [ROADMAP.md](roadmap.md).

---

## Bird's eye view

Mosaic is a self-hosted media server built as a single Go binary. A Supervisor selects which modules a user wants, compiles them into that binary, and manages the running process. There are no plugins, no dynamic libraries, and no RPC between local components.

The Platform is hexagonal. Its core defines contracts — interfaces describing what it needs — and everything technological satisfies them from outside. PostgreSQL is not privileged; it is a module that implements the storage port and could be replaced by another.

```mermaid
flowchart LR
    GQL["GraphQL"]
    HTTP["Health endpoints"]
    APP["Application services"]
    CON["Contracts"]
    DOM["Domain"]
    MOD["Modules"]
    PG[("PostgreSQL")]

    GQL --> APP
    HTTP --> APP
    APP --> CON
    CON --> DOM
    MOD --> CON
    MOD --> PG
```

Arrows mean *depends upon*. Dependencies point inward: transports depend on application services, which depend on contracts, which depend on the domain. Modules depend on contracts too, from the outside. **The domain imports nothing.**

---

## Code map

### `internal/platform/` — the core

Trusted, compiled in, defines the rules everything else follows. Imports no module and no transport.

**`domain/`** — business types with no infrastructure knowledge. `User`, `Session`, `Role`, `Grant`, `Permission`, `PasswordCredential`, `PasskeyCredential`, `RecoveryFactor`, `ConfigVersion`, `Event`, `OutboxEvent`, `DeliveryPolicy`, `ComponentHealth`, `LifecycleState`, `Secret`, `SecretRef`, the content model's `Node`, `Part`, `MediaLocation`, `Relation` and `SourceBinding`, and typed identifiers (`UserID`, `SessionID`, `EventID`, `NodeID`, …) over a shared `ID`.

**`contracts/`** — the ports. Every interface the core needs from the outside world:

| Contract | Purpose |
|---|---|
| `UnitOfWork` | `WithinTx(ctx, fn)` — the transaction boundary |
| `Tx` | Transaction scope. Stores reached through one `Tx` share one transaction |
| `StorageAdapter` | The storage port an engine implements |
| `UserStore`, `SessionStore`, `PermissionStore`, `ConfigStore`, `CredentialStore` | Persistence contracts |
| `NodeStore`, `PartStore`, `RelationStore`, `SourceBindingStore` | The content model — containment tree, bytes, association graph, identity |
| `EventOutbox`, `EventPublisher` | Event durability and delivery |
| `SecretBroker` | Secret resolution and rotation |
| `Clock`, `IDGenerator` | Determinism seams for testing |
| `HealthProbe`, `ComponentHealthReporter` | Health reporting |

**`app/`** — application services. One file per command or query: `create_local_user`, `authenticate_local_user`, `revoke_session`, `set_user_status`, `draft_config_version`, `validate_config_version`, `activate_config_version`, and read-side queries for users, permissions and configuration.

**`policy/`** — an ABAC-shaped engine. `Subject`, `Action`, `Resource`, `PolicyContext` produce a `Decision`, resolved by RBAC lookups against `PermissionStore`. Default-deny.

**`sessions/`** — `Manager` with `Issue`, `Validate`, `Revoke`.

**`config/`** — `ReloadClass`, a `Schema`/`FieldSpec` registry, `ChangedFields` diffing, and a `Manager` running the version state machine.

**`secrets/`** — `Broker` preferring the OS keychain, falling back to an AES-256-GCM encrypted local vault. Backend chosen once per process. `secret://` reference parsing.

**`events/`** — `Bus` (in-process publisher, subscriber registry keyed by event type) and `Worker` (drains the outbox on a ticker).

**`diagnostics/`** — health `Registry`, a JSON-Lines `Logger` that redacts by default, and support-bundle construction.

**`runtime/`** — the Supervisor-facing surface. Generation metadata, lifecycle state, readiness, liveness, migration tracking, config activation status, and `Shutdown`.

### `internal/modules/` — built-in modules

Infrastructure implementing Platform contracts, using the same registration and manifest shape an external module would use, but compiled in, required and trusted.

`postgres/` is the only one today: `pgx/v5`, twelve embedded SQL migrations, a deterministic migrator, implementations of every store contract, and SQLSTATE-to-category error mapping. **No pgx type, row or SQLSTATE escapes this package.**

### `internal/adapters/` — not module-shaped

Helpers that don't implement a full contract surface: `crypto/` (AES-GCM) and `filesystem/` (atomic writes). Storage engines do **not** belong here.

### `internal/transport/` — inbound

`graphql/` — a hand-built executable schema. `health/` — the Supervisor handoff endpoints.

### `internal/composition/builtin/` — module discovery

A `Registry` holding modules that present a `Manifest{ID, Version, Fulfills []string}`. Discovery is by registration rather than filesystem scan, but the shape deliberately mirrors how an external module would be discovered.

### `contracts/platform/v1/` — the public SDK surface

**Currently empty apart from `doc.go`.** Promoting the proven contracts here is the next milestone. It was once recorded as the thing blocking the reference capability; [ADR 0012](adr/0012-capabilities-do-not-own-stores.md) found the real blocker was the missing content model, which has since landed.

---

## Invariants

Break these and the architecture stops holding.

**Dependencies point inward.** Domain imports nothing. Application services depend on contracts, never on concrete module types. Transport calls application services, never storage.

**Seven error categories.** `InvalidArgument`, `Unauthenticated`, `PermissionDenied`, `NotFound`, `Conflict`, `Unavailable`, `Internal`. Modules may keep driver errors internally; nothing above sees them.

**One command order.** Validate shape → authenticate → authorise via policy → open `UnitOfWork` → load through contracts → apply domain rules → persist state *and* outbox events in the same transaction → return a Platform type.

**State and events commit together.** Structural, not conventional: `WithinTx` shares one `pgx.Tx` across every store. Proven by a test that fails mid-transaction and queries raw tables to confirm neither row persists.

**GraphQL resolvers call services only.** Enforced by a test that parses import declarations and fails on `internal/modules/postgres`, `pgx` or `database/sql`.

**Every config field declares a reload class.** `Hot`, `Restart`, `Generation`, or `Recovery`. Only Hot-only changes apply without escalation.

**At-least-once delivery.** Subscribers must be idempotent. A retry redelivers to every subscriber of that type, not only the one that failed.

**Secrets are unobservable.** Log fields redact unless explicitly marked safe; an unclassified field fails closed. Support bundles replace any free text not explicitly marked as containing nothing sensitive.

**Adding a media type is rows, not tables.** No schema migration, no new query path, no per-type column. This is the property the content model exists to deliver and the one that makes a community-built module possible without Platform changes. Vocabulary the Platform branches on is the exception and stays closed ([ADR 0015](adr/0015-open-and-closed-vocabularies.md)).

**Deletion is never a silent cascade.** Removing a node's last source binding leaves it `orphaned`, not deleted. Deleting a node that still has children, parts or bindings is refused, so a subtree is never taken by implication.

---

## Cross-cutting behaviour

**Transactions.** `Tx` enumerates the Platform's stores by name, and every store reached through one `Tx` writes to the same database transaction. The store set is Platform-owned and closed: capabilities own no schema, so there is nothing to register and nothing to resolve at runtime ([ADR 0012](adr/0012-capabilities-do-not-own-stores.md)). Growing the set means editing `Tx`, which is deliberate Platform evolution rather than a cost. One transaction spans one bounded context's stores plus the shared outbox ([ADR 0014](adr/0014-storage-authority-and-transaction-scope.md)); work crossing contexts is two transactions joined by an event.

**Events.** Writers append to the outbox inside the business transaction. The worker drains it, publishes through the bus, and marks published or records failure. Failure applies an exponential backoff capped at one hour and dead-letters after eight attempts. Events carry a full envelope: identity, type, timestamps, actor, correlation and causation identifiers, payload, redaction class.

**Migrations.** Embedded, versioned, checksummed. Applied with their tracking row in one transaction. The startup gate fails fast on a missing, checksum-mismatched, gapped, or database-ahead schema.

**Configuration.** Draft → Validated → Active, with Rejected and Superseded terminal paths. At most one Active version, enforced by a unique partial index rather than application logic.

**Shutdown.** Stop the worker's poll loop, run one final synchronous drain, exit. Proven by a test using a one-hour ticker so only the shutdown drain can deliver.

---

## The content model

Four tables — `nodes`, `parts`, `relations`, `source_bindings` — designed in [ADR 0013](adr/0013-object-graph.md) and [ADR 0014](adr/0014-storage-authority-and-transaction-scope.md). They are the first content in a schema that was otherwise entirely infrastructure.

**Containment is a tree; association is a graph.** `nodes` is one recursive tree of variable depth: a film is Work → Item, a series is Work → Container(season) → Item(episode), a chapter-only manga is Work → Item until a volume layer is inserted later. Nothing may assume a node has a parent or that a Work's children are containers. `relations` carries typed, directed, confidence-scored edges that do not nest. Conflating the two is what makes flat media models accumulate edge cases indefinitely.

**A Part is what plays.** An edition or cut is not a new Node — one Item carries however many cuts exist, because the cut is a property of which bytes play. Multi-disc releases use the same mechanism with `part_role = segment`, so there is one source-selection path rather than two. A Part points at bytes and never contains them; local paths and remote provider references are equally first-class.

**Identity resolution is visible.** A weak match lands as `pending_review` and surfaces to a user rather than silently merging two works that share a title. A merge is a confirmed high-confidence binding; a split moves a binding to a different node without re-fingerprinting the source.

### Four deliberate non-uniformities

Forcing every media type through one shape is its own bug. These four are modelled against the grain on purpose, and each is cheap to normalise away by accident, so each is pinned by a contract test:

- **Artists are not containers of albums.** Box sets, collaborations and various-artist compilations all break single-parent containment. An artist is its own Work joined to album Works by Relation.
- **Collected editions are their own Work**, related to what they collect by `collection_member` — the same mechanism as any other collection.
- **An anime and its source manga are two Works** joined by `adaptation`. They have different part structures and diverge in canon, so one tree would corrupt both.
- **IPTV programme listings never become Nodes.** A channel is a Node; a programme that airs once is not. Running identity, merge and relation machinery over guide data is waste rather than correctness.

### Implementation notes

**`media_type`, `container_type` and `item_type` are unconstrained text; the graph vocabulary is not.** [ADR 0015](adr/0015-open-and-closed-vocabularies.md) draws the line: vocabulary the Platform *branches on* — `node_kind`, `part_role`, relation types, match methods, statuses — is closed and `CHECK`-constrained, because an unrecognised value there is a traversal that does not know what it is looking at. Vocabulary that only *describes content* is open, because a `CHECK` would make every new media type a schema migration. Enforcement on the open columns is currently nothing, so a typo fragments a library silently; a `media_types` registry is the anticipated fix, triggered when something other than Platform code can introduce a type. Attribute correctness in the JSONB columns belongs to the writing capability on the same terms.

**Identifiers are UUIDv7 in native `uuid` columns**, with their own generator alongside the UUIDv4 one that continues to serve the infrastructure tables. Those keep their `text`/UUIDv4 ids and are not migrated.

**Three things ADR 0013 leaves open are unbuilt rather than invented:** the fractional ordering scheme at large scale (`natural_order` is stored as given and nothing rebalances), relation confidence decay or reverification (edges are written once, and `RelationStore` has no `Update` so the absence stays visible), and attribute validation.

---

## Supervisor handoff

Five HTTP endpoints, each a thin call into `internal/platform/runtime`:

`/metadata` · `/readyz` · `/healthz` · `/migrations` · `/config`

Readiness is false if any component reports Unavailable; Degraded alone does not block. Liveness goes false once shutdown begins, so an intentional exit is not read as a crash. The Platform never reverses a database mutation — rollback is the Supervisor activating a different Generation.

---

## Testing

`test/contract/` holds an adapter-agnostic suite proving any storage implementation satisfies the contracts. It runs against real PostgreSQL — embedded by default, or dockerised. The PostgreSQL adapter passes the same behavioural tests a future storage adapter would have to pass.

Integration tests run against a real database, not mocks. Application service tests run without PostgreSQL, against contract fakes. Boundary tests parse import declarations rather than grepping text. Where a test could pass by construction, it was verified to fail against a deliberately introduced violation.

Gate for every change: `go build ./...`, `go vet ./...`, `go test ./... -race`.

### Standing gates

Each of these must keep passing. They are the properties that stop the architecture eroding.

| Gate | Evidence required |
|---|---|
| Contract compile | Core contracts compile without adapters |
| Import boundary | Modules and transports cannot import private Platform internals |
| Application service | Commands enforce validation, authentication, policy and transactions |
| Storage contract | Adapter passes the shared contract suite against real PostgreSQL |
| Migration | Fresh install and upgrade path both tested |
| Outbox | State change and event append commit atomically |
| Policy | Denied actions cannot mutate state |
| GraphQL | Resolvers call services, not database packages |
| Diagnostics | Health reporting and support-bundle redaction verified |
| Supervisor | Process exposes readiness, liveness and shutdown behaviour |
| Content model | Tree, graph, parts and bindings pass the contract suite; the four non-uniformities stay expressible |

---

## Not built

Stated plainly so nothing here is mistaken for a description of something real.

- **Command handlers over the content model.** The four stores exist and pass the contract suite against real PostgreSQL, but no application service commands them, so there is no validate → authenticate → authorise → transact path into the graph. The `Tx` fakes in `internal/platform/app` and `internal/transport/graphql` return nil for the content stores for exactly this reason.
- **IPTV programme listings.** ADR 0013 gives them their own lightweight table keyed to the channel node, deliberately outside the Node machinery. That table is unbuilt.
- **Module permissions.** The policy engine governs *user* authority. Module authority is undecided and unimplemented.
- **External modules.** Only the built-in shape exists.
- **Jobs and diagnostics history.** Tables exist from earlier migrations with no contract or service above them. GraphQL resolvers for them return `Unavailable` rather than faking success.
- **Session refresh and device pairing.** No backing service.
- **Shell, SDUI, design language.** Nothing.
- **HTTP transport for GraphQL.** The schema is executable and tested, but not yet served.
