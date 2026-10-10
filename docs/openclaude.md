[English](./openclaude.md) | [简体中文](./openclaude.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenClaude

OpenClaude is an open-source coding-agent CLI for cloud and local model providers. It supports OpenAI-compatible APIs, Gemini, GitHub Models, Ollama, and more, with a terminal-first workflow featuring tools, agents, MCP servers, slash commands, and streaming output.

## Install OpenClaude

OpenClaude requires **Node.js 18+**. Install globally via npm:

```sh
npm install -g @gitlawb/openclaude
```

After installation, ensure **ripgrep** (`rg`) is available on your system. Verify with `rg --version`.

## Configure DeepSeek as the Provider

### Option 1 — Environment Variables (Quick Start)

Set the following environment variables before launching OpenClaude:

```sh
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_BASE_URL=https://api.deepseek.com/v1
export OPENAI_API_KEY=your-deepseek-api-key
export OPENAI_MODEL=deepseek-v4-pro
```

**Windows (PowerShell):**

```powershell
$env:CLAUDE_CODE_USE_OPENAI=1
$env:OPENAI_BASE_URL="https://api.deepseek.com/v1"
$env:OPENAI_API_KEY="your-deepseek-api-key"
$env:OPENAI_MODEL="deepseek-v4-pro"
```

You can switch to `deepseek-v4-flash` for a faster and more cost-effective experience. To set a different reasoning effort, also set `OPENAI_REASONING_EFFORT=max`.

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

### Option 2 — Interactive Setup (Recommended)

1. Run `openclaude` in your terminal.
2. Type `/provider` and follow the guided prompts.
3. Select **OpenAI-compatible** as the provider type.
4. Enter `https://api.deepseek.com/v1` as the base URL.
5. Enter your DeepSeek API key.
6. Enter `deepseek-v4-pro` or `deepseek-v4-flash` as the model name.

The provider profile will be saved for future sessions.

## Run OpenClaude

Navigate to your project directory and run:

```sh
openclaude
```

OpenClaude will load the DeepSeek model and you can start coding with agentic tools, file operations, MCP servers, and more — all from the terminal.
