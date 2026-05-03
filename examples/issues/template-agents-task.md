# [Jules Task] Draft minimal AGENTS.md for template repository

## Problem

The template repository needs a reusable `AGENTS.md` file that defines the core rules for Jules. However, it must be minimal and avoid hub-specific or case-study-specific assumptions (like hardware details or advanced autonomous workflows) to remain broadly applicable for new projects.

## Scope

Draft a minimal `AGENTS.md` covering the following core rules:
- **Issue as Source of Truth**: Treat the GitHub Issue as the primary source of requirements.
- **Small PRs**: Create focused, incremental pull requests.
- **Linked Issues**: Every PR must be linked to its originating issue.
- **Validation Notes**: Include clear validation steps in the PR description.
- **No Unrelated Refactors**: Do not perform opportunistic refactors outside the task scope.
- **No Unrelated Changes**: Do not modify files unrelated to the task.
- **No Human Identity Claims**: Do not claim human authorship or identity.
- **Human Ownership**: The human maintainer owns the review and merge process.

## Non-goals

- Do not copy the full hub `AGENTS.md` unchanged if it includes overly broad or specific context.
- Do not include `digital-logic-circuit` hardware details.
- Do not include autonomous workflows as the default operating model.

## Acceptance Criteria

- [ ] The drafted `AGENTS.md` is reusable and minimal.
- [ ] The Review-Driven workflow is kept as the default.
- [ ] The draft allows for future repository-specific adaptation.

## Validation

- Confirm the draft covers all requested core rules.
- Ensure the language is generic enough for a template repository.

## Workflow Level

- Level 1 - Human-led Jules workflow
