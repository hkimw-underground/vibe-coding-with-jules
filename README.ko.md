# Vibe Coding with Jules

[English](./README.md) · [한국어](./README.ko.md)

> 대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.  
> 이 프로젝트는 그 과정 자체를 보여줍니다.

**Vibe Coding with Jules**는 **Jules**, 즉 AI coding agent를 실제 소프트웨어 프로젝트에서 GitHub 방식으로 운영하기 위한 workflow kit입니다.

이 저장소는 단순한 프롬프트 모음이 아닙니다.

AI-assisted development를 다음 흐름으로 운영하기 위한 실전형 템플릿 저장소입니다.

- GitHub Issues
- 명확하게 범위가 잡힌 구현 태스크
- Pull Requests
- Human review
- CI checks
- 실제 case study 문서화

목표는 단순합니다.

> AI coding work를 마법처럼 포장하지 않고, 유지보수 가능한 오픈소스 엔지니어링처럼 다루는 것.

---

## Overview

AI coding agent는 경계가 명확할수록 더 잘 작동합니다.

이 저장소는 maintainer가 Jules를 명확한 개발 workflow 안에서 활용할 수 있도록 재사용 가능한 구조를 제공합니다.

AI agent에게 “프로젝트를 알아서 만들어줘”라고 맡기는 대신, 이 workflow는 다음 방식을 권장합니다.

1. GitHub Issue로 문제를 정의합니다.
2. 구현 범위를 작은 task로 나눕니다.
3. Jules가 focused pull request를 만들도록 합니다.
4. Human maintainer가 PR을 리뷰합니다.
5. CI로 회귀와 기본 품질 문제를 잡습니다.
6. 무엇이 왜 바뀌었는지 기록합니다.

이 저장소는 다른 GitHub 프로젝트에 그대로 복사하고, 수정하고, 재사용할 수 있도록 설계되어 있습니다.

---

## Why

대부분의 AI 코딩 예시는 멋지게 정리된 before-and-after 데모처럼 보입니다.

하지만 실제 엔지니어링에서 중요한 부분은 그 사이에 있습니다.

- 작업은 어떻게 정의되었는가?
- 어떤 제약 조건이 있었는가?
- AI agent의 결과물은 어떻게 리뷰되었는가?
- CI는 무엇을 잡았는가?
- Human maintainer는 무엇을 거절하거나 수정했는가?
- GitHub history는 나중에 봐도 이해 가능한가?

이 프로젝트가 존재하는 이유는 process가 중요하기 때문입니다.

좋은 AI-assisted workflow는 다른 개발자가 이해할 수 있는 GitHub history를 남겨야 합니다.

---

## Workflow

권장 workflow는 다음과 같습니다.

```text
Human Maintainer
      ↓
GitHub Issue
      ↓
Jules Task Prompt
      ↓
Implementation Branch
      ↓
Pull Request
      ↓
Human Review
      ↓
CI / Tests
      ↓
Merge or Request Changes
```

### 1. Issue에서 시작하기

의미 있는 작업은 GitHub Issue에서 시작해야 합니다.

좋은 issue에는 다음 내용이 들어갑니다.

- problem statement
- expected behavior
- constraints
- non-goals
- acceptance criteria
- testing expectations

Jules에게 product direction을 추측하게 만들면 안 됩니다.

의도와 방향은 human maintainer가 책임집니다.

---

### 2. Issue를 Jules Task로 변환하기

Jules prompt는 구체적이고, 범위가 작고, 리뷰 가능해야 합니다.

좋은 Jules task에는 보통 다음 내용이 들어갑니다.

- repository context
- target files or modules
- exact implementation goal
- constraints
- test command
- expected PR summary
- what not to touch

목표는 Jules를 “창의적으로” 만드는 것이 아닙니다.

목표는 Jules를 유용하게 만드는 것입니다.

---

### 3. Pull Request는 작게 유지하기

작은 PR일수록 AI-generated change를 리뷰하기 쉽습니다.

권장 PR 크기:

- one issue
- one responsibility
- one reviewable change
- tests included when possible

“AI가 전체를 리팩터링한 거대한 PR”은 피하는 것이 좋습니다.

---

### 4. Jules는 Coding Agent로 리뷰하기

Jules는 AI coding agent이지, 인간 팀원이 아닙니다.

따라서 다음 원칙을 지켜야 합니다.

