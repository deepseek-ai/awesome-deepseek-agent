[English](./kimi_code.md) | [简体中文](./kimi_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Kimi Code

Kimi Code is an AI coding agent that runs in the terminal, developed by Moonshot AI. It can connect to multiple LLM platforms simultaneously — including the Kimi managed service and third-party OpenAI-compatible services such as DeepSeek.

### Installing Kimi Code from Scratch

Kimi Code runs on Node.js and is distributed via npm, with an official install script for each platform.

#### Option 1: Official Install Script (Recommended)

- macOS / Linux:

```
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

- Windows (PowerShell):

```
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

> On Windows, install [Git for Windows](https://git-scm.com/download/win) before first launch — Kimi Code uses the bundled Git Bash as its shell environment.

#### Option 2: Install via npm

Requires Node.js 22.19.0 or later:

```
npm install -g @moonshot-ai/kimi-code
```

After installation, verify the executable is ready:

```
kimi --version
```

### Configuring Kimi Code

Kimi Code reads configuration from `~/.kimi-code/config.toml` (created automatically on first run). Add the DeepSeek provider and model aliases as follows.

#### Step 1: Add the DeepSeek provider

```toml
[providers.deepseek]
type = "openai"                          # DeepSeek uses the OpenAI-compatible protocol
base_url = "https://api.deepseek.com/v1"
api_key = "sk-<your-deepseek-api-key>"   # Get from https://platform.deepseek.com/api_keys
```

> **Tip:** To avoid writing the API key in plain text in the config file, put it in the provider's `env` sub-table instead. It is read only from the config file, so the key never leaks into your shell environment:
>
> ```toml
> [providers.deepseek.env]
> DEEPSEEK_API_KEY = "sk-<your-deepseek-api-key>"
> ```

#### Step 2: Declare the DeepSeek V4 models

```toml
[models."deepseek/v4-pro"]
provider = "deepseek"
model = "deepseek-v4-pro"              # current model name (DeepSeek V4)
max_context_size = 1000000             # 1M context window
capabilities = [ "tool_use" ]
display_name = "DeepSeek V4 Pro"

[models."deepseek/v4-flash"]
provider = "deepseek"
model = "deepseek-v4-flash"
max_context_size = 1000000             # 1M context window
capabilities = [ "tool_use" ]
display_name = "DeepSeek V4 Flash"
```

#### Step 3: Set DeepSeek as the default model (optional)

```toml
default_model = "deepseek/v4-pro"
```

#### Optional: Thinking / reasoning effort

DeepSeek V4 Pro supports multiple reasoning effort levels (`max` and `high`). Kimi Code handles the `reasoning_content` field and `reasoning_effort` injection automatically for OpenAI-compatible providers, so reasoning works out of the box. If you want thinking enabled by default with maximum effort:

```toml
[thinking]
enabled = true
effort = "max"
```

> If the upstream API rejects a configured effort value, pick a level the model actually supports (for DeepSeek V4 Pro: `low` / `high` / `max`).

### Using Kimi Code with DeepSeek

- Start the interactive TUI in your project directory:

```
cd /path/to/my-project
kimi
```

- Run a single instruction without entering the UI:

```
kimi -p "Take a look at this project's directory structure"
```

- Switch models at runtime with `/model` and pick `deepseek/v4-pro` or `deepseek/v4-flash`.
- Manage providers interactively: type `/provider` in the TUI (non-interactive equivalent: `kimi provider`).

DeepSeek V4 supports a 1M-token context window, already reflected in `max_context_size = 1000000` above — browsing large codebases and long-running refactors work out of the box.
