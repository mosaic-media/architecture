# Roadmap

Derived from the real state of `mosaic-platform`, not from a plan written ahead of it. Supersedes MRM-001.

---

## Where the build actually is

Fourteen slices are complete. The Platform boots against real PostgreSQL, serves a GraphQL schema, runs an outbox worker with retry and dead-lettering, resolves secrets, reports component health, and shuts down gracefully with a final outbox drain. Every slice passes `go build`, `go vet` and `go test -race` against a real database.

Two slices remain in the foundation sequence, and both are blocked behind one piece of unfinished work.

---

## The critical path

Everything below is one thread. Nothing else should start until it lands, because it is the test of Mosaic's central thesis: **that a developer who is not you can extend Mosaic through the SDK.**

### 1 — Finish the MAD-001 migration

The additive half landed: `Store[T](tx)` and the `StorageAdapter` port exist. The subtractive half has not, and until it does the store-resolution mechanism is a delegation shim over the accessors it was meant to replace.

- Seal `Tx` into an opaque marker — remove the six accessors from `internal/platform/contracts/unit_of_work.go`.
- Repoint `resolveStore` off those accessors onto the `StorageAdapter`'s live-transaction binding. This is the single place that changes; `Store[T]`'s signature and every call site stay byte-for-byte identical.
- Migrate the seven command handlers still calling `tx.Foo()` — `create_local_user`, `authenticate_local_user`, `revoke_session`, `set_user_status`, `draft_config_version`, `validate_config_version`, `activate_config_version` — plus the GraphQL package's test fake.
- Populate `contracts/platform/v1`, currently `doc.go` and nothing else.

MAD-001 rated this high blast radius and it is. It is also the gate on everything after it.

### 2 — Reference capability path

Already attempted twice and correctly reported as blocked rather than forced. A minimal capability built against *only* `contracts/platform/v1` failed because that package is empty and because `Tx` was closed — a capability had no way to join a transaction without editing Core Platform on its own behalf, violating the rule that the Runtime should require no modification to support a new capability.

Step 1 removes both walls. This slice then proves a capability can own a store, join a transaction, and persist atomically without touching Platform code.

**Exit criteria.** The proven contracts are promoted into `contracts/platform/v1` *first*, then one non-media capability proves the registration and persistence path using only those packages.

### 3 — SDK extraction readiness

Whether the contracts proven across slices 1–14 can leave the Platform repository as a standalone SDK a third party can build against.

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
- **Shell and SDUI** — the server-driven interface.
- **Mosaic Design Language** — acrylic with weight, artwork as the light source.

---

## Working rules

- **One slice at a time**, in order, each passing its gate before the next begins.
- **Report blockers, do not force past them.** The reference capability slice was stopped twice and reported instead of bodged. That was correct both times, and it is why the fix was a design decision rather than a workaround buried in code.
- **Code is authoritative where code exists.** Documentation describes what is built; it does not specify what is not.
- **When implementation contradicts a specification, the specification is wrong.** Fix it there, in the same session, rather than carrying a correction in a repository-local note.
