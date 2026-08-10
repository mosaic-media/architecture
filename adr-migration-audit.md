# ADR migration audit

**Date:** 2026-08-10 · **Scope:** all 135 records in `docs/adr/`, and every reference to them across the twelve repositories on disk.

This is a working document for one decision: moving the decision records out of `architecture` and into the repositories that own them, with each repository's series restarting at 1. **Part I** decides where each record goes. **Part II** asks whether 135 is the right number of records, and re-scopes those whose wording straddles repositories. It is not part of the published site and is not in `mkdocs.yml`. **It should be deleted once the migration lands or is abandoned** — leaving it is the "delete, do not annotate" rule broken by a document about following rules.

> **On the "do not create new documents" rule.** `CLAUDE.md` caps the corpus at three pages plus the unreachable-capability register. This file is deliberately outside `docs/`, so it publishes nowhere and adds no page. It is scaffolding for a migration, not a fifth document. If it survives past the migration, that reasoning has failed and it should go.

---

## 1. The finding that decides the shape of this project

**The corpus does not divide the way the goal assumes.** Under a strict reading of "which repository does this decision belong to," 76 of 135 records belong to no single repository, and of the 59 that do, 47 belong to `platform`. The module repositories — the ones that most obviously look like they should own their own decisions — receive **three records between them**.

That is not a defect in the corpus. It is what a corpus looks like when it documents a system whose whole design is contracts between components. A decision about a published contract exists *because* it binds more than one consumer; that is the definition of a contract.

So the migration can be run two ways, and the choice is yours. Both are modelled below with a complete per-record mapping.

| | **Option A — coupling** | **Option B — stewardship** |
|---|---|---|
| The question asked | "If this were reversed, whose code changes?" | "Who would write the successor record, and where does the mechanism live?" |
| `architecture` keeps | **76** | **4** |
| `platform` | 47 | 81 |
| `contracts` | 2 | 19 |
| `supervisor` | 5 | 11 |
| `sdk` | 1 | 10 |
| `web` | 2 | 6 |
| module repos | 3 | 4 |
| `registry` | 0 | 0 |
| **Does it meet the goal?** | **No** — 56% stays put | **Yes** — but strips `architecture` to four records |

**Recommendation: Option B, with an explicit carve-out you choose deliberately, and a citation namespace (§4) that is not optional under either option.**

Option B is defensible on its own terms: a decision can bind five repositories and still have exactly one steward — the repository holding the spec file, the lint gate, the conformance corpus or the release workflow that enforces it. That is the normal case, and treating it as "cross-cutting" is what produces the 76.

But Option B taken literally leaves `architecture` holding four records (licensing, repository naming, the module tier model, project credentials). Whether that is the right destination for a repository whose stated purpose is cross-cutting documents is a judgement, not a computation — see §6.

### What the data does *not* support

I tested whether the most-depended-upon records form a "constitutional core" that should stay in `architecture` regardless. **They do not.** Ranking records by how many other records cite them, the top twenty scatter:

| Record | Cited by | Steward under B |
|---|---:|---|
| 0017 How a capability acts | 19 | `platform` |
| 0041 Cross-client transport | 17 | `contracts` |
| 0007 Static Go module composition | 16 | `platform` |
| 0027 Modules as typed capability providers | 14 | `sdk` |
| 0064 The extension module boundary | 13 | `platform` |
| 0021 User-managed module settings | 13 | `platform` |
| 0015 Open and closed vocabularies | 13 | `platform` |
| 0004 Supervisor as host manager | 13 | `supervisor` |

There is no subset that is both foundational and homeless. The hubs belong to four different repositories, which means the citation-namespace problem in §4 cannot be dodged by keeping the important ones together.

---

## 2. Blast radius: 4,675 reference sites, 68% invisible today

Every reference below must change, because the migration changes both halves of an ADR's identity — its number *and* its repository.

| Form | Count | Files | Repos | Caught by any tool? |
|---|---:|---:|---:|---|
| Relative links between ADRs | **987** | 123 | 1 | `mkdocs --strict` only |
| Links from the four top-level pages | **223** | 4 | 1 | `mkdocs --strict` only |
| Absolute GitHub URLs from sibling repos | **134** | 27 | 11 | **nothing** |
| **Bare prose citations — `(ADR 0007)`** | **3,047** | 669 | 12 | **nothing** |
| `mkdocs.yml` nav entries | 135 | 1 | 1 | `mkdocs --strict` |
| `build_pdfs.py` PAGES entries | 14 | 1 | 1 | PDF job (14 of 135) |
| ADR numbers in filenames | 135 | 135 | 1 | `mkdocs --strict` |
| **Total** | **4,675** | | | **1,494 caught (32%)** |

Each of the 987 relative links carries the number twice — once in the label, once in the path — so they are **1,974 edit points**, not 987. No link uses a heading anchor, so anchors are not at risk.

