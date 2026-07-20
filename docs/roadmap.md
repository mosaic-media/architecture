# Roadmap

Derived from the real state of `mosaic-platform`, not from a plan written ahead of it.

---

## Where the build actually is

The Platform boots against real PostgreSQL, serves a GraphQL schema, runs an outbox worker with retry and dead-lettering, resolves secrets, reports component health, shuts down gracefully with a final outbox drain, holds a content-agnostic object graph, and exposes a content command and query API over that graph. That API's surface has been extracted into a standalone SDK module — [`github.com/mosaic-media/mosaic-sdk`](https://github.com/mosaic-media/mosaic-sdk), published at `v0.3.0`, holding the models, the nine services, the `ContentService` interface, the `Capability` interface a module implements, and an opaque `Caller` — which the Platform, the reference capability and the first optional module depend on as an external module. Every slice passes `go build`, `go vet` and `go test -race` against a real database.

The repositories are public and licensed ([ADR 0022](adr/0022-licensing.md)): the Platform under AGPL-3.0 with a module-linking exception, the SDK under Apache-2.0, optional modules under their authors' choice (the first is MIT), and this documentation under CC-BY-4.0.

Two further slices — uniform store resolution and its PostgreSQL follow-up — were built and then reverted under [ADR 0012](adr/0012-capabilities-do-not-own-stores.md), which found they solved a case the architecture had already ruled out.

The content model, its published surface, a capability that uses only that surface, and the surface's extraction into a standalone SDK module have all landed — **the thesis test passes and the critical path is complete.** Since then the first optional module (the **Stremio** addon source) has been composed into the binary and invoked through a capability registry, so the composition-and-invocation half of the extension story works too ([ADR 0019](adr/0019-module-capability-and-invocation.md), [ADR 0020](adr/0020-optional-module-composition.md)). The Shell — a Server-Driven-UI client in its own repository ([ADR 0023](adr/0023-server-driven-ui-and-the-shell.md), [ADR 0024](adr/0024-primitives-and-definitions.md)) — is built too, though the Platform does not yet emit the screens it renders. What follows (a second module, media formats, module distribution, the Platform's SDUI surface) builds on a foundation that is proven rather than assumed.

---

## The critical path

Everything below is one thread. Nothing else should start until it lands, because it is the test of Mosaic's central thesis: **that a developer who is not you can extend Mosaic through the SDK.**

### 1 — The content-agnostic object model — **done**

The node tree and relation graph, designed in [ADR 0013](adr/0013-object-graph.md), with authority and media linking settled in [ADR 0014](adr/0014-storage-authority-and-transaction-scope.md).

`nodes`, `parts`, `relations` and `source_bindings` shipped with domain types, store contracts, PostgreSQL implementations, the four stores added to `Tx`, and adapter-agnostic contract tests against real PostgreSQL. Identifiers are UUIDv7 in native `uuid` columns; the existing infrastructure tables keep their `text`/UUIDv4 ids and were not migrated. ADR 0013's four deliberate non-uniformities each have a contract test, since each is cheap to normalise away by accident.

This was the real blocker, and it had been mistaken for something else. The reference capability was recorded as blocked on an empty `contracts/platform/v1` and a closed `Tx`; both were symptoms of building the extension mechanism before the thing it extends. A capability now has somewhere to put an anime.

**Deliberately not in the slice, and still unbuilt:** export formats, the filesystem projection, streaming, the job queue, `LISTEN/NOTIFY`, and IPTV listings. None blocks the reference capability.

### 2 — Content commands and queries — **done**

The stores existed and were proven, but nothing above them did. No application service touched the graph, so the only way in was `Tx`, which the composition root holds — and a capability reaching for `Tx` directly would bypass the policy engine entirely.

This slice put the command order over the content model. Nine application services now exist, each validating, authenticating, authorising and — for writes — committing state and an outbox event in one transaction:

- **Reads:** `SearchContent` (title substring, media type, kind), `FindContentByExternalID` (provider id against the GIN index), `GetContentNode` (one node, optionally its direct children). Before this, `FindBySource` answered only *"have I bound this exact provider reference?"*; "do I already have this anime?" by title or external id was unanswerable, and the `nodes_external_ids_gin` and `nodes (media_type, title)` indexes had no query reaching them.
- **Writes:** `AddContentWork`, `AddContentChild`, `AttachContentPart` build the containment tree; `RelateContent`, `BindContentSource`, `ResolveContentBinding` write the association graph and resolve identity.

