[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← Back](../README.md)

# Integrate with Grok Build

[Grok Build](https://grok.com/cli) is a terminal-based AI coding assistant by xAI (SpaceXAI). It features a full-featured TUI, streaming responses, MCP server support, skills, subagents, and custom model integration. Grok Build supports both Anthropic-compatible (`messages`) and OpenAI-compatible (`chat_completions`) API backends.

### Installing Grok Build

Install the latest stable release:

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

Install a specific version:

```bash
curl -fsSL https://x.ai/cli/install.sh | bash -s 0.2.112
```

Verify installation:

```bash
grok --version
```

### Configuring Grok Build

Grok Build uses a TOML configuration file at `~/.grok/config.toml`. Add a `[model.<name>]` section to define a custom model backed by DeepSeek.

Grok Build supports two API backends. Choose the one that fits your workflow:

#### Option 1: Anthropic Messages API (Recommended)

This uses DeepSeek's [Anthropic-compatible API](https://api-docs.deepseek.com/guides/anthropic_api). Add the following to `~/.grok/config.toml`:

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Pro"
description = "DeepSeek V4 Pro via Anthropic API"
api_backend = "messages"
context_window = 1000000
api_key = "<your DeepSeek API Key>"
extra_headers = { "anthropic-version" = "2023-06-01" }
```

> **Important:** The `api_key` field is required. Without it, Grok Build will use your xAI session token, which DeepSeek rejects with a 401 error. Setting `api_key` tells Grok Build this is a third-party (BYOK) model.

#### Option 2: OpenAI Chat Completions API

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Pro"
description = "DeepSeek V4 Pro via OpenAI-compatible API"
context_window = 1000000
api_key = "<your DeepSeek API Key>"
```

`api_backend` defaults to `"chat_completions"`, so you can omit it.

#### Enable Max Reasoning Effort

Add the following to the `[models]` section to enable maximum reasoning effort for all models (effective for `deepseek-v4-pro`):

```toml
[models]
default = "deepseek-v4-pro"
default_reasoning_effort = "high"
```

#### Using an Environment Variable for the API Key

For better security, store your key in an environment variable instead of plain text:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Then replace `api_key` with `env_key` in your config:

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Pro"
api_backend = "messages"
context_window = 1000000
env_key = "DEEPSEEK_API_KEY"
extra_headers = { "anthropic-version" = "2023-06-01" }
```

#### Using a Flash Model

For lighter tasks, configure `deepseek-v4-flash` as a secondary model:

```toml
[model.deepseek-v4-flash]
model = "deepseek-v4-flash"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Flash"
api_backend = "messages"
context_window = 1000000
env_key = "DEEPSEEK_API_KEY"
extra_headers = { "anthropic-version" = "2023-06-01" }
```

### Using Grok Build

Launch Grok Build in your project directory:

```bash
cd /path/to/my-project
grok
```

#### Switching Models

Once inside the TUI, switch to DeepSeek with:

```
/model deepseek-v4-pro
```

Or use the model picker: press `Ctrl+M` in the scrollback pane to open the list of all available models and select with a keystroke.

#### Setting DeepSeek as Default

To start every session with DeepSeek, set the default model in `~/.grok/config.toml`:

```toml
[models]
default = "deepseek-v4-pro"
```

#### Headless Mode

For scripting and CI/CD, use Grok Build in headless mode:

```bash
grok -p "Explain how goroutines work" -m deepseek-v4-pro
```

### Troubleshooting

#### 401 "Auth recovery succeeded but inference request was still rejected"

This means Grok Build sent your xAI session token to DeepSeek instead of your API key. The fix: add `api_key` (or `env_key` + environment variable) to your `[model.deepseek-v4-pro]` config block. Grok Build only uses the per-model key for third-party endpoints when `api_key`/`env_key` is explicitly set.

#### Connection Errors

Verify the endpoint is reachable:

```bash
curl -s https://api.deepseek.com/anthropic/v1/messages \
  -H "x-api-key: <your DeepSeek API Key>" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"deepseek-v4-pro","max_tokens":16,"messages":[{"role":"user","content":"hi"}]}'
```

#### Debug Logging

```bash
GROK_LOG_FILE=/tmp/grok.log RUST_LOG=debug grok
tail -f /tmp/grok.log
```
