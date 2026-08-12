[English](./cursor.md) | [简体中文](./cursor.zh-CN.md) · [← Back](../README.md)

# Integrate with Cursor

Cursor is an AI code editor with a built-in agentic coding assistant. You can point its OpenAI-compatible API at DeepSeek to use `deepseek-v4-pro` and `deepseek-v4-flash`.

#### 1. Upgrade Cursor to the Latest Version

- Open Cursor and make sure it is updated to the latest version (Cursor → Check for Updates...).

#### 2. Open Model Settings

- Open **Settings → Models**.
- Expand the **API Keys** section.

#### 3. Override the OpenAI Base URL

- Enable **Override OpenAI Base URL** and set it to:

```
https://api.deepseek.com
```

#### 4. Configure the OpenAI API Key

- Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **OpenAI API Key** field.
- Enable **Secret saved** so the key is stored securely.

#### 5. Add Custom Models

- Click **Add Custom Model** and add the following models one by one:
  - `deepseek-v4-flash`
  - `deepseek-v4-pro`

#### 6. Start Using DeepSeek in Cursor

- Select `deepseek-v4-pro` or `deepseek-v4-flash` from the model selector in the chat / agent panel and start coding.

> **Note:** DeepSeek V4 models support up to **1 million tokens** of context. Cursor does not expose a context window setting, so the full window is available to the model automatically.
