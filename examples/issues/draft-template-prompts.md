## Problem
The future template repository needs a minimal set of reusable prompts to guide Jules through the default workflow (Issue → PR → Review → Merge). Currently, these are not consolidated or drafted specifically for template reuse.

## Scope
- Draft `prompts/issue-to-jules.md`: A concise handoff prompt for starting a task.
- Draft `prompts/pr-review.md`: A prompt for Jules to use when reviewing a PR (checking for scope, logic, and hygiene).
- Draft `prompts/maintainer-closeout.md`: A prompt for closing out a task, ensuring the issue is linked and final checks are done.
- Ensure all prompts frame Jules as an AI coding agent.
- Ensure prompts reinforce the standard workflow.

## Non-goals
- Do not add long speculative prompt libraries.
- Do not include private operations or secrets.
- Do not claim prompts replace human review.

## Acceptance Criteria
- [ ] `prompts/issue-to-jules.md` is drafted and concise.
- [ ] `prompts/pr-review.md` is drafted and focuses on quality checks.
- [ ] `prompts/maintainer-closeout.md` is drafted and covers the final merge/close steps.
- [ ] Prompts reinforce the human-led workflow.

## Validation
- Review the drafted prompts for clarity and alignment with `AGENTS.md`.
- Confirm Markdown hygiene passes for the new files.

## Workflow Level
Level 1 - Human-led Jules workflow
