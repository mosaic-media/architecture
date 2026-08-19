# A Status says whether a record is agreed, and says built-ness separately

**Status:** Accepted, and applied in the same change — sixteen records were
relabelled. Fleet-wide convention, recorded here because no mechanism enforces it
and this repository holds the decisions that have none.

## Context

Sixteen records across five repositories carried `**Status:** Proposed`, and every
one of them states a decision in the imperative in its Decision section. In this
corpus the word had come to mean *decided, not fully built*. Everywhere else in
the world it means *not yet agreed*.

That is not a tidiness problem. It is a trap laid for exactly the reader this
corpus is written for. An agent — or a person — turned loose on the records reads
sixteen settled decisions as open ones and re-litigates them, or reads them as
built and writes code against machinery that does not exist. Both failures are
expensive and neither is visible until somebody has done the work.

The fix is nearly free, because **both axes are already there.** Every one of
those sixteen status lines already states built-ness separately, in its own words:
"Nothing here is built", "Partly built", "built in part", "the CI release matrix
is built (the producing half)". The second axis was never missing. Only the first
word was wrong.

## Decision

**The first word of a Status says whether the record is agreed, and nothing else.**

- **Proposed** — put up, not yet agreed. Do not build against it.
- **Accepted** — agreed. It is what Mosaic has decided, whether or not any of it
  exists yet.
- **Superseded** — replaced, wholly or in part, by a record it names and which
  names it back.

**Built-ness is stated separately in the same line, in prose, and never encoded in
that first word.** It is the more variable of the two — a record is commonly half
built — and prose carries "the producing half is built and the consuming half does
not exist" in a way no keyword does.

**The sixteen are relabelled to Accepted in the same change as this record**, each
keeping its existing built-ness sentence untouched. Every one was checked
individually rather than swept: all sixteen state a decision, none is a proposal
awaiting agreement. Relabelling is a Status-line edit, which is precisely the edit
the append-only rule permits — the bodies are not touched.

**Most records here are born Accepted**, because this project writes a record once
the decision is made rather than to open a debate. *Proposed* stays available for
the case it names and should be rare.

## Alternatives considered

**Leave it and document the local meaning.** *Rejected:* it asks every reader to
learn that one word means the opposite of what it says, and the readers who miss
the note are exactly the ones the note exists for.

**A third status meaning "agreed but unbuilt".** *Rejected:* it merges the two
axes into one keyword again, at four values instead of three, and it still cannot
say "half".

**Drop Status and infer state from the roadmap.** *Rejected:* the roadmap tracks
the build across repositories and a record is evidence of a decision. Making one
read the other to know what it is defeats both.

## Consequences

**Nothing enforces this.** It is a convention kept by whoever writes the file, like
the rest of what a `CLAUDE.md` says.

**Enforcement is available cheaply and is not done here.** `adr_index.py` already
parses the Status line to build the index table, so checking that its first word is
one of three known values is a few lines in a tool that already reads the text. It
is a fleet tool change and therefore a re-vendor across every repository, which is
its own change rather than a side effect of this one — and worth pairing with the
re-vendor those copies already need.

**A record that genuinely is a proposal now has somewhere to live**, which it did
not while the word meant something else. That is the smaller half of the value and
the part that will matter later.
