[English](./waveloom.md) | [简体中文](./waveloom.zh-CN.md) · [← Back](../README.md)

# Integrate with Waveloom

Waveloom is an open-source Go terminal coding agent with DeepSeek V4 as its **default LLM** — no provider configuration needed, just set your API key. Built on a Think-Act-Observe loop with 12 built-in tools, a Claude Code-compatible Skill system (`.claude/skills/` drop right in), full MCP client support, and a four-tier prefix-stable compaction engine optimized for DeepSeek's cache economics.

- **GitHub:** <https://github.com/Menfre01/waveloom>

#### 1. Install Waveloom

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/Menfre01/waveloom/main/install.sh | sh

# Or Homebrew
brew install Menfre01/tap/waveloom

# Windows (PowerShell — requires Git for Windows)
powershell -c "irm https://raw.githubusercontent.com/Menfre01/waveloom/main/install.ps1 | iex"
```

Verify:

```bash
waveloom --version
```

> See the [full installation guide](https://github.com/Menfre01/waveloom#readme) for building from source, manual downloads, and other options.

#### 2. Configure DeepSeek

Create `.waveloom/settings.json` in your project (recommended) or at `~/.waveloom/settings.json` (global fallback):

```json
{
    "llm": {
        "api_key": "<your DeepSeek API Key>",
        "provider": "deepseek",
        "model": "deepseek-v4-pro",
        "base_url": "https://api.deepseek.com",
        "timeout": "600s",
        "extra_params": {
            "thinking": {"type": "enabled"},
            "reasoning_effort": "max"
        }
    }
}
```

Key fields:

| Field | Default | Notes |
|-------|---------|-------|
| `api_key` | — | Your [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| `model` | `deepseek-v4-pro` | Also supports `deepseek-v4-flash` for faster, lighter tasks |
| `extra_params.thinking` | `{"type": "enabled"}` | Enables chain-of-thought reasoning |
| `extra_params.reasoning_effort` | `"max"` | Best coding results; also supports `"high"` |

You can also use the `LLM_API_KEY` environment variable as an alternative to storing the key in a file — ideal for CI/CD.

> **Context window:** Waveloom targets DeepSeek's 1M-token context window. The prefix-stable compaction system keeps the longest common prefix cache-hot across turns, so you get extended context without the latency penalty.

#### 3. First Run

```bash
cd /path/to/my-project
waveloom
```

On first run, optionally go through the interactive setup wizard:

```bash
waveloom setup
```

The wizard walks through setting your API key, selecting a model, and configuring thinking mode.

Type natural language instructions — ask it to write code, fix bugs, explain logic, or explore the codebase. Waveloom thinks, acts, and observes in a continuous loop until the task is complete.

```text
Add input validation to the UserSignup function
Why is the login handler returning 500 on empty email?
Refactor the payment module to use the strategy pattern
```

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Enter` | Insert a newline |
| `Shift+Tab` | Enter / Exit Plan Mode |
| `Esc` | Interrupt the current turn |
| `/` | Open the slash-command menu |
| `@` | Fuzzy file picker |
| `Tab` | Navigate interactive sections |
| `Ctrl+C` (twice) | Quit |

#### Why Waveloom

- **Claude Code skill drop-in** — `.claude/skills/` directories work without modification. All 9 SKILL.md frontmatter fields, `$ARGUMENTS` substitution, and `` !`cmd` `` injection are supported.
- **Full MCP client** — connect external MCP servers alongside 12 built-in tools. Compatible with Claude Code's `.claude.json` MCP config format.
- **Plan Mode** — explore and design first, implement after approval. `Shift+Tab` to toggle; Guard-enforced write protection while planning.
- **Prefix-cache optimized compaction** — fixed system prompt, append-only history, four-tier watermark (Snip → Prune → Summarize). Maximum common prefix stays cache-hot turn after turn.
- **Permission safety** — three-tier (allow / deny / ask) with pattern-matching rules. Every write operation requires your confirmation.
- **Session persistence** — close the terminal and come back days later with `waveloom --continue`. All prior context preserved.
- **Switch models on the fly** — `/model deepseek-v4-flash` inside the TUI, or `waveloom --model deepseek-v4-flash`.
