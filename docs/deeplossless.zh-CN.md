# DeepLossless — DeepSeek 推理感知执行运行时

DeepLossless 是一个**推理感知的编码运行时**，用于减少 AI 长时间编码会话中的重复工作。它作为 HTTPS 代理位于你的编码 Agent 和 DeepSeek API 之间，提供：

- **工具缓存拦截** — 重复的 grep/搜索调用直接返回缓存结果，无需 API 往返
- **DAG 上下文组装与压缩** — 关键细节在数百轮对话中持续保留；3383+ 叶子节点自动压缩适配上下文窗口
- **失败记忆** — 记录已知的错误修复方案，避免重复尝试
- **文件声明/冲突检测** — 并行 Agent 协调文件访问
- **执行回放** — 仅追加的事件日志支持确定性回放和审计追踪
- **跨会话搜索** — 从历史对话中搜索 DAG 摘要和片段

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
# 监听 https://127.0.0.1:8080（HTTPS，自动生成证书）
# HTTP 备用：http://127.0.0.1:8081（适用于沙箱 Agent）
```

TLS 证书首次运行时自动生成。执行 `deeplossless trust` 可将自签名证书安装为系统信任。

可选参数：

| 参数 | 默认值 | 用途 |
|------|--------|------|
| `--port` | `8080` | HTTPS 监听端口 |
| `--http-port` | `8081` | 纯 HTTP 端口（0 = 禁用） |
| `--upstream` | `https://api.deepseek.com` | API 基础 URL |
| `--db-path` | `~/.deeplossless/lcm.db` | SQLite 数据库 |
| `--api-key` | （环境变量） | DeepSeek API 密钥 |
| `--admin-key` | （无） | LCM 端点独立管理密钥 |
| `--runtime-profile` | `autonomous` | 缓存/重试/上下文策略 |
| `--dag-threshold` | `0.80` | 压缩触发器（上下文窗口比例） |
| `--summarizer-budget` | `1000` | 每会话最大 LLM 摘要调用次数 |
| `--lcm-context` | （关闭） | 启用 DAG 上下文注入到系统消息 |
| `--tls-cert` / `--tls-key` | （自动） | 自定义 TLS 证书 |

### 2. 连接你的 Agent

将任何 OpenAI 兼容客户端指向 `https://127.0.0.1:8080/v1`。
无需 API 密钥 — deeplossless 自动为 localhost 注入服务器端密钥。

**Codex**（Responses API）：
```toml
# ~/.codex/config.toml
[model_providers.localproxy]
name = "deeplossless"
base_url = "https://127.0.0.1:8080/v1"
wire_api = "responses"
env_key = "DEEPSEEK_API_KEY"
```

**OpenCode**（Chat Completions）：
```json
{
  "provider": {
    "deeplossless": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "https://127.0.0.1:8080/v1" }
    }
  }
}
```

**OpenClaw**（沙箱，Responses API）：
```json
{
  "api_key": "dummy",
  "base_url": "http://127.0.0.1:8081/v1",
  "wire_api": "responses"
}
```
沙箱 Agent 使用 HTTP 端口 8081 — 它们无法访问主机环境变量或信任自签名证书。

**Claude Code**（通过 SKILL.md）：
```bash
cp SKILL.md .claude/skills/deeplossless.md
```

## 模型名称

DeepLossless 使用 DeepSeek 当前模型：

| Agent 请求 | 路由到 |
|-----------|--------|
| `deepseek-v4-pro` | `deepseek-v4-pro`（1M 上下文） |
| `deepseek-v4-flash` | `deepseek-v4-flash`（1M 上下文） |

均支持 1M token 上下文窗口。DAG 组装和自动压缩确保关键上下文在原始对话历史超出上下文窗口时仍然保留。

## LCM 端点（无损上下文管理）

所有端点仅限 localhost（无需认证）：

| 端点 | 用途 |
|------|------|
| `GET /v1/lcm/current` | 获取会话 ID |
| `GET /v1/lcm/grep/{id}?query=&limit=20` | 搜索当前会话历史 |
| `GET /v1/lcm/global/search?q=&limit=10` | 跨会话搜索，含摘要 |
| `GET /v1/lcm/cache?tool=&args=` | 执行前检查工具缓存 |
| `POST /v1/lcm/cache/put` | 存储工具结果 |
| `DELETE /v1/lcm/cache?tool=&args=` | 删除缓存结果 |
| `POST /v1/lcm/failure` | 记录失败的修复 |
| `POST /v1/lcm/plan` | 存储执行计划 |
| `GET /v1/lcm/plan/{id}` | 获取活跃计划 |
| `DELETE /v1/lcm/plan?id=` | 删除计划 |
| `POST /v1/lcm/file/claim` | 编辑前声明文件 |
| `POST /v1/lcm/file/release` | 释放文件声明 |
| `GET /v1/lcm/execution/search?q=` | 搜索执行记忆 |
| `GET /v1/lcm/runtime/stats` | 缓存命中、token、失败次数 |
| `GET /v1/lcm/health/{id}` | DAG 完整性检查 |

## 验证

### 步骤 1 — 冒烟测试（无需 API 密钥）

```bash
deeplossless demo
```

### 步骤 2 — 使用 API 密钥启动

```bash
export DEEPSEEK_API_KEY=sk-...
deeplossless

# 预期输出：
# deeplossless v0.6.0 listening on 127.0.0.1:8080
# HTTPS on 127.0.0.1:8080
# HTTP on 127.0.0.1:8081 (for sandboxed local agents)
# upstream: https://api.deepseek.com
```

### 步骤 3 — 非流式对话

```bash
curl -sk https://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"用一个词打招呼"}]}' \
  | jq '.choices[0].message.content'
```

### 步骤 4 — 流式对话

```bash
curl -skN https://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"数到 3"}],"stream":true}'
```

### 步骤 5 — 运行时统计

```bash
curl -sk https://127.0.0.1:8080/v1/lcm/runtime/stats | jq .
```

### 步骤 6 — 搜索历史上下文

```bash
# 获取会话 ID
curl -sk https://127.0.0.1:8080/v1/lcm/current

# 搜索
curl -sk "https://127.0.0.1:8080/v1/lcm/grep/1?query=搜索词&limit=10"
```

### 故障排除

启动时报 `address already in use`，更换端口：
```bash
deeplossless --port 8443 --http-port 8082
```

对话请求报错，检查：
1. API 密钥有 DeepSeek V4 模型访问权限
2. `curl -sk https://127.0.0.1:8080/health` 返回 `{"status":"healthy"}`
3. 启用 `--log-dir /tmp/logs` 查看请求诊断信息

沙箱 Agent TLS 错误，使用 HTTP 端口：
```bash
# Agent 配置：base_url = http://127.0.0.1:8081/v1
```

## 定价

当前定价请参见 [DeepSeek API 文档](https://api-docs.deepseek.com/quick_start/pricing)。DeepLossless 不增加额外 API 成本。

运行时可通过以下方式减少 token 消耗：
- 拦截重复工具调用（缓存命中避免重复执行）
- 自动压缩对话历史（DAG 上下文替代原始历史）
- 记录失败模式（减少已知错误修复的重试次数）

监控节省：
```bash
curl -sk https://127.0.0.1:8080/v1/lcm/runtime/stats | jq .
```

## 更多

- [README](https://github.com/gordonlu/deeplossless) — 完整文档
- [Agent 集成指南](https://github.com/gordonlu/deeplossless/blob/master/agent_integration.md)
- [SKILL.md](https://github.com/gordonlu/deeplossless/blob/master/SKILL.md) — Agent 可安装的技能文件
