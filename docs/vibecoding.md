[English](./vibecoding.md) | [简体中文](./vibecoding.zh-CN.md) · [← Back](../README.md)

# Integrate with VibeCoding

VibeCoding is a terminal-based AI coding assistant written in ~10,000 lines of Go, inspired by [pi.dev](https://pi.dev). It supports multiple providers (DeepSeek as default), SSE streaming, three operating modes, sandboxing via bubblewrap, session management, and a rich TUI with Markdown rendering.

- **GitHub:** <https://github.com/startvibecoding/vibecoding>

#### 1. Install VibeCoding

**Option 1: npm (Recommended)**

```bash
npm install -g vibecoding-installer
```

**Option 2: One-line Install**

Linux / macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/startvibecoding/vibecoding/main/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://raw.githubusercontent.com/startvibecoding/vibecoding/main/install.ps1 | iex
```

**Option 3: Go Install**

```bash
go install github.com/startvibecoding/vibecoding/cmd/vibecoding@latest
```

**Option 4: Build from Source**

```bash
git clone https://github.com/startvibecoding/vibecoding.git
cd vibecoding
make build
```

Verify the installation:

```bash
vibecoding --version
```

#### 2. Configure DeepSeek

VibeCoding has DeepSeek built in as the **default provider** — no manual provider setup is needed. Simply set your API key:

```bash
export DEEPSEEK_API_KEY=sk-...
```

> Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Or** configure in `settings.json` (`~/.vibecoding/settings.json` for global, `.vibe/settings.json` for per-project overrides):

```json
{
  "defaultProvider": "deepseek-openai",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "high",
  "maxContextTokens": 1000000,
  "maxOutputTokens": 384000
}
```

> DeepSeek V4 models support up to **1 million tokens** of context. The `maxContextTokens` and `maxOutputTokens` settings above reflect this.

**Key configuration options:**

| Option | Description |
|--------|-------------|
| `defaultProvider` | `"deepseek-openai"` (OpenAI-compatible, default) or `"deepseek-anthropic"` (Anthropic-compatible) |
| `defaultModel` | `deepseek-v4-pro` or `deepseek-v4-flash` |
| `defaultThinkingLevel` | `off`, `minimal`, `low`, `medium`, `high`, `xhigh` |
| `maxContextTokens` | Context window size (1000000 for DeepSeek V4) |
| `maxOutputTokens` | Max output tokens (384000) |

**Advanced example** with sandbox, approval, and compaction settings:

```json
{
  "defaultProvider": "deepseek-openai",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "high",
  "defaultMode": "agent",
  "maxContextTokens": 1000000,
  "maxOutputTokens": 384000,
  "compaction": {
    "enabled": true,
    "reserveTokens": 16384,
    "keepRecentTokens": 20000
  },
  "sandbox": {
    "enabled": true,
    "level": "standard",
    "allowNetwork": false
  },
  "retry": {
    "enabled": true,
    "maxRetries": 3,
    "baseDelayMs": 2000
  },
  "approval": {
    "bashWhitelist": ["go ", "make ", "git ", "npm "],
    "bashBlacklist": ["rm -rf", "sudo"]
  }
}
```

You can also override settings via environment variables:

| Variable | Description |
|----------|-------------|
| `DEEPSEEK_API_KEY` | DeepSeek API key |
| `VIBECODING_DIR` | Override config directory |
| `VIBECODING_PROVIDER` | Override default provider |
| `VIBECODING_MODEL` | Override default model |
| `VIBECODING_MODE` | Override default mode |
| `VIBECODING_THINKING` | Override default thinking level |

#### 3. Run VibeCoding

```bash
# Enter your project directory
cd /path/to/my-project

# Launch interactive mode
vibecoding

# Or with a specific model and thinking level
vibecoding --provider deepseek-openai --model deepseek-v4-pro --thinking high

# Non-interactive (print mode)
vibecoding -p "Write a hello world in Go"

# Continue the most recent session
vibecoding -c
```

#### Three Operating Modes

| Mode | Description |
|------|-------------|
| **Plan** | Read-only analysis and planning. Sandboxed, no file writes. |
| **Agent** (default) | Controlled read/write access. Bash requires approval (configurable whitelist). Sandboxed, no network. |
| **YOLO** | Full system access with no restrictions. |

Switch modes interactively with `/mode [plan|agent|yolo]`.

#### Interactive Commands

| Command | Description |
|---------|-------------|
| `/mode [plan\|agent\|yolo]` | Switch mode |
| `/model` | Show current model |
| `/think` | Cycle thinking level |
| `/skills` | List loaded skills |
| `/clear` | Clear conversation |
| `/help` | Show help |

#### Sandbox (Linux)

VibeCoding uses [bubblewrap](https://github.com/containers/bubblewrap) for Linux sandboxing:

```bash
# Install bubblewrap
sudo apt install bubblewrap      # Debian/Ubuntu
sudo dnf install bubblewrap      # Fedora
sudo pacman -S bubblewrap        # Arch
```

Enable sandbox with `--sandbox` flag or in settings.json.

For the full configuration reference, see the [VibeCoding docs](https://github.com/startvibecoding/vibecoding/tree/main/docs).
