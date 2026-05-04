[English](./ccx.md) | [简体中文](./ccx.zh-CN.md) · [← Back](../README.zh-CN.md)

# 通过 CCX 接入 DeepSeek — Claude Code CLI & Codex CLI/App

[CCX](https://github.com/BenedictKing/ccx) 是一个高性能的 AI API 代理与协议转换网关。通过统一的本地端点，让多种工具都能使用 DeepSeek 模型：

| 端点                   | 协议                                     | 目标工具                |
| ---------------------- | ---------------------------------------- | ----------------------- |
| `/v1/messages`         | Claude Messages API 路由                 | **Claude Code CLI**     |
| `/v1/responses`        | Responses → Chat Completions 协议转换    | **Codex CLI / App**     |
| `/v1/chat/completions` | OpenAI Chat Completions 透传             | 任何 OpenAI 兼容工具    |

一个 CCX 实例可以同时服务三条路径。按需配置对应协议的 DeepSeek 渠道后，所有兼容工具都可以使用同一个本地网关。

## 工作原理

```text
Claude Code CLI       ──→  /v1/messages          ──→  CCX (:3000)  ──→  DeepSeek Anthropic 端点
Codex CLI/App         ──→  /v1/responses         ──→  CCX (:3000)  ──→  DeepSeek Chat 端点
OpenAI-compatible app ──→  /v1/chat/completions  ──→  CCX (:3000)  ──→  DeepSeek Chat 端点
```

CCX 在内部处理协议差异：Claude Messages 请求可以路由到 DeepSeek 的 Anthropic 兼容端点，Responses 请求会映射为 Chat Completions。工具侧看到的是原生端点，上游 DeepSeek 渠道收到的是它期望的协议。

#### 1. 部署 CCX

从 [CCX Releases](https://github.com/BenedictKing/ccx/releases/latest) 下载最新二进制文件，并在同目录创建 `.env` 文件：

```bash
PROXY_ACCESS_KEY=your-strong-proxy-key
PORT=3000
ENABLE_WEB_UI=true
APP_UI_LANGUAGE=zh-CN
```

运行二进制文件后，访问 `http://localhost:3000` 进入管理面板。

也可以使用 Docker 部署：

```bash
docker run -d --name ccx \
  -p 3000:3000 \
  -v ./ccx-data:/app/data \
  -e PROXY_ACCESS_KEY="your-strong-proxy-key" \
  -e ENABLE_WEB_UI=true \
  benedictking/ccx:latest
```

#### 2. 配置 DeepSeek 渠道

##### 2.1 Codex CLI/App：Responses 渠道

为 Codex CLI/App 打开 Responses 渠道页，例如 `http://localhost:3000/channels/responses`（如果你的 CCX 使用其他端口，如 `3688`，请替换端口），添加一个 Chat service type。这里的 Base URL 是写入 CCX 的 DeepSeek 上游地址，不是 Codex 客户端连接 CCX 的本地地址：

| 字段                    | 值                                             |
| ----------------------- | ---------------------------------------------- |
| **Service type**        | Chat                                           |
| **名称**                | DeepSeek Chat                                  |
| **Base URL (OpenAI)**   | `https://api.deepseek.com/`                    |
| **API Key**             | `<你的 DeepSeek API Key>`                      |
| **Models**              | `deepseek-v4-pro`, `deepseek-v4-flash`         |

Codex CLI/App 默认使用 `gpt-5` / `mini` 作为模型名，**必须**配置模型重定向：

| 请求模型 | 重定向到              |
| -------- | --------------------- |
| `gpt-5`  | `deepseek-v4-pro`     |
| `mini`   | `deepseek-v4-flash`   |

为 Responses Chat service 配置 Model Mapping：

![Responses Chat service 模型重定向](../assets/ccx/codex-responses-redirect.png)

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

##### 2.2 Claude Code CLI：Messages 渠道

为 Claude Code CLI 打开 Messages 渠道页，例如 `http://localhost:3000/channels/messages`（如果你的 CCX 使用其他端口，如 `3688`，请替换端口），添加一个 Claude service type，并指向 DeepSeek 的 Anthropic 兼容端点：

| 字段                    | 值                                             |
| ----------------------- | ---------------------------------------------- |
| **Service type**        | Claude                                         |
| **名称**                | DeepSeek Claude                                |
| **Base URL (Anthropic)** | `https://api.deepseek.com/anthropic`          |
| **API Key**             | `<你的 DeepSeek API Key>`                      |
| **Models**              | `deepseek-v4-pro`, `deepseek-v4-flash`         |

Claude Code CLI 默认使用 Opus 4.7，也可通过 `opus` / `sonnet` / `haiku` 等别名做模型重定向：

| 请求模型 | 重定向到              |
| -------- | --------------------- |
| `opus`   | `deepseek-v4-pro`     |
| `sonnet` | `deepseek-v4-pro`     |
| `haiku`  | `deepseek-v4-flash`   |

为 Messages Claude service 配置 Model Mapping：

![Claude Code 渠道模型重定向](../assets/ccx/channel-test-success-alt.png)

#### 3. 场景 A：Claude Code CLI

Claude Code CLI 使用 Messages API。使用上面配置的 Claude 渠道，填入 Anthropic 兼容的 DeepSeek Base URL、Key 和模型映射。

将 Claude Code CLI 指向本地 CCX 网关根地址：

```bash
export ANTHROPIC_API_KEY="your-strong-proxy-key"
export ANTHROPIC_BASE_URL="http://localhost:3000"
```

验证：

```bash
claude "你好"
```

Claude Code CLI 使用默认 Opus 4.7 发送 `/v1/messages` 请求，CCX 根据模型重定向规则映射模型，完成协议转换后路由至 DeepSeek 渠道。

Claude Code 渠道面板会显示 Messages 请求流量和 token 指标：

![Claude Code 渠道使用统计](../assets/ccx/redirect-editing-chat.png)

Messages 请求日志可查看协议类型、模型重定向和响应耗时：

![Messages 请求日志](../assets/ccx/messages-channel-config.png)

#### 4. 场景 B：Codex CLI

Codex CLI 使用 OpenAI Responses API。使用上面在 Responses 渠道页配置的 Chat service type，填入 OpenAI 兼容的 DeepSeek Base URL、Key 和模型映射。

将 Codex CLI 指向本地 CCX 的 `/v1` 基础路径：

```bash
export OPENAI_API_KEY="your-strong-proxy-key"
export OPENAI_BASE_URL="http://localhost:3000/v1"
```

验证：

```bash
codex "你好"
```

Codex CLI 默认使用 `gpt-5` 作为模型名，CCX 根据渠道的模型重定向规则将其映射为 `deepseek-v4-pro` 发往 DeepSeek。也可显式指定模型：`codex --model deepseek-v4-pro "你好"`。

Responses 渠道面板会显示请求流量和 token 指标：

![DeepSeek Chat 渠道使用统计](../assets/ccx/chat-channel-config.png)

Responses 请求日志可查看协议类型、模型重定向和响应耗时：

![Responses 请求日志](../assets/ccx/channel-test-success.png)

#### 5. 场景 C：Codex App（VS Code / JetBrains）

在 Codex 扩展的设置中配置：

| 设置项       | 值                                                  |
| ------------ | --------------------------------------------------- |
| **API Key**  | `your-strong-proxy-key`                             |
| **Base URL** | `http://localhost:3000/v1`                          |
| **Model**    | `gpt-5`（CCX 自动重定向到 `deepseek-v4-pro`）       |

保存后，Codex App 发送的 Responses API 请求中默认模型为 `gpt-5`，CCX 根据渠道重定向规则自动映射为 `deepseek-v4-pro`，并翻译为 Chat Completions 调用发往 DeepSeek。

#### 6. 可选：验证模型列表

```bash
curl http://localhost:3000/v1/models \
  -H "Authorization: Bearer your-strong-proxy-key"
```

如果返回的模型列表中包含 `deepseek-v4-pro` 和 `deepseek-v4-flash`，说明渠道状态正常。

#### 故障排查

- `401 Unauthorized`：确认工具中设置的 Key 与 CCX `.env` 中的 `PROXY_ACCESS_KEY` 一致。
- `Model not found`：确认 CCX 渠道中的模型名称完全匹配 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- `Connection refused`：确认 CCX 正在 3000 端口运行，且 Base URL 指向正确的地址。
- 渠道显示 unhealthy：在 CCX 管理面板中检查 DeepSeek API Key 是否正确，以及网络是否能访问 `api.deepseek.com`。
- Claude Code 报错响应格式异常：确认 `ANTHROPIC_BASE_URL` 指向 CCX 网关根地址，而不是 `/v1` 或 `/v1/messages`。
