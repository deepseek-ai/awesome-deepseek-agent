[English](./lingxi.md) | [简体中文](./lingxi.zh-CN.md) · [← Back](../README.md)

# Integrate with LingXi

LingXi (灵犀) is a multi-model AI coding agent that runs in the terminal, powered by a pluggable LLM layer. It comes with built-in skills, MCP support, HTTP server mode, and a rich tool ecosystem (shell, file operations, and browser).

- **Homepage:** <https://lingxi.regaing.com>
- **npm:** <https://www.npmjs.com/package/@lingxi-agent/core>

#### 1. Install LingXi

- Install [Node.js](https://nodejs.org/en/download/) 20+.
- Run the following command in your terminal:

```sh
npm install -g @lingxi-agent/core
```

- Verify the installation:

```sh
lingxi --version
```

#### 2. Configure DeepSeek

LingXi defaults to DeepSeek as the provider with `deepseek-v4-flash` (fast) and `deepseek-v4-pro` (think). Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Option 1: Environment variable (simplest)**

Linux / Mac:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Windows:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

**Option 2: Configuration file**

Create `~/.LingXi/config.json` for user-level config, or `.agent/config.json` in your project for project-level settings:

```json
{
  "agentProviders": [
    {
      "id": "deepseek",
      "name": "DeepSeek",
      "provider": "deepseek",
      "fastModel": "deepseek-v4-flash",
      "thinkModel": "deepseek-v4-pro",
      "visionModel": "",
      "apiKey": "<your DeepSeek API Key>",
      "baseURL": "https://api.deepseek.com"
    }
  ]
}
```

> **Note:** You can also use `"apiKey": "$DEEPSEEK_API_KEY"` to reference an environment variable instead of hardcoding the key.

**Configuration overview:**

| Option | Default | Description |
|--------|---------|-------------|
| `permissionMode` | `normal` | Tool execution policy (`normal`, `auto`, `strict`) |
| `maxTokens` | `1048576` | Context window (1M tokens, matching DeepSeek V4) |
| `maxToolCallRounds` | `100` | Maximum tool-calling iterations per task |
| `reasoningEffort` | `medium` | Reasoning level (`low`, `medium`, `high`) |
| `toolTimeout` | `300000` | Per-tool execution timeout in ms |

LingXi supports DeepSeek's full 1M-token context window out of the box. Set `reasoningEffort` to `high` in your config for maximum reasoning depth with DeepSeek-V4-Pro.

#### 3. Run LingXi

**Interactive REPL mode:**

```sh
cd /path/to/my-project
lingxi
```

**Task mode (non-interactive):**

```sh
lingxi --task "Write a Python script to analyze CSV files" --auto
```

**HTTP Server mode (for programmatic access):**

```sh
lingxi serve --port 7907
```

The server exposes:
- `POST /rpc` — Send tasks and receive responses
- `GET /events?sessionId=` — Server-sent events stream
- `GET /healthz` — Health check

#### Key Features

| Feature | Description |
|---------|-------------|
| **13 Built-in Skills** | Auto-discovered from `~/.LingXi/skills/` and project `.agent/skills/` |
| **MCP Support** | Connect external tools via Model Context Protocol |
| **Multi-Provider** | DeepSeek, OpenAI, Anthropic, Qwen, Groq, Mistral, Gemini |
| **Tool Ecosystem** | Shell commands, file read/write, browser automation, SSH remote execution |
| **Task Tracking** | Built-in structured task management with desktop notification sync |
| **Compaction** | Automatic context compaction to stay within token limits |
