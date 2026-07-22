# Mosaic

The seed document for the rebuilt repository. Everything here is either stated by the owner or drawn from a decision record and marked as inherited. Nothing is inferred.

---

## What Mosaic Is

Mosaic is a self-hosted media server that covers every format in one place — music, television, film, anime, comics, manga, audiobooks — without requiring the user to run three separate systems to get there.

---

## Why It Exists

The self-hosted media ecosystem is fragmented, and each existing tool solves one slice well:

- **Jellyfin** handles local media.
- **Stremio** handles remote on-demand media.
- **SeAnime** handles anime and manga over torrents.

A user who wants all three runs all three. Beyond the fragmentation the ecosystem is bloated, unoptimised and stale.

Mosaic replaces that with one platform, and it has a second goal that shapes the architecture as much as the first: **the user should not feel like their own IT support.** Self-hosting normally means becoming a part-time sysadmin. Mosaic treats that as a product defect rather than an inevitability, which is why the Supervisor exists.

---

## How It Is Built

Mosaic covers every media format, but no user wants every format. That single observation produces most of the architecture.

**The Platform is hexagonal, exposing functionality through ports.** Modules extend Mosaic to new media formats by implementing those ports. This is not architectural purity for its own sake — it is the extension mechanism, and it exists so that the format coverage does not have to be built by one person.

**The Supervisor compiles the Platform Binary**, pulling down the optional modules a user selected. Modules are ordinary Go libraries compiled into a single binary rather than separate processes. This was chosen deliberately: Mosaic should not pay local transport overhead for extensibility. There are no runtime plugins, no dynamic libraries, and no RPC between local modules.

**The SDK exposes the Platform's ports in a lightweight form**, so that the open-source community can build modules against a stable contract without needing to understand the Platform's internals.

**Storage is a single PostgreSQL database.** Content is a node tree with a separate relation graph — links rather than a store — so a new media format maps onto existing structure instead of adding tables. That flexibility is what lets a module introduce a format without touching the schema. There is no second analytical database; DuckDB is not part of Mosaic.

**The interface is server-driven (SDUI)**, and Mosaic is meant to feel premium and like its own product rather than a hobbyist dashboard. The Mosaic Design Language is built on an acrylic material with weight, using artwork as the light source — the media itself illuminates the interface, because the emotional connection people have to their media is the thing worth presenting well.

---

## Decisions

### Confirmed by the owner

These were stated directly and are load-bearing.

| Decision | Reason |
|---|---|
| Self-hosted media server covering all formats | The ecosystem is fragmented across single-purpose tools |
| Supervisor manages the platform | The user should not be their own IT support |
| Hexagonal architecture, functionality exposed as ports | Ports are the module extension mechanism |
| Modules extend media formats; the community builds them | Format coverage cannot be built solo |
| Supervisor compiles modules into one Platform Binary | Avoid local transport overhead |
| SDK exposes ports lightweight | Lower the barrier for community module authors |
| Single PostgreSQL; node tree plus relation graph; links not a store; no DuckDB | Flexibility for new formats without schema change |
| SDUI | Chosen deliberately as the interface model |
| Mosaic Design Language — acrylic with weight, artwork as light source | Premium feel; media carries emotional connection |
| Open source: AGPL-3.0 Platform with a module-linking exception, permissive SDK ([ADR 0022](adr/0022-licensing.md)) | Protect the core from closed-SaaS forks while keeping the module ecosystem open under any license |

### Inherited from prior sessions — needs confirmation

These were recorded before the reset as full decision records with context, alternatives and consequences. They were the only records written in that heavyweight form, which is why they were carried forward rather than deleted. **They have not been confirmed in conversation and should each be accepted, amended or dropped.**

