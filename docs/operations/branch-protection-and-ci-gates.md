# Branch Protection and CI Gates

This guide explains how to configure GitHub branch protection and CI gates to support a safe, AI-assisted workflow.

## Why Branch Protection Matters

In an AI-assisted workflow, Jules (or any AI agent) can generate Pull Requests quickly. While this increases productivity, it also increases the risk of merging unintended changes if not properly gated.

Branch protection ensures that:
- **Human Review is Mandatory**: No code enters the `main` branch without a maintainer's sign-off.
- **CI is Enforced**: Automated checks must pass before a merge is even possible.
- **History is Preserved**: Force pushes are blocked, preventing the accidental deletion of engineering history.

## Recommended Settings for Solo Maintainers

If you are a solo maintainer, you want safety without unnecessary friction. GitHub's "Branch Protection Rules" (available in Settings > Branches) allow you to strike this balance.

### 1. Require a Pull Request Before Merging
This is the most fundamental rule. It prevents anyone (including you) from pushing directly to `main`.

- **Setting**: `Require a pull request before merging`
- **Solo Tip**: You don't necessarily need to require an approval from *another* user if you are alone, but the PR flow itself forces you to review Jules's work in the GitHub UI before it merges.

### 2. Require Status Checks to Pass Before Merging
This turns your CI into a "gate." If the tests fail, the "Merge" button is disabled.

- **Setting**: `Require status checks to pass before merging`
- **Which checks?**: Select `Validate docs and templates` (the workflow included in this starter kit).
- **Solo Tip**: This prevents you from accidentally merging a PR where Jules broke the Markdown formatting or deleted a required file.

### 3. Block Force Pushes
Force pushes can rewrite history and delete the record of how a feature was built.

- **Setting**: `Allow force pushes` (Keep this **Unchecked**)

### 4. Restrict Deletions
Prevents the accidental deletion of the `main` branch.

- **Setting**: `Allow deletions` (Keep this **Unchecked**)

## How to Scale for Teams

As your project grows, you can add stricter rules:

- **Require Approvals**: Set `Required number of approvals before merging` to 1 or 2.
- **Dismiss Stale Approvals**: Automatically dismiss a review when new commits are pushed.
- **Require Review from Code Owners**: Use a `CODEOWNERS` file to mandate reviews from specific experts for specific directories.

## Summary: The Safety Model

Branch protection doesn't make automation "fully safe," but it makes the **Safety Model** concrete:

1. **Jules** creates a focused PR.
2. **CI** validates the technical hygiene (Markdown, YAML, files).
3. **Human** reviews the logic and architectural fit.
4. **Merge** happens only when both human and machine agree.

By enforcing this flow, you ensure that Jules remains a *contributor* to your project, while you remain the *maintainer*.
