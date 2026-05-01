# Labels and Triage Guide

This guide explains a reusable label and triage model for maintainers organizing AI-assisted work in GitHub. It helps maintain a clean, organized queue of issues and pull requests, especially when using an explicit trigger like `run-jules`.

## Recommended Label Categories

To organize issues and pull requests, we recommend the following simple label taxonomy:

- `jules`: Indicates an issue or PR that is assigned to or handled by Jules. This is an informational label.
- `run-jules`: An explicit trigger label used to signal automation to start working on an issue.
- `workflow`: Used for issues discussing or documenting the Jules workflow itself.
- `documentation`: Applied to tasks focused on updating or writing documentation.
- `case-study`: Used for issues tracking the creation or progress of case studies.

You can also use optional standard labels for priority or status (e.g., `bug`, `enhancement`, `help wanted`) without overcomplicating the repository.

## Using `run-jules` as an Explicit Trigger

The `run-jules` label acts as an explicit start button for automation.

- **Adding the label:** A maintainer adds `run-jules` when an issue is scoped, reviewed, and ready for the AI agent to begin work.
- **Removing the label:** Automation (or the maintainer) should remove the label once the agent has acknowledged the task or created the PR, indicating the run has started or finished.
- **Re-adding the label:** If the PR needs significant revision or if a new iteration is required based on PR review comments, the maintainer can re-add `run-jules` to trigger another run.

### Avoiding Concurrent Duplicate Runs

It is critical to avoid accidentally triggering concurrent duplicate Jules runs on the same issue.

- **Wait for acknowledgment:** Do not add the `run-jules` label multiple times in quick succession. Wait for the agent to create a PR or comment on the issue.
- **One task at a time:** Follow the [One Jules Task At A Time](./one-jules-task-at-a-time.md) principle to prevent merge conflicts and state confusion.
- **Clear state:** Ensure the `run-jules` label is removed before triggering a new run for revisions.

## Suggested Triage Flow

This is the standard GitHub-native flow from a new issue to a merged PR:

1. **New Issue Opened:** A maintainer or contributor creates an issue. It may have standard categorizing labels (like `documentation` or `bug`).
2. **Review & Scope:** The maintainer reviews the issue to ensure it is small, focused, and appropriate for Jules.
3. **Trigger:** The maintainer assigns the `jules` label for tracking and adds the `run-jules` label to initiate the task.
4. **Agent Action:** The automation detects `run-jules`, removes the label, and begins work.
5. **PR Creation:** Jules opens a Pull Request linked to the issue.
6. **Human Review:** The maintainer reviews the PR.
   - If approved: Merge.
   - If changes are needed: Leave review comments. If the agent needs to completely re-plan, the maintainer may re-add `run-jules`.
7. **Merge & Close:** Once the PR passes CI and human review, it is merged, and the issue is closed.

This process keeps the default workflow **human-led**, ensuring that maintainers always own the architecture, direction, and final merge decisions.
