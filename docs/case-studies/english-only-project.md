# Case Study B: English-Only Project Brief

Status: Actionable Project Plan

This document serves as an actionable plan for creating Case Study B: a clean, English-only open-source project that demonstrates the Jules-assisted workflow for a global audience.

## Project Overview

### Recommended Repository Name
`md-link-linter`

### Repository Name Options
- `md-link-linter` (Recommended)
- `link-check-mini`
- `simple-md-link-checker`

### Project Goal
To build a minimalist Markdown link checker CLI tool that scans `.md` files and reports internal (local) and external (web) links that need attention.

### Target Audience
- Global open-source contributors and maintainers.
- Developers looking for a clean example of AI-assisted engineering.
- Students and teachers who need an English-only reference for the Jules workflow.

### Why This Case Study Exists
Case Study A (Digital Logic) is tied to a specific hardware/software capstone. Case Study B exists to show that the starter kit's workflow is reusable for any software project, emphasizing clarity and English-only collaboration for global readability.

### What It Demonstrates
- **Jules as an AI Coding Agent:** Jules handles implementation while the human maintainer leads architecture and review.
- **GitHub-Native Workflow:** Strict adherence to `Issue → Jules Task → Pull Request → CI → Human Review → Merge`.
- **Small, Scoped Issues:** Breaking down a project into tasks that an AI can handle with high quality and low noise.
- **Visible Engineering History:** Readable PR descriptions, clear CI status, and meaningful human review comments.

---

## Technical Plan

### Initial Repository Structure
```text
.
├── AGENTS.md (copied from starter kit)
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── main.py (or index.ts/main.go)
│   └── parser.py
├── tests/
├── docs/
├── README.md
├── LICENSE
└── requirements.txt (or package.json/go.mod)
```

### CI Plan
- **Linting:** Standard style checks for the chosen language.
- **Unit Tests:** Automated test suite running on every PR via GitHub Actions.
- **Markdown Hygiene:** Use the same script from this starter kit to validate the project's own docs.

### Review Plan
- **Architecture Review:** Maintainer ensures the logic for link extraction and validation is sound.
- **Quality Review:** Maintainer checks for edge cases (e.g., malformed URLs, missing files).
- **Workflow Review:** Maintainer verifies that Jules followed the PR template and linked the correct issue.

---

## First 5 GitHub Issues

### Issue 1: Initialize Project Scaffolding
- **Goal:** Set up the basic project structure and a "Hello World" CLI.
- **Scope:** Create `AGENTS.md`, `.github/` templates, a minimal `main` script, and a `README.md`.
- **Jules Workflow:** Jules initializes files and opens a PR showing the scaffold.
- **Validation:** Run the CLI and confirm it prints a start message.

### Issue 2: Implement Markdown Link Extraction
- **Goal:** Parse `[text](url)` patterns from a Markdown file.
- **Scope:** Create a parser module and unit tests with various link formats.
- **Jules Workflow:** Jules writes the extraction logic and tests.
- **Validation:** Tests pass for standard, relative, and absolute links.

### Issue 3: Add Internal Link Validation
- **Goal:** Verify that relative links point to actual files on disk.
- **Scope:** Implement file existence checks for links starting with `./` or `../`.
- **Jules Workflow:** Jules adds the filesystem check logic and updates tests.
- **Validation:** Tool reports failure for a link to a non-existent file.

### Issue 4: Add External Link Reporting
- **Goal:** Check if external URLs return a successful status code.
- **Scope:** Add a basic HTTP client check with a short timeout.
- **Jules Workflow:** Jules implements the network check and handles timeouts.
- **Validation:** Tool flags broken URLs (e.g., 404) while respecting the timeout.

### Issue 5: Implement Summary Reporter
- **Goal:** Provide a clear console output with results.
- **Scope:** Add a summary showing: Total links, Passed, Failed (with reasons).
- **Jules Workflow:** Jules formats the output and adds final CLI refinements.
- **Validation:** CLI output is readable and useful for CI/manual runs.

---

## Acceptance Criteria for the Case Study
1. The separate `md-link-linter` repository is public.
2. At least 5 Jules-assisted PRs have been merged following the **Review-Driven** track.
3. Jules is clearly framed as an **AI coding agent** in all PRs and the `AGENTS.md` file.
4. **Human maintainer ownership** is explicit in every merge and review comment.
5. The case study document in this repo is updated with links to the live project.

---

## Management

### Non-Goals
- Building a "perfect" or "production-grade" link checker with complex edge case handling.
- Claiming Jules can work without human review.
- Adding non-English documentation or comments.
- Using promotional language or seeking stars for the demo repo.

### Risks and Mitigations
- **Risk:** Jules makes logical errors in link parsing.
  - **Mitigation:** Maintainer review is mandatory; unit tests must cover edge cases.
- **Risk:** External link checks make CI slow or flaky.
  - **Mitigation:** Implement strict timeouts and allow the tool to run in "local-only" mode.
- **Risk:** The demo repo becomes stale.
  - **Mitigation:** Keep the scope small so it can be completed and "frozen" as a successful example.

### Connection to Starter Kit
This project uses the exact `AGENTS.md`, issue templates, and workflow tracks defined in the **AI Coding Workflow Starter Kit**. It serves as the primary "living example" for global users who want to see the kit in action.
