# Claude Instructions — Mosaic architecture

This repository holds Mosaic's cross-cutting documentation: what the system is,
how it is built, where the build has got to, and the decisions that belong to no
single repository. Implementation lives in the sibling repositories.

- **[docs/index.md](docs/index.md)** — what Mosaic is, the tradeoffs, the controlled vocabulary
- **[docs/architecture.md](docs/architecture.md)** — how the platform is built
- **[docs/roadmap.md](docs/roadmap.md)** — where the build is, across every repository
- **[docs/unreachable-capability.md](docs/unreachable-capability.md)** — what the Platform can do that nobody can ask it to do
- **[docs/adr/](docs/adr/)** — the decisions with no enforcing mechanism anywhere

## The source is authoritative, not this repository

These documents describe code that lives elsewhere. **Read the code before
writing about it.** Do not describe a contract, a package or a behaviour from
what a document says it is — open the file. This repository once held two hundred
documents describing a system nobody had checked against the source, and the
result was a roadmap built against an abandoned storage model.

If a document here disagrees with the source, **the document is wrong.** Fix it in
the same session rather than working around it.

## Rules

**Delete, do not annotate.** Superseded content is removed. Git retains it, so
nothing is lost. A banner reading "this section is historical" does not outweigh
the three hundred lines beneath it still asserting the old thing — that exact
pattern is what put a discarded analytical database back into a roadmap. It has
also been broken *here*: a correction appended to a paragraph, with the two false
sentences left standing above it.

**No description ahead of implementation.** Roadmaps may look forward.
Descriptions of the system may not. If it is not built, omit it or say plainly
that it does not exist.

**One authoritative statement per fact.** Never explain the same thing twice. This
is the rule the corpus breaks most often and most expensively: `nav:` carried a
second copy of every record's status and had drifted on four of them; the PDF
export carried a second list of records and covered fourteen of 135.

**Do not create new documents.** Four pages plus the decision records. A fifth
needs a reason that survives being asked "why does this not belong in one of the
existing four?"

**Do not resurrect the old taxonomy.** No MDL, MDS, MEG, MAC, MIP, MOP, MAD, MDP
or MRM identifiers. No document-type system, no chapter numbering, no metadata
blocks. Conventional filenames only.

**Respect the controlled vocabulary** in `docs/index.md`. One word, one meaning.
*Transport* meaning three different things is how an agent invented a module
transport layer the architecture forbids. When a word starts carrying two
meanings, add it to that table.

**State tradeoffs, do not smooth them over.** Compiling modules into one binary
trades isolation for speed. The previous corpus claimed both, and that claim
would have shipped a false security guarantee.

## What this repository keeps, and what it does not

**The records here are the ones with no enforcing mechanism in any repository** —
licensing, repository naming and topology, the module tier model, project
credentials in official builds. Everything else moved to the repository whose
spec file, lint gate, conformance corpus, composition root or release workflow
enforces it.

That test is the one to apply to a new record: *if this were revisited, whose
maintainer writes the successor, and where does the thing that enforces it live?*
A decision can bind five repositories and still have exactly one steward. Treating
every such decision as cross-cutting is what left 76 of 135 records with no home.

**The roadmap stays here** because a milestone spans repositories by construction,
and it is the single record of where the build is for all of them.

## The site

`docs/` is published to GitHub Pages with MkDocs Material, and every page is also
exported as a PDF.

