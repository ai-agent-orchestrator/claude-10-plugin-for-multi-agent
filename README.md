# 10 Claude Code Plugins for Multi-Agent Systems & Productivity

> A curated selection of 10 practical plugins from [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official), organized by **system architecture, security & loop control** and **research & documentation productivity**.
> Intended as a **feature reference table for reusing these plugins as modules** later.

**English** | [한국어](https://github.com/ai-agent-orchestrator/claude-10-plugin-for-multi-agent/tree/readme-ko)

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
| 7 | `session-report` | Summarizes long work/research sessions into structured logs of completed tasks, changes, and key decisions | Context compression for distilling long research threads into concise records |
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

```bash
claude
/plugin install security-guidance@claude-plugins-official
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
| Session summary & memory | `session-report`, `claude-md-management` | Structured summary template, guideline update rules |
| Visualization output | `playground` | Single-file HTML generation template |
| Playbook standardization | `skill-creator`, `explanatory-output-style` | `SKILL.md` format, evals, trade-off output rules |

---

## Practical Tips

- **Prefer the `/plugins` directory:** it is maintained by the Anthropic team and consists mostly of plain prompts and Python hooks. `/external_plugins` mixes in third-party MCP integrations, so check the config file (`.mcp.json`) first.
- **Portable by copying files:** even without Claude Code, `agents/*.md` and `skills/*/SKILL.md` contain clean role definitions and output-control prompts you can move into other LLM pipelines.

---

## Notes & Caveats

- Plugin names, features, and file paths here are transcribed from the provided summary notes and were not independently verified against the upstream repository. Check the actual structure and license before extracting modules.
- Upstream: <https://github.com/anthropics/claude-plugins-official>
