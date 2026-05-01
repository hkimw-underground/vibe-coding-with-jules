# Jules Web UI Feature Guide

This guide explains how the features visible in the Jules web UI map to the GitHub-native workflow. Understanding these connections helps maintainers, students, and teachers use Jules effectively as an AI coding agent.

## Repository Configuration

### Configure repo
- **What it is for:** The entry point for connecting Jules to your GitHub repository and defining basic settings.
- **When to use it:** During initial project onboarding or when you need to update repository-level permissions and access.
- **GitHub Connection:** This establishes the foundation for Jules to read issues, create branches, and open pull requests.
- **Safety Note:** Only repository maintainers should perform configuration to ensure security settings align with project policies.

### Setup script
- **What it is for:** Defines the commands Jules should run to prepare the environment (e.g., `npm install`, `pip install`).
- **When to use it:** When your project has specific build or dependency requirements that Jules needs to understand to run tests or verify code.
- **GitHub Connection:** Maps to your project's local development setup and ensures Jules's environment matches what CI or human developers use.
- **Safety Note:** Start with simple scripts. Avoid scripts that perform destructive actions or require sudo privileges.

### Environment variables
- **What it is for:** Securely providing keys, tokens, or configuration values Jules might need during execution.
- **When to use it:** When a task requires access to external APIs or specific environment-dependent configurations.
- **GitHub Connection:** Allows Jules to access necessary configuration or credentials securely, similar to how secrets are used in automated workflows.
- **Safety Note:** Never include actual secrets in your issue descriptions or public files. Use this UI feature to manage them securely.

### Network access
- **What it is for:** Controlling whether Jules can access the internet to fetch documentation or external data.
- **When to use it:** If your project depends on external resources that Jules needs to consult or interact with.
- **GitHub Connection:** Determines the scope of Jules's reach beyond the repository files.
- **Safety Note:** For maximum privacy and security, keep network access restricted unless specifically required for a task.

### Knowledge
- **What it is for:** Providing Jules with additional context, such as documentation links or specific project rules.
- **When to use it:** When your codebase has complex architectural patterns or external dependencies not fully captured in the source code.
- **GitHub Connection:** Complements `AGENTS.md` by giving Jules high-level guidance before it starts a task.
- **Safety Note:** Keep knowledge documents concise and up-to-date to avoid confusing the agent with conflicting information.

## Task Management

### Suggestions
- **What it is for:** AI-generated ideas for tasks or improvements based on the current state of the codebase.
- **When to use it:** During the "Triage" phase or when looking for small "good first issues" for Jules to handle.
- **GitHub Connection:** These can be used as starting points for new GitHub Issues.
- **Safety Note:** Always review suggestions for relevance. Not every suggestion needs to become a task.

### CI fixer
- **What it is for:** Specifically targeting and fixing broken CI builds.
- **When to use it:** When a PR has failing checks and the cause is identifiable (e.g., a linting error or a failing test).
- **GitHub Connection:** Directly responds to GitHub Actions failures, helping move a PR toward a green state.
- **Safety Note:** Verify that the fix doesn't just "silence" the error but actually addresses the underlying issue.

### Scheduled task
- **What it is for:** Automating recurring work like dependency updates or periodic documentation audits.
- **When to use it:** For maintenance tasks that don't require an immediate human trigger.
- **GitHub Connection:** Enables Jules to initiate work on a recurring schedule, helping with routine maintenance.
- **Safety Note:** Monitor scheduled tasks to ensure they don't create a backlog of unreviewed PRs.

## Planning and Execution

### Interactive plan
- **What it is for:** Reviewing and refining the steps Jules intends to take before it starts writing code.
- **When to use it:** For complex tasks where the implementation strategy is critical.
- **GitHub Connection:** This is the "pre-implementation" phase. It ensures Jules's approach aligns with the maintainer's expectations before a PR is created.
- **Safety Note:** Use the interactive plan to catch architectural misunderstandings early.

### Review
- **What it is for:** The interface for looking at Jules's proposed changes before they are finalized.
- **When to use it:** After Jules has completed its initial work but before the PR is officially ready for human review on GitHub.
- **GitHub Connection:** Acts as a bridge between "Work in Progress" and "Ready for Review."
- **Safety Note:** This is your first opportunity to catch errors. Be as thorough here as you would be on a GitHub PR.

### Start
- **What it is for:** The primary button to begin a task based on a selected issue or prompt.
- **When to use it:** Once an issue is well-defined and you are ready for Jules to begin.
- **GitHub Connection:** Triggers the creation of a new branch and the start of the coding process.
- **Safety Note:** Ensure you have selected the correct branch and issue before clicking Start.

### Branch selection
- **What it is for:** Choosing the base branch Jules should work from.
- **When to use it:** Every time you start a new task.
- **GitHub Connection:** Indicates the source branch Jules should use to start its work. Usually, this should be your default branch (e.g., `main`).
- **Safety Note:** Working off the wrong branch can lead to complex merge conflicts later.

## Analysis and Insights

### Codebase overview
- **What it is for:** A high-level summary of the project's structure, languages, and core components.
- **When to use it:** When a new maintainer or student is joining the project, or when Jules needs a "refresher" on the project scope.
- **GitHub Connection:** Provides context that helps Jules understand where new files should go or which existing files to modify.
- **Safety Note:** Use this to verify that Jules sees the repository structure correctly.

### Automatically find issue in your codebase
- **What it is for:** Identifying potential bugs or missing features by scanning the source code.
- **When to use it:** During project "cleanup" phases or when looking to improve codebase health.
- **GitHub Connection:** Helps generate a backlog of GitHub Issues that are grounded in actual code analysis.
- **Safety Note:** Treat these as "findings" that require human validation before being turned into tasks.

### Performance / design / security
- **What it is for:** Specialized analysis modes focusing on specific quality attributes.
- **When to use it:** Before a major release or when addressing technical debt.
- **GitHub Connection:** Helps maintain high standards for the repository, similar to specialized linting or security scanning tools.
- **Safety Note:** AI analysis can sometimes flag "false positives." Always use your engineering judgment.

### Configure render
- **What it is for:** Adjusting how Jules displays its output or interacts with frontend components.
- **When to use it:** If your project involves visual components that require specific rendering settings to be verified.
- **GitHub Connection:** Enhances the "Validation" part of the PR description by providing visual evidence of changes.
- **Safety Note:** Primarily useful for frontend-heavy projects.

## Advanced Tools

### Download CLI
- **What it is for:** Getting the command-line interface for Jules to run tasks from your local terminal.
- **When to use it:** When you prefer working in a terminal environment rather than the web UI.
- **GitHub Connection:** Provides an alternative way to interact with Jules from a local development environment while still connecting back to GitHub issues and PRs.
- **Safety Note:** Ensure your local environment is configured securely before using the CLI.

### Try API
- **What it is for:** Accessing Jules's capabilities programmatically.
- **When to use it:** For advanced users looking to build custom integrations or automation workflows.
- **GitHub Connection:** Allows for programmatic integration of Jules into custom tools or advanced automation experiments.
- **Safety Note:** This is an experimental feature for advanced users. Requires careful handling of API keys.
