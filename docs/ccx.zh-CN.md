[English](./ccx.md) | [简体中文](./ccx.zh-CN.md) · [← Back](../README.zh-CN.md)

# 通过 CCX 接入 Codex CLI / Codex App

[CCX](https://github.com/BenedictKing/ccx) 是一个高性能的 AI API 代理与协议转换网关。它通过本地 `/v1/messages` 透传和 `/v1/responses` → `/v1/chat/completions` 协议转换，使 Codex CLI 和 Codex App 能够使用 DeepSeek 模型 — 弥合了 Codex 的 Responses API 与 DeepSeek 的 Chat Completions API 之间的鸿沟。

## 工作原理

Codex CLI 和 Codex App 原生使用 OpenAI Responses API（`/v1/responses`），而 DeepSeek 提供的是 Chat Completions API（`/v1/chat/completions`）。CCX 位于两者之间：

- 将 `/v1/messages` 请求直接转发至上游（兼容 Claude 协议透传）
- 将 `/v1/responses` 请求转换为 `/v1/chat/completions` 请求，使 DeepSeek 模型成为 Codex 可用的模型

```text
Codex CLI / Codex App  →  CCX (:3000)  →  DeepSeek API
     /v1/responses           /v1/chat/completions
```

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

| 字段             | 值                                            |
| ---------------- | --------------------------------------------- |
| **类型**         | OpenAI Chat                                   |
| **名称**         | DeepSeek                                      |
| **Base URL**     | `https://api.deepseek.com/v1/chat/completions` |
| **API Key**      | `<你的 DeepSeek API Key>`                      |
| **Models**       | `deepseek-v4-pro`, `deepseek-v4-flash`         |

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

启用渠道并设置优先级后，渠道即可开始处理请求。

#### 3. 配置 Codex CLI

在终端中设置以下环境变量：

```bash
export OPENAI_API_KEY="your-strong-proxy-key"
export OPENAI_BASE_URL="http://localhost:3000/v1"
```

运行 Codex CLI，它会将 CCX 作为 API 端点，CCX 会将 `/v1/responses` 请求路由至 DeepSeek 渠道。

验证模型可用：

```bash
codex --model deepseek-v4-pro "你好"
```

#### 4. 配置 Codex App（VS Code / JetBrains）

在 Codex 扩展的设置中配置：

| 设置项            | 值                            |
| ----------------- | ----------------------------- |
| **API Key**       | `your-strong-proxy-key`       |
| **Base URL**      | `http://localhost:3000/v1`    |
| **Model**         | `deepseek-v4-pro`             |

保存后，Codex App 会将 Responses API 请求发送至 CCX，CCX 自动翻译为 DeepSeek 兼容的 Chat Completions 调用。

#### 5. 可选：验证配置

直接测试接口：

```bash
curl http://localhost:3000/v1/models \
  -H "Authorization: Bearer your-strong-proxy-key"
```

如果返回的模型列表中包含 `deepseek-v4-pro` 和 `deepseek-v4-flash`，说明配置成功。

#### 故障排查

- `401 Unauthorized`：确认 CCX 的 `PROXY_ACCESS_KEY` 与 Codex CLI/App 中设置的 Key 一致。
- `Model not found`：确认 CCX 渠道中的模型名称完全匹配 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- `Connection refused`：确认 CCX 正在 3000 端口运行，且 `OPENAI_BASE_URL` 指向正确的地址。
- 渠道显示 unhealthy：在 CCX 管理面板中检查 DeepSeek API Key 是否正确，以及网络是否能访问 `api.deepseek.com`。
