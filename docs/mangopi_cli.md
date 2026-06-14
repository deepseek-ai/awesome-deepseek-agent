# Integrate with Mangopi CLI

Mangopi CLI is a single-file (1732 lines), zero-dependency AI coding assistant for the terminal. Built with only the Python standard library, it runs on Python 3.8+ — no Node.js, no Docker, no framework. Just one hackable `.py` file you can read in an afternoon.

**Key highlights:**
- **Single-file architecture** — 1732 lines, 23 classes, 13 built-in tools, all in one `mangopi_cli.py`
- **Zero runtime dependencies** — Python standard library only; `pip install mangopi-cli` pulls nothing
- **Three-tier context compression** — micro (truncate stale tool output) → session (compact old turns, keep last 10) → full (LLM-driven summary), keeping long autonomous sessions within the 1M token budget
- **Multi-provider support** — DeepSeek, OpenAI, MiniMax, and any OpenAI-compatible endpoint
- **Multimodal support** — can view images (PNG/JPG/WebP) directly in the terminal via `view_image` tool
- **13 built-in tools** — file I/O (read/write/edit with diff preview), regex grep, glob search, bash execution (with 7-category dangerous command detection + y/n confirmation), web search, image viewer, skill system, long-term memory, and more
- **Safety sandbox** — dangerous command patterns require explicit confirmation; file writes are restricted to project root via `realpath` validation
- **Goal Mode** — `/g` triggers autonomous plan → execute → verify → iterate loop with persistent checkpointing
- **13 test files** — comprehensive unit tests covering safety detection, all three compaction tiers, path sandbox (including prefix collision attacks), web search, system prompt assembly, and more
- **Python 3.8–3.12** — tested across all supported versions via GitHub Actions CI
- **PyPI published** — trusted publishing via OIDC, `pip install mangopi-cli`

### Installing Mangopi CLI from Scratch

Mangopi CLI requires Python 3.8+ and nothing else — no Node.js, no Docker, no frameworks. The entire runtime is a single `mangopi_cli.py` file (1732 lines).

#### Install via pip (recommended)

```bash
pip install mangopi-cli
```

#### Install from source

```bash
git clone git@github.com:w4n9H/mangopi-cli.git
cd mangopi-cli
python mangopi_cli.py
```

### Configuring Mangopi CLI

Mangopi CLI supports all OpenAI-compatible API endpoints. Set the following environment variables:

```bash
export MANGO_KEY="<your DeepSeek API Key>"
export MANGO_API_URL="https://api.deepseek.com"
export MANGO_MODEL="deepseek-v4-flash"
export MANGO_LANG="en"                          # en (default) | zh — UI language
```

> **Note**: Mangopi CLI supports up to **1,000,000 tokens** of context (configurable via `MANGO_MAX_CONTEXT`). DeepSeek V4 models with their 1M context window are a perfect match — combined with the three-tier compaction strategy, you can run long autonomous coding sessions without exhausting the context budget.

For DeepSeek V4 Pro with reasoning/thinking mode:

```bash
export MANGO_API_URL="https://api.deepseek.com"
export MANGO_MODEL="deepseek-v4-pro"
```

Mangopi CLI automatically enables thinking mode when the model supports it. DeepSeek V4 Pro supports `max` reasoning effort level out of the box.

### Using Mangopi CLI

Start Mangopi CLI in your project directory:

```bash
cd /path/to/my-project
mangopi-cli
```

Enter interactive mode and start coding. Mangopi CLI has 13 built-in tools including file read/write/edit (with unified-diff preview), regex grep, glob search, bash execution, web search, image viewing, and more.

#### Goal Mode

Use `/g` to let Mangopi CLI autonomously plan, execute, verify, and iterate until a goal is completed:

```
/g build a FastAPI todo app with tests
```

The agent will keep working until the task is complete or you stop it. Press `Ctrl+C` to pause; resume with `/g continue`.
