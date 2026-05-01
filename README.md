# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md) · [Quickstart](./docs/quickstart.md) · [Showcase](./docs/showcase.md) · [Project Readiness](./docs/meta/project-readiness.md) · [Launch Checklist](./docs/meta/release-checklist.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)

> Most AI coding demos show only the final code.  
> This project shows the process.

**AI Coding Workflow Starter Kit for Jules** is a GitHub-native playbook for working with Jules through issues, pull requests, reviews, CI, case studies, and controlled workflow experiments.

It is built for students, teachers, first-time maintainers, and small teams who want AI-assisted coding work to leave a readable engineering history.

![Workflow overview](./docs/assets/workflow-overview.svg)

This is not a prompt dump. It is a reusable starter kit for running AI-assisted work inside normal GitHub practice.

---

## Choose Your Track

Pick the workflow that matches how much human involvement you want.

![Four workflow tracks](./docs/assets/four-tracks-overview.svg)

| Track | Best for | Human involvement | Status |
| --- | --- | --- | --- |
| **[Review-Driven](./docs/tracks/review-driven.md)** | Real projects, classrooms, starter repos | Medium | **Recommended default** |
| **[GitHub-Native Collaboration](./docs/tracks/github-native-collaboration.md)** | Learning Issues, PRs, reviews, CI, labels, and branch protection | Medium | Recommended for learning |
| **[Half Vibe Coding](./docs/tracks/half-vibe-coding.md)** | Direction from a maintainer, execution by Jules between checkpoints | Low | Advanced |
| **[Full Vibe Coding](./docs/tracks/full-vibe-coding.md)** | Sandbox experiments and workflow research | Minimal | Experimental only |

Recommended path for most readers:

```text
Start with Review-Driven.
Use GitHub-Native Collaboration when teaching or learning teamwork.
Try Half Vibe Coding only after CI and review rules are in place.
Keep Full Vibe Coding in sandbox repositories or protected branches.
```

---

## Start Here

![Getting started flow](./docs/assets/getting-started-flow.svg)

1. Read the **[Quickstart Guide](./docs/quickstart.md)**.
2. See the **[copy-first showcase](./docs/showcase.md)**.
3. Copy the starter files into your repository.
4. Open a small GitHub Issue.
5. Let Jules create a focused pull request.
6. Review the PR, check CI, and merge only when the maintainer is satisfied.

Starter files to copy first:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/docs-and-templates.yml
prompts/
examples/
```

---

## Default Workflow

The default workflow is **Review-Driven**:

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

The maintainer stays responsible for scope, architecture, validation, and the final merge decision. Jules assists with implementation and documentation work through the GitHub workflow.

---

## What This Repo Includes

- **AGENTS.md** — repository rules for Jules-assisted work
- **Issue templates** — scoped task and workflow experiment templates
- **PR template** — linked issue, validation, and review expectations
- **CI example** — lightweight checks for docs and starter kit structure
- **Prompts** — issue handoff and maintainer report prompts
- **Examples** — reusable issue and PR review examples
- **Operations guides** — one-task-at-a-time, branch protection, labels, and triage
- **Workflow tracks** — four ways to work with Jules, from review-driven to sandbox experiments
- **Case studies** — one real applied case study and one planned English-only case study

---

## Key Guides

- [Quickstart](./docs/quickstart.md)
- [Showcase](./docs/showcase.md)
- [Jules Web UI Guide](./docs/jules-web-ui.md)
- [First Contributions Guide](./docs/contributing/first-contributions.md)
- [Translation Guide](./docs/contributing/translations.md)
- [Public Share Kit](./docs/share-kit.md)
- [One Jules Task at a Time](./docs/operations/one-jules-task-at-a-time.md)
- [Branch Protection and CI Gates](./docs/operations/branch-protection-and-ci-gates.md)
- [Labels and Triage](./docs/operations/labels-and-triage.md)
- [Project Readiness](./docs/meta/project-readiness.md)
- [Documentation Audit](./docs/meta/documentation-audit.md)

---

## Case Studies

- **[Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)** — a real hardware/software capstone project using the Jules workflow.
- **[Case Study B: English-Only Project Brief](./docs/case-studies/english-only-project.md)** — a planned small open-source project for showing the same workflow to a global audience.

---

## Safety and Ownership

Stable guidance:

```text
Human decides direction.
Human owns architecture.
Human reviews final changes.
CI gates every merge.
Jules is an AI coding agent, not a human contributor.
```

Experimental guidance:

```text
Autonomous workflows belong in sandbox repos or protected branches.
Auto-merge experiments require strict CI and branch protection.
Evaluator-driven experiments need measurable tests or benchmarks.
```

---

## Repository Structure

```text
.
├── AGENTS.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
├── docs/
│   ├── assets/
│   ├── contributing/
│   │   ├── first-contributions.md
│   │   └── translations.md
│   ├── jules-web-ui.md
│   ├── quickstart.md
│   ├── showcase.md
│   ├── share-kit.md
│   ├── case-studies/
│   ├── experiments/
│   ├── meta/
│   ├── operations/
│   ├── tracks/
│   └── workflows/
├── examples/
│   ├── issues/
│   └── pr-reviews/
└── prompts/
```

---

## License

This project is licensed under the [MIT License](./LICENSE).
