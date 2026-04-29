# Vibe Coding with Jules

[English](./README.md) · [한국어](./README.ko.md)

> 대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.  
> 이 프로젝트는 그 과정 자체를 보여줍니다.

**Vibe Coding with Jules**는 **Jules**, 즉 AI coding agent를 실제 GitHub Issue → PR → Review → CI 흐름 안에서 운영하기 위한 GitHub-native workflow kit입니다.

이 저장소는 단순한 프롬프트 모음이 아닙니다.

이 프로젝트는 human maintainer가 AI coding agent를 오픈소스 협업의 기본 단위로 리드하는 방식을 보여주기 위해 설계되었습니다.

- GitHub Issues
- GitHub Actions
- 범위가 명확한 AI coding task
- Pull Requests
- Human code review
- CI checks
- 실제 case study 문서화

Repository:  
<https://github.com/hkimw-underground/vibe-coding-with-jules>

---

## Overview

많은 AI coding workflow는 개발 history 밖에서 일어납니다.

어딘가에 prompt를 씁니다.  
AI tool이 코드를 만듭니다.  
결과만 commit됩니다.  
과정은 사라집니다.

이 저장소는 다른 접근을 합니다.

의도한 workflow는 다음과 같습니다.

```text
Human Maintainer가 GitHub Issue를 작성
        ↓
GitHub Actions가 Jules를 trigger
        ↓
Jules가 focused pull request 생성
        ↓
Human Maintainer가 PR review
        ↓
CI가 변경 사항 검증
        ↓
Maintainer가 merge 또는 수정 요청
```

Jules는 **AI coding agent**로 사용됩니다.

Jules를 maintainer의 대체자로 숨기는 것이 아닙니다.

scope, architecture, review, final merge decision은 human maintainer가 책임집니다.

---

## Why

대부분의 AI 코딩 데모는 정리된 before-and-after 결과만 보여줍니다.

하지만 실제 엔지니어링에서 중요한 질문은 그 사이에 있습니다.

- AI agent에게 어떤 issue를 해결하라고 했는가?
- 어떤 제약 조건을 주었는가?
- 어떤 파일이 scope 안에 있었는가?
- human maintainer는 무엇을 review했는가?
- CI는 무엇을 검증했는가?
- 첫 PR과 최종 merge 사이에 무엇이 바뀌었는가?
- 나중에 다른 개발자가 이 history를 이해할 수 있는가?

이 프로젝트가 존재하는 이유는 process가 중요하기 때문입니다.

좋은 AI-assisted workflow는 읽을 수 있고, 리뷰할 수 있고, 재사용할 수 있는 GitHub history를 남겨야 합니다.

---

## Workflow

이 저장소는 **Jules를 위한 IssueOps**를 중심으로 설계됩니다.

매 task마다 Jules web UI에 직접 들어가는 대신, 권장 workflow는 다음과 같습니다.

```text
1. 범위가 명확한 GitHub Issue를 작성합니다.
2. `run-jules` 같은 명시적인 trigger label을 붙입니다.
3. GitHub Actions가 Issue를 기반으로 Jules task를 만듭니다.
4. Jules가 repository에서 작업하고 PR을 엽니다.
5. Maintainer가 일반 contribution처럼 PR을 review합니다.
6. CI가 통과해야 merge합니다.
```

### Recommended IssueOps Flow

```text
Issue
  ↓
Label: run-jules
  ↓
GitHub Actions
  ↓
Jules Session
  ↓
Pull Request
  ↓
Human Review
  ↓
CI
  ↓
Merge
```

이 방식은 project history를 GitHub 안에 남깁니다.

Jules web interface는 초기 setup, account connection, API key 관리에는 사용할 수 있습니다. 그 이후 목표는 GitHub Issues, PRs, Reviews, Actions 중심으로 운영하는 것입니다.

---

## What’s Included

계획된 repository structure는 다음과 같습니다.

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
│   ├── workflows/
│   │   ├── jules-issueops.yml
│   │   ├── ci.yml
│   │   └── markdown-check.yml
│   └── pull_request_template.md
├── docs/
│   ├── workflow.md
│   ├── issueops.md
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
    ├── issues/
    ├── prs/
    └── reviews/
