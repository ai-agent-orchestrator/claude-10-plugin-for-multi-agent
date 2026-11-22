# Claude Code 플러그인 10선 — 멀티 에이전트 & 생산성 모듈 가이드

> **10개 활용 범주에 해당하는 실제 플러그인 14개를 포함한 설치형 마켓플레이스**입니다.
> 요청한 [`ai-agent-orchestrator/claude-plugins-official`](https://github.com/ai-agent-orchestrator/claude-plugins-official)에서 플러그인 본체를 가져왔으며, 아래에서 다운로드하거나 Claude Code에 설치할 수 있습니다.

[English](https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent/tree/readme-en) | **한국어**

## 바로 다운로드 · 설치

**[전체 플러그인 ZIP 다운로드](https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent/archive/refs/heads/readme-ko.zip)** · **[플러그인 파일 보기](plugins/)**

ZIP에는 `plugins/` 아래 실제 훅·에이전트·스킬·스크립트·언어 서버 연동 설정과 `.claude-plugin/marketplace.json`이 들어 있습니다. 서브모듈 초기화나 별도 원본 저장소 다운로드가 필요하지 않습니다.

Claude Code **대화창**에서 마켓플레이스를 한 번 등록한 뒤 필요한 플러그인을 설치하세요.

```text
/plugin marketplace add ai-agent-orchestrator/claude-10-plugin-for-multi-agent
/plugin install security-guidance@claude-10-multi-agent
/plugin install feature-dev@claude-10-multi-agent
/plugin install pr-review-toolkit@claude-10-multi-agent
```

전체 14개를 설치하려면 등록 후 아래 명령을 각각 실행합니다.

```text
/plugin install security-guidance@claude-10-multi-agent
/plugin install hookify@claude-10-multi-agent
/plugin install ralph-loop@claude-10-multi-agent
/plugin install feature-dev@claude-10-multi-agent
/plugin install code-review@claude-10-multi-agent
/plugin install pr-review-toolkit@claude-10-multi-agent
/plugin install pyright-lsp@claude-10-multi-agent
/plugin install jdtls-lsp@claude-10-multi-agent
/plugin install session-report@claude-10-multi-agent
/plugin install project-md-management@claude-10-multi-agent
/plugin install playground@claude-10-multi-agent
/plugin install skill-creator@claude-10-multi-agent
/plugin install explanatory-output-style@claude-10-multi-agent
/plugin install plugin-dev@claude-10-multi-agent
```

`claude-md-management`는 최신 Claude Code의 제3자 플러그인 이름 제한 때문에 **`project-md-management`**로 설치합니다. 폴더 이름은 원본대로 유지하며 기능은 같습니다. 상세 변경은 [출처·라이선스 안내](THIRD_PARTY_NOTICES.md)에 기록했습니다.

### 로컬 파일로 사용

터미널에서 저장소를 받거나 위 ZIP을 풀어 사용하세요.

```bash
git clone https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent.git
cd claude-10-plugin-for-multi-agent
claude plugin marketplace add .
claude plugin install feature-dev@claude-10-multi-agent
```

마켓플레이스 등록 없이 한 세션에서만 불러올 수도 있습니다.

```bash
claude --plugin-dir ./plugins/feature-dev
```

### 포함된 플러그인 본체

| 활용 범주 | 실제 파일 | 설치 이름 |
|:--|:--|:--|
| 보안 가드레일 | [security-guidance](plugins/security-guidance/) | `security-guidance` |
| 이벤트 훅 | [hookify](plugins/hookify/) | `hookify` |
| 반복 제어 | [ralph-loop](plugins/ralph-loop/) | `ralph-loop` |
| 역할 분담 개발 | [feature-dev](plugins/feature-dev/) | `feature-dev` |
| 코드 리뷰 | [code-review](plugins/code-review/) | `code-review` |
| PR 리뷰 | [pr-review-toolkit](plugins/pr-review-toolkit/) | `pr-review-toolkit` |
| Python 언어 서버 | [pyright-lsp](plugins/pyright-lsp/) | `pyright-lsp` |
| Java 언어 서버 | [jdtls-lsp](plugins/jdtls-lsp/) | `jdtls-lsp` |
| 세션 사용량 보고서 | [session-report](plugins/session-report/) | `session-report` |
| 프로젝트 지침 관리 | [claude-md-management](plugins/claude-md-management/) | `project-md-management` |
| HTML 시각화 | [playground](plugins/playground/) | `playground` |
| 스킬 제작·평가 | [skill-creator](plugins/skill-creator/) | `skill-creator` |
| 설명형 출력 | [explanatory-output-style](plugins/explanatory-output-style/) | `explanatory-output-style` |
| 플러그인 제작 | [plugin-dev](plugins/plugin-dev/) | `plugin-dev` |

설치 이름 뒤에 `@claude-10-multi-agent`를 붙이면 이 저장소에 포함된 버전이 설치됩니다.

### 실행 환경과 파일 검증

Claude Code를 설치·인증한 환경에서 사용합니다. 훅의 외부 의존성은 각 플러그인 설정과 문서를 확인하세요. 예를 들어 `ralph-loop`는 Bash·`jq`·Perl, `security-guidance`는 Bash·Python, `hookify`는 Python 3을 사용합니다. `session-report`는 Node.js가 필요합니다. Windows의 Bash 훅에는 Git Bash 등 Bash 환경이 필요합니다.

LSP 플러그인은 **연동 설정**을 포함합니다. 실제 `pyright-langserver` 또는 `jdtls` 실행 파일은 별도로 설치해 `PATH`에 두어야 합니다. 설치 방법은 [Python 안내](plugins/pyright-lsp/README.md)와 [Java 안내](plugins/jdtls-lsp/README.md)를 확인하세요.

```bash
python scripts/verify_plugins.py
claude plugin validate .
```

[plugins.lock.json](plugins.lock.json)에 원본 커밋과 파일별 체크섬을 고정했습니다. 설치 구성은 [Claude Code 공식 마켓플레이스 문서](https://code.claude.com/docs/en/plugin-marketplaces)를 따릅니다.

---

## 목차

1. [개요](#개요)
2. [Part 1. 개발·아키텍처·에이전트 제어용](#part-1-개발아키텍처에이전트-제어용)
3. [Part 2. 리서치·문서 정리·생산성용](#part-2-리서치문서-정리생산성용)
4. [어디에서 쓰는가: 3가지 사용 방식](#어디에서-쓰는가-3가지-사용-방식)
5. [모듈 이식 가이드](#모듈-이식-가이드)
6. [실전 팁](#실전-팁)
7. [참고 및 주의사항](#참고-및-주의사항)

---

## 개요

원본 저장소는 Claude Code에서 바로 쓸 수 있는 **스킬(`SKILL.md`) · 에이전트 · 훅(Hook)** 설계 블루프린트 모음입니다. 이 문서는 그중 멀티 에이전트 오케스트레이터, 보안·비용 제어 백엔드, 리서치·문서 정리 업무에 가장 가치가 높은 10개를 정리합니다.

---

## Part 1. 개발·아키텍처·에이전트 제어용

| # | 플러그인 | 핵심 기능 | 활용 및 코드 추출 포인트 |
|:-:|:--|:--|:--|
| 1 | `security-guidance` | 파일 편집(Edit/Write)·턴 종료(Stop)·커밋 시점, 3단계로 보안 취약점 자동 스캔 | `security_reminder_hook.py`와 규칙 패턴(정규식 + LLM 검증 하이브리드)을 서버 가드레일·입력 검증 모듈에 적용 |
| 2 | `hookify` | 마크다운 설정만으로 `bash`, `file`, `stop`, `prompt` 이벤트 훅 생성·관리 | 위험한 명령 실행·루프 진입 전에 사전/사후 제어 훅을 거는 인터셉터 설계 레퍼런스 |
| 3 | `ralph-loop` | Stop Hook으로 종료를 가로채고 `--max-iterations` 한도 내에서 작업을 반복 개선 | 목표 품질까지 자체 검증·수정하되 무한 루프(과금 폭탄)를 차단하는 루프 제어 표준 패턴 |
| 4 | `feature-dev` | 탐색(Explorer) → 아키텍처 설계(Architect) → 구현 → 품질 리뷰(Reviewer)의 7단계 역할 분담 워크플로우 | 한 AI에게 통째로 맡기지 않고 기획·설계·검수 에이전트를 분리 오케스트레이션하는 프롬프트와 상태 전이 설계 |
| 5 | `code-review` / `pr-review-toolkit` | 4~6개 병렬 서브 에이전트가 버그·타입·침묵하는 실패(Silent Failure)를 교차 검증, 신뢰도 80점 미만 노이즈 필터링 | 병렬 에이전트 결과를 취합해 환각·오탐을 걸러내는 스코어링·필터링 알고리즘 |
| 6 | `pyright-lsp` / `jdtls-lsp` | Python·Java 언어 서버를 연동해 실제 타입·컴파일 오류를 실시간 진단 | 존재하지 않는 메서드·잘못된 타입을 생성하는 코드 환각 감소(백엔드 개발) |

---

## Part 2. 리서치·문서 정리·생산성용

| # | 플러그인 | 핵심 기능 | 활용 및 참고 포인트 |
|:-:|:--|:--|:--|
| 7 | `session-report` | 로컬 Claude Code 세션 기록에서 토큰·캐시 효율·서브에이전트·비용이 큰 프롬프트를 HTML 보고서로 분석 | 작업 세션의 사용량·비용·에이전트 활용 현황 점검 |
| 8 | `claude-md-management` | 세션에서 도출된 규칙·학습 내용을 `/revise-claude-md`로 프로젝트 지침서에 자동 반영 | 매번 지침을 다시 쓰지 않고 누적 규칙을 일관되게 유지 |
| 9 | `playground` | 조사 데이터, 문서 비평(document-critique), 개념도(concept-map)를 단일 인터랙티브 HTML 파일로 생성 | 별도 서버 없이 복잡한 자료·타임라인을 한눈에 시각화 |
| 10 | `skill-creator` / `explanatory-output-style` | 반복 업무를 `SKILL.md`로 패키징하고 evals로 성능 평가(`skill-creator`), 설계 트레이드오프 인사이트를 함께 출력(`explanatory-output-style`) | 반복 검토 체크리스트를 재사용·검증 가능한 표준 플레이북으로 모듈화 |

> 참고: 원문 요약에는 `plugin-dev`(`skill-creator`와 함께 SKILL.md 패키징·평가를 돕는 메타 도구)도 언급되어 있습니다. 이 문서에서는 #10 `skill-creator`와 같은 용도로 묶어 다룹니다.

---

## 어디에서 쓰는가: 3가지 사용 방식

이 플러그인들은 기본적으로 **터미널 CLI인 Claude Code 전용**입니다. 웹 `claude.ai` 채팅창과는 동작 방식이 다릅니다.

| 사용 환경 | 사용 가능 | 구체적인 활용 방법 |
|:--|:-:|:--|
| **Claude Code (터미널 CLI)** | O (기본 설계 목적) | `/plugin install` 명령으로 설치해 훅·스킬을 실시간 자동 적용 |
| **일반 웹 Claude (claude.ai)** | △ (수동 복붙) | 설치 불가. 폴더 내 `.md` 프롬프트를 복사해 Project 지침(Custom Instructions)이나 채팅 프롬프트에 사용 |
| **직접 만든 중심 에이전트 (Python)** | O (강력 추천) | ① `claude` CLI를 subprocess로 호출하거나 ② `.md` 프롬프트와 `.py` 훅만 떼어내 내 파이프라인에 이식 |

### 1) Claude Code (터미널 CLI)

```text
/plugin marketplace add ai-agent-orchestrator/claude-10-plugin-for-multi-agent
/plugin install security-guidance@claude-10-multi-agent
```

설치 후에는 Claude가 로컬 파일을 수정하거나 터미널 명령을 실행할 때마다 플러그인의 파이썬 훅(`hooks/*.py`)과 지침(`SKILL.md`)이 자동으로 개입합니다.

### 2) 일반 웹 Claude (claude.ai)

웹 버전에는 플러그인 설치 버튼이 없습니다. 대신 `feature-dev`, `session-report` 등 폴더 안의 `SKILL.md`·`agents/*.md`를 열어 역할 부여·출력 통제·검증 프롬프트를 복사해 Project 지침이나 일반 채팅에 붙여 넣으면 같은 역할 분담과 문서 정리를 시킬 수 있습니다.

### 3) 직접 만든 중심 에이전트와 연결 (추천)

Python 기반 오케스트레이터(CEO/CTO/Coder 구조, LangGraph 파이프라인 등)와 결합할 때 효과가 큽니다.

- **방법 A — CLI 서브 에이전트로 호출:** 중심 Python 에이전트가 코딩·코드 리뷰를 하청 줄 때 백그라운드로 `claude` CLI 프로세스를 띄우고 특정 플러그인 스킬만 활성화해 실행합니다.
- **방법 B — 로직·프롬프트만 Python 모듈로 이식 (추천):** `claude` CLI 의존성까지 없애고 알맹이만 편입합니다.

---

## 모듈 이식 가이드

플러그인 폴더에서 두 종류만 떼어내면 됩니다.

| 원본 파일 | 이식 대상 | 용도 |
|:--|:--|:--|
| `agents/*.md`, `skills/*/SKILL.md` | LangGraph 등 에이전트 노드의 **System Prompt** | 역할 정의·출력 통제 프롬프트 |
| `hooks/*.py` (예: `security_reminder_hook.py`) | Python/FastAPI 서버의 **입력·출력 가드레일 미들웨어** 함수 | 보안 검사·실행 차단 |

### 플러그인별 이식 매핑 (모듈화용)

| 모듈 용도 | 가져올 플러그인 | 가져올 부분 |
|:--|:--|:--|
| 보안 가드레일 | `security-guidance` | `hooks/security_reminder_hook.py`, 규칙 패턴 |
| 실행 전/후 인터셉터 | `hookify` | 이벤트별(`bash`/`file`/`stop`/`prompt`) 규칙 구조 |
| 반복 횟수·비용 제어 | `ralph-loop` | Stop Hook + `--max-iterations` 로직 |
| 역할 분담 오케스트레이션 | `feature-dev` | 단계별 에이전트 프롬프트, 상태 전이 |
| 결과 취합·필터링 | `code-review`, `pr-review-toolkit` | 병렬 에이전트 집계, 신뢰도 80점 컷오프 |
| 코드 환각 방지 | `pyright-lsp`, `jdtls-lsp` | 언어 서버 진단 연동 |
| 세션 분석·메모리 | `session-report`, `claude-md-management` | 사용량 HTML 보고서, 지침 갱신 규칙 |
| 시각화 산출물 | `playground` | 단일 HTML 생성 템플릿 |
| 플레이북 표준화 | `skill-creator`, `explanatory-output-style` | `SKILL.md` 포맷, evals, 트레이드오프 출력 규칙 |

---

## 실행 가능한 예제 (`examples/`)

위 패턴을 독립적으로 구현한 예시 코드입니다. 원본 플러그인 코드를 복사한 것이 **아닙니다**. 표준 라이브러리만 사용하며, LangGraph 빌드만 선택 사항입니다.

| 파일 | 참고한 패턴 | 제공 기능 |
|:--|:--|:--|
| [`guardrail.py`](examples/guardrail.py) | `security-guidance`, `hookify` | 정규식 사전 스캔 + 교체 가능한 LLM 검증기. `guard()`로 에이전트 호출을 입출력 미들웨어로 감쌈 |
| [`loop_control.py`](examples/loop_control.py) | `ralph-loop` | `max_iterations`·비용 상한을 가진 `run_loop()`, 종료 사유 반환 |
| [`review_aggregator.py`](examples/review_aggregator.py) | `code-review`, `pr-review-toolkit` | 병렬 리뷰어, 중복 제거, 합의 가점, 신뢰도 80점 컷오프 |
| [`prompt_loader.py`](examples/prompt_loader.py) | 전체 플러그인 | `agents/*.md`, `skills/*/SKILL.md`를 시스템 프롬프트로 로드 |
| [`orchestrator.py`](examples/orchestrator.py) | `feature-dev` | Explorer → Architect → Implementer → Reviewer 파이프라인 (순수 Python / LangGraph) |
| [`cli_subagent.py`](examples/cli_subagent.py) | 방법 A | `claude -p`를 subprocess로 호출 (CLI 필요, 테스트 대상 아님) |

```bash
pip install pytest langgraph   # langgraph는 선택
python -m pytest examples/tests
```

```python
from guardrail import guard
from loop_control import run_loop

safe_agent = guard(my_agent_call)                      # 위험한 입출력 차단
result = run_loop(step, is_done, seed="", max_iterations=5)
```

---

## 실전 팁

- **`/plugins` 디렉터리 우선 활용:** Anthropic 팀이 직접 관리하는 순수 프롬프트·파이썬 훅 위주입니다. `/external_plugins`는 외부 서드파티 MCP 연동이 섞여 있으므로 사용 전 설정 파일(`.mcp.json`)을 먼저 확인하세요.
- **파일 복사만으로 이식 가능:** Claude Code를 쓰지 않아도 각 플러그인의 `agents/*.md`, `skills/*/SKILL.md`만 열어 보면 역할 정의와 출력 통제 프롬프트가 정리되어 있어 다른 LLM 파이프라인에 옮길 수 있습니다.

---

## 참고 및 주의사항

- 포함된 14개 플러그인의 매니페스트·실제 파일·라이선스를 원본과 대조했습니다. `session-report` 설명도 실제 사용량 분석 기능에 맞게 수정했습니다.
- 가져온 저장소: [ai-agent-orchestrator/claude-plugins-official](https://github.com/ai-agent-orchestrator/claude-plugins-official), 고정 커밋 `0412be76f50ab4f4f8abff3753efa9269fbbca5b`.
- 원저작자·라이선스·배포 시 메타데이터 변경: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). 이 저장소는 Anthropic 공식 마켓플레이스와 별개의 큐레이션 배포본입니다.
