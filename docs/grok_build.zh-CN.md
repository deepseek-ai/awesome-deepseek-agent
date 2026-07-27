[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Grok Build

[Grok Build](https://grok.com/cli) 是 xAI（SpaceXAI）推出的终端 AI 编程助手。它提供功能完善的 TUI 界面，支持流式响应、MCP 服务器、Skills 技能系统、子代理，以及自定义模型接入。Grok Build 同时支持 Anthropic 兼容（`messages`）和 OpenAI 兼容（`chat_completions`）两种 API 后端。

### 安装 Grok Build

安装最新稳定版：

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

安装指定版本：

```bash
curl -fsSL https://x.ai/cli/install.sh | bash -s 0.2.112
```

验证安装：

```bash
grok --version
```

### 配置 Grok Build

Grok Build 的配置文件为 `~/.grok/config.toml`。在其中添加 `[model.<模型名称>]` 段即可定义由 DeepSeek 驱动的自定义模型。

Grok Build 支持两种 API 后端，可按需选择：

#### 方法一：Anthropic Messages API（推荐）

使用 DeepSeek 的 [Anthropic 兼容 API](https://api-docs.deepseek.com/guides/anthropic_api)。在 `~/.grok/config.toml` 中添加：

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Pro"
description = "DeepSeek V4 Pro via Anthropic API"
api_backend = "messages"
context_window = 1000000
api_key = "<你的 DeepSeek API Key>"
extra_headers = { "anthropic-version" = "2023-06-01" }
```

> **重要：** `api_key` 字段必须填写。若不设置，Grok Build 会将 xAI 的登录凭证发送给 DeepSeek，导致 401 认证失败。设置 `api_key` 后，Grok Build 会将其识别为第三方（BYOK）模型，并仅使用该密钥。

#### 方法二：OpenAI Chat Completions API

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Pro"
description = "DeepSeek V4 Pro via OpenAI-compatible API"
context_window = 1000000
api_key = "<你的 DeepSeek API Key>"
```

`api_backend` 默认为 `"chat_completions"`，因而无需显式指定。

#### 启用最大推理强度

在 `[models]` 段中添加以下内容，为所有模型启用最大推理强度（对 `deepseek-v4-pro` 生效）：

```toml
[models]
default = "deepseek-v4-pro"
default_reasoning_effort = "high"
```

#### 使用环境变量存储 API Key

为了更安全，可将密钥存入环境变量：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

然后将配置中的 `api_key` 替换为 `env_key`：

```toml
[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Pro"
api_backend = "messages"
context_window = 1000000
env_key = "DEEPSEEK_API_KEY"
extra_headers = { "anthropic-version" = "2023-06-01" }
```

#### 使用 Flash 模型

对于轻量任务，可将 `deepseek-v4-flash` 作为辅助模型：

```toml
[model.deepseek-v4-flash]
model = "deepseek-v4-flash"
base_url = "https://api.deepseek.com/anthropic/v1"
name = "DeepSeek V4 Flash"
api_backend = "messages"
context_window = 1000000
env_key = "DEEPSEEK_API_KEY"
extra_headers = { "anthropic-version" = "2023-06-01" }
```

### 使用 Grok Build

进入项目目录后启动 Grok Build：

```bash
cd /path/to/my-project
grok
```

#### 切换模型

在 TUI 中，使用以下命令切换到 DeepSeek：

```
/model deepseek-v4-pro
```

也可以使用模型选择器：在消息区按下 `Ctrl+M` 打开全部可用模型列表，一键切换。

#### 将 DeepSeek 设为默认模型

在 `~/.grok/config.toml` 中设置默认模型，每次启动都用 DeepSeek：

```toml
[models]
default = "deepseek-v4-pro"
```

#### 无头模式

适用于脚本和 CI/CD 环境：

```bash
grok -p "解释一下 Go 协程的原理" -m deepseek-v4-pro
```

### 常见问题

#### 401 "Auth recovery succeeded but inference request was still rejected"

这是因为 Grok Build 将 xAI 的登录凭证发送给了 DeepSeek，而非你的 API Key。解决方法：在 `[model.deepseek-v4-pro]` 配置中加上 `api_key` 或 `env_key`。Grok Build 仅在明确设置 `api_key`/`env_key` 后，才会对第三方端点使用该密钥，而非 session token。

#### 连接错误

验证端点是否可达：

```bash
curl -s https://api.deepseek.com/anthropic/v1/messages \
  -H "x-api-key: <你的 DeepSeek API Key>" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"deepseek-v4-pro","max_tokens":16,"messages":[{"role":"user","content":"hi"}]}'
```

#### 调试日志

```bash
GROK_LOG_FILE=/tmp/grok.log RUST_LOG=debug grok
tail -f /tmp/grok.log
```
