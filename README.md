# 10 Claude Code Plugins for Multi-Agent Systems & Productivity

> An **installable marketplace containing 14 actual plugins across 10 practical categories**.
> Plugin source is bundled from [`ai-agent-orchestrator/claude-plugins-official`](https://github.com/ai-agent-orchestrator/claude-plugins-official), ready to download or install in Claude Code.

**English** | [한국어](https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent/tree/readme-ko)

## Download and install

**[Download all plugins as a ZIP](https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent/archive/refs/heads/readme-en.zip)** · **[Browse plugin files](plugins/)**

The ZIP includes the actual hooks, agents, skills, scripts, language-server integration settings, and `.claude-plugin/marketplace.json`. No submodule initialization or separate upstream checkout is needed.

In a **Claude Code conversation**, register this marketplace once and install the plugins you need:

```text
/plugin marketplace add ai-agent-orchestrator/claude-10-plugin-for-multi-agent
/plugin install security-guidance@claude-10-multi-agent
/plugin install feature-dev@claude-10-multi-agent
/plugin install pr-review-toolkit@claude-10-multi-agent
```

To install the full selection, run these commands individually after registration:

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

The bundled `claude-md-management` installs as **`project-md-management`** because current Claude Code reserves the `claude-` prefix for Anthropic plugins. Its directory keeps the upstream name and its behavior is unchanged. See [third-party notices](THIRD_PARTY_NOTICES.md) for the metadata adaptation.

### Use local files

Clone this branch, or extract the ZIP above, then register the local directory:

```bash
git clone --branch readme-en https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent.git
cd claude-10-plugin-for-multi-agent
claude plugin marketplace add .
claude plugin install feature-dev@claude-10-multi-agent
```

For a single session without registering a marketplace:

```bash
claude --plugin-dir ./plugins/feature-dev
```

### Bundled plugins

| Purpose | Actual source files | Install name |
|:--|:--|:--|
| Security guardrails | [security-guidance](plugins/security-guidance/) | `security-guidance` |
| Event hooks | [hookify](plugins/hookify/) | `hookify` |
| Iteration control | [ralph-loop](plugins/ralph-loop/) | `ralph-loop` |
| Role-separated development | [feature-dev](plugins/feature-dev/) | `feature-dev` |
| Code review | [code-review](plugins/code-review/) | `code-review` |
| PR review | [pr-review-toolkit](plugins/pr-review-toolkit/) | `pr-review-toolkit` |
| Python language server | [pyright-lsp](plugins/pyright-lsp/) | `pyright-lsp` |
| Java language server | [jdtls-lsp](plugins/jdtls-lsp/) | `jdtls-lsp` |
| Session usage reports | [session-report](plugins/session-report/) | `session-report` |
| Project instructions | [claude-md-management](plugins/claude-md-management/) | `project-md-management` |
| Interactive HTML | [playground](plugins/playground/) | `playground` |
| Skill creation and evaluation | [skill-creator](plugins/skill-creator/) | `skill-creator` |
| Explanatory output | [explanatory-output-style](plugins/explanatory-output-style/) | `explanatory-output-style` |
| Plugin development | [plugin-dev](plugins/plugin-dev/) | `plugin-dev` |

Append `@claude-10-multi-agent` to the install name to use the version bundled here.

### Requirements and verification

Use an installed, authenticated Claude Code CLI. Check each plugin's files and documentation for its external dependencies. For example, `ralph-loop` uses Bash, `jq`, and Perl; `security-guidance` uses Bash and Python; `hookify` uses Python 3; and `session-report` uses Node.js. Bash hooks on Windows need a Bash environment such as Git Bash.

The LSP plugins bundle **integration settings**. Install the actual `pyright-langserver` or `jdtls` executable separately and put it on `PATH`. See the [Python instructions](plugins/pyright-lsp/README.md) and [Java instructions](plugins/jdtls-lsp/README.md).

```bash
python scripts/verify_plugins.py
claude plugin validate .
```

[plugins.lock.json](plugins.lock.json) pins the upstream commit and per-file checksums. Installation follows the [official Claude Code marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

---

## Table of Contents

1. [Overview](#overview)
2. [Part 1. Architecture, Security & Agent Control](#part-1-architecture-security--agent-control)
3. [Part 2. Research, Documentation & Productivity](#part-2-research-documentation--productivity)
4. [Where to Use Them: 3 Ways](#where-to-use-them-3-ways)
5. [Module Extraction Guide](#module-extraction-guide)
6. [Practical Tips](#practical-tips)
7. [Notes & Caveats](#notes--caveats)

---

## Overview

The upstream repository is a collection of design blueprints for **skills (`SKILL.md`), agents, and hooks** that work out of the box in Claude Code. This document picks the 10 most valuable for multi-agent orchestrators, security/cost-control backends, and research/documentation work.

---

## Part 1. Architecture, Security & Agent Control

| # | Plugin | Core Function | Key Takeaway / Extraction Point |
|:-:|:--|:--|:--|
| 1 | `security-guidance` | Scans for security vulnerabilities at 3 lifecycle stages: file edit/write, turn end (Stop), and commit | Reuse `security_reminder_hook.py` and its rule patterns (regex + LLM verification hybrid) in server guardrails and input validation |
| 2 | `hookify` | Creates and manages `bash`, `file`, `stop`, and `prompt` event hooks from simple Markdown rules | Reference design for pre/post-execution interceptors that stop dangerous commands or runaway loops |
| 3 | `ralph-loop` | Intercepts termination via a Stop Hook and iterates up to `--max-iterations` | Standard loop-control pattern: self-verify and refine until quality is met while preventing infinite loops and runaway cost |
| 4 | `feature-dev` | 7-step role-separated workflow: Explorer → Architect → Implementer → Reviewer | Prompts and state transitions for orchestrating separate planning, design, and review agents instead of one monolithic prompt |
| 5 | `code-review` / `pr-review-toolkit` | 4–6 parallel sub-agents cross-check bugs, types, and silent failures; findings below confidence 80 are filtered out | Scoring/filtering algorithm for aggregating parallel agent outputs and removing hallucinations and false positives |
| 6 | `pyright-lsp` / `jdtls-lsp` | Integrates Python and Java language servers for real-time type and compile diagnostics | Grounds code generation to cut hallucinated methods and wrong types in backend development |

---

## Part 2. Research, Documentation & Productivity

| # | Plugin | Core Function | Key Takeaway / Reference Value |
|:-:|:--|:--|:--|
| 7 | `session-report` | Generates HTML reports of tokens, cache efficiency, subagents, and expensive prompts from local Claude Code session transcripts | Inspect session usage, costs, and agent activity |
| 8 | `claude-md-management` | Updates project guidelines from session learnings via `/revise-claude-md` | Keeps accumulated agent rules consistent without rewriting instructions each time |
| 9 | `playground` | Generates a single standalone interactive HTML file for research data, document critiques (`document-critique`), and concept maps (`concept-map`) | Zero-server visualization of complex material and timelines |
| 10 | `skill-creator` / `explanatory-output-style` | Packages repeatable workflows into `SKILL.md` with evals (`skill-creator`); outputs design trade-off insights alongside results (`explanatory-output-style`) | Turns repetitive review checklists into reusable, testable playbooks |

> Note: the source summary also mentions `plugin-dev`, a meta tool that, like `skill-creator`, helps package and evaluate SKILL.md playbooks. It is treated here together with #10 `skill-creator`.

---

## Where to Use Them: 3 Ways

These plugins are designed for **Claude Code, the terminal CLI**. They do not work like the web `claude.ai` chat.

| Environment | Usable | How to use |
|:--|:-:|:--|
| **Claude Code (terminal CLI)** | Yes (primary target) | Install with `/plugin install`; hooks and skills apply automatically in real time |
| **Web Claude (claude.ai)** | Partial (manual copy) | No install option. Copy the `.md` prompts from plugin folders into Project instructions (Custom Instructions) or chat prompts |
| **Your own orchestrator (Python)** | Yes (recommended) | (1) call the `claude` CLI via subprocess, or (2) extract the `.md` prompts and `.py` hooks into your own pipeline |

### 1) Claude Code (terminal CLI)

```text
/plugin marketplace add ai-agent-orchestrator/claude-10-plugin-for-multi-agent
/plugin install security-guidance@claude-10-multi-agent
```

After installation, the plugin's Python hooks (`hooks/*.py`) and instructions (`SKILL.md`) intervene automatically whenever Claude edits local files or runs terminal commands.

### 2) Web Claude (claude.ai)

The web app has no plugin install button. Instead, open `SKILL.md` or `agents/*.md` in folders such as `feature-dev` or `session-report`, and paste the role, output-control, and verification prompts into Project instructions or a regular chat to get the same role separation and document organization.

### 3) Connect to your own central agent (recommended)

Works best with a Python orchestrator (e.g., CEO/CTO/Coder structure or a LangGraph pipeline).

- **Method A — CLI sub-agent:** the central Python agent delegates coding or code review by spawning a background `claude` CLI process with only the chosen plugin skills enabled.
- **Method B — Port logic and prompts into Python modules (recommended):** drop the `claude` CLI dependency and embed only the core pieces.

---

## Module Extraction Guide

Extract two kinds of files from a plugin folder:

| Source file | Port to | Purpose |
|:--|:--|:--|
| `agents/*.md`, `skills/*/SKILL.md` | **System prompt** of a LangGraph (or similar) agent node | Role definitions and output-control prompts |
| `hooks/*.py` (e.g., `security_reminder_hook.py`) | **Input/output guardrail middleware** in a Python/FastAPI server | Security checks and execution blocking |

### Per-plugin extraction map

| Module purpose | Plugin | What to take |
|:--|:--|:--|
| Security guardrail | `security-guidance` | `hooks/security_reminder_hook.py`, rule patterns |
| Pre/post-execution interceptor | `hookify` | Per-event (`bash`/`file`/`stop`/`prompt`) rule structure |
| Iteration and cost control | `ralph-loop` | Stop Hook + `--max-iterations` logic |
| Role-separated orchestration | `feature-dev` | Per-stage agent prompts, state transitions |
| Result aggregation & filtering | `code-review`, `pr-review-toolkit` | Parallel-agent aggregation, confidence-80 cutoff |
| Code hallucination prevention | `pyright-lsp`, `jdtls-lsp` | Language-server diagnostics integration |
| Session analysis & memory | `session-report`, `claude-md-management` | Usage-report HTML, guideline update rules |
| Visualization output | `playground` | Single-file HTML generation template |
| Playbook standardization | `skill-creator`, `explanatory-output-style` | `SKILL.md` format, evals, trade-off output rules |

---

## Runnable Examples (`examples/`)

Independent, illustrative implementations of the patterns above. They are **not** copies of the upstream plugin code. Stdlib only, except the optional LangGraph build.

| File | Pattern from | What it provides |
|:--|:--|:--|
| [`guardrail.py`](examples/guardrail.py) | `security-guidance`, `hookify` | Regex pre-scan + pluggable LLM verifier; `guard()` wraps any agent call as input/output middleware |
| [`loop_control.py`](examples/loop_control.py) | `ralph-loop` | `run_loop()` with `max_iterations` and cost caps, plus a stop reason |
| [`review_aggregator.py`](examples/review_aggregator.py) | `code-review`, `pr-review-toolkit` | Parallel reviewers, dedupe, agreement boost, confidence-80 cutoff |
| [`prompt_loader.py`](examples/prompt_loader.py) | all plugins | Loads `agents/*.md` and `skills/*/SKILL.md` as system prompts |
| [`orchestrator.py`](examples/orchestrator.py) | `feature-dev` | Explorer → Architect → Implementer → Reviewer pipeline, plain Python and LangGraph |
| [`cli_subagent.py`](examples/cli_subagent.py) | Method A | Calls `claude -p` via subprocess (needs the CLI; not covered by tests) |

```bash
pip install pytest langgraph   # langgraph is optional
python -m pytest examples/tests
```

```python
from guardrail import guard
from loop_control import run_loop

safe_agent = guard(my_agent_call)                      # blocks risky input/output
result = run_loop(step, is_done, seed="", max_iterations=5)
```

---

## Practical Tips

- **Prefer the `/plugins` directory:** it is maintained by the Anthropic team and consists mostly of plain prompts and Python hooks. `/external_plugins` mixes in third-party MCP integrations, so check the config file (`.mcp.json`) first.
- **Portable by copying files:** even without Claude Code, `agents/*.md` and `skills/*/SKILL.md` contain clean role definitions and output-control prompts you can move into other LLM pipelines.

---

## Notes & Caveats

- The 14 bundled plugin manifests, files, and licenses were checked against upstream. The `session-report` description now reflects its actual usage-analysis function.
- Imported from [ai-agent-orchestrator/claude-plugins-official](https://github.com/ai-agent-orchestrator/claude-plugins-official), pinned at `0412be76f50ab4f4f8abff3753efa9269fbbca5b`.
- See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for authorship, licenses, and the redistributed metadata adaptation. This is an independent curated collection, separate from Anthropic's official marketplace.
