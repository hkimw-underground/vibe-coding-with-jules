# Case Study A: Digital Logic Circuit

## Repository Overview

Repository: `hkimw-underground/digital-logic-circuit`

The `digital-logic-circuit` repository is a real-world hardware and software capstone project. It serves as a case study for integrating an AI coding agent, Jules, into a standard GitHub development workflow.

For a step-by-step guide on how to integrate this workflow into your own project, see the [Applied Repository Rollout](../operations/apply-to-existing-repo.md) guide. Lessons learned from rolling out the workflow in this case study are fed back into the starter kit to improve that guide.

## Why This is a Good Case Study

Unlike simple, isolated software experiments, a capstone project involves external constraints, complex architectures, and concrete milestones. Demonstrating the workflow here shows how the GitHub-native Issue → PR → Review → CI process can work for a structured project while keeping engineering review visible.

## Project Planning and GitHub Issues

Historically, project planning for this capstone might have relied on external trackers or ad-hoc communication. To enable the AI-assisted workflow, planning has been explicitly moved into GitHub Issues.

1. **Issue Creation**: The human maintainer translates high-level project goals into small, scoped GitHub Issues.
2. **Context**: Each issue acts as the source of truth, describing the problem, scope, constraints, and validation steps.

## Workflow Execution: Issue → Jules → PR → Review → CI

This case study describes a clear, linear workflow:

1. **Issue**: The human maintainer opens a scoped GitHub Issue.
2. **Jules**: Jules, acting as an AI coding agent, reads the issue and implements the necessary changes.
3. **PR**: Jules creates a small, focused Pull Request linking back to the issue.
4. **Review**: The human maintainer reviews the PR against the issue requirements and architecture guidelines.
5. **CI**: Automated Continuous Integration checks run against the proposed changes to validate correctness.

## Separation of Responsibilities

A key tenet of this workflow is the strict boundary between human and AI responsibilities. Jules is an AI coding agent, not a human contributor or a substitute for engineering judgment.

### Human Maintainer Responsibilities

- Define project architecture and hardware constraints.
- Scope and create GitHub Issues.
- Review Pull Requests submitted by Jules.
- Make the final merge decisions.
- Ensure the project direction aligns with external capstone requirements.

### Jules Responsibilities

- Read and understand the assigned GitHub Issue.
- Implement the requested code or documentation changes.
- Ensure changes are small, focused, and strictly scoped to the issue.
- Open a Pull Request for human review.
- Explain assumptions in the PR description if an issue is ambiguous.

## CI and Validation Expectations

Continuous Integration is critical. For the `digital-logic-circuit` repository, CI should cover:

- Syntax and compilation checks for any software components.
- Automated tests or simulations for logic circuits.
- Formatting and linting rules to maintain codebase consistency.
- Any repository-specific validation steps defined by the maintainer.

## Lessons for Other Maintainers

This case study demonstrates that:

- AI agents work best when bound by traditional engineering workflows, especially Issues and PRs.
- Keeping PRs small and strictly scoped to a single issue makes human review manageable.
- Human ownership of architecture and final review is non-negotiable for real projects.
- Explicit CI gates help keep the main branch reviewable and maintainable.
