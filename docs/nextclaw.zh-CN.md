[English](./nextclaw.md) | [简体中文](./nextclaw.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 NextClaw 中接入 DeepSeek

NextClaw 是一个开源 AI 助手，可以把你的电脑变成一个强大的工作台，用来协调 Agent、技能、CLI 工具、自动化和消息应用。

这份指南会带你在 NextClaw 中配置 DeepSeek V4，并完成第一次对话。

#### 1. 安装 NextClaw

如果还没有安装 Node.js，请先安装 Node.js。然后通过 npm 安装 NextClaw：

```bash
npm i -g nextclaw
```

启动 NextClaw：

```bash
nextclaw start
```

打开 Web UI：

```text
http://127.0.0.1:55667
```

#### 2. 配置 DeepSeek

在 Web UI 中：

1. 打开 **Providers**。
2. 选择 **DeepSeek**。
3. 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
4. API Base 默认保持为 `https://api.deepseek.com`，除非你使用兼容代理。
5. 保存 Provider 配置。

然后打开模型或默认 Agent 设置，选择当前 DeepSeek V4 模型：

```text
deepseek/deepseek-v4-pro
deepseek/deepseek-v4-flash
```

如果你需要更强的编码和推理能力，推荐使用 `deepseek-v4-pro`。如果你更看重速度和成本，可以使用 `deepseek-v4-flash`。

DeepSeek V4 支持最高 100 万 token 上下文。NextClaw 的基础配置不需要单独填写 context window 字段；使用上面的 V4 模型名，并保持 NextClaw 为较新版本即可。

对于 DeepSeek V4 Pro thinking mode，请先基于当前 NextClaw 版本验证，再使用 NextClaw 构建中暴露的最高 thinking level。不要把切回旧 V3 模型名当作 reasoning 报错的规避方案。

#### 3. 第一次运行

打开 Web UI 中的 **Chat**，发送一条测试消息：

```text
解释一下 NextClaw 如何把 DeepSeek 和工具、自动化一起使用。
```

第一次回复成功后，你可以继续接入 NextClaw 的技能、CLI 工具、定时自动化和消息应用。

#### 常见问题

- **401 / API Key 无效**：检查 Provider 设置里的 DeepSeek API Key。
- **Unknown model**：确认模型名是 `deepseek/deepseek-v4-pro` 或 `deepseek/deepseek-v4-flash`。
- **打不开 UI**：确认 `nextclaw start` 仍在运行，并打开 `http://127.0.0.1:55667`。
- **Thinking / reasoning 报错**：先升级 NextClaw，不要把旧 V3 模型名当作规避方案。
