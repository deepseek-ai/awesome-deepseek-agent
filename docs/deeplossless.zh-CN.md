# DeepLossless — DeepSeek 推理感知执行运行时

DeepLossless 是一个**推理感知的编码运行时**，用于减少 AI 长时间编码会话中的重复工作。它作为 OpenAI 兼容的代理服务器，位于你的编码 Agent 和 DeepSeek API 之间，提供：

- **工具缓存拦截** — 重复的 grep/搜索调用直接返回缓存结果，无需 API 往返
- **DAG 上下文组装** — 关键细节在数百轮对话中持续保留，即使聊天窗口溢出
- **失败记忆** — 记录已知的错误修复方案，避免重复尝试
- **执行回放** — 仅追加的事件日志支持确定性回放和审计追踪

DeepSeek V4 Pro 和 V4 Flash（均支持 1M 上下文）让长编码会话在经济上可行。DeepLossless 在此基础上增加了执行记忆。

## 安装

```bash
cargo install deeplossless
```

要求：Rust 1.85+，SQLite（内置）。

## 配置

### 1. 启动代理

```bash
export DEEPSEEK_API_KEY=sk-...
deeplossless
# 监听 http://127.0.0.1:8080
```

可选参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--port` | `8080` | 监听端口 |
| `--upstream` | `https://api.deepseek.com` | API 基础 URL |
| `--db-path` | `~/.deeplossless/lcm.db` | SQLite 数据库路径 |
| `--log-dir` | (禁用) | 每请求 JSON 指标日志 |
| `--runtime-profile` | `autonomous` | 缓存/重试/上下文策略 |

### 2. 连接你的 Agent

将任意 OpenAI 兼容客户端指向 `http://127.0.0.1:8080/v1`。

**Codex**（Responses API）：
```toml
# ~/.codex/config.toml
[model_providers.localproxy]
name = "deeplossless"
base_url = "http://127.0.0.1:8080/v1"
wire_api = "responses"
env_key = "DEEPSEEK_API_KEY"
```

**OpenCode**（Chat Completions API）：
```json
{
  "provider": {
    "deeplossless": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://127.0.0.1:8080/v1" }
    }
  }
}
```

**任意 OpenAI 兼容客户端**：
```bash
export OPENAI_BASE_URL=http://127.0.0.1:8080/v1
export OPENAI_API_KEY=sk-...
```

## 模型名称

DeepLossless 使用 DeepSeek 当前模型，并自动映射第三方名称：

| Agent 请求 | 实际路由到 |
|-----------|-----------|
| `deepseek-v4-pro` | `deepseek-v4-pro`（1M 上下文） |
| `deepseek-v4-flash` | `deepseek-v4-flash` |
| `gpt-5`、`gpt-5.5`、`o3` | `deepseek-v4-pro` |
| `gpt-*-mini` | `deepseek-v4-flash` |

DeepSeek V4 Pro 和 V4 Flash 均支持 1M token 上下文窗口。运行时的 DAG 组装确保即使原始对话历史超出上下文窗口，重要上下文也不会丢失。

## 验证

### 第 1 步 — 冒烟测试（无需 API key）

```bash
deeplossless demo
```

运行本地冒烟测试以验证二进制文件安装正确。不需要 API key 或网络访问。

### 第 2 步 — 使用 API key 启动

```bash
export DEEPSEEK_API_KEY=sk-...
deeplossless

# 预期输出：
# deeplossless listening on 127.0.0.1:8080
# upstream: https://api.deepseek.com
```

### 第 3 步 — 非流式对话

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"用一个词打招呼"}]}' \
  | jq '.choices[0].message.content'
```

应返回简单的问候语。

### 第 4 步 — 流式对话

```bash
curl -sN http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"数到3"}],"stream":true}'
```

应输出 SSE 数据块（`data: {...}`），以 `data: [DONE]` 结束。

### 第 5 步 — Responses API（Codex 路径）

```bash
curl -sN http://127.0.0.1:8080/v1/responses \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"input":"Say hi","model":"deepseek-v4-flash"}' \
  | head -20
```

应输出 Responses API SSE 事件（`event: response.created` 等）。

### 第 6 步 — 运行时统计

```bash
curl -s http://127.0.0.1:8080/v1/lcm/runtime/stats \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  | jq .
```

显示缓存命中/未命中、token 数量、运行时策略。

### 故障排除

如果第 2 步失败，报 `address already in use`，更换端口：

```bash
deeplossless --port 8081
```

如果第 3-5 步返回错误，请检查：

1. API key 是否有 DeepSeek V4 模型的访问权限
2. 代理日志是否显示 `upstream response received status=200`
3. 使用 `--log-dir /tmp/logs` 启用每请求诊断日志

## 价格

参见 [DeepSeek API 文档](https://api-docs.deepseek.com/quick_start/pricing) 获取最新价格。DeepLossless 不会产生额外的 API 费用——它在本地运行，仅将请求转发到你的 DeepSeek 账户。

运行时可以通过以下方式减少 token 消耗：
- 拦截重复的工具调用（缓存命中避免重新执行）
- 注入 DAG 上下文（减少对未变更文件的重复读取）
- 记录失败模式（减少对已知错误方案的重复尝试）

监控节省情况：
```bash
curl http://127.0.0.1:8080/v1/lcm/runtime/stats | jq .
```

## 更多信息

- [README](https://github.com/gordonlu/deeplossless) — 完整文档
- [Agent 集成指南](https://github.com/gordonlu/deeplossless/blob/master/agent_integration.md)
- [贡献指南](https://github.com/gordonlu/deeplossless/blob/master/CONTRIBUTING.md)