- Jules가 스스로 아키텍처 결정을 내린 것처럼 포장하지 않습니다.
- human review 없이 merge하지 않습니다.
- 동작한다는 이유만으로 불명확한 코드를 받아들이지 않습니다.
- generated change가 프로젝트 기준을 우회하게 두지 않습니다.

정확성, 아키텍처, 유지보수성의 최종 책임은 human maintainer에게 있습니다.

---

### 5. CI를 Gate로 사용하기

CI는 지루하지만 중요한 부분을 검증해야 합니다.

- formatting
- linting
- tests
- type checks
- build checks
- documentation checks, when applicable

깔끔한 CI pipeline은 AI-assisted development를 더 안전하고 반복 가능하게 만듭니다.

---

## What’s Included

이 저장소는 GitHub-native Jules workflow를 위한 starter kit를 목표로 합니다.

계획된 구조는 다음과 같습니다.

```text
.
├── README.md
├── README.ko.md
├── AGENTS.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   ├── jules_task.yml
│   │   └── documentation_task.yml
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml
│       └── markdown-check.yml
├── docs/
│   ├── workflow.md
│   ├── review-guide.md
│   ├── prompt-patterns.md
│   ├── anti-patterns.md
│   └── case-studies/
│       ├── digital-logic-circuit.md
│       └── english-only-project.md
├── prompts/
│   ├── issue-to-jules-task.md
│   ├── implementation-task.md
│   ├── refactor-task.md
│   ├── review-fix-task.md
│   └── ci-failure-investigation.md
└── examples/
    ├── good-issues/
    ├── good-prs/
    └── review-comments/
```

---

## Case Studies

이 프로젝트는 Jules 기반 개발 workflow의 실제 예시를 문서화합니다.

### Case Study A: Digital Logic Circuit

Repository:  
<https://github.com/hkimw-underground/digital-logic-circuit>

이 저장소는 실제 capstone project이며, project planning과 implementation workflow를 GitHub Issue / PR 중심으로 옮긴 사례입니다.

초점은 최종 코드만이 아닙니다.

이 case study는 다음 내용을 보여줍니다.

- issue-driven planning
- hardware/software constraints
- Jules implementation tasks
- human maintainer review
- project history as documentation

이 workflow에서 Jules는 AI coding agent로 사용됩니다.

아키텍처, 하드웨어 판단, 최종 리뷰의 책임은 human maintainer에게 있습니다.

---

### Case Study B: English-Only Open Source Project

Status: planned.

이 case study는 글로벌 독자를 대상으로 하는 순수 영어 오픈소스 프로젝트로 만들 예정입니다.

보여줄 내용은 다음과 같습니다.

- small issues
- focused Jules tasks
- clean PR descriptions
- CI-first development
- readable review comments
- contributor-friendly documentation

목표는 이 workflow가 학교 프로젝트나 capstone context 밖에서도 재사용될 수 있음을 보여주는 것입니다.

---

## Templates

이 저장소는 AI-assisted development에서 자주 쓰이는 템플릿을 제공합니다.

### Issue Templates

Issue template은 human과 AI coding agent 모두가 이해할 수 있는 task를 작성하도록 돕습니다.

예시:

- bug report
- feature request
- Jules task
- documentation task
- refactor task

각 issue는 다음 질문에 답해야 합니다.

```text
What problem are we solving?
What should change?
What should not change?
How do we verify the result?
```

---

### Pull Request Template

PR template은 AI-generated change를 더 쉽게 리뷰할 수 있도록 설계됩니다.

좋은 PR에는 다음 내용이 들어갑니다.

- linked issue
- summary of changes
- test results
- screenshots or logs when useful
- known limitations
- reviewer checklist

PR은 변경 사항을 담는 것에서 끝나면 안 됩니다.

왜 바뀌었는지 설명해야 합니다.

---

### Jules Task Prompts

Prompt template은 반복 가능한 task handoff를 위해 제공됩니다.

예시 prompt category:

- implement from issue
- fix review comments
- add tests
- refactor safely
- update documentation
- investigate CI failure

이 prompt들은 engineering judgment를 대체하지 않습니다.

task delegation을 더 일관되게 만들기 위한 도구입니다.

---

## Philosophy

이 프로젝트는 몇 가지 원칙을 중심으로 설계되었습니다.

