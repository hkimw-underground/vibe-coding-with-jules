# Case Study B: English-Only Open Source Project

Status: planned.

This case study will document a clean English-only open-source project using the same Jules workflow shown in this starter kit.

## Purpose

Case Study B exists to show that the workflow is reusable outside a school or capstone context, specifically for a global audience using English as the primary language for code, documentation, and collaboration.

It should demonstrate:

- Small GitHub Issues
- Focused Jules-assisted pull requests
- CI-first development
- Readable human review comments
- Clear separation between AI agent work and maintainer ownership

## Recommended Project: `md-link-linter`

To demonstrate the workflow, Case Study B recommends building a minimalist Markdown link checker CLI tool.

**Description:** A command-line tool that scans Markdown files and reports internal or external links that need attention.

### Project Constraints

- **English-only:** All code, comments, issues, and documentation should be in English.
- **Small surface:** Focus on core functionality, such as parsing links and reporting status, rather than complex edge cases.
- **Testability:** The project should support automated unit tests for link parsing and reporting behavior.
- **Issue-sized tasks:** Issues should be small enough to be completed in focused PRs with limited file changes.

### Repository Name Options

- `md-link-linter`
- `link-check-mini`
- `simple-md-link-checker`

## First 5 Starter Issues for Jules

1. **Initialize CLI project structure:** Set up a basic project structure with a CLI entry point that accepts a file path and prints `Checking [file]...`.
2. **Implement Markdown link extractor:** Write a parser to extract Markdown-style links such as `[text](url)` from a given file.
3. **Add internal link validation:** Implement a check to verify that internal relative links, such as `./docs/setup.md`, point to existing files on disk.
4. **Add external link reporting:** Add basic status reporting for external links with a clear timeout policy.
5. **Implement summary reporter:** Add a final report to the CLI output showing the total number of links checked and the items that need attention.

## Expected PR Sequence

1. **PR 1: Scaffolding** — basic project structure, dependency management, and a minimal CLI.
2. **PR 2: Link extraction** — core parsing logic with unit tests.
3. **PR 3: Local checks** — file system existence checks for relative links.
4. **PR 4: External link reporting** — external link status reporting with timeout handling.
5. **PR 5: Reporting** — clear console output and summary behavior.

Each PR should follow the same sequence:

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

## CI Requirements

- **Linting:** Standard linting rules for the chosen language.
- **Tests:** Automated test suite running on every PR via GitHub Actions.
- **Documentation hygiene:** Markdown checks for the project's own documentation.

## Review Examples to Capture

- **Approval:** A review where the maintainer confirms the link parser handles the intended Markdown formats.
- **Change request:** A review where the maintainer asks Jules to add a timeout to external link reporting.
- **Refinement:** A review where the maintainer suggests a clearer error message for missing files.

## Completion Criteria

This planned brief can be replaced by the real case study once the following are met:

1. The separate repository is created and public.
2. At least 5 Jules-assisted PRs have been merged following the workflow.
3. The repository includes a clear README and CI status.
4. Representative issues, PR descriptions, CI runs, and human reviews are linked in the final case study document.

## Maintainer Notes

When this case study is selected, replace this planned brief with:

- repository link
- project summary
- selected issues
- representative Jules-assisted PRs
- review examples
- CI results
- lessons learned