`mkdocs build --strict` is the only link validation in the entire fleet. **It stops helping precisely when it is needed:** it flags a dangling link only while both ends remain inside `docs/`. The moment two records land in different repositories, the link between them can no longer be relative, must become an absolute cross-repo URL, and is checked by nothing thereafter. After the migration, **0% of the 4,675 sites are covered by any automated check.**

---

## 3. The worst hazard: 3,047 bare citations that fail *open*

This is the finding that should govern how the migration is sequenced.

**3,047 citations, 669 files, all 12 repos, naming 130 of the 135 records.** They are prose — `(ADR 0050)`, `ADR 0016` — not links. Nothing parses them. No tool in any repository could.

- **2,051 are in Go source. 181 are in TypeScript.** Comments and one test name (`TestRoleClassTableMatchesADR0063`), all of which compile and pass regardless of what they name.
- **129 sit inside *generated* files in `contracts`** — copied out of `.proto` comments and `ui.spec.json` by the generator, and guarded by `check-generated.sh`. They cannot be hand-edited; the sources must change and the bindings be regenerated.

**The collision problem, quantified.** Today `ADR 0017` is globally unique: one string, one record, twelve repositories. Restart every repository at 1 and the low numbers are reused up to nine times.

> **105 of the 130 cited numbers (81%) are cited in bare prose from more than one repository, accounting for 2,935 of 3,047 citations — 96%.** Only 112 citations (4%) are safely repo-local.

And **955 citations (31%) name a number ≤ 0040** — squarely inside the range every renumbered repository will reoccupy. `platform` alone has 357 of them.

**The failure mode is silent and wrong, not loud and broken.** A stale `ADR 0012` in `platform` will not dangle after the migration. It will resolve, correctly and quietly, to `platform`'s *own new* ADR 12 — a different decision entirely. No 404. No red test. No broken link. The citation still reads as valid and now points at the wrong record.

That is strictly worse than a dead link, and it is the exact failure this repository's reset was performed to prevent: `CLAUDE.md` records that the previous corpus produced "a roadmap built against an abandoned storage model." A renumber without a namespace manufactures that failure 2,935 times in one commit.

---

## 4. Therefore: the citation namespace is mandatory

Restarting each repository at 1 is only safe if a citation carries its repository. Bare `ADR 0012` must stop being a valid way to cite anything.

**Proposed form: `repo#N`** — `platform#12`, `contracts#7`, `sdk#3`, `architecture#2`.

- It is unambiguous across all thirteen repositories.
- It is greppable, and the *absence* of a qualifier is greppable — `ADR [0-9]` with no repository prefix becomes a lint that any repository can run, which is the check that does not exist today.
- It reads naturally in prose and in a comment.
- It does not collide with the existing `ADR NNNN` spelling, so the migration can be verified by requiring that **zero** unqualified citations remain.

Whatever form you choose, the non-negotiable property is that **a stale citation must fail loudly rather than resolve to the wrong record.** That is achievable only if the new form is textually distinct from the old one.

### The one check worth building

A single script, vendored into each repository's existing container gate, that fails on any unqualified `ADR \d+` and on any `repo#N` naming a record that does not exist. It is perhaps thirty lines. Without it, this corpus goes from 32% checked to 0% checked, permanently — and the current 32% is the only reason the corpus is in as good a state as it is.

---

## 5. Structural obstacles

**Every destination is greenfield.** No sibling repository has a `docs/` directory at all — not one of the eleven on disk. There is no nav, no publishing pipeline, no PDF export and no link check anywhere but here. Thirteen ADR homes must be created, and the migration decides whether they are published or plain files in a repo.

**`supervisor` is not checked out but does exist.** `mosaic-media/supervisor` is a real, pushable repository; it is simply absent from this machine and from this session's scope. It is the destination for **11 records** under Option B (0004, 0005, 0006, 0033, 0060, 0121, 0123, 0124, 0125, 0126, 0127) and its ~unknown reference load is the one number in this audit that is unmeasured. Attach it before executing.

**`nav:` is the only index that exists.** There is no `docs/adr/README.md` and no manifest. Deleting nav rows deletes the sole record of each ADR's title and state. An ADR file left behind after its nav row is removed is `info`-level in MkDocs — it publishes silently and vanishes from the site's only map.

**The number lives in three places, in two formats.** Padded in the filename (`0012-…`), **unpadded in the H1** (`# 12. Capabilities do not own stores`), unpadded again in the nav label. Strict mode validates only that a path resolves — **a renumber that misses the H1 builds green.** All 135 files have the number in the heading.

**47% of records point at another record from their Status line.** 64 of 135. Several form chains that cannot be separated without a Status line reaching into another repository:

- `0108 → 0109 → 0110 → 0111` — transcode and segmentation
- `0112 → 0113 → 0114 → 0115` — subtitles
- `0124, 0125, 0126 → 0127` — Supervisor version pairing
- `0097, 0098 → 0101, 0106` — pre-session
- `0059 → 0128 → 0130, 0135` — the SDK dependency reversal