| Record | What it decides |
|---|---|
| [ADR 0001](adr/0001-transactional-store-extensibility.md) | Stores resolved uniformly through a typed accessor rather than named methods; storage behind a `StorageAdapter` port so PostgreSQL can be replaced; the SDK exposes storage for use, not modification |
| [ADR 0002](adr/0002-module-storage-and-delivery-model.md) | A Module is a Go library compiled into the binary; the Platform owns storage and schema; essential and community modules differ only in delivery, not architecture; analytical processing sits behind a port |
| [ADR 0003](adr/0003-platform-as-execution-kernel.md) | The Platform is a runtime, not an application. It owns contracts and orchestration; Modules own business behaviour |
| [ADR 0004](adr/0004-supervisor-as-host-manager.md) | The Supervisor is the always-running host-level manager, sitting below Shell, Platform and Generations |
| [ADR 0005](adr/0005-supervisor-guarantees-an-interface.md) | The Supervisor is the only public entry point and degrades through progressively simpler interfaces rather than disappearing |
| [ADR 0006](adr/0006-supervisor-orchestrates-isolated-builds.md) | The Supervisor orchestrates isolated runtime builds |
| [ADR 0007](adr/0007-static-go-module-composition.md) | Modules are Go libraries compiled into one binary — no plugins, no RPC |
| [ADR 0008](adr/0008-sdk-as-public-contract-language.md) | The SDK is the public contract language between Platform and Modules |
| [ADR 0009](adr/0009-developer-platform-toolchain.md) | The Developer Platform is an integrated toolchain |
| [ADR 0010](adr/0010-test-harness-as-development-modules.md) | The Test Harness is built from development-only Modules |
| [ADR 0011](adr/0011-platform-transports-events.md) | The Platform transports events; Modules own domain events and their names |

ADR 0004 and ADR 0005 are the recorded form of the "not your own IT support" goal. **ADR 0007 is the recorded form of the static-compilation choice**, and therefore the origin of the isolation trade-off below.

---

## Tradeoffs Accepted

Stating these plainly is the point. The previous repository claimed guarantees the architecture cannot deliver, and that is worth not repeating.

**Compiling modules into the binary trades isolation for speed.** Module code is ordinary Go code in the same process as Platform code. There is no runtime boundary, and Go provides no in-process sandbox. A module can reach anything the Platform can reach.

The consequence follows directly: **installing a community module means running arbitrary code with full Platform authority.** Module trust must therefore be established *before* the build — through curation, signing, review, or a distinction between essential and community tiers — because there is no runtime mechanism that will contain a module once it is compiled in.

A permission model is still worth having. It makes authority explicit, auditable and reviewable, and it prevents modules from *accidentally* using facilities they never declared. It is a declaration and accountability mechanism, not containment. Documentation must not describe it as containment.

---

## Controlled Vocabulary

One term meaning several things caused a real failure: an agent building the roadmap invented a module transport layer, because "transport layer" appears throughout the old corpus meaning three unrelated things — the inbound HTTP/GraphQL adapter boundary, light transport in the material system, and module IPC, which is explicitly forbidden.

Each of these words must carry exactly one meaning, everywhere.

| Term | Means | Does not mean |
|---|---|---|
| **Transport** | Reserved. Do not use unqualified. Say *inbound adapter* for HTTP/GraphQL, *light transport* for the material system | Anything to do with modules |
| **Module** | A Go library compiled into the Platform Binary, extending Mosaic | A plugin, an extension, a separate process |
| **Gateway** | Reserved. An *outbound* adaptor exposing Mosaic through a foreign client's protocol (facade); the inverse of an inbound *Module* source. None built (ADR 0043) | An inbound source, or anything Mosaic *consumes* |
| **Stale-while-revalidate** | Serving the last known-good *read* from a snapshot while a fresh one is fetched, then replacing it (ADR 0052) | *Optimistic UI*, which renders a predicted **write** outcome before the server confirms it. Mosaic predicts nothing |
| **Platform** | Mosaic's own code and contracts | The binary; say *Platform Binary* for that |
| **Supervisor** | The component that selects modules, builds the binary and manages the running system | The Platform, or the Runtime |
| **Store** | A typed persistence contract resolved within a transaction | The database |
| **Node tree** | The content-agnostic object model | A filesystem |
| **Single binary** | The Platform Binary the Supervisor compiles Modules into (ADR 0007) | The database, which runs as its own process. "Single binary dropped" referred only to not bundling PostgreSQL |
| **Canon** | Reserved. The database is authoritative (ADR 0014) | `.mos` and NFO, which are exports |
| **Part** | The bytes an item plays, local path or remote reference | A section of a file, or a node |

Add to this table whenever a word starts carrying two meanings. Removing an ambiguity is cheaper than debugging what it generated.

---

## Settled In Code

The `platform` repository has the full critical path standing — a runnable process, the first optional module and its user-managed settings — with two slices built and then reverted under [ADR 0012](adr/0012-capabilities-do-not-own-stores.md). Where code exists, **the code is authoritative** and this repository does not restate it. Questions the old corpus argued about for chapters are already answered:

