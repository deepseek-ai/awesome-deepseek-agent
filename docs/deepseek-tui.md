[English](./deepseek-tui.md) | [简体中文](./deepseek-tui.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek-TUI

DeepSeek-TUI is an open-source terminal AI coding assistant built in Rust as a Codex-style 13-crate workspace. It talks to `api.deepseek.com` directly, supports DeepSeek-V4-Pro and DeepSeek-V4-Flash with the full 1M-token context window, and ships sandboxed tool execution on macOS (Seatbelt), Linux (Landlock), and Windows.

- **GitHub:** <https://github.com/Hmbown/DeepSeek-TUI>

#### 1. Install DeepSeek-TUI

Choose any of:

```sh
# npm (cross-platform prebuilt binaries)
npm install -g deepseek-tui

# Cargo (build from source — Rust 1.85+ required)
cargo install deepseek-tui-cli

# Or download a release binary from
#   https://github.com/Hmbown/DeepSeek-TUI/releases
```

Verify:

```sh
deepseek --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). On first run, `deepseek auth` walks you through saving it to `~/.deepseek/config.toml`. You can also set `DEEPSEEK_API_KEY` as an environment variable.

#### 3. Enter a project directory and launch

```sh
cd /path/to/my-project
deepseek
```

`deepseek` is the canonical entry point. It dispatches to the interactive TUI by default, or to subcommands like `deepseek doctor`, `deepseek mcp list`, `deepseek serve --http`, `deepseek -p "one-shot prompt"`, and `deepseek --yolo`.

By default DeepSeek-TUI uses **DeepSeek-V4-Pro**. Press `Shift+Tab` to cycle reasoning effort (`off → high → max`). Press `Tab` to cycle modes:

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

`~/.deepseek/config.toml` is the main config (see `config.example.toml` in the repo for every option). Key environment overrides:

| Variable | Description |
|---|---|
| `DEEPSEEK_API_KEY` | API key (overrides config) |
| `DEEPSEEK_BASE_URL` | API base URL — defaults to `https://api.deepseek.com`; use `https://api.deepseeki.com` for the China endpoint |
| `DEEPSEEK_MODEL` | Override default model |
| `DEEPSEEK_PROVIDER` | Switch provider — e.g. `nvidia-nim` (uses `NVIDIA_API_KEY`) |
| `RUST_LOG` | Logging verbosity (e.g. `RUST_LOG=debug`) |

#### MCP, Skills, and Hooks

- **MCP servers** — configure via `~/.deepseek/mcp.json` or `deepseek mcp add ...`. DeepSeek-TUI is both an MCP client and an MCP server (`deepseek mcp serve`).
- **Skills** — drop a `SKILL.md` under `~/.deepseek/skills/<name>/` (user-level) or `./.deepseek/skills/<name>/` (project-level).
- **Hooks** — pre/post lifecycle hooks (stdout / jsonl / webhook) configured in `[hooks]` in `config.toml`.
- **Sub-agents** — the model can spawn child agents via `agent_spawn` and use the full lifecycle family (`agent_wait`, `agent_result`, `agent_cancel`, ...).
- **RLM** — built-in recursive-LM tool processes oversized inputs in a sandboxed Python REPL without polluting the parent context.

#### HTTP runtime API

`deepseek serve --http` exposes a `/v1/*` runtime API for embedding DeepSeek-TUI in IDEs and web UIs (sessions, threads, turns, tasks, automations, MCP, skills). See [`docs/RUNTIME_API.md`](https://github.com/Hmbown/DeepSeek-TUI/blob/main/docs/RUNTIME_API.md) for the contract.
