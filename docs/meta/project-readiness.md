# Project Readiness

**The AI Coding Workflow Starter Kit for Jules** is a GitHub-native starter kit for leading AI coding agents through normal engineering practices.

## What this project provides

This repository provides reusable templates, review checklists, CI constraints, and examples needed to establish a verifiable issue-to-merge workflow for AI agents.

## How it differs from a prompt dump

Rather than providing isolated instructions or large prompts for a single IDE interaction, this kit embeds guidance into standard GitHub mechanisms: issues, pull requests, automated CI checks, and human code reviews. It demonstrates the verifiable process of writing code, not just the final outcome.

## Quality Checklist

- [x] Scoped issue templates for agent tasks
- [x] Pull request templates requiring linked issues and validation notes
- [x] Lightweight CI checks for Markdown and YAML hygiene
- [x] Reusable starter kit files (`AGENTS.md`, `.github/`)
- [x] Examples of issues and PR reviews
- [x] Case studies documenting real-world workflow usage

## Current Limitations

- Automation is deliberately constrained; human review remains mandatory for merging.
- High-level architectural and design decisions are out of scope for the agent and must be provided by the human maintainer.
- Advanced autonomous workflows (like evaluator-driven evolution) are strictly experimental and isolated from production branches.

## Resources

- [Quickstart Guide](../quickstart.md)
- [Example Issues](../../examples/issues/README.md) and [PR Reviews](../../examples/pr-reviews/README.md)
- [Workflow Levels](../workflows/workflow-levels.md)
- [Case Studies](../case-studies/digital-logic-circuit.md)

*Note: The default workflow in this starter kit remains human-led. Jules is an AI coding agent, and human maintainers are responsible for defining the scope, guiding direction, and approving the final work.*
