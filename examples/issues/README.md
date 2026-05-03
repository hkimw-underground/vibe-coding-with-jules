# Example Issues for Jules

This directory contains concrete examples of how to write scoped, "Jules-ready" issues. These examples follow the standard `jules_task.yml` template.

## Why Scoped Issues Matter

Jules performs best when the problem and scope are clearly defined. A well-scoped issue:
- Reduces the risk of unrelated changes.
- Makes the PR easier for humans to review.
- Ensures CI can validate the specific change.

## Examples

- [Documentation Task](./docs-task.md): Adding or updating documentation.
- [CI/Tooling Task](./ci-task.md): Modifying GitHub Actions or local scripts.
- [Scoped Refactor Task](./refactor-task.md): Cleaning up code without changing behavior.
- [Template AGENTS Task](./template-agents-task.md): Drafting minimal rules for a template repository.
- [Template README Task](./template-readme-task.md): Drafting a copy-first README for a new repository.
- [Minimal PR Template Task](./pr-template-task.md): Drafting a reusable PR template.
- [Lightweight CI Task](./lightweight-ci-task.md): Adding minimal docs and template validation.
- [Case Study B Task](./case-study-b-task.md): Initializing an English-only sample project.
- [README Role Separation Task](./readme-role-separation.md): Improving top-level role separation for the Hub, Template, and Case Studies.
- [Fleet Queue Test Size Task](./fleet-queue-test-size-task.md): Adding a note about starting Fleet queue tests small before scaling.

## How to Use These Examples

You can copy the raw Markdown from these files and paste them into a new GitHub Issue, or use them as a reference when filling out the `Jules task` issue template in your own repository.
