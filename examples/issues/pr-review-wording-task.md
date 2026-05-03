# [Jules Task] PR Review Examples Wording Check

## Problem

The examples in `examples/pr-reviews/` demonstrate how human maintainers provide feedback to Jules. We need to ensure that the wording in these examples consistently frames Jules as an AI coding agent and never implies human identity or authorship.

## Scope

- Inspect all files in `examples/pr-reviews/`.
- Perform tiny wording cleanups ONLY if the AI framing is weak or incorrect.
- Ensure the language reinforces that Jules is an AI agent being steered by a human.

## Non-goals

- Do not change workflows.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria

- [ ] All files in `examples/pr-reviews/` correctly frame Jules as an AI coding agent.
- [ ] No wording suggests human identity for Jules.
- [ ] Markdown hygiene is maintained.

## Validation

- Review the changes in `examples/pr-reviews/`.
- Confirm that the AI agent framing is strictly followed.

## Workflow Level

- Level 1 - Human-led Jules workflow
