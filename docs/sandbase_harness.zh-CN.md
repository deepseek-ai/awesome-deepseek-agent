[English](./sandbase_harness.md) | [简体中文](./sandbase_harness.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 SandBase Harness 中接入 DeepSeek V4

[SandBase Harness](https://github.com/sandbaseai/sandbase-harness) 是一个开源 Agent 运行时，提供持久化会话、沙箱化工具执行、MCP 工具、Skills、审计、回放和本地 Web 控制台。

## 安装 SandBase Harness

安装 Node.js 22 或更高版本，然后创建工作区：

```bash
mkdir my-sandbase-agents
cd my-sandbase-agents
npx managed-agents init
```

设置 DeepSeek API Key，避免将密钥写入工作区：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

启动运行时：

```bash
npx managed-agents start
```

打开 `http://127.0.0.1:3000/dashboard`。

## 配置 DeepSeek V4

在控制台进入 **Settings > Models**，切换到 JSON 编辑器并填写：

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

保存并激活配置。SandBase Harness 会把 `reasoning_effort` 传递到 OpenAI 兼容的 Chat Completions 请求中。对 `deepseek-v4-pro` 使用 `max` 可以启用其最强推理模式。

DeepSeek V4 支持最高 100 万 token 上下文。SandBase Harness 会自动压缩长会话，目前不提供单独的上下文窗口设置，因此无需填写不会生效的 `context_window` 字段。

## 创建 Agent 并运行第一个任务

创建 `agents/sandbase-coding-agent.yaml`：

```yaml
name: sandbase-coding-agent
model: deepseek-v4-pro
system: 你是一个严谨的编程 Agent。请检查仓库、进行聚焦的修改并完成验证。
tools:
  - type: agent_toolset_20260401
```

重启运行时或执行 `npx managed-agents reload`，在控制台中打开该 Agent、创建会话，然后发送一个任务，例如：

```text
检查这个仓库，解释其架构，并找出一项可以通过测试验证的小型改进。
```

如果更看重低延迟而不是最大推理深度，可以改用 `deepseek-v4-flash`。

## 安全说明

- 请把 `DEEPSEEK_API_KEY` 保存在运行时环境变量中，不要提交到仓库。
- 默认本地沙箱会以当前操作系统用户身份执行命令，适合可信开发环境；如需更强的隔离边界，请使用 Docker 或 Kubernetes 沙箱提供方。

## DeepSeek Harness 相关资源

SandBase Harness 还提供了连接 DeepSeek 官方 Harness 运行时的桥接能力。如需了解上游运行时心智模型、Web 与 Headless 快速入门、工具策略管线、MCP、Python SDK、Windows 边界和排障方法，请参阅基于官方来源编写的 [DeepSeek Harness Handbook](https://github.com/sandbaseai/deepseek-harness-handbook)。其最新 Release 还附带一份可下载的 10 页英文速查指南。
