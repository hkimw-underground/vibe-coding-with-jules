# [Jules Task] Draft minimal PR template for jules-workflow-template

## Problem
Create a minimal PR template for the future `jules-workflow-template` to make Jules-assisted work reviewable and auditable.

## Scope
Draft a `.github/PULL_REQUEST_TEMPLATE.md` file that includes the following sections:
- **Linked Issue**: A way to link to the originating issue (e.g., `Closes #`).
- **Summary**: A short description of the changes.
- **Scope**: What was changed and why.
- **Non-goals**: What was intentionally not changed.
- **Validation**: Evidence of testing or verification (manual or CI).
- **Risks**: Any potential risks or side effects.
- **Human Review Checklist**: Items for the maintainer to check during review.
- **Maintainer Merge Decision**: A section for the final approval.

## Non-goals
- Do not add auto-merge functionality.
- Do not use language that makes Jules look like a human contributor.
- Do not require complex external tooling or setup.
- Do not modify existing GitHub Actions workflows.

## Acceptance Criteria
- [ ] The PR template is concise and reusable.
- [ ] The template includes a section for validation notes.
- [ ] The template keeps human review as a mandatory part of the loop.
- [ ] The template clearly separates AI-assisted implementation from human maintainer oversight.

## Validation
- Confirm the draft file exists and matches the requirements.
- Verify that the template structure is consistent with other starter kit documents.

## Workflow Level
Level 1 - Human-led Jules workflow
