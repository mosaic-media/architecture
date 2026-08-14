# Architecture

How Mosaic is built. This document describes the system as it exists in `platform`, not a system that is planned. Where it describes something unbuilt, it says so.

Read this before changing anything. For what Mosaic is and why, see [what Mosaic is](index.md). For what is being built next, see [the roadmap](roadmap.md).

---

## Bird's eye view

Mosaic is a self-hosted media server built as a Go binary that CI compiles from a version tag ([platform#38](https://github.com/mosaic-media/platform/blob/main/docs/adr/0038-platform-binary-built-by-ci.md)). The core modules are linked into it — no plugin, no dynamic library, no RPC between them. **Extension modules are not in that binary**: they are installed by a user at runtime and run in their own process behind a gRPC harness ([architecture#3](adr/0003-two-module-tiers.md), [platform#39](https://github.com/mosaic-media/platform/blob/main/docs/adr/0039-extension-module-boundary.md)), which is the one place Mosaic does pay a transport cost, deliberately, for a boundary.

The Platform is hexagonal. Its core defines contracts — interfaces describing what it needs — and everything technological satisfies them from outside.

```mermaid
flowchart LR
    RPC["Connect: Auth + Session"]
    HTTP["Health endpoints"]
    APP["Application services"]
    CON["Platform contracts"]
    DOM["Domain"]
    SDK["Published SDK"]
    BM["Built-in module"]
    CM["Core module"]
    HOST["Extension host"]
    PG[("PostgreSQL")]

    subgraph own ["its own process"]
        EM["Extension module"]
    end

    RPC --> APP
    HTTP --> APP
    APP --> CON
    APP --> SDK
    CON --> DOM
    BM --> CON
    BM --> PG
    HOST --> CON
    CM --> SDK
    EM --> SDK
```

Arrows mean *depends upon*, and nothing else — the process boundary is drawn as a box rather than an arrow, because an arrow that sometimes meant "calls over gRPC" would be the ambiguity this repository keeps paying for. Dependencies point inward: transports depend on application services, which depend on contracts, which depend on the domain. **The domain imports nothing.**

The two module halves depend on different things, and it matters. A **built-in** module implements the Platform's own contracts from outside — which is why PostgreSQL is not privileged and could be replaced. A **core** or **extension** module never sees those contracts at all; it compiles against the published SDK, which is what makes the tier a delivery decision rather than a rewrite. The extension host is Platform code, on the Platform's side of that line.

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
| the store set | Persistence contracts, reached through `Tx` and **enumerated only in `contracts/unit_of_work.go`**, each accessor carrying the record that added it. It grows with the Platform, so a second list here would be a stale one — read the type |
| `EventOutbox`, `EventPublisher` | Event durability and delivery |
| `SecretBroker` | Secret resolution and rotation |
| `Clock`, `IDGenerator` | Determinism seams for testing |
| `HealthProbe`, `ComponentHealthReporter` | Health reporting |

**`app/`** — application services, **one file per command or query**, which is the convention rather than a list: the directory is the index and it is long, spanning identity, roles and delegation, configuration versions, content and enrichment, library rules, playback and watch state, modules and extensions, telemetry, jobs and server setup. Two files there are load-bearing beyond their own command — `service.go` holds `enter`, the single authenticate-and-authorise gate every entry point passes through, and `system_principal.go` is the caller background work acts as.

**`policy/`** — an ABAC-shaped engine. `Subject`, `Action`, `Resource`, `PolicyContext` produce a `Decision`, resolved by RBAC lookups against `PermissionStore`. Default-deny.

**`sessions/`** — `Manager` with `Issue`, `Validate`, `Revoke`.

**`config/`** — `ReloadClass`, a `Schema`/`FieldSpec` registry, `ChangedFields` diffing, and a `Manager` running the version state machine.

**`secrets/`** — `Broker` preferring the OS keychain, falling back to an AES-256-GCM encrypted local vault. Backend chosen once per process. `secret://` reference parsing.

**`events/`** — `Bus` (in-process publisher, subscriber registry keyed by event type) and `Worker` (drains the outbox on a ticker).

**`diagnostics/`** — health `Registry`, a JSON-Lines `Logger` that redacts by default, and support-bundle construction.

**`runtime/`** — the Supervisor-facing surface. Generation metadata, lifecycle state, readiness, liveness, migration tracking, config activation status, and `Shutdown`.

### `internal/modules/` — built-in modules

Infrastructure implementing Platform contracts, using the same registration and manifest shape a module of either outer tier would use, but compiled in, required and trusted.

`postgres/` is the only one today: `pgx/v5`, embedded and versioned SQL migrations, a deterministic migrator, implementations of every store contract, and SQLSTATE-to-category error mapping. **No pgx type, row or SQLSTATE escapes this package.**

### `internal/adapters/` — not module-shaped

Helpers that don't implement a full contract surface: `crypto/` (AES-GCM for the secret vault, and an Argon2id `PasswordHasher`), `filesystem/` (atomic writes), and two smaller ones for the instance identity and for listeners. Storage engines do **not** belong here.

`extension/` sits here too and is the exception worth knowing: it is the **host** of the extension tier rather than a member of any tier — the fetcher, the installer, the signature and digest verification, the go-plugin harness and the egress-containment report. Nothing above the capability registry knows it exists, because what the Platform holds is a `v1.Capability` whichever side of the process boundary answers it.

An adapter is not a built-in module: there is no manifest and no registration through `internal/composition/builtin`, because each fulfils a single small port rather than a broad contract surface. It is still swappable, behind the same hexagonal seam — the composition root wires it directly. The password hasher satisfies the `domain.PasswordVerifier` port (`Hash`/`Verify`) and is chosen in `main.go`, so replacing Argon2id with bcrypt, scrypt or an HSM-backed signer is a one-line change there. The `crypto` package imports no Platform code, so the compile-time assertion that it satisfies the port lives in its external test package rather than coupling the adapter to `domain`.

### `internal/transport/` — inbound

`session/` — the **first-party client transport**, a typed two-lane Connect/gRPC surface generated from one `.proto` ([contracts#5](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0005-cross-client-transport-two-lane-rpc.md)). Lane 1 is unary intents (`Attach`/`Navigate`/`Invoke`/`SubmitInput`); lane 2 is one server-streaming `Subscribe` per session over which the Platform pushes region updates, shell mutations, toasts and unsolicited events. Both lanes multiplex onto one HTTP/2 connection (served over h2c). A per-session **outbound mailbox** owns the wire — unary handlers only enqueue; a single sender goroutine drains to `Send` (gRPC `Send` is not goroutine-safe) — and a monotonic per-session `seq` with a bounded replay buffer gives stream resume, which subsumes [supervisor#4](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0004-supervisor-driven-live-handover.md)'s handover. An `Invoke` routes straight to the application services (`ImportContent`/`ConfigureModule`/`playPart`) through a `dispatch` switch that is now the complete enumeration of what a client can invoke — since [platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md) there is no other transport to reach a command through, so an action `dispatch` cannot map does not exist. The screen emit-side ([platform#19](https://github.com/mosaic-media/platform/blob/main/docs/adr/0019-sdui-emit-side.md)) backs it; `UINode` subtrees ride the envelope as SDUI-JSON bytes ([contracts#5](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0005-cross-client-transport-two-lane-rpc.md)'s encoding option (a)). This supersedes the bespoke WebSocket of [platform#22](https://github.com/mosaic-media/platform/blob/main/docs/adr/0022-live-session-websocket.md); the first-party clients are ported and the chain works end to end.

`auth/` — the Connect **`AuthService`** ([platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md)): `SignIn`/`SignOut` over `AuthenticateLocalUser`/`RevokeSession`. It is a service of its own because it is the one call made *without* a session — every `SessionService` request begins with a session ref. Together with `session/` it is the **entire** client API: [platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md) deleted the GraphQL transport that [contracts#5](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0005-cross-client-transport-two-lane-rpc.md) had retained as an external/tooling surface, having found it had no caller — the Shell used exactly one operation of it (`signIn`), and its other resolvers duplicated commands the session transport already dispatched. `rpc/` — the plumbing both services share: the Platform's seven error categories mapped onto Connect status codes (the thing GraphQL's always-200 envelope could not do), and the telemetry interceptor that seeds each request's trace ([platform#33](https://github.com/mosaic-media/platform/blob/main/docs/adr/0033-instrument-at-the-seams.md)), parameterised by component so each service names itself. `screens/` — the SDUI emit-side ([platform#19](https://github.com/mosaic-media/platform/blob/main/docs/adr/0019-sdui-emit-side.md)) the session transport renders through; `artwork/` — the artwork proxy ([platform#20](https://github.com/mosaic-media/platform/blob/main/docs/adr/0020-artwork-proxy-and-cache.md)); `playback/` — the media origin ([platform#25](https://github.com/mosaic-media/platform/blob/main/docs/adr/0025-playback-consumer-and-media-origin.md)); `health/` — the Supervisor handoff endpoints. The composition root serves the client-facing API and the operational handoff on separate ports (`:8081` and `:8080`), and constructs `app.Service` with an Argon2id password hasher. **Not every Platform capability is client-reachable** — the full list is [Unreachable capability](unreachable-capability.md), and it is longer than the transport change that prompted it. Creating roles, granting them, drafting and activating config versions and setting user status have commands, policy actions and tests, but no client surface: they had GraphQL mutations with no UI behind them, and [platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md) chose to delete rather than re-port them, on the grounds that they arrive properly as server-emitted screens when an admin UI exists. A fresh server establishes its first authority by being **claimed**: it seeds no administrator, and boots to a setup wizard where the first person to reach it becomes one ([platform#54](https://github.com/mosaic-media/platform/blob/main/docs/adr/0054-claiming-an-unclaimed-server.md)). `bootstrap.EnsureAdmin` survives beside that, env-gated, idempotent and unset by default, for an automated deployment and for a box whose login was lost.

### `internal/composition/builtin/` — module discovery

A `Registry` holding modules that present a `Manifest{ID, Version, Fulfills []string}`. Discovery is by registration rather than filesystem scan, but the shape deliberately mirrors how a module from its own repository is discovered.

### Core and extension modules — their own repositories

Distinct from `internal/modules/` (built-in, trusted, required) and from `capabilities/reference/` (a package *inside* the Platform module): both of these tiers are a **Go module in its own repository**, importing only the SDK and invoked through the capability registry ([platform#15](https://github.com/mosaic-media/platform/blob/main/docs/adr/0015-module-capability-and-invocation.md), [platform#16](https://github.com/mosaic-media/platform/blob/main/docs/adr/0016-optional-module-composition.md)). What separates them is how they arrive: a **core** module is a `go.mod` dependency compiled in, an **extension** module is installed at runtime and hosted out of process. The code is written the same way for either ([architecture#3](adr/0003-two-module-tiers.md)).

[`module-stremio-addons`](https://github.com/mosaic-media/module-stremio-addons) is the first: a client of the Stremio addon protocol. It implements the SDK `Capability` interface (`Manifest()` plus `Import(ctx, ContentService, ImportRequest)`), owns no schema, and reflects movies and TV into the graph — metadata as the Work and its tree, streams as `RemoteLocation` Parts, the two independent so a meta-only addon adds no Parts. A boundary test, and Go itself, keep it to the SDK and the standard library.

It is an **extension** module, so the Platform does not depend on it at all ([platform#51](https://github.com/mosaic-media/platform/blob/main/docs/adr/0051-extension-installation-is-user-initiated-and-persistent.md)): it appears in neither `go.mod` nor the composition root, and a user installs it at runtime through the `installExtension` action, after which the extension Manager adopts it across restarts. The **core** modules — `module-tmdb`, `module-cinemeta`, `module-remote-playback` — are the `go.mod` dependencies at tagged versions, compiled in; read `go.mod` for which and at what version, rather than a list here. A caller invokes a module through the `ImportContent` command (the session transport's `importContent` action, policy action `content.import`), which authorises the caller, resolves the capability by id, and hands it the `app.Service` as its `ContentService` — so the module's own writes each re-authorise as the invoking user ([platform#13](https://github.com/mosaic-media/platform/blob/main/docs/adr/0013-how-a-capability-acts.md)). Explicit registration stands in for [platform#4](https://github.com/mosaic-media/platform/blob/main/docs/adr/0004-static-go-module-composition.md)'s eventual Build-Pipeline-generated `imports.go`.

The addons the Stremio module sources from are **user-managed settings**, not composed-in config ([platform#17](https://github.com/mosaic-media/platform/blob/main/docs/adr/0017-module-settings.md)): a `ModuleSettingsStore` (one jsonb document per module id, joined to `Tx`) holds them, generic `configureModule`/`moduleSettings` commands (actions `module.configure`/`module.read`) set and read them, and the Platform hands them to the module on each invocation through `ImportRequest.Settings`. The Platform stores the document opaquely; the module interprets it (`{"addons":[...]}`). This is the first of the SDK gaps building the module surfaced.

### The published SDK — its own module

The public contract surface ([platform#12](https://github.com/mosaic-media/platform/blob/main/docs/adr/0012-published-contract-surface.md)) has been **extracted into a standalone module**, [`github.com/mosaic-media/sdk`](https://github.com/mosaic-media/sdk). The Platform depends on it importing `github.com/mosaic-media/sdk/contracts/platform/v1`. It is pre-1.0 and bumps additively whenever a module finds a gap; **the version in use is `platform/go.mod` and the per-version changelog is the SDK's own `README.md`**, so neither is restated here.

It carries the content models (`Node`, `Part`, `Relation`, `SourceBinding` and their vocabularies), the content command, query and result types, the `ContentService` interface `internal/platform/app.Service` implements, the `Capability` interface a module of either tier implements, the provider roles, the ambient `Telemetry` handle, and an opaque `Caller`. The store contracts, `Tx` and the identity and configuration models are **not** in it — they are Platform↔engine plumbing and stay internal. Because the SDK is a separate module, Go itself forbids it from importing the Platform's `internal/`, so an internal-type leak is a compile error rather than something a test must catch. `capabilities/reference` (the reference capability) and `test/sdkprobe` build against the SDK and nothing else of the Platform's; `test/sdkboundary` compiles the probe as a standing check.

Known gap: `ContentService` exposes no *read* for relations (`ListFrom`/`ListTo`), so a capability can create edges but not query them back through the surface. The reference capability does not need it; it is a candidate addition rather than a defect.

### The Shell — a package in the `web` workspace

The human-facing surface, [`web/packages/shell`](https://github.com/mosaic-media/web/tree/main/packages/shell), is a **client of the Platform over Connect** ([platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md)) — not a Module, not part of the binary — in the first-party `web` workspace (React + TypeScript + Vite), AGPL-3.0-only ([architecture#1](adr/0001-licensing.md)). It is **Server-Driven** ([contracts#1](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0001-server-driven-ui-and-the-shell.md)): the Platform sends a tree of typed `UINode`s carrying declarative `Action` envelopes, and the Shell renders it. The vocabulary is open (an unknown node type degrades to a placeholder) and the contract is technology-agnostic, so a future Flutter client for TV, desktop and mobile renders the same payloads.

Its components are **primitives or definitions** ([contracts#2](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0002-primitives-and-definitions.md)): a small, irreducible set of native primitives (the cross-client vocabulary, styled from tokens) and everything else — containers included — as `ComponentDefinition` data. **Definitions are authored only in the contract and the client bundles none** ([contracts#7](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0007-components-are-authored-only-in-the-contract.md)): ~30 components once lived as hand-written TypeScript in the React client, the Platform served a dump of *that*, and the contract's own four copies had silently drifted. The React implementation of that vocabulary — primitives, registry, renderer, definition expander, token skin — has itself been extracted into a shared package, `sdui-react` (below), so the Shell is now a thin app on top of it. The SDUI contract — the schema, the standard definition library and the tokens — is likewise its own repository, `contracts` (below), because two Go producers already need it ([contracts#3](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0003-sdui-contract-repository.md)).

### The SDUI contract — its own repository

[`contracts`](https://github.com/mosaic-media/contracts) is to the interface what the SDK is to content: the language-neutral contract a **producer** (the Platform's emit-side, a UI-contributing Module) emits and a **client** (the Shell, a native client) renders ([contracts#1](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0001-server-driven-ui-and-the-shell.md), [contracts#3](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0003-sdui-contract-repository.md)). It carries the schema as **JSON Schema** (`UINode` open tree, the `Action` envelope, `ComponentDefinition`) — JSON for the *authoring* layer, because the vocabulary is open and the definitions and tokens are JSON data. The *wire* is protobuf end to end: `UINode` is generated as a message too ([contracts#6](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0006-contracts-protobuf-workspace.md)), and since [platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md) protobuf/Connect is the only client transport there is. It ships a **Go producer binding** (`Node`/`Action` types plus standard-component builders), a **TypeScript** binding for the Shell, the **standard definition library** as data, and the **design tokens** (DTCG). Apache-2.0, like the SDK ([architecture#1](adr/0001-licensing.md)). A `replace` directive is for local cross-repo work and may not land in a commit. Go consumers are presently pinned to it by **pseudo-version** rather than by tag, because tag pushes are refused from the environment it is built in — an ordinary `require` resolved from the proxy, which keeps that rule intact.

### The React runtime and the storybook — packages in the `web` workspace

The **web renderer** of the contract is a shared package, [`web/packages/sdui-react`](https://github.com/mosaic-media/web/tree/main/packages/sdui-react) (`@mosaic-media/sdui-react`, [web#1](https://github.com/mosaic-media/web/blob/main/docs/adr/0001-react-sdui-runtime.md)): the React implementation of the primitives, the registry, the recursive renderer, the definition expander, the runtime provider, and the token skin. It is the reference *web* rendering engine; the Shell and the storybook consume it as **peers**. AGPL-3.0-only — first-party client code, distinct from the Apache-2.0 contract. A native (Flutter) client would be its own runtime implementing the same contract.

The **component storybook**, [`web/packages/storybook`](https://github.com/mosaic-media/web/tree/main/packages/storybook), renders every component live from `@mosaic-media/sdui` data beside the `UINode` payload that produced it — bespoke rather than Storybook.js, because a definitions-as-data component's API *is* its payload. It is deployed to [mosaic-media.github.io/web](https://mosaic-media.github.io/web/).

---

## Invariants

Break these and the architecture stops holding.

**Dependencies point inward.** Domain imports nothing. Application services depend on contracts, never on concrete module types. Transport calls application services, never storage.

**The SDK says how a module interacts with the Platform; the Platform holds the implementations.** The published contract names no implementation and depends on nothing, so which library the Platform uses stays the Platform's own choice rather than a version floor in every module author's build and a breaking change to a third-party surface whenever it moves. The surface may be *wide* — a module nobody has imagined has to be expressible, and a missing verb is found only by whoever it blocks — but never *deep*; the two are not in tension, because a contract can declare a great many interfaces and still name no library, which is what the content surface already does. **Not held today:** the SDK's `go.mod` requires four OpenTelemetry API modules. [sdk#10](https://github.com/mosaic-media/sdk/blob/main/docs/adr/0010-the-sdk-carries-no-implementation.md) reverses that clause of [sdk#8](https://github.com/mosaic-media/sdk/blob/main/docs/adr/0008-opentelemetry-is-the-telemetry-implementation.md) — the OTel wiring moves to the Platform and to the extension harness, and OpenTelemetry stays the implementation in every process — and it is not built.

**Seven error categories.** `InvalidArgument`, `Unauthenticated`, `PermissionDenied`, `NotFound`, `Conflict`, `Unavailable`, `Internal`. Modules may keep driver errors internally; nothing above sees them.

**One command order.** Validate shape → authenticate → authorise via policy → open `UnitOfWork` → load through contracts → apply domain rules → persist state *and* outbox events in the same transaction → return a Platform type. Authenticate and authorise are one call, `Service.enter`, returning an `authorized` ([platform#41](https://github.com/mosaic-media/platform/blob/main/docs/adr/0041-authorization-is-carried-in-the-type.md)) — an internal helper takes that value and reads stores directly, so only an entry point takes a `v1.Caller`. Enforced by a conformance suite that asserts every caller-bearing method refuses an unknown session and an ungranted caller, and fails the build when a new one is added without a row.

**State and events commit together.** Structural, not conventional: `WithinTx` shares one `pgx.Tx` across every store. Proven by a test that fails mid-transaction and queries raw tables to confirm neither row persists.

**Transports call services only.** Enforced by a test that parses import declarations and fails on `internal/modules/postgres`, `pgx` or `database/sql`. It lived in the GraphQL transport, which was the first one; since [platform#37](https://github.com/mosaic-media/platform/blob/main/docs/adr/0037-one-client-transport.md) retired that package the copies in `transport/auth` and `transport/health` carry the rule.

**Every config field declares a reload class.** `Hot`, `Restart`, `Generation`, or `Recovery`. Only Hot-only changes apply without escalation.

**At-least-once delivery.** Subscribers must be idempotent. A retry redelivers to every subscriber of that type, not only the one that failed.

**Secrets are unobservable.** Log fields redact unless explicitly marked safe; an unclassified field fails closed. Support bundles replace any free text not explicitly marked as containing nothing sensitive.

**Adding a media type is rows, not tables.** No schema migration, no new query path, no per-type column. This is the property the content model exists to deliver and the one that makes a community-built module possible without Platform changes. Vocabulary the Platform branches on is the exception and stays closed ([platform#11](https://github.com/mosaic-media/platform/blob/main/docs/adr/0011-open-and-closed-vocabularies.md)).

**Deletion is never a silent cascade.** Removing a node's last source binding leaves it `orphaned`, not deleted. Deleting a node that still has children, parts or bindings is refused, so a subtree is never taken by implication.

---

## Cross-cutting behaviour

**Transactions.** `Tx` enumerates the Platform's stores by name, and every store reached through one `Tx` writes to the same database transaction. The store set is Platform-owned and closed: capabilities own no schema, so there is nothing to register and nothing to resolve at runtime ([platform#8](https://github.com/mosaic-media/platform/blob/main/docs/adr/0008-capabilities-do-not-own-stores.md)). Growing the set means editing `Tx`, which is deliberate Platform evolution rather than a cost. One transaction spans one bounded context's stores plus the shared outbox ([platform#10](https://github.com/mosaic-media/platform/blob/main/docs/adr/0010-storage-authority-and-transaction-scope.md)); work crossing contexts is two transactions joined by an event.

**Events.** Writers append to the outbox inside the business transaction. The worker drains it, publishes through the bus, and marks published or records failure. Failure applies an exponential backoff capped at one hour and dead-letters after eight attempts. Events carry a full envelope: identity, type, timestamps, actor, correlation and causation identifiers, payload, redaction class.

**Migrations.** Embedded, versioned, checksummed. Applied with their tracking row in one transaction. The startup gate fails fast on a missing, checksum-mismatched, gapped, or database-ahead schema.

**Configuration.** Draft → Validated → Active, with Rejected and Superseded terminal paths. At most one Active version, enforced by a unique partial index rather than application logic.

**Shutdown.** Stop the worker's poll loop, run one final synchronous drain, exit. Proven by a test using a one-hour ticker so only the shutdown drain can deliver.

---

## The content model

Four tables — `nodes`, `parts`, `relations`, `source_bindings` — designed in [platform#9](https://github.com/mosaic-media/platform/blob/main/docs/adr/0009-object-graph.md) and [platform#10](https://github.com/mosaic-media/platform/blob/main/docs/adr/0010-storage-authority-and-transaction-scope.md). They are the first content in a schema that was otherwise entirely infrastructure.

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

**`media_type`, `container_type` and `item_type` are unconstrained text; the graph vocabulary is not.** [platform#11](https://github.com/mosaic-media/platform/blob/main/docs/adr/0011-open-and-closed-vocabularies.md) draws the line: vocabulary the Platform *branches on* — `node_kind`, `part_role`, relation types, match methods, statuses — is closed and `CHECK`-constrained, because an unrecognised value there is a traversal that does not know what it is looking at. Vocabulary that only *describes content* is open, because a `CHECK` would make every new media type a schema migration. Open is not unguarded: stores canonicalise on write, so `Anime Series`, `anime-series` and `anime_series` are one media type and not three, and a write returns the canonical value. What normalisation cannot recover — a missing separator, a misspelling — is owed to the `media_types` registry landing with the reference capability. Attribute correctness in the JSONB columns belongs to the writing capability on the same terms.

**Identifiers are UUIDv7 in native `uuid` columns**, with their own generator alongside the UUIDv4 one that continues to serve the infrastructure tables. Those keep their `text`/UUIDv4 ids and are not migrated.

**Three things [platform#9](https://github.com/mosaic-media/platform/blob/main/docs/adr/0009-object-graph.md) leaves open are unbuilt rather than invented:** the fractional ordering scheme at large scale (`natural_order` is stored as given and nothing rebalances), relation confidence decay or reverification (edges are written once, and `RelationStore` has no `Update` so the absence stays visible), and attribute validation.

---

## Supervisor handoff

Five HTTP endpoints, each a thin call into `internal/platform/runtime`:

`/metadata` · `/readyz` · `/healthz` · `/migrations` · `/config`

Readiness is false if any component reports Unavailable; Degraded alone does not block. Liveness goes false once shutdown begins, so an intentional exit is not read as a crash. The Platform never reverses a database mutation — rollback is the Supervisor activating a different Generation.

---

## Testing

`test/contract/` holds an adapter-agnostic suite proving any storage implementation satisfies the contracts. It runs against real PostgreSQL — embedded by default, or dockerised. The PostgreSQL adapter passes the same behavioural tests a future storage adapter would have to pass.

Integration tests run against a real database, not mocks. Application service tests run without PostgreSQL, against contract fakes. Boundary tests parse import declarations rather than grepping text. Where a test could pass by construction, it was verified to fail against a deliberately introduced violation.

**The gate runs in `platform`'s test container, not on the host** — `docker compose -f docker-compose.test.yml run --rm test`, which its CI runs as the same file rather than a transcription. That is not ceremony: the two dependencies that matter most fail *soft*. Without a reachable PostgreSQL the storage contract tests skip and the run still prints `ok`, and without `ffprobe` playback relays unprobed, which is a behaviour change rather than an error. A host-side `go test ./...` therefore passes while testing far less than it appears to.

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
| Transports | Handlers call services, not database packages |
| Diagnostics | Health reporting and support-bundle redaction verified |
| Supervisor | Process exposes readiness, liveness and shutdown behaviour |
| Content model | Tree, graph, parts and bindings pass the contract suite; the four non-uniformities stay expressible |

---

## Not built

Stated plainly so nothing here is mistaken for a description of something real.

This section covers what does not *exist*. Its counterpart is
[Unreachable capability](unreachable-capability.md) — what exists, works, is
tested, and has no way for a human to reach it. That register is the more
dangerous of the two, because nothing in the build or the test suite reports it,
and it is where the current examples live. **Do not copy one here**: the example
this section used to carry was discharged, and went on asserting the opposite for
weeks because a second copy has nothing keeping it honest.

- **IPTV programme listings.** [platform#9](https://github.com/mosaic-media/platform/blob/main/docs/adr/0009-object-graph.md) gives them their own lightweight table keyed to the channel node, deliberately outside the Node machinery. The reasoning is written into the content-model migration as a comment; the table is not.
- **Module-granular permissions.** The policy engine governs *user* authority, and a capability acts as its invoking user ([platform#13](https://github.com/mosaic-media/platform/blob/main/docs/adr/0013-how-a-capability-acts.md)). Authority a module holds *distinct* from that user is scoped to a future record and not built. **The system principal is no longer part of this gap** — background work has a caller of its own and passes the same boundary as everything else.
- **Device pairing.** No backing service.
- **The Mosaic Design Language.** The Shell ships a neutral, token-driven skin; the design language that will replace those token values — acrylic with weight, artwork as the light source — is not built.
