# [Jules Task] Design copy-first path from hub to future jules-workflow-template

## Problem

We need to design a "copy-first" path that allows users to easily transition from this hub repository (`vibe-coding-with-jules`) to a standalone, minimal template repository (`jules-workflow-template`). Currently, this repo serves as both a playbook and a source for starter files, which might confuse users looking for a "clean" starting point.

## Scope

Docs-only planning for:
- Identifying where to link the future template repo (e.g., `README.md`, `docs/showcase.md`, `docs/quickstart.md`).
- Defining exactly which files should be copied first to the minimal template (e.g., `AGENTS.md`, `.github/`, `prompts/`).
- Determining which files should stay only in the hub (e.g., case studies, advanced workflow tracks, meta docs).
- Designing the messaging to avoid confusing readers between the "full playbook" (this hub) and the "minimal template".

## Non-goals

- Do not create the template repo in this task.
- Do not move files.
- Do not delete hub docs.
- Do not add repository settings changes.

## Acceptance Criteria

- [ ] The plan clearly separates hub and template responsibilities.
- [ ] The plan identifies specific locations in current docs for the new links.
- [ ] The messaging avoids promotional or hyped language.
- [ ] The plan is short and practical.

## Validation

- Review the proposed documentation updates in a follow-up task.

## Workflow Level

- Level 3 - Human issue only
