# Jules + Evaluator-driven Evolution

This is an experimental workflow inspired by AlphaEvolve-style systems and open evolutionary coding loops.

The goal is not to let an agent freely redesign a project. The goal is to combine measurable evaluators with Jules-managed GitHub work.

## Intended Pipeline

```text
Human defines objective
→ evaluator or benchmark scores candidate changes
→ evolution loop searches for variants
→ best candidate becomes a GitHub Issue or PR
→ Jules cleans up implementation
→ CI validates
→ human maintainer reviews
```

## Role Split

```text
Evaluator-driven evolution = candidate search / optimization
Jules = GitHub-native implementation and cleanup
Human maintainer = objective, constraints, review, merge decision
```

## Good Targets

Use this only when success can be measured.

Good examples:

- benchmark performance
- test coverage improvement
- lint/format convergence
- deterministic output quality metrics
- small algorithmic optimization tasks

Bad examples:

- vague UX improvement
- architecture direction
- branding decisions
- large product rewrites
- security-sensitive logic

## Required Artifacts

Each experiment should produce:

- objective definition
- evaluator command
- baseline score
- candidate score
- changed files
- PR summary
- CI result
- maintainer notes

## Safety Rule

No evaluator-driven workflow should merge directly into the default branch without human review unless it is running in a sandbox with strict branch protection and a documented rollback path.
