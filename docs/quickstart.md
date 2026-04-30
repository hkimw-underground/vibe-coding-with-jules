# Quickstart Guide

This guide shows you how to adopt the AI Coding Workflow Starter Kit for Jules in your own repository.

## 1. Copy the Starter Kit Files

Copy the following files and directories from this repository into your own:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/jules_task.yml
.github/ISSUE_TEMPLATE/workflow_experiment.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/docs-and-templates.yml
```

*(Optional but recommended)* You can also copy `prompts/` and `examples/` for reference.

## 2. Customize the Files

Edit the copied files to match your project:

- Update `.github/PULL_REQUEST_TEMPLATE.md` to remove any validation steps that do not apply to your project.
- Adjust `AGENTS.md` if your project has specific rules (e.g., "Always use TypeScript" or "Run `npm test` before submitting").
- Modify the `.github/workflows/docs-and-templates.yml` file to fit your CI setup, or remove it if you prefer different validation.

## 3. Create the First Jules-Ready Issue

Create an issue in your repository. Be specific and scoped.

**Good Issue Example:**
```text
Title: Add a Quickstart guide

Body:
Create `docs/quickstart.md`.
It should include steps on how to copy starter kit files and create a Jules issue.
Do not modify other existing documentation.
```

## 4. Hand the Issue to Jules

Use the issue as the single source of truth. When assigning the task to Jules, simply provide the link to the issue or paste its contents. Jules will use the instructions in the issue and `AGENTS.md` to guide its work.

## 5. Review the First Pull Request

Jules will create a pull request linked to the issue. Before merging, verify:

- Does the PR strictly solve the linked issue?
- Is the scope controlled (no unrelated files changed)?
- Are assumptions clearly stated in the PR description?
- Are validation steps or tests included?

## 6. Validate Docs and CI

Ensure all automated checks pass:

- Check that Markdown hygiene passes.
- Confirm YAML files are structurally valid.
- Verify that your project's primary CI pipeline passes.

If CI fails, do not ignore it. Ask Jules to investigate and fix the root cause.

## 7. What Not to Automate at the Beginning

Start with the **Human-led Jules workflow** (Level 1).

- **Do not auto-merge.** Always require human review.
- **Do not skip CI.** Let CI gate every merge.
- **Do not let Jules decide project architecture.** Maintainers own the direction.
- **Do not present Jules as a human.** Keep the engineering history transparent.
