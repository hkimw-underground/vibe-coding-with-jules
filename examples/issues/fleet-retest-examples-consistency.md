# [Jules Task] Fleet retest 2: examples index consistency check

## Problem

The index file `examples/issues/README.md` may be out of sync with the actual contents of the `examples/issues/` directory as new example tasks are added.

## Scope

- Inspect the `examples/issues/` directory.
- Audit `examples/issues/README.md`.
- Add any missing example files to the README index with a brief, one-sentence description.
- Remove or update any stale or incorrect entries.
- Ensure Markdown hygiene (no trailing spaces, final newline).

## Non-goals

- Do not change repository workflows.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not add broad new examples; only index existing ones.

## Acceptance Criteria

- [ ] `examples/issues/README.md` accurately lists all relevant example issues in the directory.
- [ ] Links in the README are functional.
- [ ] No stale entries remain.
- [ ] Markdown hygiene passes.

## Validation

- Verify that all files in `examples/issues/` (that are meant to be indexed) are present in `examples/issues/README.md`.
- Run a local Markdown hygiene check if available.

## Workflow Level

- Level 1 - Human-led Jules workflow
