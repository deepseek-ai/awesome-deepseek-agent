[English](./openagentd.md) | [简体中文](./openagentd.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenAgentd

[OpenAgentd](https://github.com/lthoangg/openagentd) 是开源的本地 AI Agent 桌面控制台。它在本机运行 FastAPI sidecar 与 React UI，支持主 Agent + 成员 Agent 的团队模式，并内置 DeepSeek Provider。

#### 1. 安装 OpenAgentd

macOS 桌面版可以通过 Homebrew 安装：

```bash
brew install --cask lthoangg/tap/openagentd
```

也可以从 [OpenAgentd Releases 页面](https://github.com/lthoangg/openagentd/releases/latest) 下载最新的 macOS / Linux 桌面构建。

如果使用 CLI / 本地 Web Server：

```bash
uv tool install openagentd
openagentd init
openagentd
```

OpenAgentd 会在 `http://localhost:4082` 启动本地 UI。

#### 2. 配置 DeepSeek

在桌面或 Web UI 中打开 **Settings → Providers**，选择 **DeepSeek**，填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)，并选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`。

你也可以直接编辑主 Agent 配置文件 `~/.config/openagentd/agents/openagentd.md`：

```yaml
---
name: openagentd
role: lead
model: deepseek:deepseek-v4-pro
temperature: 0.2
thinking_level: high
---
```

如果使用编码模式，请在 `~/.config/openagentd/agents/coding/openagentd.md` 中设置同样的模型。

OpenAgentd 会将 `thinking_level` 映射为 DeepSeek 的 thinking mode 字段。编码任务推荐使用 `deepseek-v4-pro` 与 `thinking_level: high`，如果更看重速度和成本，可以选择 `deepseek-v4-flash`。DeepSeek V4 支持 100 万 token 上下文窗口；OpenAgentd 内置 DeepSeek Provider 不需要额外配置上下文窗口。

#### 3. 开始使用

启动 OpenAgentd，新建会话并发送消息即可。编码模式下，OpenAgentd 会在同一个本地 UI 中展示工作区文件、工具调用、内联 diff、todos 与团队成员运行状态，由 DeepSeek 驱动 Agent 循环。
