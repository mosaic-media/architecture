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

**Modules come in two tiers, and only one of them is compiled in** ([architecture#3](adr/0003-two-module-tiers.md)). A **core module** is an ordinary Go library linked into the Platform Binary — no plugin, no dynamic library, no RPC — which is how the formats every install needs avoid paying local transport overhead for extensibility. An **extension module** is its own repository and its own release, installed by a user at runtime from a signed index and run **out of process** behind a harness ([platform#39](https://github.com/mosaic-media/platform/blob/main/docs/adr/0039-extension-module-boundary.md), [platform#51](https://github.com/mosaic-media/platform/blob/main/docs/adr/0051-extension-installation-is-user-initiated-and-persistent.md)). A module is written the same way for either tier; the tier is a delivery and coupling decision, not a contract one.

**CI builds the Platform Binary from a version tag**, cross-compiled with checksums, rather than assembling it on the user's machine ([platform#38](https://github.com/mosaic-media/platform/blob/main/docs/adr/0038-platform-binary-built-by-ci.md), superseding [platform#4](https://github.com/mosaic-media/platform/blob/main/docs/adr/0004-static-go-module-composition.md)'s build sequence). The Supervisor's half of that — downloading, verifying and activating a release — is decided and does not exist. Installed extensions are the **Platform's** to discover, verify and manage, not the Supervisor's ([platform#49](https://github.com/mosaic-media/platform/blob/main/docs/adr/0049-the-platform-manages-extension-modules.md)).

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
| Core modules compiled into one Platform Binary, which CI builds ([platform#38](https://github.com/mosaic-media/platform/blob/main/docs/adr/0038-platform-binary-built-by-ci.md)) | Avoid local transport overhead. The extension tier pays that cost deliberately, in exchange for a process boundary ([architecture#3](adr/0003-two-module-tiers.md)) |
| SDK exposes ports lightweight | Lower the barrier for community module authors |
| Single PostgreSQL; node tree plus relation graph; links not a store; no DuckDB | Flexibility for new formats without schema change |
| SDUI | Chosen deliberately as the interface model |
| Mosaic Design Language — acrylic with weight, artwork as light source | Premium feel; media carries emotional connection |
| Open source: AGPL-3.0 Platform with a module-linking exception, permissive SDK ([architecture#1](adr/0001-licensing.md)) | Protect the core from closed-SaaS forks while keeping the module ecosystem open under any license |

### Inherited from prior sessions — needs confirmation

These were recorded before the reset as full decision records with context, alternatives and consequences. They were the only records written in that heavyweight form, which is why they were carried forward rather than deleted. **They were never confirmed in conversation, and each should be accepted, amended or dropped.**

The column below says what each one *decides*, not where it stands. **Several have since been superseded, wholly or in part, and each record's own Status line is the authoritative account of that** — read it there rather than inferring currency from this table.

| Record | What it decides |
|---|---|
| [platform#1](https://github.com/mosaic-media/platform/blob/main/docs/adr/0001-transactional-store-extensibility.md) | Stores resolved uniformly through a typed accessor rather than named methods; storage behind a `StorageAdapter` port so PostgreSQL can be replaced; the SDK exposes storage for use, not modification |
| [platform#2](https://github.com/mosaic-media/platform/blob/main/docs/adr/0002-module-storage-and-delivery-model.md) | A Module is a Go library compiled into the binary; the Platform owns storage and schema; essential and community modules differ only in delivery, not architecture; analytical processing sits behind a port |
| [platform#3](https://github.com/mosaic-media/platform/blob/main/docs/adr/0003-platform-as-execution-kernel.md) | The Platform is a runtime, not an application. It owns contracts and orchestration; Modules own business behaviour |
| [supervisor#1](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0001-supervisor-as-host-manager.md) | The Supervisor is the always-running host-level manager, sitting below Shell, Platform and Generations |
| [supervisor#2](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0002-supervisor-guarantees-an-interface.md) | The Supervisor is the only public entry point and degrades through progressively simpler interfaces rather than disappearing |
| [supervisor#3](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0003-supervisor-orchestrates-isolated-builds.md) | The Supervisor orchestrates isolated runtime builds |
| [platform#4](https://github.com/mosaic-media/platform/blob/main/docs/adr/0004-static-go-module-composition.md) | Modules are Go libraries compiled into one binary — no plugins, no RPC |
| [sdk#1](https://github.com/mosaic-media/sdk/blob/main/docs/adr/0001-sdk-as-public-contract-language.md) | The SDK is the public contract language between Platform and Modules |
| [platform#5](https://github.com/mosaic-media/platform/blob/main/docs/adr/0005-developer-platform-toolchain.md) | The Developer Platform is an integrated toolchain |
| [platform#6](https://github.com/mosaic-media/platform/blob/main/docs/adr/0006-test-harness-as-development-modules.md) | The Test Harness is built from development-only Modules |
| [platform#7](https://github.com/mosaic-media/platform/blob/main/docs/adr/0007-platform-transports-events.md) | The Platform transports events; Modules own domain events and their names |

[supervisor#1](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0001-supervisor-as-host-manager.md) and [supervisor#2](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0002-supervisor-guarantees-an-interface.md) are the recorded form of the "not your own IT support" goal. **[platform#4](https://github.com/mosaic-media/platform/blob/main/docs/adr/0004-static-go-module-composition.md) is the recorded form of the static-compilation choice**, and therefore the origin of the isolation trade-off below.

---

## Tradeoffs Accepted

Stating these plainly is the point. The previous repository claimed guarantees the architecture cannot deliver, and that is worth not repeating.

**The isolation tradeoff differs by tier, and stating the stronger of the two is the mistake to avoid.**

**Compiling a core module into the binary trades isolation for speed.** Its code is ordinary Go code in the same process as Platform code. There is no runtime boundary, Go provides no in-process sandbox, and it can reach anything the Platform can reach. Trust is therefore established *before* the build, which is affordable only because the core set is small, first-party and closed.

**An extension module has a process boundary, and that is a weaker guarantee than it sounds.** It runs out of process, so it cannot reach the Platform's memory — but denying it a network of its own is an operating-system mechanism needing privileges a non-root Platform does not have, and on macOS and Windows there is no low-cost mechanism at all. **Egress containment is a property of the deployment, not a guarantee the Platform can make**, so the Platform reports which posture it is in rather than claiming enforcement uniformly. Trust here rests on the signed index and the binary digest, checked at install and re-checked at boot, rather than on review before a build.

A permission model is still worth having, and for neither tier is it containment. It makes authority explicit, auditable and reviewable, and it prevents modules from *accidentally* using facilities they never declared. It is a declaration and accountability mechanism. Documentation must not describe it as containment.

---

## Controlled Vocabulary

One term meaning several things caused a real failure: an agent building the roadmap invented a module transport layer, because "transport layer" appears throughout the old corpus meaning three unrelated things — the inbound HTTP/GraphQL adapter boundary, light transport in the material system, and module IPC, which is explicitly forbidden.

Each of these words must carry exactly one meaning, everywhere.

| Term | Means | Does not mean |
|---|---|---|
| **Transport** | Reserved. Do not use unqualified. Say *inbound adapter* for HTTP/GraphQL, *light transport* for the material system | Anything to do with modules |
| **Module** | A unit extending Mosaic through the SDK's ports, in one of two tiers ([architecture#3](adr/0003-two-module-tiers.md)): a **core** module is a Go library linked into the Platform Binary, an **extension** module is its own release, installed at runtime and run out of process | Part of the Platform itself. Say which tier when it matters — an unqualified *module* must not be read as "compiled in" |
| **Gateway** | Reserved. An *outbound* adaptor exposing Mosaic through a foreign client's protocol (facade); the inverse of an inbound *Module* source. None built ([architecture#2](adr/0002-repository-naming-convention.md)) | An inbound source, or anything Mosaic *consumes* |
| **Stale-while-revalidate** | Serving the last known-good *read* from a snapshot while a fresh one is fetched, then replacing it ([platform#30](https://github.com/mosaic-media/platform/blob/main/docs/adr/0030-cache-first-rendering-and-source-health.md)) | *Optimistic UI*, which renders a predicted **write** outcome before the server confirms it. Mosaic predicts nothing |
| **Platform** | Mosaic's own code and contracts | The binary; say *Platform Binary* for that |
| **Supervisor** | The host-level process manager and single front door: runs the Platform and the Shell, terminates TLS, activates a Generation ([supervisor#1](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0001-supervisor-as-host-manager.md), [supervisor#2](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0002-supervisor-guarantees-an-interface.md)) | The Platform, or the Runtime. It no longer selects modules ([platform#49](https://github.com/mosaic-media/platform/blob/main/docs/adr/0049-the-platform-manages-extension-modules.md)) or builds anything ([platform#38](https://github.com/mosaic-media/platform/blob/main/docs/adr/0038-platform-binary-built-by-ci.md)) |
| **Issue** | A durable, typed statement that something is operationally wrong, held by the Platform until resolved ([platform#74](https://github.com/mosaic-media/platform/blob/main/docs/adr/0074-operational-findings-are-durable-state.md)) | A GitHub issue, a log line, or a health state — health says whether traffic should arrive, an Issue says what a person should do |
| **Suggestion** | A named action offered against an Issue, rendered into words by the client ([platform#74](https://github.com/mosaic-media/platform/blob/main/docs/adr/0074-operational-findings-are-durable-state.md)) | A recommendation to the user about content |
| **Store** | A typed persistence contract resolved within a transaction | The database |
| **Node tree** | The content-agnostic object model | A filesystem |
| **Single binary** | The Platform Binary, carrying the core modules, cross-compiled by CI from a version tag ([platform#38](https://github.com/mosaic-media/platform/blob/main/docs/adr/0038-platform-binary-built-by-ci.md)) | The database, which runs as its own process — and neither does it contain an extension module, which runs as its own process too. "Single binary dropped" referred only to not bundling PostgreSQL |
| **Canon** | Reserved. The database is authoritative ([platform#10](https://github.com/mosaic-media/platform/blob/main/docs/adr/0010-storage-authority-and-transaction-scope.md)) | `.mos` and NFO, which are exports |
| **Part** | The bytes an item plays, local path or remote reference | A section of a file, or a node |

Add to this table whenever a word starts carrying two meanings. Removing an ambiguity is cheaper than debugging what it generated.

---

## Settled In Code

Where code exists, **the code is authoritative** and this repository does not restate it. [The roadmap](roadmap.md) is the single record of how far the build has got; what follows is narrower and does not go stale with it — questions the old corpus argued about for chapters, which the code has since answered outright:

| Question | Answer, in code |
|---|---|
| Shutdown sequencing | Stop the worker's poll loop, run one final synchronous outbox drain, then exit. Proven by a test that starts a one-hour ticker so only the shutdown drain can deliver |
| Retry and dead-lettering | Exponential backoff capped at one hour, dead-letter after eight attempts, failure bookkeeping recorded per event |
| Delivery semantics | At-least-once. Subscribers must be idempotent; a retry redelivers to every subscriber of that type |
| Error taxonomy | Seven categories — `InvalidArgument`, `Unauthenticated`, `PermissionDenied`, `NotFound`, `Conflict`, `Unavailable`, `Internal`. No driver type escapes a module boundary |
| Command boundary | Validate, authenticate, authorise, open `UnitOfWork`, load, apply, persist state and outbox in one transaction, return a Platform type |
| Storage extensibility | `Tx` names a closed, Platform-owned store set; capabilities own no schema, so there is nothing to register. `StorageAdapter` remains a port. [platform#8](https://github.com/mosaic-media/platform/blob/main/docs/adr/0008-capabilities-do-not-own-stores.md), superseding [platform#1](https://github.com/mosaic-media/platform/blob/main/docs/adr/0001-transactional-store-extensibility.md) |
| Package tiers | Core Platform, built-in module, extension module. Postgres is a built-in module, not an adapter |
| User authorisation | Real ABAC-shaped policy engine, default-deny, enforced at the application service |

## Deliberately Undecided

Nothing. The list held three entries, which turned out to be four questions —
one entry carried both the manifest and the selection — and each now has a record:

| Was undecided | Closed by |
|---|---|
| What a module may do differently from its invoking user | [platform#85](https://github.com/mosaic-media/platform/blob/main/docs/adr/0085-a-modules-authority-is-declared-and-consented.md) — declared in the signed manifest, consented at install |
| The manifest's full shape, and whether the declared unit is the module or the capability | [platform#97](https://github.com/mosaic-media/platform/blob/main/docs/adr/0097-a-manifest-names-one-capability-and-separates-asks-from-offers.md) — one capability per manifest; an unknown offer is ignored and an unknown ask refuses |
| Where a core-module selection lives | [supervisor#14](https://github.com/mosaic-media/supervisor/blob/main/docs/adr/0014-a-generation-carries-its-selection.md) — in the Generation, so it inherits rollback; requested through a screen |
| Backpressure thresholds and queue bounds | [platform#98](https://github.com/mosaic-media/platform/blob/main/docs/adr/0098-a-queue-that-is-behind-raises-an-issue.md) — a queue does not refuse; age past a threshold raises an Issue |

Decided is not built. [The roadmap](roadmap.md) is where that distinction lives,
and all four of these are unbuilt. [The work graph](work-graph.md) is where the
unbuilt part is decomposed into units, with what each depends on and what proves
it done — it deliberately carries no status, so that the roadmap stays the one
answer to how far the build has got.

**The list was never the only register.** Emptying it prompted a sweep of every
record in every repository for open-question language, which found twelve more
that nothing was tracking — precedence, revocation, extension updates, two
leftovers from the object graph, and the meaning of a record's own Status among
them. All twelve are now recorded. The lesson is the register's: a list somebody
has to remember to add to will be incomplete, and the reliable place an open
question lives is the record that hit it.

Add to this list when something is deferred *on purpose* — a question whose
answer should wait for the first case that forces it. An item here is a decision
not yet taken; an item that is merely unimplemented belongs in the roadmap.

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
