[English](./gliding-horse.md) | [简体中文](./gliding-horse.zh-CN.md) · [← Back](../README.md)

# Integrate with Gliding Horse

Gliding Horse is an open-source industrial-grade AI agent operating system written in Rust. It orchestrates multiple agents through the PDCA cycle (Plan → Do → Check → Act), backed by a knowledge graph, a skill graph, and a 4-layer memory system (L0 Sled → L1 Session → L2 Blackboard → L3 Projection). It ships **Gliding Code**, a terminal AI coding assistant (TUI), and supports DeepSeek-V4-Pro and DeepSeek-V4-Flash with the full 1M-token context window. DeepSeek-V4-Flash uses the native **Responses API** (`/v1/responses`); other models fall back to chat completions automatically.

- **GitHub:** <https://github.com/doiito/gliding_horse>

#### 1. Install Gliding Code

Choose any of:

```sh
# Download a prebuilt binary from GitHub Releases (Linux musl, macOS, Windows):
#   https://github.com/doiito/gliding_horse/releases
tar xzf glidingcode-*.tar.gz     # Linux / macOS
./glidingcode --help

# Build from source (Rust toolchain required):
git clone https://github.com/doiito/gliding_horse.git
cd gliding_horse
cargo build -p code_cli --release
./target/release/glidingcode --help
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) and export it:

```sh
export DEEPSEEK_API_KEY="sk-..."
```

The API base URL defaults to `https://api.deepseek.com` (override with `DEEPSEEK_API_URL`).

#### 3. Run a one-shot task

```sh
./glidingcode "Explain how Rust's borrow checker works"
```

Or start the interactive TUI:

```sh
./glidingcode
```

By default Gliding Code uses **DeepSeek-V4-Flash**, which is routed through the native DeepSeek **Responses API** (`/v1/responses`) — no `data: [DONE]` terminator, semantic `response.*` SSE events. Switch models inside the TUI with `/model deepseek-v4-flash|deepseek-v4-pro`, or set the default on the CLI:

```sh
./glidingcode --model deepseek-v4-pro "Design a REST API for a todo app"
```

DeepSeek-V4 models support a **1M-token context window**; Gliding Code applies the full 1M context (`1_048_576`) for `deepseek-v4*` models, and reasoning content from native reasoning models is surfaced as thinking steps.

#### 4. Configuration

| Variable | Description |
|---|---|
| `DEEPSEEK_API_KEY` | API key (also accepts `AGENT_OS_GATEWAY_API_KEY`) |
| `DEEPSEEK_API_URL` | API base URL — defaults to `https://api.deepseek.com` |
| `USE_RESPONSES_API` | `1`/`true` to force the Responses API (`/v1/responses`), `0` to force chat completions. Defaults to `true` for DeepSeek-V4-Flash. |
| `GLIDING_HORSE_DATA` | Data directory for memory/knowledge-graph stores (defaults to `~/.gliding_horse/data`) |

#### 5. Key features

- **PDCA orchestration** — multi-agent Plan/Do/Check/Act cycles with 7-level adaptive execution (L0 instant → L6 emergency), so the model plans, executes, verifies, and refines until the task is done.
- **MCP support** — attach any MCP server with `--mcp-server name=url` (HTTP SSE) or `--mcp-server-stdio name='{"command":"npx","args":[...]}'` (stdio).
- **Knowledge graph & skill graph** — tasks are grounded in a knowledge graph, and completed work is recorded into a self-evolving skill graph.
- **Checkpoint & resume** — `--list-checkpoints` and `--resume <task_iri>` let you resume interrupted tasks.
- **Responses API native support** — DeepSeek-V4-Flash requests go through the official Responses API with streaming `response.*` events and tool-call roundtrips.
