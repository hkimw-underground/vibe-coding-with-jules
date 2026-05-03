# [Jules Task] Draft minimal issue templates for jules-workflow-template

## Goal
Draft minimal issue templates (`jules_task.yml` and `workflow_experiment.yml`) for the future `jules-workflow-template`.

## Context
These templates will serve as the starting point for users adopting the Jules workflow in the new template repository. They should be clean, reusable, and stripped of project-specific fields while maintaining core workflow principles.

## Scope
Create a PR drafting the following files in `.github/ISSUE_TEMPLATE/`:
- `jules_task.yml`
- `workflow_experiment.yml`

The forms must capture:
- **goal**
- **context**
- **scope**
- **non-goals**
- **acceptance criteria**
- **validation**
- **output required**

## Non-goals
- Do not add heavy automation.
- Do not add labels through admin settings.
- Do not include project-specific fields from Case Study A.
- Do not claim experiments are the default.

## Acceptance Criteria
- [ ] The issue requests minimal reusable forms.
- [ ] The issue keeps experiments clearly marked.
- [ ] The issue asks for docs-only output.

## Validation
- Confirm the presence of the YAML files in the PR.
- Verify that the templates contain all requested fields.

## Workflow Level
- Level 1 - Human-led Jules workflow
