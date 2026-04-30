# AI Coding Workflow Starter Kit for Jules

[English](./README.md) · [한국어](./README.ko.md) · [기여하기](./CONTRIBUTING.md) · [행동 강령](./CODE_OF_CONDUCT.md) · [보안](./SECURITY.md)

> 대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.  
> 이 프로젝트는 그 과정 자체를 보여줍니다.

**AI Coding Workflow Starter Kit for Jules**는 AI 코딩 에이전트(**Jules**)를 GitHub Issue, Pull Request, Review, CI 안에서 운영하기 위한 GitHub-native playbook입니다. AI-assisted work가 깨끗하고 전문적인 engineering history를 남기도록 돕는 reusable starter kit입니다.

---

## Why This Kit?

대부분의 AI 코딩 workflow는 휘발성인 채팅 로그 안에 숨겨져 있습니다. 이 키트는 표준 GitHub 관행을 사용하여 그 과정을 투명하게 공개합니다.

- **추적 가능한 이력**: 모든 변경 사항은 Issue와 연결되며 PR review를 통해 검증됩니다.
- **Human-in-the-Loop**: Human maintainer가 방향을 리드하고, Jules는 세부 사항을 구현합니다.
- **재사용 가능한 템플릿**: 바로 사용 가능한 Issue template, PR format, handoff prompt를 제공합니다.
- **실전 검증**: 엄격한 human-led 방식부터 실험적인 루프까지, 자율성 수준별 workflow를 문서화했습니다.

목표는 단순합니다. **Human maintainer가 AI coding agent를 리드한다.** 이는 "AI가 혼자서 프로젝트를 만든다"는 뜻이 아니라, 확장 가능한 AI-assisted engineering을 의미합니다.

---

## Core Workflow

Human maintainer는 표준 GitHub flow를 사용하여 과정을 리드합니다.

```text
Issue → Jules Task → Pull Request → Human Review → CI → Merge
```

1. **Human**이 scoped GitHub Issue를 작성합니다.
2. **Jules**가 task를 구현하고 focused PR을 생성합니다.
3. **CI**가 변경 사항을 검증합니다.
4. **Human**이 diff를 review하고 merge합니다.

---

## Repository Structure

```text
.
├── AGENTS.md            # Jules를 위한 필수 지침
├── .github/             # GitHub Issue 및 PR 템플릿
├── docs/                # Workflow level 및 Case Study
├── examples/            # Issue 및 PR review 예시
├── prompts/             # 표준화된 AI handoff prompt
├── README.md
└── README.ko.md
```

---

## Getting Started

### 1. 핵심 파일 복사하기
이 workflow를 시작하려면 다음 파일들을 저장소에 추가하세요.

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `prompts/`

### 2. Jules 연결하기
Jules가 저장소에 접근할 수 있고 `AGENTS.md` 파일을 읽을 수 있는지 확인합니다.

### 3. 작은 Issue 하나로 시작하기
잘 정의된 Issue(예: "Add unit tests for the login module")를 열고 `jules_task.yml` 템플릿을 사용하세요.

---

## Workflow Levels

Human의 개입 수준에 따라 workflow를 분류합니다. Level 1을 기본 권장 사항으로 합니다.

| Level | Workflow | Human role | Status |
| --- | --- | --- | --- |
| 1 | Human-led Jules workflow | Issue 작성, PR review, merge | **권장** |
| 2 | Semi-autonomous Jules workflow | Issue 작성, 최종 PR review | 실용적 |
| 3 | Human issue only | Issue 작성; Jules가 구현 담당 | 고급 |
| 4 | Daily agentic maintainer loop | Daily report를 보고 방향 조정 | 실험적 |
| 5 | No-human sandbox workflow | 관찰 또는 audit만 수행 | Sandbox 전용 |

---

## Case Studies

- **[Case Study A: Digital Logic Circuit](./docs/case-studies/digital-logic-circuit.md)**: Jules를 통해 관리된 실제 hardware/software 프로젝트 사례.
- **[Case Study B: English-Only Project](./docs/case-studies/english-only-project.md)**: 글로벌 독자를 위한 오픈소스 사례 (준비 중).

---

## Core Message

대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다. **이 프로젝트는 과정을 보여줍니다.**

```text
Issue → Prompt → Plan → Pull Request → Review → CI → History
```

진짜 AI-assisted engineering은 여기서 일어납니다.

---

## 라이선스

이 프로젝트는 [MIT 라이선스](./LICENSE)를 따릅니다.
