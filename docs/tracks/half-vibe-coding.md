# Half Vibe Coding Track

Half Vibe Coding is an advanced workflow that allows Jules more autonomy while maintaining periodic human checkpoints to ensure the project stays on track.

## What it is
A "low-touch" workflow where Jules handles multiple related tasks or more complex implementations with less frequent human intervention than the Review-Driven track.

## Who it is for
- Experienced maintainers who have established trust in Jules's performance on a specific codebase.
- Projects with very strong CI and automated test suites.
- Rapid prototyping where the architecture is already well-defined.

## Human Involvement Level
**Low-Medium.** Humans provide high-level direction and perform final audits rather than step-by-step guidance.

## Recommended Use Cases
- Iterative improvements on established features.
- Large-scale refactors where the goal is clearly defined by existing tests.
- Internal tools with lower risk profiles.

## Workflow Summary
1. **Strategic Issue:** Human defines a broader goal or a sequence of tasks.
2. **Autonomous Execution:** Jules works through the tasks, potentially opening and updating multiple PRs.
3. **Continuous CI:** The project relies heavily on CI to catch regressions in real-time.
4. **Periodic Audit:** Human reviews the overall progress at key milestones.
5. **Batch Merge:** Human merges batches of verified changes.

## Safety Notes
- Requires a comprehensive test suite (high code coverage) to be safe.
- Not recommended for junior developers or new projects without established patterns.
- Human "eyes-on" is still required before major releases.

## When not to use it
- New architecture or security-sensitive code.
- Public-facing repositories without strict branch protection.
