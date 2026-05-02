# Applied Repository Rollout

The AI Coding Workflow Starter Kit for Jules is designed to be copied into existing repositories. This guide explains how to roll out the starter kit to a real, ongoing project.

We use `hkimw-underground/digital-logic-circuit` as the motivating example for this guide. That repository is [Case Study A](../case-studies/digital-logic-circuit.md) — a real hardware and software capstone project. While `digital-logic-circuit` is the specific case study demonstrating the workflow in action, `vibe-coding-with-jules` remains the reusable template and playbook for any project. Lessons learned from the applied case study are brought back to improve this starter kit.

## The Rollout Process

Do not copy every file from the starter kit at once. Start small, verify the workflow, and expand as needed.

### 1. Audit current repo state
Before adding the starter kit, check your repository's baseline:
- Is there a clear `README.md` explaining the project?
- Are there existing linting or test scripts?
- What are the current branch protection rules?

### 2. Copy starter files
Copy only the essential files to establish the workflow boundary:
- `AGENTS.md`
- `.github/ISSUE_TEMPLATE/jules_task.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`

### 3. Adapt `AGENTS.md` to the repo domain
`AGENTS.md` is the primary rulebook for Jules. You must customize it for your project's specific context.
For example, in `digital-logic-circuit`, the `AGENTS.md` must be updated to clarify that Jules is not allowed to modify hardware simulation schematics without explicit test coverage, or that Python scripts must target a specific hardware environment.

### 4. Add issue templates
Ensure `.github/ISSUE_TEMPLATE/jules_task.yml` is in place. This enforces that every Jules task starts with a clear, scoped GitHub Issue written by a human maintainer.

### 5. Add PR template
The `.github/PULL_REQUEST_TEMPLATE.md` ensures that Jules links back to the motivating issue and includes validation notes. This keeps human review focused.

### 6. Add lightweight CI
Jules needs fast feedback. Add a minimal GitHub Actions workflow to check formatting or run basic tests.
If your repository doesn't have tests yet, start with something simple like syntax checking.

### 7. Create the first Jules setup issue
Open a small, low-risk GitHub Issue. Good first issues include:
- "Add a standard `.gitignore` for the project."
- "Format all Python files using `black`."
- "Write a basic unit test for an existing utility function."

### 8. Run the first Jules PR
Assign the issue to Jules. Jules, acting as an AI coding agent, will read the issue and create a small, focused Pull Request.

### 9. Review and merge
The human maintainer reviews the PR.
- Did Jules follow the scope?
- Did CI pass?
- Does the architecture still align with the project goals?
Merge only when satisfied. The maintainer retains full ownership.

### 10. Feed lessons back into the starter kit
As you run more tasks, you will find gaps. Update your local `AGENTS.md` or issue templates. If a workflow improvement is generally useful (like a better PR review prompt), bring that lesson back to the main starter kit repository.
