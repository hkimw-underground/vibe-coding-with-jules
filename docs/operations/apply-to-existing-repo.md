# Applied Repository Rollout Guide

This guide explains how to apply the Jules AI Coding Workflow Starter Kit to an existing, real-world repository.

While the [Quickstart Guide](../quickstart.md) covers the basic setup, this rollout guide focuses on the practical steps needed to integrate Jules into a project that already has its own history, architecture, and team culture.

## Real-World Example: Case Study A

The `hkimw-underground/digital-logic-circuit` project serves as the motivating example for this guide. It is a real hardware/software capstone project that adopted this workflow.

- **Applied Case Study**: `digital-logic-circuit` (The real project)
- **Playbook Source**: `vibe-coding-with-jules` (This repository)

**Note**: Do not treat the case study repository as a generic template. Use this repository (`vibe-coding-with-jules`) as your source for the latest starter files and best practices.

---

## Rollout Process

### 1. Audit Current Repository State

Before adding AI workflows, understand the starting point.

- **Review branching strategy**: Is there a `main` or `develop` branch? Are there branch protection rules?
- **Check CI status**: Does the project already have automated tests or linting?
- **Identify high-traffic files**: Which files are most likely to cause merge conflicts?
- **Define Jules's role**: Is Jules being brought in for documentation, testing, or feature development?

### 2. Copy Starter Files

Copy the following core files from this starter kit into your project's root:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/docs-and-templates.yml
prompts/
examples/
```

### 3. Adapt `AGENTS.md` to the Project Domain

The `AGENTS.md` file is the most important document for Jules. It must be customized to your project.

- **Project Purpose**: Define what the project actually does (e.g., "A digital logic simulator for educational use").
- **Tech Stack**: Specify languages, frameworks, and hardware constraints.
- **Rules of Engagement**: Define where Jules is allowed to make changes and where it must ask for permission.
- **Verification**: List the commands Jules must run to verify its work (e.g., `npm test`, `pytest`, or hardware simulation scripts).

### 4. Add Issue and PR Templates

Ensure the templates in `.github/` align with your team's workflow.

- **Issue Template**: Use the `jules_task.yml` template to ensure every AI task has a clear Problem, Scope, and Acceptance Criteria.
- **PR Template**: Use the provided template to require Jules to link to the issue and provide validation notes.

### 5. Add Lightweight CI

If your project doesn't have CI, start with the provided `docs-and-templates.yml`.

- It ensures that Jules follows Markdown hygiene and YAML syntax rules.
- It prevents Jules from accidentally deleting or moving required workflow files.

### 6. Create the First "Jules Setup" Issue

Don't start with a complex feature. The first issue should be about establishing the workflow.

**Example Issue:**
```text
[Jules Task] Initialize Jules workflow and verify CI

Problem:
The repository needs to verify that the Jules workflow is correctly configured.

Scope:
- Check that AGENTS.md accurately reflects the current project structure.
- Ensure all .md files end with a newline (Markdown hygiene).

Acceptance Criteria:
- Docs CI passes.
- PR is created following the standard template.
```

### 7. Run the First Jules PR

Direct Jules to the setup issue. Observe its plan and execution.

- **Plan Review**: Check if Jules understands the `AGENTS.md` instructions.
- **Execution**: Watch for any unexpected file modifications.
- **PR Creation**: Ensure the PR description is clear and links back to the issue.

### 8. Human Review and Merge

**Human ownership is non-negotiable.**

- A human maintainer must review every line of code.
- Provide feedback to Jules if the PR doesn't meet project standards.
- Merge only when the maintainer is satisfied.

### 9. Feed Lessons Back into the Starter Kit

As you use Jules in a real project, you will discover new patterns, common failures, or better prompts.

- **Generalize lessons**: If you find a better way to structure an issue, update your local templates.
- **Contribute back**: If the lesson is applicable to other projects, consider opening a PR to this starter kit (`vibe-coding-with-jules`).

---

## Key Principles

1. **Jules is an AI Coding Agent**: Frame Jules as a managed contributor, not a human replacement or a black-box automation.
2. **Maintainer Ownership**: Humans remain responsible for architecture, security, and final validation.
3. **Process Over Code**: The goal is a readable, auditable engineering history in GitHub.
