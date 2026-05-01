# Case Study B: English-Only Open Source Project

Status: actionable plan.

This case study defines a clean English-only open-source project that can demonstrate the same Jules workflow shown in this starter kit.

Case Study B is intentionally small. The goal is not to build a large product. The goal is to create a readable public history of issues, Jules-assisted pull requests, CI checks, and human maintainer reviews.

## Purpose

Case Study B exists to show that the workflow is reusable outside a school or capstone context, specifically for a global audience using English as the primary language for code, documentation, and collaboration.

It should demonstrate:

- Small GitHub Issues
- Focused Jules-assisted pull requests
- CI-first development
- Readable human review comments
- Clear separation between AI agent work and maintainer ownership
- A complete project history that new readers can understand quickly

## Target Audience

This case study is designed for:

- developers evaluating Jules-assisted GitHub workflows
- students learning issue-driven development
- teachers looking for a small classroom-friendly example
- maintainers who want to keep AI-assisted work reviewable
- contributors who want to understand how the starter kit works in a real repository

## Repository Name Options

- `md-link-linter`
- `link-check-mini`
- `simple-md-link-checker`
- `tiny-md-link-audit`
- `markdown-link-lab`

## Recommended Project: `md-link-linter`

The recommended Case Study B project is `md-link-linter`.

**Description:** A small command-line tool that scans Markdown files and reports links that need attention.

This project is a good fit because it is:

- easy to understand without domain-specific knowledge
- small enough for issue-sized Jules tasks
- testable with unit tests and fixture files
- useful enough to feel real
- documentation-friendly for global readers

## Project Goal

Build a minimal Markdown link checker CLI that can:

1. accept one or more Markdown file paths
2. extract Markdown links such as `[text](target)`
3. check local relative links against the filesystem
4. report external links without making the project depend on complex crawling behavior
5. print a clear summary that can be tested in CI

## What This Case Study Demonstrates

The case study should demonstrate the Review-Driven workflow as the default path:

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

The maintainer owns scope, architecture, validation, review, and merge decisions. Jules is an AI coding agent that assists with implementation inside the GitHub workflow.

The final case study should show:

- how issues are scoped before Jules starts work
- how PRs stay focused
- how CI catches regressions
- how the maintainer requests changes
- how review comments preserve architecture and quality boundaries
- how a small project can grow through traceable GitHub history

## Initial Repository Structure

A simple starting structure is enough:

```text
.
├── README.md
├── LICENSE
├── pyproject.toml
├── src/
│   └── md_link_linter/
│       ├── __init__.py
│       ├── cli.py
│       ├── parser.py
│       ├── checker.py
│       └── reporter.py
├── tests/
│   ├── fixtures/
│   │   ├── basic-links.md
│   │   └── broken-local-link.md
│   ├── test_parser.py
│   ├── test_checker.py
│   └── test_reporter.py
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        └── ci.yml
```

Python is a practical default because the repository can stay small, tests are easy to run in CI, and the source layout is readable for students and first-time contributors.

## First 5 GitHub Issues

### Issue 1: Initialize CLI project structure

**Goal:** Set up the repository structure, package metadata, and a minimal CLI entry point.

**Expected Jules workflow:** Jules creates the basic project files and a simple command that accepts a path and prints a predictable message.

**Validation:** CI runs a smoke test for the CLI entry point.

### Issue 2: Implement Markdown link extractor

**Goal:** Extract Markdown-style inline links such as `[text](target)` from a file.

**Expected Jules workflow:** Jules adds parser logic and unit tests using Markdown fixture files.

**Validation:** Tests cover normal links, multiple links, and files with no links.

### Issue 3: Add internal link validation

**Goal:** Check whether relative links point to existing local files.

**Expected Jules workflow:** Jules adds filesystem validation behind a small interface and updates tests.

**Validation:** Tests cover valid local links, missing files, and links that should be ignored.

### Issue 4: Add external link reporting policy

**Goal:** Classify external links and report them clearly without building a complex crawler.

**Expected Jules workflow:** Jules adds conservative reporting behavior and documents what is and is not checked.

**Validation:** Tests confirm external links are detected and reported separately from local links.

### Issue 5: Implement summary reporter

**Goal:** Print a final report showing total links checked, local failures, external links, and files scanned.

**Expected Jules workflow:** Jules adds reporter logic and updates CLI output tests.

**Validation:** Tests assert stable output for fixture files.

## Expected PR Sequence

1. **PR 1: Scaffolding** — basic project structure, dependency management, CI, and a minimal CLI.
2. **PR 2: Link extraction** — core parsing logic with unit tests.
3. **PR 3: Local checks** — filesystem existence checks for relative links.
4. **PR 4: External link reporting** — conservative external link reporting policy.
5. **PR 5: Summary output** — clear console output and summary behavior.

Each PR should include:

- linked issue
- short summary
- validation steps
- CI results
- maintainer review decision

## CI Plan

The sample repository should use GitHub Actions from the first PR.

Minimum CI:

- install dependencies
- run unit tests
- run linting or formatting checks if configured
- run Markdown hygiene checks for documentation

Keep CI small. The goal is fast feedback, not a complex release pipeline.

## Review Plan

The maintainer should review each Jules-assisted PR for:

- whether the PR follows the linked issue
- whether the diff is small enough to review
- whether tests prove the intended behavior
- whether architecture boundaries stay simple
- whether CI passes without weakening checks
- whether the PR introduces unrelated refactors

Useful review examples to capture:

- **Approval:** The maintainer confirms the parser handles the intended Markdown formats.
- **Change request:** The maintainer asks Jules to split unrelated behavior into a separate issue.
- **Validation request:** The maintainer asks for a missing fixture or test case.
- **Safety boundary:** The maintainer rejects broad external network checking until the scope is better defined.

## Acceptance Criteria for the Case Study

The planned brief can be replaced by a real case study once:

1. The separate repository is created and public.
2. The repository is English-only.
3. At least five focused issues are opened.
4. At least five Jules-assisted PRs are merged through the Review-Driven workflow.
5. Each merged PR includes CI evidence and human maintainer review.
6. The repository README explains the project and links back to this starter kit.
7. The final case study document links representative issues, PRs, CI runs, and review comments.

## Non-goals

This case study should not:

- become a large application
- demonstrate fully autonomous production merging
- require complex external network crawling
- replace human maintainer review
- present Jules as a human contributor
- depend on private repositories or private data
- optimize for feature count over process clarity

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| The project becomes too large | Keep the first milestone limited to five issues. |
| PRs become hard to review | Enforce one issue per PR and request changes when scope expands. |
| External link checking becomes flaky | Treat external links as a reporting category first; avoid network-heavy behavior in early PRs. |
| The case study looks like a toy | Keep the tool small but real: CLI, tests, fixtures, CI, and documented behavior. |
| Jules output is treated as automatically correct | Require human review, CI evidence, and validation notes on every PR. |

## Connection Back to This Starter Kit

The Case Study B repository should copy or adapt:

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/PULL_REQUEST_TEMPLATE.md`
- a lightweight GitHub Actions workflow
- relevant prompts from `prompts/`
- review examples from `examples/pr-reviews/`

The case study should link back to:

- [Quickstart](../quickstart.md)
- [Showcase](../showcase.md)
- [Review-Driven Track](../tracks/review-driven.md)
- [Jules Web UI Guide](../jules-web-ui.md)

## Maintainer Notes

When the real case study is created, replace this plan with:

- repository link
- project summary
- selected issues
- representative Jules-assisted PRs
- review examples
- CI results
- lessons learned

Until then, this document should remain an actionable plan for creating the English-only sample repository.
