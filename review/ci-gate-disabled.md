# The CI Quality Gate Is Disabled

**This is temporary and must be reversed.** It is recorded here rather than in `docs/` because it describes the state of the repository's tooling, not the architecture of Mosaic.

## What was changed

`.github/workflows/docs.yml` publishes the documentation site from `main`. That `deploy` job used to depend on all four quality checks:

```yaml
needs: [structure, vale, markdownlint, links]
```

That line has been removed. The four jobs still run on every push and pull request, and they still report pass or fail. They simply no longer block publication.

## Why

The gate was doing the opposite of its job. Three of the four checks fail on pre-existing content:

| Check | State | Cause |
|-------|-------|-------|
| `structure` — `validate_docs.py` | Failing | 3 findings: MIP-004, MIP-005 and MIP-006 have no content chapters |
| `vale` | Failing | 141 errors, ~1,800 warnings, almost all uppercase RFC 2119 keywords |
| `markdownlint` | Failing | ~1,384 findings, of which ~1,284 are unlabelled code fences |
| `links` — lychee | Passing | 0 errors |

None of these are regressions. They are the documentation debt the rewrite exists to clear. But while the gate was in place, the published site stopped updating — which blocked reading the documentation, which is a prerequisite for reviewing and fixing it.

Publication was blocked by problems that publication is needed to fix.

## When to re-enable

Restore the gate once the documentation rewrite is complete and the checks reflect real regressions rather than inherited debt. Concretely:

- [ ] Every specification is rewritten — see [rewrite-progress.md](rewrite-progress.md)
- [ ] `python3 scripts/validate_docs.py` passes, which requires MIP-004, MIP-005 and MIP-006 to gain content chapters (Q-019 in [open-questions.md](open-questions.md))
- [ ] The uppercase RFC 2119 conflict is resolved either way (Q-006) — the guides converted to sentence case, or MDG-001 chapter 10 amended to record them as an exception
- [ ] `MD040` cleared: every code fence carries a language
- [ ] `vale docs` and `markdownlint` report clean, or their remaining findings are deliberately accepted

## How to re-enable

Add the dependency back to the `deploy` job in `.github/workflows/docs.yml`:

```yaml
  deploy:
    name: Deploy to GitHub Pages
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: [structure, vale, markdownlint, links]
    runs-on: ubuntu-latest
```

Then delete this file, and remove the `TEMPORARY` comment block above that job.

## If the rewrite stalls

If the corpus is not going to be finished soon, do not simply leave this note here indefinitely. Prefer one of:

- **Partial gate.** Restore `needs: [structure, links]` only. Those two pass today apart from the three protocol stubs, so fixing Q-019 alone would make a real gate possible without waiting for the prose work.
- **Baseline.** Record the current findings so only new violations fail, which restores a meaningful gate immediately and keeps the debt visible.

An indefinitely disabled gate is worse than no gate, because the workflow still looks as though it protects something.
