# Applied Repository Rollout

This guide explains how to apply the Jules workflow starter kit to an existing repository without confusing the playbook repository with the applied case study.

Use this guide when you want to take the workflow from `vibe-coding-with-jules` and install it into a real project.

## Case Study A example

We use `hkimw-underground/digital-logic-circuit` as the motivating example.

- `vibe-coding-with-jules` is the reusable hub and playbook.
- `digital-logic-circuit` is the applied case study.
- The case study should not be treated as the generic template.
- Lessons from the case study should be generalized back into this repo only after they are proven through real issues, PRs, CI checks, and human review.

## Rollout process

Do not copy every file from the starter kit at once. Start small, verify the workflow, and expand as needed.

### 1. Audit current repo state

Before adding the starter kit, check the repository baseline:

- Is there a clear `README.md` explaining the project?
- Are there existing linting, test, or documentation checks?
- What are the current branch protection rules?
- Which files are high-risk or frequently changed?
- Which areas require human judgment, hardware access, or security review?

### 2. Copy starter files

Copy only the essential files needed to establish the workflow boundary:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/jules_task.yml
.github/ISSUE_TEMPLATE/workflow_experiment.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/docs-and-templates.yml
docs/jules-workflow.md
```

You can add prompts and examples later after the first setup PR proves that the workflow works.

### 3. Adapt `AGENTS.md` to the repo domain

`AGENTS.md` is the primary rulebook for Jules. Customize it for the project's specific context.

For `digital-logic-circuit`, the file should explain that:

- the repository is a hardware/software capstone project
- Jules is an AI coding agent, not a human contributor
- the human maintainer owns hardware judgment, architecture, security, validation, review, and merge decisions
- changes to authentication, lock/unlock behavior, camera handling, model loading, GPIO, and fail-safe behavior require careful human review

For other repositories, replace those domain rules with the equivalent high-risk areas in that project.

### 4. Add issue templates

Add `.github/ISSUE_TEMPLATE/jules_task.yml` so Jules tasks start from scoped GitHub Issues.

A good issue should include:

- Goal
- Context
- Scope
- Non-goals
- Risk areas
- Acceptance Criteria
- Validation
- Output Required

### 5. Add a PR template

Add `.github/PULL_REQUEST_TEMPLATE.md` so every PR asks for:

- linked issue
- summary
- scope check
- validation notes
- maintainer review focus
- AI-agent disclosure when Jules assisted the work

### 6. Add lightweight CI

Add a small GitHub Actions workflow first. The goal is fast feedback, not heavy automation.

A good first CI workflow checks:

- YAML syntax
- Markdown hygiene
- required workflow files

For code-heavy repositories, add tests only when the expected test command is already clear.

### 7. Create the first Jules setup issue

Open a small, low-risk issue that installs or verifies the workflow.

Good first setup issues include:

- install the Jules workflow starter kit
- add or refine `docs/jules-workflow.md`
- validate Markdown and YAML workflow files
- document which areas require human hardware or security review

Avoid starting with broad code refactors or behavior changes.

### 8. Run the first Jules PR

Use the setup issue as the source of truth. Jules should create a small, focused PR.

During the first PR, check:

- whether Jules followed `AGENTS.md`
- whether the PR stayed in scope
- whether unrelated files were avoided
- whether validation notes are present
- whether CI passed

### 9. Review and merge

The human maintainer reviews the PR.

Before merge, check:

- Did Jules follow the issue?
- Did CI pass?
- Are the domain-specific safety rules still correct?
- Are there hardware, security, or deployment assumptions that need manual review?
- Is Jules framed as an AI coding agent rather than a human contributor?

Merge only when the maintainer is satisfied.

### 10. Feed lessons back into the starter kit

As the applied repository starts using Jules, keep notes about what worked and what was confusing.

Feed lessons back into `vibe-coding-with-jules` when they are generally useful, such as:

- better issue template wording
- stronger review checklist items
- clearer CI guidance
- safer language for hardware or security projects
- practical examples from real PR reviews

## What not to do

Do not treat an applied case study as the generic template. A case study contains project-specific assumptions.

Do not treat the starter kit as a replacement for human review.

Do not present Jules as a human contributor.

Do not start with autonomous workflows in production repositories.

## Summary

The rollout path is:

```text
Audit repo → copy minimal starter files → adapt AGENTS.md → open setup issue → Jules PR → CI → human review → merge → feed lessons back
```

This keeps the workflow practical, reviewable, and reusable across projects.
