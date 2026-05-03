# [Jules Task] Fleet wave 10-8: prompts directory index check

## Goal
Check whether the `prompts/` directory has enough context for maintainers to use prompts safely and update its index if necessary.

## Problem
The `prompts/` directory contains reusable prompts for Jules, but it may lack a clear index or README explaining how maintainers should use these prompts safely and effectively.

## Scope
- Inspect the `prompts/` directory.
- Update only a prompt README or a small prompt note (e.g., `prompts/README.md`) if one exists.
- If there is no obvious file, report no change rather than creating broad new content.

## Non-goals
- Do not change workflows.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria
- [ ] The `prompts/` directory has been inspected.
- [ ] A `README.md` or similar index file in `prompts/` is updated or verified as sufficient.
- [ ] No broad new content is created if no obvious file exists.
- [ ] Markdown hygiene passes.

## Validation
- Confirm that any changes to `prompts/` are minimal and focused on documentation/indexing.
- Confirm that Jules reported no change if no suitable index file was found.

## Metadata
- Labels: `jules`
- Track: Review-Driven
