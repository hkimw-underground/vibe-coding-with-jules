# [Jules Task] Fleet smoke: add tiny docs queue note

## Problem

As we scale Jules usage and explore "Fleet Mode" (running multiple Jules tasks), we need to remind maintainers to keep initial queue tests small and focused to verify state accounting before scaling to large batches.

## Scope

- Add or refine a tiny documentation note in `docs/operations/one-jules-task-at-a-time.md`.
- The note should advise keeping Fleet queue tests small (e.g., 1-2 tasks) before scaling to ensure state accounting and labeling flows are working as expected.
- Ensure the note fits naturally within the "Why One Task at a Time?" or "When Are Concurrent Tasks Acceptable?" sections.

## Non-goals

- Do not change the fundamental "One Jules Task at a Time" rule.
- Do not add complex Fleet Mode configuration details.
- Do not modify any other files.

## Acceptance Criteria

- [ ] `docs/operations/one-jules-task-at-a-time.md` contains a note about small Fleet queue tests.
- [ ] The note is clear and concise.
- [ ] Markdown hygiene passes.

## Validation

- Review the changes in `docs/operations/one-jules-task-at-a-time.md`.
- Confirm the note is present and accurately reflects the goal of small-scale testing.

## Workflow Level

- Level 1 - Human-led Jules workflow
