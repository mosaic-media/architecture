# Open Questions and Documentation Defects

A register of things found in the documentation that **cannot be fixed by editing prose**, because resolving them requires knowing what Mosaic actually does.

This file is deliberately outside `docs/`. MkDocs never publishes it and `scripts/validate_docs.py` never scans it, so it can name unresolved contradictions plainly without those contradictions appearing on the documentation site as though they were content.

## Why this exists

The documentation rewrite fixes how the documentation reads. It cannot fix whether the documentation is *true*. Three classes of problem surface during a rewrite and all three are recorded here rather than guessed at:

- **Contradictions** — two documents, or two sections of one document, state incompatible rules. Picking a side without knowing the architecture would silently invent it.
- **Underspecified** — a passage is vague, hedged, or defers to an owner it never names. Making it concrete requires facts that exist in someone's head or in the codebase, not in this repository.
- **Duplication** — the same concept is defined in several places. Deduplicating means deciding which document owns it, which is an authority decision.

An agent rewriting prose must never resolve these by inference. Fabricated architecture is worse than vague architecture, because it reads as settled.

## How to use this

Answer entries inline. Edit the **Resolution** line, set **Status** to `Answered`, and the next documentation pass will apply it and set the entry to `Resolved`.

| Status | Meaning |
|--------|---------|
| `Open` | Needs a decision from someone who knows the architecture. |
| `Answered` | Decision recorded here; not yet applied to the documentation. |
| `Resolved` | Applied. Kept for traceability. |
| `Won't fix` | Deliberately left as-is, with the reason recorded. |

Identifiers are permanent. A resolved entry keeps its number.

---

# Contradictions

## Q-001 — Which layer owns a Driving Port?

**Status:** `Open`
**Where:** [MEG-004 ch03](../docs/engineering/guides/meg-004-hexagonal-architecture/03-driving-ports.md), [ch02](../docs/engineering/guides/meg-004-hexagonal-architecture/02-ports.md), [ch04](../docs/engineering/guides/meg-004-hexagonal-architecture/04-driven-ports.md)

Chapter 03 states that Driving Ports "belong to the Application layer immediately surrounding the Domain". Chapter 02's guidelines state that Ports must belong to the Domain, and chapter 04 repeats that for Driven Ports.

Either Driving Ports are a deliberate exception, or one of these statements is wrong. This is load-bearing: it determines which package a Port interface is declared in.

**Resolution:**

## Q-002 — Does a Driving Port receive transport models or business models?

**Status:** `Open`
**Where:** [MEG-004 ch03](../docs/engineering/guides/meg-004-hexagonal-architecture/03-driving-ports.md), sections *Request Models* and *Validation*

*Request Models* says transport models should be translated before reaching the Port, which implies a Port never sees a transport model. *Validation* says Driving Ports "should receive already valid transport models", which implies it does.

Both statements were preserved verbatim during the rewrite rather than picking a side.

**Resolution:**

## Q-003 — "Define Ports Last" contradicts its own chapter

**Status:** `Open`
**Where:** [MEG-004 ch13](../docs/engineering/guides/meg-004-hexagonal-architecture/13-modelling-guidelines.md)

The section heading says "Define Ports Last". The chapter's own Philosophy makes defining Ports step 3 of 5, before implementing Adapters and assembling the Composition Root. The body text ("Ports should emerge naturally") is consistent with the Philosophy; only the heading conflicts.

Probably just a wrong heading, but changing it changes guidance, so it is not an editorial fix.

**Resolution:**

## Q-004 — Dependency arrows point the wrong way

**Status:** `Open`
**Where:** [MEG-004 ch11](../docs/engineering/guides/meg-004-hexagonal-architecture/11-runtime-boundary.md), *Relationship to MEG* diagram

The diagram renders `Domain → Ports → Adapters → Reactive Runtime → Infrastructure`, with arrows pointing outward from the Domain. The guide's central rule, stated in chapters 09 and 13, is that dependencies point inward.

If the arrows mean "layering" rather than "depends on", the diagram needs a different notation, because every other diagram in the guide uses arrows for dependency.

**Resolution:**

## Q-005 — Can one Adapter implement several Ports?

**Status:** `Open`
**Where:** [MEG-004 ch05](../docs/engineering/guides/meg-004-hexagonal-architecture/05-adapters.md), [ch07](../docs/engineering/guides/meg-004-hexagonal-architecture/07-driven-adapters.md)

Chapter 05 titles a section "One Adapter, One Technology" and lists "Shared Adapters: one Adapter implementing unrelated Ports" as prohibited. The guidelines in both 05 and 07 state that an Adapter "must implement one **or more** Ports".

These reconcile only if "unrelated" carries the whole distinction, which is never defined. What makes two Ports related enough to share an Adapter?

**Resolution:**

## Q-006 — Uppercase RFC 2119 keywords across the engineering guides

**Status:** `Open`
**Where:** MEG-001 through MEG-009, MIP-003 — roughly 1,800 occurrences across 162 files
**Also:** [MDG-001 ch10](../docs/engineering/documentation/mdg-001-documentation-authority-guide/10-standards-mapping.md)

MDG-001 chapter 10 adopts RFC 2119 *semantics* but explicitly rejects its uppercase typography. Most engineering guides are written in uppercase `MUST` / `SHOULD` / `MAY`, and MEG-001's own Document Control defines an uppercase normative table, which directly contradicts the ratified standard.

Either those guides are rewritten to sentence case, or MDG-001 chapter 10 records them as a standing exception. Vale reports these as warnings today, which drowns other signal.

MEG-004 has already been converted, so the pattern is proven.

MEG-005 has now been converted too, leaving only its Normative Language table uppercase. That table is the same construct MEG-001 uses, so whichever way this is decided, the two should be decided together.

**Resolution:**

## Q-026 — Dependency arrows contradict the stated startup order

**Status:** `Open`
**Where:** [MEG-005 ch05](../docs/engineering/guides/meg-005-runtime-architecture/05-dependency-graph.md), [ch04](../docs/engineering/guides/meg-005-runtime-architecture/04-service-lifecycle.md)

Chapter 05's *Directed Graph* section states the convention explicitly: an edge from A to B means A depends upon B, and direction communicates dependency, never execution. *Runtime Services* obeys it, drawing `Worker Manager → Execution Engine → Capability Registry`, which makes the Capability Registry a leaf and is consistent with it starting first.

Three other diagrams draw the same components in the opposite direction, `Capability Registry → Execution Engine → Scheduler → Worker Manager`, and the surrounding prose calls that the startup order. Under the chapter's own rule that chain asserts the Capability Registry depends upon the Execution Engine, inverting the dependency the rest of the chapter states. The identical chain also appears in chapter 04 under *Lifecycle Dependencies*.

Resolving it means committing to one convention — edges as dependency, so startup reads leaves-first, or edges as execution order, which would contradict *Directed Graph* as written — and then reversing arrows across two chapters. Both readings are internally coherent and nothing in the repository settles which MEG-005 intends, so every diagram was left exactly as committed and the surrounding prose phrased neutrally.

**Resolution:**

## Q-027 — No Runtime component owns retry policy

**Status:** `Open`
**Where:** [MEG-005 ch06](../docs/engineering/guides/meg-005-runtime-architecture/06-execution-engine.md), [ch07](../docs/engineering/guides/meg-005-runtime-architecture/07-worker-manager.md), [ch08](../docs/engineering/guides/meg-005-runtime-architecture/08-scheduler-architecture.md)

Chapter 06 states that the Execution Engine does not own retries, then says "The Runtime decides: retry, dead letter, shutdown" without naming which subsystem holds that decision. Every named candidate disclaims it in its own chapter.

Chapter 08 makes the gap sharper still: the Scheduler owns "retry timing" and "delayed execution" but explicitly does not own "retries". The intended split is presumably that something decides *whether* to retry while the Scheduler decides *when*, but the document never says so, and *Delayed Execution*'s only example is a metadata retry, which makes the boundary look self-contradictory.

Either a component not yet described in MEG-005 owns retry policy, or one of these chapters is wrong.

**MEG-002 answers one level above the component boundary and so does not resolve this.** [MEG-002 ch13](../docs/engineering/guides/meg-002-event-driven-runtime/13-retry-strategy.md) *Runtime Ownership* assigns retry scheduling, timing, counting, cancellation and observability to "the runtime", and its Philosophy states "Retry infrastructure belongs to the runtime. Recovery belongs to the capability." It names no component.

MEG-005 is itself split: [ch16](../docs/engineering/guides/meg-005-runtime-architecture/16-contributor-guidance.md) says a Worker Manager should "let the Scheduler own the retry" and [ch08](../docs/engineering/guides/meg-005-runtime-architecture/08-scheduler-architecture.md) lists retry timing among Scheduler responsibilities, while [ch06](../docs/engineering/guides/meg-005-runtime-architecture/06-execution-engine.md) says "The Runtime decides whether to retry, dead letter or shut down." MEG-002 sides with the latter phrasing. Whether retry *timing* (Scheduler) and retry *policy* (Runtime) are deliberately different owners needs an architecture decision. See also Q-090, which records that no bound on retries is stated anywhere.

**Resolution:**

## Q-028 — Startup has eleven diagram stages and ten numbered headings

**Status:** `Open`
**Where:** [MEG-005 ch10](../docs/engineering/guides/meg-005-runtime-architecture/10-startup.md), *Startup Sequence* against *Stage 1* to *Stage 10*

The sequence diagram names `Mark Ready` and `Begin Execution` as separate stages, while the headings collapse readiness and execution into Stage 9 and Stage 10, with `Bootstrap` and `Load Configuration` mapping onto Stages 1 and 2. The mapping from diagram node to numbered stage is not one-to-one.

Deciding which is authoritative means either adding a stage boundary or removing one, so both were left as committed.

**Resolution:**

## Q-042 — MEG-003 chapters 08 and 09 state three incompatible rules

**Status:** `Open`
**Where:** [MEG-003 ch08](../docs/engineering/guides/meg-003-domain-driven-design/08-aggregates.md), [ch09](../docs/engineering/guides/meg-003-domain-driven-design/09-aggregate-roots.md)

Both chapters carry a Mosaic Guidelines list, and the two lists disagree on three points. An implementer reading only one chapter gets a different rule from one reading only the other:

- **Unit of persistence.** Chapter 08 requires repositories to persist *Aggregates*; chapter 09 requires them to persist *Aggregate Roots*. Chapter 08's *Persistence* section introduces a third noun, "consistency boundaries". If the Root is the boundary these coincide, but they are written as distinct normative requirements.
- **Source of Domain Events.** Chapter 08 calls Aggregates the *primary* source, which admits others; chapter 09 calls Aggregate Roots the *canonical* source, which does not. Neither says whether a non-Root Entity inside an Aggregate may raise a Domain Event.
- **Cross-Aggregate transactions.** Chapter 08's body says one transaction *should* modify one Aggregate, while its own Anti-Patterns section opens "The following practices are prohibited" and lists Cross-Aggregate Transactions. A recommendation and a prohibition on the same behaviour, three sections apart.

Related to Q-045, which covers the broader overlap between these two chapters.

**Resolution:**

## Q-043 — May a Domain Service raise a Domain Event?

**Status:** `Open`
**Where:** [MEG-003 ch10](../docs/engineering/guides/meg-003-domain-driven-design/10-domain-services.md), *Domain Events*; [ch11](../docs/engineering/guides/meg-003-domain-driven-design/11-domain-events.md), *Mosaic Guidelines*

Chapter 10 says business facts should originate from Aggregates "whenever practical", which implies an exception exists. Chapter 11 says Domain Events must originate from Aggregates, which allows none. Chapter 10 separately forbids Domain Services from publishing runtime events, which is a different prohibition again.

Either a Domain Service may raise a Domain Event directly in some named circumstance, or chapter 10's hedge is wrong. Both wordings were preserved unchanged.

**Resolution:**

## Q-044 — The infrastructure-dependency prohibition is stated three different ways

**Status:** `Open`
**Where:** [MEG-003 ch06](../docs/engineering/guides/meg-003-domain-driven-design/06-entities.md), *Persistence* and *Anti-Patterns*; [ch07](../docs/engineering/guides/meg-003-domain-driven-design/07-value-objects.md), *Anti-Patterns*

What is presumably one rule appears as three overlapping but non-identical lists. Chapter 06's Anti-Patterns prohibit SQL, HTTP, JSON and Logging; chapter 07's prohibit SQL, HTTP, Logging and **Runtime**; chapter 06's *Persistence* names SQL, PostgreSQL, DuckDB, HTTP and JSON.

