# [Jules Task] Update README with Architecture Diagram

## Problem
The current `README.md` describes the project structure in text, but it lacks a visual architecture diagram. This makes it harder for new contributors to understand how the components interact at a glance.

## Scope
- Create a simple Mermaid.js diagram representing the system architecture.
- Insert the diagram into `README.md` under the "Architecture" section.
- Ensure the diagram is rendered correctly in GitHub's preview.

## Non-goals
- Do not rewrite existing text in `README.md` unless necessary for the diagram placement.
- Do not add external image files; use Mermaid.js code blocks only.
- Do not change the underlying architecture.

## Acceptance Criteria
- [ ] `README.md` contains a Mermaid.js diagram.
- [ ] The diagram accurately reflects the current directory structure and data flow.
- [ ] Markdown hygiene passes (no trailing spaces, file ends with newline).

## Validation
- Use `read_file` to verify the Mermaid block is correctly formatted.
- Verify the position of the diagram in the document.

## Workflow Level
- Level 1 - Human-led Jules workflow
