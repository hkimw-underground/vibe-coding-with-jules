# GitHub-Native Collaboration Track

This track is designed for learning how to work with Jules in a way that mirrors professional engineering teamwork. It treats Jules as a managed contributor within the standard GitHub flow.

## What it is
A structured, pedagogical workflow that emphasizes the use of GitHub's native features—Issues, Pull Requests, and Reviews—to direct and mentor Jules.

## Who it is for
- Students learning modern software engineering practices.
- Teachers looking for a repeatable model for AI-assisted education.
- First-time maintainers who want to build a clean project history.

## Human Involvement Level
**High.** The human maintainer acts as a mentor and technical lead, providing clear specifications and detailed feedback on every PR.

## Recommended Use Cases
- Educational projects and bootcamps.
- Open-source projects looking to onboard new maintainers.
- Small teams establishing their first AI-assisted workflow.

## Workflow Summary
1. **Issue:** Human creates a well-scoped issue.
2. **Task:** Jules is assigned to the issue.
3. **Draft PR:** Jules opens a Draft PR early to show progress.
4. **Review:** Human provides feedback via PR comments.
5. **Iteration:** Jules updates the PR based on feedback.
6. **Merge:** Human performs a final review and merges.

## Safety Notes
- Always use Branch Protection rules to prevent direct pushes to `main`.
- Ensure CI runs on every Pull Request.
- Treat Jules's code with the same (or more) scrutiny as a human intern's code.

## When not to use it
- In highly experimental "sandbox" environments where speed is prioritized over process.
- For trivial, one-off scripts where a full PR cycle is overkill.
