# Documentation Audit Checklist

This checklist is used by maintainers to audit the consistency and quality of documentation before public sharing, tagged releases, or major README updates. This focuses on document quality and consistency across the starter kit, complementing the public launch checklist.

## 1. Identity & Framing

- [ ] **Jules Identity**: Jules is always framed as an AI coding agent, never as a human contributor.
- [ ] **Maintainer Ownership**: The workflow clearly preserves human maintainer ownership (e.g., human decides direction, reviews PRs, and makes final merge decisions).
- [ ] **No Promotional Language**: Documentation uses practical, non-promotional language and avoids external ranking or hype-heavy language.

## 2. Structure & Consistency

- [ ] **Repository Structure**: The `Repository Structure` tree in both `README.md` and `README.ko.md` exactly matches the actual file tree in the repository.
- [ ] **Link Validity**: All internal links across documents are relative and valid.
- [ ] **Korean Translation Alignment**: The structure and content of `README.ko.md` remains strictly aligned with `README.md`, especially when top-level structure changes.

## 3. Workflow & Automation

- [ ] **Separation of Workflows**: Documentation clearly separates experiment workflows from recommended, stable maintainer workflows.
- [ ] **Branch Protection Framing**: Branch protection and CI gates are described as necessary safeguards, not as absolute guarantees.

## 4. Examples & Case Studies

- [ ] **Scoped Examples**: Reference examples remain strictly scoped and copyable for users.
- [ ] **Case Study Status**: Documentation clearly states that Case Study A is complete and Case Study B is planned (unless Case Study B content has been updated).
