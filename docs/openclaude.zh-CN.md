[English](./openclaude.md) | [简体中文](./openclaude.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenClaude

OpenClaude 是一个开源的编程 Agent 命令行工具，支持云端和本地模型提供商。它兼容 OpenAI API、Gemini、GitHub Models、Ollama 等多种后端，提供终端优先的工作流，包含工具调用、Agent、MCP 服务器、斜杠命令和流式输出等功能。

## 安装 OpenClaude

OpenClaude 需要 **Node.js 18+**。通过 npm 全局安装：

```sh
npm install -g @gitlawb/openclaude
```

安装后，请确保系统中已安装 **ripgrep**（`rg` 命令），可通过 `rg --version` 验证。

## 配置 DeepSeek 为模型提供商

### 方式一 — 环境变量（快速启动）

在启动 OpenClaude 前设置以下环境变量：

```sh
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_BASE_URL=https://api.deepseek.com/v1
export OPENAI_API_KEY=你的-DeepSeek-API-密钥
export OPENAI_MODEL=deepseek-v4-pro
```

**Windows (PowerShell)：**

```powershell
$env:CLAUDE_CODE_USE_OPENAI=1
$env:OPENAI_BASE_URL="https://api.deepseek.com/v1"
$env:OPENAI_API_KEY="你的-DeepSeek-API-密钥"
$env:OPENAI_MODEL="deepseek-v4-pro"
```

如需更快速且更具成本效益的体验，可将模型切换为 `deepseek-v4-flash`。如需设置不同的推理强度，可同时设置 `OPENAI_REASONING_EFFORT=max`。

从 [DeepSeek 平台](https://platform.deepseek.com/api_keys) 获取 API 密钥。

### 方式二 — 交互式配置（推荐）

1. 在终端中运行 `openclaude`。
2. 输入 `/provider` 并按引导提示操作。
3. 选择 **OpenAI-compatible** 作为提供商类型。
4. 输入 `https://api.deepseek.com/v1` 作为基础 URL。
5. 输入你的 DeepSeek API 密钥。
6. 输入 `deepseek-v4-pro` 或 `deepseek-v4-flash` 作为模型名称。

配置完成后，供应商配置文件将保存，后续会话无需重复配置。

## 运行 OpenClaude

进入你的项目目录并运行：

```sh
openclaude
```

OpenClaude 将加载 DeepSeek 模型，你就可以开始在终端中使用 Agent 工具、文件操作、MCP 服务器等各项功能进行编码了。
