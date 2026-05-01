# Jules Web UI Feature Guide

This guide explains how the visible Jules web UI features can fit into a GitHub-native workflow. It is written for maintainers, students, teachers, and first-time users who want to understand when each control is useful.

The descriptions below are workflow guidance, not a promise of exact product behavior. Some options may depend on repository permissions, account settings, product availability, or the selected task mode.

## Repository Configuration

### Configure repo

- **What it is for:** Connecting a repository to Jules and reviewing repository-level settings.
- **When to use it:** During initial onboarding or when repository access, defaults, or project settings need to be reviewed.
- **GitHub connection:** Treat this as the setup step before issue-driven Jules work can happen in a repository.
- **Safety note:** Repository configuration should be handled by a maintainer who understands the repo's security and collaboration policy.

### Setup script

- **What it is for:** Defining setup commands Jules may need before building, testing, or inspecting the project.
- **When to use it:** When the repository needs specific dependency installation or setup steps.
- **GitHub connection:** Keep this close to the same setup path used by human contributors and CI.
- **Safety note:** Start with small, repeatable commands. Avoid destructive commands or scripts that require elevated privileges.

### Environment variables

- **What it is for:** Supplying configuration values that a task may need at runtime.
- **When to use it:** When tests, builds, or integrations depend on environment-specific configuration.
- **GitHub connection:** Treat these like other repository-level secret or configuration settings: document what is needed, but do not expose values in public docs or issues.
- **Safety note:** Never paste real secrets into GitHub Issues, PRs, README files, or prompts.

### Network access

- **What it is for:** Controlling whether a task may use network access beyond the repository contents.
- **When to use it:** When a task genuinely needs external documentation, package access, APIs, or network checks.
- **GitHub connection:** Decide whether the task should be self-contained or allowed to depend on external resources.
- **Safety note:** Keep network access restricted unless the task clearly needs it.

### Knowledge

- **What it is for:** Providing Jules with extra project context, such as architecture notes, documentation links, or repo-specific rules.
- **When to use it:** When important project context is not obvious from the codebase alone.
- **GitHub connection:** Use it alongside `AGENTS.md`, issue templates, and PR templates.
- **Safety note:** Keep knowledge sources short, current, and consistent with the repository docs.

## Task Management

### Suggestions

- **What it is for:** Surfacing possible tasks or improvement ideas.
- **When to use it:** During backlog grooming, teaching sessions, or when looking for small starter tasks.
- **GitHub connection:** Convert useful suggestions into scoped GitHub Issues before asking Jules to work on them.
- **Safety note:** Treat suggestions as candidates, not decisions. A maintainer should choose what becomes an issue.

### CI fixer

- **What it is for:** Helping investigate and repair failing CI or validation checks.
- **When to use it:** When a PR or branch has a clear failing check that should be fixed without expanding scope.
- **GitHub connection:** Use it with GitHub Actions logs, PR checks, and validation notes.
- **Safety note:** Verify that the change fixes the root cause instead of hiding or weakening the check.

### Scheduled task

- **What it is for:** Running recurring maintenance work on a schedule, where available.
- **When to use it:** For predictable maintenance such as documentation audits, dependency checks, or periodic cleanup prompts.
- **GitHub connection:** Scheduled work should still produce reviewable GitHub artifacts, such as issues, branches, PRs, or maintainer reports, depending on configuration.
- **Safety note:** Avoid schedules that create more work than the maintainer can review.

## Planning and Execution

### Interactive plan

- **What it is for:** Reviewing or shaping the intended approach before implementation begins.
- **When to use it:** For tasks where architecture, file boundaries, or sequencing matter.
- **GitHub connection:** Use the plan to confirm that the task still matches the GitHub Issue before code changes begin.
- **Safety note:** This is a good place to catch scope creep early.

### Review

- **What it is for:** Inspecting Jules-assisted work before deciding whether it is ready for GitHub review or further iteration.
- **When to use it:** After Jules has produced a proposed change, plan, or result.
- **GitHub connection:** Use this step before approving, requesting changes, or merging a PR.
- **Safety note:** Do not skip GitHub PR review just because the web UI result looks plausible.

### Start

- **What it is for:** Beginning a Jules task from a selected prompt, issue, or workflow entry point.
- **When to use it:** After the task is scoped, the branch target is checked, and required context is available.
- **GitHub connection:** This is the handoff point from maintainer intent to Jules-assisted work.
- **Safety note:** Confirm the selected repository, branch, and issue before starting.

### Branch selection

- **What it is for:** Choosing the branch context for Jules-assisted work.
- **When to use it:** Before starting work, especially if the repo has multiple release, experiment, or documentation branches.
- **GitHub connection:** Prefer starting from the intended default or feature base branch to avoid unnecessary conflicts.
- **Safety note:** The wrong base branch can create confusing diffs or stale PRs.

## Analysis and Insights

### Codebase overview

- **What it is for:** Getting a high-level summary of the repository structure and major components.
- **When to use it:** When onboarding a new maintainer, student, or task context.
- **GitHub connection:** Use the overview to decide where a new issue or PR should focus.
- **Safety note:** Treat the overview as a starting point. Confirm important details in the source files.

### Automatically find issue in your codebase

- **What it is for:** Looking for possible codebase issues, cleanup opportunities, or improvement candidates.
- **When to use it:** During triage, refactoring planning, or educational code review.
- **GitHub connection:** Turn confirmed findings into scoped GitHub Issues before implementation.
- **Safety note:** Findings need human validation before becoming work items.

### Performance / design / security

- **What it is for:** Reviewing the codebase through a specific quality lens.
- **When to use it:** Before releases, during architecture review, or when preparing focused improvement tasks.
- **GitHub connection:** Convert useful findings into labeled issues or review comments.
- **Safety note:** AI-assisted analysis can produce false positives. Validate before acting.

### Configure render

- **What it is for:** Adjusting render or preview-related settings when a project needs visual inspection.
- **When to use it:** For frontend, documentation, or UI-heavy projects where rendered output matters.
- **GitHub connection:** Use rendered output as supporting validation evidence in PRs when relevant.
- **Safety note:** Visual checks are useful, but they do not replace tests or code review.

## Advanced Tools

### Download CLI

- **What it is for:** Accessing a command-line workflow when the CLI is available for your account or environment.
- **When to use it:** When a maintainer prefers terminal-based workflows or wants local workflow integration.
- **GitHub connection:** Keep the same issue, branch, PR, and review discipline used in the web UI.
- **Safety note:** Local credentials and environment settings should be handled carefully.

### Try API

- **What it is for:** Exploring API-based integration options when available.
- **When to use it:** For advanced maintainers experimenting with custom workflow integrations.
- **GitHub connection:** API-based workflows should still create reviewable GitHub artifacts and respect branch protection.
- **Safety note:** Treat API usage as advanced. Protect keys, limit permissions, and test in a sandbox first.
