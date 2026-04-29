# Vibe Coding with Jules

[English](./README.md) · [한국어](./README.ko.md)

> Most AI coding demos show only the final code.  
> This project shows the process.

**Vibe Coding with Jules** is a GitHub-native workflow kit for using **Jules**, an AI coding agent, through real Issue → PR → Review → CI workflows.

This is not a prompt dump.

This repository is designed to show how a human maintainer can lead an AI coding agent using the same primitives that already make open-source collaboration work:

- GitHub Issues
- GitHub Actions
- scoped AI coding tasks
- pull requests
- human code review
- CI checks
- documented case studies

Repository:  
<https://github.com/hkimw-underground/vibe-coding-with-jules>

---

## Overview

Most AI coding workflows still happen outside the development history.

A prompt is written somewhere.
An AI tool generates code.
The final result is committed.
The process disappears.

This repository takes a different approach.

The intended workflow is:

```text
Human Maintainer opens a GitHub Issue
        ↓
GitHub Actions triggers Jules
        ↓
Jules creates a focused pull request
        ↓
Human Maintainer reviews the PR
        ↓
CI validates the change
        ↓
Maintainer merges or requests changes
```

Jules is used as an **AI coding agent**, not as a hidden replacement for maintainership.

The human maintainer owns the scope, architecture, review, and final merge decision.

---

## Why

Most AI coding demos show a polished before-and-after result.

That hides the most important engineering questions:

- What issue was the AI agent asked to solve?
- What constraints were given?
- What files were in scope?
- What did the human maintainer review?
- What did CI verify?
- What changed between the first PR and the final merge?
- Can another developer understand the history later?

This project exists because the process matters.

A good AI-assisted workflow should leave behind a GitHub history that is readable, reviewable, and reusable.

---

## Workflow

This repository is built around **IssueOps for Jules**.

Instead of manually visiting the Jules web UI for every task, the preferred workflow is:

```text
1. Write a scoped GitHub Issue.
2. Add an explicit trigger label, such as `run-jules`.
3. GitHub Actions builds a Jules task from the Issue.
4. Jules works on the repository and opens a PR.
5. The maintainer reviews the PR like any other contribution.
6. CI must pass before merge.
```

### Recommended IssueOps Flow

```text
Issue
  ↓
Label: run-jules
  ↓
GitHub Actions
  ↓
Jules Session
  ↓
Pull Request
  ↓
Human Review
  ↓
CI
  ↓
Merge
```

This keeps the project history inside GitHub.

The Jules web interface may still be used for initial setup, account connection, and API key management. After that, the goal is to operate primarily from GitHub Issues, PRs, reviews, and Actions.

---

## What’s Included

Planned repository structure:

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
│   ├── workflows/
│   │   ├── jules-issueops.yml
│   │   ├── ci.yml
│   │   └── markdown-check.yml
│   └── pull_request_template.md
├── docs/
│   ├── workflow.md
│   ├── issueops.md
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
    ├── issues/
    ├── prs/
    └── reviews/
