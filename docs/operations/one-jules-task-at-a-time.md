# Operations Guide: One Jules Task at a Time

Managing an AI coding agent requires sequencing to maintain a clean engineering history. While it is tempting to run multiple tasks in parallel, doing so can lead to stale Pull Requests (PRs) and merge conflicts, especially when tasks touch shared files.

## Why One Task at a Time?

Jules operates based on the current state of the repository. If you start Task B before Task A is merged:

1. **Stale Context**: Task B may not "see" the changes from Task A.
2. **Merge Conflicts**: Both tasks might modify the same lines in shared files (e.g., `README.md`, `AGENTS.md`, or CI configs).
3. **Duplicate Work**: If Task A and Task B overlap in scope, Jules might implement the same logic twice in different ways.

**Running tasks sequentially ensures that each task begins with the most up-to-date `main` branch.**

## When Concurrent Tasks are Acceptable

Concurrency is safe when tasks are strictly isolated:

- Tasks touch different, unrelated directories (e.g., `docs/case-studies/` vs `examples/issues/`).
- Tasks do not modify shared configuration files.
- The repository has high modularity.

## How Duplicate or Stale PRs Happen

1. **Parallel Triggers**: A maintainer adds the `run-jules` label to two issues simultaneously.
2. **Delayed Review**: Task A is finished but sits in PR. Task B is started from `main`, unaware of Task A's pending changes.
3. **Overlapping Scope**: Two issues describe similar problems, leading Jules to create similar PRs.

## How to Sequence Tasks Safely

### 1. Sequence Issue Labels

Do not label multiple issues with `run-jules` at once.

- **Workflow**: Label Issue #1 → Wait for PR → Review/Merge PR → Update `main` → Label Issue #2.

### 2. Keep Main Up to Date

Before starting a new Jules task, ensure your remote `main` branch is up to date. Jules typically starts its task by checking out the latest `main`; if `main` is behind, Jules will work on stale code.

### 3. Handle Stale PRs

If a PR becomes stale due to a merge in `main`:

- Ask Jules to rebase or update the branch.
- If the PR is no longer needed, close it promptly to keep the PR list manageable.

## Closing Duplicate PRs

When Jules creates a duplicate or unnecessary PR, close it with a clear comment. This keeps the history clean and informs other maintainers.

### Suggested Maintainer Comments

**For a duplicate PR:**
> Closing this as a duplicate of #PR_NUMBER. We are currently sequencing Jules tasks to avoid conflicts in shared files.

**For a stale PR that is no longer needed:**
> Closing this PR as the requirements have been addressed in #PR_NUMBER.

**To Jules when requesting a restart:**
> This PR has major conflicts with the updated `main`. I am closing this. Please start a new task based on the latest `main` branch from Issue #ISSUE_NUMBER.

---

*Note: Jules is an AI coding agent. Proper sequencing is a maintainer's responsibility to ensure a high-quality repository history.*
