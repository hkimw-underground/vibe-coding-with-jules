# Case Study B: English-Only Open Source Project

Status: planned.

This case study documents a clean English-only open-source project using the same Jules workflow shown in this starter kit.

## Project Goal

Build a small documentation and tooling-oriented project that allows readers to understand the entire repository quickly while remaining real enough to show issues, pull requests, CI, review comments, and maintainer decisions.

## Recommended Project Direction

**Recommended Repository Name:** `github-workflow-lab`

**Proposed Repository Name Options:**
- `github-workflow-lab`
- `jules-workflow-demo-notes`
- `issue-driven-docs-demo`
- `tiny-maintainer-playbook`

### Target Audience

The target audience includes students, teachers, first-time open-source maintainers, and developers looking for practical examples of an AI-assisted development process that leaves a readable GitHub history.

### Why This Case Study Exists

Case Study B exists to show that the workflow is reusable outside a school or capstone context. It provides a clean example for a global audience using English as the primary language for code, documentation, and collaboration. It makes the starter kit easier to trust for global readers.

### What It Demonstrates About the Jules Workflow

This project demonstrates:
- Small, focused GitHub Issues
- Jules as an AI coding agent generating scoped pull requests
- CI-first development (validating Markdown hygiene and links)
- Readable human review comments
- Clear separation between AI agent work and human maintainer ownership
- Review-Driven as the default workflow track

## Initial Repository Structure

Before the first issue, the repository will contain basic scaffolding:

```text
github-workflow-lab/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── jules_task.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── validate.yml
├── docs/
│   └── index.md
├── README.md
├── AGENTS.md
└── LICENSE
```

## First 5 GitHub Issues

1. **Add Markdown linting to CI:** Set up a step in `.github/workflows/validate.yml` to check for trailing spaces and required newlines in Markdown files.
2. **Create repository setup guide:** Add `docs/setup.md` explaining how to clone the repository and run the new validation script locally.
3. **Add broken link checker:** Add a step to the CI workflow that verifies all internal relative links in the documentation point to existing files.
4. **Draft maintainer review guidelines:** Create `docs/review-guidelines.md` detailing how a human maintainer should review PRs created by Jules.
5. **Update README with project index:** Update `README.md` to include a table of contents linking to all files in the `docs/` directory.

## Expected Jules Workflow for Each Issue

For every issue, the maintainer and Jules will follow the Review-Driven workflow:

1. **Issue Creation:** The human maintainer opens a scoped GitHub issue detailing the requirement.
2. **Jules Task:** The maintainer assigns the task to Jules, ensuring the scope matches the issue.
3. **Pull Request:** Jules (the AI coding agent) creates a small, focused pull request with the necessary changes.
4. **CI Validation:** Automated checks (Markdown linting, link checking) run against the PR.
5. **Human Review:** The maintainer reviews the changes, leaving readable comments for approvals or change requests.
6. **Merge:** After CI passes and the maintainer approves, the maintainer merges the PR.

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

## CI Plan

- **Validation Checks:** GitHub Actions will enforce Markdown hygiene (no tabs, required newlines, specific trailing space rules) on every PR.
- **Link Checking:** A script will ensure all internal relative links resolve correctly.

## Review Plan

- **Human Ownership:** The human maintainer owns the architecture, validation, review, and final merge decision.
- **Review Examples:** The case study will capture real review scenarios, such as confirming correct link structures, requesting clearer documentation wording, or asking Jules to fix a failing CI check.

## Risks and Mitigations

- **Risk:** Jules modifies files outside the issue scope.
  - **Mitigation:** Rely on the Review-Driven track. The maintainer will request changes to revert out-of-scope edits before merging.
- **Risk:** CI checks fail due to incorrect Markdown formatting.
  - **Mitigation:** The issue templates and `AGENTS.md` will explicitly state the formatting rules. CI gates will prevent merging until Jules fixes the formatting.
- **Risk:** The repository becomes too complex for a quick demo.
  - **Mitigation:** Keep the project strictly focused on documentation and simple validation scripts. Avoid building a large application.

## Acceptance Criteria for the Case Study

This planned brief can be replaced by the real case study once the following are met:

- The separate `github-workflow-lab` repository is created and public.
- At least 5 Jules-assisted PRs have been merged following the Review-Driven workflow.
- The repository includes a clear README, CI status, and documented review examples.
- Representative issues, PR descriptions, CI runs, and human reviews are linked in the final case study document.

## Non-Goals

- Do not claim Jules can safely work without human review in production.
- Do not present Jules as a human contributor; always frame it as an AI coding agent.
- Do not use promotional language or mention external rankings or lists.

## Connection Back to This Starter Kit

This case study is a direct application of the AI Coding Workflow Starter Kit for Jules. It uses the same `.github` templates, `AGENTS.md` guidelines, and Review-Driven track defined in the starter kit, proving that the workflow is adaptable to standard, English-only open-source repositories.
