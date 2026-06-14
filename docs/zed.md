[English](./zed.md) | [简体中文](./zed.zh-CN.md) · [← Back](../README.md)

# Integrate with Zed

> **Requires:** Zed v0.160 or later.

Zed is a high-performance, collaborative code editor with a built-in AI agent. DeepSeek is supported as a first-class API provider — no OpenAI-compatible workaround needed. API keys are stored in your system keychain, not in `settings.json`.

Reference: [Zed Docs — Use API Access](https://zed.dev/docs/ai/use-api-access)

#### 1. Get a DeepSeek API Key

- Visit the [DeepSeek platform](https://platform.deepseek.com/api_keys) and create an API key.
- Make sure your account has credits or paid API usage enabled.

#### 2. Open Agent Settings (UI)

- Open Zed.
- Open the command palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Linux/Windows).
- Type `agent: open settings` and select it. This opens the Agent Settings panel.

In the Agent Settings panel you'll see sections for each LLM provider. Scroll to the **DeepSeek** section.

#### 3. Enter Your API Key

- In the Agent Settings panel, go to the **DeepSeek** section.
- Enter your DeepSeek API key. Zed saves it to your system keychain — never in `settings.json`.

Alternatively, set the `DEEPSEEK_API_KEY` environment variable. Non-empty environment variables take precedence over the keychain value.

#### 4. (Optional) Add Custom Models

Zed ships with default DeepSeek models. To ensure you have the latest `deepseek-v4-pro` and `deepseek-v4-flash` with 1M context, add custom models in your settings file:

Open with `zed: open settings file` and add:

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

> **Note:** DeepSeek V4 models support up to **1 million tokens** of context. `max_tokens` sets the context window (1,000,000) and `max_output_tokens` caps the response length (384,000).

#### 5. Select the Model and Start Using Zed

- Open the Agent Panel with `Ctrl+Enter` (or click the AI icon in the status bar).
- Choose **DeepSeek V4 Pro** or **DeepSeek V4 Flash** from the model dropdown.
- Type your prompt and press `Enter`. The Zed Agent can read, edit, search, and run code in your project.

You can also use the Inline Assistant: select code, press `Ctrl+Enter`, and describe the change.
