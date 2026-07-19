# 15. Open and closed vocabularies in the object graph

**Status:** Accepted. Refines [ADR 0013](0013-object-graph.md).
**Date:** 2026-07-19

## Context

[ADR 0013](0013-object-graph.md) describes `media_type` as naming "the kind of thing" and then lists ten examples — `movie`, `tv_series`, `anime_series`, `album`, `book`, `manga_series`, `comic_series`, `podcast`, `iptv_channel`, `collection`. It does not say whether that list is exhaustive. The same silence covers `container_type` and `item_type`.

Implementing the model forced the question, and the answer turned out to be already latent in ADR 0013 twice over.

First, its Consequences state: **"Adding a media type is rows, not tables. That is the property the whole model exists to deliver, and it is what makes a community-built module possible without Platform changes."** A `CHECK` constraint enumerating the known types would make every new media type a schema migration, which is exactly the property being denied.

Second, the list is provably incomplete. ADR 0013's own first non-uniformity states that an artist is its own Work joined to album Works by Relation — and `artist` is not among the ten. A closed list would have made the decision unimplementable on the day it was written.

Underneath the ambiguity, two different kinds of vocabulary had been conflated. Some of these columns name **what the Platform's machinery does** and are read by Platform code to decide behaviour. Others name **what a thing is**, and the Platform never branches on them. Those two need opposite treatment, and neither ADR 0013 nor the implementation had said so.

## Decision

**Vocabulary that the Platform branches on is closed and constrained. Vocabulary that only describes content is open and unconstrained.**

The test: *does Platform code read this value to decide what to do?* If yes it is structural, belongs to the Platform, and a new value is a Platform change. If no, it is descriptive, belongs to whoever is cataloguing, and a new value is data.

**Open — unconstrained text, no `CHECK`:**

- `media_type` — `movie`, `anime_series`, `artist`, and whatever a module brings
- `container_type` — `season`, `volume`, `arc`, `disc`, `box_set`, …
- `item_type` — `episode`, `track`, `chapter`, `issue`, …

The constants the Platform declares for these are a starting vocabulary for its own use, not a closed set.

**Closed — `CHECK`-constrained:**

- `node_kind` (`work`, `container`, `item`) — traversal depends on it
- `part_role` (`edition`, `segment`) — source selection depends on it
- `relation_type` — specific features read specific edge types
- `origin`, `match_method` — identity resolution machinery
- node and binding `status` values — state machines

The JSONB `attributes` and `external_ids` columns follow the open rule for the same reason, as ADR 0013 already established: the schema does not validate them, and correctness belongs to the writing capability.

### Enforcement today is nothing, and that has a cost

This is stated plainly rather than left to be discovered. `anime_series`, `anime-series` and `animeseries` are three distinct media types that browse as three separate libraries. Nothing catches it. A typo in a capability is silent fragmentation, surfacing as a user wondering why half their anime disappeared.

That cost is accepted **for now** and is not permanent.

### The anticipated mechanism, and its trigger

The eventual answer is a Platform-owned `media_types` registry — a table the Platform seeds, that a module contributes to through the manifest it already declares, with a foreign key from `nodes.media_type`. It gives referential integrity while keeping ADR 0013's phrase literally true: adding a media type is a row.

**It is not built now, and the trigger for building it is: when something other than Platform code can introduce a media type.**

Today every value is written by Platform code or by a capability in this repository, where a typo is a bug found in review. The registry's value appears when a third party ships a module. Building it earlier would require answering questions nothing is asking — what an uninstall does to a registered type, and what happens to nodes still using one — and inventing answers to unasked questions is the specific failure that retired the previous specification corpus.

## Alternatives considered

**A closed `CHECK` on the media vocabulary.** Referential safety immediately, and the simplest thing that could work. *Rejected:* it makes every new media type a schema migration, contradicting ADR 0002 and ADR 0013's stated purpose, and it is already wrong today — `artist` is required by ADR 0013's own non-uniformity and absent from its list. It would also put the Platform in the position of ratifying media types, which is the coupling the generic object model exists to avoid.

**Building the `media_types` registry now.** Correct destination, wrong time. *Rejected:* it forces answers on uninstall semantics and orphaned-type handling while there is no external module system to give those answers meaning. Recorded above as anticipated, with an explicit trigger, so the intent is not lost.

**A shape constraint** — `CHECK (media_type ~ '^[a-z][a-z0-9_]*$')`. Cheap, and catches `Anime Series` or `anime-series`. *Rejected:* it catches malformed values but not misspelled ones, which is the failure that actually costs a user their library, so it buys little. It also risks reintroducing the original problem in miniature: if module-supplied types later want namespacing (`animekit:ova`), a strict pattern blocks it and relaxing it becomes the migration this ADR exists to avoid. Better to add the registry, which subsumes it.

**Treating every one of these columns as open**, including `node_kind` and `part_role`. Uniform and simple to state. *Rejected:* Platform code switches on those values. An unrecognised `node_kind` is not a new media type, it is a traversal that does not know what it is looking at, and it should fail at write time rather than at read time.

## Consequences

**Adding a media type stays free**, which is the property ADR 0013 exists to deliver and the precondition for a community module introducing a format the Platform has never heard of.

**The Platform never ratifies a media type.** It has no list to be added to and no opinion to express, which is what keeps a module from needing a Platform change to ship.

**Typos fragment silently until the registry lands.** This is the accepted cost, and it is a known gap rather than an oversight. A capability writing media types is responsible for using constants rather than string literals.

**There is now a rule for future columns.** When the object graph grows a column with a small set of allowed values, the open/closed question has an answer — ask whether Platform code branches on it — instead of being settled per column by whoever implements it.

**ADR 0013's illustrative lists stay illustrative.** They are the Platform's starting vocabulary, and the absence of `artist` from them is a gap in the example rather than a constraint on the model.
