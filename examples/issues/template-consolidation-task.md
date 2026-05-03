# [Jules Task] Consolidate scaffolding for jules-workflow-template

## Problem
The `jules-workflow-template` repository needs a complete set of minimal, reusable scaffolding files to serve as a clean "copy-first" starting point for new projects. Currently, several overlapping tasks exist for individual files (README, AGENTS.md, templates, prompts), which should be consolidated into one focused effort to avoid branch conflicts and ensure consistency.

## Scope
Draft the following minimal, reusable files for the future `jules-workflow-template` repository:

1. **README.md**:
   - Concise purpose and "copy-first" usage steps.
   - List of core files included.
   - Explicit "Review-Driven" default workflow (Issue -> PR -> Review -> Merge).
   - Safety notes framing Jules as an AI coding agent.
   - Link back to the `vibe-coding-with-jules` hub/playbook.

2. **AGENTS.md**:
   - Core rules: Issue as source of truth, small focused PRs, linked issues required, validation notes in descriptions.
   - No unrelated refactors or file modifications.
   - No human identity claims; human maintainer review/merge ownership.

3. **.github/ISSUE_TEMPLATE/**:
   - Minimal `jules_task.yml` and `workflow_experiment.yml` forms.

4. **Prompts**:
   - `prompts/issue-to-jules.md`: Concise handoff prompt.
   - `prompts/pr-review.md`: Quality and hygiene check prompt.
   - `prompts/maintainer-closeout.md`: Task completion and merge checklist.

5. **Design Hub-to-Template Path**:
   - Define which hub files are template-ready and where to place links in the hub documentation to guide users to the minimal template.

## Non-goals
- Do not create the template repository in this task.
- Do not add complex automation or project-specific fields.
- Do not claim autonomous workflows are the default.
- Do not delete hub-specific documentation.

## Acceptance Criteria
- [ ] All requested files are drafted and consolidated in one PR.
- [ ] Scaffolding is minimal, reusable, and stripped of hub-specific details.
- [ ] Human maintainer review is explicitly required in all documents.
- [ ] Jules is clearly framed as an AI coding agent throughout.

## Validation
- Review the consolidated drafts for clarity, consistency, and Markdown hygiene.
- Verify that the "copy-first" path is clear and doesn't confuse hub vs. template roles.

## Workflow Level
- Level 1 - Human-led Jules workflow