Whether `Runtime` is deliberately Value-Object-only matters, because [MEG-004](../docs/engineering/guides/meg-004-hexagonal-architecture/01-hexagonal-philosophy.md) treats the Runtime as infrastructure for the whole Domain, which would make it apply to Entities too.

**Resolution:**

## Q-060 — Who grants a permission, and at which stage?

**Status:** `Open`
**Where:** [MEG-006 ch09](../docs/engineering/guides/meg-006-module-platform/09-permissions.md), [ch06](../docs/engineering/guides/meg-006-module-platform/06-activation.md), [ch02](../docs/engineering/guides/meg-006-module-platform/02-module-manifest.md)
**Also:** [MEG-009 ch05](../docs/engineering/guides/meg-009-security-architecture/05-capability-permissions.md)

Three chapters place the grant at three different points. Chapter 09 says the Runtime grants permissions *during* activation, after the manifest is read and validated. Chapter 06 lists "permissions approved" as an activation *prerequisite* and states that if any prerequisite fails "activation must not begin at all". Chapter 09's own guideline list says permissions must be granted *before execution*, which is a third boundary. Chapter 02 requires "permission review before activation" without saying by whom.

The grantor is never named. Chapter 09 mentions human involvement only for *changes* — an added permission requires operator approval — and nothing states whether a first install requires operator consent or whether the Runtime grants declared permissions automatically. MEG-009 chapter 05 draws an explicit `Approval` stage between Validation and Activation that MEG-006 has no counterpart for.

Whether the security model has a human consent gate, and at which stage authority is conferred, is a design fact. Either reading invents the platform's consent model.

**Resolution:**

## Q-061 — What happens when a permission is denied, and can one be revoked?

**Status:** `Open`
**Where:** [MEG-006 ch09](../docs/engineering/guides/meg-006-module-platform/09-permissions.md), *Permission Enforcement*, *Permission Denial*, *Optional Permissions*
**Also:** [MEG-009 ch05](../docs/engineering/guides/meg-009-security-architecture/05-capability-permissions.md)

Chapter 09 says that without `blob.read` "the SDK rejects the request", and that the Runtime should provide diagnostics and operator visibility. It never says whether the SDK returns an error the capability can handle, panics, or deactivates the capability. MEG-009 describes a materially different model in which unavailable authority simply does not exist, so the contract is never injected and `ctx.BlobStore()` cannot be called at all.

The activation-time case is equally open: if a manifest declares a permission that is not granted, nothing says whether activation fails or the capability activates with reduced authority. Reduced-authority operation is described only for *optional* dependencies and *optional* permissions.

MEG-006 never mentions **revocation**, while MEG-009 requires it to be immediate and emits `PermissionRevoked` telemetry. Whether a running capability's authority can be withdrawn at all is therefore undecided.

Denial semantics and revocability are runtime behaviour with security consequences and cannot be inferred from the prose.

**Resolution:**

## Q-062 — Three chapters give three different capability lifecycle orders

**Status:** `Open`
**Where:** [MEG-006 ch03](../docs/engineering/guides/meg-006-module-platform/03-discovery.md), [ch04](../docs/engineering/guides/meg-006-module-platform/04-registration.md), [ch05](../docs/engineering/guides/meg-006-module-platform/05-dependency-resolution.md), [ch06](../docs/engineering/guides/meg-006-module-platform/06-activation.md)

- ch03 *Discovery Before Execution*: Discovery → Validation → Registration → Activation → Execution, with dependency resolution absent entirely.
- ch03 *Discovery Pipeline* places the Dependency Resolver **inside** discovery, before the build workspace.
- ch04 *Registration Before Activation*: resolution **after** registration.
- ch06 *Purpose*: resolution **before** registration. ch05 agrees with ch06, which makes ch04 the outlier.

Chapter 04 itself distinguishes two registrations — build-time manifest admission and Runtime `sdk.Register` — which sit on opposite sides of the build, so ordering resolution against "registration" requires knowing which one each diagram means.

**Resolution:**

## Q-063 — Does Discovery or Registration populate the Capability Registry, and is the SDK Registry the same store?

**Status:** `Open`
**Where:** [MEG-006 ch03](../docs/engineering/guides/meg-006-module-platform/03-discovery.md), [ch04](../docs/engineering/guides/meg-006-module-platform/04-registration.md)

Chapter 03 says the resulting Capability Registry should be identical regardless of discovery order, and its anti-pattern forbids discovery from modifying Runtime state "beyond the Capability Registry" — implying discovery writes to it — while its *Implicit Registration* anti-pattern simultaneously forbids discovery from registering anything. Chapter 04 states flatly that registration populates the Capability Registry.

Chapter 04 then names two registries. *Runtime Admission* says registration admits the Module into the **SDK registry**, which "holds the result"; *Registry Population* says registration populates the **Capability Registry**, "the Runtime's authoritative source of capability information"; and *Duplicate Registries* prohibits holding capability information anywhere else, which the SDK registry appears to do.

Whether these are one store, two stores, or one feeding the other is an architecture fact — MAC-001 and MEG-005 chapter 14 both use "SDK Registry" — and the "authoritative source" prohibition makes it load-bearing.

**Resolution:**

## Q-064 — The permission manifest has three shapes, one contradicting MIP-002

**Status:** `Open`
**Where:** [MEG-006 ch09](../docs/engineering/guides/meg-006-module-platform/09-permissions.md), [ch02](../docs/engineering/guides/meg-006-module-platform/02-module-manifest.md), [ch04](../docs/engineering/guides/meg-006-module-platform/04-registration.md)
**Also:** [MIP-002](../docs/engineering/protocols/mip-002-module-manifest-protocol/index.md)

MIP-002 — which chapter 02 declares authoritative — and chapter 02's own example use a **nested** form (`permissions: network: - graphql.anilist.co`). Chapter 09 uses a **flat string list** plus `network.outbound` as a permission name plus a separate top-level `network: hosts:` block. MEG-009 chapter 05 uses a third form again.

Chapter 09 also introduces `optionalPermissions`, and chapter 05 introduces `optionalDependencies` and `conflicts`, none of which appear in MIP-002. Chapter 02 states that MEG-006 does not restate the manifest contract, yet its example already diverges from MIP-002 by dropping the `events.publishes.public/private` split.

Manifest field shape is MIP-002's contract, so choosing one requires knowing which the parser implements.

**Resolution:**

## Q-065 — Configuration ownership contradicts MEG-005

**Status:** `Open`
**Where:** [MEG-006 ch10](../docs/engineering/guides/meg-006-module-platform/10-configuration.md), *Live Configuration* and *Configuration Sources*
**Also:** [MEG-005 ch18](../docs/engineering/guides/meg-005-runtime-architecture/18-configuration-and-secrets.md)

Two incompatible models are described for the same subject:

- **Who decides warm-apply versus restart.** MEG-006 says capabilities should decide whether configuration can be applied dynamically. MEG-005 says the Runtime classifies changes and the Supervisor warms a new generation and switches, with restart as the fallback when a transition is unsafe. This is the direct answer to Q-034's undefined *unsafe* criterion — MEG-006 contradicts it rather than answering it, and supplies no criterion of its own.
- **Precedence.** MEG-005 gives five levels ending in "explicitly permitted runtime overrides". MEG-006 gives six differently named sources and then says "the Runtime owns precedence between them", which contradicts MEG-005's fixed documented order. MEG-006's "administrative overrides" carries the same defect Q-034 records: no statement of who holds the authority or what may be overridden.

**Resolution:**

## Q-066 — Isolation is guaranteed without a mechanism, inside a single statically linked binary

**Status:** `Open`
**Where:** [MEG-006 ch12](../docs/engineering/guides/meg-006-module-platform/12-isolation.md), [ch13](../docs/engineering/guides/meg-006-module-platform/13-platform-guidelines.md), [ch16 ADR-001](../docs/engineering/guides/meg-006-module-platform/16-adrs.md)

Chapter 12 asserts that an execution failure in one capability should not affect unrelated capabilities, that the Runtime should ensure Playback continues, and that a misbehaving module remains constrained by permissions, contracts and Runtime boundaries. No mechanism is named anywhere — no panic recovery, goroutine supervision, worker boundary or resource quota. The only support offered is a citation to the AWS bulkhead pattern, which describes pool or process partitioning.

This sits directly against MEG-006's own ADR-001, which makes the product one statically linked Go executable in which Platform code and Module code are both ordinary Go code, with no RPC or process boundary. Either a containment mechanism exists and is unwritten, or these guarantees are weaker than stated.

This is the most consequential entry recorded against MEG-006: the isolation claims are what make third-party modules safe to install.

**Resolution:**

## Q-067 — `CapabilityContext` is declared as fields and used as methods

**Status:** `Open`
**Where:** [MEG-006 ch08](../docs/engineering/guides/meg-006-module-platform/08-module-sdk.md), *Capability Context* and *Permissions*

The struct embeds `Logger`, `Scheduler`, `Configuration`, `Events` and `Health` as bare type names, but the chapter then accesses them as methods — `ctx.Configuration()`, `ctx.Scheduler()`, `ctx.Events()`, `ctx.Logger()`, `ctx.Health()` — which embedded fields would not provide. The struct and the call sites cannot both be right; both were preserved exactly.

Separately, `ctx.BlobStore()` is used as the worked permissions example but is not among the SDK's listed contracts, models or context members, and `blob.read` is the chapter's only permission string.

**Resolution:**

## Q-082 — MEG-002 and MEG-005 order the shutdown stages incompatibly

**Status:** `Open`
**Where:** [MEG-002 ch17](../docs/engineering/guides/meg-002-event-driven-runtime/17-runtime-shutdown.md), *Shutdown Sequence*; [MEG-005 ch11](../docs/engineering/guides/meg-005-runtime-architecture/11-shutdown.md), *Shutdown Sequence*

The two documents specify the same procedure in two different orders:

- **MEG-002:** stop accepting → cancel scheduling → drain queues → finish active work → **release resources → stop workers** → runtime stops.
- **MEG-005:** cooldown → capability drain → **worker drain → runtime services stop → resource release** → kernel shutdown → process exit.

MEG-002 releases resources *before* it stops workers; MEG-005 stops workers *before* it releases resources and states the governing rule explicitly — "Worker disposal should occur only after execution completes". MEG-002 asserts of its own ordering that "The order is deliberate. Changing it risks inconsistent behaviour."

These cannot both be right, and MEG-002's order releases database transactions, file handles and network connections that its own chapter 10 says workers may still hold. This is the highest-consequence contradiction found in this document: implemented as written, it is a use-after-release during every shutdown.

**Resolution:**

## Q-083 — Chapter 20 mandates a deduplication key that chapter 12 makes optional

**Status:** `Open`
**Where:** [MEG-002 ch20](../docs/engineering/guides/meg-002-event-driven-runtime/20-v2-event-backbone.md), *Delivery Semantics*; [ch12](../docs/engineering/guides/meg-002-event-driven-runtime/12-idempotency.md), *Event Recording*

Chapter 20 requires that consumers "must be idempotent and must use the event identifier or an equivalent deduplication key when applying side effects". Chapter 12 says subscribers *may* maintain a processed-event store, adds that "the runtime does not require a specific implementation, only the resulting behaviour", and actively prefers business keys over event identifiers.

The two agree that subscribers must be idempotent. They disagree on whether a deduplication key is mandated, and chapter 20 mandates the specific mechanism chapter 12 declines to mandate.

**Resolution:**

## Q-084 — Chapter 20 is titled "v2" but written as current commitment

**Status:** `Open`
**Where:** [MEG-002 ch20](../docs/engineering/guides/meg-002-event-driven-runtime/20-v2-event-backbone.md)

The file is named *v2 Event Backbone* and the index carries a "Current v2 direction" banner, but the chapter's epigraph opens "**Current direction:** Mosaic uses a PostgreSQL transactional outbox", the tense is present throughout, and it closes with a *Required Guarantees* section carrying six normative `must` clauses.

If the backbone is deferred, [MDG-001 ch04](../docs/engineering/documentation/mdg-001-documentation-authority-guide/04-writing-standards.md) is breached — planning language must not make uncommitted work appear mandatory. If it is not deferred, the "v2" title is misleading and the chapter is a second authority for material chapters 07 and 12 to 15 already own.

The chapter also departs from the house template: `##` headings with no `---` rules, no Purpose, Philosophy, Mosaic Guidelines or Summary section, and a bold callout in place of the italic epigraph. Reshaping it interacts with the lifecycle question, so nothing was normalised.

**Resolution:**

## Q-085 — Trace propagation ownership contradicts MEG-008

**Status:** `Open`
**Where:** [MEG-002 ch16](../docs/engineering/guides/meg-002-event-driven-runtime/16-correlation-and-observability.md); [MEG-008 ch04](../docs/engineering/guides/meg-008-observability/04-distributed-tracing.md)

