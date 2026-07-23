[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← Back](../README.md)

# 接入 Grok Build

Grok Build (`grok`) 是 xAI 推出的终端 AI 编程 Agent —— 一个全屏 TUI 界面，能够理解代码库、编辑文件、执行 Shell 命令、搜索网页、管理后台任务并编排子 Agent。其多模型架构原生支持多种模型后端：默认使用 xAI 的 Grok 模型，其他第三方供应商（包括 **DeepSeek**）可通过 `~/.grok/config.toml` 进行配置。

- **GitHub:** <https://github.com/xai-org/grok-build>

### 1. 安装 Grok Build

```sh
# macOS / Linux / Git Bash
curl -fsSL https://x.ai/cli/install.sh | bash

# Windows PowerShell
irm https://x.ai/cli/install.ps1 | iex

# 验证安装
grok --version
```

### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

### 3. 配置 DeepSeek 作为模型供应商

打开 `~/.grok/config.toml`，为每个 DeepSeek 模型添加 `[model.<id>]` 配置块。最简配置如下：

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
api_backend = "chat_completions"
context_window = 1000000
provider_alias = "d"
provider_name = "DeepSeek"

[model.deepseek-v4-flash]
model = "deepseek-v4-flash"
base_url = "https://api.deepseek.com/v1"
api_backend = "chat_completions"
context_window = 1000000
provider_alias = "d"
provider_name = "DeepSeek"
```

> **API Key 设置：** 通过 `DEEPSEEK_API_KEY` 环境变量设置 API Key，或在模型配置中使用 `env_key` / `api_key`：
>
> ```toml
> env_key = "DEEPSEEK_API_KEY"
> # 或
> api_key = "sk-your-deepseek-api-key"
> ```

#### 将 DeepSeek 设为默认模型

在 `[models]` 配置段中指定默认模型：

```toml
[models]
default = "deepseek-v4-pro"
```

#### 推理 / 思考模式

DeepSeek V4 Pro 支持 `max` 和 `high` 两种推理强度。在模型配置中启用：

```toml
[model.deepseek-v4-pro]
# ...（其他字段如上）
reasoning_effort = "max"
supports_reasoning_effort = true
```

在 TUI 中可通过 `Ctrl+R` 循环切换推理强度。

### 4. 启动 Grok Build

```sh
cd /path/to/your-project
grok
```

Grok Build 启动时使用默认模型。使用以下命令在运行时切换：

| 命令 | 功能 |
|---------|------|
| `/m deepseek-v4-pro` | 切换到 DeepSeek V4 Pro |
| `/m deepseek-v4-flash` | 切换到 DeepSeek V4 Flash |
| `/m:d` | 切换到 `provider_alias = "d"` 对应的模型（DeepSeek） |

也可以在启动时指定模型：

```sh
grok -m deepseek-v4-pro
```

### 核心功能

- **多模型编排** —— 可为不同任务生成使用不同模型的子 Agent。DeepSeek 驱动的 `general-purpose` 子 Agent 可与 xAI 模型作为协调器协同工作。
- **完整工具集** —— 文件读写编辑、Shell 命令、后台任务、网页搜索、MCP 工具、Skills 等全部可用，不限模型后端。
- **会话中切换模型** —— 在不丢失上下文的情况下切换模型；切换到较小上下文窗口时 TUI 会自动重新压缩。
- **BYOK 支持** —— 通过 `api_key`、`env_key` 或 `extra_headers` 为每个模型配置自有 API Key，适用于需要自定义请求头认证的供应商。

### 配置参考

| 字段 | 说明 | 必填 |
|-------|------|------|
| `model` | 发送给 API 的模型 ID | 是 |
| `base_url` | API 端点基础 URL | 是 |
| `api_backend` | `"chat_completions"`（OpenAI 兼容）、`"messages"`（Anthropic 兼容）、`"responses"`（xAI） | 否（默认：`chat_completions`） |
| `context_window` | 上下文窗口总 token 数 | 是 |
| `api_key` | 硬编码的 API Key（推荐使用 `env_key` 以保障安全） | 否 |
| `env_key` | 存放 API Key 的环境变量名 | 否 |
| `provider_alias` | 用于 `/m:<alias>` 切换的短别名（如 `"d"`） | 否 |
| `provider_name` | TUI 中显示的供应商名称（如 `"DeepSeek"`） | 否 |
| `reasoning_effort` | 推理强度：`"low"`、`"medium"`、`"high"`、`"max"` | 否 |
| `supports_reasoning_effort` | 启用推理强度 UI | 否 |
| `extra_headers` | 额外 HTTP 请求头（如自定义认证） | 否 |
