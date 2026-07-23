[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← Back](../README.md)

# Integrate with Grok Build

Grok Build (`grok`) is xAI's terminal-based AI coding agent — a full-screen TUI that understands your codebase, edits files, executes shell commands, searches the web, manages long-running tasks, and orchestrates subagents. Its multi-LLM architecture supports multiple model backends natively: the default is xAI's Grok, and third-party providers (including **DeepSeek**) can be configured via `~/.grok/config.toml`.

- **GitHub:** <https://github.com/xai-org/grok-build>

### 1. Install Grok Build

```sh
# macOS / Linux / Git Bash
curl -fsSL https://x.ai/cli/install.sh | bash

# Windows PowerShell
irm https://x.ai/cli/install.ps1 | iex

# Verify
grok --version
```

### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

### 3. Configure DeepSeek as a Provider

Open `~/.grok/config.toml` and add a `[model.<id>]` entry for each DeepSeek model you want to use. The minimal configuration:

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
api_backend = "chat_completions"
context_window = 1000000
provider_alias = "d"
provider_name = "DeepSeek"

[model.deepseek-v4-flash]
model = "deepseek-v4-flash"
base_url = "https://api.deepseek.com/v1"
api_backend = "chat_completions"
context_window = 1000000
provider_alias = "d"
provider_name = "DeepSeek"
```

> **API Key Setup:** Set your DeepSeek API key via the `DEEPSEEK_API_KEY` environment variable, or use `env_key` / `api_key` in the model entry:
>
> ```toml
> env_key = "DEEPSEEK_API_KEY"
> # or
> api_key = "sk-your-deepseek-api-key"
> ```

#### Set DeepSeek as the Default Model

To make DeepSeek the default model for new sessions, add a `[models]` section:

```toml
[models]
default = "deepseek-v4-pro"
```

#### Reasoning / Thinking Mode

DeepSeek V4 Pro supports `max` and `high` reasoning efforts. Enable it in the model config:

```toml
[model.deepseek-v4-pro]
# ... (other fields above)
reasoning_effort = "max"
supports_reasoning_effort = true
```

You can cycle reasoning effort at runtime with `Ctrl+R` in the TUI.

### 4. Launch Grok Build

```sh
cd /path/to/your-project
grok
```

Grok Build starts with the default model. Use these commands to switch at runtime:

| Command | What it does |
|---------|-------------|
| `/m deepseek-v4-pro` | Switch to DeepSeek V4 Pro |
| `/m deepseek-v4-flash` | Switch to DeepSeek V4 Flash |
| `/m:d` | Switch to the model with `provider_alias = "d"` (DeepSeek) |

You can also set the model at launch:

```sh
grok -m deepseek-v4-pro
```

### Key Features

- **Multi-model orchestration** — spawn subagents with different models for different tasks. A DeepSeek-powered `general-purpose` subagent can work alongside xAI models as the orchestrator.
- **Full tool suite** — file read/write/edit, shell commands, background tasks, web search, MCP tools, skills, and more — all available with any configured model backend.
- **Session model switching** — change models mid-session without losing context; the TUI automatically re-compacts when switching to a smaller context window.
- **BYOK support** — bring your own API key per model via `api_key`, `env_key`, or `extra_headers` for providers that require custom header-based auth.

### Configuration Reference

| Field | Description | Required |
|-------|-------------|----------|
| `model` | Model ID sent to the API | Yes |
| `base_url` | API endpoint base URL | Yes |
| `api_backend` | `"chat_completions"` (OpenAI-compat), `"messages"` (Anthropic-compat), `"responses"` (xAI) | No (default: `chat_completions`) |
| `context_window` | Total context window in tokens | Yes |
| `api_key` | Hardcoded API key (use `env_key` instead for security) | No |
| `env_key` | Environment variable name(s) for the API key | No |
| `provider_alias` | Short alias for `/m:<alias>` switching (e.g. `"d"`) | No |
| `provider_name` | Display name shown in the TUI (e.g. `"DeepSeek"`) | No |
| `reasoning_effort` | Reasoning level: `"low"`, `"medium"`, `"high"`, `"max"` | No |
| `supports_reasoning_effort` | Enable reasoning effort UI | No |
| `extra_headers` | Additional HTTP headers (e.g. custom auth) | No |