MEG-008 states "The Runtime owns propagation. **The SDK exposes it.**" MEG-002 says only that "the runtime owns tracing infrastructure" and never mentions the SDK. Resolution depends on whether MIP-004 carries it, and MIP-004 is a published stub (Q-019).

More fundamentally, **Correlation ID and Causation ID appear nowhere in MEG-008 at all.** MEG-008 requires a "trace identifier, parent span, correlation metadata" and has no causation concept. Whether Causation ID and parent span are one mechanism under two names is exactly what must not be inferred, so MEG-002's vocabulary was preserved unchanged.

**Resolution:**

## Q-086 — Priority is optional and its outcome is recommended

**Status:** `Open`
**Where:** [MEG-002 ch15](../docs/engineering/guides/meg-002-event-driven-runtime/15-backpressure.md), *Priority* and *Mosaic Guidelines*

The body says the scheduler *may* prioritise work; the guidelines say high-priority work *should* remain responsive. An optional mechanism cannot deliver a recommended outcome, so one of the two normative levels is wrong. Related to Q-032, which records that MEG-005's priority tiers never connect to admission.

**Resolution:**

---

# Duplication and Ownership

## Q-007 — MEG-004 chapters 02 and 04 are substantially the same chapter

**Status:** `Open`
**Where:** [ch02 Ports](../docs/engineering/guides/meg-004-hexagonal-architecture/02-ports.md), [ch04 Driven Ports](../docs/engineering/guides/meg-004-hexagonal-architecture/04-driven-ports.md)

*Why Ports Exist* and *Why Driven Ports Exist* use the same Playback and PostgreSQL example and the same diagrams. *Ports Describe Behaviour*, *Business Language*, *Ports Are Stable* and the "ports are small" material appear in both. Chapter 02's *Mosaic Examples* is a superset of chapter 04's *Examples Within Mosaic*.

If 02 owns the general Port rules, much of 04 could become a sentence and a cross-reference.

**Resolution:**

## Q-008 — MEG-004 chapters 05 and 07 overlap substantially

**Status:** `Open`
**Where:** [ch05 Adapters](../docs/engineering/guides/meg-004-hexagonal-architecture/05-adapters.md), [ch07 Driven Adapters](../docs/engineering/guides/meg-004-hexagonal-architecture/07-driven-adapters.md)

Error Translation, Mapping, Composition Root, Multiple Adapters and the Shared Adapters anti-pattern appear in near-identical form in both. The `Domain → PlaybackRepository → PostgreSQL Adapter → Database` argument appears in chapters 04, 05 **and** 07.

**Resolution:**

## Q-009 — Repeated sections within single chapters

**Status:** `Open`
**Where:** MEG-004 chapters 02, 08, 09, 12, 13

Several sections make the same argument twice:

- ch02: *Ports Are Stable* and *Port Evolution*; *Ports Are Small* and *One Responsibility*
- ch08: *Adapters*, *Ports* and *Infrastructure* restate chapters 02 and 05 with no cross-reference
- ch12 *Test Composition Root* duplicates ch09 *Testing*
- ch13 *Runtime Is Infrastructure* restates chapter 11 wholesale, and says so ("One subtle guideline deserves repeating")
- Three near-identical litmus tests: ch12 *Domain Isolation*, ch12 *Architecture Verification*, ch13 *Design For Testing*

Each survives the rewrite because deleting one is a content decision.

**Resolution:**

## Q-010 — MDL-005 and MDP-001 overlap chapter for chapter

**Status:** `Open`
**Where:** [MDL-005](../docs/design/language/mdl-005-composition-model/index.md), [MDP-001](../docs/engineering/architecture/mdp-001-adaptive-composition-runtime/index.md)

| MDP-001 | MDL-005 already owns |
|---------|----------------------|
| 03 Composition Solver | 09 Composition Solving |
| 05 Runtime Hierarchy | 02 Hierarchy, 03 Priority, 04 Hero |
| 06 Adaptive Layout | 06 Adaptive Composition, 07 Density, 08 Breathing Space, 05 Anchors |
| 10 Multi-Device Composition | 10 Device Independence |

MDL-005 is authoritative; MDP-001 is deferred. The overlap is therefore not harmful today, but it means two documents describe the same concepts at different levels of commitment.

**Resolution:**

## Q-011 — MAC-001 and MDP-001 both claim orchestration

**Status:** `Open`
**Where:** [MAC-001 ch02](../docs/engineering/architecture/mac-001-platform-architecture/02-runtime-boundary.md), [MDP-001 ch07](../docs/engineering/architecture/mdp-001-adaptive-composition-runtime/07-behaviour-orchestration.md), [ch08](../docs/engineering/architecture/mdp-001-adaptive-composition-runtime/08-runtime-pipelines.md)

MAC-001 states the Runtime owns dependency graph management and execution orchestration. MDP-001 chapter 07 defines a dependency graph and asserts that "Behavioural ordering remains architecturally defined by this specification".

A deferred proposal should not claim architectural authority over something the Canon owns.

**Resolution:**

## Q-012 — MDP-001 asserts definitions in the MDS namespace

**Status:** `Open`
**Where:** [MDP-001](../docs/engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) chapters 02, 04, 05, 06, 07, 08, 09

Seven chapters open with "Within MDS, **X** is defined as…". MDP-001 is a deferred, non-authoritative proposal and cannot define terms in the Design System namespace. The phrasing is left over from when this material was an active MDS specification.

Fixing it means rewriting the definitional sentence in seven chapters, which changes what the document claims about itself.

**Resolution:**

## Q-029 — "Runtime Kernel" and "Microkernel Runtime" may be the same thing

**Status:** `Open`
**Where:** [MEG-005 ch16](../docs/engineering/guides/meg-005-runtime-architecture/16-contributor-guidance.md), [ch15](../docs/engineering/guides/meg-005-runtime-architecture/15-adrs.md), [glossary](../docs/engineering/guides/meg-005-runtime-architecture/glossary.md)

Chapter 16 uses "Runtime Kernel" throughout, including in *Before Modifying The Kernel* and its checklist, while chapter 15's Decision Areas list uses "Microkernel Runtime". These may name the same component, or may be a whole-versus-part distinction.

The glossary does not settle it, because it separately defines both *Kernel* and *Runtime Kernel* — see Q-040. Unifying the terms would assert an architectural identity that cannot be verified from the repository, so all three spellings were left as written.

**Resolution:**

## Q-045 — MEG-003 chapters 08 and 09 are substantially the same chapter

**Status:** `Open`
**Where:** [ch08 Aggregates](../docs/engineering/guides/meg-003-domain-driven-design/08-aggregates.md), [ch09 Aggregate Roots](../docs/engineering/guides/meg-003-domain-driven-design/09-aggregate-roots.md)

The MEG-003 counterpart to Q-007. The two chapters restate each other in nine places: *Persistence* is near-verbatim in both; cross-Aggregate references build the same `Collection → MediaID` example against the same Fowler citation; Domain Events use the same `Complete()` → `PlaybackCompleted` example; the transactional boundary is argued three times across the two; invariant enforcement appears in four sections; size and cohesion twice; *Mosaic Examples* twice with **different** responsibility bullets (see Q-051); the anti-pattern lists overlap; and the single-Root rule is stated in 08 and re-argued as the whole of 09.

A workable split, if someone wants one: 08 owns *boundary identification* — which rules must hold together, size, Bounded Context ownership, cross-Aggregate eventual consistency — and 09 owns the *enforcement mechanism* — single entry point, hidden internals, API shape, constructors, identity. Under that split, References, Persistence, Transactions, Domain Events and Mosaic Examples currently sit in the wrong chapter or in both.

The three outright contradictions this overlap produces are recorded separately as Q-042.

**Resolution:**

## Q-046 — MEG-003 chapters 06 and 07 are mirror images

**Status:** `Open`
**Where:** [ch06 Entities](../docs/engineering/guides/meg-003-domain-driven-design/06-entities.md), [ch07 Value Objects](../docs/engineering/guides/meg-003-domain-driven-design/07-value-objects.md)

The two chapters teach the same distinction twice from opposite ends. Chapter 06's *What Is Not An Entity?* lists Duration, Resolution, Rating, Language and Genre; chapter 07's *What Is Not A Value Object?* lists Media, User, Collection and Playback Session. Identity-based equality is defined in 06 *Equality* and defined again by negation in 07 *Value Defines Equality*. The rule that an invalid instance should never exist because the constructor enforces it appears as a full section in both. Both carry a near-identical *Evolution* section.

Deciding which chapter owns the contrast, and whether the other should summarise and link per [MDG-001 *Avoid Duplication*](../docs/engineering/documentation/mdg-001-documentation-authority-guide/04-writing-standards.md), is an authority decision.

**Resolution:**

## Q-047 — MEG-003 chapter 15 restates chapters 04 to 14

**Status:** `Open`
**Where:** [MEG-003 ch15](../docs/engineering/guides/meg-003-domain-driven-design/15-modelling-guidelines.md)

*Identify Entities*, *Identify Value Objects*, *Identify The Aggregate*, *Find The Aggregate Root*, *Introduce Domain Services Carefully*, *Introduce Repositories Last* and *Protect Invariants* each re-derive the defining test from the chapter that owns the concept, so the identity-versus-value test, the consistency-boundary test and the "Domain Services should remain rare" rule now each exist in two places.

This may well be deliberate, since a guidelines chapter that summarises is doing its job. It is recorded because the repeated tests are stated as rules rather than as summaries with links, which is what makes them able to drift. *Resist Technical Thinking* and *Common Modelling Mistakes* also duplicate each other within chapter 15 itself.

The same question applies to the glossary, which carries full definitions of Aggregate, Aggregate Root, Bounded Context, Entity, Value Object, Domain Service, Factory and Repository, each of which has a dedicated chapter.

**Resolution:**

## Q-048 — MEG-003 has a chapter about ADRs and no ADRs

**Status:** `Open`
**Where:** [MEG-003 ch16](../docs/engineering/guides/meg-003-domain-driven-design/16-adrs.md)

The chapter defines when to create a decision record and names seven decision areas — Library Is The Core Aggregate, Playback As Independent Context, Metadata Ownership, Continue Watching Model, Recommendation Domain, Media Identity Strategy, Collection Ownership — but contains no decision records, and no `ADR-nnn` identifier appears anywhere in MEG-003. The chapter is 49 lines and was confirmed as a genuine stub rather than padded.

Either these seven decisions were never recorded, or they live somewhere the chapter does not point to. Two of the seven — Continue Watching Model and Recommendation Domain — have no corresponding chapter in MEG-003 modelling them at all, so it is not clear whether they are forward-looking placeholders or references to modelling that was dropped.

MEG-006's equivalent chapter is *not* a stub — it carries four complete records — but has the same shortfall at larger scale: see Q-072.

**Resolution:**

## Q-068 — MEG-006 and MEG-009 both define the capability permission model

**Status:** `Open`
**Where:** [MEG-006 ch09](../docs/engineering/guides/meg-006-module-platform/09-permissions.md), [MEG-009 ch05](../docs/engineering/guides/meg-009-security-architecture/05-capability-permissions.md)

The two chapters share the epigraph, the least-privilege `blob.read` / `blob.*` example, the `ctx.BlobStore()` enforcement example, the Marketplace justification section, the Permission Evolution triple, the Runtime Visibility question and most anti-patterns. MEG-006 chapter 09 contains no link to MEG-009, and MEG-006's index lists MEG-009 under *future companion specifications* although it is present and Draft.

Where they diverge they diverge substantively — see Q-060, Q-061 and Q-080 — and MEG-009 additionally owns Secrets and Revocation that MEG-006 omits. Deduplicating therefore changes rules rather than wording, and deciding whether a guide chapter or the security architecture owns the model is an authority decision.

**Resolution:**

## Q-069 — MEG-006 chapter 07 restates chapters 03 to 06, and 08 overlaps 14

**Status:** `Open`
**Where:** [MEG-006 ch07](../docs/engineering/guides/meg-006-module-platform/07-module-lifecycle.md), [ch08](../docs/engineering/guides/meg-006-module-platform/08-module-sdk.md), [ch14](../docs/engineering/guides/meg-006-module-platform/14-developer-platform.md), [ch15](../docs/engineering/guides/meg-006-module-platform/15-test-harness.md)

Chapter 07's Discovery, Registration, Resolution and Activation sections restate chapters 03, 04, 05 and 06 almost stage for stage, framing as lifecycle stages what those chapters own as processes. Its *Upgrade Lifecycle* overlaps chapter 11.

