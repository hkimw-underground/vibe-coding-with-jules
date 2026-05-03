# [Jules Task] Applied rollout guide gap check

**Labels**: `jules`, `documentation`, `operations`

## Problem

The repository contains operations guides for labels, triage, and sequencing, but it may lack a clear, step-by-step path for applying the Jules workflow to an existing, non-starter-kit repository.

## Goal

Ensure that `docs/operations/` provides a clear starting point for maintainers who want to adopt this workflow in their own projects.

## Scope

- Inspect the contents of `docs/operations/`.
- If a guide for applying Jules to an existing repo is missing, propose a minimal `apply-to-existing-repo.md` outline.
- If a relevant guide exists but isn't easily discoverable, add a tiny link or note to the appropriate operations document.
- Ensure the guidance remains practical, GitHub-native, and frames Jules as an AI coding agent.

## Non-goals

- Do not change workflows.
- Do not change repository configuration.
- Do not auto-merge.
- Do not present Jules as a human contributor.
- Do not make broad rewrites.
- Do not modify unrelated files.

## Acceptance Criteria

- [ ] `docs/operations/` is audited for rollout guidance.
- [ ] A minimal guide is proposed or a discoverability link is added.
- [ ] Markdown hygiene passes.
- [ ] The change is docs-only and low-risk.

## Validation

- Confirm the existence or update of the rollout guide.
- Verify that links are relative and functional.
- Confirm Jules is framed as an AI coding agent.

## Workflow Level

- Level 1 - Human-led Jules workflow
