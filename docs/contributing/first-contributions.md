# First Contributions Guide

Welcome to the AI Coding Workflow Starter Kit for Jules. This repository is a learning resource and a GitHub-native playbook for managing AI-assisted development with Jules.

This guide helps new contributors find a practical place to start, whether they are students, teachers, translators, documentation contributors, developers, or maintainers.

**Important:** Jules is an AI coding agent, not a human contributor. Contributors are not required to use Jules. All contributions, whether human-authored or AI-assisted, must be reviewed by a human maintainer before merging.

---

## Where to Contribute

### For Students

If you are learning GitHub or AI-assisted development, start with small documentation and example improvements.

- **Good first issues:** Look for issues labeled `good first issue` or `documentation`.
- **First contribution idea:** Fix a typo, clarify a confusing sentence in the README, or suggest a new example in the `examples/` directory.

### For Teachers

If you are an educator, your feedback can improve the learning path for classrooms and student teams.

- **First contribution idea:** Review `docs/tracks/github-native-collaboration.md` and suggest classroom-friendly clarifications.
- **First contribution idea:** Propose an example issue or review comment that would help students learn GitHub-native workflows.

### For Translators

We welcome translators and international contributors who want to make this starter kit useful beyond English and Korean readers.

- **Translation PR flow:** English (`.md`) is the source language, and Korean (`.ko.md`) is currently maintained as a companion language.
- **First contribution idea:** Review the [Translation Guide](./translations.md), then open an issue using the [Translation Issue Template](../../.github/ISSUE_TEMPLATE/translation.yml) proposing a translation for `docs/quickstart.md` or one operation guide.

### For Documentation Contributors

Clear documentation is one of the main goals of this project.

- **Docs-only PR flow:** Open an issue proposing a documentation change, then create a small PR that updates the relevant Markdown files.
- **First contribution idea:** Audit one existing guide for clarity, missing links, or outdated wording.

### For Developers

Developers can contribute to the workflow templates, CI checks, examples, and repository structure.

- **First contribution idea:** Suggest a lightweight CI check in `.github/workflows/docs-and-templates.yml` if it improves validation without adding heavy automation.
- **First contribution idea:** Propose a small improvement to a GitHub Issue template or PR template.

### For Maintainers Reviewing Jules-assisted PRs

If you maintain a project using this starter kit, review quality is one of the most important contributions.

- **Review contribution flow:** Check that the PR follows the linked issue, includes validation notes, passes CI, and avoids unrelated refactors.
- **First contribution idea:** Use `examples/pr-reviews/` as a reference and contribute a clear approval or change-request example.

---

## Best Practices for First Contributions

### 1. Keep Issues Small and Focused

Avoid broad or vague issues like "Improve the docs" or "Refactor the project." Use specific, reviewable changes instead.

- **Bad:** "Make the repository better."
- **Good:** "Add a troubleshooting section to the Quickstart guide."

### 2. Follow the Workflow

Most changes should start with a GitHub Issue.

```text
Issue → optional Jules task → Pull Request → CI → Human review → Merge
```

### 3. Suggest Workflow Improvements Carefully

If you have ideas for improving how the project uses Jules, open a **Workflow Experiment** issue. Explain the proposed change, expected outcome, risks, and how the experiment preserves human ownership and CI gates.

### 4. Keep AI-assisted Work Reviewable

Whether you wrote the change yourself or used Jules to assist, the final PR must be small enough for a human maintainer to review. Do not self-merge. If a change is too broad, split it into smaller issues.

## Markdown Hygiene

Before submitting, check that Markdown files:

- end with a single newline
- use spaces instead of tabs
- avoid trailing spaces except intentional Markdown hard line breaks
- keep links relative when linking within this repository

These rules help keep CI predictable and make reviews easier.