Chapters 08 and 14 duplicate the nine-line `mosaic ...` command list verbatim and both carry a *Manifest Generation* section making related but non-identical claims, with neither deferring to the other. Their prose pointers are mutually consistent — 08 says chapter 14 defines the Developer Platform, 14 says the SDK is one component within it — so the overlap is in the material, not the framing. Chapter 14 also enumerates the harness capability list before correctly deferring to chapter 15.

The same lifecycle stages recur in MEG-005's Supervisor and startup chapters, so the ownership question spans two documents.

**Resolution:**

## Q-070 — MEG-006 cites no MIP at all, while depending on two

**Status:** `Open`
**Where:** [MEG-006 index](../docs/engineering/guides/meg-006-module-platform/index.md), [references](../docs/engineering/guides/meg-006-module-platform/references.md), [ch02](../docs/engineering/guides/meg-006-module-platform/02-module-manifest.md)

Chapter 02 states that the authoritative manifest contract is [MIP-002](../docs/engineering/protocols/mip-002-module-manifest-protocol/index.md). The index lists only MEG-001 to MEG-005 as required reading, and `references.md` contains no MIP entry whatsoever.

MIP-005 — the Module Adapter Contract Protocol these chapters presuppose — is referenced nowhere in MEG-006 and is itself a published stub with no chapters (Q-019). The adapter contract MEG-006 is built on is therefore both uncited and unwritten.

**Resolution:**

## Q-071 — Two incompatible ADR numbering schemes coexist across the corpus

**Status:** `Open`
**Where:** [MEG-006 ch16](../docs/engineering/guides/meg-006-module-platform/16-adrs.md), [ch15](../docs/engineering/guides/meg-006-module-platform/15-test-harness.md), MAC-001, MEG-002, MDL-001, MDS-001, MDP-002

MEG-006 uses document-scoped identifiers (`MEG-006 ADR-001` to `ADR-004`), as do MAC-001 and MEG-002. MDL-001 owns a **global** ADR-001 to ADR-004, MDS-001 owns ADR-084 onwards, and MDP-002 owns ADR-163 to ADR-176. MEG-006's four identifiers therefore duplicate MDL-001's numerically.

MEG-006 chapter 15 cites a bare "ADR-004", which under the global scheme resolves to MDL-001's record rather than MEG-006's — so the ambiguity is already producing a wrong reference.

Q-024 records a narrower numbering conflict within the deferred proposals; this entry is the corpus-wide version, and both should be settled together.

**Resolution:**

## Q-072 — Sixteen of MEG-006's twenty decision areas have no record

**Status:** `Open`
**Where:** [MEG-006 ch16](../docs/engineering/guides/meg-006-module-platform/16-adrs.md), *Decision Areas*

The chapter contains four complete decision records with Context, Decision, Alternatives, Consequences and Implementation Implications, so unlike MEG-003's equivalent it is genuine content. But it lists twenty decision areas and records only four. Manifest-Driven Platform, Permission Model, Capability Lifecycle, Dependency Resolution Strategy, Marketplace Compatibility, Module Isolation and ten others have no record anywhere in the repository.

Several of those unrecorded areas are exactly the subjects this rewrite found to be contradictory or unspecified — Permission Model (Q-060, Q-061), Module Isolation (Q-066), Capability Lifecycle (Q-062) — which suggests the missing records are the reason those chapters disagree.

**Resolution:**

## Q-087 — MEG-002 chapter 16 duplicates MEG-008 and cites it nowhere

**Status:** `Open`
**Where:** [MEG-002 ch16](../docs/engineering/guides/meg-002-event-driven-runtime/16-correlation-and-observability.md), [references](../docs/engineering/guides/meg-002-event-driven-runtime/references.md)

Chapter 16 runs to 420 lines covering the three observability pillars, correlation and causation identifiers, distributed tracing, structured logging, metrics, health and privacy. [MEG-008](../docs/engineering/guides/meg-008-observability/index.md) has a dedicated chapter for each.

`MEG-008 — Observability` appears in the whole of MEG-002 exactly once: as a bare bullet in `references.md`, under a *Planned Engineering Specifications* heading although it is published (Q-058). A grep of the folder returns no other occurrence, so the chapter that duplicates the observability specification never refers the reader to it.

MEG-002 chapter 16 also parallels MEG-005 chapter 19, whose redaction list is similar but not identical, with no citation either way. The substantive divergences are recorded as Q-085.

**Resolution:**

## Q-088 — MEG-002 chapter 17 and MEG-005 chapter 11 are the same chapter

**Status:** `Open`
**Where:** [MEG-002 ch17](../docs/engineering/guides/meg-002-event-driven-runtime/17-runtime-shutdown.md), [MEG-005 ch11](../docs/engineering/guides/meg-005-runtime-architecture/11-shutdown.md)

Both cover runtime shutdown at the same depth: signals, the initiating-request list, admission closure, worker cancellation, the resource-ownership rule, forced-shutdown fallback, health progression, restart recovery, testing and the anti-pattern set all appear in both.

Deciding which document owns runtime shutdown is an authority decision, and it must be made before Q-082 and Q-036 can be settled — those record that the two chapters give incompatible stage orderings and different deadline values for the same procedure.

MEG-002 chapter 17 additionally contains no cross-references at all: it names MEG-002 once as bare text and links nothing, despite depending on retry, idempotency and observability material owned by its own chapters 12, 13 and 16, and on durable retry state described by chapter 20.

**Resolution:**

## Q-089 — Chapter 20 restates chapters 07 and 12 to 15

**Status:** `Open`
**Where:** [MEG-002 ch20](../docs/engineering/guides/meg-002-event-driven-runtime/20-v2-event-backbone.md)

Chapter 20 compresses the delivery, idempotency, ordering and retry rules that chapters 07 and 12 to 15 own, in different wording and — as Q-083 records — at a different normative strength. Its Transactional Outbox and Retry And Dead Letters sections describe a concrete PostgreSQL mechanism for what chapter 17's Retry Queue describes abstractly, with no cross-reference either way. Chapter 17 never mentions dead letters, which chapter 20 treats as the terminal state of exhausted retries.

Whether chapter 20 supersedes those chapters or merely summarises them depends on the lifecycle question in Q-084.

**Resolution:**

---

# Underspecified — needs domain knowledge

These cannot be made concrete by rewriting. The facts are not in this repository.

## Q-013 — Where do transaction responsibilities live?

**Status:** `Open`
**Where:** [MEG-004 ch03](../docs/engineering/guides/meg-004-hexagonal-architecture/03-driving-ports.md), *Transactions*

"Those responsibilities belong elsewhere within the architecture" names no owner. Chapters 09 and 10 look like the likely home, but that could not be confirmed, so no cross-reference was invented.

Note that [MAD-001](../docs/engineering/architecture/mad-001-transactional-store-extensibility/index.md) records the Platform transaction boundary decision and may already answer this.

**Resolution:**

## Q-014 — The "Application layer" is never defined

**Status:** `Open`
**Where:** MEG-004, referenced in ch03, never defined

Chapter 03 places Driving Ports in "the Application layer immediately surrounding the Domain". No chapter defines that layer, and it does not appear in the guide's own modelling guidelines. Related to Q-001.

**Resolution:**

## Q-015 — Go examples carry no real signatures

**Status:** `Open`
**Where:** MEG-004, throughout

Every Go example is elided: `FindByID(...)`, `Metadata(...)`. Real parameter and return types appear nowhere in the guide.

This is the largest single contributor to the "too abstract" problem in this document. Filling it in requires the actual SDK contract, which is the province of [MEG-015](../docs/engineering/guides/meg-015-platform-foundation-implementation/03-platform-contracts.md) and [MIP-004](../docs/engineering/protocols/mip-004-platform-sdk-contract-protocol/index.md).

**Resolution:**

## Q-016 — Unexplained phrases that read as placeholders

**Status:** `Open`
**Where:** MEG-004 chapters 05, 06, 07

- ch05 *Multiple Adapters*: "This is the Platform foundation value proposition of Ports and Adapters" — the phrase denotes nothing defined anywhere.
- ch06 *Authorisation*: "Authorisation decisions should **generally** occur before entering the Domain" — the hedge implies exceptions, presumably data-scoped permissions the Domain must enforce, but none are named.
- ch07 *External Service Adapters*: "retries (where appropriate)" — no criterion. The chapter's *Retry Behaviour* section distinguishes infrastructure from runtime retries but never says when to use either.

**Resolution:**

## Q-017 — Diagrams that draw lists as dependency chains

**Status:** `Open`
**Where:** MEG-004 ch09, ch11, ch12

Several retained diagrams render enumerations as linear chains, implying dependencies that probably do not exist:

- ch09 *Infrastructure Assembly*: `Configuration → Logger → Database → Blob Storage → HTTP Client`
- ch09 *Adapter Assembly*: `Database → Playback Repository → Metadata Repository → Collection Repository` — the three repositories almost certainly each depend on the Database, not on one another
- ch11 *The Runtime Is Infrastructure*: `HTTP → Runtime → Database → Blob Storage → External APIs`
- ch12 *Testing Strategy*: `Domain → Application → Adapters → Integration → End-to-End`

Each should probably become a branching diagram or a plain list. Deciding which requires knowing the real structure.

**Resolution:**

## Q-018 — Runtime Assembly chain is ambiguous

**Status:** `Open`
**Where:** [MEG-004 ch09](../docs/engineering/guides/meg-004-hexagonal-architecture/09-composition-root.md), *Runtime Assembly*

`Event Publisher → Runtime Adapter → Playback Service` — whether this means the Service receives the Adapter, or something else, is not stated anywhere in the guide.

**Resolution:**

## Q-019 — MIP-004, MIP-005 and MIP-006 have no chapters

**Status:** `Open`
**Where:** [MIP-004](../docs/engineering/protocols/mip-004-platform-sdk-contract-protocol/index.md), [MIP-005](../docs/engineering/protocols/mip-005-module-adapter-contract-protocol/index.md), [MIP-006](../docs/engineering/protocols/mip-006-generation-composition-protocol/index.md)

Each states a real contract in three paragraphs on its landing page and has no chapters. Each now opens with an "Outline only" notice, and `validate_docs.py` reports all three as `book-stub`. These are the only three findings the validator still reports.

They need contract chapters written, which requires the actual contract.

**Resolution:**

## Q-030 — The Resource Manager is never defined

**Status:** `Open`
**Where:** [MEG-005 ch09](../docs/engineering/guides/meg-005-runtime-architecture/09-resource-management.md), *Resource Allocation* and *Resource Independence*

The chapter repeatedly assigns behaviour to a Resource Manager — it allocates, it provides resource information, it stays independent of scheduling — but has no "What Is The Resource Manager?" section, unlike every peer chapter. Whether it is a Runtime Service in its own right, a facet of the Runtime Kernel, or a notional grouping of per-owner logic is never stated.

*Resource Ownership* then assigns every concrete resource to some other component — Worker Manager, Scheduler, Execution Engine, Capability Registry — which reads as though the Resource Manager owns nothing directly. That may be deliberate or it may be the gap.

**Resolution:**

## Q-031 — Worker pool scaling strategies are named but undefined

**Status:** `Open`
**Where:** [MEG-005 ch07](../docs/engineering/guides/meg-005-runtime-architecture/07-worker-manager.md), *Scaling*

`Static`, `Adaptive` and `Configured` appear as the three permitted pool strategies with no definition here or anywhere else in the folder, and the distinction between Static and Configured is not self-evident. All three terms were preserved without gloss.

**Resolution:**

## Q-032 — Priority tiers never connect to admission

**Status:** `Open`
**Where:** [MEG-005 ch08](../docs/engineering/guides/meg-005-runtime-architecture/08-scheduler-architecture.md), *Priority*; [ch09](../docs/engineering/guides/meg-005-runtime-architecture/09-resource-management.md), *Resource Admission*

Chapter 08 gives three tiers with example workloads and then states "Priority influences admission. Not business semantics." Nothing says what admission does with priority — whether high-priority work preempts, jumps the queue, or is merely evaluated earlier — and chapter 09, which owns admission, does not mention priority at all.

**Resolution:**

## Q-033 — Generation garbage collection policy is defined nowhere

**Status:** `Open`
**Where:** [MEG-005 ch14](../docs/engineering/guides/meg-005-runtime-architecture/14-supervisor-model.md), *Atomic Runtime Activation* and *Atomic Upgrade Model*

"Previous runtimes should be retained until later garbage collection policy permits deletion", and a `Garbage Collect Later` node, both defer to a retention policy that no document in the repository defines — not MEG-005, not [MEG-006](../docs/engineering/guides/meg-006-module-platform/index.md), not [MOP-001](../docs/engineering/operations/mop-001-observability-operations/index.md). How many previous Generations are kept, and on what trigger, is unresolved.

