# [Jules Task] Quickstart role separation check

## Problem
We need to ensure `docs/quickstart.md` clearly separates the Hub/Playbook repository from the future template repository to avoid user confusion.

## Scope
- Inspect `docs/quickstart.md` (specifically the introduction and Step 1).
- Make a tiny wording cleanup **only if** the copy-first path is unclear or if the distinction between this Hub and the dedicated template repo needs reinforcement.
- Ensure the tone matches the "One Repository, Three Roles" framing in the main README.

## Non-goals
- Do not change workflows or repository configuration.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria
- [ ] `docs/quickstart.md` wording is checked for role separation.
- [ ] Any necessary cleanups are minimal and docs-only.
- [ ] The "copy-first" path remains clear for users.

## Validation
- Confirm the wording aligns with the repository's role as a Hub.
- Run Markdown hygiene checks.

## Workflow Level
- Level 1 - Human-led Jules workflow
