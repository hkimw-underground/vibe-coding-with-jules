# Jules를 위한 AI 코딩 워크플로우 스타터 키트

[English](./README.md) · [한국어](./README.ko.md) · [프로젝트 준비 상태](./docs/meta/project-readiness.md) · [출시 체크리스트](./docs/meta/release-checklist.md) · [기여하기](./CONTRIBUTING.md) · [행동 강령](./CODE_OF_CONDUCT.md) · [보안](./SECURITY.md)

> 대부분의 AI 코딩 데모는 완성된 코드만 보여줍니다.  
> 이 프로젝트는 그 과정 자체를 보여줍니다.

**AI Coding Workflow Starter Kit for Jules**는 AI 코딩 에이전트인 Jules를 전문적인 엔지니어링 프로세스로 이끌기 위한 GitHub 네이티브 플레이북입니다. AI 보조 작업을 "마법 같은 프롬프트"에서 벗어나 Issue, Pull Request, Review, CI의 영역으로 옮깁니다.

---

## 트랙 선택하기

Jules와 어떻게 일하고 싶으신가요? 목표에 맞는 트랙을 선택하세요.

| 트랙 | 목표 | 추천 대상 | 레벨 |
| --- | --- | --- | --- |
| **Review-Driven** | **기본 권장.** 높은 품질과 깔끔한 이력. | 모두에게 권장 | 1 |
| **GitHub-Native Collaboration** | 전문적인 워크플로우 학습. | 학생 및 교사 | 1 |
| **Half Vibe Coding** | CI 게이트를 활용한 빠른 반복 작업. | 숙련된 사용자 | 2-3 |
| **Full Vibe Coding** | **실험적.** 자율적인 샌드박스 실험. | 연구자 및 실험가 | 5-6 |

---

## 시작하기

1. **[Quickstart 가이드](./docs/quickstart.md)** — 첫 번째 Jules 태스크를 시작하기 위한 단계별 온보딩.
2. **스타터 키트 복사** — `AGENTS.md`, `.github/`, `prompts/` 폴더를 프로젝트에 추가하세요.
3. **Issue 열기** — Jules가 해결할 작고 명확한 태스크를 정의하세요.
4. **Review & Merge** — PR과 CI 프로세스를 통해 Jules를 리드하세요.

---

## 기본 워크플로우 작동 방식

**Review-Driven** 트랙은 이 프로젝트가 권장하는 표준 방식입니다. 사람이 아키텍처를 통제하고 Jules가 구현을 담당하도록 보장합니다.

1. **Issue**: 메인테이너가 구체적인 태스크를 정의합니다.
2. **Task**: Jules가 변경 사항을 계획하고 구현합니다.
3. **Pull Request**: Jules가 해당 Issue와 연결된 PR을 생성합니다.
4. **CI**: 자동화된 체크를 통해 변경 사항을 검증합니다.
5. **Review**: 메인테이너가 코드를 리뷰하고 필요한 경우 수정을 요청합니다.
6. **Merge**: 메인테이너가 최종 머지 결정을 내립니다.

---

## 포함된 내용

- **범위가 제한된 Issue 템플릿**: Jules 태스크 및 실험을 위해 사전 설정됨.
- **PR 템플릿**: 검증 체크리스트가 포함된 표준화된 형식.
- **워크플로우 레벨**: 사람 주도 태스크부터 실험적 자율성까지 단계별 구분.
- **참조 예시**: 실제 Issue 및 메인테이너 리뷰 사례.
- **CI 검증**: Markdown 및 YAML 위생을 위한 가벼운 체크 도구.
- **재사용 가능한 프롬프트**: 업무 전달 및 상태 보고용 템플릿.

---

## 케이스 스터디

- **[Case Study A: 디지털 논리 회로](./docs/case-studies/digital-logic-circuit.md)** — Jules 워크플로우를 적용한 하드웨어/소프트웨어 캡스톤 프로젝트.
- **[Case Study B: md-link-linter](./docs/case-studies/english-only-project.md)** — (예정) CI 우선 접근 방식으로 구축된 미니멀 Markdown 링크 체커.

---

## 안전 및 책임

- **사람 중심**: 사람이 방향을 결정하고 아키텍처를 소유합니다.
- **에이전트로서의 Jules**: Jules는 AI 코딩 에이전트이며, 인간 기여자로 포장되지 않습니다.
- **CI 게이트**: 모든 머지는 자동화된 체크(CI)를 통과해야 합니다.
- **실험용 샌드박스**: Full Vibe Coding은 반드시 샌드박스 환경에서만 수행되어야 합니다.

---

## 라이선스

이 프로젝트는 [MIT 라이선스](./LICENSE)를 따릅니다.
