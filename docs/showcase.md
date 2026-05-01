# Showcase

## What this is

A GitHub-native playbook and starter kit for working with Jules, an AI coding agent, leaving a readable engineering history.

## Who it is for

Students, teachers, first-time maintainers, and small teams who want to incorporate AI assistance while maintaining high engineering standards and human oversight.

## Copy these files first

1. **`AGENTS.md`**: Sets the rules for Jules, establishing its identity as an AI agent and not a human contributor.
2. **`.github/ISSUE_TEMPLATE/`**: Provides the structural input needed by Jules to understand and execute tasks effectively.
3. **`.github/PULL_REQUEST_TEMPLATE.md`**: Enforces accountability, validation notes, and human review expectations for every merged PR.
4. **`.github/workflows/docs-and-templates.yml`**: Contains baseline CI checks for markdown and yaml formats.
5. **`prompts/`**: Gives helpful predefined instructions to initialize handoffs and summaries.
6. **`examples/`**: Offers examples of issues and PR reviews to model good practices.

## Default workflow

This repository recommends the **Review-Driven** workflow:

`Issue → Jules task → Pull request → CI → Human review → Merge`

## Choose a track

- **Review-Driven:** The default for real projects. You guide, Jules acts, CI tests, and you review.
- **GitHub-Native Collaboration:** Learn how to collaborate using Issues, PRs, and Labels. Great for education.
- **Half Vibe Coding:** Lower touch. You set the direction, and Jules operates semi-autonomously between check-ins.
- **Full Vibe Coding:** For sandbox experiments only. High automation, minimal human oversight.

## For contributors

Jules is an AI coding agent, not a human contributor. Maintainers must always retain control and understanding over their repository. If you'd like to get involved:

- Read the **[Quickstart Guide](./quickstart.md)** to copy the starter kit.
- Read the **[First Contributions Guide](./contributing/first-contributions.md)** to see where to help.

## Next step

Human maintainers own the final review, architecture, and merge decisions. Try opening a small, well-scoped GitHub issue and use Jules to resolve it, ensuring a human always approves the pull request.
