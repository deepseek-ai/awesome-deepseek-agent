[English](./deepseek-cli.md) | [简体中文](./deepseek-cli.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek-CLI

DeepSeek-CLI is an open-source **agentic** terminal AI coding assistant powered by DeepSeek. Written in TypeScript and shipped as a single ~60 MB binary built with [Bun](https://bun.sh), it pairs streaming chat completions with tool calling — the model can read files, run shell commands, edit code, search the repo, and fetch the web to actually complete tasks, not just talk about them.

- **GitHub:** <https://github.com/charsdavy/deepseek-cli>

#### 1. Install DeepSeek-CLI

Choose any of:

```sh
# Homebrew (recommended)
brew tap charsdavy/tap
brew install deepseek

# Build from source (Bun ≥ 1.1 required)
git clone https://github.com/charsdavy/deepseek-cli.git
cd deepseek-cli
bun install
bun run build          # → ./dist/deepseek
```

If you built from source, copy `./dist/deepseek` to a directory on your `PATH`. Verify with `deepseek -V`.

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). Run `deepseek auth` once to store it in `~/.deepseek-cli/config.json` (file mode `0600`), or set the `DEEPSEEK_API_KEY` environment variable instead.

#### 3. Launch

```sh
cd /path/to/my-project
deepseek                                 # interactive REPL
deepseek "summarize the architecture"    # one-shot prompt
deepseek -m deepseek-v4-pro "prove 7 is prime"
deepseek -m deepseek-v4-flash "explain this test file"
deepseek --yolo "fix the failing tests"  # auto-approve tool calls
```

By default DeepSeek-CLI runs on the `auto` model, which picks **DeepSeek-V4-Pro** or **DeepSeek-V4-Flash** based on task complexity. Pass `-m deepseek-v4-pro` / `-m deepseek-v4-flash` to pin a model. Inside the REPL, `/model` opens an arrow-key wizard to set the model, reasoning effort (`off/high/max`), and the context-trim budget — with presets up to the full **1M-token** context window. DeepSeek-V4-Pro is a thinking model by default; `--reasoning-effort max` (or `/reasoning effort max`) enables the deepest reasoning level.

#### Built-in tools

The agent drives the work through a tool loop — each turn it can call any of the 14 built-in tools (independently, in parallel):

| Tool | What it does |
|---|---|
| `read_file` / `read_files` | Read one file, or batch-read several in a single call |
| `write_file` / `edit_file` | Create/overwrite files, or apply exact string replacements |
| `bash` | Run a shell command with workdir, timeout, and output truncation |
| `glob` / `grep` | Match file paths, or search contents (ripgrep with Node fallback) |
| `list_dir` | Single-level directory listing |
| `web_fetch` / `web_search` | Fetch a URL (HTML → Markdown), or search via DuckDuckGo — no API key needed |
| `git_diff` / `git_status` | Read-only structured `git diff` / `git status` |
| `task` | Spawn a nested sub-agent for a subtask; independent subtasks run in parallel |
| `todo_write` | Maintain an in-memory task list the model can read/update |

#### Key REPL commands

| Command | What it does |
|---|---|
| `/model [name]` | Setup wizard (model → effort → context), or quick-switch a model |
| `/reasoning [on|off|effort high|max]` | Show/set the thinking default and intensity |
| `/context [tokens]` | Show/set the context-trim budget |
| `/mcp [name]` | List MCP servers, or toggle a server's tools |
| `/skill [name]` | Pick/toggle skills for the session |
| `/allow [tool|all|reset]` | Authorize a tool for the session |
| `/approve [auto|ask]` | Toggle bash approval mode |
| `/tokens` | Show token usage (estimate + real API totals) |
| `/new` · `/save` · `/undo` · `/retry` | Start fresh, save, drop the last turn, or re-run the last prompt |
| `/export [path]` | Dump the transcript to stdout or a file |
| `/sessions [query]` | List or search saved sessions |

#### Configuration

Configuration lives in `~/.deepseek-cli/config.json`. Environment variables override it:

| Variable | Description |
|---|---|
| `DEEPSEEK_API_KEY` | API key (preferred over the file) |
| `DEEPSEEK_BASE_URL` | Override the API base URL |
| `DEEPSEEK_MODEL` | Default model id |

Key CLI flags:

| Flag | Description |
|---|---|
| `-m, --model <name>` | Model id (default `auto`) |
| `--yolo` / `--approval-mode <ask|auto|yolo>` | Skip / configure permission prompts |
| `--reasoning-effort <high|max>` | Thinking intensity (default `high`; `max` = deeper) |
| `--max-context <tokens>` | Context-trim budget (default 60000) |
| `--max-iterations <n>` | Cap the agent loop (default 30) |
| `--base-url <url>` | Override the API base URL (for proxies / self-hosted endpoints) |
| `-c` / `--resume <id>` | Resume the most recent or a specific session |
| `--output-format <text|json>` | One-shot: emit a single JSON result for CI |

#### MCP, Skills, and project instructions

- **MCP servers** — add via `deepseek mcp add ...` (stored in `~/.deepseek-cli/mcp.json` or `<repo>/.mcp.json`); their tools appear as `mcp_<server>_<tool>`. Mark a server `--dangerous` to require per-call approval.
- **Skills** — loadable instruction packs from deepseek, Claude Code, and Codex skill directories (flat `<name>.md` or `<name>/SKILL.md` layouts). Scaffold one with `deepseek skill create <name>`, activate with `/skill`.
- **Project instructions** — the agent auto-loads `AGENTS.md`, `deepseek.md`, `.cursorrules`, `CLAUDE.md`, or `.deepseek` from the repo root into the system prompt. `deepseek init` scaffolds an `AGENTS.md` template.
- **Session persistence** — every interactive turn auto-saves to `~/.deepseek-cli/sessions/`; reference files inline with `@path/to/file`.

DeepSeek-CLI is MIT-licensed, has zero runtime dependencies (the API client is raw `fetch` + SSE), and streams with a reasoning trace. See the [README](https://github.com/charsdavy/deepseek-cli) for the full command reference.
