[English](./ok.md) | [简体中文](./ok.zh-CN.md) ↩ [← Back](./../README.md)

# Integrate with OK

OK is an open-source **AI agent infrastructure** — a single 15 MB static binary that
packs self-evolving skills, multi-agent DAG orchestration, OS-level sandbox (macOS
Seatbelt, Linux Landlock, Windows AppContainer), MCP-native plugin support, and a
cryptographic ProofChain audit trail into one engine. It ships with TUI, desktop
(Wails), VS Code, and JetBrains frontends, plus 7 chat-platform bots out of the box.

DeepSeek is OK's **default and recommended** model provider. The config ships
pre-set for `deepseek-v4-flash` and `deepseek-v4-pro`, with 1M context window,
max thinking effort, and zero-translation direct calls to `api.deepseek.com`.

#### 1. Prerequisites

- [Go](https://go.dev/dl/) 1.22+ (to build from source), or download a
  [pre-built binary](https://github.com/NB-Agent/ok/releases).
- **Windows users** — Git for Windows is recommended so `bash` works out of the box.

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
You'll set it as the `DEEPSEEK_API_KEY` environment variable — OK reads it on
startup and never stores it on disk.

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. Install OK

```sh
# Build from source (recommended — single static binary)
git clone https://github.com/NB-Agent/ok.git
cd ok
make build          # → bin/ok
# or: make cross    # → dist/ (darwin|linux|windows × amd64|arm64)

# Move it somewhere on PATH
mv bin/ok /usr/local/bin/
```

Or download a pre-built binary from the
[releases page](https://github.com/NB-Agent/ok/releases).

#### 4. Configure

Run the setup wizard (interactive, creates `ok.toml` in your current directory):

```sh
ok setup
```

Choose **DeepSeek** when prompted for a provider. The wizard enables both
`deepseek-v4-flash` (default executor) and `deepseek-v4-pro` (for complex tasks).

Or copy this minimal `ok.toml` to your project root:

```toml
default_model = "deepseek"

[[providers]]
name           = "deepseek"
kind           = "openai"
base_url       = "https://api.deepseek.com"
models         = ["deepseek-v4-flash", "deepseek-v4-pro"]
default        = "deepseek-v4-flash"
api_key_env    = "DEEPSEEK_API_KEY"
context_window = 1000000
```

> [!TIP]
> Set `planner_model = "deepseek-v4-pro"` under `[agent]` to enable two-model
> collaboration — a low-frequency planner (Pro) that decomposes tasks and a fast
> executor (Flash) that runs them.

OK configures **max thinking effort** automatically for `deepseek-v4-pro` via
the OpenAI-compatible `reasoning_effort` parameter, so you get the best coding
experience with zero extra setup.

#### 5. First Run

```sh
# Enter your project
cd /path/to/my-project

# Interactive chat
ok chat

# Headless (CI / scripts)
ok run "implement the TODOs in main.go"

# Use Pro for a single task
ok run --model deepseek-v4-pro "add unit tests for this function"
```

Inside `ok chat`, type `/init` to generate an `AGENTS.md` (project memory) so
the agent understands your codebase. Type `/help` for the full slash-command
reference.

<div align="center">
<img src="https://raw.githubusercontent.com/NB-Agent/ok/main/docs/logo.svg" width='640' />
</div>
