[English](./illusion_code.md) | [简体中文](./illusion_code.zh-CN.md) · [← Back](../README.md)

# Integrate with IllusionCode

IllusionCode is an open-source terminal AI coding assistant that inherits Claude Code's prompt system and tool architecture, reimplemented in Python with multi-provider support, MCP extension, bilingual UI, and terminal rendering.

- **GitHub:** <https://github.com/YunTaiHua/illusion-code>

#### 1. Install IllusionCode

- Install [Python](https://www.python.org/downloads/) 3.10+.
- Install [Node.js](https://nodejs.org/en/download/) 18+ (for the TUI frontend).

**Option A: Install from PyPI (recommended)**

```sh
pip install illusion-code
```

Verify the installation:

```sh
illusion --version
```

**Option B: Install from source**

```sh
git clone https://github.com/YunTaiHua/illusion-code.git
cd illusion-code
uv sync
```

> **Tip:** You can also install from source with `pip install .` (auto-builds frontends) or `pip install -e .` for editable mode.

#### 2. Configure IllusionCode

**Option A: Interactive login (recommended)**

```sh
illusion auth login
```

Select **Custom provider** → set `api_format: openai` → set `base_url: https://api.deepseek.com/v1` → enter your API Key.

**Option B: Edit settings file directly**

Create or edit `~/.illusion/settings.json`:

```json
{
  "model": "env_1.model_1",
  "env_1": {
    "api_format": "openai",
    "base_url": "https://api.deepseek.com/v1",
    "api_key": "sk-...",
    "model_1": "deepseek-v4-pro",
    "model_2": "deepseek-v4-flash"
  }
}
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Configuration options:**

| Option | Description |
|--------|-------------|
| `model` | Active model reference, format `env_N.model_N` (e.g. `env_1.model_2` for Flash) |
| `api_format` | API format — `"openai"` for DeepSeek |
| `base_url` | API base URL — `https://api.deepseek.com/v1` |
| `api_key` | Your DeepSeek API key |
| `model_1` / `model_2` | Model names, e.g. `deepseek-v4-pro` or `deepseek-v4-flash` |

#### 3. Launch IllusionCode

```sh
cd /path/to/my-project
illusion
```

**CLI options:**

| Flag | Description |
|------|-------------|
| `-m env_1.model_2` | Switch model at launch |
| `-p "prompt"` | Non-interactive mode — run a single prompt |
| `--continue` | Resume the last conversation |
| `--resume <session-id>` | Restore a specific session |
| `--permission-mode` | Set permission mode (`default` / `plan` / `full_auto`) |
| `--api-format openai` | Override API format |
| `illusion web` | Launch the Web UI (default port 3000) |
| `illusion web --port 8080` | Launch Web UI on a custom port |

#### Reasoning Effort

IllusionCode supports reasoning effort levels via the `effort_level` setting in `~/.illusion/settings.json`:

```json
{
  "effort_level": "max"
}
```

Available levels: `low`, `medium`, `high`, `xhigh`, `max`. Use `max` for the best coding experience with DeepSeek-V4-Pro.

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Enter` | Insert a newline |
| `ctrl+x` | Interrupt the current model turn |
| `/` | Open the slash command menu |
| `/new` | Start a fresh conversation |
| `/resume` | Choose a previous conversation to continue |
| `/model` | Switch model interactively |
| `/memory` | View and manage persistent memory |
| `/config` | View and edit settings |
| `/skills` | List and manage skills |
| `/hooks` | Manage hook configurations |
| `/mcp` | Manage MCP server connections |
| `/exit` | Quit IllusionCode |

#### Features

- **34+ built-in tools** — file operations, shell execution, search, task management, agent collaboration, and more
- **47 slash commands** and **7 built-in agents** (general-purpose, Explore, Plan, verification, worker, statusline-setup, illusion-guide)
- **Dual UI:** Terminal TUI (React + Ink) and Web UI (React + Vite + Tailwind)
- **Permission modes:** `default` / `plan` / `full_auto`, with fine-grained per-tool and per-path rules
- **Multi-provider support:** Anthropic Claude, OpenAI-compatible endpoints, GitHub Copilot OAuth, OpenAI Codex, and 20+ auto-detected providers (OpenRouter, DashScope, Groq, Ollama, vLLM, etc.)
- **Multi-environment config:** Switch between providers via `env_N` groups without reconfiguration
- **MCP extension:** Dynamic tool registration from MCP servers, with project-level and global configs
- **Plugin & Skill systems:** Installable plugins and loadable skills for extending functionality
- **Hook system:** Event-driven hooks (PRE/POST tool use, user prompt submit) supporting command, prompt, HTTP, and agent hook types
- **Memory system:** Persistent project knowledge across sessions
- **Cron scheduler:** Scheduled tasks with job management, execution history, and daemon mode
- **LSP integration:** Language Server Protocol support for code intelligence
- **Sandbox support:** Configurable network and filesystem restrictions
- **Bilingual UI:** Chinese and English, controlled by `ui_language` in `~/.illusion/settings.json`
- **1M context window:** DeepSeek V4 models support up to 1 million tokens
- **Self-update:** `illusion update` checks PyPI for newer versions

For more configuration options, see the [IllusionCode documentation](https://github.com/YunTaiHua/illusion-code/blob/main/README.md).
