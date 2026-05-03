# [Jules Task] PR review examples tone check

## Problem

The example PR reviews in `examples/pr-reviews/` serve as a guide for human maintainers. We need to ensure they maintain a consistent tone that frames Jules as an AI coding agent and not a human contributor, as per the project's core principles.

## Scope

- Inspect the following files in `examples/pr-reviews/`:
  - `approve.md`
  - `request-changes.md`
  - `validation-needed.md`
- Perform a tiny tone cleanup **only if needed** to ensure the examples do not present Jules as a human colleague.

## Non-goals

- Do not change workflows or repository configuration.
- Do not auto-merge or self-merge.
- Do not make broad rewrites or opportunistic refactors.
- Do not modify files outside of `examples/pr-reviews/`.

## Acceptance Criteria

- [ ] Each reviewed file correctly frames the interaction as Maintainer -> AI Agent.
- [ ] No changes are made if the tone is already correct.
- [ ] Markdown hygiene passes.

## Validation

- Confirm that the wording in the PR review examples is practical and consistent with `AGENTS.md`.

## Workflow Level

- Level 1 - Human-led Jules workflow
