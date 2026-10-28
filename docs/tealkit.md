[English](./tealkit.md) | [简体中文](./tealkit.zh-CN.md) · [← Back](../README.md)

# Integrate with TealKit CLI

TealKit CLI (`tealkit`) is an open-source terminal AI coding agent, workflow runner, and AgentSkills execution environment. It features Claude Code / Roo Code style autonomous coding modes (Architect, Code, and Ask), 10 native filesystem and terminal execution tools, Model Context Protocol (MCP) server support, and local RAG.

- **GitHub:** <https://github.com/lschaffer/tealkit>
- **Website:** <https://tealkit.dev>

---

#### 1. Install TealKit CLI

You can install TealKit CLI via pre-packaged standalone release or compile it from source using the Dart SDK.

- **Standalone Windows x64 Bundle:**
  Download and unzip [`tealkit_cli_setup.zip`](https://tealkit.dev/download/tealkit_cli_setup.zip) (~55MB, includes `tealkit.exe`, required native runtime dynamic libraries, and default configurations).

- **Build from Source (Dart SDK >= 3.8 / Flutter):**
  ```bash
  git clone https://github.com/lschaffer/tealkit.git
  cd tealkit/cli
  dart pub get
  dart build cli -o build/cli
  ```

- **Verify installation:**
  ```bash
  tealkit --version
  ```

---

#### 2. Configure DeepSeek

TealKit CLI configures LLM providers in `llm.yaml` (located in your working directory or global settings `~/.tealkit/llm.yaml`).

1. Set your DeepSeek API key:
   - **Linux / macOS:**
     ```bash
     export DEEPSEEK_API_KEY="sk-..."
     ```
   - **Windows (PowerShell):**
     ```powershell
     $env:DEEPSEEK_API_KEY="sk-..."
     ```
   *(Or set `DEEPSEEK_API_KEY=sk-...` in your project `.env` file)*

2. Configure DeepSeek V4 models in `llm.yaml`:

```yaml
# TealKit LLM Configuration
temperature: 0.2
max_tokens: 8192
max_tool_iterations: 150

llms:
  - name: "deepseek"
    provider: "openai_compatible"
    model: "deepseek-v4-pro"
    api_key: "${DEEPSEEK_API_KEY}"
    base_url: "https://api.deepseek.com/v1"
    context_window: 1000000
    reasoning_effort: "max"

  - name: "deepseek-flash"
    provider: "openai_compatible"
    model: "deepseek-v4-flash"
    api_key: "${DEEPSEEK_API_KEY}"
    base_url: "https://api.deepseek.com/v1"
    context_window: 1000000
```

> **Note on DeepSeek V4 Capabilities:**
> - **1M Context Window:** DeepSeek V4 models support up to **1,000,000 tokens** of context window (`context_window: 1000000`).
> - **Reasoning Effort:** `deepseek-v4-pro` supports deep thinking mode with `reasoning_effort: "max"` for complex coding and architectural analysis.

---

#### 3. First Run

Run TealKit's autonomous coding agent inside any project directory:

```bash
# Launch interactive coding agent REPL (defaults to active LLM in llm.yaml)
tealkit code

# Or run a direct prompt turn
tealkit code "Analyze this repository and summarize the architecture"
```

#### Interactive Commands & Slash Shortcuts

Inside the REPL:
- `/llm deepseek` — Switch to `deepseek-v4-pro` on the fly.
- `/cost` or `/estimated_costs` — Display real-time token counts and cost estimation.
- `/save <name>` / `/resume <name>` — Persist and resume multi-turn coding sessions.
- `Ctrl+V` — Paste clipboard content directly into terminal prompts.
- `Ctrl+Enter` / `Enter` (configurable) — Send prompt to the agent.

#### Using Agent Skills (`SKILL.md`)

TealKit automatically discovers and executes AgentSkills from:
- `~/.tealkit/skills/<name>/SKILL.md`
- `./skills/<name>/SKILL.md`

All skills automatically receive native filesystem, terminal execution, and web search tools without requiring custom boilerplate tool declarations.
