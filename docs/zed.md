[English](./zed.md) | [简体中文](./zed.zh-CN.md) · [← Back](../README.md)

# Integrate with Zed

Zed is a high-performance, collaborative code editor built in Rust. It has a built-in AI assistant that supports OpenAI-compatible API providers, including DeepSeek.

#### 1. Open Settings

- Open Zed.
- Open the command palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Linux/Windows).
- Type `zed: open settings` and select it.

Alternatively, open `~/.config/zed/settings.json` directly.

#### 2. Configure the Assistant

Add a `deepseek` provider under the `assistant` section in your `settings.json`. Use the `openai_compatible` provider type pointing to the DeepSeek API:

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

> **Note:** DeepSeek V4 models support up to **1 million tokens** of context. The `max_tokens` and `max_completion_tokens` are set to 384,000 to reflect the maximum output tokens. Zed will manage the full context window automatically.

#### 3. Add Your API Key

Open the command palette (`Cmd+Shift+P` / `Ctrl+Shift+P`), type `assistant: open configuration` and select it. Add your DeepSeek API key:

```json
{
  "provider": {
    "deepseek": {
      "api_key": "sk-your-deepseek-api-key"
    }
  }
}
```

Alternatively, set the `DEEPSEEK_API_KEY` environment variable and omit `api_key` from the configuration.

#### 4. Enable Max Thinking (Recommended)

DeepSeek V4 Pro supports reasoning effort levels for better code generation. Add the `reasoning_effort` parameter to the model configuration to enable `max` thinking:

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

#### 5. Start Using Zed with DeepSeek

- Open the assistant panel with `Ctrl+Enter` (or click the AI icon in the status bar).
- Type your prompt and press `Enter` to send.
- You can also use inline transformations: select code, press `Ctrl+Enter`, and describe the change you want.

Your Zed editor is now powered by DeepSeek!
