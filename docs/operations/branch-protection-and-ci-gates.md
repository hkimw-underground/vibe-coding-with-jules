# Branch Protection and CI Gates

To safely manage Jules as an AI coding agent, your repository needs branch protection rules and CI (Continuous Integration) gates. This ensures that `main` is protected, and every change proposed by Jules is verified and approved by a human maintainer before merging.

This guide explains why branch protection matters for AI workflows and provides recommended settings for a small maintainer-owned repository.

## Why CI Gates Matter for Jules

Jules creates pull requests based on issues. While Jules is skilled, it is an agent, not a human. It can make logical errors, misinterpret ambiguous requirements, or format code incorrectly.

- **Human Review:** Forces a human maintainer to review the AI's work, validating its intent and correctness.
- **CI Validation:** Ensures code formatting (like Markdown hygiene) and structure (like YAML syntax) are correct without wasting human review time.
- **Protected `main`:** Prevents Jules (or any contributor) from accidentally pushing broken code directly to the primary branch.

## Recommended Settings for Solo Maintainers

For a solo maintainer using this starter kit, you want a lightweight policy that enforces safety without being overly restrictive.

### 1. Go to Repository Settings

Navigate to your repository on GitHub.
1. Click **Settings** in the top navigation bar.
2. In the left sidebar under "Code and automation", click **Branches**.
3. Click **Add branch protection rule**.

### 2. Configure the Rule

Set the **Branch name pattern** to `main` (or `master`, depending on your default branch).

Check the following settings:

- [x] **Require a pull request before merging**
  - This ensures Jules cannot push directly to `main`.
  - Leave **Require approvals** unchecked or set to 0 if you are a solo maintainer, as you cannot approve your own PRs. If you work in a team, require at least 1 approval.
- [x] **Require status checks to pass before merging**
  - [x] **Require branches to be up to date before merging** (Optional but recommended to prevent merge conflicts).
  - Search for and select your CI workflows in the status checks box. For this starter kit, select the job name for the docs workflow (e.g., `Validate docs and templates` or `docs-and-templates`).
- [x] **Do not allow bypassing the above settings**
  - Ensure this applies to administrators as well, so even you don't accidentally bypass the CI gates.
- [x] **Restrict who can push to matching branches**
  - Leave this empty to prevent anyone from pushing directly to `main`.
- [x] **Allow force pushes** (Leave unchecked)
  - Blocking force pushes protects the history of `main`.
- [x] **Allow deletions** (Leave unchecked)
  - Restricts accidental deletion of the `main` branch.

### 3. Save Changes

Click **Create** or **Save changes** at the bottom of the page.

## Scaling Up for Teams

The settings above are lightweight and designed for a solo maintainer. If you work with a team, you can tighten the rules:

- Require at least 1 or 2 human approvals.
- Enforce code owner reviews if your repository uses a `CODEOWNERS` file.
- Require conversations to be resolved before merging.

## Note on Automation Safety

Branch protection is a crucial layer of defense, but it does not make automation fully safe. Always review the changes Jules proposes. Branch protection ensures the *process* is followed, but the *quality* of the code still requires human oversight.
