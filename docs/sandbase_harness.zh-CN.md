# 在 DeepSeek Harness 中使用 SandBase Harness

本指南通过 MCP 将 DeepSeek Harness 连接到本地 SandBase Harness 运行时。SandBase 负责持久会话、工具治理、审批、凭据、审计和回放；它不是托管模型服务，DeepSeek 模型仍由 DeepSeek Harness 配置。

## 前置条件

- Node.js 22+ 和 npm 10+
- 支持 stdio MCP 的 DeepSeek Harness
- DeepSeek API key，或 DeepSeek Harness 支持的其他供应商
- 使用已发布 bridge 镜像时需要 Docker

请使用当前 DeepSeek V4 名称 `deepseek-v4-pro` 或 `deepseek-v4-flash`，不要使用已弃用的 V3 模型名称。DeepSeek V4 支持最高 100 万 token 上下文。当 DeepSeek Harness 暴露这些控制项时，按其文档启用 1M 上下文和最大思考/推理级别；本文不虚构供应商配置字段。

## 1. 安装并启动 SandBase Harness

```bash
git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness
npm ci
npm run build:runtime
mkdir ../sandbase-workspace && cd ../sandbase-workspace
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
```

默认 local provider 使用操作系统用户运行。需要更强隔离时，请按照[部署指南](https://github.com/sandbaseai/sandbase-harness/blob/main/docs/deployment.md)配置 Docker 或 Kubernetes；隔离和资源边界取决于后端及部署配置。

## 2. 配置 MCP 和模型

从旁边的 workspace 将源码目录安装到 DeepSeek Harness Web profile：

```bash
export MANAGED_AGENTS_URL=http://127.0.0.1:3000
# 只有运行时启用认证时才设置 MANAGED_AGENTS_API_KEY。
cd ../sandbase-workspace
dsh plugin --profile web add -w ../sandbase-harness
dsh web
```

在 DeepSeek Harness 自身的供应商设置中选择 `deepseek-v4-pro`（最高推理）或 `deepseek-v4-flash`（较低延迟），并按其当前文档配置 endpoint、key、上下文窗口和思考控制。SandBase 是 MCP/运行时层，不替代模型配置。

bridge 只连接 `MANAGED_AGENTS_URL`。不要把 API key 写入提交文件或截图；使用源码目录也可避免与另一个无 scope 的 npm `managed-agents` 包混淆。

## 3. 首次运行

在 DeepSeek Harness Web 会话中，让它列出 Agent、创建会话、运行一个简短任务、查看结果并列出 artifact。bridge 工具包括 `list_agents`、`create_session`、`run_session`、`get_session`、`list_artifacts` 和 `stop_session`。

排查 MCP 前先验证运行时：

```bash
curl --fail --silent --show-error "$MANAGED_AGENTS_URL/v1/x/health"
curl --fail --silent --show-error "$MANAGED_AGENTS_URL/v1/agents"
```

如果第二个请求需要认证，请使用运行时接受的 bearer key 重试。health 成功不代表 MCP 已获得 agents API 权限。

## 故障排查与边界

- `MCP startup failed`：执行 `npm run build:runtime`，确认 `dist/mcp/index.js` 存在。
- `fetch failed`：启动运行时并检查 `MANAGED_AGENTS_URL`。
- `401` 或 `403`：仅在运行时要求时设置 `MANAGED_AGENTS_API_KEY`。
- 没有 SandBase 工具：确认 Web profile 安装了旁边的源码目录，并检查 DSH 启动日志。

会话数据和 artifact 保存在配置的 SandBase workspace。local process、Docker、Kubernetes 和 worker 后端不提供相同隔离能力；运行不受信任任务前请评估所选后端和部署配置。本文不构成安全认证。

## 来源

- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness)
- [v0.3.8 release](https://github.com/sandbaseai/sandbase-harness/releases/tag/v0.3.8)
- [安装与 MCP 配置](https://github.com/sandbaseai/sandbase-harness/blob/main/llms-install.md)
- [DeepSeek Harness 集成示例](https://github.com/sandbaseai/sandbase-harness/tree/main/examples/deepseek-harness)
- [DeepSeek API 文档](https://api-docs.deepseek.com/)
