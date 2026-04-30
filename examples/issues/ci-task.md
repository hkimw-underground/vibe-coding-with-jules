# [Jules Task] Add Python 3.12 to test matrix

## Problem

Python 3.12 was released recently, but our GitHub Actions test suite only runs against Python 3.10 and 3.11. We need to ensure our library is compatible with 3.12.

## Scope

- Update `.github/workflows/test.yml` to include `3.12` in the `python-version` matrix.
- Ensure any `actions/setup-python` steps are compatible with 3.12 (e.g., using `v5`).

## Non-goals

- Do not update the minimum required Python version in `setup.py` or `pyproject.toml` (we still support 3.10).
- Do not fix code deprecation warnings in this PR; we will handle those in a separate task.

## Acceptance Criteria

- [ ] `test.yml` includes Python 3.12 in the matrix.
- [ ] GitHub Actions syntax is valid.

## Validation

The PR should confirm:
- The YAML syntax passes validation.
- The CI workflow triggers successfully on the PR and passes for all three Python versions.

## Jules Instructions

Focus only on updating the CI configuration. Do not modify application code. If tests fail on 3.12 due to our code, mention it in the PR description but do not attempt to fix it in this PR.