Under Option B these mostly stay together (the playback and subtitle chains are all `platform`; the Supervisor chain all `supervisor`), but `0059 → 0128` sits inside `sdk` while `0130`'s siblings do not, and the pre-session chain splits `platform` from `contracts`. Check each chain before moving it.

**History will not follow.** These clones are shallow (50 commits). Moving files between repositories loses their history unless you graft it with `git filter-repo` or a subtree merge. Decide explicitly whether that matters; the ADRs' value is partly that they are dated evidence.

**The rule being reversed is asserted in eleven places.** Ten sibling `CLAUDE.md` files plus this repository's own carry the sentence *"Records live only in `architecture/docs/adr/`, numbered sequentially in kebab-case."* All eleven must change in the same commit series, or the fleet's own instructions will tell the next session to undo the migration.

---

## 6. What `architecture` is left holding

Under Option B, four records: **0022** (licensing), **0043** (repository naming), **0062** (two module tiers), **0105** (project credentials in official builds). Each was kept because it has no enforcing artefact in any repository — nothing reads a repository name; the tier assignment is validated by nothing; 0105's mechanism is deliberately replicated per module, which is the asymmetry the record exists to correct.

The four documents are a different matter and mostly stay:

- **`roadmap.md`** (3,066 lines) is organised by milestone, not by repository — 2,600 lines sit under a single "The milestones" heading, and a milestone spans repositories by construction. It is structurally cross-cutting and should not be split. But it holds **130 ADR links**, every one of which becomes an unchecked cross-repo URL. The most-maintained page in the corpus becomes the least verifiable.
- **`index.md`**, **`architecture.md`**, **`unreachable-capability.md`** — 93 ADR links between them, same conversion.

**The gap Option B creates.** With records dispersed and `nav:` gone as the index, nothing anywhere lists what has been decided. That is a genuinely cross-cutting need and the natural fifth thing for this repository to hold: **a register of every record across every repository** — repo, number, title, status, one line each. Not copies; pointers. It replaces `nav:` as the map, it is the lookup table the `repo#N` lint needs, and it is the only artefact that can answer "has this already been decided somewhere?" after the corpus is dispersed.

---

## 7. Defects found along the way, independent of the migration

These are real now and worth fixing whether or not the move happens. Several are the precise failure modes `CLAUDE.md` warns about.

**1. `build_pdfs.py` exports 14 of 135 ADRs.** `PAGES` stops at ADR 0014. **121 records have silently had no PDF for the life of the repository**, and `unreachable-capability.md` is omitted entirely — contradicting `CLAUDE.md`'s claim that "every page is also exported as a PDF." `PAGES` and `nav:` are two hand-maintained lists that nothing cross-checks.

**2. Four nav labels contradict the record they point at.** `mkdocs.yml` labels ADRs 0046, 0049, 0052 and 0060 "(proposed)" while their own Status lines read "Accepted (built…)" or "Built in part." The nav carries a second copy of each record's status — a direct breach of "one authoritative statement per fact" — and it has drifted. **61 nav labels also differ from their file's H1 title.**

**3. ADR 0007 is half-reversed with no pointer in either direction.** 0007 rejects "Module RPC processes" by name. 0064 puts extension modules "in their own process over a Unix socket," 0077 adopts go-plugin's gRPC harness, and 0081 installs them at runtime. **0077 never mentions 0007; 0007's Status is a bare "Accepted."** The repository's own rule: a decision the code deliberately reverses "earns a new record that supersedes it… point both records at each other through their Status lines." The successor exists; both pointers are missing. 0007 is cited by 16 other records.

