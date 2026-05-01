# GitHub-Native Collaboration Track

This track is designed for learning how to work with Jules through professional GitHub teamwork. It keeps Jules framed as an AI coding agent operating inside the standard GitHub flow.

## What it is

A structured, teaching-friendly workflow that uses GitHub's native features — Issues, Pull Requests, Reviews, Labels, CI, and branch protection — to guide AI-assisted work.

## Who it is for

- Students learning modern software engineering practices.
- Teachers looking for a repeatable model for AI-assisted education.
- First-time maintainers who want to build a clean project history.

## Human Involvement Level

**High.** The human maintainer acts as project lead, providing clear specifications and detailed feedback on every PR.

## Recommended Use Cases

- Educational projects and bootcamps.
- Open-source projects teaching GitHub collaboration.
- Small teams establishing their first AI-assisted workflow.

## Workflow Summary

1. **Issue:** Human creates a well-scoped issue.
2. **Task:** Jules works from the issue as the source of truth.
3. **Draft PR:** Jules opens a PR to show progress.
4. **Review:** Human provides feedback through PR comments.
5. **Iteration:** Jules updates the PR based on feedback.
6. **Merge:** Human performs a final review and merges.

## Safety Notes

- Use branch protection rules to prevent direct pushes to `main`.
- Ensure CI runs on every pull request.
- Review Jules-assisted changes with the same care you would apply to any untrusted code contribution.

## When not to use it

- Highly experimental sandbox environments where speed is prioritized over process.
- Trivial, one-off scripts where a full PR cycle is unnecessary.
