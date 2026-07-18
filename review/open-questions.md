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
**Where:** [MEG-004 index](../docs/engineering/guides/meg-004-hexagonal-architecture/index.md), [MEG-005 index](../docs/engineering/guides/meg-005-runtime-architecture/index.md), both *Repository Structure*

The tree names `README.md` as the folder's landing file; the real file is `index.md`. The folder path shown, `engineering/meg/MEG-004 Hexagonal Architecture/`, does not match the real `docs/engineering/guides/meg-004-hexagonal-architecture/`.

Preserved verbatim under the no-invention rule. Other specifications may carry the same stale tree.

MEG-005 and MEG-003 confirm this is a pattern rather than a one-off. Each shows `engineering/meg/<Document Title>/` containing `README.md`, with the same two defects, while the chapter filenames they list are correct. Only the folder path and the landing filename are stale. Whether these trees are meant to be accurate or merely illustrative should be settled once and applied to every specification that carries one.

**Resolution:**

## Q-022 — MDP-001 listed twice with an identical label

**Status:** `Open`
**Where:** [MEG-004 references](../docs/engineering/guides/meg-004-hexagonal-architecture/references.md), [MEG-005 references](../docs/engineering/guides/meg-005-runtime-architecture/references.md), [MEG-003 references](../docs/engineering/guides/meg-003-domain-driven-design/references.md)

Listed once pointing at `index.md` and once at `14-adaptive-tile-model.md`, both labelled "MDP-001 — Adaptive Composition Runtime". The second entry needs a distinguishing label.

All three guides carry the identical pair, so the fix should be applied to each. All three also file MDP-001 under a *Mosaic Design Specifications* heading although it lives under `docs/engineering/architecture/` — see Q-040, which records that alongside the MEG-005 glossary defects.

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

- MDP-001 is listed beneath *Mosaic Design Specifications* between MDS entries, but it lives under `docs/engineering/architecture/`, not `docs/design/system/`. MEG-003 and MEG-004 file it the same way, so this is a corpus-wide misfiling rather than a MEG-005 slip.
- MDS-006 and MDS-007 exist in the repository but are absent from that list, while MDS-008 is present.
- The glossary defines both *Kernel* and *Runtime Kernel* for what appears to be the same component, with overlapping but non-identical content — the *Kernel* entry carries the microkernel comparison and its citation, the *Runtime Kernel* entry carries the small, stable and business-agnostic list. Merging them would drop or relocate a citation.
- *Recovery UI* refers to "the embedded recovery renderer" in lower case, while Embedded Recovery Renderer is defined elsewhere as a capitalised proper noun.

See also Q-022, which covers the duplicated MDP-001 entry in the same file.

**Resolution:**

## Q-041 — "Version 0.4" refers to a version MEG-005 does not declare

**Status:** `Open`
**Where:** [MEG-005 ch00](../docs/engineering/guides/meg-005-runtime-architecture/00-document-control.md), *Purpose*

"Version 0.4 records the Supervisor Build Pipeline as an isolated runtime composition and activation flow." MEG-005 declares no version anywhere, and CLAUDE.md forbids a `Version:` metadata field, so the number refers to nothing. Under [MDG-001 ch03](../docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md) only the contract a MIP defines carries a version.

The sentence is presumably a leftover from a versioned draft, but deleting it would remove a statement about what the document covers.

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

## Q-058 — MEG-003 misstates the publication state of MEG-004

**Status:** `Open`
**Where:** [MEG-003 index](../docs/engineering/guides/meg-003-domain-driven-design/index.md), *Dependencies*; [references](../docs/engineering/guides/meg-003-domain-driven-design/references.md), *Planned Engineering Specifications*

Both lists describe MEG-004 as future or planned. [MEG-004](../docs/engineering/guides/meg-004-hexagonal-architecture/index.md) is published, and is the calibration reference this rewrite is measured against. The index also lists MEG-006 before MEG-005.

Correcting it means knowing the real Status of every MEG in the list, which is a lifecycle question governed by [MDG-001 ch03](../docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md) rather than an editorial one.

**Resolution:**

## Q-059 — Citation label does not match its subject

**Status:** `Open`
**Where:** [MEG-003 ch09](../docs/engineering/guides/meg-003-domain-driven-design/09-aggregate-roots.md), *Identity*

The aggregate-root article is cited with the link text "Baeldung on Kotlin", which does not match the subject matter and looks like a copy error. Preserved verbatim; worth checking against `references.md`.

**Resolution:**

---

# Resolved

Entries move here once applied, with their original number.

*(none yet)*
