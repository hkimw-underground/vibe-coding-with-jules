# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md)

> 대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.  
> 이 프로젝트는 그 과정 자체를 보여줍니다.

**AI Coding Workflow Starter Kit for Jules**는 Jules를 GitHub Issue, Pull Request, Review, CI, case study, controlled automation 안에서 운영하기 위한 GitHub-native playbook입니다.

이 저장소는 단순한 prompt 모음이 아닙니다. AI-assisted work가 읽을 수 있는 engineering history를 남기도록 돕는 reusable starter kit입니다.

Repository: <https://github.com/hkimw-underground/vibe-coding-with-jules>

권장 public positioning:

```text
Repo name: jules-workflow-starter-kit
Display title: AI Coding Workflow Starter Kit for Jules
Tagline: Most AI coding demos show only the final code. This project shows the process.
```

---

## What This Is

이 저장소는 Jules를 일반적인 GitHub 개발 관행 안에서 운영하기 위한 template과 예시를 제공합니다.

- scoped GitHub Issues
- Jules task handoff prompts
- small pull requests
- human review checklists
- CI-first validation
- case study documentation
- controlled automation experiments

핵심 메시지는 단순합니다.

> Human maintainer가 AI coding agent를 GitHub-native engineering practice 안에서 리드한다.

아래 메시지가 아닙니다.

> AI가 프로젝트 전체를 혼자 만들었다.

---

## Workflow Levels

이 starter kit은 안정적인 maintainer workflow와 실험적 automation을 분리합니다.

| Level | Workflow | Human role | Status |
| --- | --- | --- | --- |
| 1 | Human-led Jules workflow | issue 작성, PR review, merge | recommended default |
| 2 | Semi-autonomous Jules workflow | issue 작성, final PR review | practical advanced mode |
| 3 | Human issue only | issue만 작성, Jules가 implementation/PR update | advanced with strict CI |
| 4 | Daily agentic maintainer loop | daily report를 보고 방향 조정 | advanced planning loop |
| 5 | No-human sandbox workflow | 관찰 또는 audit만 수행 | experiment only |
| 6 | Jules + evaluator-driven evolution | objective/evaluator 정의, 결과 review | experiment only |

기본값은 Level 1입니다. Level 5와 6은 sandbox 또는 protected experiment branch에서만 다룹니다.

---

## Core Workflow

```text
Human maintainer가 scoped GitHub Issue 작성
        ↓
Jules가 task 구현
        ↓
Jules가 focused PR 생성 또는 publish
        ↓
CI가 변경 사항 검증
        ↓
Human maintainer가 diff review
        ↓
Maintainer가 merge 또는 수정 요청
```

이 workflow는 과정을 GitHub history에 남깁니다.

```text
Issue → Jules task → PR → Review → CI → Merge
```

나중에 다른 개발자가 history를 이해할 수 없다면 workflow가 실패한 것입니다.

---

## Repository Structure

```text
.
├── README.md
├── README.ko.md
├── AGENTS.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── jules_task.yml
│   │   └── workflow_experiment.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── workflows/
│   │   └── workflow-levels.md
│   ├── experiments/
│   │   ├── no-human-only-jules-workflow.md
│   │   └── jules-alpha-evolve.md
│   └── case-studies/
│       ├── digital-logic-circuit.md
│       └── english-only-project.md
└── prompts/
    ├── issue-to-jules-task.md
    └── daily-maintainer-report.md
```

---

## Getting Started

### 1. Starter Kit 복사하기

프로젝트에 필요한 부분을 복사합니다.

```text
AGENTS.md
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
docs/workflows/
prompts/
```

### 2. Jules 연결하기

Jules에서 GitHub repository 연결을 확인합니다.

### 3. 작은 Issue 하나로 시작하기

좋은 issue:

```text
Add a PR template that requires linked issue, validation steps, and reviewer checklist.
```

나쁜 issue:

```text
Improve the project.
```

### 4. Jules에게 Focused PR 요청하기

Issue를 source of truth로 사용합니다. Jules prompt는 issue를 reviewable PR로 바꾸는 역할을 해야지, issue 자체를 대체하면 안 됩니다.

### 5. Merge 전 Review하기

Merge 전에 다음을 확인합니다.

- PR이 linked issue를 해결하는가?
- scope가 통제되어 있는가?
- 관련 없는 파일이 바뀌지 않았는가?
- tests 또는 validation steps가 포함되어 있는가?
- CI가 통과하는가?
- 구현이 유지보수 가능한가?
- 나중에 다른 개발자가 이 history를 이해할 수 있는가?

---

## Case Studies

### [Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)

Repository: <https://github.com/hkimw-underground/digital-logic-circuit>

실제 hardware/software capstone case study입니다. 외부 project tracker에 있던 planning과 implementation workflow를 GitHub Issues, PRs, human review, Jules-assisted implementation 중심으로 옮기는 사례입니다.

Architecture, hardware constraints, scope, review, final merge decision은 maintainer가 책임집니다.

### Case Study B: English-Only Open Source Project

Status: planned.

글로벌 독자를 위한 순수 영어 오픈소스 사례입니다. 학교/capstone 맥락 밖에서도 small issues, focused Jules PRs, CI-first development, readable review comments가 재사용 가능하다는 것을 보여주는 목적입니다.

---

## Safety Position

이 저장소는 automation을 다루지만, automation 자체를 기본 목표로 삼지 않습니다.

Stable guidance:

```text
Human decides direction.
Human owns architecture.
Human reviews final changes.
CI gates every merge.
Jules is never presented as a human contributor.
```

Experimental guidance:

```text
No-human workflows must run in sandbox repos or protected branches.
Auto-merge requires strict CI and branch protection.
Evaluator-driven evolution must use measurable tests or benchmarks.
```

---

## Core Message

대부분의 AI coding demo는 완성된 코드만 보여줍니다.

이 프로젝트는 과정을 보여줍니다.

```text
Issue.
Prompt.
Plan.
Pull request.
Review.
CI.
History.
```

진짜 AI-assisted engineering은 여기서 일어납니다.
