# Labels and Triage Guide

This guide explains how to organize AI-assisted work using GitHub labels and a structured triage flow. A consistent labeling model helps maintainers track Jules's progress, manage experiments, and ensure a clean engineering history.

## Recommended Label Categories

| Category | Labels | Description |
| --- | --- | --- |
| **Core Tasks** | `jules`, `task` | Standard coding tasks for Jules to implement. |
| **Experiments** | `experiment`, `workflow` | Testing advanced or non-default Jules workflows. |
| **Content** | `documentation`, `example` | Updates to guides, READMEs, or reusable examples. |
| **Tracking** | `case-study` | Issues related to specific case studies. |
| **Triggers** | `run-jules` | The explicit signal to trigger a Jules run. |

## Labels for Jules Tasks

Use `jules` and `task` for standard issues where you want Jules to provide a focused Pull Request. These usually follow the `jules_task.yml` template.

- `jules`: Identifies the issue as intended for the AI coding agent.
- `task`: Indicates a concrete unit of work with defined acceptance criteria.

## Labels for Workflow Experiments

Use `experiment` and `workflow` for tasks that test new ways of working with Jules (e.g., Level 5 or Level 6 workflows). These usually follow the `workflow_experiment.yml` template.

- `experiment`: Signals that the result may be non-deterministic or requires a sandbox.
- `workflow`: Focuses on the process itself rather than a specific feature.

## Labels for Documentation and Examples

Use `documentation` and `example` to distinguish content-heavy tasks from code-heavy ones.

- `documentation`: For core guides, README updates, or API docs.
- `example`: For adding or refining files in the `examples/` directory.

## Labels for Case Studies

Use `case-study` to group issues that belong to a specific narrative or real-world application, such as the Digital Logic Circuit or the English-Only Project.

## The `run-jules` Trigger

The `run-jules` label is the primary mechanism for controlling when Jules starts working on an issue.

1. **Explicit Trigger:** Jules should only start when the `run-jules` label is added to an issue.
2. **Remove After Start:** Once Jules has picked up the task and opened a PR, the maintainer (or an automated script, if configured) should remove the label.
3. **Re-triggering:** If a Jules run fails or produces an unsatisfactory PR, close the PR, address any issues in the issue description, and re-add `run-jules` to start a fresh attempt.

## Avoiding Concurrent Duplicate Runs

To maintain a clean history and avoid merge conflicts, follow the principle of **one Jules task at a time** on shared files.

- Do not add `run-jules` to multiple issues that modify the same files (e.g., `README.md`).
- Wait for the previous Jules PR to be merged before triggering the next related task.
- For more details, see [One Jules Task at a Time](./one-jules-task-at-a-time.md).

## Suggested Triage Flow

A structured flow ensures that human maintainers remain in control of the project direction.

1. **New Issue:** A human creates an issue (using a template).
2. **Triage:** A human reviews the issue, adds category labels (`jules`, `task`, `documentation`), and ensures the scope is clear.
3. **Trigger:** A human adds `run-jules` when ready for implementation.
4. **Implementation:** Jules creates a branch and opens a Pull Request.
5. **Review:** A human reviews the PR, provides feedback, or requests changes.
6. **Merge:** A human merges the PR once it meets all acceptance criteria and passes CI.

## Optional Labels

Maintainers may add additional labels without overcomplicating the workflow:
- **Priority:** `p0` (urgent), `p1` (standard), `p2` (backlog).
- **Status:** `blocked` (waiting on human decision), `in-progress` (Jules is working).

## Summary

Labels in this starter kit are not just for organization—they are control signals. By using `run-jules` as an explicit trigger and following a human-led triage flow, you ensure that Jules remains a productive, managed contributor to your project.
