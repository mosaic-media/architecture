# Claude Instructions — Mosaic architecture

This repository holds the documentation that belongs to no single repository:
what Mosaic is, how it is built, where the build has got to, and the decisions
with no enforcing mechanism anywhere. It also owns the decision-record tooling
the whole fleet vendors, and the reusable workflow that publishes every
repository's Pages site.

It contains no implementation. Everything it describes lives in a sibling
repository, and **the source is authoritative, not this repository.**

## Rules every Mosaic repository follows

These are the fleet-wide conventions. Every other repository's `CLAUDE.md` links
here rather than restating them, so this is the only copy.

### What a CLAUDE.md may say

**It states rules, and facts about its own repository. It does not state facts
about another one — it links instead.** An audit of all thirteen found 74 stale
claims, and 62 of them were assertions about somebody else's repository. A fact
about this repository stays true because whoever changes the code changes the
sentence in the same commit. A fact about another one dies the moment they edit
it, and nothing here goes red.

The same goes for anything already published in a generated artefact — versions,
counts, what is built. Point at the artefact.

**Nothing enforces this.** It is a convention, kept by whoever writes the file.
The one fleet-wide rule that *is* enforced is the citation form below.

### Decision records

- **`docs/adr/`**, numbered from 1 in every repository, with `docs/adr/README.md`
  a generated index. Read the index first; it is the bounded thing.
- **A record's heading carries no number.** The number lives in the filename and
  the index, so a record's anchor survives renumbering.
- **Cite a record as `repo#N`, and make it a link** — a relative path within a
  repository, an absolute URL across them, a bare label only where no URL is
  possible, such as a code comment or a Dockerfile.
- **Records live with the code that enforces them** — the spec file, the lint
  gate, the conformance corpus, the composition root, the release workflow. A
  decision can bind five repositories and still have one steward. Only the
  records with no enforcing mechanism anywhere stay here.
- **They are append-only.** A record is evidence, not documentation, and its
  value is that it was not edited afterwards. State changes go in the
  `**Status:**` line and nowhere else. A reversal earns a new record that
  supersedes it, with both pointing at each other through their Status lines; the
  old body stays exactly as it was. An unbuilt decision is not a superseded one.

The old unqualified spelling — the bare word followed by a number — is refused by
`scripts/adr_lint.py`, which every repository vendors and runs in its own gate.
The reason it is worth a lint: once every repository numbers from 1, a stale
unqualified citation does not dangle. It resolves, quietly, to whichever record
the citing repository happens to hold at that number, which is a different
decision. No 404 and no red test.

(The lint cannot tell quoting from citing, so a document that spells the old form
out fails it. That is why this paragraph describes it instead.)

### The roadmap

**`docs/roadmap.md` here is the single record of where the build is, across every
repository**, because a milestone spans repositories by construction. Read it
before starting and update it in the same session as the change that dates it —
not in a follow-up, which does not happen.

A slice that lands is marked landed with what it left out named in the same
sentence; "built" with no qualifier claims the whole slice shipped. Implementation
that departed from its record is recorded where it departed. A capability with no
client path is not done — it is [owed](docs/unreachable-capability.md).

### Demonstrated, not asserted

**Say what you actually ran.** A skipped test is not a passed test. Each
repository's container is the authority on its own gate, and the checks that
matter fail *soft*: a missing PostgreSQL skips storage tests and still prints
`ok`, a missing generator toolchain produces a drift guard that passes by not
running. Where a container cannot be run, running what you can on the host beats
running nothing — provided you report which checks ran and which did not.

### Commit and push

- **Commit and push each repository separately.** They are siblings on disk and
  independent in git.
- **Commit author identity** is `AdamNi-7080 <anicholls41@gmail.com>`. Set it
  repo-locally rather than globally if git has none configured.
- **Push once the change has been demonstrated working in this session.** Commit
  locally and say so otherwise. **Force-push always requires asking.**

## Rules for this repository

**Read the code before writing about it.** Do not describe a contract, a package
or a behaviour from what another document says it is — open the file. This
repository once held two hundred documents describing a system nobody had checked
against the source, and the result was a roadmap built against an abandoned
storage model. If a document here disagrees with the source, the document is
wrong; fix it in the same session.

