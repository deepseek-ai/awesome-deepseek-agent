[English](./redcode.md) | [简体中文](./redcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 RedCode

RedCode 是基于 OpenCode 深度二次开发的中文母语 AI 编程助手，提供终端（TUI）与桌面（GUI）两种形态。它在 OpenCode 引擎之上增加了 DeepSeek 优先适配、前缀缓存优化和多模型支持。

#### 1. 安装 RedCode

```bash
git clone https://github.com/JiaHuiRed/RedCode.git
cd RedCode
bun install
```

#### 2. 配置 DeepSeek

打开 `~/.redcode/redcode.jsonc`，添加 DeepSeek 供应商：

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

> **100 万 token 上下文** — DeepSeek V4 支持最多 100 万 token 的上下文窗口，RedCode 通过 `limit.context` 暴露该能力。

> **深度思考** — DeepSeek V4 Pro 支持高推理强度。RedCode 内置的 DeepSeek 专属系统提示词已针对该模式优化。

#### 3. 启动使用

```bash
cd packages/opencode && bun run dev
```

- 输入 `/connect`，输入 `deepseek` 并选择供应商
- 选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`
- 开始编程
