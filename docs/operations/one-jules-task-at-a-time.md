# One Jules Task at a Time

While dogfooding this starter kit, we learned a practical operational lesson: **running multiple Jules tasks concurrently on shared files can create duplicate or stale Pull Requests.**

This guide explains how to sequence Jules tasks safely, especially when tasks touch shared documentation or workflow files, and how to manage duplicate PRs when they occur.

## Why One Task at a Time?

Jules, as an AI coding agent, creates a branch from the current state of the repository, makes changes based on the issue, and opens a Pull Request.

If you assign two tasks to Jules simultaneously, and both tasks require modifying a shared file such as `README.md` or `.github/workflows/docs-and-templates.yml`:

1. **Branch 1** modifies the shared file.
2. **Branch 2** modifies the same shared file based on the old state.
3. Both branches open PRs.
4. When PR 1 merges, PR 2 may face merge conflicts or need a fresh run from the updated `main` branch.

Running one Jules task at a time helps each new task branch from a `main` branch that includes all previous updates.

## When Are Concurrent Tasks Acceptable?

Concurrent Jules tasks are acceptable when the tasks modify **strictly disjoint** areas of the codebase. For example:

- Task A updates `docs/case-studies/digital-logic-circuit.md`.
- Task B adds a new feature in `src/utils/math.js`.

If you are confident the files will not overlap, you can run them simultaneously. If there is any risk of overlap, such as adding to a shared list of links in the README, queue the tasks.

## Managing Issue Labels

To sequence tasks effectively using labels like `run-jules`:

1. Add `run-jules` to the first issue.
2. Wait for Jules to open the PR.
3. Review and merge the PR.
4. Once `main` is updated, add `run-jules` to the next issue.

## Keeping `main` Current Between Tasks

Always wait for a PR to merge before triggering the next Jules task that might touch the same files. If you trigger a task on an outdated `main` and a PR is opened:

- Check whether the PR still applies cleanly.
- If the PR has conflicts or duplicates already-merged work, close it with a clear maintainer comment.
- Re-trigger the task from the updated `main` branch if the work is still needed.

## Handling Duplicate or Stale PRs

If you accidentally trigger multiple tasks and get duplicate PRs attempting to solve similar problems or modifying the same shared file:

1. Identify the PR that best solves the issue or is closest to mergeable.
2. Review and merge that PR.
3. Cleanly close the duplicate PRs.

### Suggested Maintainer Comments for Closing Duplicates

When closing a stale or duplicate PR created by Jules, leave a clear comment for the engineering history:

> **Closing as duplicate.** This change was addressed in #123. The underlying issue will be re-evaluated if needed.

> **Closing as stale.** Another PR updated the shared `README.md` and this branch is now out of date. I will re-trigger the task from the updated `main` branch if the work is still needed.

By keeping a clean history and sequencing tasks logically, maintainers can guide Jules effectively without creating unnecessary conflict resolution work.
