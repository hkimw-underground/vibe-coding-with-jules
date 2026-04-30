# One Jules Task at a Time

While dogfooding this starter kit, we learned a valuable operational lesson: **running multiple Jules tasks concurrently on shared files creates duplicate or stale Pull Requests.**

This guide explains how to sequence Jules tasks safely, especially when tasks touch shared documentation or workflow files, and how to manage duplicate PRs when they occur.

## Why One Task at a Time?

Jules, as an AI coding agent, creates a branch from the current state of the repository, makes changes based on the issue, and opens a Pull Request.

If you assign two tasks to Jules simultaneously, and both tasks require modifying a shared file (e.g., `README.md` or `.github/workflows/docs-and-templates.yml`):
1. **Branch 1** modifies the shared file.
2. **Branch 2** modifies the same shared file based on the old state.
3. Both branches open PRs.
4. When PR 1 merges, PR 2 may face merge conflicts or overwrite PR 1's changes if merged without a rebase.

Running one Jules task at a time ensures that each new task branches from a `main` branch that includes all previous updates.

## When Are Concurrent Tasks Acceptable?

Concurrent Jules tasks are safe when the tasks modify **strictly disjoint** areas of the codebase. For example:
- Task A updates `docs/case-studies/digital-logic-circuit.md`
- Task B adds a new feature in `src/utils/math.js`

If you are confident the files will not overlap, you can run them simultaneously. If there is any risk of overlap (like adding to a shared list of links in the `README`), queue the tasks.

## Managing Issue Labels

To sequence tasks effectively using labels like `run-jules`:
1. Add `run-jules` to the first issue.
2. Wait for Jules to open the PR.
3. Review, approve, and **merge the PR**.
4. Once `main` is updated, add `run-jules` to the next issue.

## How to Keep `main` Up to Date Between Tasks

Always wait for a PR to merge before triggering the next Jules task that might touch the same files. If you do trigger a task on an outdated `main` and a PR is opened:
- If the PR has conflicts, Jules cannot resolve them natively if the conflict requires complex human judgment.
- You may need to close the PR and ask Jules to try again by re-triggering the task on the updated `main`.

## Handling Duplicate or Stale PRs

If you accidentally trigger multiple tasks and get duplicate PRs attempting to solve similar problems or modifying the same shared file:
1. Identify the PR that best solves the issue or is closest to mergeable.
2. Review and merge that PR.
3. **Cleanly close the duplicate PRs.**

### Suggested Maintainer Comments for Closing Duplicates

When closing a stale or duplicate PR created by Jules, leave a clear comment for the engineering history:

> **Closing as duplicate.** This change was addressed in #123. The underlying issue will be re-evaluated if needed.

> **Closing as stale.** Another PR updated the shared `README.md` and this branch is now out of date. I will re-trigger the task from the updated `main` branch.

By keeping a clean history and sequencing tasks logically, maintainers can guide Jules effectively without creating unnecessary conflict resolution work.