### Human Maintainer Leads

Maintainer가 책임지는 것:

- product direction
- architecture
- scope
- tradeoffs
- final review

Jules는 구현하고, 수정하고, 보조할 수 있습니다.

하지만 Jules가 조용히 프로젝트 방향을 정하게 두면 안 됩니다.

---

### AI Work Should Be Reviewable

AI-generated code는 명확한 흔적을 남겨야 합니다.

```text
Issue → Task Prompt → PR → Review → CI → Merge
```

history가 이해하기 어렵다면 workflow가 실패한 것입니다.

---

### Small PRs Beat Big Magic

큰 AI-generated PR은 리뷰하기 어렵습니다.

이 workflow는 다음을 선호합니다.

- small changes
- clear acceptance criteria
- testable outputs
- reviewable commits

목표는 화려한 데모가 아니라 유지보수성입니다.

---

### CI Is Part of the Workflow

CI는 선택 장식이 아닙니다.

AI-assisted change가 검증되지 않은 추측이 되지 않도록 막는 safety layer입니다.

---

### Do Not Pretend the AI Is Human

Jules는 AI coding agent입니다.

이 저장소는 Jules를 인간 contributor처럼 포장하는 표현을 피합니다.

이 프로젝트가 전달하려는 메시지는 다음입니다.

> Human maintainer가 AI coding agent를 GitHub-native engineering practice 안에서 리드할 수 있다.

아래 메시지가 아닙니다.

> AI가 프로젝트 전체를 혼자 만들었다.

---

## Getting Started

### 1. Repository Structure 복사하기

이 저장소를 자신의 프로젝트 starter kit으로 사용할 수 있습니다.

복사할 수 있는 항목:

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE`
- `.github/pull_request_template.md`
- `.github/workflows`
- `docs/`
- `prompts/`

---

### 2. 첫 Issue 만들기

작고 구체적인 task부터 시작하세요.

좋은 첫 task 예시:

- add a missing test
- improve README setup instructions
- fix one bug
- add one small feature
- refactor one module

다음과 같은 모호한 issue는 피하는 것이 좋습니다.

```text
Make this project better.
```

대신 이렇게 쓰는 것이 좋습니다.

```text
Add a CI workflow that runs tests on every pull request.
```

---

### 3. Jules Task Prompt 작성하기

Issue를 source of truth로 사용합니다.

좋은 task prompt에는 다음 내용이 들어갑니다.

```text
Repository context:
Task:
Files to inspect:
Constraints:
Acceptance criteria:
Test command:
Expected PR description:
Do not touch:
```

---

### 4. Pull Request 리뷰하기

Merge 전에 다음을 확인합니다.

- PR이 issue를 해결하는가?
- scope가 통제되어 있는가?
- 관련 없는 파일이 바뀌지 않았는가?
- test가 포함되었거나 업데이트되었는가?
- CI가 통과하는가?
- 구현이 유지보수 가능한가?
- 나중에 다른 개발자가 이 history를 이해할 수 있는가?

---

### 5. 결과 문서화하기

PR이 merge된 뒤에도 issue와 PR history는 개발 과정을 설명해야 합니다.

그 history 자체가 프로젝트의 일부입니다.

AI-assisted development에서는 process가 portfolio입니다.

---

## Who This Is For

이 저장소는 다음 사람들을 위한 것입니다.

- AI coding agent를 실험하는 open-source maintainer
- GitHub로 capstone project를 운영하려는 학생
- 더 깔끔한 AI-assisted workflow를 원하는 개발자
- prompt-to-PR workflow를 반복 가능하게 만들고 싶은 팀
- AI coding work를 reviewable하게 만들고 싶은 사람

---

## Project Status

이 저장소는 reusable workflow template이자 public playbook으로 구축 중입니다.

초기 초점은 documentation, templates, case studies입니다.

---

## License

재사용 목적에 맞는 license를 선택하세요.

이런 유형의 저장소에 추천되는 license:

- MIT License: 넓은 재사용에 적합
- Apache-2.0: patent language가 필요한 경우
- CC BY 4.0: documentation-heavy reuse에 적합

---

## Core Message

대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.

이 프로젝트는 과정을 보여줍니다.

```text
Issue.
Prompt.
Pull request.
Review.
CI.
History.
```

진짜 AI-assisted engineering은 여기서 일어납니다.
