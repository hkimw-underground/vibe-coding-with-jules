# [Jules Task] Draft lightweight CI workflow for template repository

## Problem
Future template repositories need a standard, lightweight CI workflow to ensure basic health (file existence, Markdown quality, and YAML validity) without adding the complexity of heavyweight dependencies, package publishing, or release automation.

## Scope
- Draft a minimal GitHub Actions workflow specification.
- The workflow should include checks for:
    - Presence of required files (e.g., `README.md`, `LICENSE`, `AGENTS.md`).
    - Markdown hygiene (e.g., basic readability, no trailing spaces).
    - YAML syntax validation for all files in `.github/workflows/`.
    - A basic safety check to ensure no obvious forbidden private files (like `.env` or secret keys) are included in the repository structure.
- Request a documentation/specification output (`docs/spec/ci-draft.md`) before any implementation.

## Non-goals
- Do not create or modify real GitHub Actions workflows in other active repositories.
- Do not add package publishing logic.
- Do not add release automation or version tagging.
- Do not add heavyweight dependencies or complex build systems.

## Acceptance Criteria
- [ ] The issue defines a minimal CI concept focused on health and safety.
- [ ] The draft workflow is designed to be safe and understandable for a beginner template repository.
- [ ] The task explicitly requests a documentation or specification output first.

## Validation
- Review the drafted specification for alignment with the "lightweight" and "safe" goals.
- Confirm the proposed checks are feasible using standard, minimal tools (e.g., shell scripts, basic Ruby/Python/Node scripts already present in the environment).

## Workflow Level
- Level 1 - Human-led Jules workflow
