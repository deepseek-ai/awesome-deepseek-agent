[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← Back](../README.md)

# Integrate with Grok Build

Grok Build (`grok`) is xAI's terminal AI coding agent: a full-screen TUI that reads your codebase, edits files, runs shell commands, calls MCP tools, and orchestrates subagents. It defaults to xAI-hosted Grok models, and it also speaks OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages — so DeepSeek V4 can be added as a custom model in `~/.grok/config.toml`.

- **Docs:** https://docs.x.ai/build/overview
- **Install:** https://x.ai/cli/install.sh (macOS / Linux) · https://x.ai/cli/install.ps1 (Windows)

> **Preferred backend for agent/tool loops:** DeepSeek's [Anthropic-compatible endpoint](https://api.deepseek.com/anthropic). DeepSeek thinking mode requires `reasoning_content` to be passed back on subsequent requests that carry tools. The Anthropic Messages API avoids the OpenAI `400` (`The reasoning_content in the thinking mode must be passed back to the API`) that some Chat Completions clients hit. Grok's `messages` backend is the matching protocol.

#### 1. Install Grok Build

macOS / Linux / Git Bash:

```shell
curl -fsSL https://x.ai/cli/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

Verify:

```shell
grok --version
```

#### 2. Get a DeepSeek API Key

Create a key at the [DeepSeek Platform](https://platform.deepseek.com/api_keys) (it starts with `sk-`).

Linux / Mac:

```shell
export DEEPSEEK_API_KEY="sk-..."
```

Windows (PowerShell):

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

#### 3. Add DeepSeek V4 to `config.toml`

Config file:

- Linux / macOS: `~/.grok/config.toml`
- Windows: `%USERPROFILE%\.grok\config.toml`

If the file does not exist, create it.

```toml
[models]
default = "deepseek-v4-pro"
default_reasoning_effort = "max"

[model.deepseek-v4-pro]
model = "deepseek-v4-pro[1m]"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Pro"
api_backend = "messages"
context_window = 1000000
env_http_headers = { "x-api-key" = "DEEPSEEK_API_KEY" }
extra_headers = { "anthropic-version" = "2023-06-01" }

[model.deepseek-v4-flash]
model = "deepseek-v4-flash[1m]"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Flash"
api_backend = "messages"
context_window = 1000000
env_http_headers = { "x-api-key" = "DEEPSEEK_API_KEY" }
extra_headers = { "anthropic-version" = "2023-06-01" }
```

- `[1m]` on the Anthropic model id requests DeepSeek V4's 1 million token context.
- `default_reasoning_effort = "max"` maps to DeepSeek V4's `max` thinking effort (DeepSeek's highest coding setting). `high` is a lower mapped tier.
- Keep the API key in `DEEPSEEK_API_KEY`. Do not paste it into `config.toml`.

#### 4. First run

```shell
cd /path/to/my-project
grok
```

Or pin the model on the command line:

```shell
grok -m deepseek-v4-pro --effort max
```

Confirm the model with `grok models` or `grok inspect`. In the TUI:

| Command | Action |
| --- | --- |
| `/model deepseek-v4-pro` | Switch to DeepSeek V4 Pro |
| `/model deepseek-v4-flash` | Switch to DeepSeek V4 Flash |
| `/effort max` | Set thinking effort to `max` on the current model |
| `Ctrl+M` | Open the model picker (from the scrollback pane) |

#### Optional: OpenAI Chat Completions backend

If you prefer DeepSeek's OpenAI-compatible endpoint (`https://api.deepseek.com`):

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Pro"
api_backend = "chat_completions"
context_window = 1000000
env_key = "DEEPSEEK_API_KEY"
```

Use this only if your Grok build correctly echoes `reasoning_content` on tool-calling turns. If you see `400` errors about `reasoning_content`, switch back to the Anthropic `messages` config in step 3.

#### Resources

- [Grok Build custom models](https://docs.x.ai/docs/build/overview)
- [DeepSeek thinking mode](https://api-docs.deepseek.com/guides/thinking_mode)
- [DeepSeek Anthropic API](https://api-docs.deepseek.com/guides/anthropic_api)
