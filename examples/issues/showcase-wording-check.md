# [Jules Task #FLEET-WAVE-010-2] Fleet wave 10-2: showcase copy-first wording check

## Problem
The `docs/showcase.md` file describes the "copy-first" reusable starter files. We must ensure it maintains the correct role separation: this repository is the **Hub and Playbook**, while providing files that can be copied to other repositories (or will eventually power the dedicated template repository). It should not be confused for the template repository itself.

## Goal
Inspect `docs/showcase.md` and make a tiny wording cleanup only if needed to ensure it doesn't sound like *this* repository is the dedicated template.

## Scope
- Inspect `docs/showcase.md`.
- Perform tiny wording cleanups if the current phrasing is ambiguous regarding its role as the Hub vs. a template.

## Non-goals
- Do not change workflows.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria
- [ ] `docs/showcase.md` clearly describes the files as reusable components of the starter kit.
- [ ] The wording avoids claiming this repository is the template repository.
- [ ] Changes are minimal and maintain the existing tone.

## Validation
- Review the wording changes for clarity.
- Run Markdown hygiene checks.

## Workflow Level
- Level 1 - Human-led Jules workflow

## Labels
- `jules`
