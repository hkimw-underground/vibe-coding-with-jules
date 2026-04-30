# Quickstart Guide: Adopting the Jules Workflow

This guide provides a copy-ready process for adopting the Jules AI coding workflow in your own repository.

## 1. Copy the Starter Kit Files

Copy these core files into your target repository:

| Path | Description |
| --- | --- |
| `AGENTS.md` | Core instructions and project context for Jules. |
| `.github/ISSUE_TEMPLATE/` | Scoped issue templates for tasks and experiments. |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template with validation checklists. |
| `.github/workflows/docs-and-templates.yml` | Lightweight CI for Markdown and YAML hygiene. |

**Optional but recommended:**
- `prompts/`: Reusable prompts for handoffs and reports.
- `examples/`: Reference issues and PR reviews.

## 2. Customize Your Configuration

Edit these fields to match your repository:

- **`AGENTS.md`**: Update the "Repository Structure" and any specific coding standards or "Memories" relevant to your project.
- **`.github/ISSUE_TEMPLATE/jules_task.yml`**: Update the `labels` or `assignees` if you use specific ones for AI tasks.
- **`.github/workflows/docs-and-templates.yml`**: Update the `required_paths` list if you choose not to copy certain optional files.

## 3. Create Your First Jules-Ready Issue

Start with a small, well-defined task. Avoid vague requests like "refactor the project."

**Example Issue Body:**
```text
[Jules Task] Add a basic unit test for the `utils/math.py` module.

Problem:
The math utility functions are currently untested.

Scope:
- Create `tests/test_math.py`.
- Add tests for `add`, `subtract`, and `multiply` functions.

Acceptance Criteria:
- Tests pass locally.
- 100% coverage for `utils/math.py`.
```

## 4. Hand the Issue to Jules

1. Open the issue in GitHub.
2. In your Jules interface (or agentic environment), point Jules to the issue URL.
3. Jules should create a plan, execute the changes, and open a Pull Request.

## 5. Review the First PR

Treat Jules like a junior engineer. Do not auto-merge.

- **Check Scope**: Did Jules touch unrelated files?
- **Verify Logic**: Does the code solve the problem described in the issue?
- **Read History**: Are the commit messages and PR description clear?
- **Request Changes**: If something is wrong, comment on the PR and ask Jules to fix it.

## 6. Validate Before Merge

1. Ensure all CI checks pass.
2. Run the code locally if possible.
3. Verify that documentation (like `AGENTS.md`) is updated if the project structure changed.

## What NOT to Automate (Yet)

As you begin, keep these steps manual to maintain quality:

- **Architecture Decisions**: Humans should define the high-level design.
- **Final Merge**: Always require a human "LGTM" before merging to `main`.
- **Large Refactors**: Break big changes into small, Jules-sized issues.

---

*Note: Jules is an AI coding agent. Maintain a clean engineering history by following the Issue → Jules → PR → Review flow.*