**4. Two Status lines disagree about whether the system principal exists.** 0058 says retention "was built in M0.1: the hourly `telemetry.retention` job runs as the system principal." 0049 says its refresh job "remains blocked on the jobs runner, the scheduler and the system principal." `platform/CLAUDE.md` sides with 0049. The disagreement sits in the Status line — the one field that is supposed to be current. (0057's body says "blocked" too, but bodies are append-only history and that one is correct as written.)

**5. 0079 and 0081 contradict each other, dated the same day.** 0079: "nothing here is built." 0081: "beyond the install-and-verify path ADR 0079 already produced."

**6. 0039's Status says the code does the opposite of its body**, and the body reads as settled throughout — the Shell still parses URLs into screens.

**7. 0051's Status claims a dialect table keyed on addon manifest id.** It does not exist in `module-stremio-addons`; only the generic fallback parser does.

**8. 0090's "identical everywhere" threshold exists only as `VISIBILITY_THRESHOLD = 0.5` in `web`**, pinned by no contract entry and no conformance case — so the one client that implements it defines it.

**9. 0133's body argues from a premise its own Status line records as false.** The Status correction is right (`OpenOverlay` and the three surfaces exist, with a live call site); the body's Alternatives section is misleading if ever read apart from it.

**10. A stray tree in `web`.** `web/mosaic-shell/` is not one of the three documented packages and carries an ADR citation in a test file.

---

## 8. Suggested sequence

The ordering matters more than usual, because the only check in the fleet disappears midway.

1. **Fix §7 items 1–4 first, while everything is still in one repository** and `mkdocs --strict` still covers 1,210 links. These are cheap now and expensive later.
2. **Decide Option A or B, and the carve-out.** Write it down; it is the rule every future record is filed under.
3. **Agree the citation form** (`repo#N` or another) and **build the lint before moving anything.** Run it against the current corpus to establish a clean baseline.
4. **Attach `supervisor`** and measure its reference load — the one unmeasured number here.
5. **Create the register** in `architecture` from the current `nav:`, before `nav:` is dismantled. It is the only complete index that exists.
6. **Move one repository first as a pilot.** `contracts` (19 records) or `supervisor` (11) is the right size — large enough to hit real problems, small enough to reverse. `platform` at 81 is the wrong place to learn.
7. **Rewrite citations repo by repo**, mechanically, with the lint as the gate. Note the 129 citations in `contracts`' generated files must be changed at source and regenerated.
8. **Update the eleven `CLAUDE.md` files** in the same series.
9. **Consolidate, if at all, only now** — after the namespace exists, so the 4,675-site rewrite is paid once rather than twice. See §14 for what is worth merging and what is not.
10. **Delete this document.**

---

# Part II — the enrichment pass

Added 2026-08-10, second pass. Part I asked *where each record goes*. This part asks *whether 135 records is the right number*, and whether a record's wording can be scoped so its home is obvious rather than argued.

## 9. The premise, tested

The observation prompting this pass — that some chains are four consecutive records back to back — is right, and understates it.

**133 of the 135 records sit inside a run of consecutive numbers written on the same day.** Only 0099 and 0100 stand alone. There are 19 such runs:

| Run | Records | Date |
|---|---:|---|
| 0045–0065 | 21 | 2026-07-22 |
| 0018–0034 | 17 | 2026-07-20 |
| 0083–0098 | 16 | 2026-07-25 |
| 0121–0130 | 10 | 2026-08-09 |
| 0035–0044 | 10 | 2026-07-21 |
| 0074–0082 | 9 | 2026-07-24 |
| 0003–0011 | 9 | 2026-07-14 |
| 0066–0073 | 8 | 2026-07-23 |
| …11 more runs | 2–6 each | |

The whole corpus was written in 27 days. So the one-decision-per-record granularity is substantially an artefact of **authoring in sittings**, not of decisions arriving separately over time. That is evidence for consolidation, not proof of it — whether a run is one decision or several that happened to land together is answerable only by reading the bodies, which is what this pass did for all 135.

## 10. The result: 135 → 111, and why it is not 60

Seven clusters were assessed independently, each required to enumerate the decisions carried in and out and prove nothing was dropped.

| Cluster | In | Out | |
|---|---:|---:|---|
| Playback, transcode, subtitles | 18 | **9** | the one big win |
| SDUI contract and vocabulary | 25 | **19** | |
| Modules, tiers, distribution | 23 | **19** | |
| Supervisor and host | 17 | **14** | |
| Auth, session, secrets | 15 | **13** | |
| Content model, storage, artwork | 26 | **25** | barely moves |
| Telemetry and observability | 11 | **12** | **grows** |
| **Total** | **135** | **111** | **−18%** |

**An 18% reduction, not the halving the same-day-run data suggests.** One cluster grows. That gap between the premise and the result is the most useful thing in this pass, and it has a single cause.

### The binding constraint is reversals, not authoring style

All seven assessments converged independently on the same rule: **never merge across a reversal.** Where record B overturned record A, merging them keeps the answer and deletes the argument the answer had to beat — and a rejected alternative with a reason attached is precisely what stops a decision being re-litigated in eighteen months.

The refusals are more instructive than the merges:

- **0059 → 0128 → 0135** (may the SDK depend on OpenTelemetry: no, then yes, then no again). Refused, and rightly: 0135 is still `Proposed` while `sdk/go.mod` still requires the four OTel modules, so a merged record would describe code that does not exist. The reversal is also two-of-three — one ground was genuinely settled by 0128, two were reinstated by 0135 — and only three records can say that.
- **0001 / 0012** (transactional store extensibility). The corpus's only record of a reversal that *reached code and was backed out*. It is what explains `StorageAdapter` surviving with no `Store[T]` beside it.
- **0068 / 0102** (session credentials). Merging would delete the `HttpOnly`/XSS argument that `localStorage` had to beat — a security rationale, not a historical note.
- **0088 / 0096** (the form merge rule). The account of the bug 0088 hid — a blank field beating a typed value, storing silently, answering `200`, found by typing `GB` into a region box — dies in the merge. The corrected rule survives; the reason anyone should care does not.

Runs consolidate well when they are **one decision plus its serial refinements** and badly when they are **one decision plus its corrections**. Those look identical from the outside — consecutive numbers, same day, cross-referencing Status lines — and can only be told apart by reading. That is why this pass could not be done from the index.

### The clean case, for contrast

**0108 → 0109 → 0110 → 0111 merges 4 → 1.** Three of the four were written on 2026-07-30 and two were superseded before the day ended. There is no independent decision among them — only four attempts at one question (how a stream ffmpeg produces is made seekable) and the measurements that killed three. The merged Status must still carry *"built on both sides and never played"* and *"this is the fourth design"*, or the merge launders a record that admits it was wrong.

## 11. The real prize is re-homing, not the count

Across the seven clusters: roughly **24 merges, 12 splits and 17 reframes**. The splits are what serve your stated goal, because they attack the actual cause of the 76 cross-cutting records in Part I — **a record that bundles two repositories' decisions in one body has no clean home, and never will until it is split.**

Worked examples, each verified against code rather than prose:

- **0031** (the server-emitted app shell) carries separate rejected alternatives for its server half and its client half. Split → `platform` / `web`.
- **0084** (vocabulary negotiation): `VocabularyProfile` and `fallback` are fields in `contracts`' protos, while the degradation pass is `platform/internal/transport/vocabulary/`. Split → `contracts` / `platform`.
- **0061** (one client transport) splits into a `platform` record (delete the GraphQL transport; `dispatch` is the boundary) and a `contracts` record (`AuthService` as its own service).
- **0052** carries a notification model already implemented and cited in `contracts/session.proto`. That half moves to the repository that implements it.
- **0128** has one Status line covering three build states in three repositories — already stale.
- **Seven records in the module cluster alone** decide something for `sdk` and something for `platform` in one body. That is why 0077 currently sits in a different repository from the record it refines.

The effect on the distribution is modest in aggregate and large where it matters:

| Repo | Disperse only | Disperse + consolidate | Δ |
|---|---:|---:|---:|
| `platform` | 81 | **63** | −18 |
| `contracts` | 19 | **17** | −2 |
| `sdk` | 10 | **9** | −1 |
| `supervisor` | 11 | **8** | −3 |
| `web` | 6 | **5** | −1 |
| `architecture` | 4 | **5** | +1 |
| module repos | 4 | **4** | 0 |
| **Total** | **135** | **111** | **−24** |

`platform` absorbs the whole reduction, falling from 60% of the corpus to 57%. **The module repositories gain nothing** — consolidation does not fix the distribution problem Part I identified, and nothing in this pass suggests it should be expected to.

## 12. Two decisions this pass forces

**A. The append-only rule.** Merging bodies is a head-on collision with the rule asserted in eleven `CLAUDE.md` files: *"Never rewrite a record's body… State changes go in the Status line and nowhere else."* That rule governs **maintaining** a corpus. This migration **re-founds** one — new repositories, numbering from 1 — and a re-founding is the one moment transcription is legitimate, provided the original survives. The mechanism, which this project has used before:

1. Tag the current corpus (`pre-adr-split-2026-08-10`), exactly as `pre-reset-2026-07-19` preserved the last one.
2. Consolidated records are **new** records in the new series, each naming in its Status line the originals it supersedes.
3. No original is edited. They cease to be the live series and remain reachable at the tag.

Anything less — editing bodies in place and calling it consolidation — breaks the rule for real, and the rule is load-bearing.

**B. Where the reversals go.** 111 records still carry the reversal chains that refused to merge. Those chains are the corpus's most valuable content and the most fragile under renumbering, because a Status line pointing at a superseded record is exactly the cross-repo citation nothing checks (§2). Most chains stay within one repository under this mapping — the playback and subtitle chains are all `platform`, the upgrade chain all `supervisor` — but **0059 → 0128 → 0135 sits inside `sdk` while 0130's siblings do not**, and the pre-session chain splits `platform` from `contracts`. Check each chain before moving it.

## 13. Further defects found in this pass

Independent of the migration, and additional to §7.

**11. Two contract-level constants exist only in one client.** ADR 0090 states the impression threshold is *"arbitrary, like any threshold, but **stated** and identical"* across clients; ADR 0093 names a 600px prefetch margin. **Verified:** `VISIBILITY_THRESHOLD = 0.5` and `PREFETCH_MARGIN_PX = 600` live in `web/packages/sdui-react/src/` and appear nowhere in `contracts` — not in `ui.spec.json`, not in the conformance corpus, not in `REFERENCE.md`. A second client would guess. `check-vocabulary.mjs` cannot catch it, because it compares vocabulary members, not constants.

**12. Status lines stale in both directions.** 0047 is stale in four clauses (progress reporting, `subtitleTracks`, next-up and resume are all built — `hls.js` and `jassub` are real `sdui-react` dependencies); 0050 is stale the other way (HLS landed); 0036, 0074 and 0075 read `Proposed` and are built; 0099 reads `Proposed` while describing built code.

**13. Three unrecorded reversals in the auth cluster** — 0102 reverses 0068 on cookies, and 0106 reverses 0061 on the `capabilities` field. Neither is recorded as a reversal, so a careless consolidation would launder both.

**14. 0064 rejects the standard library's `plugin` package while 0077 adopts `hashicorp/go-plugin`.** Correct as written — they are different things — but merged carelessly they read as self-contradictory.

**15. 0011's module half has no SDK surface at all**; 0014's export formats and 0030's second slice are unbuilt while their records do not say so.

### Corrections to Part I

- **Retired.** An agent reported that code discloses the server name pre-authentication, against 0097. **It does not.** `setupServerStep()` collects a name in the setup wizard, the review step echoes back what the user typed, and `claimEnvelope` is documented as *"what the setup wizard's submit collects"* — all inbound. No read of a configured name into a pre-auth tree exists.
- **Softened.** ADR 0124 was reported as contradicting working code by rejecting an aggregated catalogue. Its own Status line already acknowledges the departure — *"the Supervisor reads a signed index from a configured URL today, and no official one exists"* — and the roadmap agrees. It is recorded, just as a build-state note rather than as the reversal of a named rejected alternative.

## 14. Revised recommendation

Consolidation is worth doing, but **not for the record count**, and it should not gate the migration.

1. **Do the splits.** Twelve of them, and they are the only move that measurably improves where records live. A split record has one owner by construction.
2. **Do the four clean merges** — the playback run (4→1), the subtitle run (5→1), the upgrade run (3→1), the bindings/scopes/fields run (3→1). Together they account for 11 of the 24 removed records and none crosses a reversal.
3. **Leave the reversal chains alone.** They are 18% of the corpus and most of its value.
4. **Treat consolidation as optional and sequence it after the citation namespace (§4) exists** — merging records changes numbers a second time, and doing that before the lint exists means paying the 4,675-site rewrite twice.

---

## Appendix — complete mapping, all 135 records

`Coupling` is Option A. `Steward` is Option B. `New id` is the Option B destination with its renumbered position, preserving current relative order within each repository.

| Old | Title | Coupling | Steward | New id |
|---|---|---|---|---|
| 0001 | Transactional store extensibility | platform | platform | `platform#1` |
| 0002 | Module storage and delivery model | architecture | platform | `platform#2` |
| 0003 | Platform as execution kernel | architecture | platform | `platform#3` |
| 0004 | Supervisor as Mosaic host manager | supervisor | supervisor | `supervisor#1` |
| 0005 | Supervisor guarantees an intelligent interface | supervisor | supervisor | `supervisor#2` |
| 0006 | Supervisor orchestrates isolated runtime builds | supervisor | supervisor | `supervisor#3` |
| 0007 | Static Go module composition | architecture | platform | `platform#4` |
| 0008 | SDK as public contract language | architecture | sdk | `sdk#1` |
| 0009 | Developer Platform as an integrated toolchain | architecture | platform | `platform#5` |
| 0010 | Test Harness as development modules | architecture | platform | `platform#6` |
| 0011 | Platform transports events, modules own domain events | architecture | platform | `platform#7` |
| 0012 | Capabilities do not own stores | platform | platform | `platform#8` |
| 0013 | The object graph: Node, Part, Relation | architecture | platform | `platform#9` |
| 0014 | Storage authority, media linking and transaction scope | platform | platform | `platform#10` |
| 0015 | Open and closed vocabularies in the object graph | platform | platform | `platform#11` |
| 0016 | The published contract surface | architecture | platform | `platform#12` |
| 0017 | How a capability acts | platform | platform | `platform#13` |
| 0018 | First-administrator bootstrap | platform | platform | `platform#14` |
| 0019 | The module capability and invocation contract | platform | platform | `platform#15` |
| 0020 | Optional-module composition | platform | platform | `platform#16` |
| 0021 | User-managed module settings | platform | platform | `platform#17` |
| 0022 | Licensing | architecture | architecture | `architecture#1` |
| 0023 | Server-Driven UI and the Shell | architecture | contracts | `contracts#1` |
| 0024 | Primitives and definitions: no component holdouts | architecture | contracts | `contracts#2` |
| 0025 | The SDUI contract repository | architecture | contracts | `contracts#3` |
| 0026 | The React SDUI runtime is a shared package | web | web | `web#1` |
| 0027 | Modules as typed capability providers | architecture | sdk | `sdk#2` |
| 0028 | Virtual browse and materialized library | platform | platform | `platform#18` |
| 0029 | The Platform's SDUI emit-side | platform | platform | `platform#19` |
| 0030 | The artwork proxy (and cache) | platform | platform | `platform#20` |
| 0031 | The Shell is a pure renderer; the app shell is server-emitted | architecture | platform | `platform#21` |
| 0032 | The live session over a bidirectional WebSocket | architecture | platform | `platform#22` |
| 0033 | Supervisor-driven live-session handover | architecture | supervisor | `supervisor#4` |
| 0034 | Rich metadata: the descriptive surface grows a preview | architecture | sdk | `sdk#3` |
| 0035 | Metadata is a required capability with a default provider | platform | platform | `platform#23` |
| 0036 | Capability-gated affordances and consumer roles | platform | platform | `platform#24` |
| 0037 | Completing the Stremio source surface | module-stremio-addons | module-stremio-addons | `module-stremio-addons#1` |
| 0038 | Module-contributed settings UI | architecture | sdk | `sdk#4` |
| 0039 | Server-owned navigation: a screen-agnostic client | architecture | web | `web#2` |
| 0040 | Definitions and the skin are server-delivered data | architecture | contracts | `contracts#4` |
| 0041 | Cross-client transport: protobuf and two lanes | architecture | contracts | `contracts#5` |
| 0042 | The web frontend is one workspace; split repos only to enforce a boundary | architecture | web | `web#3` |
| 0043 | Repository names encode role, not the org — drop the redundant prefix | architecture | architecture | `architecture#2` |
| 0044 | The SDUI and session contracts are protobuf in one workspace | architecture | contracts | `contracts#6` |
| 0045 | The playback consumer contract and the Platform-hosted media origin | architecture | platform | `platform#25` |
| 0046 | Playback state is Platform-owned | platform | platform | `platform#26` |
| 0047 | The player is a client primitive over a server-issued ticket | architecture | web | `web#4` |
| 0048 | Stream selection against a client profile | platform | platform | `platform#27` |
| 0049 | The resolution cache and capability classes | platform | platform | `platform#28` |
| 0050 | Probing, and the per-stream playback decision | platform | platform | `platform#29` |
| 0051 | Modules as anti-corruption layers: source dialects and a tested-source registry | architecture | module-stremio-addons | `module-stremio-addons#2` |
| 0052 | Cache-first rendering, and telling the truth when a source is down | platform | platform | `platform#30` |
| 0053 | Telemetry is ambient in context | platform | platform | `platform#31` |
| 0054 | The correlation ID is the trace ID | architecture | platform | `platform#32` |
| 0055 | Instrument at the seams | platform | platform | `platform#33` |
| 0056 | Redaction classes are the PII boundary | architecture | platform | `platform#34` |
| 0057 | Audit is a store, not a log stream | platform | platform | `platform#35` |
| 0058 | Telemetry storage, retention, and expert mode | platform | platform | `platform#36` |
| 0059 | Modules observe through the SDK | sdk | sdk | `sdk#5` |
| 0060 | The Supervisor observes independently | supervisor | supervisor | `supervisor#5` |
| 0061 | One client transport: retire GraphQL | architecture | platform | `platform#37` |
| 0062 | Two module tiers | architecture | architecture | `architecture#3` |
| 0063 | The Platform binary is built by CI; the Supervisor selects, not compiles | architecture | platform | `platform#38` |
| 0064 | The extension module boundary | architecture | platform | `platform#39` |
| 0065 | Module distribution and trust: signed binaries and user-added repositories | architecture | platform | `platform#40` |
| 0066 | Authorization is carried in the type | platform | platform | `platform#41` |
| 0067 | Authorization has three mechanisms, not one | platform | platform | `platform#42` |
| 0068 | One principal, many credentials | platform | platform | `platform#43` |
| 0069 | Privilege cannot escalate through delegation | platform | platform | `platform#44` |
| 0070 | The web player is the browser, not a media framework | web | web | `web#5` |
| 0071 | Content artwork is stored on the node | architecture | platform | `platform#45` |
| 0072 | The guaranteed metadata provider needs no credential | architecture | module-cinemeta | `module-cinemeta#1` |
| 0073 | Stream resolution is decoupled from metadata provenance | architecture | platform | `platform#46` |
| 0074 | Artwork is a candidate set | architecture | platform | `platform#47` |
| 0075 | The artwork provider role | architecture | sdk | `sdk#6` |
| 0076 | A curated stream provider beside the addon host | module-aiostreams | module-aiostreams | `module-aiostreams#1` |
| 0077 | go-plugin is the extension module harness | architecture | sdk | `sdk#7` |
| 0078 | Core modules keep their repositories; CI carries the version bump | architecture | platform | `platform#48` |
| 0079 | The Platform manages extension modules; the Supervisor manages the binary | architecture | platform | `platform#49` |
| 0080 | Deployment topologies: a native binary that runs in a container or on bare metal | architecture | platform | `platform#50` |
| 0081 | Extension installation is user-initiated and persistent | platform | platform | `platform#51` |
| 0082 | Components are authored only in the contract, and clients bundle none | architecture | contracts | `contracts#7` |
| 0083 | One generated SDUI vocabulary | contracts | contracts | `contracts#8` |
| 0084 | Vocabulary negotiation and deliberate degradation | architecture | platform | `platform#52` |
| 0085 | Module types are namespaced | architecture | contracts | `contracts#9` |
| 0086 | Bindable props, and no expression language | architecture | contracts | `contracts#10` |
| 0087 | State scopes | architecture | contracts | `contracts#11` |
| 0088 | Fields and forms | architecture | contracts | `contracts#12` |
| 0089 | Validation, and the symmetric rejection | architecture | contracts | `contracts#13` |
| 0090 | Lifecycle triggers, and the telemetry lane that is not needed | architecture | web | `web#6` |
| 0091 | Accessibility in the contract | architecture | contracts | `contracts#14` |
| 0092 | Focus and spatial navigation | architecture | contracts | `contracts#15` |
| 0093 | Lazy lists | architecture | contracts | `contracts#16` |
| 0094 | The conformance corpus | architecture | contracts | `contracts#17` |
| 0095 | The generated vocabulary reference | contracts | contracts | `contracts#18` |
| 0096 | Retiring `$value`, and the merge rule it hid | architecture | contracts | `contracts#19` |
| 0097 | The pre-session tree, and what a locked door may say | architecture | platform | `platform#53` |
| 0098 | Claiming an unclaimed server | platform | platform | `platform#54` |
| 0099 | The development module repository, and the build tag that keeps it out of releases | platform | platform | `platform#55` |
| 0100 | The browse roles rank their providers; they do not union them | platform | platform | `platform#56` |
| 0101 | The pre-session bootstrap carries its own vocabulary | architecture | platform | `platform#57` |
| 0102 | The session credential is a bearer pair every client can hold | architecture | platform | `platform#58` |
| 0103 | One library, many viewers | platform | platform | `platform#59` |
| 0104 | The library is built from rules, and a job maintains it | platform | platform | `platform#60` |
| 0105 | Official builds carry project credentials, and a personal key replaces one | architecture | architecture | `architecture#4` |
| 0106 | The pre-session action lane | architecture | platform | `platform#61` |
| 0107 | The Platform keeps what a source told it, and tops up the tree | platform | platform | `platform#62` |
| 0108 | The origin is a pipe only where it must be | platform | platform | `platform#63` |
| 0109 | The transcoded stream is segmented, not byte-addressed | architecture | platform | `platform#64` |
| 0110 | The segment length is measured from the source, not chosen | platform | platform | `platform#65` |
| 0111 | The playlist is a nominal grid, and a segment index is a seek instruction | platform | platform | `platform#66` |
| 0112 | Language is a person's preference, and subtitles answer to whether it was met | platform | platform | `platform#67` |
| 0113 | Subtitles are a rendition, extracted a window at a time | platform | platform | `platform#68` |
| 0114 | A subtitle track has a form, and only one form can be burned into the picture | platform | platform | `platform#69` |
| 0115 | A styled subtitle track goes to the client whole, and burning is what is left when it cannot | architecture | platform | `platform#70` |
| 0116 | A preference is a default, an override is one sitting | platform | platform | `platform#71` |
| 0117 | The subtitles role gets a consumer, and the Platform fetches what it finds | platform | platform | `platform#72` |
| 0118 | Playing something unowned adds it | platform | platform | `platform#73` |
| 0119 | Operational findings are durable state | architecture | platform | `platform#74` |
| 0120 | The children listen on Unix sockets | architecture | platform | `platform#75` |
| 0121 | Two supervised images, a DIY path, and the Supervisor's own contract dependency | architecture | supervisor | `supervisor#6` |
| 0122 | Two signing keys, held offline, rotated by overlap | architecture | platform | `platform#76` |
| 0123 | The Supervisor answers the Platform's client surface when the Platform is absent | supervisor | supervisor | `supervisor#7` |
| 0124 | The Platform and the Shell are resolved independently and paired by contract major | architecture | supervisor | `supervisor#8` |
| 0125 | Major upgrades are staged, never automatic | architecture | supervisor | `supervisor#9` |
| 0126 | Before 1.0, the upgrade caution window shifts by one | architecture | supervisor | `supervisor#10` |
| 0127 | The monitored version is the contract, not the artefact | architecture | supervisor | `supervisor#11` |
| 0128 | OpenTelemetry is the telemetry implementation | architecture | sdk | `sdk#8` |
| 0129 | The upgrade channel is the handoff and the register | architecture | platform | `platform#77` |
| 0130 | The module metric surface | architecture | sdk | `sdk#9` |
| 0131 | Passkeys are an optional layer on a public origin | platform | platform | `platform#78` |
| 0132 | TOTP is the second factor that works everywhere | platform | platform | `platform#79` |
| 0133 | An optional capability is announced once, when it becomes possible | platform | platform | `platform#80` |
| 0134 | The install key | platform | platform | `platform#81` |
| 0135 | The SDK carries no implementation | architecture | sdk | `sdk#10` |

---

*Generated 2026-08-10 from the corpus at `docs/adr/` and a full reference sweep of the twelve repositories on disk. `supervisor` was not available to scan; its inbound reference load is unmeasured.*