```

---

## Case Studies

이 저장소는 Jules 기반 실제 workflow를 문서화합니다.

### Case Study A: Digital Logic Circuit

Repository:  
<https://github.com/hkimw-underground/digital-logic-circuit>

이 저장소는 실제 capstone project이며, project planning과 implementation workflow를 GitHub Issue / PR 중심으로 옮긴 사례입니다.

초점은 최종 코드만이 아닙니다.

이 case study는 다음을 보여줍니다.

- issue-driven planning
- hardware/software constraints
- Jules implementation tasks
- human maintainer review
- CI and validation expectations
- project history as documentation

이 workflow에서 Jules는 AI coding agent입니다. architecture, hardware decision, scope control, final review는 human maintainer가 책임집니다.

---

### Case Study B: English-Only Open Source Project

Status: planned.

이 case study는 글로벌 독자를 위한 순수 영어 오픈소스 프로젝트로 만들 예정입니다.

보여줄 내용은 다음과 같습니다.

- small issues
- automated Jules task triggering
- focused pull requests
- clean PR descriptions
- CI-first development
- readable review comments
- contributor-friendly documentation

목표는 이 workflow가 학교 프로젝트나 capstone context 밖에서도 재사용될 수 있음을 보여주는 것입니다.

---

## Templates

이 저장소는 반복 가능한 AI-assisted development를 위한 template을 제공합니다.

### Issue Templates

Issue template은 AI coding agent가 시작하기 전에 maintainer가 작업을 명확하게 정의하도록 돕습니다.

좋은 issue는 다음 질문에 답해야 합니다.

```text
What problem are we solving?
What should change?
What should not change?
How do we verify the result?
```

### Pull Request Template

PR template은 AI-generated change를 더 쉽게 review할 수 있도록 설계됩니다.

좋은 PR에는 다음이 포함되어야 합니다.

- linked issue
- summary of changes
- validation steps
- screenshots or logs when useful
- known limitations
- reviewer checklist

PR은 변경 사항을 담는 것에서 끝나면 안 됩니다.

변경 이유와 검증 방법을 설명해야 합니다.

### Jules Task Prompts

Prompt template은 반복 가능한 task handoff를 위해 포함됩니다.

예시 category:

- implement from issue
- fix review comments
- add tests
- refactor safely
- update documentation
- investigate CI failure

Issue는 source of truth로 남아야 합니다.

Prompt는 scoped issue를 reviewable PR로 바꾸는 데 도움을 주는 도구이지, engineering judgment를 대체하는 도구가 아닙니다.

---

## Philosophy

### Human Maintainer Leads

Maintainer가 책임지는 것:

- product direction
- architecture
- scope
- tradeoffs
- final review
- merge decisions

Jules는 구현하고, 수정하고, 보조할 수 있습니다.

하지만 Jules가 조용히 프로젝트 방향을 정하게 두면 안 됩니다.

### AI Work Should Be Reviewable

AI-generated code는 명확한 흔적을 남겨야 합니다.

```text
Issue → Action Run → PR → Review → CI → Merge
```

history가 이해하기 어렵다면 workflow가 실패한 것입니다.

### Small PRs Beat Big Magic

큰 AI-generated PR은 review하기 어렵습니다.

이 workflow는 다음을 선호합니다.

- small changes
- clear acceptance criteria
- testable outputs
- reviewable diffs

목표는 화려한 데모가 아니라 유지보수성입니다.

### CI Is Part of the Workflow

CI는 선택 장식이 아닙니다.

AI-assisted change가 검증되지 않은 추측이 되지 않도록 막는 safety layer입니다.

### Do Not Pretend the AI Is Human

Jules는 AI coding agent입니다.

이 저장소는 Jules를 human contributor처럼 포장하는 표현을 피합니다.

이 프로젝트가 전달하려는 메시지는 다음입니다.

> Human maintainer가 AI coding agent를 GitHub-native engineering practice 안에서 리드할 수 있다.

아래 메시지가 아닙니다.

> AI가 프로젝트 전체를 혼자 만들었다.

---

## Getting Started

### 1. Repository를 Starter Kit으로 사용하기

필요한 부분을 복사해서 사용할 수 있습니다.

- `AGENTS.md`
- `.github/ISSUE_TEMPLATE`
- `.github/workflows/jules-issueops.yml`
- `.github/pull_request_template.md`
- `docs/`
- `prompts/`

### 2. Jules를 한 번만 연결하기

초기 setup에서는 Jules web app에서 GitHub repository 연결과 API key 발급이 필요할 수 있습니다.

setup 이후에는 GitHub Issues, Actions, PRs, Reviews 중심으로 운영하는 것이 목표입니다.

### 3. Jules API Key를 GitHub Secrets에 추가하기

API key는 repository secret으로 저장합니다.

```text
JULES_API_KEY
```

API key를 repository에 commit하면 안 됩니다.

### 4. 범위가 명확한 Issue 만들기

작고 구체적인 task부터 시작합니다.

좋은 예시:

```text
Add AGENTS.md for Jules workflow rules.
Add markdown documentation CI.
Add a pull request template for AI-assisted contributions.
```

다음처럼 모호한 task는 피합니다.

```text
Make this project better.
```

### 5. GitHub에서 Jules Trigger하기

trigger label을 추가합니다.

```text
run-jules
```

그러면 GitHub Actions가 Jules를 호출하고, 해당 issue를 해결하는 focused PR 생성을 요청합니다.

### 6. Merge 전에 Review하기

Merge 전에 다음을 확인합니다.

- PR이 issue를 해결하는가?
- scope가 통제되어 있는가?
- 관련 없는 파일이 바뀌지 않았는가?
- tests 또는 validation steps가 있는가?
- CI가 통과하는가?
- 구현이 유지보수 가능한가?
- 나중에 다른 개발자가 이 history를 이해할 수 있는가?

---

## Who This Is For

이 저장소는 다음 사람들을 위한 것입니다.

- AI coding agent를 실험하는 open-source maintainer
- GitHub-native AI workflow를 원하는 개발자
- GitHub Issue와 PR로 capstone project를 운영하려는 학생
- IssueOps 기반 AI task delegation을 반복 가능하게 만들고 싶은 팀
- AI coding work를 reviewable하게 만들고 싶은 사람

---

## Project Status

이 저장소는 reusable workflow template이자 public playbook으로 구축 중입니다.

초기 초점은 다음입니다.

- README
- AGENTS.md
- GitHub Issue templates
- Jules IssueOps workflow
- PR template
- CI examples
- case study documentation

---

## License

추천 license:

- MIT License: 넓은 재사용에 적합
- Apache-2.0: patent language가 필요한 경우
- CC BY 4.0: documentation-heavy reuse에 적합

---

## Core Message

대부분의 AI coding demo는 완성된 코드만 보여줍니다.

이 프로젝트는 과정을 보여줍니다.

```text
Issue.
Action run.
Prompt.
Pull request.
Review.
CI.
History.
```

진짜 AI-assisted engineering은 여기서 일어납니다.
