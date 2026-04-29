# Workflow Levels

This starter kit separates practical maintainer workflows from experimental automation.

## Level 1: Human-led Jules Workflow

Recommended default.

```text
Human creates issue
→ Jules implements
→ Jules opens PR
→ CI runs
→ Human verifies
→ Human merges
```

Use this when the project is public, important, or still defining its architecture.

## Level 2: Semi-autonomous Jules Workflow

```text
Human creates issue
→ Jules implements
→ Jules opens PR
→ CI runs
→ Jules fixes CI or review feedback
→ Human final review
→ Human merges
```

This is useful when the task is well-scoped and validation is clear.

## Level 3: Human Issue Only

```text
Human creates issue
→ Jules implements
→ Jules updates PR until checks pass
→ auto-merge or human merge after required gates
```

Use only with strict CI and branch protection.

## Level 4: Daily Agentic Maintainer Loop

```text
Jules or automation summarizes project state
→ proposes next tasks
→ human maintainer redirects priority
→ Jules executes selected task
```

This workflow is for direction-setting, not blind autonomy.

## Level 5: No-human Sandbox Workflow

Experiment only.

```text
Agent creates issue
→ Jules implements
→ Jules verifies
→ auto-merge after required checks
```

Run this only in a sandbox repository or protected experiment branch.

## Level 6: Jules + Evaluator-driven Evolution

Experiment only.

```text
Evaluator defines score
→ evolution loop generates candidates
→ best candidate becomes issue or PR
→ Jules cleans up implementation
→ CI validates
→ human reviews
```

This works best for measurable optimization targets, not vague product direction.

## Rule of Thumb

The more autonomous the workflow becomes, the stronger the safety gates must be.

```text
More autonomy → smaller scope → stronger CI → clearer rollback path
```
