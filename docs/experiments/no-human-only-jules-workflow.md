# No-human-only Jules Workflow

This is an experiment, not the recommended default workflow.

The purpose is to study how far a Jules-based workflow can be automated while keeping the result auditable through GitHub.

## Experimental Pipeline

```text
Agent creates issue
→ Jules starts task
→ Jules implements change
→ Jules verifies result
→ Jules opens PR
→ required CI checks run
→ auto-merge after protected gates
```

## Required Safety Boundaries

Use this only when all of the following are true:

- The repository is a sandbox or the branch is explicitly experimental.
- Branch protection is enabled.
- Required CI checks are configured.
- Auto-merge is allowed only after all checks pass.
- No production secrets are exposed.
- Rollback is documented.
- Logs, prompts, issues, PRs, and CI results remain visible.

## Not Allowed

Do not use this workflow to bypass human review on important code.

Do not present the result as human-authored.

Do not run broad refactors through this workflow.

## Good Use Cases

- documentation formatting experiments
- benchmark-only code search experiments
- generated examples in disposable branches
- repeatable CI-gated maintenance tasks

## Bad Use Cases

- architecture changes
- security-sensitive code
- dependency upgrades without review
- production deployment changes
- large multi-file rewrites

## Maintainer Position

No-human workflows are useful as research artifacts. They are not the baseline recommendation of this starter kit.