This matters operationally: Generations carry a Platform, a Shell and Modules, so an undefined retention policy is an unbounded disk commitment on a self-hosted installation.

**Resolution:**

## Q-034 — Configuration precedence and activation turn on two undefined terms

**Status:** `Open`
**Where:** [MEG-005 ch18](../docs/engineering/guides/meg-005-runtime-architecture/18-configuration-and-secrets.md), *Configuration sources and precedence* and *Schema and activation*

The precedence ordering ends with "explicitly permitted runtime overrides" without saying who grants the permission, what may be overridden, or how the permission is declared. Every other level in the ordering names its owner.

Separately, structural configuration changes get a warm-and-switch path with "restart is the fallback when a seamless transition is unsafe". The entire branch turns on *unsafe*, and no test for it is given.

**Resolution:**

## Q-035 — Migration strategy is hedged into a non-decision

**Status:** `Open`
**Where:** [MEG-005 ch20](../docs/engineering/guides/meg-005-runtime-architecture/20-persistence-and-recovery.md), *Migration strategy*

`pgroll`-style dual schema views are recommended "where practical", leaving it unclear whether this is the required mechanism, a recommendation or an aspiration, and no decision record covers it. The surrounding text makes a hard normative claim about pre-migration backups, so the softness here reads as unintentional rather than deliberate.

**Resolution:**

## Q-036 — Shutdown deadline value is unattributed

**Status:** `Open`
**Where:** [MEG-005 ch11](../docs/engineering/guides/meg-005-runtime-architecture/11-shutdown.md), *Shutdown Deadlines*

The only concrete number in the chapter, 60 seconds, appeared solely as a diagram node label with no text stating whether it is a default, a recommendation or an illustration, while the timeout is simultaneously described as configurable. It was preserved hedged as an example rather than promoted to a default.

**MEG-002 states a different number for what appears to be the same budget.** [MEG-002 ch17](../docs/engineering/guides/meg-002-event-driven-runtime/17-runtime-shutdown.md) *Timeouts* gives **30 seconds**, also only inside a Mermaid node label, also unattributed, also described as configurable. Either the two documents disagree, or these are two nested budgets that nothing distinguishes. See Q-088, which records that the two chapters are otherwise the same chapter, and Q-082, which records that they also order the shutdown stages incompatibly.

**Resolution:**

## Q-049 — Nobody owns transaction scope

**Status:** `Open`
**Where:** [MEG-003 ch12](../docs/engineering/guides/meg-003-domain-driven-design/12-repositories.md), *Repository Responsibilities*, *Transactions* and *Repository Lifetime*

The chapter says twice that Repositories do not own transactions — "Repositories participate in transactions. They do not own them" — but never names who does. [MEG-004 ch07](../docs/engineering/guides/meg-004-hexagonal-architecture/07-driven-adapters.md) separately lists transaction management among Repository Adapter responsibilities.

These are probably reconcilable, with the Adapter running the mechanics while something above decides the scope, but MEG-003 does not say so and naming the owner would mean inventing it.

This is the MEG-003 face of Q-013, which records the same gap in MEG-004. [MAD-001](../docs/engineering/architecture/mad-001-transactional-store-extensibility/index.md) may already answer both.

**Resolution:**

## Q-050 — Read models and CQRS are gestured at but never sited

**Status:** `Open`
**Where:** [MEG-003 ch12](../docs/engineering/guides/meg-003-domain-driven-design/12-repositories.md), *Queries*

The section introduces a Read Model and a Continue Watching View and says the design "aligns naturally with CQRS", without saying whether Mosaic adopts CQRS, where read models live, or what "often belong elsewhere" resolves to.

`read model` appears in [MEG-005 ch17](../docs/engineering/guides/meg-005-runtime-architecture/17-graphql-projection.md) and in MEG-010, so an answer may already exist — but deciding which document owns the concept is an authority decision.

**Resolution:**

## Q-051 — Cross-Aggregate consistency has no decision rule

**Status:** `Open`
**Where:** [MEG-003 ch14](../docs/engineering/guides/meg-003-domain-driven-design/14-domain-invariants.md), *Cross-Aggregate Rules*; [ch08](../docs/engineering/guides/meg-003-domain-driven-design/08-aggregates.md), *Consistency Boundary*

Chapter 14 says cross-Aggregate rules "should rarely be enforced through distributed transactions" and that "only rules requiring immediate consistency belong inside one Aggregate", without saying how an engineer determines that a rule requires immediate consistency. `Library Storage Quota` and `Subscription Limits` are named as examples and left unclassified.

Chapter 08 hedges the same boundary from the other side: outside the Aggregate "only eventual consistency should **generally** be assumed", naming no exception.

Separately, the two chapters' *Mosaic Examples* sections give different answers for the same concepts — Library is "media ownership / import state / source configuration" in chapter 08 and "importing media / source ownership / library consistency" in chapter 09, and Collection gains "duplicate prevention" in 09 that 08 omits.

**Resolution:**

## Q-052 — Names used once and never defined

**Status:** `Open`
**Where:** MEG-003 chapters 04, 05, 06, 10, 12

Six terms appear in normative examples without being defined anywhere in the repository. Each was preserved verbatim because guessing an expansion would settle it:

- **Infuse Module** — [ch04](../docs/engineering/guides/meg-003-domain-driven-design/04-bounded-contexts.md) *Modules And Contexts*, presented as a Playback Context module. Appears nowhere else; unclear whether it is a planned integration or a placeholder, and whether it belongs alongside Jellyfin, Plex, Stremio, TMDB, AniList and Trakt.
- **Primary Metadata** — [ch05](../docs/engineering/guides/meg-003-domain-driven-design/05-context-maps.md) *Module Relationships*, sourcing `MetadataFetched`. Either a distinct context no chapter introduces, or loose phrasing for the Metadata Context.
- **Observability Context** — ch05 *Conformist*, its only appearance. Absent from the Bounded Context list and from the Mosaic Context Map, so chapter 05's own guideline that every Bounded Context appears in a Context Map is arguably violated by its own example.
- **Metadata Entity** — [ch06](../docs/engineering/guides/meg-003-domain-driven-design/06-entities.md) *Entity Ownership*. Elsewhere metadata is treated as an attribute that changes on a Media Entity, so it is unclear whether this is a modelled Entity or a placeholder.
- **Recommendation Created** — [ch10](../docs/engineering/guides/meg-003-domain-driven-design/10-domain-services.md) *Domain Events*, in the position of an intermediate value or event. If it is an event it collides with the rule that only Aggregates raise events, because the node precedes the Aggregate.
- **MOS Files** — [ch12](../docs/engineering/guides/meg-003-domain-driven-design/12-repositories.md) *Multiple Storage Engines*, listed as a storage technology beside PostgreSQL, DuckDB, Blob Storage and Filesystem. The string appears nowhere else in the repository, not even in MEG-003's own glossary.

Chapter 08 *Aggregate Behaviour* has a milder version of the same problem: "Services coordinate. Aggregates decide." never says whether these are Domain Services or application services.

**Resolution:**

## Q-053 — Subdomain classification is incomplete

**Status:** `Open`
**Where:** [MEG-003 ch03](../docs/engineering/guides/meg-003-domain-driven-design/03-subdomains.md), *Mosaic Core Domains*

"The following are currently considered Core Domains" names Library, Playback and Metadata, but *Purpose* lists nine capabilities and the Supporting and Generic sections account for further names. Several — Collections, Users, Search, Modules — appear as subdomains without a category.

Whether the uncategorised ones are Supporting by default or simply unclassified is a strategic-investment decision, which is exactly what the chapter says subdomain classification is for.

**Resolution:**

## Q-054 — Domain ownership names teams that may not exist

**Status:** `Open`
**Where:** [MEG-003 ch03](../docs/engineering/guides/meg-003-domain-driven-design/03-subdomains.md), *Domain Ownership*

The chapter requires every subdomain to have a clearly defined owner and names a "Playback Team" and a "Metadata Team". Nothing in the repository establishes that these teams exist, or that per-team ownership is the intended model rather than illustration. The labels were folded into prose verbatim, without softening or hardening the claim.

**Resolution:**

## Q-055 — Rules stated without the detail needed to apply them

**Status:** `Open`
**Where:** [MEG-003 ch14](../docs/engineering/guides/meg-003-domain-driven-design/14-domain-invariants.md), [ch15](../docs/engineering/guides/meg-003-domain-driven-design/15-modelling-guidelines.md)

Three places state a rule and stop short of what an engineer would need to follow it:

- ch14 *Value Objects* gives candidate invariants as "non-negative", "finite" and "valid range" without stating what the valid range for `Duration` is, or naming who decides.
- ch14 *Anti-Patterns* declares six practices prohibited in one-line subsections with no statement of what enforcement looks like — review gate, lint, or nothing.
- ch15 *Modelling Checklist* says "If any answer is 'no', continue modelling. Implementation should wait", naming no reviewer or approval step, so whether this is a hard gate or advice is unclear.

Separately, ch15 *Raise Domain Events* says "That question belongs to the runtime" — its only mention of a runtime — without linking [MEG-002](../docs/engineering/guides/meg-002-event-driven-runtime/index.md), although MEG-004 links it for the same separation. Adding that cross-reference would assert a dependency between MEG-003 and MEG-002 that is not recorded.

**Resolution:**

## Q-073 — The manifest has three filenames and two scopes

**Status:** `Open`
**Where:** [MEG-006 ch02](../docs/engineering/guides/meg-006-module-platform/02-module-manifest.md), [ch03](../docs/engineering/guides/meg-006-module-platform/03-discovery.md), [ch08](../docs/engineering/guides/meg-006-module-platform/08-module-sdk.md), [ch13](../docs/engineering/guides/meg-006-module-platform/13-platform-guidelines.md), [ch14](../docs/engineering/guides/meg-006-module-platform/14-developer-platform.md), [glossary](../docs/engineering/guides/meg-006-module-platform/glossary.md)

Chapter 02 is titled *Module Manifest*, its example is Module-scoped (`id: anilist`), and the glossary makes *Module Manifest* the artefact the Supervisor consumes. But chapters 03 and 13 say every **capability** carries a `capability.yaml`, while chapters 08 and 14 say tooling generates `module.yaml`. "Capability Manifest" is used across six MEG-006 files — including as the first node of chapter 10's normative *Configuration Model* diagram and inside the glossary's own *Capability Descriptor* entry — yet the glossary defines *Manifest* and *Module Manifest* and never *Capability Manifest*.

Whether the declared unit is the Go Module or the capability determines discovery, dependency resolution and the entire composition model. MIP-002 is named as the protocol authority without resolving it, and this cannot be settled editorially.

**Resolution:**

## Q-074 — MEG-006 terms used once in normative text and defined nowhere

**Status:** `Open`
**Where:** MEG-006 chapters 03, 05, 06, 08, 15

The MEG-006 counterpart to Q-052. Each was confirmed by grep to appear only where cited:

- **capability criticality** — [ch06](../docs/engineering/guides/meg-006-module-platform/06-activation.md) *Partial Platform Activation* says criticality "should be declared within the manifest" so the Runtime can distinguish optional from critical failures. No such field exists in MIP-002. This is the sole mechanism deciding whether an activation failure aborts platform startup.
- **Registered Module Capability** — ch06 *Purpose* defines activation as the transition from this to an Operational Capability. Neither term is defined for Module capabilities; "Operational Capability" is defined in MEG-005's glossary for Runtime Services.
- **Composition Root** — ch06 *Capability Construction* has the Runtime construct capabilities "through the Composition Root", used once, unlinked. MEG-004's Composition Root is a whole-application assembly concept, not a per-capability constructor.
- **Marketplace Cache, Enterprise Repository, Development Workspace** — [ch03](../docs/engineering/guides/meg-006-module-platform/03-discovery.md) *Discovery Sources*, each appearing exactly once in the repository. The chapter says the Module Catalogue derives from "configured discovery sources" without saying who configures them. Whether a Supervisor must implement four source types or one is undecided.
- **`machine-learning`, `FanArt`, `Local Artwork`, `Local Metadata`** — [ch05](../docs/engineering/guides/meg-006-module-platform/05-dependency-resolution.md), used as concrete capability identifiers in optional-dependency and grouping examples.
- **TorBox** — [ch15](../docs/engineering/guides/meg-006-module-platform/15-test-harness.md) *Media*, listed beside Jellyfin as a production integration; appears once in the entire repository.
- **Runtime SDUI** — ch15, listed as a real Platform component that stays real under test. Defined only in MEG-005's glossary and MDS-001/MDS-003; `SDUI` is never expanded anywhere in MEG-006.