```

---

## Case Studies

This repository will document real Jules-based workflows.

### Case Study A: Digital Logic Circuit

Repository:  
<https://github.com/hkimw-underground/digital-logic-circuit>

This is a real capstone project used as a case study for moving project planning and implementation work into a GitHub Issue / PR based workflow.

The focus is not only the final code.

The case study will show:

- issue-driven planning
- hardware/software constraints
- Jules implementation tasks
- human maintainer review
- CI and validation expectations
- project history as documentation

In this workflow, Jules is an AI coding agent. The human maintainer remains responsible for architecture, hardware decisions, scope control, and final review.

---

### Case Study B: English-Only Open Source Project

Status: planned.

This case study will be a clean English-only open-source project designed for a global audience.

It will demonstrate:

- small issues
- automated Jules task triggering
- focused pull requests
- clean PR descriptions
- CI-first development
- readable review comments
- contributor-friendly documentation

The goal is to show that the same workflow can be reused outside a school or capstone context.

---

## Templates

This repository provides templates for repeatable AI-assisted development.

### Issue Templates

Issue templates help maintainers define work clearly before an AI coding agent starts.

A good issue should answer:

```text
What problem are we solving?
What should change?
What should not change?
How do we verify the result?
```

### Pull Request Template

The PR template is designed to make AI-generated changes easier to review.

A good PR should include:

- linked issue
- summary of changes
- validation steps
- screenshots or logs when useful
- known limitations
- reviewer checklist

The PR should explain the change, not just contain the change.

### Jules Task Prompts

Prompt templates are included for repeatable task handoff.

Example categories:

- implement from issue
- fix review comments
- add tests
- refactor safely
- update documentation
- investigate CI failure

The issue remains the source of truth.

Prompts should help convert a scoped issue into a reviewable PR. They should not replace engineering judgment.

---

## Philosophy

### Human Maintainer Leads

The maintainer owns:

- product direction
- architecture
- scope
- tradeoffs
- final review
- merge decisions

Jules can implement, modify, and assist.

Jules should not silently define the project.

### AI Work Should Be Reviewable

AI-generated code should leave behind a clear trail:

```text
Issue → Action Run → PR → Review → CI → Merge
```

If the history is hard to understand, the workflow failed.

### Small PRs Beat Big Magic

Large AI-generated pull requests are difficult to review.

This workflow prefers:

- small changes
- clear acceptance criteria
- testable outputs
- reviewable diffs

The goal is maintainability, not spectacle.

### CI Is Part of the Workflow

CI is not optional decoration.

It is the safety layer that keeps AI-assisted changes from becoming unreviewed guesses.

### Do Not Pretend the AI Is Human

Jules is an AI coding agent.

This repository avoids language that presents Jules as a human contributor.

The intended message is:

> A human maintainer can lead an AI coding agent through GitHub-native engineering practices.

Not:

> AI built the whole project by itself.

---

## Getting Started

### 1. Use the Repository as a Starter Kit

Copy the parts you need:

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE`
- `.github/workflows/jules-issueops.yml`
- `.github/pull_request_template.md`
- `docs/`
- `prompts/`

### 2. Connect Jules Once

Initial setup may require the Jules web app to connect the GitHub repository and generate an API key.

After setup, the intended workflow should happen mainly through GitHub Issues, Actions, PRs, and Reviews.

### 3. Add the Jules API Key to GitHub Secrets

Store the API key as a repository secret:

```text
JULES_API_KEY
```

Do not commit API keys to the repository.

### 4. Create a Scoped Issue

Start with a small, concrete task.

Good examples:

```text
Add AGENTS.md for Jules workflow rules.
Add markdown documentation CI.
Add a pull request template for AI-assisted contributions.
```

Avoid vague tasks such as:

```text
Make this project better.
```

### 5. Trigger Jules from GitHub

Add the trigger label:

```text
run-jules
```

GitHub Actions should then invoke Jules and ask it to create a focused PR for the issue.

### 6. Review Before Merge

Before merging, check:

- Does the PR solve the issue?
- Is the scope controlled?
- Are unrelated files changed?
- Are tests or validation steps included?
- Does CI pass?
- Is the implementation maintainable?
- Would another developer understand this history later?

---

## Who This Is For

This repository is for:

- open-source maintainers experimenting with AI coding agents
- developers who want GitHub-native AI workflows
- students running capstone projects through Issues and PRs
- teams that want repeatable IssueOps-based AI task delegation
- anyone who wants AI coding work to be reviewable

---

## Project Status

This repository is being built as a reusable workflow template and public playbook.

The initial focus is:

- README
- AGENTS.md
- GitHub Issue templates
- Jules IssueOps workflow
- PR template
- CI examples
- case study documentation

---

## License

Recommended options:

- MIT License for broad reuse
- Apache-2.0 if explicit patent language is preferred
- CC BY 4.0 for documentation-heavy reuse

---

## Core Message

Most AI coding demos show only the final code.

This project shows the process:

```text
Issue.
Action run.
Prompt.
Pull request.
Review.
CI.
History.
```

That is where real AI-assisted engineering happens.
