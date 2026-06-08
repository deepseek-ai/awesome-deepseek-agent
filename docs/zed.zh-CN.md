[English](./zed.md) | [简体中文](./zed.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Zed

Zed 是一款用 Rust 构建的高性能协作代码编辑器。其内置的 AI 助手支持 OpenAI 兼容的 API 供应商，包括 DeepSeek。

#### 1. 打开设置

- 打开 Zed。
- 打开命令面板（macOS：`Cmd+Shift+P`，Linux/Windows：`Ctrl+Shift+P`）。
- 输入 `zed: open settings` 并选择。

也可以直接打开 `~/.config/zed/settings.json` 文件。

#### 2. 配置助手

在 `settings.json` 中的 `assistant` 部分添加 `deepseek` 供应商。使用 `openai_compatible` 供应商类型指向 DeepSeek API：

```json
{
  "assistant": {
    "default_model": {
      "provider": "deepseek",
      "model": "deepseek-v4-pro"
    },
    "version": "2",
    "provider": {
      "deepseek": {
        "name": "deepseek",
        "type": "openai_compatible",
        "api_url": "https://api.deepseek.com",
        "available_models": [
          {
            "name": "deepseek-v4-pro",
            "max_tokens": 384000,
            "max_completion_tokens": 384000
          },
          {
            "name": "deepseek-v4-flash",
            "max_tokens": 384000,
            "max_completion_tokens": 384000
          }
        ]
      }
    }
  }
}
```

> **注意：** DeepSeek V4 模型支持最高 **100 万 token** 的上下文窗口。`max_tokens` 和 `max_completion_tokens` 设置为 384,000 以匹配最大输出 token 数。Zed 会自动管理完整的上下文窗口。

#### 3. 添加 API Key

打开命令面板（`Cmd+Shift+P` / `Ctrl+Shift+P`），输入 `assistant: open configuration` 并选择。添加你的 DeepSeek API Key：

```json
{
  "provider": {
    "deepseek": {
      "api_key": "sk-your-deepseek-api-key"
    }
  }
}
```

或者设置 `DEEPSEEK_API_KEY` 环境变量，即可在配置中省略 `api_key`。

#### 4. 启用 Max Thinking（推荐）

DeepSeek V4 Pro 支持推理强度级别，可获得更好的代码生成效果。在模型配置中添加 `reasoning_effort` 参数以启用 `max` 级别思考：

```json
{
  "name": "deepseek-v4-pro",
  "max_tokens": 384000,
  "max_completion_tokens": 384000,
  "extra_params": {
    "reasoning_effort": "max"
  }
}
```

#### 5. 开始在 Zed 中使用 DeepSeek

- 按 `Ctrl+Enter` 打开助手面板（或点击状态栏中的 AI 图标）。
- 输入提示词并按 `Enter` 发送。
- 你也可以使用内联转换：选中代码，按 `Ctrl+Enter`，然后描述你想要的更改。

你的 Zed 编辑器现已由 DeepSeek 驱动！
