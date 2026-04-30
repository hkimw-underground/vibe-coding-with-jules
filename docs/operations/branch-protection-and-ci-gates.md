# Branch Protection and CI Gates

Use branch protection rules and CI gates to keep the Jules workflow reviewable. The goal is simple: changes can be proposed quickly, but `main` should still be protected by pull requests, required checks, and human review.

This guide explains why branch protection matters for AI-assisted workflows and provides recommended settings for a small maintainer-owned repository.

## Why CI Gates Matter for Jules

Jules creates pull requests based on issues. Like any automated coding agent, it can misread ambiguous requirements, touch files outside the intended scope, or format documentation incorrectly.

- **Human Review:** Keeps a human maintainer responsible for intent, correctness, architecture, and merge decisions.
- **CI Validation:** Checks formatting and structure, such as Markdown hygiene and YAML syntax, before review time is spent on details.
- **Protected `main`:** Reduces the chance that unreviewed or unvalidated changes land on the primary branch.

## Recommended Settings for Solo Maintainers

For a solo maintainer using this starter kit, use a lightweight policy that enforces review without adding unnecessary friction.

### 1. Go to Repository Settings

Navigate to your repository on GitHub.

1. Click **Settings** in the top navigation bar.
2. In the left sidebar under **Code and automation**, click **Branches** or **Rulesets**.
3. Create a new branch protection rule or branch ruleset for your default branch.

### 2. Configure the Rule

Set the branch name pattern to `main`, or to your repository's default branch if it uses a different name.

Recommended baseline:

- [x] **Require a pull request before merging**
  - This keeps changes on a PR path before they reach `main`.
  - For a solo maintainer, keep approval requirements lightweight. If GitHub prevents self-approval in your setup, rely on PR review plus required checks instead of requiring another account.
- [x] **Require status checks to pass before merging**
  - Enable required checks for your CI workflows.
  - For this starter kit, use the docs workflow check, such as `Validate docs and templates`.
- [x] **Require branches to be up to date before merging**
  - Optional but useful when multiple PRs touch shared files.
- [x] **Block force pushes**
  - Keep force pushes disabled for `main` so history stays reviewable.
- [x] **Restrict deletions**
  - Prevent accidental deletion of the default branch.

Optional hardening:

- Apply the rule to administrators if your project needs a stricter policy.
- Restrict who can push to matching branches if multiple people have write access.
- Require conversations to be resolved before merging when PR discussions carry important decisions.

### 3. Save Changes

Click **Create** or **Save changes** at the bottom of the page.

## Scaling Up for Teams

The settings above are lightweight and designed for a solo maintainer. If you work with a team, tighten the rules gradually:

- Require at least 1 or 2 human approvals.
- Enforce code owner reviews if your repository uses a `CODEOWNERS` file.
- Require conversations to be resolved before merging.
- Require signed commits if your project needs stronger provenance controls.

## Note on Automation Safety

Branch protection is a useful control, but it does not make automation fully safe. It helps enforce the process: PR first, CI second, human review before merge. The quality and direction of the project still require maintainer judgment.
