# AGENTS.md

This repository is an AI Coding Workflow Starter Kit for Jules. It uses Jules as an AI coding agent inside a GitHub-native maintainer workflow.

Jules is not presented as a human contributor. The maintainer owns direction, architecture, review, and merge decisions unless a document is explicitly marked as an experiment.

## Default Operating Model

The recommended default workflow is:

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

All production-oriented work should follow this model.

## Rules for Jules

- Treat the GitHub Issue as the source of truth.
- Create small, focused pull requests.
- Link each PR to the originating issue.
- Do not modify unrelated files.
- Do not perform opportunistic refactors.
- State assumptions clearly when the issue is ambiguous.
- Include validation steps in the PR description.
- Respect CI failures and investigate root causes.
- Do not claim human authorship or human identity.
- Do not self-merge in the default workflow.

## Workflow Levels

This repository documents multiple workflow levels:

1. Human-led Jules workflow: recommended default.
2. Semi-autonomous Jules workflow: Jules may fix CI/review feedback, human still merges.
3. Human issue only: maintainer writes issue, Jules handles implementation and PR updates under strict CI.
4. Daily agentic maintainer loop: Jules reports project state, human steers direction.
5. No-human sandbox workflow: experiment only.
6. Jules + evaluator-driven evolution: experiment only.

Levels 1-4 may be documented as practical workflows. Levels 5-6 must be labeled as experiments and must not be presented as the default recommendation.

## Safety Rules for Experiments

Experimental automation must follow these rules:

- Use sandbox repositories or protected experiment branches.
- Require CI gates before any merge.
- Prefer auto-merge only when branch protection is configured.
- Keep logs, prompts, and evaluation results visible.
- Never hide that an AI coding agent performed the work.
- Do not present autonomous workflows as safer than human-reviewed workflows.

## Review Expectations

A reviewable Jules PR should answer:

```text
What issue does this solve?
What changed?
What did not change?
How was it validated?
What assumptions were made?
What should the human maintainer inspect carefully?
```

If the PR cannot answer those questions, it is not ready to merge.

## Project Philosophy

Most AI coding demos show only the final code. This repository shows the process.

The goal is not to prove that AI can replace maintainers. The goal is to show how a human maintainer can lead an AI coding agent through issues, PRs, reviews, CI, and controlled automation.
