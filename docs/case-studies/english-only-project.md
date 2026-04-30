# Case Study B: English-Only Open Source Project

Status: planned.

This case study will document a clean English-only open-source project using the same Jules workflow shown in this starter kit.

## Purpose

Case Study B exists to show that the workflow is reusable outside a school or capstone context. It will demonstrate how a human maintainer leads Jules (an AI coding agent) through standard GitHub engineering practices for a globally accessible open-source project.

It should demonstrate:

- Small GitHub Issues
- Focused Jules pull requests
- CI-first development
- Readable human review comments
- Clear separation between AI agent work and maintainer ownership

## Recommended Project Direction

**Primary Option: Markdown link checker mini CLI**

A small English-only developer tool or documentation-focused utility is the best fit because it is easy for global readers to understand, test, and review. A Markdown link checker mini CLI provides a real, testable implementation surface without domain-specific complexity.

### Project Constraints

To ensure a clear, readable case study, the project must:

- **English-Only:** All code, comments, issues, and documentation must be in English.
- **Small Surface:** Focus on core functionality (parsing links, checking status) rather than complex edge cases.
- **Testability:** Must support automated unit tests for link parsing and status checking.
- **Jules-Friendly:** Issues should be small enough to be completed in single-digit file changes.
- **Identity:** Maintain Jules's identity strictly as an AI coding agent, not a human contributor.

### Repository Name Options

- `md-link-linter`
- `markdown-link-validator`
- `jules-linter-demo`

## First 5 Starter Issues for Jules

1. **Initialize CLI project structure**: Set up a basic project structure with a CLI entry point that accepts a file path and prints "Checking [file]...".
2. **Implement Markdown link extractor**: Write a parser to extract all Markdown-style links `[text](url)` from a given file.
3. **Add internal link validation**: Implement a check to verify that internal relative links (e.g., `./docs/setup.md`) point to existing files on disk.
4. **Add external link validation**: Use a lightweight HTTP library to check if external URLs return a successful status code.
5. **Implement summary reporter**: Add a final report to the CLI output showing the total number of links checked, number of broken links, and a list of failed URLs.

## Expected PR Sequence

1. **PR 1 (Scaffolding)**: Basic project structure, dependency management, and "hello world" CLI.
2. **PR 2 (Link Extraction)**: Core parsing logic with unit tests.
3. **PR 3 (Local Check)**: File system existence checks for relative links.
4. **PR 4 (Remote Check)**: Network requests for external links with timeout handling.
5. **PR 5 (UX/Reporting)**: Polished console output and error summary.

## CI Requirements

The project must implement CI gates to enforce quality before human review:

- **Linting**: Standard linting rules for the chosen language.
- **Tests**: Automated test suite running on every PR via GitHub Actions.
- **Hygiene**: Markdown hygiene checks for the project's own documentation.

## Review Examples to Capture

During the project, maintainers should save examples of:

- **Change Request**: A PR where the maintainer requested changes due to scope creep or naming conventions.
- **CI Fix**: A PR where Jules added tests or refined logic to fix a CI failure.
- **Clean Approval**: A PR approved and merged cleanly after addressing human feedback.

## Completion Criteria

The planned brief can be replaced with the real case study when the following criteria are met:

1. The repository is created and public.
2. At least 5 Jules-driven PRs have been merged following the workflow.
3. PRs clearly demonstrate the human-led AI coding process (Issue → PR → Review → Merge).
4. Representative PRs, descriptions, CI runs, and human reviews are captured and documented.

## Maintainer Notes

When this case study is selected, replace this placeholder with:

- repository link
- project summary
- selected issues
- representative Jules PRs
- review examples
- CI results
- lessons learned
