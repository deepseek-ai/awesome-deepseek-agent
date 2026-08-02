[English](./deepdepcat.md) | [简体中文](./deepdepcat.zh-CN.md) · [↩ Back](../README.md)

# Integrate with DeepDepCat

DeepDepCat is an all-in-one AI desktop workbench (native Tauri + React + Rust app) with two integrated workspaces: a **coding workspace** with permission modes, subagent orchestration, and multi-session parallel conversations; and a **document/office-automation workspace** — Word/PPT/Excel generation, OCR, table processing, media conversion, web fetching — with a live task panel. Both run on DeepSeek V4 with 1M context and configurable reasoning effort.

- **GitHub:** <https://github.com/hanmirage/deepdepcat>
- **Platforms:** Windows / macOS / Linux

#### 1. Install DeepDepCat

Download the installer for your platform from the [releases page](https://github.com/hanmirage/deepdepcat/releases), or build from source:

```sh
git clone https://github.com/hanmirage/deepdepcat.git
cd deepdepcat
npm install
npm run tauri dev
```

#### 2. Configure the DeepSeek provider

Open **Settings → Model Providers**, select the built-in **DeepSeek** provider (it is pre-created):

| Field | Value |
|-------|-------|
| API Key | `sk-...` from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) |
| Base URL | `https://api.deepseek.com` (default) |
| API Format | `OpenAI-compatible` (default) |
| Models | Add `deepseek-v4-pro` and/or `deepseek-v4-flash` — the model picker reads this list directly |

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

> **Tip:** Newly added models default to a **1,000,000-token (1M) context window** — DeepSeek V4 supports up to 1M tokens of context. You can verify/adjust the value per model in the provider settings.

#### 3. Enable deep thinking

DeepSeek V4 Pro supports multiple reasoning effort levels. In DeepDepCat:

- **Settings → General → "DeepSeek 自动优化" (auto reasoning)** — when on, the agent uses `max` reasoning effort for the best coding experience.
- **Input-bar reasoning selector** (Code workspace) — explicitly pick `auto` / `high` / `max` per conversation; `auto` follows the setting above.

#### 4. First run

- **Code workspace**: type a task (e.g. "explain this repo"), pick an interaction mode (confirm / plan / accept edits / auto) and an execution strategy (standard / plan execute / reflexion / tree of thoughts / coordinator) from the input bar.
- **Depwork workspace**: describe a document task (e.g. "generate a Word report from these notes") — the task panel auto-expands on the right with live step progress; you can collapse it anytime.

#### Key Features

| Feature | Description |
|---------|-------------|
| Dual workspaces | Coding + document/office automation in ONE app, each with its own tool set and system prompt |
| Multi-session parallelism | Sessions run concurrently without blocking each other; per-session live indicators and stop buttons in the sidebar |
| Subagent orchestration | Decompose complex tasks into parallel subagents with live activity tracking |
| Ecosystem skill reuse | Reuse existing agent skill ecosystems (Claude/Cursor skills and plugin layouts, e.g. `~/.claude/skills`, `~/.cursor/skills`) |
| 1M context | DeepSeek V4's full context window, with a live context usage ring in the input bar |
| Silent updates | Small releases auto-download and install on app exit — zero interruption |
| Sandbox & permissions | File edits require approval per interaction mode; configurable sandbox profiles |

#### Configuration options (Settings → Model Providers)

| Option | Description |
|--------|-------------|
| `baseUrl` | API base URL, defaults to `https://api.deepseek.com` |
| `apiFormat` | `openai` (OpenAI-compatible) or `anthropic` |
| `context_window` | Per-model context window in tokens — set `1000000` for DeepSeek V4 |
| `reasoning_effort` | `auto` / `high` / `max` — controls how much the model thinks before answering |

Pricing follows the official [DeepSeek pricing pages](https://api-docs.deepseek.com/quick_start/pricing).
