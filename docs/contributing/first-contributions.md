# First Contributions Guide

Welcome! We are excited to have you contribute to the AI Coding Workflow Starter Kit for Jules. This repository is designed to be a learning resource and a practical toolkit for GitHub-native AI-assisted development.

Whether you are a student, teacher, translator, or developer, there is a place for you to contribute.

## How to Contribute by Role

### For Students
- **Try the workflow:** Use this starter kit in your own projects and report what worked or what was confusing.
- **Improve examples:** If an example in `examples/` could be clearer, propose an update.
- **Fix typos:** Help us keep the documentation polished.

### For Teachers
- **Share use cases:** Let us know how you are using this kit in your classroom.
- **Suggest curriculum ideas:** Propose new guides or tracks that would help students learn GitHub-native workflows.
- **Review documentation:** Help ensure our explanations are pedagogically sound for beginners.

### For Translators
- **Translate core guides:** Help us reach a global audience by translating files into your native language.
- **Review existing translations:** Check `README.ko.md` or other translated files for accuracy and clarity.
- **See the [Translation Guide](./translations.md)** for specific technical requirements.

### For Documentation Contributors
- **Clarify guides:** If a step in a guide is hard to follow, suggest a clearer phrasing.
- **Add visual aids:** Suggest improvements to our SVG diagrams or propose new ones.
- **Keep links updated:** Report or fix broken relative links.

### For Developers
- **Workflow experiments:** Suggest or implement new workflow levels or automation experiments.
- **CI improvements:** Propose lightweight checks that help maintain repository hygiene without adding heavy automation.
- **Bug fixes:** Fix issues in the example scripts or templates.

### For Maintainers (Reviewing Jules-assisted PRs)
- **Review for readability:** Ensure that Jules-assisted PRs leave a clear, understandable engineering history.
- **Verify scope:** Check that the PR strictly follows the linked issue and doesn't include unrelated changes.
- **Provide feedback:** Give Jules (or the human managing it) constructive feedback on code quality and documentation style.

---

## Recommended First Tasks

We label beginner-friendly tasks as `good first issue`. Here are some common examples:

1.  **Docs-only fixes:** Correcting typos or improving phrasing in a single markdown file.
2.  **Adding a translation:** Translating a short operation guide or the quickstart.
3.  **Refining an issue template:** Suggesting a small field change to `jules_task.yml` to make it more descriptive.
4.  **Audit an example:** Checking that an example in `examples/issues/` still matches the latest templates.

---

## Contribution Flows

### Docs-only PR Flow
1.  **Open an Issue:** Use the **Jules Task** template (even if you aren't using Jules). Briefly describe the fix.
2.  **Create a Branch:** Give it a descriptive name like `docs-fix-typo-readme`.
3.  **Make Changes:** Edit the markdown file(s).
4.  **Submit PR:** Link the issue (e.g., `Closes #123`).
5.  **Validation:** Mention that you checked the markdown hygiene locally (see [Markdown Hygiene](#markdown-hygiene)).

### Translation PR Flow
1.  **Open an Issue:** State which file you intend to translate and into which language.
2.  **Check existing work:** Ensure nobody else is already working on that translation.
3.  **Create a Branch:** Use a name like `lang-ko-quickstart`.
4.  **Translate:** Create a new file with the appropriate extension (e.g., `docs/quickstart.ko.md`).
5.  **Submit PR:** Link the issue and follow the [Translation Guide](./translations.md).

### Example Review Contribution Flow
If you want to contribute a review example:
1.  **Find a PR:** Look for a merged PR that demonstrates a good interaction between a human and Jules.
2.  **Draft the example:** Follow the structure in `examples/pr-reviews/README.md`.
3.  **Submit PR:** Link an issue describing why this example is valuable for learners.

---

## Keeping Issues Small and Reviewable

To ensure a smooth contribution process, especially when using Jules:

- **Avoid broad or vague issues:** Don't open an issue like "Improve documentation." Instead, use "Add a first contributions guide to the contributing folder."
- **One task, one PR:** Keep PRs focused. If you notice an unrelated bug while working on a task, open a separate issue for it.
- **Human-reviewable changes:** Even when Jules assists, the final PR must be readable by a human. If a change is too complex to review easily, it should be broken down into smaller issues.
- **Jules is an assistant:** Remember that Jules is an AI coding agent. You (the human) are responsible for the final quality and correctness of the work you submit.

## Markdown Hygiene

Before submitting, please ensure your files:
- End with a single newline.
- Use spaces (not tabs) for indentation.
- Have no trailing spaces (except exactly two for hard line breaks).

These rules are enforced by our CI to keep the repository clean and consistent.

---

*Thank you for contributing to the future of AI-assisted development!*
