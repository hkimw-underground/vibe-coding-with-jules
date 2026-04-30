# Public Launch Checklist

This checklist is used by maintainers to verify that the repository is ready to present externally before public sharing. It focuses on practical launch readiness, ensuring consistency and completeness of the public-facing documentation and configurations.

## Review Items

### Documentation and Presentation
- [ ] **README first-screen review**: The [README](../../README.md) clearly explains the project's purpose and tagline on the first screen.
- [ ] **Repository description and topics**: The GitHub repository has a clear description and appropriate topics set.
- [ ] **Relative links and document tree consistency**: All relative links in documents are correct, and the document tree in the README matches the actual repository structure.
- [ ] **No language presenting Jules as a human contributor**: All public-facing documentation clearly identifies Jules as an AI coding agent or managed contributor.
- [ ] **Examples and Quickstart discoverability**: The [Quickstart Guide](../quickstart.md) and examples are prominently linked and easily discoverable.
- [ ] **Case Study status clarity**: The completion status of Case Study A (Digital Logic) and Case Study B (English-Only) is clear.

### CI and Workflows
- [ ] **CI green status**: All required GitHub Actions CI checks (like Docs and Templates validation) are passing.
- [ ] **Branch protection / required checks**: The `main` branch is properly protected, and required checks are enforced as detailed in the [Branch Protection Guide](../operations/branch-protection-and-ci-gates.md).

### Community and Contributions
- [ ] **Issue templates and PR template presence**: Issue templates for tasks and experiments, as well as the PR template, are present in the `.github` directory.
- [ ] **Community files presence**: Standard community files like `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `SECURITY.md` are available.
- [ ] **No open stale or duplicate PRs**: Ensure tasks have been sequenced safely to prevent stale PRs as described in the [Operations Guide](../operations/one-jules-task-at-a-time.md).
