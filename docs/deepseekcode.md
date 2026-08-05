[English](./deepseekcode.md) | [简体中文](./deepseekcode.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeekCode

DeepSeekCode is a local-first AI coding agent written in TypeScript and built on Bun. A single server backend drives three UIs — a terminal (Ink TUI), a React web UI, and a Tauri desktop app — and pending approvals can also be resumed from IM channels (WeChat, Feishu, Slack, Discord, Telegram, WhatsApp, …). It talks to `api.deepseek.com` out of the box, supports DeepSeek-V4-Pro and DeepSeek-V4-Flash with the full 1M-token context window, and streams reasoning content (`reasoning_content`) natively. The server binds to `127.0.0.1` only, so your code stays on your machine.

- **Download / docs:** <https://deepseekcode.github.io/deepseekwork/>
- **npm:** `@deepseekcode/cli`

#### 1. Install DeepSeekCode

**CLI (recommended for developers)** — requires Node.js 18+ or Bun:

```sh
npm install -g @deepseekcode/cli
```

Verify the installation:

```sh
dscode --version
```

`dscode` and `deepseekcode` both point to the same binary.

**Desktop app (Windows / macOS / Linux)** — download the Tauri 2 installer (`.exe` / `.msi` / `.dmg` / `.deb` / `.rpm` / `.AppImage`) from <https://deepseekcode.github.io/deepseekwork/>. It embeds the same local server and Web UI — no Node.js or Bun needed.

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure DeepSeekCode

DeepSeekCode reads provider settings from `~/.agent/config.yaml` (Windows: `%USERPROFILE%\.agent`). Create it with your key and model:

```yaml
provider:
  provider: deepseek
  baseUrl: https://api.deepseek.com/v1
  apiKey: sk-...
  model: deepseek-v4-pro          # or deepseek-v4-flash
  apiType: openai-chat-completions
  maxTokens: 384000
  contextWindow: 1000000          # DeepSeek V4 full 1M-token context
  temperature: 0.2
```

Configuration options:

| Option | Description |
|--------|-------------|
| `provider` | `deepseek` (default), `openai`, or `openai-compatible` |
| `baseUrl` | API base URL, defaults to `https://api.deepseek.com/v1` |
| `apiKey` | DeepSeek API key (or set `DEEPSEEKCODE_API_KEY`) |
| `model` | `deepseek-v4-pro` or `deepseek-v4-flash` (or set `DEEPSEEKCODE_MODEL`) |
| `apiType` | `openai-chat-completions` (default), `openai-completions`, or `openai-responses` |
| `maxTokens` | Max output tokens (up to 1,024,000) |
| `contextWindow` | Context window in tokens — set `1000000` for the full 1M context |
| `temperature` | Sampling temperature, default `0.2` |

On first run, DeepSeekCode walks you through the provider setup if nothing is configured — or use the web UI's graphical provider editor / edit `~/.agent/config.yaml` directly.

#### 4. Enter a project directory and launch

```sh
cd /path/to/my-project
dscode
```

DeepSeekCode starts a local server (HTTP `:8080`, WebSocket `:8081`) and opens the terminal TUI. Use `dscode run --backend <url>` to attach a UI to an existing backend, `dscode exec '<prompt>'` for non-interactive runs (JSONL output), and `dscode test-fix` for the auto-fix test loop.

#### Key commands

| Command | What it does |
|---|---|
| `dscode` / `dscode start` | Start local core + interactive terminal |
| `dscode run --backend <url>` | Connect a UI to an existing backend |
| `dscode exec '<prompt>'` | Non-interactive run with JSONL output |
| `dscode test-fix` | Self-healing test loop (test → analyze → fix → verify) |
| `dscode codeview` | AI code review (bugs + unwired features) |
| `/mode act\|plan\|goal` | Switch execution mode |
| `/pipeline on\|off\|auto` | ReAct ↔ workflow auto-routing override |
| `/auto` | Toggle auto-approval for hooks |
| `/mcp <action>` | Manage MCP servers |
| `/weixin` | Bind WeChat via QR code |

#### Workflow, MCP, and Channels

- **Plan / Act / Goal modes** — plan mode is read-only; risky operations (write / execute / network) are gated by a risk-tiered permission engine with target-scoped approvals.
- **ReAct ↔ Workflow routing** — a router decides per request whether a task runs as a free-form ReAct loop or a structured DAG workflow, with speculative parallel execution and safe fallback.
- **MCP** — mount external MCP servers via `/mcp`; a health-check endpoint (`/api/mcp/health`) is built in.
- **IM channels** — 16+ built-in adapters (WeChat, Feishu, Slack, Discord, Telegram, WhatsApp, …) let you resume and approve pending tasks from chat.
- **Skills** — `.skill.md` skill files (project- and user-level) extend the agent with reusable capabilities.
- **Thinking / reasoning** — thinking mode is enabled by default for DeepSeek V4; `reasoning_content` is streamed back and rendered in the UI. Use `deepseek-v4-pro` for the best coding experience.
