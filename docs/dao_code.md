[English](./dao_code.md) | [简体中文](./dao_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Dao Code

Dao Code (command `dao`) is an open-source, MIT-licensed terminal AI coding agent built around DeepSeek-V4 (up to 1M tokens of context). Its guiding principle is cache economics: DeepSeek prices a prefix-cache hit about two orders of magnitude below a miss — for deepseek-v4-pro, $0.003625 vs $0.435 per 1M input tokens, roughly 1/120. So Dao Code keeps the system prefix, tool table, and memory byte-stable to maximize the hit rate, and runs reflection and memory on forks that reuse the main prefix cache. The payoff: cross-session memory and a continuous self-correction layer — a challenger that re-examines repeated failures, a refocuser that catches scope creep — add almost no token cost. Across 7 real open-source bug-fix tasks (3.89M input tokens), it sustained a 95.8% aggregate cache-hit rate.

What sets it apart from other DeepSeek terminal agents is memory you can trust: cross-session memory is deterministically re-verified against your live code on every startup — stale facts are pruned, not blindly accumulated — paired with a challenger/refocuser layer that self-corrects throughout: steadier and more accurate on everyday tasks, and markedly harder to derail on long ones.

It also hardens long autonomous runs: crash recovery (`dao -c`), shadow-git checkpoints (`/restore`, `/rewind`) that never touch your `.git`, a Definition-of-Done gate (`verify_done`), stuck-loop detection, an autonomous `/goal` mode, and parallel / background / worktree-isolated sub-agents. The fundamentals are all there too: the full 1M-token context window, a complete built-in tool set, layered allow/ask/deny permissions with a security sandbox (secret scanning, SSRF guard, keychain), Agent Skills, MCP (stdio + HTTP/SSE), lifecycle hooks, custom sub-agents / slash commands / plugins, multi-account profiles, and OS-level scheduling. Config-compatible with Claude Code. Taiji-themed Ink TUI.

- **GitHub:** <https://github.com/tigicion/dao-code>

#### 1. Install Dao Code

**Option A — one-line install (no Node required):**

```sh
curl -fsSL https://raw.githubusercontent.com/tigicion/dao-code/master/install.sh | sh
```

Or download a prebuilt binary from [Releases](https://github.com/tigicion/dao-code/releases) (macOS arm64/x64, Linux arm64/x64, Windows x64).

**Option B — npm (requires Node ≥ 20, all platforms):**

```sh
npx dao-code        # zero-install try
npm i -g dao-code   # global install, command name `dao`
```

Verify the installation:

```sh
dao --version
```

#### 2. Configure Dao Code

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

The simplest path is to just run `dao` — on first launch with no key detected, it guides you to paste one and saves it to `~/.dao/config.json` (read automatically next time). You can also set it manually:

| Method | Command |
|--------|---------|
| `.env` (project root, all platforms) | add a line `DEEPSEEK_API_KEY=sk-...` |
| macOS / Linux | `export DEEPSEEK_API_KEY=sk-...` |
| Windows PowerShell | `$env:DEEPSEEK_API_KEY="sk-..."` |
| Windows CMD | `set DEEPSEEK_API_KEY=sk-...` |

**Configuration options:**

| Variable | Description | Default |
|----------|-------------|---------|
| `DEEPSEEK_API_KEY` | Your DeepSeek API key | — |
| `DEEPSEEK_BASE_URL` | API endpoint | `https://api.deepseek.com` |
| `DEEPSEEK_MODEL` | Model name — `deepseek-v4-pro` or `deepseek-v4-flash` | `deepseek-v4-pro` |
| `DAO_REASONING_EFFORT` | Thinking effort — keep at `max` for the deepest reasoning | `max` |
| `DAO_CONTEXT_WINDOW` | Context budget in tokens | `1000000` |
| `DAO_MAX_TURNS` | Max tool turns per round | `50` |
| `DAO_THEME` | `light` / `dark` terminal background | auto-detect |

DeepSeek-V4 supports up to 1M tokens of context, and Dao Code sets its context budget to **1,000,000 tokens by default** (override with `DAO_CONTEXT_WINDOW`). Thinking mode ships at `max` effort out of the box.

#### 3. Enter a project directory and launch Dao Code

```sh
cd /path/to/my-project
dao
```

Run a one-shot task (runs and exits, good for scripts):

```sh
dao "make formatDate in src/utils.ts timezone-aware"
```

Resume the last session after a crash:

```sh
dao -c
```

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `↑` / `↓` | Browse input history |
| `Esc` | Interrupt the current round (stops both model stream and shell) |
| `Shift+Tab` | Cycle permission mode (default / acceptEdits / auto / plan) |
| `@` + path, then `Tab` | Reference a file with autocomplete |
| `Ctrl+O` | Expand / collapse full tool output and thinking |
| `Ctrl+A` / `Ctrl+E` | Move cursor to line start / end |

#### Common Slash Commands

| Command | Action |
|---------|--------|
| `/init` | Scan the repo and generate `DAO.md` (project overview, auto-loaded later) |
| `/model [id]` | Switch model (toggles `deepseek-v4-pro` / `deepseek-v4-flash`) |
| `/mode [x]` | Permission mode: `default` / `acceptEdits` / `auto` / `plan` |
| `/goal <goal>` | Autonomous long-task mode (auto-approve + continuous progress) |
| `/cost` | Show token usage and prefix-cache hit rate |
| `/skills` | List / toggle Agent Skills |
| `/compact` · `/clear` · `/help` · `/exit` | Compact · clear · command list · quit |

#### Using Agent Skills

Dao Code supports progressively-disclosed Agent Skills, plus MCP servers and lifecycle hooks. It is config-compatible with Claude Code (`settings.json`, `SKILL.md`, `hooks.json`, `mcp.json`), so existing CC skills and configs work directly.

- **Project-level skills:** `./.dao/skills/<name>/SKILL.md`
- **MCP servers:** `./.dao/mcp.json`
- **Hooks:** `./.dao/hooks.json`
