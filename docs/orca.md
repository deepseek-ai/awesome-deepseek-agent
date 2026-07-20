[English](./orca.md) | [简体中文](./orca.zh-CN.md) · [← Back](../README.md)

# Integrate with Orca

Orca is an open-source, DeepSeek-native coding agent for the terminal, built in Rust and distributed as a single binary. It talks to `api.deepseek.com` directly with SSE streaming, prefix-cache-friendly prompt assembly, the full 1M-token context window with automatic compaction, and OS-level sandboxing (Seatbelt on macOS, bubblewrap / Landlock + seccomp on Linux).

- **GitHub:** <https://github.com/echoVic/blade-deepseek>
- **Website:** <https://orcaagent.dev/>

#### 1. Install Orca

Choose either:

```sh
# npm (prebuilt binaries for macOS / Linux, ARM64 and x64)
npm install -g @blade-ai/orca

# Or the native install script
curl -fsSL https://orcaagent.dev/install.sh | sh
```

Verify:

```sh
orca --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then export it:

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. Enter a project directory and launch

```sh
cd /path/to/my-project
orca                              # interactive TUI
orca exec "fix the failing test"  # headless, for scripts and CI
```

By default Orca routes the main agent loop to **DeepSeek-V4-Pro** with reasoning effort **`max`**, and auxiliary work (summaries, compaction) to **DeepSeek-V4-Flash**. Use the `/model` menu in the TUI to change the model and reasoning effort (`high` / `max`), or set them in config:

```toml
# ~/.orca/config.toml
model = "deepseek-v4-pro"
reasoning_effort = "max"
```

Orca uses the full **1M-token context window** and compacts automatically at 80% pressure, preserving the system prompt and recent messages.

#### Key commands

| Command | What it does |
|---|---|
| `/mode` | Switch approval mode: `suggest` / `auto-edit` / `full-auto` |
| `/plan` | Read-only planning mode |
| `/goal` | Set a persistent objective; Orca keeps working with stall detection instead of a fixed turn ceiling |
| `/trust` | Manage folder trust (untrusted folders default to read-only, no network) |
| `/workflows` | Run background JavaScript workflows |
| `/cost` | Show session token usage and estimated cost |
| `@` | Search files, skills, plugins, and MCP resources |

#### Configuration

`~/.orca/config.toml` is the main config. Key environment overrides:

| Variable | Description |
|---|---|
| `DEEPSEEK_API_KEY` | API key |
| `ORCA_MODEL` | Override default model |
| `ORCA_BASE_URL` | API base URL — defaults to `https://api.deepseek.com` |
| `ORCA_REASONING_EFFORT` | Reasoning effort (`high` / `max`) |

#### MCP, Skills, and Verification

- **MCP servers** — stdio and SSE transports; MCP tools and resources join the unified `@` mention search. MCP elicitation requests are routed to interactive TUI prompts.
- **Skills** — drop a `SKILL.md` under `~/.orca/skills/<name>/` (user-level) or in a trusted project.
- **Verification** — `orca exec --verifier "cargo test" "fix it"` gates task completion on a real command passing.
- **Sandboxing** — shell commands run inside OS-level isolation; strict policies refuse to execute rather than fall back to running unsandboxed.
