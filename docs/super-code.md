[English](./super-code.md) | [简体中文](./super-code.zh-CN.md) · [← Back](../README.md)

# Integrate with Super Code

Super Code is a terminal AI coding assistant built in Python, featuring multi-agent orchestration, persistent memory across sessions, snippet-based edit safety, and multi-model support via OpenAI-compatible API.

- **GitHub:** <https://github.com/weiqiang136/super-code>

#### 1. Install Super Code

**From source (all platforms)**

- Install [Python](https://www.python.org/downloads/) 3.11+.
- Clone the repository and install dependencies:

```sh
git clone https://github.com/weiqiang136/super-code.git
cd super-code
pip install -r requirements.txt
```

**Portable executable (Windows)**

Download `super-code.exe` from the [Releases page](https://github.com/weiqiang136/super-code/releases) and place it in a directory on your `PATH`.

#### 2. Configure Super Code

Create `~/.config/super-code/super-code.json` (global) or `./.super-code.json` (project-level) with your DeepSeek API key:

```json
{
  "provider": "openai",
  "model": "deepseek-v4-pro",
  "api_key": "sk-...",
  "base_url": "https://api.deepseek.com",
  "max_tokens": 131072,
  "timeout": 300,
  "model_profiles": {
    "deepseek": {
      "extra_body": {
        "reasoning_effort": "max"
      }
    }
  }
}
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

> **Note:** DeepSeek V4 models support up to **1 million tokens** of context. Super Code uses the OpenAI-compatible protocol — `base_url` points to DeepSeek's API endpoint. For the faster model, set `"model": "deepseek-v4-flash"`.

**Configuration options:**

| Option | Description |
|--------|-------------|
| `provider` | Always `"openai"` (DeepSeek uses OpenAI-compatible protocol) |
| `model` | `deepseek-v4-pro` or `deepseek-v4-flash` |
| `api_key` | Your DeepSeek API key |
| `base_url` | `https://api.deepseek.com` |
| `max_tokens` | Max output tokens (default 131072) |
| `timeout` | HTTP timeout in seconds (default 300, recommended ≥ 300 for thinking models) |
| `model_profiles` | Per-model extra request body parameters. For DeepSeek, set `reasoning_effort` to `"max"` or `"high"` via `extra_body` |
| `coordinator` | Enable multi-agent coordinator mode (default `false`) |

**Portable distribution:** Place `super-code.json` in the same directory as `super-code.exe` for zero-config deployment — the executable auto-detects it.

#### 3. Launch Super Code

```sh
cd /path/to/my-project
python -m src.tui.app
# or: super-code (if using the portable executable)
```

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Tab` | Toggle Plan mode (read-only tools) |
| `Esc` | Interrupt the current model turn |
| `/help` | Show available slash commands |
| `/resume` | Continue a previous conversation |
| `/clear` | Start a fresh conversation |
| `/rename <title>` | Rename the current session |
| `/memory` | View memory index |
| `/dream` | Consolidate session memories |

#### Using Agent Skills

Super Code discovers Skills from these locations:

- **User-level:** `~/.config/super-code/skills/<name>/SKILL.md`
- **Project-level:** `./.super-code/skills/<name>/SKILL.md`

Type `/<skill-name>` to invoke a skill directly, or use the `Skill` tool.

#### Multi-Agent Coordinator Mode

Enable `"coordinator": true` in the config to unlock parallel agent orchestration. The coordinator spawns workers with the `Agent` tool, sends follow-ups via `SendMessage`, and stops workers with `TaskStop`. Each worker runs in an isolated Engine with auto-approved read-only tools.
