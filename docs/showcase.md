# Showcase

A copy-first overview for using this starter kit in your own repository.

## What this is

AI Coding Workflow Starter Kit for Jules is a GitHub-native playbook for running Jules-assisted work through issues, pull requests, reviews, CI, and maintainer-controlled workflow tracks.

The goal is simple: make AI-assisted coding work leave a readable project history instead of a private prompt trail.

## Who it is for

This starter kit is designed for:

- students learning GitHub collaboration
- teachers running project-based classes
- first-time maintainers setting up a small repository
- documentation contributors and translators
- developers experimenting with Jules inside normal GitHub practice

## Copy these files first

Start by copying the smallest useful set into your own repository.

| File or directory | Why copy it |
| --- | --- |
| `AGENTS.md` | Gives Jules repository-specific rules, boundaries, and workflow expectations. |
| `.github/ISSUE_TEMPLATE/` | Provides scoped issue templates for Jules tasks, workflow experiments, and translations. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Keeps PRs tied to issues, validation notes, and human review. |
| `.github/workflows/docs-and-templates.yml` | Adds a lightweight CI example for checking docs and starter kit structure. |
| `prompts/` | Gives maintainers reusable handoff and reporting prompts. |
| `examples/` | Provides example issues and PR review comments that can be adapted. |

You do not need to copy everything at once. Start with the default Review-Driven workflow, then add more guides only when your project needs them.

## Default workflow

The recommended default is Review-Driven:

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

In this workflow, the maintainer owns scope, architecture, validation, and the final merge decision. Jules assists with implementation or documentation work through the GitHub workflow.

## Choose a track

| Track | Use it when |
| --- | --- |
| [Review-Driven](./tracks/review-driven.md) | You want the safest default path for real projects and classrooms. |
| [GitHub-Native Collaboration](./tracks/github-native-collaboration.md) | You want to teach or learn Issues, PRs, reviews, CI, labels, and branch protection. |
| [Half Vibe Coding](./tracks/half-vibe-coding.md) | You want Jules to execute between maintainer checkpoints. |
| [Full Vibe Coding](./tracks/full-vibe-coding.md) | You are running a sandbox experiment with minimal human involvement. |

Full Vibe Coding is experimental. Use it in sandbox repositories or protected branches, not as the default path for production work.

## For contributors

Contributors are not required to use Jules.

Useful starting points:

- [First Contributions Guide](./contributing/first-contributions.md)
- [Translation Guide](./contributing/translations.md)
- [Jules Web UI Guide](./jules-web-ui.md)

Translation contributors are welcome. Keep technical meaning, links, filenames, and code blocks accurate unless the change is intentional and explained in the PR.

## Next step

Read the [Quickstart Guide](./quickstart.md) or the [Applied Repository Rollout Guide](./operations/apply-to-existing-repo.md), copy the starter files you need, and open one small issue before asking Jules to work.

Jules is an AI coding agent, not a human contributor. Human maintainers remain responsible for review, validation, and merge decisions.
