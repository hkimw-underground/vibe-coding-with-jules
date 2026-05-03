# [Jules Task] Draft minimal PR template for template repository

## Problem
The future template repository needs a minimal, reusable Pull Request template. The current PR template in the hub repository contains hub-specific workflow levels and experiment options that might be too complex for a new project.

## Scope
- Draft a minimal `.github/PULL_REQUEST_TEMPLATE.md` for the template repository.
- Include the following essential sections:
  - **Summary**: A brief description of changes.
  - **Linked Issue**: A mandatory link to the originating issue.
  - **Validation**: Checkboxes for tests and manual validation notes.
  - **Scope Control**: Affirmations that no unrelated changes or refactors are included.
  - **Maintainer Review Checklist**: A short list of checks for the human reviewer.

## Non-goals
- Do not include hub-specific workflow levels (Level 4, Experiments, etc.).
- Do not add complex automation or bot instructions to the template.

## Acceptance Criteria
- [ ] The drafted PR template is concise and reusable.
- [ ] Essential safety and validation checks are preserved.
- [ ] The template reinforces the human-led Review-Driven workflow.

## Validation
- Review the drafted template for clarity and completeness.
- Ensure the Markdown syntax is correct.

## Workflow Level
- Level 1 - Human-led Jules workflow
