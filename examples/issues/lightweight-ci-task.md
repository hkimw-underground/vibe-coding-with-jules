# [Jules Task] Add lightweight CI for docs and templates

## Problem
The template repository needs a way to automatically validate documentation hygiene (no trailing spaces, final newline) and issue template YAML syntax to prevent regressions. It should be lightweight and avoid complex dependencies.

## Scope
- Create `.github/workflows/docs-and-templates.yml`.
- Add a job to validate YAML syntax in `.github/ISSUE_TEMPLATE/`.
- Add a job to validate Markdown hygiene (trailing spaces, final newline).
- Ensure the workflow runs on pull requests and pushes to `main`.

## Non-goals
- Do not add complex code coverage or deployment scripts.
- Do not add third-party actions unless necessary and minimal.
- Do not modify existing documentation.

## Acceptance Criteria
- [ ] `.github/workflows/docs-and-templates.yml` exists and is valid.
- [ ] YAML validation correctly identifies syntax errors in templates.
- [ ] Markdown validation correctly identifies hygiene issues.

## Validation
- Introduce a temporary YAML error to verify CI fails.
- Introduce a temporary trailing space to verify CI fails.
- Ensure CI passes once errors are corrected.

## Workflow Level
- Level 1 - Human-led Jules workflow
