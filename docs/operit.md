[English](./operit.md) | [简体中文](./operit.zh-CN.md) · [← Back](../README.md)

# Integrate with Operit

Operit is an open-source Android AI Agent that provides all-around assistant capabilities. DeepSeek V4 can be used through Operit's built-in DeepSeek setup or through an OpenAI-compatible endpoint.

#### 1. Install Operit

- Download the latest APK from the [Operit official website](https://operit.app/), or use the [GitHub releases page](https://github.com/AAswordman/Operit/releases).
- Launch Operit and complete the first-run onboarding.

See the official [Operit beginner guide](https://operit.app/#/guide/new) for the full onboarding walkthrough.

#### 2. Configure DeepSeek

During first-run setup, tap `Get token`. Operit will open its built-in DeepSeek page. Create an API Key there, then paste it back into Operit to start chatting.

Operit will automatically fill in `deepseek-v4-flash`.

DeepSeek V4 supports up to a 1M-token context window. You can adjust the context amount you want to use in Operit's context compression settings.

To configure it manually, open `Settings` -> `Model and Parameter Configuration`, create a configuration, and use:

```text
Provider: DeepSeek
Endpoint: https://api.deepseek.com/v1/chat/completions
API Key: <your DeepSeek API Key>
Model: deepseek-v4-pro or deepseek-v4-flash
```

#### 3. Get Started

Return to the chat page, select the DeepSeek model, and send a test message.
