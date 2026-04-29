# Vibe Coding with Jules

[English](./README.md) · [한국어](./README.ko.md)

> Most AI coding demos show only the final code.  
> This project shows the process.

**Vibe Coding with Jules** is a GitHub-native workflow kit for using **Jules**, an AI coding agent, in real software projects.

This is not a prompt dump.

It is a practical template repository for running AI-assisted development through:

- GitHub Issues
- scoped implementation tasks
- pull requests
- human review
- CI checks
- documented case studies

The goal is simple:

> Treat AI coding work like maintainable open-source engineering — not magic, not vibes-only, and not hidden behind a final demo.

---

## Overview

AI coding agents are most useful when they are given clear boundaries.

This repository provides a reusable structure for maintainers who want to guide Jules through a disciplined development workflow.

Instead of asking an AI agent to “build the project,” this workflow encourages maintainers to:

1. Define the problem in a GitHub Issue.
2. Scope the work into a small implementation task.
3. Let Jules produce a focused pull request.
4. Review the PR as a human maintainer.
5. Use CI to catch regressions.
6. Document what changed and why.

The repository is designed to be copied, adapted, and reused in other GitHub projects.

---

## Why

Most AI coding examples are presented as polished before-and-after demos.

That hides the most important part of real engineering:

- How was the task specified?
- What constraints were given?
- How was the AI agent reviewed?
- What did CI catch?
- What did the human maintainer reject or adjust?
- How did the project history stay understandable?

This project exists because the process matters.

A good AI-assisted workflow should leave behind a GitHub history that another developer can understand.

---

## Workflow

The recommended workflow is:

```text
Human Maintainer
      ↓
GitHub Issue
      ↓
Jules Task Prompt
      ↓
Implementation Branch
      ↓
Pull Request
      ↓
Human Review
      ↓
CI / Tests
      ↓
Merge or Request Changes
```

### 1. Start with an Issue

Every meaningful task should begin with a GitHub Issue.

A good issue should include:

- problem statement
- expected behavior
- constraints
- non-goals
- acceptance criteria
- testing expectations

Jules should not be asked to guess the product direction.

The human maintainer owns the intent.

---

### 2. Convert the Issue into a Jules Task

The Jules prompt should be specific, scoped, and reviewable.

A good Jules task usually includes:

- repository context
- target files or modules
- exact implementation goal
- constraints
- test command
- expected PR summary
- what not to touch

The goal is not to make Jules “creative.”

The goal is to make Jules useful.

---

### 3. Keep Pull Requests Small

Small PRs make AI-generated changes easier to review.

Recommended PR size:

- one issue
- one responsibility
- one reviewable change
- tests included when possible

Avoid large “AI refactor everything” pull requests.

---

### 4. Review Jules Like a Coding Agent

Jules is an AI coding agent, not a human teammate.

That means:

- do not pretend Jules made architectural decisions independently
- do not merge without human review
- do not accept unclear code just because it works
- do not let generated changes bypass project standards

The human maintainer is responsible for correctness, architecture, and maintainability.

---

### 5. Let CI Be the Gate

CI should verify the boring but important parts:

- formatting
- linting
- tests
- type checks
- build checks
- documentation checks, when applicable

A clean CI pipeline makes AI-assisted development safer and more repeatable.

---

## What’s Included

This repository is intended to provide a complete starter kit for GitHub-native Jules workflows.

Planned structure:

```text
.
├── README.md
├── README.ko.md
├── AGENTS.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   ├── jules_task.yml
│   │   └── documentation_task.yml
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml
│       └── markdown-check.yml
├── docs/
│   ├── workflow.md
│   ├── review-guide.md
│   ├── prompt-patterns.md
│   ├── anti-patterns.md
│   └── case-studies/
│       ├── digital-logic-circuit.md
│       └── english-only-project.md
├── prompts/
│   ├── issue-to-jules-task.md
│   ├── implementation-task.md
│   ├── refactor-task.md
│   ├── review-fix-task.md
│   └── ci-failure-investigation.md
└── examples/
    ├── good-issues/
    ├── good-prs/
    └── review-comments/
```

---

## Case Studies

This project documents real examples of Jules-based development workflows.

### Case Study A: Digital Logic Circuit

Repository:  
<https://github.com/hkimw-underground/digital-logic-circuit>

This is a real capstone project used as a case study for moving project planning and implementation work into a GitHub Issue / PR based workflow.

The focus is not only on the final code.

The case study highlights:

- issue-driven planning
- hardware/software constraints
- Jules implementation tasks
- human maintainer review
- project history as documentation

