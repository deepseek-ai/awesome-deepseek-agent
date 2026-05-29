[English](./codewhale.md) | [简体中文](./codewhale.zh-CN.md) · [← Back](../README.md)

# Integrate with CodeWhale(formerly DeepSeek-TUI)

CodeWhale is an open-source terminal AI coding assistant built in Rust as a Codex-style 13-crate workspace. It talks to `api.deepseek.com` directly, supports DeepSeek-V4-Pro and DeepSeek-V4-Flash with the full 1M-token context window, and ships sandboxed tool execution on macOS (Seatbelt), Linux (Landlock), and Windows.

- **GitHub:** <https://github.com/Hmbown/CodeWhale>

#### 1. Install CodeWhale

Choose any of:

```sh
# npm (cross-platform prebuilt binaries)
npm install -g codewhale

# Cargo (build from source — Rust 1.85+ required)
cargo install codewhale-cli --locked   # `codewhale` (entry point)
cargo install codewhale-tui --locked   # `codewhale-tui` (TUI binary)

# Or download a release binary from
#   https://github.com/Hmbown/CodeWhale/releases
```

Verify:

```sh
codewhale --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). On first run, `codewhale auth` walks you through saving it to `~/.codewhale/config.toml`. You can also set `DEEPSEEK_API_KEY` as an environment variable.

#### 3. Enter a project directory and launch

```sh
cd /path/to/my-project
codewhale
```

`codewhale` is the canonical entry point. It dispatches to the interactive TUI by default, or to subcommands like `codewhale doctor`, `codewhale mcp list`, `codewhale serve --http`, `codewhale -p "one-shot prompt"`, and `codewhale --yolo`.

By default CodeWhale uses **DeepSeek-V4-Pro**. Press `Shift+Tab` to cycle reasoning effort (`off → high → max`). Press `Tab` to cycle modes:

| Mode | What it does |
|---|---|
| **Plan** | Read-only investigation. No mutations, no shell. |
| **Agent** | Multi-step tool use. Side-effectful tools require approval. |
| **YOLO** | Auto-approve all tools. Lifts workspace boundary. |

#### Key shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Enter` | Insert a newline |
| `Tab` | Cycle TUI mode (Plan / Agent / YOLO) |
| `Shift+Tab` | Cycle reasoning effort (off / high / max) |
| `Esc` | Interrupt the current model turn |
| `/` | Open the slash-command menu |
| `?` | Show keybinding help |
| `Ctrl+C` (twice) | Quit |

#### Configuration

`~/.codewhale/config.toml` is the main config (see `config.example.toml` in the repo for every option). Key environment overrides:

| Variable | Description |
|---|---|
| `DEEPSEEK_API_KEY` | API key (overrides config) |
| `DEEPSEEK_BASE_URL` | API base URL — defaults to `https://api.deepseek.com`; use `https://api.deepseeki.com` for the China endpoint |
| `DEEPSEEK_MODEL` | Override default model |
| `DEEPSEEK_PROVIDER` | Switch provider — e.g. `nvidia-nim` (uses `NVIDIA_API_KEY`) |
| `RUST_LOG` | Logging verbosity (e.g. `RUST_LOG=debug`) |

#### MCP, Skills, and Hooks

- **MCP servers** — configure via `~/.codewhale/mcp.json` or `codewhale mcp add ...`. CodeWhale is both an MCP client and an MCP server (`codewhale mcp serve`).
- **Skills** — drop a `SKILL.md` under `~/.codewhale/skills/<name>/` (user-level) or `./.codewhale/skills/<name>/` (project-level).
- **Hooks** — pre/post lifecycle hooks (stdout / jsonl / webhook) configured in `[hooks]` in `config.toml`.
- **Sub-agents** — the model can spawn child agents via `agent_spawn` and use the full lifecycle family (`agent_wait`, `agent_result`, `agent_cancel`, ...).
- **RLM** — built-in recursive-LM tool processes oversized inputs in a sandboxed Python REPL without polluting the parent context.

#### HTTP runtime API

`codewhale serve --http` exposes a `/v1/*` runtime API for embedding CodeWhale in IDEs and web UIs (sessions, threads, turns, tasks, automations, MCP, skills). See [`docs/RUNTIME_API.md`](https://github.com/Hmbown/CodeWhale/blob/main/docs/RUNTIME_API.md) for the contract.
