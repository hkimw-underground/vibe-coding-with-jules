# Public Launch Checklist

This checklist is used by maintainers to verify that the repository is ready for public sharing or a tagged release. It focuses on practical readiness, consistency, and professional presentation.

## 1. First Impressions & Presentation

- [ ] **README First-Screen Review**: The top of the README clearly states the project purpose and provides immediate value.
- [ ] **Repository Description**: The GitHub repository description is concise and accurate.
- [ ] **Repository Topics**: Relevant topics (e.g., `ai`, `workflow`, `github-actions`, `jules`) are set to improve discoverability.
- [ ] **No Promotional Language**: Documentation uses practical, non-promotional language and avoids external ranking language.
- [ ] **Jules Identity**: All documentation correctly refers to Jules as an AI coding agent, never as a human contributor.

## 2. Content & Navigation

- [ ] **Relative Links**: All internal links use relative paths and are verified to work.
- [ ] **Document Tree Consistency**: The `Repository Structure` in the README matches the actual file tree.
- [ ] **Quickstart Discoverability**: The [Quickstart Guide](../quickstart.md) is easy to find from the README.
- [ ] **Examples Discoverability**: [Reference Examples](../../examples/) are clearly linked and accessible.
- [ ] **Case Study Clarity**: Status for [Case Study A](../case-studies/digital-logic-circuit.md) (complete) and [Case Study B](../case-studies/english-only-project.md) (actionable plan) is clearly stated.

## 3. Workflow & Safety

- [ ] **CI Status**: The `Validate docs and templates` workflow is passing on the `main` branch.
- [ ] **Branch Protection**: `main` branch has protection rules enabled, including PR-based changes and passing CI before merge.
- [ ] **Issue Templates**: [Jules Task](../../.github/ISSUE_TEMPLATE/jules_task.yml) and [Workflow Experiment](../../.github/ISSUE_TEMPLATE/workflow_experiment.yml) templates are present and functional.
- [ ] **PR Template**: The [Pull Request Template](../../.github/PULL_REQUEST_TEMPLATE.md) is present and includes validation checklists.

## 4. Maintenance & Operations

- [ ] **One Jules Task at a Time**: The [sequencing guide](../operations/one-jules-task-at-a-time.md) is present to prevent merge conflicts.
- [ ] **No Stale PRs**: All duplicate or stale PRs are closed with clear maintainer comments.
- [ ] **Clean History**: Recent commit history reflects the intended workflow: Issue → PR → Review → Merge.

## 5. Community & Legal

- [ ] **Community Files**: `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `SECURITY.md` are present in the root.
- [ ] **License**: `LICENSE` file (MIT) is present and correctly configured.
- [ ] **Agent Instructions**: `AGENTS.md` is present to guide AI agents, including Jules, working on the repo.