Two shapes were decided in the building. A child inherits its work id and media type from its parent, so a season cannot declare a different media type than its series. A binding is created confirmed or pending-review, never rejected — rejection is a resolution of an existing binding, not a state to create one in.

It was scheduled ahead of the reference capability because it is needed under every resolution of the boundary problem below, so none of it could be wasted. It did **not** resolve either blocker: every content command still authorises on a user session, and the contracts still reference `domain` types under `internal/`.

### 3 — Reference capability path — **done**

Attempted twice and correctly reported as blocked rather than forced, then blocked a third time on two things neither attempt had reached — both decided (ADR 0016, ADR 0017) and built. The capability now exists and passes: **the thesis holds.** A package that imports only `contracts/platform/v1`, owns no schema and touches no Platform internals sources an anime over HTTP, searches by provider id to avoid duplicating, creates the work with a source binding, builds its season/episode/part tree, and — honouring ADR 0013 — creates the source manga as its own Work joined by an adaptation edge rather than folding it into one tree. It runs against real PostgreSQL through the postgres harness: a fake provider serves canned metadata over `httptest`, and the test asserts the work is findable by external id, the tree is where it belongs, the edge and both bindings landed, every command emitted its event, and a second import is idempotent.

`capabilities/reference/` lives outside `internal/` and a boundary test parses its imports to keep it to `v1` and the standard library — the stop point made executable. It owns its provider integration outright (an HTTP metadata source on `net/http`), since the Platform offers no HTTP contract and does not need to (ADR 0007).

Two findings from building it. The published surface was **sufficient** — no private import was needed, which is the proof the contracts are ready. And one gap: `ContentService` has no *read* for relations (`ListFrom`/`ListTo`), so the test reads the adaptation edge through the store; the capability's own flow does not need it, so it is a candidate addition to `v1`, not a blocker.

The remainder of this section records how the block was cleared.

#### Done: the published surface ([ADR 0016](adr/0016-published-contract-surface.md))

The block was that every contract signature references a `domain` type under `internal/`, which Go forbids an external module from importing. The fix corrected the roadmap's own framing: a capability does **not** call the store contracts (`NodeStore`, `Tx`, `StorageAdapter`) — those are Platform↔engine plumbing. It calls the application-service API.

`contracts/platform/v1` now holds that surface: the content models (moved out of `internal/platform/domain`, not duplicated), the nine content command, query and result types, the `ContentService` interface `app.Service` implements, and an opaque `Caller`. The store contracts and the identity and configuration models stayed internal. The enforcement is a standing test — `test/sdkprobe` is a separate Go module that imports only `v1` and exercises the whole service; `test/sdkboundary` builds it, and because an external module cannot import `internal/`, a public signature that leaked an internal type fails that build. Verified by watching it fail on a deliberately added internal import.

#### Decided: how a capability acts ([ADR 0017](adr/0017-how-a-capability-acts.md))

A capability does not originate authority. The Platform invokes it within a context carrying a principal, and it forwards that context to every service it calls. For the reference capability the principal is the invoking user, so nothing in the policy engine changes and every created node traces to the person who caused it. This is realised as the `Caller`: a session reference the capability forwards, only as authoritative as the session behind it. A system principal for background work, and module-granular authority, are named future decisions rather than machinery built now.

#### How the block was cleared

Its purpose changed under [ADR 0012](adr/0012-capabilities-do-not-own-stores.md). It was to prove a capability could own a store and join a transaction. Since capabilities own no schema, it proves instead what a capability actually does, shaped like the anime module the platform exists to support: source metadata from an external provider, search existing content, create nodes and relations, and cause events. All four are done.

Sourcing metadata needs no Platform HTTP contract, which is worth stating because it looks like a gap and is not one. Capabilities compile into the binary with trust established before the build ([ADR 0007](adr/0007-static-go-module-composition.md)), so a capability imports `net/http` itself — as the reference capability's metadata source does. A Platform-provided client is worth having eventually for rate limiting and secret handling; it is not a prerequisite.

#### Not carried here after all: the `media_types` registry

