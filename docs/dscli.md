[English](./dscli.md) | [简体中文](./dscli.zh-CN.md) · [← Back](../README.md)

# Integrate with dscli

dscli is an AI-enhanced developer toolbox that runs in the terminal. It connects directly to the DeepSeek API and supports AI chat with tool calling (file operations, Git, code search, etc.), code completion, and more.

- **GitCode:** <https://gitcode.com/dscli/dscli>

#### 1. Install Go

- Install [Go](https://go.dev/dl/) 1.21+.

#### 2. Install dscli

```bash
# Install via go install (recommended)
go install gitcode.com/dscli/dscli@latest

# Or clone and build from source
git clone https://gitcode.com/dscli/dscli.git
cd dscli
make install
```

Verify the installation:

```bash
dscli version
```

#### 3. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 4. Configure

Set your API key as an environment variable:

```bash
export DEEPSEEK_API_KEY="sk-..."
```

Optional environment variables:

| Variable | Description | Default |
|---|---|---|
| `DEEPSEEK_API_KEY` | Your DeepSeek API key (required) | — |
| `DEEPSEEK_BASE_URL` | API base URL | `https://api.deepseek.com` |
| `MODEL_DEEPSEEK_CHAT` | Chat model name | `deepseek-v4-flash` |
| `MODEL_DEEPSEEK_REASONER` | Reasoner model name | `deepseek-v4-pro` |

Configuration files are stored under `~/.dscli/`:
- `dscli.env` — environment overrides
- `sqlite.db` — chat history database
- `dscli.log` — log file

#### 5. Use dscli

**AI Chat with tool calling:**

```bash
# Basic chat (Markdown output)
echo "Create a main.go file with an HTTP server" | dscli chat

# Use the pro model for complex analysis
echo "Analyze the performance bottlenecks in this code" | dscli chat --model deepseek-v4-pro

# Org-mode output
echo "Explain this algorithm" | dscli chat --mode org

# Stream output
echo "Write a function to reverse a linked list" | dscli chat --stream
```

**Code completion:**

```bash
echo "func fibonacci(n int) int {" | dscli fim
```

**Check models and balance:**

```bash
# List available models
dscli models

# Check account balance
dscli balance

# JSON format output
dscli models --format json
dscli balance --format json
```

#### Key Features

- **Tool calling** — the AI can read/write files, run Git commands, search code, and more
- **Project-aware** — automatically detects the Git repo root and isolates chat history per project
- **Multi-format output** — Markdown (default) and Org mode
- **Streaming** — real-time token-by-token output with `--stream`
- **SQLite storage** — persistent chat history for context-aware conversations

#### Shortcuts / Flags

| Flag | Description |
|---|---|
| `--model` | Model to use: `deepseek-v4-flash` (default) or `deepseek-v4-pro` |
| `--mode` | Output mode: `markdown` (default) or `org` |
| `--stream` | Enable streaming output |
| `--histsize` | Number of history messages to load (default: 8) |
| `--verbose` | Enable verbose/debug output |
| `--no-color` | Disable color output |
| `--no-timestamp` | Disable timestamp display |
