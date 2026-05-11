[English](./halfcopilot.md) | [简体中文](./halfcopilot.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 HalfCopilot

HalfCopilot 是一个开源的**多模型 Agent 框架 CLI**，提供漂亮的聊天界面，支持 DeepSeek、MiniMax、Qwen、OpenAI、Anthropic 等多家模型供应商，内置工具系统、技能系统、MCP 协议和持久化记忆能力。

#### 1. 安装 HalfCopilot

- 安装 [Node.js](https://nodejs.org/en/download/) 20+。
- 在终端中运行以下命令安装 HalfCopilot：

```bash
npm install -g halfcopilot
```

- 安装完成后验证版本：

```bash
halfcop --version
```

#### 2. 配置 DeepSeek 供应商

HalfCopilot 的配置文件位于 `~/.halfcopilot/settings.json`。运行交互式配置来添加 DeepSeek：

```bash
halfcop setup
```

在厂商列表中选择 **DeepSeek**，然后输入你的 API Key。配置工具会自动设置以下模型：

| 模型 | 上下文窗口 | 最大输出 |
|------|-----------|---------|
| `deepseek-v4-pro` | 131,072（API 支持 1M） | 8,192 |
| `deepseek-v4-flash` | 131,072（API 支持 1M） | 8,192 |
| `deepseek-chat` | 65,536 | 8,192 |
| `deepseek-reasoner` | 65,536 | 8,192 |

> **注意：** DeepSeek V4 系列 API 支持高达 **100 万 token** 上下文。HalfCopilot 配置中的 `context_window` 是 prompt 缓存和滑动窗口管理的有保障限制。

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 运行与切换模型

- 启动交互式聊天：

```bash
halfcop
```

- 使用 `/model` 查看可用模型并通过编号或名称切换：

```bash
/model                # 列出模型及编号
/model 2              # 按编号切换
/model deepseek-v4-pro # 按名称切换
```

- 使用 `/provider` 在已配置的厂商间切换：

```bash
/provider deepseek
```

#### 4. 使用 Agent 功能

HalfCopilot 提供完整的 Agent 循环，包含工具执行、思考模式和技能系统：

- **工具使用**：文件操作、bash、grep、glob —— 基于权限自动批准或需确认。
- **思考模式**：DeepSeek V4 模型的 `<think>` 标签内容会在聊天界面中内联渲染。
- **技能系统**：内置 git 提交、测试运行、代码审查、文档生成和重构技能。
- **MCP 支持**：通过 MCP 协议连接外部工具（在 `settings.json` 中配置）。

#### 5. 单命令模式

无需进入交互模式，直接执行单个 prompt：

```bash
halfcop run "解释这段代码"
halfcop run --provider deepseek --model deepseek-v4-pro "Review this file"
```

#### 配置参考

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
