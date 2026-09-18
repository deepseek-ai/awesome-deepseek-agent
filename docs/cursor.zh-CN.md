[English](./cursor.md) | [简体中文](./cursor.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Cursor

Cursor 是一款内置 Agent 编程助手的 AI 代码编辑器。通过将其 OpenAI 兼容 API 指向 DeepSeek，即可使用 `deepseek-v4-pro` 和 `deepseek-v4-flash`。

#### 1. 升级 Cursor 到最新版本

- 打开 Cursor，确认已升级到最新版本（Cursor → Check for Updates...）。

#### 2. 打开模型设置

- 打开 **Settings → Models**。
- 展开 **API Keys** 部分。

#### 3. 覆盖 OpenAI Base URL

- 启用 **Override OpenAI Base URL**，并填入：

```
https://api.deepseek.com
```

#### 4. 配置 OpenAI API Key

- 在 **OpenAI API Key** 中填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- 启用 **Secret saved**，安全保存密钥。

#### 5. 添加自定义模型

- 点击 **Add Custom Model**，依次添加以下模型：
  - `deepseek-v4-flash`
  - `deepseek-v4-pro`

#### 6. 在 Cursor 中使用 DeepSeek

- 在对话 / Agent 面板的模型选择器中选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`，即可开始编程。

> **提示：** DeepSeek V4 系列模型支持高达 **100 万 token** 的上下文窗口。Cursor 未提供上下文窗口配置项，模型将自动获得完整的上下文能力。
