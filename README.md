# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md) · [Contributing](./CONTRIBUTING.md) · [Code of Conduct](./CODE_OF_CONDUCT.md) · [Security](./SECURITY.md)

> Most AI coding demos show only the final code.  
> This project shows the process.

**AI Coding Workflow Starter Kit for Jules** is a reusable GitHub-native playbook for maintainers who want AI-assisted work to leave a clean engineering history. It provides templates for leading Jules through issues, pull requests, reviews, CI, case studies, and controlled automation.

---

## What This Is

This repository provides reusable templates and examples for running Jules inside normal GitHub development practice:

- scoped GitHub Issues
- Jules task handoff prompts
- small pull requests
- human review checklists
- CI-first validation
- case study documentation
- controlled automation experiments

The core message is simple:

> A human maintainer leads an AI coding agent through GitHub-native engineering practices.

Not:

> AI built the whole project by itself.

---

## Workflow Levels

This starter kit separates stable maintainer workflows from experimental automation.

| Level | Workflow | Human role | Status |
| --- | --- | --- | --- |
| 1 | Human-led Jules workflow | creates issue, reviews PR, merges | recommended default |
| 2 | Semi-autonomous Jules workflow | creates issue, reviews final PR | practical advanced mode |
| 3 | Human issue only | writes issue; Jules handles implementation and PR updates | advanced with strict CI |
| 4 | Daily agentic maintainer loop | steers direction from daily reports | advanced planning loop |
| 5 | No-human sandbox workflow | observes or audits only | experiment only |
| 6 | Jules + evaluator-driven evolution | defines objective/evaluator and reviews result | experiment only |

The default workflow is Level 1. Levels 5 and 6 belong in sandboxes, not unprotected production branches.

---

## Core Workflow

```text
Human maintainer opens a scoped GitHub Issue
        ↓
Jules implements the task
        ↓
Jules opens or publishes a focused PR
        ↓
CI validates the change
        ↓
Human maintainer reviews the diff
        ↓
Maintainer merges or requests changes
```

This keeps the process visible:

```text
Issue → Jules task → PR → Review → CI → Merge
```

If another developer cannot understand the history later, the workflow failed.

---

## Repository Structure

```text
.
├── README.md
├── README.ko.md
├── AGENTS.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── jules_task.yml
│   │   └── workflow_experiment.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── examples/
│   ├── issues/
│   └── pr-reviews/
├── docs/
│   ├── workflows/
│   │   └── workflow-levels.md
│   ├── experiments/
│   │   ├── no-human-only-jules-workflow.md
│   │   └── jules-alpha-evolve.md
│   └── case-studies/
│       ├── digital-logic-circuit.md
│       └── english-only-project.md
└── prompts/
    ├── issue-to-jules-task.md
    └── daily-maintainer-report.md
```

---

## Getting Started

### 1. Copy the Starter Kit

Copy the following folders and files directly into your own repository to get started:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
examples/
docs/workflows/
prompts/
```

### 2. Connect Jules

Use Jules to connect the GitHub repository and confirm that Jules can access the target repo.

### 3. Start with One Small Issue

Good issue:

```text
Add a PR template that requires linked issue, validation steps, and reviewer checklist.
```

Bad issue:

```text
Improve the project.
```

### 4. Ask Jules for a Focused PR

Use the issue as the source of truth. A Jules prompt should convert the issue into a reviewable PR, not replace the issue.

### 5. Review Before Merge

Before merging, check:

- Does the PR solve the linked issue?
- Is the scope controlled?
- Are unrelated files changed?
- Are tests or validation steps included?
- Does CI pass?
- Is the implementation maintainable?
- Would another developer understand this history later?

---

## Case Studies

### [Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)

Repository: <https://github.com/hkimw-underground/digital-logic-circuit>

This is a real hardware/software capstone case study. It shows how planning and implementation can move from an external project tracker into GitHub Issues, PRs, human review, and Jules-assisted implementation.

The maintainer owns architecture, hardware constraints, scope, review, and final merge decisions.

### [Case Study B: English-Only Open Source Project](./docs/case-studies/english-only-project.md)

Status: planned.

This will be a clean English-only project for a global audience. It should demonstrate small issues, focused Jules PRs, CI-first development, and readable review comments outside a school/capstone context.

---

## Safety Position

This repository supports automation, but it does not treat automation as the default goal.

Stable guidance:

```text
Human decides direction.
Human owns architecture.
Human reviews final changes.
CI gates every merge.
Jules is never presented as a human contributor.
```

Experimental guidance:

```text
No-human workflows must run in sandbox repos or protected branches.
Auto-merge requires strict CI and branch protection.
Evaluator-driven evolution must use measurable tests or benchmarks.
```

---

## Core Message

Most AI coding demos show only the final code.

This project shows the process:

```text
Issue.
Prompt.
Plan.
Pull request.
Review.
CI.
History.
```

That is where real AI-assisted engineering happens.

---

## License

This project is licensed under the [MIT License](./LICENSE).
