# [Jules Task] Add Linting Step to CI Workflow

## Problem
Currently, our CI workflow only runs tests. We need to add a linting step to ensure code quality and consistency across all pull requests before they are merged.

## Scope
- Modify `.github/workflows/ci.yml` to add a new job or step for linting.
- Use the project's standard linter (e.g., `eslint`, `flake8`, `rubocop` depending on the language).
- The CI should fail if the linting step finds any errors.

## Non-goals
- Do not fix existing linting errors in the codebase unless they prevent the new CI step from passing.
- Do not change the linter configuration file itself.
- Do not modify the test job.

## Acceptance Criteria
- [ ] `.github/workflows/ci.yml` includes a linting step.
- [ ] The linting step runs on every pull request.
- [ ] CI successfully fails if a linting error is introduced.

## Validation
- Verify the YAML syntax of the modified workflow file.
- Run the linter locally to ensure it works as expected before pushing.

## Workflow Level
- Level 1 - Human-led Jules workflow