**Resolution:**

## Q-075 — Chapter 11 versions five artefacts, none of which is a MIP contract

**Status:** `Open`
**Where:** [MEG-006 ch11](../docs/engineering/guides/meg-006-module-platform/11-versioning.md)

The chapter mandates a per-capability `version`, a `manifestVersion`, an SDK version constraint, a Runtime version, per-contract versions, and a Runtime/SDK/manifest compatibility matrix. The repository rule, from [MDG-001 ch03](../docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md), is that only the contract a MIP defines carries a version.

Manifest and SDK versions arguably belong to MIP-002 and MIP-004, but chapter 11 never says so and neither MIP declares them. Capability version and Runtime version have no MIP behind them at all. Someone must decide which of these are MIP contract versions, to be declared in the owning MIP, and which are artefact versions outside the rule.

**Resolution:**

## Q-076 — MEG-006's SDK examples carry no real signatures, and MIP-004 is a stub

**Status:** `Open`
**Where:** [MEG-006 ch08](../docs/engineering/guides/meg-006-module-platform/08-module-sdk.md), throughout

Every SDK call is elided — `Schedule(...)`, `Publish(...)`, `Subscribe(...)`, `Info(...)`, `FindCapability(...)`, `Assert(...)`. This is the same defect Q-015 records for MEG-004, and it has the same cause and a worse consequence here: chapter 08 never cites [MIP-004](../docs/engineering/protocols/mip-004-platform-sdk-contract-protocol/index.md) or MEG-015 at all, and MIP-004 is itself a published stub with no content chapters (Q-019).

The contract this chapter describes therefore has no published owner to defer to. Filling in the signatures requires the actual SDK contract; adding the cross-reference requires deciding that MIP-004 owns it.

**Resolution:**

## Q-077 — The Developer Platform describes tooling with no evidence it exists

**Status:** `Open`
**Where:** [MEG-006 ch14](../docs/engineering/guides/meg-006-module-platform/14-developer-platform.md)

The chapter alternates between settled-fact phrasing and hedges for the same subject — "The Mosaic CLI **is** the primary developer interface", "The Development Supervisor **owns** the local development lifecycle", against "the exact command syntax may evolve". A reader cannot tell whether `mosaic dev` is runnable today or is being commissioned. Tense was deliberately left unchanged, because changing it changes what the document claims is built.

Three further gaps in the same chapter:

- **Development Supervisor** is called "a development-only Supervisor implementation" while being required to share production orchestration, validation, build invocation, health-check and activation behaviour "wherever practical", and the Anti-Patterns section prohibits a Development Runtime Fork. Whether that means one codebase with a development mode or two implementations kept in sync is the difference between a config flag and a maintenance burden.
- **"Wherever practical"** is the load-bearing hedge in a must-not-fork chapter, while *Production Fidelity* supplies a precise five-item list of permitted differences. Either the list is exhaustive and the hedge should go, or the hedge is real and the list is illustrative.
- **`mosaic package` and `mosaic publish`** commit to a six-stage pipeline including Sign And Upload, and to package reproducibility and provenance, while no repository document defines a signing model, a package format or a Module Catalogue protocol. The chapter says as much itself.

**Resolution:**

## Q-078 — Contract exposure and compatibility declaration have no named owner

**Status:** `Open`
**Where:** [MEG-006 ch17](../docs/engineering/guides/meg-006-module-platform/17-contributor-guidance.md), *Before Exposing Contracts*, *Before Releasing*, *Marketplace Readiness*

The chapter says public Runtime contracts become "long-lived commitments" but never says who approves a capability exposing a new public contract, or where that approval is recorded. *Before Editing The Runtime* names "architectural review" for Runtime changes; whether the same body governs contract exposure is unstated across MEG-006.

Separately, two checklists require compatibility to be "declared". Chapter 11 defines an SDK version, a manifest version and a compatibility matrix, but nothing states which of those a capability author must declare at release and which the Runtime derives. Resolving it would mean inventing a release contract.

**Resolution:**

## Q-090 — Retry is required to be bounded by nothing in particular

**Status:** `Open`
**Where:** [MEG-002 ch13](../docs/engineering/guides/meg-002-event-driven-runtime/13-retry-strategy.md), *Maximum Retries*, *Retry Budget*, *Retry Cancellation*, *Retry Classification*

The chapter prohibits infinite retries and requires retries to terminate, but states no maximum, no default and no configuration point. The retained diagram shows four attempts and is captioned as illustration. *Retry Budget* names three dimensions — maximum retries, maximum retry duration, maximum concurrent retries — with no values and no enforcing component.

Two further gaps in the same chapter: *Retry Cancellation* makes restart-resumption an opt-in ("unless explicitly configured") while *Retry Persistence* makes it a default expectation ("should survive runtime restarts"), naming neither the mechanism nor who decides which retries are correctness-critical; and *Retry Classification* says errors "should communicate retry intent" through "future runtime APIs" that do not exist, while the runtime is forbidden from inspecting error messages.

This compounds chapter 14's guarantee that "every accepted event will eventually be delivered (subject to retry policy)" — with no stated bound, that guarantee has no floor.

**Resolution:**

## Q-091 — Backpressure states no threshold anywhere

**Status:** `Open`
**Where:** [MEG-002 ch15](../docs/engineering/guides/meg-002-event-driven-runtime/15-backpressure.md), *Bounded Queues*, *Queue Growth*, *Adaptive Scaling*, *Mosaic Guidelines*

The chapter mandates a "maximum size" for every queue, a bounded worker pool, action "before queues become completely full", a named `Near Capacity` state and bounded scaling — with no number, formula, default, configuration surface or owner anywhere. `Near Capacity` is a named state with no entry condition.

Separately, *Load Shedding* closes with "The runtime should understand this distinction" without saying how work is classified as sheddable. This is load-bearing for modules: *Module Isolation* requires backpressure against a misbehaving module, but a module defines its own event types, so the runtime has no stated basis for judging them.

Values are a capacity-planning decision and may belong to MEG-005 chapter 09 (Resource Management), which Q-030 already records as never defining the Resource Manager.

**Resolution:**

## Q-092 — Idempotency defines the obligation but no detection mechanism

**Status:** `Open`
**Where:** [MEG-002 ch12](../docs/engineering/guides/meg-002-event-driven-runtime/12-idempotency.md), *Event Identity*, *Event Recording*, *Event Replay*

Chapters 07, 08 and 09 all forward-reference this chapter, and it does discharge the obligation normatively: every subscriber must be idempotent, duplicate delivery must produce the same business state, correctness must not depend on exactly-once. What it never defines is **how a duplicate is detected**. Using the Event ID is a `should`, maintaining a processed-event store is a `may`, and where that store lives, who owns it and what the deduplication key is are unstated. A subscriber can satisfy every `must` while performing no duplicate detection at all.

The chapter also gives no retention window for processed Event IDs, and that collides with its own *Event Replay* section: replay must remain safe and intentionally re-delivers historical events, but indefinite retention makes replay a no-op unable to rebuild a projection, which is the stated point of replay. If entries expire, nothing says when.

**Resolution:**

## Q-093 — Ordering guarantees name nothing that enforces them

**Status:** `Open`
**Where:** [MEG-002 ch14](../docs/engineering/guides/meg-002-event-driven-runtime/14-event-ordering.md), *Per-Entity Ordering*, *Runtime Guarantees*, *Replay Ordering*, *Purpose*

*Per-Entity Ordering* says ordering "should generally be scoped to a business entity" and "provides deterministic behaviour", while *Runtime Guarantees* states the runtime does not guarantee subscriber or cross-capability ordering. No partition key, per-entity queue or serialisation point is named, and the hedge "should generally" names no exception.

Two further unqualified escape hatches in the same chapter: business state should converge "regardless of delivery order **wherever practical**", and replay "should preserve original occurrence order **where practical**" — neither naming the impractical case, and *Replay Ordering* naming no mechanism that preserves occurrence order.

Chapter 14 is the owner chapter 12 declines to name when it says "ordering guarantees belong elsewhere", but the pointer is unlinked and unnamed in both directions.

**Resolution:**

## Q-094 — Publisher-side validation has no defined scope or owner

**Status:** `Open`
**Where:** [MEG-002 ch08](../docs/engineering/guides/meg-002-event-driven-runtime/08-publishers.md), *Constructing Events*; [ch07](../docs/engineering/guides/meg-002-event-driven-runtime/07-event-bus.md); [ch09](../docs/engineering/guides/meg-002-event-driven-runtime/09-subscribers.md)

Chapter 07 excludes business validation from the Event Bus and chapter 08 assigns validation to the publisher, but chapter 09 also requires subscribers to validate on receipt — supported version, required payload fields, mandatory identifiers, business preconditions. Whether publisher-side validation is envelope-level, payload-level or both is unstated, as is whether MIP-001 owns the rule.

Separately, chapter 08's *Publisher Failure* permits treating a publication failure as non-fatal "unless the runtime explicitly guarantees deferred publication", without saying whether such a guarantee exists. The Transactional Outbox reference two sections earlier is introduced as industry practice rather than a Mosaic commitment, so a reader cannot tell whether the escape clause is live — though chapter 20 does describe an outbox, unreferenced from here (Q-089).

**Resolution:**

## Q-095 — Checkpointing is asserted, undefined, and contradicts two sections

**Status:** `Open`
**Where:** [MEG-002 ch10](../docs/engineering/guides/meg-002-event-driven-runtime/10-worker-lifecycle.md), *Long Running Tasks*, *Restart Behaviour*, *Anti-Patterns*

*Long Running Tasks* says tasks should "checkpoint where practical", without defining what a checkpoint is, where it lives, or how a restarted worker resumes from one. *Restart Behaviour* argues restart is safe *because* "business state belongs elsewhere", and the *Permanent Mutable State* anti-pattern prohibits workers retaining business state between tasks.

A checkpoint looks like exactly the worker-held progress state those two sections rule out — unless it is stored outside the worker, which the chapter does not say.

The same chapter's *Worker Pools* closes "Worker pools are discussed further in future runtime specifications" with no identifier, where the convention requires an unavailable reference to be marked `planned; not yet published`.

**Resolution:**

## Q-096 — Degraded and unhealthy are illustrated but never distinguished

**Status:** `Open`
**Where:** [MEG-002 ch16](../docs/engineering/guides/meg-002-event-driven-runtime/16-correlation-and-observability.md), *Health*

The section gives example strings — `External API unavailable` for degraded, `Database disconnected` for unhealthy — but states no rule for classifying a condition into one or the other, and never says what the runtime does differently in response, in particular whether a degraded capability still receives work.

Related: *Privacy* makes a must-level prohibition defeasible with "unless explicitly required", naming no approver, declaration mechanism or review path, while MEG-005 chapter 19 states the equivalent rule flatly with no exemption. And nothing states whether runtime events such as `WorkerStarted` are subject to the chapter's own correlation rules — they are declared "runtime events rather than business events", yet the guidelines require every workflow to carry a Correlation ID and `WorkerStarted` has no workflow.

**Resolution:**

## Q-097 — Architectural review has no owner or trigger

**Status:** `Open`
**Where:** [MEG-002 ch19](../docs/engineering/guides/meg-002-event-driven-runtime/19-contributor-guidance.md), *Before Changing Runtime Behaviour*

Seven categories of change "should require architectural review", but nothing says who reviews, what artefact records the outcome, or whether chapter 18's ADR mechanism is that artefact. This is a governance boundary rather than an editorial gap, and it is the same shape as Q-078, which records that MEG-006 never names who approves a capability exposing a public contract.

**Resolution:**

---

# Factual and naming defects

Small, but each changes meaning, so none were fixed during the rewrite.

## Q-020 — `ArtworkProvider` or `ArtworkStore`?

**Status:** `Open`
**Where:** [MEG-004 ch02](../docs/engineering/guides/meg-004-hexagonal-architecture/02-ports.md), *Ports Are Small*

Used once as `ArtworkProvider`; every other mention across the guide is `ArtworkStore`. Likely a typo in a normative example, but the two names imply different Port responsibilities.

**Resolution:**

## Q-021 — Stale repository trees describing a layout that no longer exists

**Status:** `Open`
**Where:** [MEG-004 index](../docs/engineering/guides/meg-004-hexagonal-architecture/index.md), [MEG-005 index](../docs/engineering/guides/meg-005-runtime-architecture/index.md), [MEG-003 index](../docs/engineering/guides/meg-003-domain-driven-design/index.md), [MEG-006 index](../docs/engineering/guides/meg-006-module-platform/index.md), [MEG-002 index](../docs/engineering/guides/meg-002-event-driven-runtime/index.md), all *Repository Structure*

