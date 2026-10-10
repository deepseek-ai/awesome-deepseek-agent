[English](./lingxi.md) | [简体中文](./lingxi.zh-CN.md) · [← Back](../README.md)

# 接入 LingXi（灵犀）

LingXi（灵犀）是一款运行在终端内的多模型 AI 编程 Agent，由可插拔 LLM 层驱动。内置 Skills、MCP 支持、HTTP 服务模式，以及丰富的工具生态（Shell 命令、文件操作、浏览器自动化等）。

- **官网:** <https://lingxi.regaing.com>
- **npm:** <https://www.npmjs.com/package/@lingxi-agent/core>

#### 1. 安装 LingXi

- 安装 [Node.js](https://nodejs.org/en/download/) 20+。
- 在终端中运行以下命令：

```sh
npm install -g @lingxi-agent/core
```

- 验证安装：

```sh
lingxi --version
```

#### 2. 配置 DeepSeek

LingXi 默认使用 DeepSeek 作为提供商，fast 模型为 `deepseek-v4-flash`、think 模型为 `deepseek-v4-pro`。从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**方式一：环境变量（推荐）**

Linux / Mac：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

**方式二：配置文件**

创建 `~/.LingXi/config.json`（用户级）或项目中的 `.agent/config.json`（项目级）：

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
      "apiKey": "<你的 DeepSeek API Key>",
      "baseURL": "https://api.deepseek.com"
    }
  ]
}
```

> **提示：** 也可使用 `"apiKey": "$DEEPSEEK_API_KEY"` 引用环境变量，避免在配置文件中明文存储密钥。

**配置项概览：**

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `permissionMode` | `normal` | 工具执行策略（`normal`、`auto`、`strict`） |
| `maxTokens` | `1048576` | 上下文窗口（1M tokens，完整支持 DeepSeek V4） |
| `maxToolCallRounds` | `100` | 单次任务最大工具调用轮数 |
| `reasoningEffort` | `medium` | 推理强度（`low`、`medium`、`high`） |
| `toolTimeout` | `300000` | 单次工具执行超时（毫秒） |

LingXi 原生支持 DeepSeek V4 的 100 万 token 上下文窗口。将 `reasoningEffort` 设为 `high` 可获得 DeepSeek-V4-Pro 的最大推理深度。

#### 3. 运行 LingXi

**交互式 REPL 模式：**

```sh
cd /path/to/my-project
lingxi
```

**任务模式（非交互）：**

```sh
lingxi --task "写一个 Python 脚本来分析 CSV 文件" --auto
```

**HTTP 服务模式（供程序调用）：**

```sh
lingxi serve --port 7907
```

服务端提供以下端点：
- `POST /rpc` — 发送任务并接收响应
- `GET /events?sessionId=` — Server-Sent Events 流
- `GET /healthz` — 健康检查

#### 核心特性

| 特性 | 说明 |
|------|------|
| **13 个内置 Skills** | 自动发现 `~/.LingXi/skills/` 和项目 `.agent/skills/` 中的技能 |
| **MCP 支持** | 通过 Model Context Protocol 接入外部工具 |
| **多提供商** | DeepSeek、OpenAI、Anthropic、Qwen、Groq、Mistral、Gemini |
| **工具生态** | Shell 命令、文件读写、浏览器自动化、SSH 远程执行 |
| **任务追踪** | 内置结构化任务管理，支持桌面通知同步 |
| **上下文压缩** | 自动压缩上下文以保持在 token 限制内 |
