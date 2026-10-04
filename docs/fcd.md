# FCD (FUA CODE) — DeepSeek Agent Guide

FCD is a free, closed-source terminal & desktop AI coding agent by FUA STUDIO. It ships a streaming CLI (`fcd.exe`), a liquid-glass Qt desktop (`fcd-desktop.exe`), a Linux binary and an Android app — all driven by the same agent core. This guide walks through installing FCD, wiring it to DeepSeek models, and running your first tasks, including the multi-agent **FUA Workflow (FWF)** mode.

## Features

- Streaming CLI + Qt liquid-glass desktop (Windows / Linux / Android)
- Built-in tools: read/write/edit files, glob, grep, shell commands; MCP server presets
- **Approval Agent**: every tool call is risk-assessed by an independent judge model before execution (APPROVE / DENY / ASK-user)
- **FUA Workflow (FWF)**: 2–6 built-in agents work in parallel (leader / planner / workers), with group chat and DMs
- Weekly usage quotas, redeemable plan codes, session persistence, context auto-compaction

## Installation

### Windows

1. Download `FCD-Setup.exe` from the FCD GitHub Releases page and run it. The installer deploys `fcd.exe` (CLI), `fcd.ico` and Start-menu / desktop shortcuts.
2. Optionally download `fcd-desktop.exe` (single-file Qt desktop) for the GUI experience.

### Linux

Download `fcd.elf`, mark it executable and run it:

```bash
chmod +x fcd.elf
./fcd.elf
```

### Android

Install `FCD-0.0.1.apk` (no root required). The Android build exposes the same chat loop with a mobile-friendly tool set.

## Configuration — DeepSeek models

FCD speaks the OpenAI-compatible `chat/completions` protocol, which DeepSeek serves at `https://api.deepseek.com/v1`.

1. Start `fcd` and add your DeepSeek endpoint with your API key (create one at <https://platform.deepseek.com/api_keys>):

   ```
   /add https://api.deepseek.com/v1 deepseek-v4-pro <YOUR_API_KEY>
   ```

2. Switch the default model (supports index / name):

   ```
   /models deepseek-v4-pro
   ```

3. For faster, cheaper turns use the flash tier:

   ```
   /add https://api.deepseek.com/v1 deepseek-v4-flash <YOUR_API_KEY>
   /models deepseek-v4-flash
   ```

### Enable the 1M context window

DeepSeek's v4 models expose a **1,000,000-token context window**. FCD stores per-model context limits in `data/config.json`; set `max_context_tokens` to 1,000,000 on the model entry you added:

```json
{
  "models": [{
    "id": "…",
    "model": "deepseek-v4-pro",
    "max_context_tokens": 1000000,
    "max_output_tokens": 384000
  }]
}
```

FCD automatically compacts history as the conversation approaches the configured budget, so very large repositories stay usable in a single session.

### Max thinking / reasoning effort

DeepSeek v4 supports a maximum reasoning effort. In FCD, turn thinking on and push effort to `max`:

```
/think on
/think-effort max
```

FCD maps this to the OpenAI-compatible `reasoning_effort: max` parameter for DeepSeek requests. Do not disable thinking as a workaround for API errors — with v4 models, `max` effort is stable and gives the best code quality.

> Pricing is not listed here; always verify against the official DeepSeek pricing page before budgeting.

## First run

From a project directory, launch `fcd` and try a real coding task:

```
> 找出 src 下所有 TODO 并汇总成表格
> 把 utils/time.py 重构成 dataclass 并保持 API 兼容，跑通测试
```

FCD streams the model's answer as Markdown, shows every tool call, and supports `/adm <M|auto|ALL>` approval modes:

- `auto` (default): the **Approval Agent** independently risk-checks each operation before it runs. Safe reads pass instantly; risky or out-of-scope actions are **asked to you** (`y/N`) — the judge only ever sees the tool name and argument summary, never file contents, so prompt-injection inside files cannot bypass the gate.
- `M`: confirm every tool call manually.
- `ALL`: fully automatic.

Other useful commands: `/usage` (quota bar), `/redeem <code>` (plan codes), `/mcp` (MCP presets), `/clear` (reset context).

## FUA Workflow (FWF) — multi-agent mode

FWF runs several built-in agents as a team: 1 **leader**, 1 **planner** and the rest **workers** (2–6 agents total).

```
/fwf on                          # default roster: 3 free built-in models
/fwf on deepseek-v4-pro deepseek-v4-flash deepseek-v4-pro --judge deepseek-v4-flash
/fwf off
```

- The **planner** proposes `PLAN: [step1]|[step2]|…`, the **leader** reviews it (`PLAN-REVIEW: APPROVE / REVISE`), then assigns `TASK: [i] …` lines; workers execute **in parallel** and report back; the leader posts `FINAL: …`.
- Talk to the whole team by just typing (group broadcast), or DM one member with `@2 你的问题`.
- Usage is consumed at **N× speed** (each agent counts its own time); FWF asks for confirmation **before** starting and warns about prompt-injection risk — external skills / MCP servers are not recommended inside FWF.
- Every member's tool call still goes through the independent **Approval Agent** first.

## Resources

- [GitHub repository](https://github.com/FUA-Studio/FCD) — releases, downloads and announcements
- In-app docs: `/help`, `/mcp`, `/fwf` status output
