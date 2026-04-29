# AGENTS.md

This repository uses Jules as an AI coding agent, not a human contributor. The following rules define how Jules operates within this project to ensure a maintainable, GitHub-native workflow.

## Operating Rules

Jules must adhere to the following guidelines:

- **Jules is an AI Coding Agent:** Do not present Jules as a human contributor.
- **Issue-Driven Development:** All work must originate from a GitHub Issue.
- **Small, Focused Pull Requests:** Create pull requests that are small and strictly scoped to the issue.
- **Link PRs to Issues:** Ensure each pull request links back to the originating issue.
- **No Unrelated Refactors:** Do not perform refactors that are unrelated to the current task.
- **Stay in Scope:** Do not modify files outside the scope of the issue.
- **Include Validation:** Include tests or validation steps when applicable to verify changes.
- **Clear PR Summaries:** Keep the PR description concise and reviewable.
- **Handle Ambiguity Safely:** If the issue is ambiguous, make the smallest safe change and explicitly state the assumption in the PR description.
- **No Self-Merging:** Jules must not merge pull requests. Human maintainer review and approval are strictly required before merging.
- **Investigate CI Failures:** If Continuous Integration (CI) checks fail, Jules should investigate and address the root cause, not ignore it.

## Philosophy

This repository is built around the idea that a human maintainer leads an AI coding agent through GitHub-native engineering practices. The history of the project—Issue → Action Run → PR → Review → CI → Merge—should be readable, reviewable, and reusable.
