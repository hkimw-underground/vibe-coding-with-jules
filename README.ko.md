# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md) · [Quickstart](./docs/quickstart.md) · [프로젝트 준비 상태](./docs/meta/project-readiness.md) · [출시 체크리스트](./docs/meta/release-checklist.md) · [기여하기](./CONTRIBUTING.md) · [보안](./SECURITY.md)

> 대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.  
> 이 프로젝트는 그 과정 자체를 보여줍니다.

**AI Coding Workflow Starter Kit for Jules**는 Jules를 GitHub Issue, Pull Request, Review, CI, case study, controlled workflow experiment 안에서 운영하기 위한 GitHub-native playbook입니다.

이 저장소는 학생, 교사, GitHub를 처음 쓰는 maintainer, 작은 팀이 AI-assisted coding work를 읽을 수 있는 engineering history로 남기도록 돕습니다.

단순한 prompt 모음이 아닙니다. 일반적인 GitHub practice 안에서 AI-assisted work를 운영하기 위한 reusable starter kit입니다.

---

## 트랙 선택하기

원하는 인간 개입 수준에 맞는 workflow를 고르세요.

![Four Tracks Overview](./docs/assets/four-tracks-overview.svg)

| 트랙 | 적합한 상황 | 인간 개입 | 상태 |
| --- | --- | --- | --- |
| **[Review-Driven](./docs/tracks/review-driven.md)** | 실제 프로젝트, 수업, starter repo | 중간 | **기본 권장** |
| **[GitHub-Native Collaboration](./docs/tracks/github-native-collaboration.md)** | Issue, PR, review, CI, label, branch protection 학습 | 중간 | 학습용 권장 |
| **[Half Vibe Coding](./docs/tracks/half-vibe-coding.md)** | maintainer가 방향을 주고 Jules가 checkpoint 사이를 실행 | 낮음 | 고급 |
| **[Full Vibe Coding](./docs/tracks/full-vibe-coding.md)** | sandbox experiment와 workflow research | 최소 | 실험 전용 |

대부분의 독자에게 추천하는 순서:

![Workflow Overview](./docs/assets/workflow-overview.svg)

```text
Review-Driven으로 시작합니다.
GitHub 협업을 가르치거나 배울 때 GitHub-Native Collaboration을 사용합니다.
CI와 review rule이 잡힌 뒤에 Half Vibe Coding을 시도합니다.
Full Vibe Coding은 sandbox repo 또는 protected branch에서만 다룹니다.
```

---

## 시작하기

![Getting Started Flow](./docs/assets/getting-started-flow.svg)

1. **[Quickstart Guide](./docs/quickstart.md)**를 읽습니다.
2. starter file을 자신의 repository에 복사합니다.
3. 작은 GitHub Issue를 엽니다.
4. Jules가 focused pull request를 만들게 합니다.
5. PR을 review하고, CI를 확인한 뒤, maintainer가 만족할 때만 merge합니다.

먼저 복사할 starter file:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/docs-and-templates.yml
prompts/
examples/
```

---

## 기본 워크플로우

기본 workflow는 **Review-Driven**입니다.

![Workflow Overview](./docs/assets/workflow-overview.svg)

```text
Issue → Jules task → Pull request → CI → Human review → Merge
```

Maintainer는 scope, architecture, validation, final merge decision을 계속 책임집니다. Jules는 GitHub workflow 안에서 implementation과 documentation 작업을 보조합니다.

---

## 포함된 내용

- **AGENTS.md** — Jules-assisted work를 위한 repository rule
- **Issue templates** — scoped task와 workflow experiment template
- **PR template** — linked issue, validation, review expectation
- **CI example** — docs와 starter kit 구조를 확인하는 lightweight check
- **Prompts** — issue handoff와 maintainer report prompt
- **Examples** — reusable issue와 PR review example
- **Operations guides** — one-task-at-a-time, branch protection, labels, triage
- **Workflow tracks** — review-driven부터 sandbox experiment까지 4가지 Jules workflow
- **Case studies** — 실제 적용 사례 1개와 planned English-only case study 1개

---

## 주요 가이드

- [Quickstart](./docs/quickstart.md)
- [One Jules Task at a Time](./docs/operations/one-jules-task-at-a-time.md)
- [Branch Protection and CI Gates](./docs/operations/branch-protection-and-ci-gates.md)
- [Labels and Triage](./docs/operations/labels-and-triage.md)
- [Project Readiness](./docs/meta/project-readiness.md)
- [Documentation Audit](./docs/meta/documentation-audit.md)

---

## 케이스 스터디

- **[Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)** — Jules workflow를 적용한 실제 hardware/software capstone project.
- **[Case Study B: English-Only Project Brief](./docs/case-studies/english-only-project.md)** — 글로벌 독자를 위한 작은 open-source project 계획 문서.

---

## 안전 및 책임

Stable guidance:

```text
Human decides direction.
Human owns architecture.
Human reviews final changes.
CI gates every merge.
Jules is an AI coding agent, not a human contributor.
```

Experimental guidance:

```text
Autonomous workflows belong in sandbox repos or protected branches.
Auto-merge experiments require strict CI and branch protection.
Evaluator-driven experiments need measurable tests or benchmarks.
```

---

## Repository Structure

```text
.
├── AGENTS.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
├── docs/
│   ├── quickstart.md
│   ├── case-studies/
│   ├── experiments/
│   ├── meta/
│   ├── operations/
│   ├── tracks/
│   └── workflows/
├── examples/
│   ├── issues/
│   └── pr-reviews/
└── prompts/
```

---

## 라이선스

이 프로젝트는 [MIT License](./LICENSE)를 따릅니다.
