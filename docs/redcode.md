[English](./redcode.md) | [简体中文](./redcode.zh-CN.md) · [← Back](../README.md)

# Integrate with RedCode

RedCode is a Chinese-native AI coding agent forked from OpenCode, available in terminal (TUI) and desktop (GUI). It adds DeepSeek-first tuning, prefix-cache optimization, and multi-model support on top of the OpenCode engine.

#### 1. Install RedCode

```bash
git clone https://github.com/JiaHuiRed/RedCode.git
cd RedCode
bun install
```

#### 2. Configure DeepSeek

Open `~/.redcode/redcode.jsonc` and add the DeepSeek provider:

```jsonc
"provider": {
  "deepseek": {
    "options": {
      "baseURL": "https://api.deepseek.com/v1",
      "apiKey": "<YOUR_DEEPSEEK_API_KEY>"
    },
    "models": {
      "deepseek-v4-pro": {
        "name": "DeepSeek V4 Pro",
        "temperature": true,
        "reasoning": true,
        "tool_call": true,
        "limit": { "context": 1000000, "output": 65536 }
      },
      "deepseek-v4-flash": {
        "name": "DeepSeek V4 Flash",
        "temperature": true,
        "reasoning": true,
        "tool_call": true,
        "limit": { "context": 1000000, "output": 65536 }
      }
    }
  }
}
```

> **1M context** — DeepSeek V4 supports up to 1 million tokens of context. RedCode exposes this via `limit.context`.

> **Max thinking** — DeepSeek V4 Pro supports high reasoning effort. RedCode's DeepSeek-specific system prompt is optimized for this mode out of the box.

#### 3. First Run

```bash
cd packages/opencode && bun run dev
```

- Press `/connect`, type `deepseek`, and select the provider.
- Choose `deepseek-v4-pro` or `deepseek-v4-flash`.
- Start coding.