- **Diagrams are Mermaid**, in a ```` ```mermaid ```` fence. They render on the
  site and in GitHub's Markdown view. Do not draw structure with ASCII arrows — it
  renders as a code block and reads as noise. A fenced text block is still right
  when fixed-width layout *is* the subject, such as a directory tree.
- **Adding a top-level page means editing `nav:` and `TOP_LEVEL` in
  `scripts/build_pdfs.py`.** That friction is deliberate.
- **Adding a decision record means editing `nav:` and nothing else.** Its PDF is
  derived from `nav:`, and the export refuses to run if a record is missing from
  `nav:` or `nav:` names a record with no file.
- **`nav:` labels are derived from each record's heading.** Do not write a status
  into a label; the record's `**Status:**` line is where that lives.

## The tooling this repository owns for the whole fleet

`scripts/` holds the decision-record tools. **This repository is their source**;
other repositories vendor copies, and the copies say so in their header.

| | |
|---|---|
| `adr_index.py` | generates `docs/adr/README.md`; `--check` refuses a stale one |
| `adr_lint.py` | refuses an unqualified citation, a `repo#N` that does not resolve, and a cross-repository citation in Markdown that is not a link |
| `adr_rewrite.py` | rewrites citations from a mapping; `--requalify` follows records that move again |
| `shared_rules.py` | writes `shared/repository-rules.md` into every repository's `CLAUDE.md` between its markers; `--check` fails on a copy that differs |
| `vendored_scripts.py` | checks every repository's vendored copy against this one; `--write` re-vendors |
| `build_pdfs.py` | renders the site to PDF, deriving the record pages from `nav:` |

**`shared/repository-rules.md` is the fleet's shared block.** Edit it here and run
`scripts/shared_rules.py --write`. Never edit the generated region in another
repository's `CLAUDE.md`; its own gate will refuse it.

**Every other repository vendors `adr_lint.py`, most also `adr_index.py`, and
each runs its copy in its own gate.** So editing a tool here changes nothing
anywhere else until it is re-vendored — and eleven gates go on enforcing the
version from before the edit, reporting clean. That is not hypothetical: widening
the lint to read `.mod` files found four citations that had survived the whole
migration, and for three commits the other copies still could not see them.
**Run `scripts/vendored_scripts.py --fleet .. --write` in the same session as any
change to a tool**, and commit each repository separately. The check needs the
siblings on disk, so it cannot run in CI here — that limit is real and is why the
habit matters.

**The lint's ceiling is a ratchet, not a target.** It is the count of citations
still written in the old unqualified form, it only goes down, and it is at zero
here. It was 4,618 across the fleet when the records were dispersed, which is why
the flag exists at all; a repository that reintroduces the old spelling raises its
own ceiling rather than lowering the bar, and that is the thing to refuse.

## The build runs in a container

```bash
docker compose -f docker-compose.test.yml run --rm test
```

That installs the pinned `requirements.txt` and runs the record index check, the
citation lint and `mkdocs build --strict`, which is what catches a document
pointing at a page or an anchor that no longer exists — the ordinary consequence
of "delete, do not annotate".

The PDF export is a **separate service**, because it downloads a Chromium and its
system libraries to produce artefacts CI publishes anyway:

```bash
docker compose -f docker-compose.test.yml run --rm pdfs
```

Run it when changing `scripts/build_pdfs.py`, or to check that a Mermaid diagram
renders as a diagram rather than as a code block. That is the whole reason the
export drives a browser: the diagrams are drawn by JavaScript.

## Working expectations

- Verify claims against the source repository rather than against another
  document.
- Prefer deleting to adding. This repository got into trouble by growing.
- When something is undecided, say so. An honest gap is worth more than a
  plausible invention that reads as settled.
- Commit with a message explaining what changed and why. If a change corrects
  something the documentation got wrong, say what it got wrong.

<!-- shared-rules:begin -->
## Rules every Mosaic repository shares

*Generated. The source is `architecture/shared/repository-rules.md`; edit it there
and run `scripts/shared_rules.py --write` across the fleet. A copy edited in place
fails its repository's gate, which is the point: these rules were eleven
hand-kept copies in four variants, and the abridged ones had quietly dropped the
reasoning while keeping the rules — and in one case dropped a rule outright.*

### What this file may say

**A `CLAUDE.md` states rules, and facts about its own repository. It does not
state facts about another one — it links instead.**

