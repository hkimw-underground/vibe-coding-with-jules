# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md) · [Project Readiness](./docs/meta/project-readiness.md) · [Launch Checklist](./docs/meta/release-checklist.md) · [Contributing](./CONTRIBUTING.md) · [Code of Conduct](./CODE_OF_CONDUCT.md) · [Security](./SECURITY.md)

> Most AI coding demos show only the final code.  
> This project shows the process.

**AI Coding Workflow Starter Kit for Jules** is a GitHub-native playbook for leading Jules—an AI coding agent—through a professional engineering process. It moves AI-assisted work out of "magic prompts" and into issues, pull requests, reviews, and CI.

---

## Choose Your Track

How do you want to work with Jules? Pick the track that fits your goals.

| Track | Goal | Recommended for | Level |
| --- | --- | --- | --- |
| **Review-Driven** | **Default.** High quality, clean history. | Everyone | 1 |
| **GitHub-Native Collaboration** | Learning the professional workflow. | Students & Teachers | 1 |
| **Half Vibe Coding** | Low-touch, fast iteration with CI gates. | Advanced users | 2-3 |
| **Full Vibe Coding** | **Experimental.** Autonomous sandboxing. | Researchers | 5-6 |

---

## Start Here

1. **[Quickstart Guide](./docs/quickstart.md)** — Step-by-step onboarding for your first Jules task.
2. **Copy the Starter Kit** — Add `AGENTS.md`, `.github/`, and `prompts/` to your repository.
3. **Open an Issue** — Define a small, scoped task for Jules to solve.
4. **Review & Merge** — Lead Jules through the PR and CI process.

---

## How the Default Workflow Works

The **Review-Driven** track is our recommended standard. It ensures that humans remain in control of the architecture while Jules handles the implementation.

1. **Issue**: A human maintainer defines a scoped task.
2. **Task**: Jules plans and implements the change.
3. **Pull Request**: Jules opens a PR linked to the issue.
4. **CI**: Automated checks validate the change.
5. **Review**: A human maintainer reviews the code and requests changes if needed.
6. **Merge**: The human maintainer makes the final decision to merge.

---

## What This Repo Includes

- **Scoped Issue Templates**: Pre-configured for Jules tasks and experiments.
- **PR Templates**: Standardized format with validation checklists.
- **Workflow Levels**: From human-led tasks to experimental autonomy.
- **Reference Examples**: Real-world issues and maintainer review examples.
- **CI Validation**: Lightweight checks for Markdown and YAML hygiene.
- **Reusable Prompts**: Templates for handoffs and status reporting.

---

## Case Studies

- **[Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)** — A hardware/software capstone project using the Jules workflow.
- **[Case Study B: md-link-linter](./docs/case-studies/english-only-project.md)** — (Planned) A minimalist Markdown link checker built with a CI-first approach.

---

## Safety & Ownership

- **Human-Led**: A human decides the direction and owns the architecture.
- **Jules as an Agent**: Jules is an AI coding agent, not a human contributor.
- **CI Gates**: Every merge should be gated by automated checks.
- **Sandbox for Experiments**: Full Vibe Coding must stay in sandbox environments.

---

## License

This project is licensed under the [MIT License](./LICENSE).
