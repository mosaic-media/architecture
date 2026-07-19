# Roadmap

Derived from the real state of `mosaic-platform`, not from a plan written ahead of it.

---

## Where the build actually is

Thirteen slices are complete. The Platform boots against real PostgreSQL, serves a GraphQL schema, runs an outbox worker with retry and dead-lettering, resolves secrets, reports component health, shuts down gracefully with a final outbox drain, and holds a content-agnostic object graph. Every slice passes `go build`, `go vet` and `go test -race` against a real database.

Two further slices — uniform store resolution and its PostgreSQL follow-up — were built and then reverted under [ADR 0012](adr/0012-capabilities-do-not-own-stores.md), which found they solved a case the architecture had already ruled out.

The content model was the last thing blocking the critical path. What remains is the thesis test itself.

---

## The critical path

Everything below is one thread. Nothing else should start until it lands, because it is the test of Mosaic's central thesis: **that a developer who is not you can extend Mosaic through the SDK.**

### 1 — The content-agnostic object model — **done**

The node tree and relation graph, designed in [ADR 0013](adr/0013-object-graph.md), with authority and media linking settled in [ADR 0014](adr/0014-storage-authority-and-transaction-scope.md).

`nodes`, `parts`, `relations` and `source_bindings` shipped with domain types, store contracts, PostgreSQL implementations, the four stores added to `Tx`, and adapter-agnostic contract tests against real PostgreSQL. Identifiers are UUIDv7 in native `uuid` columns; the twenty-five infrastructure tables keep their `text`/UUIDv4 ids and were not migrated. ADR 0013's four deliberate non-uniformities each have a contract test, since each is cheap to normalise away by accident.

This was the real blocker, and it had been mistaken for something else. The reference capability was recorded as blocked on an empty `contracts/platform/v1` and a closed `Tx`; both were symptoms of building the extension mechanism before the thing it extends. A capability now has somewhere to put an anime.

**Deliberately not in the slice, and still unbuilt:** export formats, the filesystem projection, streaming, the job queue, `LISTEN/NOTIFY`, and IPTV listings. None blocks the reference capability.

**Carried forward:** no application service commands the graph yet. The reference capability should go through application services rather than reaching for `Tx` itself, so command handlers over the content model are the likely first move in step 2.

### 2 — Reference capability path

Attempted twice and correctly reported as blocked rather than forced.

Its purpose changed under [ADR 0012](adr/0012-capabilities-do-not-own-stores.md). It was to prove a capability could own a store and join a transaction. Since capabilities own no schema, it should now prove what a capability actually does, shaped like the anime module the platform exists to support:

- source metadata from an external provider
- search existing content
- create nodes and relations in the generic model
- publish an event

**Exit criteria.** The proven contracts are promoted into `contracts/platform/v1` *first*, then one capability does all four using only those packages, owning no schema and touching no Platform code.

### 3 — SDK extraction readiness

Whether the contracts proven across the completed slices can leave the Platform repository as a standalone SDK a third party can build against.

**Exit criteria.** Import boundaries are enforced, and the promoted `contracts/platform/v1` surface is confirmed to expose no private Platform internals. This slice *verifies* isolation; it does not populate the surface for the first time — that happens in step 2.

### The stop point

> **The Platform is ready for SDK work when the reference capability uses only published contract packages and no private Platform internals.**
>
> **If the reference capability requires a private import, the contracts are not ready to publish.**

This is the rule to hold the line on. A private import that gets waved through is the moment the ecosystem becomes second-class — the community developer hits a wall the built-in modules never hit, and the extension model quietly stops being real.

**Steps 2 and 3 together are the thesis test.** If a capability can be built entirely against the published contract surface, the module ecosystem works. If it cannot, the extension model needs rethinking — and better to learn that now than after building media formats on top of it.

### Acceptance baseline

Before the foundation is considered ready for SDK extraction:

- `go test ./...` passes
- adapter contract tests pass against real PostgreSQL
- migration tests run from an empty database
- import boundary checks pass
- GraphQL resolver tests prove service routing
- Supervisor health probes pass against a running process

---

## After the thesis holds

Deliberately unplanned in detail. These follow only once the extension mechanism is proven, and each should be scoped when it starts rather than now.

- **First real module** — one media format end to end, built the way a community developer would build it. The first honest test of the SDK's ergonomics.
- **Module permissions** — what a module declares, who grants it, what enforcement means given modules compile into the binary. See the isolation tradeoff in [the overview](index.md); this is a declaration and audit mechanism, not containment.
- **Module distribution** — how the Supervisor discovers, selects and pulls a community module. Manifest shape, signing, trust tiers.
- **Export formats** — NFO for other systems, `.mos` for Mosaic-to-Mosaic portability. Generated on demand from authoritative state ([ADR 0014](adr/0014-storage-authority-and-transaction-scope.md)).
- **Job queue** — the `jobs` tables exist with no service on them. `SELECT ... FOR UPDATE SKIP LOCKED` is the intended pattern, for import, provider sync and enrichment.
- **`LISTEN`/`NOTIFY`** — an accelerator over the outbox worker's existing poll, not a replacement for it. Notifications are dropped when no listener is connected, so the poll stays as the floor.
- **Shell and SDUI** — the server-driven interface.
- **Mosaic Design Language** — acrylic with weight, artwork as the light source.

---

## Working rules

- **One slice at a time**, in order, each passing its gate before the next begins.
- **Report blockers, do not force past them.** The reference capability slice was stopped twice and reported instead of bodged. That was correct both times, and it is why the fix was a design decision rather than a workaround buried in code.
- **Code is authoritative where code exists.** Documentation describes what is built; it does not specify what is not.
- **When implementation contradicts a specification, the specification is wrong.** Fix it there, in the same session, rather than carrying a correction in a repository-local note.
