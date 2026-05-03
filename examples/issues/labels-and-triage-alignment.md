# [Jules Task] Align Labels and Triage with Review-Driven Track terminology

## Problem

The documentation in `docs/operations/labels-and-triage.md` describes the standard triage flow but does not explicitly name it the "Review-Driven" track, which is the primary terminology used in `docs/tracks/review-driven.md` and `AGENTS.md`. Consistency in terminology helps users navigate the workflow tracks.

## Scope

- Inspect `docs/operations/labels-and-triage.md`.
- Update the wording in the "Suggested Triage Flow" section or introduction to explicitly reference the "Review-Driven" track as the default workflow.
- Ensure the description of the flow remains consistent with the steps outlined in `docs/tracks/review-driven.md`.
- Perform a tiny wording cleanup only if needed to improve clarity and alignment.

## Non-goals

- Do not change the actual workflows or labels.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria

- [ ] `docs/operations/labels-and-triage.md` explicitly mentions the "Review-Driven" track.
- [ ] The terminology aligns with `docs/tracks/review-driven.md`.
- [ ] Markdown hygiene passes (newline at end, no tabs, 0 or 2 trailing spaces).

## Validation

- Read `docs/operations/labels-and-triage.md` to confirm the update.
- Verify consistency with `docs/tracks/review-driven.md`.

## Labels
`jules`, `documentation`, `workflow`

## Workflow Level

- Level 1 - Human-led Jules workflow