The tree names `README.md` as the folder's landing file; the real file is `index.md`. The folder path shown, `engineering/meg/MEG-004 Hexagonal Architecture/`, does not match the real `docs/engineering/guides/meg-004-hexagonal-architecture/`.

Preserved verbatim under the no-invention rule. Other specifications may carry the same stale tree.

MEG-005, MEG-003, MEG-006 and MEG-002 confirm this is a pattern rather than a one-off. Each shows `engineering/meg/<Document Title>/` containing `README.md`, with the same two defects, while the chapter filenames they list are correct. Only the folder path and the landing filename are stale. Whether these trees are meant to be accurate or merely illustrative should be settled once and applied to every specification that carries one.

**Resolution:**

## Q-022 — MDP-001 listed twice with an identical label

**Status:** `Open`
**Where:** [MEG-004 references](../docs/engineering/guides/meg-004-hexagonal-architecture/references.md), [MEG-005 references](../docs/engineering/guides/meg-005-runtime-architecture/references.md), [MEG-003 references](../docs/engineering/guides/meg-003-domain-driven-design/references.md), [MEG-006 references](../docs/engineering/guides/meg-006-module-platform/references.md), [MEG-002 references](../docs/engineering/guides/meg-002-event-driven-runtime/references.md)

Listed once pointing at `index.md` and once at `14-adaptive-tile-model.md`, both labelled "MDP-001 — Adaptive Composition Runtime". The second entry needs a distinguishing label.

All five guides checked so far carry the identical pair, so the fix should be applied to each. All three also file MDP-001 under a *Mosaic Design Specifications* heading although it lives under `docs/engineering/architecture/` — see Q-040, which records that alongside the MEG-005 glossary defects.

**Resolution:**

## Q-023 — MEG-004 index diagram implies a false dependency

**Status:** `Open`
**Where:** [MEG-004 index](../docs/engineering/guides/meg-004-hexagonal-architecture/index.md), *Relationship to MEG*

The diagram renders as one linear chain alternating document identifiers and concept names — `MEG-001 → Engineering Standards → MEG-002 → Reactive Runtime → …` — which reads as "Engineering Standards depends on MEG-002".

Re-wiring it means asserting a dependency structure between the engineering guides that is not recorded anywhere.

**Resolution:**

## Q-024 — Conflicting ADR numbering in the deferred proposals

**Status:** `Open`
**Where:** [MDP-002 ch11](../docs/engineering/architecture/mdp-002-tile-framework/11-tile-governance.md), [ch12](../docs/engineering/architecture/mdp-002-tile-framework/12-tile-decision-history.md), [MDP-001 ch11](../docs/engineering/architecture/mdp-001-adaptive-composition-runtime/11-governance.md)

MDP-002 chapter 11 lists ADR-163 to ADR-167. Chapter 12 defines ADR-168 to ADR-176 covering substantially the same five decisions, with no cross-reference. One numbering scheme is stale.

Separately, MDP-001 chapter 11 lists ADR-149 to ADR-153 as bare table rows; those ADRs are defined nowhere in the repository.

**Resolution:**

## Q-025 — Four ADRs may survive the deferral

**Status:** `Open`
**Where:** [MDP-001 ch12](../docs/engineering/architecture/mdp-001-adaptive-composition-runtime/12-decision-history.md)

Most decision records in this chapter bind only the deferred runtime, but four appear to bind Mosaic regardless:

- **ADR-163** — the client resolves geometry; SDUI never sends coordinates. Chapter 10 says this boundary is still live.
- **ADR-164** — ClearLogo versus Mona Sans title treatment. A concrete v1 rule with no post-v1 gate.
- **ADR-165** — Acrylic Assembly is not material fusion. Cross-references MDS-003 as owner.
- **ADR-166** — Adaptive Composition and Authored Layout as peer client consumption modes. Half of this is v1 today.

Extracting them into a MAD would mean *accepting* decisions on the owner's behalf, so nothing was moved.

**Resolution:**

## Q-037 — Diagrams that draw fan-outs and state machines as linear chains

**Status:** `Open`
**Where:** [MEG-005 index](../docs/engineering/guides/meg-005-runtime-architecture/index.md), [ch01](../docs/engineering/guides/meg-005-runtime-architecture/01-runtime-philosophy.md), [ch03](../docs/engineering/guides/meg-005-runtime-architecture/03-capability-registry.md), [ch14](../docs/engineering/guides/meg-005-runtime-architecture/14-supervisor-model.md)

The MEG-005 counterpart to Q-017. Several retained diagrams draw a straight chain where the structure is plainly not linear, so each asserts relationships the prose never claims:

- ch01 *Runtime Kernel*: `Runtime Kernel → Capability Registry → Execution Engine → Scheduler → Worker Manager → Resource Manager`, while the sentence beneath describes a fan-out — "Every other Runtime component builds upon this foundation". The chain also makes the Registry depend on the Execution Engine, which nothing supports.
- ch03 *Dependency Discovery*: `Recommendations → Requires → Playback → Metadata` literally asserts that Playback depends on Metadata; the prose says only that Recommendations requires both.
- ch14 *Supervisor State Machine*: eleven states wired as one chain ending `Healthy → Updating → Rollback → Recovery → Maintenance`, which claims every healthy system proceeds unconditionally to rollback and then to recovery. The real transition set — which states are terminal, what is reachable from `Recovery`, how `Maintenance` is entered — is stated nowhere.
- ch14 *Atomic Runtime Activation*: a `Healthy?` decision node with no failure edge. The failure path exists only in the following sentence.
- index *Relationship to MEG*: one chain alternating document identifiers and concept names, so it reads as "Engineering Standards depends on MEG-002". The same defect as Q-023 in MEG-004.

Redrawing any of these asserts a structure that is not recorded, so all were left as committed.

**Resolution:**

## Q-038 — "open for module" is a mangled Open/Closed Principle

**Status:** `Open`
**Where:** [MEG-005 ch03](../docs/engineering/guides/meg-005-runtime-architecture/03-capability-registry.md), *Why A Registry Exists*

The closing sentence reads "The Runtime becomes open for module while remaining closed for modification." The intended reference is the Open/Closed Principle — open for *extension* — and MDG-001 terminology replaces *Extension* with *Module*, which looks to have been applied mechanically to a fixed external term of art, leaving ungrammatical text.

The fix could be "open for modules", or restoring "extension" as an external term the terminology mapping should not touch, or a rephrase avoiding both. That is a terminology-authority decision, so the sentence was left byte-identical.

**Resolution:**

## Q-039 — Unverifiable citations used for load-bearing claims

**Status:** `Open`
**Where:** [MEG-005 ch01](../docs/engineering/guides/meg-005-runtime-architecture/01-runtime-philosophy.md), [ch02](../docs/engineering/guides/meg-005-runtime-architecture/02-runtime-kernel.md), [ch12](../docs/engineering/guides/meg-005-runtime-architecture/12-runtime-state.md), [ch13](../docs/engineering/guides/meg-005-runtime-architecture/13-runtime-modelling-guidelines.md)

The operating-system analogy that frames the whole document, and the microkernel claim in chapter 02, both cite `https://operatingsystemsauthority.com/operating-system-kernel` under the link text "Operating Systems". The domain does not correspond to a recognisable standards body, textbook or vendor, unlike the `alistair.cockburn.us` and `microservices.io` citations used elsewhere in the guides.

Chapters 12 and 13 have a milder version of the same problem: a bare Wikipedia "Architectural state" link and a Qt blog post, each appended mid-sentence at the end of a section, reading as filler rather than deliberate references.

All were preserved verbatim. Someone should confirm each source is real and citable, substitute a canonical reference where it is not, and decide whether the surviving ones belong in `references.md` instead of inline.

**Resolution:**

## Q-040 — MEG-005 reference and glossary defects

**Status:** `Open`
**Where:** [MEG-005 references](../docs/engineering/guides/meg-005-runtime-architecture/references.md), [glossary](../docs/engineering/guides/meg-005-runtime-architecture/glossary.md)

Four small defects, each changing meaning rather than wording, so none were fixed:

- MDP-001 is listed beneath *Mosaic Design Specifications* between MDS entries, but it lives under `docs/engineering/architecture/`, not `docs/design/system/`. MEG-003, MEG-004, MEG-006 and MEG-002 file it the same way, so this is a corpus-wide misfiling rather than a MEG-005 slip. The MEG-006 and MEG-002 lists also omit MDS-006 and MDS-007, which exist on disk, while including MDS-008.
- MDS-006 and MDS-007 exist in the repository but are absent from that list, while MDS-008 is present.
- The glossary defines both *Kernel* and *Runtime Kernel* for what appears to be the same component, with overlapping but non-identical content — the *Kernel* entry carries the microkernel comparison and its citation, the *Runtime Kernel* entry carries the small, stable and business-agnostic list. Merging them would drop or relocate a citation.
- *Recovery UI* refers to "the embedded recovery renderer" in lower case, while Embedded Recovery Renderer is defined elsewhere as a capitalised proper noun.

See also Q-022, which covers the duplicated MDP-001 entry in the same file.

**Resolution:**

## Q-041 — Unanchored version numbers in Document Control

**Status:** `Open`
**Where:** [MEG-005 ch00](../docs/engineering/guides/meg-005-runtime-architecture/00-document-control.md), [MEG-006 ch00](../docs/engineering/guides/meg-006-module-platform/00-document-control.md), [MEG-002 ch00](../docs/engineering/guides/meg-002-event-driven-runtime/00-document-control.md), all *Purpose*

"Version 0.4 records the Supervisor Build Pipeline as an isolated runtime composition and activation flow." MEG-005 declares no version anywhere, and CLAUDE.md forbids a `Version:` metadata field, so the number refers to nothing. Under [MDG-001 ch03](../docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md) only the contract a MIP defines carries a version.

MEG-006 and MEG-002 carry the identical construction — "Version 0.8 defines the Test Harness as a deterministic suite of development-only Modules" and "Version 0.3 aligns implementation guidance with MIP-001" — so this is a pattern rather than a slip.

The sentences are presumably leftovers from versioned drafts, but deleting them would remove the only statement of what each revision covers.

**Resolution:**

## Q-056 — MEG-003 diagrams draw splits and cycles as straight chains

**Status:** `Open`
**Where:** [MEG-003 ch03](../docs/engineering/guides/meg-003-domain-driven-design/03-subdomains.md), [ch05](../docs/engineering/guides/meg-003-domain-driven-design/05-context-maps.md)

The MEG-003 counterpart to Q-017 and Q-037. Two retained diagrams assert a shape the prose contradicts:

- ch03 *Evolving Subdomains* draws `Metadata → Providers → Artwork → Translation` as a linear chain while the prose describes a subdomain *splitting*. The correct shape is almost certainly a fan-out from Metadata, but that changes what the diagram claims about whether Providers, Artwork and Translation are peers or layers.
- ch05 *Avoid Bidirectional Dependencies* and *Anti-Patterns → Circular Relationships* both render the cycle as `N1["Playback"] → N2["Metadata"] → N3["Playback"]`, using two separate nodes carrying the same label instead of closing the loop back to `N1`. Both therefore render as a chain and do not depict the cycle they warn against. The fix is one line, but it changes what the diagram asserts, and it is not clear whether the duplication is an authoring mistake or a deliberate way of showing the return path.

**Resolution:**

## Q-057 — Naming inconsistencies within MEG-003

**Status:** `Open`
**Where:** MEG-003 chapters 00, 02, 03, 08, 09, 10, 11

Each of these is small, each changes meaning, and none were normalised:

- **Recommendation / Recommendations** — ch02 *Business Before Technology* gives the singular as the preferred domain term while *Avoid Abbreviations* gives the plural as the preferred expansion of Recs. ch03 uses the plural for the subdomain and the singular in "Recommendation Module".
- **Collection** — ch02 *One Name, One Meaning* uses Collection as its worked example of a word overloaded across concepts, while *Mosaic Examples* lists it under good names. *Context Matters* reconciles the two, but a reader meets the contradiction first.
- **Playback Session / PlaybackSession / Playback** — ch08 names the Aggregate "Playback Session" and sometimes "Playback"; ch09 names the Root type `PlaybackSession`. Plausibly a deliberate Aggregate-versus-Root convention, equally plausibly drift.
- **Runtime Adapter / Runtime Translation** — ch11 uses both for what appears to be one thing. [MEG-004](../docs/engineering/guides/meg-004-hexagonal-architecture/01-hexagonal-philosophy.md) uses Runtime Adapter.
- **`CollectionOrderingPolicy`** — ch10 *Examples Within Mosaic* lists it beside `MetadataMatcher`, `DuplicateResolver` and `RecommendationEngine`. Nothing says whether "Policy" is a sanctioned Domain Service suffix or an inconsistency with the naming guidance two sections earlier.
- **"Platform foundation domain"** — ch00 *Design Philosophy* attributes to Evans a focus on "the Platform foundation domain". The DDD term is *core domain*, and MEG-003's own scope lists Core domains separately. Either a Mosaic-specific renaming or a transcription error.

