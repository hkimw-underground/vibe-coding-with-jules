# Project Readiness Checklist

This document provides a concise overview of the repository's current state, quality standards, and planned improvements. It helps maintainers and readers understand the project's maturity and focus.

## Project Summary
A GitHub-native starter kit for leading the Jules AI coding agent through a structured engineering process of issues, pull requests, and human review.

## What This Project Provides
- **Scoped Issue Templates**: Pre-configured templates for Jules tasks and workflow experiments.
- **PR Templates**: Standardized pull request format with validation checklists.
- **Workflow Levels**: A framework for transitioning from human-led tasks to experimental automation.
- **Reference Examples**: Real-world examples of issues and maintainer reviews.
- **CI Validation**: Automated checks for Markdown hygiene, YAML syntax, and repository structure.
- **Reusable Prompts**: Templates for handoffs and status reporting.

## Why This is Not a Prompt Dump
Unlike collections of "magic prompts," this project focuses on the **engineering process**. It treats AI as a contributor within a standard Git-based workflow. The goal is not just to generate code, but to create a readable, auditable, and maintainable engineering history where human maintainers retain control and accountability.

## Quality Checklist
- [x] **Core Documentation**: README and Quickstart guide are complete and up-to-date.
- [x] **Bilingual Support**: Key documentation (README) is available in both English and Korean.
- [x] **Structural Integrity**: A dedicated CI workflow ensures all required starter kit files are present.
- [x] **Validation Gates**: Markdown and YAML syntax checks are enforced for all contributions.
- [x] **Real-World Evidence**: Case studies demonstrate the workflow's application in practical scenarios.
- [x] **Community Standards**: Includes Code of Conduct, Contributing guidelines, and Security policy.

## Current Limitations
- **Case Study B (English-Only)**: Currently planned and documented as a placeholder.
- **Advanced Workflow Levels**: Levels 4-6 (e.g., daily agentic maintainer loop, no-human sandbox) are considered experimental and should not be used in production environments.
- **Automation Scope**: The project intentionally avoids "auto-merge" or "auto-fix" automation to prioritize human oversight.

## Key Resources
- **[Quickstart Guide](../quickstart.md)**: Step-by-step onboarding for your first Jules task.
- **[Reference Examples](../../examples/)**: Scoped issues and PR review examples.
- **[Workflow Levels](../workflows/workflow-levels.md)**: Detailed breakdown of the six levels of AI integration.
- **[Case Studies](../case-studies/)**: Analysis of the workflow applied to real-world projects.

## Human-Led by Default
The default and recommended workflow for this project remains **Level 1: Human-led Jules workflow**. A human maintainer is responsible for creating issues, reviewing every pull request, and making final merge decisions. Jules is a tool to assist, not a replacement for human engineering judgment.
