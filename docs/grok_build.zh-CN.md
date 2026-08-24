[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← Back](../README.md)

# 接入 Grok Build

Grok Build（`grok`）是 xAI 推出的终端 AI 编程 Agent：全屏 TUI，可阅读代码库、编辑文件、执行 Shell 命令、调用 MCP 工具并编排子 Agent。默认使用 xAI 托管的 Grok 模型，同时支持 OpenAI Chat Completions、OpenAI Responses 与 Anthropic Messages 三种协议，因此可以在 `~/.grok/config.toml` 中把 DeepSeek V4 配成自定义模型。

- **文档：** https://docs.x.ai/build/overview
- **安装：** https://x.ai/cli/install.sh（macOS / Linux）· https://x.ai/cli/install.ps1（Windows）

> **Agent / 工具循环推荐后端：** DeepSeek 的 [Anthropic 兼容端点](https://api.deepseek.com/anthropic)。思考模式下，带 `tools` 的后续请求必须回传 `reasoning_content`。Anthropic Messages API 可以避开部分 Chat Completions 客户端会出现的 `400` 错误（`The reasoning_content in the thinking mode must be passed back to the API`）。Grok 的 `messages` 后端对应这一协议。

#### 1. 安装 Grok Build

macOS / Linux / Git Bash：

```shell
curl -fsSL https://x.ai/cli/install.sh | bash
```

Windows（PowerShell）：

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

验证安装：

```shell
grok --version
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key（以 `sk-` 开头）。

Linux / Mac：

```shell
export DEEPSEEK_API_KEY="sk-..."
```

Windows（PowerShell）：

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

#### 3. 在 `config.toml` 中接入 DeepSeek V4

配置文件位置：

- Linux / macOS：`~/.grok/config.toml`
- Windows：`%USERPROFILE%\.grok\config.toml`

若文件不存在，请先创建。

```toml
[models]
default = "deepseek-v4-pro"
default_reasoning_effort = "max"

[model.deepseek-v4-pro]
model = "deepseek-v4-pro[1m]"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Pro"
api_backend = "messages"
context_window = 1000000
env_http_headers = { "x-api-key" = "DEEPSEEK_API_KEY" }
extra_headers = { "anthropic-version" = "2023-06-01" }

[model.deepseek-v4-flash]
model = "deepseek-v4-flash[1m]"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Flash"
api_backend = "messages"
context_window = 1000000
env_http_headers = { "x-api-key" = "DEEPSEEK_API_KEY" }
extra_headers = { "anthropic-version" = "2023-06-01" }
```

- Anthropic 模型名上的 `[1m]` 用于请求 DeepSeek V4 的 100 万 token 上下文。
- `default_reasoning_effort = "max"` 对应 DeepSeek V4 的 `max` 思考强度（官方推荐的编程档位）。`high` 是更低的映射档。
- 把 API Key 放在 `DEEPSEEK_API_KEY` 环境变量中，不要写进 `config.toml`。

#### 4. 首次运行

```shell
cd /path/to/my-project
grok
```

也可以在启动时指定模型：

```shell
grok -m deepseek-v4-pro --effort max
```

用 `grok models` 或 `grok inspect` 确认模型已加载。在 TUI 中：

| 命令 | 作用 |
| --- | --- |
| `/model deepseek-v4-pro` | 切换到 DeepSeek V4 Pro |
| `/model deepseek-v4-flash` | 切换到 DeepSeek V4 Flash |
| `/effort max` | 将当前模型的思考强度设为 `max` |
| `Ctrl+M` | 打开模型选择器（在滚动历史区） |

#### 可选：OpenAI Chat Completions 后端

如果更想走 DeepSeek 的 OpenAI 兼容端点（`https://api.deepseek.com`）：

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Pro"
api_backend = "chat_completions"
context_window = 1000000
env_key = "DEEPSEEK_API_KEY"
```

仅当当前 Grok 版本会在工具调用回合正确回传 `reasoning_content` 时使用。如果出现关于 `reasoning_content` 的 `400` 错误，请改回第 3 步的 Anthropic `messages` 配置。

#### 相关资源

- [Grok Build 自定义模型](https://docs.x.ai/docs/build/overview)
- [DeepSeek 思考模式](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)
- [DeepSeek Anthropic API](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)
