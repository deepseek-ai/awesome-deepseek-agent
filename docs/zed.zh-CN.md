[English](./zed.md) | [简体中文](./zed.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Zed

> **要求：** Zed v0.160 或更高版本。

Zed 是一款内置 AI Agent 的高性能协作代码编辑器。DeepSeek 作为一级 API 供应商直接支持，无需通过 OpenAI 兼容方式绕行。API Key 保存在系统钥匙串中，而非 `settings.json`。

参考：[Zed 文档 — 使用 API 访问](https://zed.dev/docs/ai/use-api-access)

#### 1. 获取 DeepSeek API Key

- 访问 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
- 确保账户已充值或有可用的 API 额度。

#### 2. 打开 Agent 设置界面

- 打开 Zed。
- 打开命令面板（macOS：`Cmd+Shift+P`，Linux/Windows：`Ctrl+Shift+P`）。
- 输入 `agent: open settings` 并选择。这将打开 Agent 设置面板。

在 Agent 设置面板中你会看到各个 LLM 供应商的配置区域。滚动到 **DeepSeek** 部分。

#### 3. 输入 API Key

- 在 Agent 设置面板中，找到 **DeepSeek** 部分。
- 输入你的 DeepSeek API Key。Zed 会将其保存到系统钥匙串中，绝不会写入 `settings.json`。

你也可以设置 `DEEPSEEK_API_KEY` 环境变量。非空环境变量的优先级高于钥匙串中的值。

#### 4. （可选）添加自定义模型

Zed 内置了默认的 DeepSeek 模型。为确保使用最新的 `deepseek-v4-pro` 和 `deepseek-v4-flash`（含 100 万 token 上下文），可在设置文件中添加自定义模型：

通过 `zed: open settings file` 打开设置文件，添加：

```json
{
  "language_models": {
    "deepseek": {
      "api_url": "https://api.deepseek.com",
      "available_models": [
        {
          "name": "deepseek-v4-flash",
          "display_name": "DeepSeek V4 Flash",
          "max_tokens": 1000000,
          "max_output_tokens": 384000
        },
        {
          "name": "deepseek-v4-pro",
          "display_name": "DeepSeek V4 Pro",
          "max_tokens": 1000000,
          "max_output_tokens": 384000
        }
      ]
    }
  }
}
```

> **注意：** DeepSeek V4 模型支持最高 **100 万 token** 的上下文窗口。`max_tokens` 设置上下文窗口大小（1,000,000），`max_output_tokens` 限制响应长度（384,000）。

#### 5. 选择模型并开始使用

- 按 `Ctrl+Enter` 打开 Agent 面板（或点击状态栏中的 AI 图标）。
- 从模型下拉菜单中选择 **DeepSeek V4 Pro** 或 **DeepSeek V4 Flash**。
- 输入提示词并按 `Enter` 发送。Zed Agent 可以在项目中读取、编辑、搜索和运行代码。

你也可以使用内联助手：选中代码，按 `Ctrl+Enter`，然后描述你想要的更改。