**Resolution:**

## Q-058 — Published specifications listed as planned or future

**Status:** `Open`
**Where:** [MEG-003 index](../docs/engineering/guides/meg-003-domain-driven-design/index.md) and [references](../docs/engineering/guides/meg-003-domain-driven-design/references.md); [MEG-006 index](../docs/engineering/guides/meg-006-module-platform/index.md) and [references](../docs/engineering/guides/meg-006-module-platform/references.md); [MEG-002 index](../docs/engineering/guides/meg-002-event-driven-runtime/index.md) and [references](../docs/engineering/guides/meg-002-event-driven-runtime/references.md)

Both lists describe MEG-004 as future or planned. [MEG-004](../docs/engineering/guides/meg-004-hexagonal-architecture/index.md) is published, and is the calibration reference this rewrite is measured against. The index also lists MEG-006 before MEG-005.

MEG-006 has the same defect at larger scale: MEG-007, MEG-008, MEG-009 and MEG-010 are each full multi-chapter specifications on disk with `Status: Draft`, yet `references.md` lists all four as planned, while the index lists three as future and omits MEG-010 entirely. MEG-006 chapter 09 depends on MEG-009 in substance (Q-068) while its index calls MEG-009 future.

MEG-002 is the worst instance found: its `references.md` lists **eight** specifications as planned — MEG-003 through MEG-010 — and all eight exist on disk with `Status: Draft`. Its index repeats the defect under a "Future companion specifications" heading, and both lists place MEG-006 before MEG-005.

Correcting it means knowing the real Status of every MEG in each list, which is a lifecycle question governed by [MDG-001 ch03](../docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md) rather than an editorial one.

**Resolution:**

## Q-059 — Citation label does not match its subject

**Status:** `Open`
**Where:** [MEG-003 ch09](../docs/engineering/guides/meg-003-domain-driven-design/09-aggregate-roots.md), *Identity*

The aggregate-root article is cited with the link text "Baeldung on Kotlin", which does not match the subject matter and looks like a copy error. Preserved verbatim; worth checking against `references.md`.

**Resolution:**

## Q-079 — MEG-006 diagrams contradict the prose beside them

**Status:** `Open`
**Where:** MEG-006 chapters 03, 04, 05, 06, 08, 12, index, 00

The MEG-006 counterpart to Q-017, Q-037 and Q-056, and the largest instance so far:

- [ch05](../docs/engineering/guides/meg-006-module-platform/05-dependency-resolution.md) *Capability Graph* draws `Library → Metadata → Playback → Recommendations` directly beneath prose stating that Recommendations depends on Playback and Playback on Metadata — the exact opposite — and inserts Library, which no prose claims. [ch06](../docs/engineering/guides/meg-006-module-platform/06-activation.md) *Activation Order* reuses the identical chain and reads it as execution sequence, so the two chapters use one diagram for two incompatible relations. MEG-006 never states its own arrow convention, although MEG-005 chapter 05 states one explicitly (Q-026). ch05's *Multiple Providers* and *Capability Groups* use arrows for a third relation again.
- [ch08](../docs/engineering/guides/meg-006-module-platform/08-module-sdk.md) *Dependency Direction* drew `Modules → Mosaic SDK → Platform` beneath prose saying both depend on the SDK and neither on the other. The diagram was deleted under the two-and-three-node rule, which incidentally removed the contradiction; if the intended shape is a fan-in it should be reinstated deliberately.
- [ch04](../docs/engineering/guides/meg-006-module-platform/04-registration.md) *Runtime Visibility* introduces a fan-out with "Examples include:" and then draws the four Runtime Services as one dependency chain.
- [ch03](../docs/engineering/guides/meg-006-module-platform/03-discovery.md) *Capability Descriptor* draws a composition as a sequence.
- [ch12](../docs/engineering/guides/meg-006-module-platform/12-isolation.md) *Isolation Layers* draws seven independent dimensions as a linear pipeline, directly beneath prose calling them independent.
- The index and ch00 both draw one chain alternating document identifiers with concept names, as MEG-004 and MEG-005 do (Q-023, Q-037). The ch00 variant additionally asserts `MDL → MDS → MEG-001`, a dependency of the Go standards on the Design System that nothing records.

**Resolution:**

## Q-080 — Naming inconsistencies within MEG-006

**Status:** `Open`
**Where:** MEG-006 chapters 01, 03, 04, 09, 11, 14, glossary

- **Module Descriptor / Capability Descriptor** — ch03's section heading, body text, diagram node and guideline use both for one artefact. The glossary defines only *Capability Descriptor*; "Module Descriptor" is defined nowhere.
- **`logging.write` / `logs.write`** and **`trace.write` / `traces.create`** — ch09 uses the first of each pair, MEG-009 the second. `logging.write` appears nowhere else in the repository. Permission strings are an enforced identifier space. ch09's category set also differs from MEG-009's by one category each way, with neither document mentioning the other.
- **Platform Contract / Runtime Contract** — the glossary defines both, nothing distinguishes them, and the chapters use them interchangeably. *Manifest* and *Module Manifest* overlap the same way (see Q-073).
- **Runtime / Platform Binary** — ch01 says the Platform Binary changes while the Runtime foundation does not, then says the final Runtime is a single statically linked executable, which makes them the same object.
- **Web Shell / Shell** — ch14 uses both with no cross-reference to an owning document and no glossary entry.
- **"Capabilities remain independently deployable"** — ch01 *Mosaic Principles*, against the same chapter's statements that Modules are statically linked and that adding a capability requires a new Platform package. The principle may mean independently *composable*.

**Resolution:**

## Q-081 — MEG-006 citations are mangled or point at unrelated projects

**Status:** `Open`
**Where:** [MEG-006 ch09](../docs/engineering/guides/meg-006-module-platform/09-permissions.md), [ch05](../docs/engineering/guides/meg-006-module-platform/05-dependency-resolution.md), [ch06](../docs/engineering/guides/meg-006-module-platform/06-activation.md), [ch00](../docs/engineering/guides/meg-006-module-platform/00-document-control.md), [index](../docs/engineering/guides/meg-006-module-platform/index.md), [references](../docs/engineering/guides/meg-006-module-platform/references.md)

Two distinct defects, both affecting load-bearing claims.

**URLs mangled by the Extension → Module terminology mapping.** Two Chrome citations point at `developer.chrome.com/docs/modules/...` and `developer.chrome.com/modules/manifest`. The real path is `extensions`, so both links are probably dead. The MDN citation in the same chapter still contains `WebExtensions`, so the substitution was applied inconsistently. This is Q-038's defect applied to external URLs, and raises the same question: does the terminology mapping apply to external terms of art?

**Sources that are not recognisable authorities.** Three separate normative claims in ch05 — topological sort with cycle detection, conflict validation before load order, and incremental resolution — all cite the same URL, the API documentation of an Elixir terminal-UI library's plugin resolver. ch06's readiness/initialisation separation cites a generated wiki page for a personal VS Code extension. `references.md` further carries a "GitHub" label pointing at a non-GitHub domain, an "arc42 Quality Model" label pointing at a plugin-architecture page, and four citations to domains corresponding to no recognisable standards body, vendor or textbook — unlike the `semver.org`, `go.dev` and `docs.aws.amazon.com` citations used elsewhere in the same chapters. None appear in `references.md`.

Same class as Q-039; each should be confirmed real and citable or substituted.

**Resolution:**

## Q-098 — MEG-002 diagrams contradict the prose beside them

**Status:** `Open`
**Where:** [MEG-002 ch07](../docs/engineering/guides/meg-002-event-driven-runtime/07-event-bus.md), [ch08](../docs/engineering/guides/meg-002-event-driven-runtime/08-publishers.md), [ch13](../docs/engineering/guides/meg-002-event-driven-runtime/13-retry-strategy.md)

The MEG-002 counterpart to Q-017, Q-037, Q-056 and Q-079. Rule 5 licenses deleting a diagram that *restates* prose, not silently rewiring one that contradicts it, so each was preserved as committed:

- ch07 *Fan-Out*: the prose says "One event may have many subscribers" and "The Event Bus performs the fan-out automatically", while the diagram draws a six-node **chain** — `PlaybackCompleted → Statistics → Recommendations → History → Achievements → Analytics`. Read literally it says Statistics publishes to Recommendations, which the rest of the chapter prohibits. The intended shape is almost certainly the fan-out drawn two sections earlier in *Delivery Model*.
- ch08 *Multiple Events*: the prose says one operation may publish several independent facts; the diagram draws `Import Media → media.imported → LibraryUpdated`, i.e. one event causing the next. If that is *not* a defect — if `LibraryUpdated` really is published by a subscriber to `media.imported` — then the section's claim is illustrated by an example that does not demonstrate it, and the example should change instead.
- ch13 *Retry Independence* (deleted under the chain rule): the prose says subscribers never block one another; the diagram drew `media.imported → Metadata Retry → Artwork Success → Search Success` serially, which is the exact blocking the prose prohibits. The labels were folded into prose as three independent outcomes, the plain meaning of the surrounding sentences, but the original author may have intended something else.

**Resolution:**

## Q-099 — "runtime" and "Runtime" are used inconsistently within and across documents

**Status:** `Open`
**Where:** MEG-002 throughout; [MEG-005](../docs/engineering/guides/meg-005-runtime-architecture/index.md), [MEG-006](../docs/engineering/guides/meg-006-module-platform/index.md), [MEG-008](../docs/engineering/guides/meg-008-observability/index.md)

MEG-002 writes lower-case **runtime** in most prose, including in normative guidelines, while capitalising **Mosaic Runtime** as a proper name. Its chapters 03 and 06 use capitalised **Runtime** exclusively, and chapters 07, 08, 13, 14 and 17 mix both, sometimes within a paragraph. MEG-005, MEG-006 and MEG-008 capitalise in the same normative positions where MEG-002 does not — MEG-008's "The Runtime owns propagation" is the direct counterpart of MEG-002's "the runtime owns tracing infrastructure".

The pattern is consistent enough to look deliberate — capitalised where the Runtime is a named component, lower-case where it is the coordinating concept — but that distinction is stated nowhere. Either it is real and belongs in [MDG-001 ch04](../docs/engineering/documentation/mdg-001-documentation-authority-guide/04-writing-standards.md)'s terminology table, or MEG-002 is the outlier and needs a mechanical pass. Every occurrence was preserved exactly as found.

**Resolution:**

## Q-100 — Two event-naming conventions coexist

**Status:** `Open`
**Where:** MEG-002 chapters 08, 12, 13, 14; [ch04](../docs/engineering/guides/meg-002-event-driven-runtime/04-event-naming.md)

Dotted lower-case (`media.imported`, `playback.started`) and PascalCase (`PlaybackCompleted`, `MetadataImported`, `MetadataCorrected`, `MetadataFetched`, `ArtworkDownloaded`, `LibraryUpdated`) both appear throughout. In chapter 12's *Event Ordering* the two sit inside a single comparison of the same playback lifecycle, reading as two schemes for the same events.

Chapter 04 owns event naming and MIP-001 owns the contract, so this may encode a real distinction — business events against runtime events, say — but neither chapter states one. Every name was preserved byte-exactly.

**Resolution:**

## Q-101 — MEG-002 glossary defects

**Status:** `Open`
**Where:** [MEG-002 glossary](../docs/engineering/guides/meg-002-event-driven-runtime/glossary.md)

- **Module event visibility is defined twice under three names.** *Event Visibility* defines both public and private events, then *Private Event* and *Public Event* define the same concepts again with more precision, adding "manifest-declared subscriptions" which *Event Visibility* omits. Which is canonical depends on whether MIP-002 owns the classification; chapter 18 links MIP-002 for exactly this, the glossary does not.
- **Alphabetical order is broken in section E:** Event, Event Bus, Event Envelope, *Event Visibility*, *Event Payload*. This interacts with the entry above, so both are worth fixing together.
- **`SWR` is defined but unused.** *Common Acronyms* expands SWR to Stale-While-Revalidate; the term appears nowhere else in MEG-002 and has no runtime referent, so it appears carried over from another document's glossary.

**Resolution:**

---

# Resolved

Entries move here once applied, with their original number.

*(none yet)*