**Delete, do not annotate.** Superseded content is removed — git retains it. A
banner reading "this section is historical" does not outweigh the three hundred
lines beneath it still asserting the old thing.

**One authoritative statement per fact.** This is the rule the corpus breaks most
often and most expensively: `nav:` once carried a second copy of every record's
status and had drifted on four of them.

**No description ahead of implementation.** Roadmaps may look forward;
descriptions of the system may not. If it is not built, omit it or say plainly
that it does not exist.

**Do not create new documents.** Four pages plus the decision records. A fifth
needs a reason that survives being asked why it does not belong in one of the
four.

**Do not resurrect the old taxonomy.** No MDL, MDS, MEG, MAC, MIP, MOP, MAD or
MDP identifiers, no document-type system, no chapter numbering, no metadata
blocks. Conventional filenames only.

**Respect the controlled vocabulary in `docs/index.md`.** One word, one meaning.
*Transport* meaning three different things is how an agent invented a module
transport layer the architecture forbids. When a word starts carrying two
meanings, add it to that table.

**State tradeoffs, do not smooth them over.** Compiling modules into one binary
trades isolation for speed. The previous corpus claimed both, and that claim
would have shipped a false security guarantee.

## The site

`docs/` is published to GitHub Pages with MkDocs Material.

- **Diagrams are Mermaid**, in a fenced ```` ```mermaid ```` block — they render
  on the site and in GitHub's Markdown view. Do not draw structure with ASCII
  arrows. A fenced text block is still right when fixed-width layout *is* the
  subject, such as a directory tree.
- **Adding a top-level page means editing `nav:` and `TOP_LEVEL` in
  `scripts/build_pdfs.py`.** That friction is deliberate.
- **Adding a decision record means editing `nav:` and nothing else.** Its PDF is
  derived from `nav:`, and the export refuses to run if a record is missing from
  `nav:` or `nav:` names a record with no file.
- **`nav:` labels come from each record's heading.** Never write a status into a
  label; the record's `**Status:**` line is where that lives.

`.github/workflows/pages-site.yml` is a **reusable workflow** that other
repositories call to publish their own README and records. Changing it changes
every caller's site.

## The tooling this repository owns for the fleet

`scripts/` holds the decision-record tools. **This repository is their source;**
other repositories vendor copies, and the copies say so in their header.

| | |
|---|---|
| `adr_index.py` | generates `docs/adr/README.md`; `--check` refuses a stale one |
| `adr_lint.py` | refuses an unqualified citation, an unresolvable `repo#N`, a cross-repository citation in Markdown that is not a link, and a link whose target is not the record its label names |
| `adr_rewrite.py` | rewrites citations from a mapping; `--requalify` follows records that move again |
| `vendored_scripts.py` | checks every repository's vendored copy against this one; `--write` re-vendors |
| `build_pdfs.py` | renders the site to PDF, deriving the record pages from `nav:` |

**Editing a tool here changes nothing anywhere else until it is re-vendored** —
and the other gates go on enforcing the previous version while reporting clean.
That is not hypothetical: widening the lint to read `.mod` files found four
citations that had survived the whole migration, and for three commits the other
copies could not see them. **Run `scripts/vendored_scripts.py --fleet .. --write`
in the same session as any change to a tool**, and commit each repository
separately. The check needs the siblings on disk, so it cannot run in CI here.

**The lint's `--max-unqualified` ceiling is a ratchet, not a target.** It counts
citations still in the old form, it only goes down, and it is at zero here. A
repository that reintroduces the old spelling raises its own ceiling rather than
lowering the bar; refuse that.

## The gate

```bash
docker compose -f docker-compose.test.yml run --rm test
```

That installs the pinned `requirements.txt`, then runs the record index check,
the citation lint and `mkdocs build --strict` — which is what catches a document
pointing at a page or an anchor that no longer exists, the ordinary consequence
of "delete, do not annotate".

The PDF export is a **separate service**, because it downloads a Chromium and its
system libraries to produce artefacts CI publishes anyway:

```bash
docker compose -f docker-compose.test.yml run --rm pdfs
```

Run it when changing `scripts/build_pdfs.py`, or to check that a Mermaid diagram
renders as a diagram rather than as a code block — the diagrams are drawn by
JavaScript, which is the whole reason the export drives a browser.
