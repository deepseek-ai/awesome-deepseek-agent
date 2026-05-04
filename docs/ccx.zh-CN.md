[English](./ccx.md) | [简体中文](./ccx.zh-CN.md) · [← Back](../README.zh-CN.md)

# 通过 CCX 接入 DeepSeek — Claude Code CLI & Codex CLI/App

[CCX](https://github.com/BenedictKing/ccx) 是一个高性能的 AI API 代理与协议转换网关。通过统一的本地端点，让多种工具都能使用 DeepSeek 模型：

| 端点                 | 协议                                        | 目标工具              |
| -------------------- | ------------------------------------------- | --------------------- |
| `/v1/messages`       | Claude Messages API 透传                    | **Claude Code CLI**   |
| `/v1/responses`      | Responses → Chat Completions 协议转换       | **Codex CLI / App**   |
| `/v1/chat/completions` | OpenAI Chat Completions 透传              | 任何 OpenAI 兼容工具   |

一个 CCX 实例同时服务三条路径 — 只需添加一个 DeepSeek 渠道，所有使用上述协议的工即可直接使用。

## 工作原理

```text
Claude Code CLI ──→  /v1/messages ──→  CCX (:3000)  ──→  DeepSeek API
Codex CLI/App  ──→  /v1/responses ──→  CCX (:3000)  ──→  DeepSeek API
                                            │
                          /v1/chat/completions (透传)
```

CCX 在内部处理协议差异：Claude Messages 请求被转换为 Chat Completions 再发往上游 DeepSeek 渠道，Responses 请求同样映射为 Chat Completions。工具侧看到的是原生端点，DeepSeek 收到的则是标准的 Chat Completions 调用。

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

在浏览器中打开 CCX 管理面板 `http://localhost:3000`，进入 **渠道管理**，添加新渠道：

| 字段             | 值                                              |
| ---------------- | ----------------------------------------------- |
| **类型**         | OpenAI Chat                                     |
| **名称**         | DeepSeek                                        |
| **Base URL**     | `https://api.deepseek.com/v1/chat/completions`  |
| **API Key**      | `<你的 DeepSeek API Key>`                        |
| **Models**       | `deepseek-v4-pro`, `deepseek-v4-flash`           |

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

Codex CLI/App 默认使用 `gpt-5` / `mini` 作为模型名，**必须**配置模型重定向。Claude Code CLI 使用 `opus` / `sonnet` / `haiku`，重定向为推荐（也可直接 `--model deepseek-v4-pro`）：

| 请求模型       | 重定向到              | 适用工具           |
| -------------- | --------------------- | ------------------ |
| `gpt-5`        | `deepseek-v4-pro`     | Codex CLI/App      |
| `mini`         | `deepseek-v4-flash`   | Codex CLI/App      |
| `opus`         | `deepseek-v4-pro`     | Claude Code CLI（推荐）|
| `sonnet`       | `deepseek-v4-pro`     | Claude Code CLI（推荐）|
| `haiku`        | `deepseek-v4-pro`     | Claude Code CLI（推荐）|

在 CCX 渠道设置中填写 Model Mapping（模型映射）即可完成重定向。

#### 3. 场景 A：Claude Code CLI

Claude Code CLI 使用 Messages API。配置一个类型为 **Claude Code** 的渠道，填入 DeepSeek Base URL 和 Key，并设置模型映射。渠道管理界面会显示请求量、平均延迟和成功率等使用统计：

![Claude Messages 渠道使用统计](../assets/ccx/messages-channel-config.png)

将 Claude Code CLI 指向 CCX 的 `/v1/messages` 端点：

```bash
export ANTHROPIC_API_KEY="your-strong-proxy-key"
export ANTHROPIC_BASE_URL="http://localhost:3000/v1/messages"
```

验证：

```bash
claude --model deepseek-v4-pro "你好"
```

Claude Code CLI 发送 `/v1/messages` 请求，CCX 将其转换并路由至 DeepSeek 渠道。

#### 4. 场景 B：Codex CLI

Codex CLI 使用 OpenAI Responses API。配置一个类型为 **DeepSeek** 的渠道（OpenAI Chat），填入 DeepSeek Base URL、Key 和模型映射。渠道管理界面会显示请求量、平均延迟和成功率等使用统计：

![DeepSeek Chat 渠道使用统计](../assets/ccx/chat-channel-config.png)

将 Codex CLI 指向 CCX 的 `/v1` 基础路径：

```bash
export OPENAI_API_KEY="your-strong-proxy-key"
export OPENAI_BASE_URL="http://localhost:3000/v1"
```

验证：

```bash
codex "你好"
```

Codex CLI 默认使用 `gpt-5` 作为模型名，CCX 根据渠道的模型重定向规则将其映射为 `deepseek-v4-pro` 发往 DeepSeek。也可显式指定模型：`codex --model deepseek-v4-pro "你好"`。

#### 5. 场景 C：Codex App（VS Code / JetBrains）

在 Codex 扩展的设置中配置：

| 设置项            | 值                            |
| ----------------- | ----------------------------- |
| **API Key**       | `your-strong-proxy-key`       |
| **Base URL**      | `http://localhost:3000/v1`    |
| **Model**         | `gpt-5`（CCX 自动重定向到 `deepseek-v4-pro`） |

保存后，Codex App 发送的 Responses API 请求中默认模型为 `gpt-5`，CCX 根据渠道重定向规则自动映射为 `deepseek-v4-pro`，并翻译为 Chat Completions 调用发往 DeepSeek。

#### 6. 可选：查看请求日志

CCX 内置日志监控，可实时查看每个请求的模型路由、延迟和响应状态：

![请求日志监控](../assets/ccx/log-monitoring.png)

#### 7. 可选：验证模型列表

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
- Claude Code 报错响应格式异常：确认 `ANTHROPIC_BASE_URL` 以 `/v1/messages` 结尾（而非仅 `/v1`）。
