[English](./codewhale.md) | [简体中文](./codewhale.zh-CN.md) · [← Back](../README.md)

# Integrate with CodeWhale (formerly DeepSeek-TUI)

CodeWhale is a DeepSeek-first open-source Rust terminal coding agent. It keeps DeepSeek as the default and first-class provider path, with native support for DeepSeek-V4-Pro / DeepSeek-V4-Flash, the full 1M-token context window, reasoning streaming, cache metrics, and thinking-effort control. At the same time, CodeWhale remains compatible with OpenRouter, local vLLM / SGLang / Ollama deployments, OpenAI-compatible gateways, and other open-model routes.

- **GitHub:** <https://github.com/Hmbown/CodeWhale>
- **Website:** <https://codewhale.net/>

#### 1. Install CodeWhale

Choose any of:

```sh
# npm (cross-platform prebuilt binaries)
npm install -g codewhale

# Cargo (build from source — Rust 1.88+ required)
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

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then save it for the DeepSeek provider:

```sh
codewhale auth set --provider deepseek
codewhale auth status
codewhale doctor
```

You can also set `DEEPSEEK_API_KEY` as an environment variable. Saved config lives in `~/.codewhale/config.toml`; legacy `~/.deepseek/` config is still read as a compatibility fallback.

#### 3. Enter a project directory and launch

```sh
cd /path/to/my-project
codewhale
```

`codewhale` is the canonical entry point. It dispatches to the interactive TUI by default, or to subcommands like `codewhale doctor`, `codewhale mcp list`, `codewhale serve --http`, `codewhale exec`, `codewhale -p "one-shot prompt"`, and `codewhale --yolo`.

By default, CodeWhale uses the native DeepSeek provider and **DeepSeek-V4-Pro**. Press `Shift+Tab` to cycle reasoning effort (`off → high → max`). Press `Tab` to cycle modes:

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

`~/.codewhale/config.toml` is the main config. Key environment overrides:

| Variable | Description |
|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API key |
| `DEEPSEEK_BASE_URL` | DeepSeek API base URL, defaults to `https://api.deepseek.com` |
| `DEEPSEEK_MODEL` | Override the DeepSeek model, e.g. `deepseek-v4-pro` or `deepseek-v4-flash` |
| `CODEWHALE_PROVIDER` | Select a provider route, e.g. `deepseek`, `openrouter`, `vllm`, `sglang`, or `ollama` |
| `CODEWHALE_MODEL` | Override the selected provider's model |
| `RUST_LOG` | Logging verbosity, e.g. `RUST_LOG=debug` |

`DEEPSEEK_PROVIDER` remains accepted as a legacy alias, but new configs should prefer `CODEWHALE_PROVIDER`.

#### MCP, Skills, and Hooks

- **MCP servers** — configure via `~/.codewhale/mcp.json` or `codewhale mcp add ...`. CodeWhale is both an MCP client and an MCP server (`codewhale mcp serve`).
- **Skills** — drop a `SKILL.md` under `~/.codewhale/skills/<name>/` (user-level) or `./.codewhale/skills/<name>/` (project-level).
- **Hooks** — pre/post lifecycle hooks (stdout / jsonl / webhook) configured in `[hooks]` in `config.toml`.
- **Sub-agents / Fleet** — CodeWhale can run child agents and Fleet workers through the same provider-aware runtime.
- **Local and open-model routes** — OpenRouter, vLLM, SGLang, Ollama, and other provider routes use the same approvals, sandboxing, rollback, and tool surface.

#### HTTP runtime API

`codewhale serve --http` exposes a `/v1/*` runtime API for embedding CodeWhale in IDEs and web UIs (sessions, threads, turns, tasks, automations, MCP, skills). See [`docs/RUNTIME_API.md`](https://github.com/Hmbown/CodeWhale/blob/main/docs/RUNTIME_API.md) for the contract.
