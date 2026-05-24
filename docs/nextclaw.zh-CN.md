[English](./nextclaw.md) | [简体中文](./nextclaw.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 NextClaw 中接入 DeepSeek

NextClaw 把你的电脑变成一个强大的 AI 助手，协调 Agent、技能、CLI 工具、自动化和消息应用。

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

1. 打开 **Settings**。
2. 打开 **Providers**。
3. 选择 **DeepSeek**。
4. 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
5. API Base 默认保持为 `https://api.deepseek.com`，除非你使用兼容代理。
6. 保存 Provider 配置。

#### 3. 第一次运行

打开 Web UI 中的 **Chat**，在消息框的模型选择器中选择一个 DeepSeek V4 模型，然后发送一条测试消息：

```text
deepseek/deepseek-v4-pro
deepseek/deepseek-v4-flash
```

```text
解释一下 NextClaw 如何把 DeepSeek 和工具、自动化一起使用。
```

第一次回复成功后，你可以继续接入 NextClaw 的技能、CLI 工具、定时自动化和消息应用。

#### 常见问题

- **401 / API Key 无效**：检查 Provider 设置里的 DeepSeek API Key。
- **看不到 DeepSeek V4 模型**：先保存 DeepSeek Provider 设置，然后重新打开 **Chat** 并检查模型选择器。
- **打不开 UI**：确认 `nextclaw start` 仍在运行，并打开 `http://127.0.0.1:55667`。