| Question | Answer, in code |
|---|---|
| Shutdown sequencing | Stop the worker's poll loop, run one final synchronous outbox drain, then exit. Proven by a test that starts a one-hour ticker so only the shutdown drain can deliver |
| Retry and dead-lettering | Exponential backoff capped at one hour, dead-letter after eight attempts, failure bookkeeping recorded per event |
| Delivery semantics | At-least-once. Subscribers must be idempotent; a retry redelivers to every subscriber of that type |
| Error taxonomy | Seven categories — `InvalidArgument`, `Unauthenticated`, `PermissionDenied`, `NotFound`, `Conflict`, `Unavailable`, `Internal`. No driver type escapes a module boundary |
| Command boundary | Validate, authenticate, authorise, open `UnitOfWork`, load, apply, persist state and outbox in one transaction, return a Platform type |
| Storage extensibility | `Tx` names a closed, Platform-owned store set; capabilities own no schema, so there is nothing to register. `StorageAdapter` remains a port. ADR 0012, superseding ADR 0001 |
| Package tiers | Core Platform, built-in module, external module. Postgres is a built-in module, not an adapter |
| User authorisation | Real ABAC-shaped policy engine, default-deny, enforced at the application service |

## Deliberately Undecided

- **Module-granular permissions.** A capability acts as its invoking user ([ADR 0017](adr/0017-how-a-capability-acts.md)), so the acting-principal question is decided. What a *module* may do *differently* from that user — who grants it, whether an operator approves at install, what a declaration commits to — is scoped to its own future ADR, triggered by the first capability that needs authority distinct from its user's.
- **The module manifest's *full* shape**, and whether the declared unit is the module or the capability. The optional-module composition and invocation path now exists — an external-shaped module (the Stremio module) is registered and invoked through a capability registry with a *minimal* `Manifest` ([ADR 0019](adr/0019-module-capability-and-invocation.md), [ADR 0020](adr/0020-optional-module-composition.md)). What the manifest grows to carry (declared permissions, sourced media types) is still open, as is the Supervisor's build-time *selection* of modules.
- **Backpressure thresholds and queue bounds.**
- **The first-administrator injection channel.** The Platform seeds the first admin from environment variables today, as a deliberate bridge ([ADR 0018](adr/0018-first-admin-bootstrap.md)). The eventual owner is Supervisor onboarding, and how it hands the initial credential to the Platform — a `secret://` reference, standard input, one-time material — is left to the work that designs that onboarding flow. `EnsureAdmin` stays the seam; only the channel changes.
- **The public SDK surface** is published, proven and extracted ([ADR 0016](adr/0016-published-contract-surface.md)). It is its own module — [`github.com/mosaic-media/sdk`](https://github.com/mosaic-media/sdk) — carrying the content services, models and an opaque `Caller`, with the store contracts kept internal. `v0.1.0` extracted the content surface; `v0.2.0` adds the `Capability` interface a module implements ([ADR 0019](adr/0019-module-capability-and-invocation.md)); `v0.3.0` adds the `ImportRequest` struct that hands a module its user-managed settings ([ADR 0021](adr/0021-module-settings.md)). The Platform depends on it as an external module; the reference capability imported an anime end to end against a real database, and the first optional module (the Stremio addon source) is now composed in, invoked through the capability registry, and configured at runtime by a user pasting an addon manifest URL. The critical path is complete, and the composition-and-invocation half of the extension story with it.

---

## Rules For This Repository

The previous repository failed for two structural reasons, both diagnosed by the owner. These rules exist to prevent recurrence.

**1. Git is the memory. The working tree is the truth.**

The old repository served two masters — AI memory across sessions, and human source of truth — and those want opposite things. Memory accumulates and records the journey; truth records only the current state. When one artifact does both, memory wins by volume, and abandoned ideas get retrieved as though they were current. That is exactly how a superseded SQLite-and-filesystem model, and a discarded second analytical database, ended up shaping a roadmap.

Superseded content is **deleted, not annotated**. A banner saying "this section is historical" does not outweigh three hundred lines and a diagram saying otherwise. Git retains every abandoned idea permanently, so deleting costs nothing. Where a rejected option matters, it belongs in a decision record's Alternatives section — one paragraph, in the document that supersedes it.

**2. No specification ahead of implementation.**

Roadmaps may look forward. Specifications may not. Documentation written for unbuilt software has nothing pushing back on it, which is how two documents can describe incompatible shutdown sequences indefinitely without anything breaking. Write the specification once the code exists and the specification describes something real.

**3. One authoritative statement per fact.**

If two documents answer the same question, a reader — human or agent — picks one, and the choice is arbitrary. Duplication is a correctness bug, not a tidiness issue.
