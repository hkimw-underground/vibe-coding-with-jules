# [Jules Task] Fleet queue test size operations guide note

## Problem
Fleet queue tests should be conducted incrementally to ensure stability and reliable state accounting. We need to document the recommendation to start small before scaling to larger batches.

## Scope
- Update `docs/operations/one-jules-task-at-a-time.md` to include a short note about Fleet queue testing strategy.
- The note should recommend starting with 1 task, then 3 tasks, before moving to larger batches.

## Non-goals
- Do not change workflows or repository configuration.
- Do not perform unrelated documentation refactors.

## Acceptance Criteria
- [ ] `docs/operations/one-jules-task-at-a-time.md` contains the new note about Fleet queue scaling.
- [ ] The note is concise and clear.
- [ ] Markdown hygiene passes (no tabs, single newline at EOF, 0 or 2 trailing spaces).

## Validation
- Verify the content of `docs/operations/one-jules-task-at-a-time.md`.
- Ensure the documentation remains scannable and accurate.

## Workflow Level
- Level 1 - Human-led Jules workflow
