# Documentation Audit Checklist

This checklist is used by maintainers to ensure high quality and consistency across the starter kit's documentation. It focuses on maintaining the project's professional tone, human-led workflow position, and structural accuracy.

## 1. Identity and Ownership

- [ ] **AI Agent Framing**: Jules is consistently referred to as an "AI coding agent," never as a "human contributor," "team member," or "developer" without the AI qualifier.
- [ ] **Human Ownership**: Documentation reinforces that the human maintainer owns the architecture, decision-making, and final review process.
- [ ] **No Personification**: Avoid language that implies Jules has human emotions, intentions, or independent agency outside of the defined workflow.

## 2. Structural Accuracy

- [ ] **README Repository Tree**: The "Repository Structure" section in both `README.md` and `README.ko.md` matches the actual file system.
- [ ] **Relative Links**: All internal documentation links are relative and resolve correctly within the repository.
- [ ] **Starter Kit Parity**: The `required_paths` in `.github/workflows/docs-and-templates.yml` align with the actual files intended for the starter kit.

## 3. Content Consistency

- [ ] **Case Study Status**: [Case Study A](../case-studies/digital-logic-circuit.md) is marked as complete, and [Case Study B](../case-studies/english-only-project.md) is an actionable brief.
- [ ] **Workflow Separation**: Recommended workflows (Level 1-3) are clearly distinguished from experimental or sandbox workflows (Level 5-6).
- [ ] **Safeguard Language**: Branch protection and CI gates are described as "safeguards" or "gates," not absolute guarantees of code quality or security.
- [ ] **Bilingual Alignment**: Top-level structural changes in `README.md` are reflected in `README.ko.md` to maintain parity.

## 4. Quality and Tone

- [ ] **No Promotional Language**: Documentation remains practical and avoids hype, "magic," or marketing-heavy descriptions.
- [ ] **No External Rankings**: Avoid mentioning submission to external lists, rankings, or "awesome" collections.
- [ ] **Copyable Examples**: All [examples](../../examples/) remain scoped, functional, and easy for users to copy into their own projects.
- [ ] **Markdown Hygiene**: Files end with a newline, contain no tabs, and use trailing spaces only for hard line breaks (exactly two).