An audit of all twelve of these files against their source found 74 stale claims.
None of roughly 180 rules was wrong; 62 of the 74 were facts about somebody
else's repository. Ownership predicts rot: a fact about this repository stays true
because whoever changes the code changes the sentence in the same session, and a
fact about another one dies the moment they edit it with nothing here going red.

The same applies to facts this repository already publishes in a generated
artefact — counts, versions, what is built. Point at the artefact.

### Decision records live with the code they govern

Each repository owns the records whose *mechanism* it holds — the spec file, the
lint gate, the conformance corpus, the composition root, the release workflow.
A decision can bind five repositories and still have exactly one steward.

- **`docs/adr/`**, numbered from 1 in every repository, with `docs/adr/README.md`
  a **generated** index. Read the index first; it is the bounded thing.
- **A record's heading carries no number.** The number lives in the filename and
  the index only, so a record's anchor survives being renumbered.
- **Cite a record as `repo#N`, and make it a link** — a relative path within a
  repository, an absolute URL across them, and the bare label only where no URL
  is possible, such as a code comment or a Dockerfile. The old `ADR NNNN`
  spelling is refused by a lint: once every repository numbers from 1, that form
  resolves quietly to a *different* record instead of dangling, and no tool in
  the fleet could detect it.
- **Cross-cutting records stay in [`architecture`](https://github.com/mosaic-media/architecture)** —
  the ones with no enforcing mechanism anywhere: licensing, repository naming and
  topology, the module tier model.

### Decision records are append-only

An ADR is an account of what was decided and why, at a time. It is evidence, not
documentation, and its value is that it was not edited afterwards.

- **Never rewrite a record's body** — not to correct it, not to annotate it, not
  to add "as built, this differs". That turns a record into a running commentary
  and destroys the thing it is for.
- **State changes go in the `**Status:**` line and nowhere else** — built, built
  in part (naming the part), or superseded, wholly or partly.
- **A changed decision earns a new record that supersedes it**, with its own
  Context / Decision / Alternatives / Consequences, and both records then point
  at each other through their Status lines. The old body stays exactly as it was.
- **An unbuilt decision is not a superseded one.** "Not done yet" belongs in the
  Status line and the roadmap; only a reversal earns a new record.

### The roadmap is maintained, not consulted

**`docs/roadmap.md` in [`architecture`](https://github.com/mosaic-media/architecture)
is the single record of where the build is, across every repository.** It stays
there because a milestone spans repositories by construction. Read it before
starting, and **update it in the same session as the change that dates it** — not
in a follow-up, which does not happen.

- A slice that lands is marked landed, **with what it left out named in the same
  sentence**. "Built" with no qualifier claims the whole slice shipped.
- Implementation that departed from its record is recorded where it departed.
  The surprises are the most valuable thing in it.
- **Do not restate the roadmap here.** A second copy of "what is built" in a
  `CLAUDE.md` is how the first copy goes stale unnoticed.
- A capability with no client path is not done — it is
  [owed](https://github.com/mosaic-media/architecture/blob/main/docs/unreachable-capability.md).

### Demonstrated, not asserted

**Say what you actually ran.** A skipped test is not a passed test, and "it should
work" is not evidence.

Each repository's container is the authority on its own gate, and the command is
in that repository's section below. It exists because the checks that matter fail
*soft*: a missing PostgreSQL skips storage tests and still prints `ok`, a missing
generator toolchain produces a drift guard that passes by not running. Where the
container cannot be run, running what you can on the host is better than running
nothing — **provided you report which checks ran and which did not.** Claiming a
gate passed when it was not executed is the one thing this rule exists to stop.

### Commit and push

- **Commit and push each repository separately.** They are siblings on disk and
  independent in git.
- **Commit author identity** must be `AdamNi-7080 <anicholls41@gmail.com>`. If git
  has no identity configured, set it repo-locally rather than globally.
- **Push once the change has been demonstrated working in this session.** Commit
  locally and say so otherwise. **Force-push always requires asking.**
<!-- shared-rules:end -->
