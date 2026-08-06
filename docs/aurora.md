[English](./aurora.md) | [简体中文](./aurora.zh-CN.md) · [← Back](../README.md)

# Integrate with Aurora

Aurora is the **control hub of the AI application era** — one account, one gateway, and every supported agent and client reaches the world's best models through it. Bring your own DeepSeek API key, create an Aurora key, then start building with DeepSeek-V4 from your existing client or from Aurora Assistant.

- **Website:** <https://auroramos.com>

#### 1. Download Aurora

Go to <https://auroramos.com>, download the Aurora client for your platform (macOS / Windows), and install it.

#### 2. Create an Aurora account

Launch Aurora and sign up for an account. New accounts start with a trial and a signup credit grant.

#### 3. Import a DeepSeek API Key

1. Get a DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
2. In the Aurora console, open **API Platforms** and import your DeepSeek API key as an API Platform resource.

Aurora now routes DeepSeek traffic through your account — identity, spend, and audit converge in one place.

#### 4. Create an Aurora personal API Key

In **API Keys**, create a **Personal** key. Your clients use this key as the bearer credential when talking to Aurora's gateway.

#### 5. Start building with DeepSeek-V4

**Path A — from your existing client (via Aurora Desktop):**

1. Open Aurora Desktop and go to its **local invocation page**.
2. Pick the client you already use — Claude Code, Codex, or Claude Desktop.
3. In the **key picker**, select the **Personal** Aurora key you just created.
4. In the **model picker**, select `deepseek/deepseek-v4-flash` or `deepseek/deepseek-v4-pro`.
5. Start calling. Requests are routed through your Aurora account to DeepSeek.

**Path B — from Aurora Assistant (terminal):**

1. Launch Aurora Assistant.
2. Run `/key` and select the **Personal** Aurora key you just created in the key picker.
3. Run `/model` and select `deepseek/deepseek-v4-flash` or `deepseek/deepseek-v4-pro` in the model picker.
4. Optionally run `/effort` to set the reasoning effort level.
5. Start building.

#### Notes

- DeepSeek-V4 models support a **1M-token** context window.
- Thinking mode is on by default; Aurora maps reasoning effort levels across providers.
