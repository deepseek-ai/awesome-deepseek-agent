[English](./kinetaios.md) | [简体中文](./kinetaios.zh-CN.md) · [← Back](../README.md)

# Integrate with KinetAios

[KinetAios](https://github.com/phinn/KinetAios) is a local-first, multi-engine AI agent dashboard. It runs **Direct (V1 ReAct / V2 / V3 DAG-parallel), Claude Code, Codex, and DeepSeek Harness** side-by-side from one window, with cross-engine long-term memory (SQLite + FTS5) and a built-in MCP server — no account, your LLM API key is the only auth.

This guide shows how to install KinetAios and use the **DeepSeek Harness** engine (or the Direct engine with a DeepSeek model) with your DeepSeek API key.

> DeepSeek renamed its models in April 2026. This guide uses the current names **deepseek-v4-pro** / **deepseek-v4-flash** (not the deprecated `deepseek-chat` / `deepseek-reasoner`). DeepSeek V4 supports up to **1M tokens** of context.

---

#### 1. Install KinetAios

Download the latest release from the [releases page](https://github.com/phinn/KinetAios/releases/latest):

- **Windows** — `KinetAios-Setup-3.3.0.exe` (NSIS installer)
- **macOS** — see releases

> The build is unsigned, so Windows SmartScreen / macOS Gatekeeper will warn — allow manually.

Alternatively, run from source (requires **Node.js 18+** and internet for the `better-sqlite3` native module):

```sh
git clone https://github.com/phinn/KinetAios.git
cd KinetAios/KinetAiosWin
npm install      # postinstall rebuilds better-sqlite3 for Electron
npm run build
npm start
```

> On a CN network, `npm install` may time out fetching the Electron binary. The repo's `.npmrc` is already configured with the npmmirror mirror; on failure run:
> `ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ node node_modules/electron/install.js`

---

#### 2. Get your DeepSeek API key

1. Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
2. Create an API key and copy it.

---

#### 3. Configure the DeepSeek provider

1. Launch KinetAios.
2. Click **⚙** (top-right) → **Settings** → **API**.
3. Pick the **DeepSeek** preset (OpenAI-compatible). It fills in:
   - **Base URL**: `https://api.deepseek.com`
   - **Model**: `deepseek-v4-pro` (use `deepseek-v4-flash` for a faster, cheaper option)
4. Paste your DeepSeek API key into **API Key**.
5. Click **Test connection** — once it passes, the provider is ready.

> KinetAios encrypts the key locally via Electron `safeStorage` (macOS Keychain / Windows DPAPI). No relay server is involved — your key never leaves your machine.

> **1M context window** — DeepSeek V4 supports up to **1,000,000 tokens** of context. KinetAios lets you use the full window:
>
> - **OpenAI-compatible (DeepSeek preset)**: in the per-session model dropdown, set the context budget to `1000000`. The token/char ratio is tracked per protocol so the estimate stays accurate across concurrent sessions.
> - **Anthropic-compatible**: use the model id `deepseek-v4-pro[1m]` (the `[1m]` suffix enables the 1M context tier).
> - If you leave the default, the **auto-compaction** loop still keeps history within budget by summarizing early turns (compaction events are visualized in the UI with before/after token counts).
> - You can also inspect/edit the raw history via the **Context inspector** (Chat tab → context inspector) to verify the live token usage.

> **Max thinking / reasoning effort** — DeepSeek V4 Pro supports multiple reasoning effort levels (`max`, `high`). To get the best coding experience:
>
> - **Direct engine + OpenAI-compatible endpoint**: KinetAios sends `reasoning_effort` in the request body. Set it to `max` in the per-session model dropdown (the Direct engine supports per-protocol token calibration, so reasoning budget is tracked separately from the output budget).
> - **DeepSeek Harness engine**: reasoning effort is forwarded to the `dsh` CLI; pick the `max` level in the per-session model settings so the harness runs with full reasoning.
>
> Don't disable thinking mode as a workaround for API errors — if you hit a reasoning-content passback issue, point users to the upstream fix instead. See the [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode) for details.

---

#### 4. First run

KinetAios exposes DeepSeek through two engines, switchable per session:

- **Direct engine + DeepSeek model** — uses the built-in ReAct loop (Direct V1/V2/V3) with DeepSeek as the LLM. Best for tool-heavy tasks (shell, read/write/edit file, grep, glob, web_fetch, web_search, memory…).
- **DeepSeek Harness engine** (v3.0+) — spawns the `dsh` CLI with OpenAI-compatible SSE streaming and OpenAI / Pi-AI provider adapters, with automatic retry and token metering.

**To start a task:**

1. Click **＋** (new session) in the sidebar.
2. In the chat composer, pick the engine from the dropdown (Direct or DeepSeek Harness).
3. Make sure the model is set to `deepseek-v4-pro` (or `deepseek-v4-flash`).
4. Type a task, e.g.:

```
List the files in the current directory and summarize what this project does.
```

KinetAios runs tools, streams the answer, and auto-extracts durable facts into long-term memory for the next turn.

---

#### 5. Highlights

- **Four engines from one window** — Direct V1/V2/V3 + Claude Code + Codex + DeepSeek Harness
- **Cross-engine long-term memory** — SQLite + FTS5 + semantic recall, one user profile across all engines
- **20+ built-in tools** — `shell`, `read_file`, `write_file`, `edit_file`, `grep`, `glob`, `web_fetch`, `web_search`, `recall_memory`, `dispatch_agent`, `team_broadcast` …
- **MCP client + built-in MCP server** — auto-discovers Claude Code / Codex MCP configs; built-in server exposes `run_agent` for remote control
- **Skills / commands / agents auto-scan** — Claude Code + Codex skills are available via the `/` menu
- **Plugin SDK v3** — plugins can contribute tools, slash commands, hooks, and full-screen panels
- **Multimodal** — image input, voice transcription, realtime voice chat, screenshot
- **Pipeline** — cross-engine orchestration with per-stage engine + prompt
- **Session branching & export/import** — fork from any turn; full state serialization for cross-machine handoff
- **Local-first, no account**

---

## Links

- Repo: <https://github.com/phinn/KinetAios>
- Website: <https://phinn.github.io/KinetAios/>
- Releases: <https://github.com/phinn/KinetAios/releases/latest>
- DeepSeek Platform: <https://platform.deepseek.com/>
- DeepSeek API Docs: <https://api-docs.deepseek.com/>
