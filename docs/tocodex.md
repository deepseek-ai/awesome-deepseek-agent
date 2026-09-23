[English](./tocodex.md) | [简体中文](./tocodex.zh-CN.md) · [← Back](../README.md)

# Integrate with ToCodex

ToCodex is an AI-powered coding assistant that runs as a VS Code extension, IDE, desktop app, or CLI. It supports OpenAI-compatible providers, multi-model routing, MCP tools, and scheduled automation, so you can plug in DeepSeek-V4-Pro or DeepSeek-V4-Flash in a few minutes.

- **Website:** <https://tocodex.com>
- **VS Code Marketplace:** <https://marketplace.visualstudio.com/items?itemName=ToCodex.tocodex>
- **Open-source (Community):** <https://github.com/tocodex-ai/tocodex-community>

#### 1. Install ToCodex

**Option A: Install from the VS Code Marketplace**

- Open VS Code.
- Click the **Extensions** icon in the activity bar (or press `Ctrl+Shift+X`).
- Search for `ToCodex`.
- Click **Install** on the **ToCodex** extension.

Or install from the command line:

```sh
code --install-extension tocodex.tocodex
```

**Option B: Use the ToCodex Desktop app or IDE**

Download from <https://tocodex.com/download.html> — the desktop client works out of the box on Windows 10/11 and macOS.

#### 2. Get a DeepSeek API Key

- Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys) and create an API key.

#### 3. Add DeepSeek as an API Provider

- Open the ToCodex settings / provider management page.
- Choose **OpenAI Compatible** (or a DeepSeek preset if available).
- Fill in the following fields:

| Field | Value |
|-------|-------|
| Base URL | `https://api.deepseek.com` |
| API Key | Your DeepSeek API key (`sk-...`) |
| Model ID | `deepseek-v4-pro` (or `deepseek-v4-flash`) |

> **Note:** The current model IDs are `deepseek-v4-pro` and `deepseek-v4-flash`. The old `deepseek-chat` and `deepseek-reasoner` IDs are deprecated.

#### 4. Configure context window and thinking mode

DeepSeek V4 models support up to **1 million tokens** of context and a maximum output of 384K tokens. If the model config in ToCodex lets you set these values, use:

- `context_window: 1000000`
- `max_tokens: 384000`

DeepSeek V4 supports both thinking (reasoning) and non-thinking modes (thinking mode is on by default). In ToCodex, make sure thinking mode stays enabled and use a high reasoning effort (e.g. `max`) for the best coding experience. Do not disable thinking mode as a workaround — it degrades model performance.

#### 5. First run

- Open your project folder in VS Code.
- Select the `deepseek-v4-pro` model in the model picker.
- Send a prompt such as `explain this codebase` to verify the connection.

You're all set — start coding with DeepSeek inside ToCodex.

#### Troubleshooting

- **401 Unauthorized**: double-check the API key and make sure there are no extra spaces.
- **Model not found**: confirm the Model ID is exactly `deepseek-v4-pro` or `deepseek-v4-flash` (the old `deepseek-chat` / `deepseek-reasoner` IDs stopped serving).
- **Long context**: ToCodex supports 1M context; if requests fail on very large inputs, reduce the input size or check the official [rate limits](https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit).
