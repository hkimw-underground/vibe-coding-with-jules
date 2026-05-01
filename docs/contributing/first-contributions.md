# First Contributions Guide

Welcome to the AI Coding Workflow Starter Kit! We are thrilled that you are considering making your first contribution. This repository is a learning environment and a GitHub-native playbook for managing AI-assisted development with Jules.

This guide is designed to help you find the right place to start, whether you are a student, teacher, translator, documentation contributor, or developer.

**Important Reminder:** Jules is an AI coding agent, not a human contributor. You are not required to use Jules to contribute to this project. All contributions, whether human-authored or AI-assisted, must be reviewed by a human maintainer before merging.

---

## Where to Contribute

### 🧑‍🎓 For Students
If you are learning GitHub or how to work with AI agents, this repository is a safe place to practice.
- **Good first issues:** Look for issues labeled `good first issue` or `documentation`.
- **First contribution idea:** Fix a typo, clarify a confusing sentence in the README, or suggest a new example in the `examples/` directory.

### 👩‍🏫 For Teachers
If you are an educator, we welcome improvements to our workflow tracks and learning materials.
- **First contribution idea:** Review the `docs/tracks/github-native-collaboration.md` track and suggest clarifications or classroom-friendly adaptations.
- **First contribution idea:** Add a new issue template or example review specifically tailored for student assignments.

### 🌍 For Translators
We explicitly welcome translators and international contributors to help make this starter kit accessible to a global audience.
- **Translation PR flow:** English (`.md`) is the source language, and Korean (`.ko.md`) is our companion language.
- **First contribution idea:** Review our [Translation Guide](./translations.md) and open a PR to translate the `docs/quickstart.md` or one of the operations guides into your language.

### ✍️ For Documentation Contributors
Clear documentation is the backbone of this project.
- **Docs-only PR flow:** Open an issue proposing a documentation change. Once approved, create a small PR updating the `.md` files. Ensure you check for Markdown hygiene (no tabs, single newline at EOF).
- **First contribution idea:** Audit one of our existing guides for clarity, or propose a new FAQ entry based on your experience setting up the starter kit.

### 💻 For Developers
Developers can contribute to the core workflow, CI checks, and templates.
- **First contribution idea:** Suggest a new lightweight CI check in `.github/workflows/docs-and-templates.yml` to improve our validation process.
- **First contribution idea:** Propose improvements to our GitHub Issue templates to make them more robust for Jules tasks.

### 🛡️ For Maintainers (Reviewing Jules-assisted PRs)
If you are maintaining a project using this starter kit, your primary contribution is review.
- **Review contribution flow:** Reviewing a PR is a vital contribution. Check that the PR strictly follows the linked issue, validation notes are present, and no unrelated refactors were made.
- **First contribution idea:** Use our example reviews in `examples/pr-reviews/` as a template to provide constructive feedback on an open PR.

---

## Best Practices for First Contributions

### 1. Keep Issues Small and Focused
Avoid broad or vague issues like "Improve the docs" or "Refactor the project." Instead, propose specific, actionable changes.
- **Bad:** "Make the repository better."
- **Good:** "Add a troubleshooting section to the Quickstart guide."

### 2. Follow the Workflow
All changes must start with a GitHub Issue.
```text
Issue → (Optional) Jules task → Pull Request → CI → Human Review → Merge
```

### 3. Suggesting Workflow Improvements
If you have ideas for improving how we work with Jules, open a **Workflow Experiment** issue. Clearly outline the proposed change, the expected outcome, and how it aligns with our core principles (e.g., human ownership, CI gates).

### 4. Human Review is Mandatory
Whether you wrote the code yourself or used Jules to assist, a human maintainer must review and approve the PR. Do not self-merge. Jules-assisted work should remain small, scoped, and easily reviewable by a maintainer.

We look forward to your contributions! If you have any questions, feel free to open an issue or ask for clarification.