The original plan ([ADR 0015](adr/0015-open-and-closed-vocabularies.md)) had this slice carry the registry that catches a media type which was never real (a missing separator or a misspelling, which normalisation cannot recover). It did not, and ADR 0015 is amended to say why: the reference capability is an anime importer that uses only known media types, so it never introduces a novel one, and the registry depends on the capability manifest shape, which is still undecided. The registry now waits on that manifest mechanism and on a capability that genuinely introduces a new type. Until then normalisation is the whole of the enforcement.

**Exit criteria — met.** The surface of [ADR 0016](adr/0016-published-contract-surface.md) is published into `contracts/platform/v1`, and one capability does all four using only those packages, acting as its invoking user ([ADR 0017](adr/0017-how-a-capability-acts.md)), owning no schema and touching no Platform code.

### 4 — SDK extraction — **done**

Whether the contracts proven across the completed slices can leave the Platform repository as a standalone SDK a third party can build against. They can, and they have: the surface is now its own module, [`github.com/mosaic-media/mosaic-sdk`](https://github.com/mosaic-media/mosaic-sdk), published at `v0.1.0`.

`contracts/platform/v1` moved out of the Platform repository into the SDK module unchanged, and the Platform now depends on it as an ordinary tagged dependency — no `replace` directive, so a fresh clone resolves it through the module proxy. Several separate modules build against the published SDK: the Platform, the reference capability, `test/sdkprobe`, and the Stremio module in its own repository. The surface holds no private Platform internals, because Go itself now forbids it — an external module cannot import the Platform's `internal/`, so a leak would fail to compile rather than needing a test to catch it.

**Exit criteria — met.** The surface left the repository as a standalone module, and the Platform and the reference capability build against it as external consumers.

The SDK is pre-1.0 deliberately (now at `v0.3.0`) and may still change. The relation-read gap noted in step 3, and any surface a second capability turns out to need, are the kind of change a `v0.x` bump absorbs before the surface is declared stable.

### The stop point — cleared

> **The Platform is ready for SDK work when the reference capability uses only published contract packages and no private Platform internals.**
>
> **If the reference capability requires a private import, the contracts are not ready to publish.**

The reference capability landed against `contracts/platform/v1` alone, enforced by a boundary test that parses its imports. It needed no private import, so the line held rather than being waved through — which is what makes the surface ready to extract.

**Step 3 was the thesis test, and it passed; step 4 extracted the surface it proved.** A capability can be built entirely against the published contract surface, and that surface is now a standalone module a third party depends on rather than a package inside this repository. The extension model is real, end to end.

### Since the thesis: the platform runs

Beyond the critical path, the Platform is now a usable process rather than only a tested library:

- **GraphQL is served over HTTP** — a hand-written handler on `:8081/graphql` (Supervisor handoff stays on `:8080`), and the composition root constructs `app.Service` for the first time. Content is exposed: search, node read, external-id lookup, and the six content mutations, each projecting the published SDK's models.
- **Real password auth** — an Argon2id hasher (`internal/adapters/crypto`), so sign-in actually verifies.
- **Permissions can be assigned through the Platform** — `PermissionStore` gained `CreateRole`/`GrantRole`, with commands and GraphQL mutations. `PermissionStore` was read-only before; authority could only be seeded by raw SQL.
- **The first admin bootstraps itself** — `bootstrap.EnsureAdmin`, env-gated and idempotent, so a human can start the binary and use it ([ADR 0018](adr/0018-first-admin-bootstrap.md), a deliberate bridge until Supervisor onboarding owns it). Proven end to end over HTTP against real PostgreSQL: sign in with a password, import a work and a season, query them back.

### Acceptance baseline

Before the foundation is considered ready for SDK extraction:

- `go test ./...` passes
- adapter contract tests pass against real PostgreSQL
- migration tests run from an empty database
- import boundary checks pass
- GraphQL resolver tests prove service routing
- Supervisor health probes pass against a running process

---

## What is next

The critical path is complete and the platform runs. The first optional module has since landed (below); the remaining threads run around it. **The active thread is the one immediately below — modules as typed providers — decided in ADRs and not yet built.** The others (hardening, the rest of the module system, exports, jobs) run around it.

### The active thread: modules as typed providers, and two content planes — **backend done (slices 1–3); SDUI remaining (slice 4)**

Building the Stremio module against real addons showed the module contract is too narrow. A `Capability` today is a single write verb, `Import(query)` ([ADR 0019](adr/0019-module-capability-and-invocation.md)), which forces the caller to already hold a raw provider id (`movie/tt1254207`). But a Stremio addon is a *set of resources* — `meta`, `catalog`, `catalog/…/search`, `stream` — and the product needs all of them: a user should search Mosaic and have it use the module with **no raw ids**, an admin should browse the module's **collections** and pick which to publish as library, metadata should **enrich** existing nodes, and streams should attach to published items. And browsing a source must **not** flood the object graph — a source exposes far more than anyone curated.

Two decisions answer this, written ahead of the build (unusually) and now **Accepted** as slices 1–3 have landed:

- **[ADR 0027](adr/0027-modules-as-typed-capability-providers.md) — modules as typed capability providers.** The module contract becomes declared **provider roles**, one per resource kind: `MetadataProvider`, `SearchProvider`, `CatalogProvider`, `StreamProvider`. A module implements only the roles it fills and declares them in a new `Manifest.Provides []Role` — the manifest-shape growth [ADR 0019](adr/0019-module-capability-and-invocation.md) predicted, and what the `media_types` registry ([ADR 0015](adr/0015-open-and-closed-vocabularies.md)) has waited on. The Platform holds a **provider registry keyed by role**; that registry is the seam other modules will resolve through. Per the design call: the contract *supports* module-to-module use, but only the Platform resolves through it in this slice (build platform-first). `Import` survives, narrowed to "materialize *this* virtual result."
- **[ADR 0028](adr/0028-virtual-and-materialized-content.md) — virtual browse and materialized library.** Content exists in two planes. The **virtual plane** is what a provider returns on read — `SearchResult`/`CatalogItem` DTOs, never persisted; browsing is a read. The **materialized plane** is the object-graph library, written only by an explicit **curated act** (an admin publishing a collection, a user picking a search result), which reuses the existing import path. Streams **snapshot onto the curated set** (bounded by curation, so safe). Search is a **union** of providers + local library, deduped by source binding, each row marked *in library* vs *virtual*. This answers "don't overwhelm the DB" structurally: uncurated content never reaches a store.

**Build sequence — pick the lowest unbuilt slice; each passes `go build`/`go vet`/`go test -race` before the next:**

1. **SDK `v0.4.0` — done.** The four provider interfaces, the `SearchResult`/`CatalogItem` virtual DTOs, `Manifest.Provides`, and the import verb narrowed to a `ContentRef`. Published at `mosaic-sdk` `v0.4.0`, no `replace`.
2. **Stremio providers — done.** All four roles implemented in `mosaic-module-stremio` (`v0.2.0`): `meta`/`stream` moved behind `MetadataProvider`/`StreamProvider`, and the `catalog` + `catalog/…/search` paths added. (Two blocking addon-reachability bugs were fixed first — manifest-URL normalisation and a User-Agent, without which Cloudflare-fronted addons 403'd.)
3. **Platform — done.** A `CapabilityRegistry` that resolves providers by role (and verifies declared roles at boot); `SearchAvailableContent` fans out to every `SearchProvider` and unions with the library, marking each result in-library by source binding; `ListModuleCatalogs`/`ListCatalogItems` browse a module's collections; `ImportContent` narrowed to materialise a `ContentRef`. GraphQL: `searchAvailableContent`, `moduleCatalogs`, `catalogItems`, and a ref-input `importContent`. Green against real PostgreSQL.
4. **SDUI screens — remaining.** The **user search screen** and the **admin collection browser** are the *first real screens the Platform emits* ([ADR 0023](adr/0023-server-driven-ui-and-the-shell.md)), so this converges with the SDUI emit-side below; build the emit-side against [`mosaic-sdui`](https://github.com/mosaic-media/mosaic-sdui)'s Go producer binding and point the Shell at real payloads. The GraphQL those screens read (search, browse-catalogs, materialise) now exists from slice 3.

**Two seams left open on purpose** (named, not answered — an agent hitting them should stop and decide, not invent):

- **Provider precedence** — which provider wins when several fill one role. Moot with one module; belongs with cross-module use.
- **Cross-module authority and the system principal** — whose authority a module-to-module call carries, and the no-user identity background enrichment needs ([ADR 0017](adr/0017-how-a-capability-acts.md)'s reserved gap, shared with module-declared jobs).

### The first optional module — **done**

An **official optional module** is built exactly as a third-party module would be — its own Go module, importing only the SDK and nothing of the Platform's, compiled into the binary and invoked by the Platform. "Official" describes only its authorship (the Mosaic team), not its shape; the discipline is the point, because building it the third-party way is what proves the third-party way exists. It shipped as the **Stremio addon-source module** (movies and TV), not the anime module first sketched here — because the reference capability is *already* an anime importer, so a second anime consumer would only re-walk the same shape, whereas a different media type stresses the surface from a fresh angle and is the first thing to exercise [ADR 0014](adr/0014-storage-authority-and-transaction-scope.md)'s `RemoteLocation` Part path.

The reference capability already proved the *authoring* half — a package can be written against the SDK alone and drive `ContentService`. This slice built the *composition and invocation* half, which did not exist:

- **A capability/registration surface in the SDK** (a `v0.2.0` addition, since evolved to `v0.3.0` — see the settings gap below). ADR 0008 always reserved "capability interfaces" and "module registration APIs" for the SDK, but ADR 0016 populated only the content services. The shape: a `Capability` interface a module implements — `Manifest()` plus `Import(ctx, ContentService, ImportRequest)` — and a minimal `Manifest`.
- **A capability registry and an `ImportContent` command in the Platform.** The composition root registers each module's capability; a generic `importContent(capabilityId, query)` command authenticates and authorises the caller, then invokes the named capability, forwarding that caller so the module acts as its invoking user ([ADR 0017](adr/0017-how-a-capability-acts.md)) and passing the Platform itself as the `ContentService`.
- **The GraphQL `importContent` mutation** over that command, so a user triggers an import over the served API.
- **Static composition** ([ADR 0007](adr/0007-static-go-module-composition.md)): the composition root imports the module and registers it, standing in for the Supervisor's eventual build-time module *selection*. **Not blocked on the Supervisor** — the mechanism of how a module plugs in is what this defines; the Supervisor automating *which* modules is later.

**Approach: a walking skeleton.** Build the thinnest real vertical end to end — SDK surface → a separate module → static composition → one invocation → real content in PostgreSQL — deciding shapes in code, then capturing what solidifies as ADRs (the module capability/invocation contract, and the composition model), written retrospectively once the code settles rather than as an RFC first.

**Invocation model:** the Platform invokes a *registered capability*. The module depends only on the SDK; the Platform owns the invocation surface and routes to it. The alternative — a module contributing its own GraphQL — was rejected because a third party can't import the Platform's transport without breaking the SDK-only boundary. Captured in [ADR 0019](adr/0019-module-capability-and-invocation.md) and [ADR 0020](adr/0020-optional-module-composition.md), written after the code settled.

**Resource-aware, so streams do not gate metadata.** The module uses whatever resources each configured addon declares (Stremio's `meta`, `stream`, …). Metadata creates the Work and its season/episode tree with an external-id binding; streams attach a `RemoteLocation` Part. The two are independent — a meta-only addon yields metadata with *no* Parts, so a user can enrich local media through Stremio addons without adopting remote streaming.

**Deliberately still deferred by this slice:** the full manifest shape (starts minimal, grows), the `media_types` registry (the Stremio module uses known media types), module-granular permissions (it acts with the invoking user's authority), and play-time stream *resolution*/transcoding (the future Remote Media module — the Stremio module only snapshots a stream location). Those remain future work below.

**Modules are the forcing function for the SDK.** Building the Stremio module is how the SDK's gaps get found. Two are identified so far:

- **User-managed module settings — done ([ADR 0021](adr/0021-module-settings.md)).** A user adds a Stremio addon by manifest URL at runtime rather than by an env var at composition time. A Platform-owned `ModuleSettingsStore` (one jsonb document per module id), generic `configureModule`/`moduleSettings` commands and GraphQL, and SDK `v0.3.0` handing a module its settings through `ImportRequest`. Retired the `MOSAIC_STREMIO_ADDONS` bridge.
- **Module-declared cron/jobs — identified, not built.** A module needs to register recurring work the Platform runs (cleanup, periodic refresh). This converges three deferred pieces at once: the jobs runner (tables exist, no service), a scheduler/recurrence layer (none), and the **system principal** ([ADR 0017](adr/0017-how-a-capability-acts.md)'s named gap — a no-user job has no session to forward). It is the "Background work" thread below, now with a concrete trigger.

**Harden the SDK toward stable (it is pre-1.0 on purpose, now `v0.3.0`), in parallel or alongside:**

- **The relation-read gap.** `ContentService` can write edges (`RelateContent`) but has no `ListFrom`/`ListTo` to read them, so a capability can't query the graph it builds. Small and additive — a `v0.x` bump. The most self-contained next thing.
- **A second capability** — a different media type (music, comics), built against the SDK, to stress the surface from a fresh angle and surface what a real second consumer needs before the surface stabilises. Likely forces the relation-read gap and, if it introduces a novel media type, the `media_types` registry.

**The rest of the module system** (the slice above starts it; these follow):

- **The full capability manifest shape.** The module slice starts it minimal (id, version, name) and grows it as needs appear — permissions a module declares, media types it sources, whatever the Supervisor's onboarding surfaces.
- **The `media_types` registry** ([ADR 0015](adr/0015-open-and-closed-vocabularies.md)) — catches a media type that was never real, which normalisation cannot. Waits on the manifest shape and on a module that introduces a new type (the Anime module does not).
- **Module-granular permissions and a system principal** ([ADR 0017](adr/0017-how-a-capability-acts.md)) — authority a module holds distinct from its invoking user, and a no-user identity for background work. (User permissions management is built, and the module slice acts with the invoking user's authority.)
- **Module distribution** — how a community module is discovered, selected and pulled: signing, trust tiers, and the Supervisor's build-time selection on top of the static composition the module slice defines.

**The rest, unplanned in detail, each scoped when it starts:**

- **Export formats** — NFO for other systems, `.mos` for Mosaic-to-Mosaic portability, generated on demand from authoritative state ([ADR 0014](adr/0014-storage-authority-and-transaction-scope.md)).
- **Job queue** — the `jobs` tables exist with no service; `SELECT ... FOR UPDATE SKIP LOCKED` is the intended pattern, for import, provider sync and enrichment.
- **`LISTEN`/`NOTIFY`** — an accelerator over the outbox worker's poll, not a replacement; notifications drop when no listener is connected, so the poll stays the floor.
- **The Platform's SDUI surface** — the server half of the server-driven interface. The client half exists: [`mosaic-shell`](https://github.com/mosaic-media/mosaic-shell) is a React/TypeScript/Vite Server-Driven-UI client ([ADR 0023](adr/0023-server-driven-ui-and-the-shell.md)) whose whole component set is primitives + `ComponentDefinition` data ([ADR 0024](adr/0024-primitives-and-definitions.md)), on a neutral token-driven skin, technology-agnostic so a future Flutter client renders the same payloads. The shared contract also has a home now — [`mosaic-sdui`](https://github.com/mosaic-media/mosaic-sdui), JSON Schema plus a Go producer binding, the standard definitions and the tokens ([ADR 0025](adr/0025-sdui-contract-repository.md)) — so the Platform and Modules build screens against typed Go; the web renderer is a shared package, [`mosaic-sdui-react`](https://github.com/mosaic-media/mosaic-sdui-react) ([ADR 0026](adr/0026-react-sdui-runtime.md)), and a live component storybook ([`mosaic-storybook`](https://github.com/mosaic-media/mosaic-storybook)) documents it at [mosaic-media.github.io/mosaic-storybook](https://mosaic-media.github.io/mosaic-storybook/). What is unbuilt is the server actually emitting screens and their queries — until it does, the Shell runs on mock payloads. This is the human-facing surface everything built to date has lacked, the Platform being reachable only through the GraphQL API. **The first screens to emit are named by the active thread above** — the user search screen and the admin collection browser ([ADR 0028](adr/0028-virtual-and-materialized-content.md)) — so the emit-side lands as step 4 of that thread rather than as a separate greenfield effort.
- **Mosaic Design Language** — the values that replace the Shell's neutral tokens: acrylic with weight, artwork as the light source.

---

## Working rules

- **One slice at a time**, in order, each passing its gate before the next begins.
- **Report blockers, do not force past them.** The reference capability slice was stopped twice and reported instead of bodged. That was correct both times, and it is why the fix was a design decision rather than a workaround buried in code.
- **Code is authoritative where code exists.** Documentation describes what is built; it does not specify what is not.
- **When implementation contradicts a specification, the specification is wrong.** Fix it there, in the same session, rather than carrying a correction in a repository-local note.
