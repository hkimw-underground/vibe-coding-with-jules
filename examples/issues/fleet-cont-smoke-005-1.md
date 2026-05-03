# [Jules Task] Fleet continuous smoke 1: docs index wording check

## Problem

This is a controlled live smoke for autorun-jules PR #18. The runner should be started with JULES_MAX_CONCURRENT=3, so only three tasks should dispatch at first and the remaining two should wait until a slot opens.

## Scope

Inspect `docs/operations/labels-and-triage.md` and check the description of the `jules` label.

The current text describes it as purely "informational," but in Fleet Mode v1, the `jules` label can also act as an automated dispatch trigger for the Continuous Scheduler.

**Proposed Change:**
Update the description of the `jules` label in `docs/operations/labels-and-triage.md` to acknowledge its role in automated dispatch if applicable.

Target file:
`docs/operations/labels-and-triage.md`

## Non-goals

- Do not change workflows.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria

- [ ] Exactly one GitHub Issue is created for this task.
- [ ] The issue is docs-only and low-risk.
- [ ] The `jules` label is applied.
- [ ] No PR is merged automatically.

## Validation

- Confirm the issue URL and `jules` label.

## Workflow Level

- Level 1 - Human-led Jules workflow
- Fleet Mode v1 pop-and-dispatch validation