In this workflow, Jules is used as an AI coding agent.

The human maintainer remains responsible for architecture, hardware decisions, and final review.

---

### Case Study B: English-Only Open Source Project

Status: planned.

This case study will be a clean, English-only open-source project designed for a global audience.

It will demonstrate:

- small issues
- focused Jules tasks
- clean PR descriptions
- CI-first development
- readable review comments
- contributor-friendly documentation

The goal is to show how the same workflow can be reused outside of a school or capstone context.

---

## Templates

This repository includes templates for common AI-assisted development workflows.

### Issue Templates

The issue templates help maintainers write tasks that are clear enough for both humans and AI coding agents.

Examples:

- bug report
- feature request
- Jules task
- documentation task
- refactor task

Each issue should answer:

```text
What problem are we solving?
What should change?
What should not change?
How do we verify the result?
```

---

### Pull Request Template

The PR template is designed to make AI-generated changes easier to review.

A good PR should include:

- linked issue
- summary of changes
- test results
- screenshots or logs when useful
- known limitations
- reviewer checklist

The PR should explain the change, not just contain the change.

---

### Jules Task Prompts

Prompt templates are included for repeatable task handoff.

Example prompt categories:

- implement from issue
- fix review comments
- add tests
- refactor safely
- update documentation
- investigate CI failure

These prompts are not meant to replace engineering judgment.

They are meant to make task delegation more consistent.

---

## Philosophy

This project is built around a few principles.

### Human Maintainer Leads

The maintainer owns:

- product direction
- architecture
- scope
- tradeoffs
- final review

Jules can implement, modify, and assist.

Jules should not silently define the project.

---

### AI Work Should Be Reviewable

AI-generated code should leave behind a clear trail:

```text
Issue → Task Prompt → PR → Review → CI → Merge
```

If the history is hard to understand, the workflow failed.

---

### Small PRs Beat Big Magic

Large AI-generated pull requests are difficult to review.

This workflow prefers:

- small changes
- clear acceptance criteria
- testable outputs
- reviewable commits

The goal is maintainability, not spectacle.

---

### CI Is Part of the Workflow

CI is not optional decoration.

It is the safety layer that keeps AI-assisted changes from becoming unreviewed guesses.

---

### Do Not Pretend the AI Is Human

Jules is an AI coding agent.

This repository avoids language that presents Jules as a human contributor.

The intended message is:

> A human maintainer can lead an AI coding agent through GitHub-native engineering practices.

Not:

> AI built the whole project by itself.

---

## Getting Started

### 1. Copy This Repository Structure

Use this repository as a starter kit for your own project.

You can copy:

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE`
- `.github/pull_request_template.md`
- `.github/workflows`
- `docs/`
- `prompts/`

---

### 2. Create a First Issue

Start with a small, concrete task.

Good first examples:

- add a missing test
- improve README setup instructions
- fix one bug
- add one small feature
- refactor one module

Avoid starting with a vague issue like:

```text
Make this project better.
```

Prefer:

```text
Add a CI workflow that runs tests on every pull request.
```

---

### 3. Write a Jules Task Prompt

Use the issue as the source of truth.

A good task prompt should include:

```text
Repository context:
Task:
Files to inspect:
Constraints:
Acceptance criteria:
Test command:
Expected PR description:
Do not touch:
```

---

### 4. Review the Pull Request

Before merging, check:

- Does the PR solve the issue?
- Is the scope controlled?
- Are unrelated files changed?
- Are tests included or updated?
- Does CI pass?
- Is the implementation maintainable?
- Would another developer understand this history later?

---

### 5. Document the Result

After the PR is merged, the issue and PR history should explain the development process.

That history is part of the project.

For AI-assisted development, the process is the portfolio.

---

## Who This Is For

This repository is for:

- open-source maintainers experimenting with AI coding agents
- students using GitHub for capstone projects
- developers who want cleaner AI-assisted workflows
- teams that want repeatable prompt-to-PR practices
- anyone who wants AI coding work to be reviewable

---

## Project Status

This repository is currently being built as a reusable workflow template and public playbook.

The initial focus is documentation, templates, and case studies.

---

## License

Choose a license that matches your intended reuse policy.

Recommended for this type of repository:

- MIT License for broad reuse
- Apache-2.0 if you want explicit patent language
- CC BY 4.0 for documentation-heavy reuse

---

## Core Message

Most AI coding demos show only the final code.

This project shows the process:

```text
Issue.
Prompt.
Pull request.
Review.
CI.
History.
```

That is where real AI-assisted engineering happens.
