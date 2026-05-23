[English](./dotcraft.md) | [简体中文](./dotcraft.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DotCraft

DotCraft 是一个项目级 .NET/C# Agent Harness。Desktop、TUI、CLI、机器人与自动化入口共享同一个工作区中的会话、技能、工具、审批和可观测能力。

- **GitHub：** <https://github.com/DotHarness/dotcraft>
- **文档：** <https://dotharness.github.io/dotcraft/>

DotCraft 通过 OpenAI 兼容的 Chat Completions API 接入 DeepSeek。它内置 Deep Thinking 适配器，可在工具调用轮次中保留 `reasoning_content`，并可将 DeepSeek V4 的上下文窗口配置为 100 万 token。

#### 1. 安装 DotCraft

从以下地址下载最新 DotCraft Desktop release：

```text
https://github.com/DotHarness/dotcraft/releases
```

安装适合你操作系统的包，然后启动 DotCraft Desktop。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 在 Desktop 中配置 DeepSeek

在 DotCraft 中打开一个真实项目目录作为工作区，然后进入 **Settings -> Model Providers**，创建一个 provider：

| 字段 | 值 |
|------|----|
| Provider id | `deepseek` |
| Display name | `DeepSeek` |
| Protocol | `openai` |
| Endpoint | `https://api.deepseek.com/v1` |
| API Key | 你的 DeepSeek API Key |
| Model | `deepseek-v4-pro` |
| Reasoning | Enabled |
| Reasoning effort | Extra High |
| Context window | `1000000` tokens |

如果更看重低延迟或成本，可以将 `deepseek-v4-flash` 作为轻量模型选项。

DotCraft 内置的 Deep Thinking 适配器会自动作用于 DeepSeek 模型和 DeepSeek endpoint。在工具调用对话中，它会把模型返回的 reasoning 元数据和 assistant 工具调用一起回传，从而让 thinking mode 与 agent 工作流保持兼容。

#### 4. 首次运行

在 DotCraft Desktop 中：

1. 打开项目工作区。
2. 新建一个 session。
3. 如果尚未选中，请选择 DeepSeek provider 和 `deepseek-v4-pro` 模型。
4. 发送一个仓库理解请求：

```text
请阅读这个仓库的 README 和 docs，告诉我这个项目怎么启动。
```

此时 session 应该会通过 DeepSeek V4 Pro 流式返回回答。Reasoning 内容会按照 DotCraft 默认的 reasoning 展示行为显示。

#### 其他 DotCraft 入口

完成 Desktop 配置后，同一个工作区配置可被 DotCraft 的其他入口复用：

| 入口 | 适合场景 |
|------|----------|
| Desktop | 图形化工作区、provider 配置、会话、trace、审批 |
| TUI | 通过 DotCraft AppServer 连接的完整终端界面 |
| CLI | 一次性项目任务和本地自动化命令 |
| ACP | 通过 Agent Client Protocol 接入编辑器和 IDE |
| 机器人与自动化 | 面向聊天平台和定时任务的共享工作区会话 |

#### 相关资源

- [DotCraft](https://github.com/DotHarness/dotcraft)
- [DotCraft 快速开始](https://dotharness.github.io/dotcraft/getting-started)
- [DotCraft 配置指南](https://dotharness.github.io/dotcraft/config_guide)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
