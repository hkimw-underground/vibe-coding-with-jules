# Labels and Triage Guide

This guide explains a reusable label and triage model for maintainers organizing AI-assisted work in GitHub. It helps maintain a clean queue of issues and pull requests, especially when using an explicit trigger like `run-jules`.

## Recommended Label Categories

To organize issues and pull requests, use a small label taxonomy:

- `jules`: Indicates an issue or PR related to Jules-assisted work. This is an informational label.
- `run-jules`: An explicit trigger label used to signal that an issue is ready for a Jules run.
- `workflow`: Used for issues discussing or documenting the Jules workflow itself.
- `documentation`: Applied to tasks focused on updating or writing documentation.
- `case-study`: Used for issues tracking the creation or progress of case studies.

You can also use optional standard labels for priority or status, such as `bug`, `enhancement`, or `help wanted`, without overcomplicating the repository.

## Using `run-jules` as an Explicit Trigger

The `run-jules` label works like a start signal.

- **Adding the label:** A maintainer adds `run-jules` when an issue is scoped, reviewed, and ready for Jules to begin work.
- **Removing the label:** The label should be removed once the run has started or a PR has been opened.
- **Re-adding the label:** If the PR needs a new attempt, close or review the current PR first, update the issue with clearer instructions, and then re-add `run-jules`.

## Avoiding Concurrent Duplicate Runs

Avoid triggering multiple Jules runs for the same issue or for overlapping files.

- Do not add `run-jules` multiple times in quick succession.
- Wait for Jules to create a PR or comment on the issue before triggering another run.
- Follow the [One Jules Task At A Time](./one-jules-task-at-a-time.md) principle to prevent merge conflicts and duplicated work.
- Remove `run-jules` before starting a later revision.

## Suggested Triage Flow

This is the standard GitHub-native flow from a new issue to a merged PR:

1. **New Issue Opened:** A maintainer or contributor creates an issue. It may have standard labels like `documentation` or `bug`.
2. **Review and Scope:** The maintainer reviews the issue to ensure it is small, focused, and appropriate for Jules.
3. **Trigger:** The maintainer adds `jules` for tracking and `run-jules` when the task is ready.
4. **Jules Run:** Jules works on the task and opens a pull request.
5. **Human Review:** The maintainer reviews the PR.
   - If approved: merge.
   - If changes are needed: leave review comments or update the issue before another run.
6. **Merge and Close:** Once the PR passes CI and human review, merge it and close the issue.

This process keeps the default workflow **human-led**. The maintainer owns the architecture, direction, review, and final merge decision.
