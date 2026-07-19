# Roadmap

Derived from the real state of `mosaic-platform`, not from a plan written ahead of it.

---

## Where the build actually is

The Platform boots against real PostgreSQL, serves a GraphQL schema, runs an outbox worker with retry and dead-lettering, resolves secrets, reports component health, shuts down gracefully with a final outbox drain, holds a content-agnostic object graph, and exposes a content command and query API over that graph. That API's surface is now published in `contracts/platform/v1` — the models, the nine services, the `ContentService` interface and an opaque `Caller` — and an external module compiles against it in the test suite. Every slice passes `go build`, `go vet` and `go test -race` against a real database.

Two further slices — uniform store resolution and its PostgreSQL follow-up — were built and then reverted under [ADR 0012](adr/0012-capabilities-do-not-own-stores.md), which found they solved a case the architecture had already ruled out.

The content model, its published surface, and a capability that uses only that surface have all landed — **the thesis test passes.** What remains is extracting the surface into a standalone SDK repository a third party builds against.

---

## The critical path

Everything below is one thread. Nothing else should start until it lands, because it is the test of Mosaic's central thesis: **that a developer who is not you can extend Mosaic through the SDK.**

### 1 — The content-agnostic object model — **done**

The node tree and relation graph, designed in [ADR 0013](adr/0013-object-graph.md), with authority and media linking settled in [ADR 0014](adr/0014-storage-authority-and-transaction-scope.md).

`nodes`, `parts`, `relations` and `source_bindings` shipped with domain types, store contracts, PostgreSQL implementations, the four stores added to `Tx`, and adapter-agnostic contract tests against real PostgreSQL. Identifiers are UUIDv7 in native `uuid` columns; the twenty-five infrastructure tables keep their `text`/UUIDv4 ids and were not migrated. ADR 0013's four deliberate non-uniformities each have a contract test, since each is cheap to normalise away by accident.

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

### 4 — SDK extraction readiness

Whether the contracts proven across the completed slices can leave the Platform repository as a standalone SDK a third party can build against.

**Exit criteria.** Import boundaries are enforced, and the promoted `contracts/platform/v1` surface is confirmed to expose no private Platform internals. This slice *verifies* isolation; it does not populate the surface for the first time — that happens in step 3.

The standing check is the one ADR 0016 makes an enforcement: a throwaway module compiled against the published package builds only if the surface is importable and self-contained, so an `internal/` leak fails the build rather than being rediscovered by hand.

### The stop point — cleared

> **The Platform is ready for SDK work when the reference capability uses only published contract packages and no private Platform internals.**
>
> **If the reference capability requires a private import, the contracts are not ready to publish.**

The reference capability landed against `contracts/platform/v1` alone, enforced by a boundary test that parses its imports. It needed no private import, so the line held rather than being waved through — which is what makes the surface ready to extract.

**Step 3 was the thesis test, and it passed.** A capability can be built entirely against the published contract surface. Step 4 confirms the surface can leave this repository as that same standalone thing a third party depends on.

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
