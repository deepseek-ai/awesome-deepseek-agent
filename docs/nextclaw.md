[English](./nextclaw.md) | [简体中文](./nextclaw.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with NextClaw

NextClaw turns your computer into a powerful AI assistant that coordinates agents, skills, CLI tools, automations, and messaging apps.

This guide shows how to configure DeepSeek V4 in NextClaw and send your first message.

#### 1. Install NextClaw

Install Node.js first if you have not already. Then install NextClaw from npm:

```bash
npm i -g nextclaw
```

Start NextClaw:

```bash
nextclaw start
```

Open the Web UI:

```text
http://127.0.0.1:55667
```

#### 2. Configure DeepSeek

In the Web UI:

1. Open **Settings**.
2. Open **Providers**.
3. Select **DeepSeek**.
4. Paste your [DeepSeek API key](https://platform.deepseek.com/api_keys).
5. Keep the API base as `https://api.deepseek.com` unless you use a compatible proxy.
6. Save the provider configuration.

Then open the model or default agent settings and choose one of the current DeepSeek V4 models:

```text
deepseek/deepseek-v4-pro
deepseek/deepseek-v4-flash
```

#### 3. First Run

Open **Chat** in the Web UI and send a short test prompt:

```text
Explain how NextClaw can use DeepSeek together with tools and automations.
```

After the first reply works, you can connect more NextClaw capabilities, such as skills, CLI tools, scheduled automations, and messaging apps.

#### Troubleshooting

- **401 / invalid API key**: Check the DeepSeek API key in the provider settings.
- **Unknown model**: Make sure the model is `deepseek/deepseek-v4-pro` or `deepseek/deepseek-v4-flash`.
- **Cannot open the UI**: Confirm `nextclaw start` is still running and open `http://127.0.0.1:55667`.
