[English](./yoyo.md) | [简体中文](./yoyo.zh-CN.md) · [← Back](../README.md)

# Integrate with yoyo

yoyo is an open-source terminal coding agent written in Rust — and a self-evolving one: it reads its own source, plans improvements, implements them, and commits when tests pass, in public. As a product it's a streaming REPL with 90+ slash commands, subagent orchestration (`/spawn --parallel`, background jobs), watch mode, MCP servers, a skills system, and 15 providers — DeepSeek among them, first-class.

- **GitHub:** <https://github.com/yologdev/yoyo-evolve>

#### 1. Install yoyo

Choose any of:

```sh
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/yologdev/yoyo-evolve/main/install.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/yologdev/yoyo-evolve/main/install.ps1 | iex

# crates.io
cargo install yoyo-agent

# Or download a release binary from
#   https://github.com/yologdev/yoyo-evolve/releases
```

Verify:

```sh
yoyo --version
```

#### 2. Get a DeepSeek API Key

Create a key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys) and export it:

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. Configure

Create `.yoyo.toml` in your project root (or `~/.yoyo.toml` globally):

```toml
provider = "deepseek"
model = "deepseek-v4-pro"      # or deepseek-v4-flash
thinking = "high"              # sent as reasoning_effort: "high"
context_window = 1000000       # DeepSeek V4 supports 1M tokens
```

Or pass the same as flags, no config file needed:

```sh
yoyo --provider deepseek --model deepseek-v4-pro --thinking high --context-window 1000000
```

yoyo talks to `https://api.deepseek.com/v1` (OpenAI-compatible). Thinking mode is enabled by mapping yoyo's `thinking` level to the `reasoning_effort` request field — `high` is the maximum level yoyo currently sends. Don't disable thinking to work around errors; DeepSeek V4's thinking mode is the default and works out of the box here.

> **Note:** current yoyo releases print a harmless `Unknown model 'deepseek-v4-pro'` warning and proceed — the built-in model list still shows the pre-April-2026 names. Tracked in [yologdev/yoyo-evolve#584](https://github.com/yologdev/yoyo-evolve/issues/584); the config above is the current-model setup and works today.

#### 4. First run

```sh
cd /path/to/my-project

# Interactive REPL (default)
yoyo

# One-shot prompt
yoyo "explain this codebase"

# Pipe input
echo "write tests for src/parser.rs" | yoyo
```

In the REPL, `/help` shows the grouped command reference. A few worth knowing:

| Command | What it does |
|---|---|
| `/plan` | Plan a feature before implementing |
| `/spawn <task>` | Delegate to a subagent (`--parallel`, `--bg` for fan-out/background) |
| `/watch` | Auto-run lint + test after every change |
| `/risk` | Per-file risk scores from git history |
| `/model`, `/provider` | Switch model or provider mid-session |
| `/cost`, `/tokens` | Spend and context-window usage |
| `!<cmd>` | Run a shell command directly, zero tokens |

#### Configuration reference

| Key (`.yoyo.toml`) | Flag | Description |
|---|---|---|
| `provider = "deepseek"` | `--provider deepseek` | Selects the DeepSeek API |
| `model` | `--model` | `deepseek-v4-pro` or `deepseek-v4-flash` |
| `thinking` | `--thinking` | `off` / `minimal` / `low` / `medium` / `high` → `reasoning_effort` |
| `context_window` | `--context-window` | Set to `1000000` for DeepSeek V4's 1M context |
| — | `DEEPSEEK_API_KEY` | API key (environment variable) |

#### MCP and Skills

- **MCP servers** — `mcp = ["npx some-mcp-server"]` in `.yoyo.toml` or `--mcp <cmd>` (stdio transport). yoyo pre-flights tool names to avoid collisions with its builtins.
- **Skills** — `--skills <dir>` loads markdown skill files with YAML frontmatter; `/skill install gh:user/repo` installs community skills.
- **Custom commands** — drop `.md` files in `.yoyo/commands/` to register your own slash commands.
