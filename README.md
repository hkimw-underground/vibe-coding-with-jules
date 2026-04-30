# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md) · [Contributing](./CONTRIBUTING.md) · [Code of Conduct](./CODE_OF_CONDUCT.md) · [Security](./SECURITY.md)

> Most AI coding demos show only the final code.  
> This project shows the process.

**AI Coding Workflow Starter Kit for Jules** is a GitHub-native playbook for leading an AI coding agent (**Jules**) through issues, pull requests, reviews, and CI. This is a reusable starter kit for maintainers who want AI-assisted work to leave a clean, professional engineering history.

---

## Why This Kit?

Most AI coding workflows are hidden in ephemeral chat logs. This kit brings that process into the light using standard GitHub practices.

- **Traceable History**: Every change is linked to an issue and validated via PR review.
- **Human-in-the-Loop**: The human maintainer leads the direction; Jules implements the details.
- **Reusable Templates**: Ready-to-use issue templates, PR formats, and handoff prompts.
- **Battle-Tested**: Documented levels of autonomy, from strict human-led to experimental loops.

The goal is simple: **A human maintainer leads an AI coding agent.** This is not about "AI building a project alone"—it's about AI-assisted engineering that scales.

---

## Core Workflow

A human maintainer leads the process using the standard GitHub flow:

```text
Issue → Jules Task → Pull Request → Human Review → CI → Merge
```

1. **Human** opens a scoped GitHub Issue.
2. **Jules** implements the task and opens a focused PR.
3. **CI** validates the change.
4. **Human** reviews the diff and merges.

---

## Repository Structure

```text
.
├── AGENTS.md            # Mandatory instructions for Jules
├── .github/             # GitHub Issue and PR templates
├── docs/                # Workflow levels and case studies
├── examples/            # Example issues and PR reviews
├── prompts/             # Standardized AI handoff prompts
├── README.md
└── README.ko.md
```

---

## Getting Started

### 1. Copy the Core Files
Add these files to your repository to start using the workflow:

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `prompts/`

### 2. Connect Jules
Ensure Jules has access to your repository and can read the `AGENTS.md` file.

### 3. Start with a Small Issue
Open a well-defined issue (e.g., "Add unit tests for the login module") and use the `jules_task.yml` template.

---

## Workflow Levels

We categorize workflows by the level of human involvement. Level 1 is the recommended default.

| Level | Workflow | Human role | Status |
| --- | --- | --- | --- |
| 1 | Human-led Jules workflow | Creates issue, reviews PR, merges | **Recommended** |
| 2 | Semi-autonomous Jules workflow | Creates issue, reviews final PR | Practical |
| 3 | Human issue only | Writes issue; Jules handles implementation | Advanced |
| 4 | Daily agentic maintainer loop | Steers direction from daily reports | Experimental |
| 5 | No-human sandbox workflow | Observes or audits only | Sandbox only |

---

## Case Studies

- **[Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)**: A real-world hardware/software project managed via Jules.
- **[Case Study B: English-Only Project](./docs/case-studies/english-only-project.md)**: A clean, open-source example for a global audience (Planned).

---

## Core Message

Most AI coding demos show only the final code. **This project shows the process:**

```text
Issue → Prompt → Plan → Pull Request → Review → CI → History
```

That is where real AI-assisted engineering happens.

---

## License

This project is licensed under the [MIT License](./LICENSE).
