# Case Study A: Digital Logic Circuit

## Overview
**Repository:** [hkimw-underground/digital-logic-circuit](https://github.com/hkimw-underground/digital-logic-circuit)

Digital Logic Circuit is a hardware/software capstone project focused on designing and simulating digital logic circuits. This repository contains the source code for the simulator, hardware descriptions, and the necessary tooling to bridge high-level logic with hardware implementation.

## Why this is a good Jules workflow case study
This project represents a complex, multi-disciplinary engineering task that involves both software logic and hardware constraints. It is an ideal case study because:
- It involves high-stakes architectural decisions (hardware constraints).
- It requires a clear separation of concerns between logic design and implementation.
- It demonstrates how a legacy project or a project started with external tracking can be transitioned into a modern, AI-assisted GitHub-native workflow.

## Transition to GitHub Issues/PRs
Originally, project planning and task tracking were managed through external tools or ad-hoc communication. To integrate Jules effectively, the workflow was moved entirely to GitHub:
1.  **Scoped Issues:** Every feature or bug fix starts as a scoped GitHub Issue.
2.  **Explicit Context:** Issues provide hardware specs, desired logic behavior, and existing constraints.
3.  **Audit Trail:** The entire reasoning process, from issue description to Jules's implementation and human review, is captured in the GitHub history.

## Jules Responsibilities
In this project, Jules is tasked with:
- Implementing logic simulation algorithms based on specified requirements.
- Writing unit tests for software components.
- Generating boilerplate for hardware description files.
- Drafting documentation for new features.
- Fixing bugs identified during CI or manual testing.

## Human Maintainer Responsibilities
The human maintainer remains the "Pilot in Command":
- **Architecture & Design:** Deciding the overall system architecture and hardware constraints.
- **Task Scoping:** Breaking down complex hardware requirements into manageable GitHub Issues for Jules.
- **Code Review:** Critically reviewing Jules's PRs for architectural alignment, performance, and hardware safety.
- **Final Approval:** Merging PRs only after ensuring they meet all project standards.

## CI and Validation
Validation is critical given the hardware/software nature of the project:
- **Linting & Style:** Ensuring code consistency.
- **Unit Tests:** Jules-implemented logic must pass all functional tests.
- **Simulation Checks:** Validating that logic changes do not break existing circuit simulations.
- **Hardware Consistency:** Verifying that generated hardware descriptions are syntactically correct and follow project-specific rules.

## Lessons Learned
1.  **Process Over Code:** The success of the project depends more on the *workflow* (Issue → PR → Review) than on the raw speed of AI coding.
2.  **Clear Boundaries:** Explicitly defining what Jules handles (implementation, tests) versus what the human handles (architecture, review) prevents scope creep and ensures safety.
3.  **Human-in-the-Loop:** Even with high-quality AI assistance, human review is the final safeguard against subtle logic errors that could impact hardware behavior.
4.  **History Matters:** A clean GitHub history makes the project maintainable for future contributors, regardless of whether a human or an AI wrote the initial code.
