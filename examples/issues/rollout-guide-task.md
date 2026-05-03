# [Jules Task] Add applied repository rollout guide

## Problem

The starter kit explains how to use Jules workflows inside a repository, but it should also explain how to apply the starter kit to an existing real project. This guide is needed to help maintainers transition from using the playbook to applying it in their own domain.

This task is a recreation of [vibe-coding-with-jules #95](https://github.com/hkimw-underground/vibe-coding-with-jules/issues/95).

## Scope

Create:

- `docs/operations/apply-to-existing-repo.md`

Update if useful:

- `README.md`
- `README.ko.md`
- `docs/showcase.md`
- `docs/case-studies/digital-logic-circuit.md`
- `.github/workflows/docs-and-templates.yml`

The guide should explain how to apply this starter kit to an existing repository:

1. Audit current repo state
2. Copy starter files
3. Adapt `AGENTS.md` to the repo domain
4. Add issue templates
5. Add PR template
6. Add lightweight CI
7. Create the first Jules setup issue
8. Run the first Jules PR
9. Review and merge
10. Feed lessons back into the starter kit

## Case Study A Reference

Use `hkimw-underground/digital-logic-circuit` as the motivating example, but keep the guide reusable for any project.

The guide should explain that:

- `digital-logic-circuit` is a real applied case study.
- `vibe-coding-with-jules` remains the reusable template/playbook.
- The case study should not be treated as the generic template.
- Lessons from the case study can be generalized back into this repo.

## Non-goals

- Do not modify the case study repository from this PR.
- Do not duplicate the entire Quickstart guide.
- Do not claim all projects can safely use autonomous workflows.
- Do not present Jules as a human contributor.
- Do not add heavy automation.
- Do not use promotional language.

## Acceptance Criteria

- [ ] `docs/operations/apply-to-existing-repo.md` exists.
- [ ] The guide clearly separates template repo and applied case study repo.
- [ ] The guide includes a step-by-step rollout process.
- [ ] The guide explains how to adapt `AGENTS.md` to a real project domain.
- [ ] The guide includes a feedback loop from case study back to starter kit.
- [ ] README or Showcase links are updated if useful.
- [ ] Docs CI checks the new guide if appropriate.
- [ ] Jules remains framed as an AI coding agent.
- [ ] Human maintainer ownership remains explicit.
- [ ] Docs CI passes.

## Validation

The PR should confirm:

- Links are relative and correct.
- Markdown hygiene passes.
- Docs CI passes.
- No changes are made to the case study repository.
- Jules remains framed as an AI coding agent.
- Human maintainer review remains required.

## Workflow Level

- Level 1 - Human-led Jules workflow
