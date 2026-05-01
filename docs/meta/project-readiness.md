# Project Readiness Checklist

This document provides a concise overview of the repository's current state, quality standards, and planned improvements. It helps maintainers and readers understand the project's maturity and focus.

## Project Summary

A GitHub-native starter kit for leading the Jules AI coding agent through a structured engineering process of issues, pull requests, CI, and human review.

## What This Project Provides

- **Scoped Issue Templates**: Pre-configured templates for Jules tasks and workflow experiments.
- **PR Templates**: Standardized pull request format with validation checklists.
- **Workflow Levels**: A framework for moving from human-led tasks to controlled automation experiments.
- **Reference Examples**: Copyable examples of issues and maintainer reviews.
- **CI Validation**: Automated checks for Markdown hygiene, YAML syntax, and repository structure.
- **Reusable Prompts**: Templates for handoffs and status reporting.

## Why This Is Not a Prompt Dump

Unlike collections of "magic prompts," this project focuses on the **engineering process**. It treats Jules as an AI coding agent operating inside a standard GitHub workflow. The goal is not just to generate code, but to create a readable, auditable, and maintainable engineering history where human maintainers retain control and accountability.

## Quality Checklist

- [x] **Core Documentation**: README and Quickstart guide are complete and up-to-date.
- [x] **Bilingual Support**: Key README documentation is available in both English and Korean.
- [x] **Structural Integrity**: A dedicated CI workflow ensures all required starter kit files are present.
- [x] **Validation Gates**: Markdown and YAML syntax checks run for documentation and template changes.
- [x] **Practical Evidence**: Case Study A documents the workflow in a real project, while Case Study B provides an actionable project plan for global audiences.
- [x] **Community Standards**: Includes Code of Conduct, contributing guidelines, license, and security policy.

## Current Limitations

- **Case Study B (English-Only)**: While the plan is actionable, the separate demonstration repository is yet to be created.
- **Advanced Workflow Levels**: Levels 4-6, such as daily maintainer reports and sandbox-only automation experiments, are intentionally documented as advanced or experimental.
- **Automation Scope**: The default workflow does not recommend auto-merge or unattended project changes. Automation should remain gated by CI, branch protection, and human review unless it is explicitly isolated in a sandbox.

## Key Resources

- **[Quickstart Guide](../quickstart.md)**: Step-by-step onboarding for your first Jules task.
- **[Reference Examples](../../examples/)**: Scoped issues and PR review examples.
- **[Workflow Levels](../workflows/workflow-levels.md)**: Detailed breakdown of the six workflow levels.
- **[Case Studies](../case-studies/)**: Workflow examples and planned case study material.

## Human-Led by Default

The default and recommended workflow for this project remains **Level 1: Human-led Jules workflow**. A human maintainer is responsible for creating issues, reviewing every pull request, and making final merge decisions. Jules is an AI coding agent that assists the workflow, not a replacement for human engineering judgment.
