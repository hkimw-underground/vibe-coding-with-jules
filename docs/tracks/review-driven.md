# Review-Driven Track (Recommended Default)

The Review-Driven track is the standard, production-ready workflow for the Jules Starter Kit. It balances productivity with rigorous safety and quality control.

## What it is
The "Golden Path" for working with Jules. It mandates human review for every single line of code before it reaches the main branch.

## Who it is for
- Professional developers and maintainers.
- Production-grade repositories.
- Anyone who wants the safest and most reliable experience with Jules.

## Human Involvement Level
**Medium-High.** Humans define the tasks and review the results, but Jules handles the heavy lifting of implementation.

## Recommended Use Cases
- Production applications.
- Complex feature development.
- Bug fixes in critical systems.

## Workflow Summary
1. **Issue:** Human creates a focused task.
2. **Implementation:** Jules works on the task and opens a PR.
3. **Automated Checks:** CI validates the PR (tests, linting, hygiene).
4. **Human Review:** A human maintainer reviews the PR and requests changes if needed.
5. **Final Approval:** Human merges only after CI passes and review is satisfied.

## Safety Notes
- This is the safest workflow for production environments.
- Human review is the primary safeguard against AI hallucinations or regressions.
- CI acts as a secondary gate for hygiene and regression testing.

## When not to use it
- In "Full Vibe" experimental sandboxes where you are intentionally removing human gates.
