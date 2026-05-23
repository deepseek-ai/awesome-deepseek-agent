[English](./halfcopilot.md) | [简体中文](./halfcopilot.zh-CN.md) · [← Back](../README.md)

# Integrate with HalfCopilot

HalfCopilot is an open-source multi-model agent framework CLI with a beautiful chat interface. It supports DeepSeek, MiniMax, Qwen, OpenAI, and Anthropic providers with built-in tools, a skills system, MCP protocol, and persistent memory.

#### 1. Install HalfCopilot

- Install [Node.js](https://nodejs.org/en/download/) 20+.
- Run the following command in your terminal to install HalfCopilot:

```bash
npm install -g halfcopilot
```

- After installation, verify the installation:

```bash
halfcop --version
```

#### 2. Configure DeepSeek Provider

HalfCopilot stores its configuration at `~/.halfcopilot/settings.json`. Run the interactive setup to add DeepSeek:

```bash
halfcop setup
```

Select **DeepSeek** from the provider list, then enter your API key. The setup automatically configures the following models:

| Model | Context Window | Max Output |
|-------|---------------|------------|
| `deepseek-v4-pro` | 131,072 (1M via API) | 8,192 |
| `deepseek-v4-flash` | 131,072 (1M via API) | 8,192 |
| `deepseek-chat` | 65,536 | 8,192 |
| `deepseek-reasoner` | 65,536 | 8,192 |

> **Note:** DeepSeek V4 models support up to **1 million tokens** of context through the API. The `context_window` in HalfCopilot's config reflects the guaranteed limit for prompt caching and sliding window management.

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Run and Select Model

- Start the interactive chat:

```bash
halfcop
```

- Use `/model` to list available models and switch by number or name:

```bash
/model                # List models with indices
/model 2              # Switch by index
/model deepseek-v4-pro # Switch by name
```

- Use `/provider` to switch between configured providers:

```bash
/provider deepseek    # Switch to DeepSeek
```

#### 4. Using Agent Features

HalfCopilot provides an agent loop with tool execution, thinking mode support, and skills:

- **Tool use**: File operations, bash, grep, glob — auto-approved or confirmed based on permissions.
- **Thinking mode**: DeepSeek V4 models with `<think>` tags are rendered inline in the chat interface.
- **Skills**: Built-in skills for git commits, test running, code review, documentation generation, and refactoring.
- **MCP support**: Connect external tools via the MCP protocol (configured in `settings.json`).

#### 5. Single Command Mode

Run a single prompt without entering interactive mode:

```bash
halfcop run "Explain this codebase"
halfcop run --provider deepseek --model deepseek-v4-pro "Review this file"
```

#### Configuration Reference

```json
{
  "defaultProvider": "deepseek",
  "defaultModel": "deepseek-v4-pro",
  "providers": {
    "deepseek": {
      "type": "openai-compatible",
      "baseUrl": "https://api.deepseek.com",
      "apiKey": "sk-...",
      "models": {
        "deepseek-v4-pro": { "contextWindow": 131072, "maxOutput": 8192 },
        "deepseek-v4-flash": { "contextWindow": 131072, "maxOutput": 8192 }
      }
    }
  },
  "maxTurns": 50
}
```
