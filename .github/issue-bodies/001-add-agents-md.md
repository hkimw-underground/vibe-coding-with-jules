## Goal

Add a repository-level `AGENTS.md` file that defines how Jules should operate in this project.

This repository is a GitHub-native workflow kit for using Jules as an AI coding agent. The `AGENTS.md` file should make the operating rules clear for future AI-assisted tasks.

## Scope

Create:

- `AGENTS.md`

The document should explain:

- Jules is an AI coding agent, not a human contributor.
- Work should start from a GitHub Issue.
- Pull requests should be small and scoped.
- Jules should avoid unrelated refactors.
- Jules should include clear PR summaries.
- Tests or validation steps should be included when applicable.
- Human maintainer review is required before merge.
- CI failures should be investigated, not ignored.

## Non-goals

Do not modify:

- `README.md`
- `README.ko.md`
- GitHub issue templates
- CI workflows
- prompt templates

Those will be handled in separate issues.

## Acceptance Criteria

- `AGENTS.md` exists at the repository root.
- The document is written in English.
- The tone is practical and maintainer-oriented.
- The document clearly states that Jules is an AI coding agent.
- The document encourages issue-driven, PR-based, CI-checked development.
- The document avoids exaggerated AI marketing language.
