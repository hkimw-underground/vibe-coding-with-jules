# [Docs] Improve hub README first-screen role separation

## Problem

The current `README.md` (and `README.ko.md`) first screen does not clearly distinguish between the different roles in the ecosystem:
1. This repository (`hkimw-underground/vibe-coding-with-jules`) acts as the **Hub/Playbook**.
2. A future repository will be the **copy-first template** for easy adoption.
3. **Case Study A** (`hkimw-underground/digital-logic-circuit`) is a real applied example.
4. **Case Study B** is an actionable plan for a small project.

The README currently makes the hub look like a minimal template, which can be confusing for new users looking for either the documentation or the starter files.

## Scope

Improve the top section of `README.md` and `README.ko.md` to clarify these roles:
- Add a **one-line repository role** (e.g., "The central playbook and ecosystem hub for the Jules AI coding workflow").
- Create a clear **"Start here" path** that directs users based on their goal (e.g., "I want to learn the workflow" -> Playbook, "I want to start a new project" -> Template Repo).
- Add **link placeholders** for the template repository (to be filled when available).
- Mention **Case Study A** prominently but concisely on the first screen to show the workflow in action.
- Ensure the core message remains central: "Most AI coding demos show only the final code. This project shows the process."

## Non-goals

- Do not rewrite the full README.
- Do not add star-begging or hype language.
- Do not add marketing-heavy "awesome list" mentions.
- Do not change any GitHub Action workflow files.

## Acceptance Criteria

- [ ] The top section of the README clearly identifies the repo's role as a "Hub/Playbook".
- [ ] A "Start here" path is visible on the first screen.
- [ ] Placeholders for the future template repo are included.
- [ ] Case Study A is mentioned concisely.
- [ ] The tagline "Most AI coding demos show only the final code. This project shows the process." is preserved.
- [ ] Markdown hygiene and bilingual alignment (EN/KO) are maintained.

## Validation

- Run local Markdown hygiene checks.
- Verify visual separation on the first screen.

## Workflow Level

- Level 1 - Human-led Jules workflow
