# Case Study B: English-Only Open Source Project

Status: planned.

This case study will document a clean English-only open-source project using the same Jules workflow shown in this starter kit.

## Purpose

Case Study B exists to show that the workflow is reusable outside a school or capstone context. It will demonstrate how a human maintainer leads Jules (an AI coding agent) through standard GitHub engineering practices for a globally accessible open-source project.

It should demonstrate:

- small GitHub Issues
- focused Jules pull requests
- CI-first development
- readable human review comments
- clear separation between AI agent work and maintainer ownership

## Recommended Project Direction

**Primary Option: Markdown link checker mini CLI**

A small English-only developer tool or documentation-focused utility is the best fit because it is easy for global readers to understand, test, and review. A Markdown link checker mini CLI provides a real, testable implementation surface without domain-specific complexity.

## Project Constraints

To ensure a clear, readable case study, the project must:

- Avoid private, school-specific, or organization-specific context.
- Not be used to demonstrate fully autonomous development.
- Not mix unrelated goals such as branding, large architecture rewrites, or product strategy.
- Maintain Jules's identity strictly as an AI coding agent, not a human contributor.

## Suggested Repository Name Options

- `md-link-checker-cli`
- `markdown-link-validator`
- `simple-md-link-checker`

## First 5 Starter Issues for Jules

1. **Setup project scaffolding and CI:** Initialize the project structure and add a basic GitHub Actions workflow for linting and testing.
2. **Implement CLI argument parsing:** Add the ability to accept a file path or directory as input.
3. **Implement Markdown parsing:** Extract all URLs from the provided Markdown files.
4. **Implement HTTP link validation:** Check the extracted URLs to see if they return a 200 OK status.
5. **Format output results:** Display the results of the link checks clearly in the console (e.g., success, broken links).

## Expected Workflow Sequence

The project will strictly follow this PR sequence for every task:

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

Each PR must be small, focused, and directly linked to a single issue. Unrelated refactors are prohibited.

## CI Requirements

The project must implement CI gates to enforce quality before human review:

- **Linting:** Code formatting and style checks.
- **Tests:** Automated unit tests for core logic (e.g., parsing, validation).
- **Build/Type Check:** If applicable, ensure the project builds or type-checks successfully.

CI must pass before the maintainer reviews the PR.

## Review Examples to Capture

During the project, maintainers should save examples of:

- A PR where the maintainer requested changes due to scope creep.
- A PR where Jules added tests to fix a CI failure.
- A PR approved and merged cleanly after addressing human feedback.

## Completion Criteria

The planned brief can be replaced with the real case study when the following criteria are met:

- The repository is created and public.
- The 5 starter issues are completed via the Jules workflow.
- PRs clearly demonstrate the human-led AI coding process.
- Examples of issues, PR descriptions, CI runs, and human reviews are captured and documented.
