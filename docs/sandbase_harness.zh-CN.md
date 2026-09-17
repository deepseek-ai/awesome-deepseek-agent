[English](./sandbase_harness.md) | [简体中文](./sandbase_harness.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 将 SandBase Harness 接入 DeepSeek V4

SandBase Harness 是一个本地优先的 AI Agent 运行时，用于持久化、可审计的 Agent 会话。它通过 DeepSeek 的 OpenAI 兼容 API 支持 DeepSeek V4，也可以通过 stdio MCP Bridge 将运行时接入 DeepSeek Harness。

- **GitHub：** <https://github.com/sandbaseai/sandbase-harness>
- **运行时文档：** <https://github.com/sandbaseai/sandbase-harness/blob/main/docs/deepseek-v4.md>

#### 1. 安装 SandBase Harness

使用带标签的源码版本，保证运行时和 MCP 集成可复现：

```sh
git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness
npm ci
npm run build:runtime
mkdir ../my-agents
cd ../my-agents
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
```

SandBase Harness 需要 Node.js 22 或更高版本。运行时默认在 `http://127.0.0.1:3000` 提供本地 API。

#### 2. 配置 DeepSeek V4

在 [DeepSeek Platform](https://platform.deepseek.com/api_keys) 创建 API Key，然后为运行时进程设置环境变量：

```sh
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

打开 `http://127.0.0.1:3000/dashboard`，进入 **Settings > Models**，切换到 JSON 并保存：

```json
{
  "vendor": "openai_compatible",
  "base_url": "https://api.deepseek.com/v1",
  "api_key": "${DEEPSEEK_API_KEY}",
  "options": {
    "reasoning_effort": "max"
  }
}
```

创建 Agent 时，使用 `deepseek-v4-pro` 获得更强的编码和 Agent 能力；如果更关注延迟，可使用 `deepseek-v4-flash`。DeepSeek V4 支持最高 100 万 Token 上下文；SandBase Harness 会自动压缩过长会话。

#### 3. 运行第一个会话

在 Console 中选择 Agent，使用一个小型验证任务启动会话，例如：

```text
检查这个项目，说明它的测试命令，不要修改任何文件。
```

运行时会保留会话、工具活动、产物和终止事件元数据，便于检查与回放。不要将 API Key 提交到工作区。

#### 可选：通过 MCP 连接 DeepSeek Harness

按上面的步骤构建运行时，然后在 DeepSeek Harness 工作区中运行：

```sh
export MANAGED_AGENTS_URL=http://127.0.0.1:3000
curl --fail --silent --show-error "$MANAGED_AGENTS_URL/v1/x/health"
dsh plugin --profile web add -w ../sandbase-harness
dsh web
```

安装后的 Bundle 会通过 `mcp__sandbase__*` 命名空间暴露 Agent、持久化会话、流式轮次、产物和取消操作。如果运行时启用了认证，请在启动 DeepSeek Harness 前同时设置 `MANAGED_AGENTS_API_KEY`。

