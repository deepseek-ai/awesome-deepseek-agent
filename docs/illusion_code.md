[English](./illusion_code.md) | [简体中文](./illusion_code.zh-CN.md) · [← Back](../README.md)

# Integrate with IllusionCode

IllusionCode is an open-source terminal AI coding assistant that inherits Claude Code's prompt system and tool architecture, reimplemented in Python with multi-provider support, MCP extension, bilingual UI, and terminal rendering.

- **GitHub:** <https://github.com/YunTaiHua/illusion-code>

#### 1. Install IllusionCode

- Install [Python](https://www.python.org/downloads/) 3.10+.
- Install [Node.js](https://nodejs.org/en/download/) 18+ (for the TUI frontend).
- Clone and set up the project:

```sh
git clone https://github.com/YunTaiHua/illusion-code.git
cd illusion-code
uv sync
```

- Verify the installation:

```sh
uv run illusion --version
```

> **Tip:** You can also install globally with `pip install -e .` and then run `illusion` directly.

#### 2. Configure IllusionCode

**Option A: Interactive login (recommended)**

Use `uv run` for first-time login; afterward, you can run `illusion` directly.

```sh
uv run illusion auth login
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
uv run illusion
```

**CLI options:**

| Flag | Description |
|------|-------------|
| `-m env_1.model_2` | Switch model at launch |
| `-p "prompt"` | Non-interactive mode — run a single prompt |
| `--continue` | Resume the last conversation |
| `--api-format openai` | Override API format |

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
| `/exit` | Quit IllusionCode |

#### Features

- **36 built-in tools** + MCP dynamic tool extension
- **52 slash commands** and **7 built-in agents**
- **Permission modes:** `default` / `plan` / `full_auto`
- **Bilingual UI:** Chinese and English, controlled by `ui_language` in `~/.illusion/settings.json`
- **1M context window:** DeepSeek V4 models support up to 1 million tokens

For more configuration options, see the [IllusionCode documentation](https://github.com/YunTaiHua/illusion-code/blob/main/README.md).
