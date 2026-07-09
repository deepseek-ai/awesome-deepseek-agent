[English](./octo-agent.md) | [简体中文](./octo-agent.zh-CN.md) · [← Back](../README.md)

# Integrate with octo-agent

octo-agent is an open-source general-purpose AI agent that works as both a coding assistant and a general agent. It ships with a terminal UI (TUI), a local Web UI, built-in tools, MCP support, skills, and human-in-the-loop approval for side-effectful actions.

- **GitHub:** <https://github.com/open-octo/octo-agent>

#### 1. Install octo-agent

```sh
# macOS / Linux
curl -fsSL https://octo-agent.dev/install.sh | sh

# Windows: download the installer from the latest release
# https://github.com/open-octo/octo-agent/releases/latest
```

Or grab a prebuilt binary for your platform from the [GitHub Releases](https://github.com/open-octo/octo-agent/releases/latest) page.

Verify:

```sh
octo --version
```

#### 2. Get a DeepSeek API Key

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). For security, set it as an environment variable:

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. Configure DeepSeek as the default provider

octo-agent supports the OpenAI and Anthropic wire protocols. DeepSeek exposes both, so you can pick either.

**Option A: OpenAI-compatible endpoint (recommended)**

```sh
octo config
# Choose: OpenAI-compatible → set base URL to https://api.deepseek.com/v1 → model deepseek-chat
```

Or use the `custom` vendor with the OpenAI protocol:

```sh
CUSTOM_BASE_URL=https://api.deepseek.com/v1 \
CUSTOM_API_KEY=$DEEPSEEK_API_KEY \
  octo --provider custom --protocol openai --model deepseek-chat "..."
```

**Option B: Anthropic-compatible endpoint**

```sh
octo config
# Choose: Custom → Anthropic protocol → base URL https://api.deepseek.com/anthropic → model deepseek-chat
```

Save the defaults so you don't need flags every time:

```sh
octo config
octo config show   # print effective settings
octo config path   # print the config file location
```

#### 4. Start using octo-agent

Run a one-shot task in the terminal:

```sh
octo "Explain the README and suggest three improvements"
```

Launch the interactive TUI:

```sh
octo
```

Start the local web server (default `http://127.0.0.1:8088`):

```sh
octo serve
```

#### 5. Mode and permission controls

octo-agent supports three permission modes:

| Mode | Behavior |
|---|---|
| **interactive** | Ask before shell, file edits, and other side-effectful tools (default) |
| **strict** | More conservative approvals |
| **auto** | Auto-approve tools; use with caution |

Set it interactively with `octo config`, or per-run:

```sh
octo --permission-mode interactive "..."
```

#### Configuration reference

Key environment variables and CLI flags:

| Variable / flag | Description |
|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API key |
| `OPENAI_API_KEY` | Used when `--provider openai` is selected |
| `CUSTOM_BASE_URL` | Base URL for the `custom` provider |
| `CUSTOM_API_KEY` | API key for the `custom` provider |
| `--model` | Select model by the `model` name in config |
| `--reasoning-effort` | `low` \| `medium` \| `high` \| `xhigh` \| `max` |
| `--show-reasoning` | Surface the reasoning trace in the Web UI |
| `--no-tools` | Chat-only mode, no tool loop |

The full config schema lives in `~/.octo/config.yml`. See the [octo-agent docs](https://octo-agent.dev/docs/reference/config-file/) for all options.

#### Local server and API

`octo serve` exposes a local HTTP and WebSocket server. By default it listens on `127.0.0.1:8088` and requires no authentication from the loopback interface; set `access_key` in `~/.octo/config.yml` if you expose it beyond localhost.

```sh
octo serve
```

The server powers the web UI, session management, and streaming chat. See the [HTTP API reference](https://octo-agent.dev/docs/reference/http-api/) for endpoints.

#### MCP and skills

- **MCP servers** — configure in `~/.octo/mcp.json` or use the slash command in chat.
- **Skills** — place a `SKILL.md` under `~/.octo/skills/<name>/` (user-level) or `./.octo/skills/<name>/` (project-level).
- **Sub-agents** — the model can spawn child agents to delegate work.

See the [octo-agent guides](https://octo-agent.dev/docs/guides/) for details.
