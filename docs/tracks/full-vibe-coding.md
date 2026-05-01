# Full Vibe Coding Track (Experimental)

Full Vibe Coding is an experimental sandbox workflow where human intervention is minimized to observe how Jules handles end-to-end development.

## What it is
A high-autonomy, experimental mode. It is used to test the limits of what Jules can accomplish when given broad objectives and automated feedback loops.

## Who it is for
- Workflow researchers and AI engineers.
- Maintainers building "autonomous" experimental prototypes.
- Educational demonstrations of AI agent capabilities.

## Human Involvement Level
**Very Low.** Humans act primarily as observers or high-level objective setters.

## Recommended Use Cases
- Sandbox repositories.
- Non-production experiment branches.
- Researching AI agent behaviors and failure modes.

## Workflow Summary
1. **Objective:** Human sets a broad goal (e.g., "Build a CLI that does X").
2. **Loop:** Jules creates issues, implements code, runs tests, and potentially auto-merges into an experiment branch.
3. **Observability:** Humans monitor logs or progress reports.
4. **Audit:** A final human audit is performed on the resulting artifact.

## Safety Notes
- **WARNING:** Do not use this track on production branches or repositories with sensitive data.
- Requires sandboxing (e.g., dedicated containers or limited API keys).
- Auto-merge must be restricted to non-critical branches.

## When not to use it
- Production codebases.
- Any project where reliability and security are primary requirements.
- Public repositories where unvetted AI code could cause harm or reputational damage.
