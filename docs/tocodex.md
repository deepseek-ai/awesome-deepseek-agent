[English](./tocodex.md) | [简体中文](./tocodex.zh-CN.md) · [← Back](../README.md)

# Integrate with ToCodex

ToCodex is an open-source, enterprise-grade general-purpose AI coding agent, available as a desktop app, a VS Code extension, and a CLI. DeepSeek is a built-in, top-listed model provider in ToCodex, so you only need to fill in your API key to get started — no manual endpoint or model setup required.

#### 1. Install ToCodex

- Open VS Code.
- Click the **Extensions** icon in the activity bar (or press `Ctrl+Shift+X`).
- Search for `ToCodex`.
- Find the **ToCodex** extension in the results and click **Install**.

> You can also download the desktop app or install the CLI from the [ToCodex website](https://tocodex.com).

#### 2. Open the Provider Selector

- Launch ToCodex from the activity bar.
- On the onboarding screen (or **Settings → Providers → API Provider**), open the provider list.
- DeepSeek is listed as a built-in provider — select **DeepSeek**.

<div align="center">
<img src="./assets/tocodex_step_1.png" width="250" border="1" />
</div>

#### 3. Configure the DeepSeek Provider

- With **DeepSeek** selected as the API Provider, paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys).
- ToCodex automatically fetches the available DeepSeek models, along with their specs and pricing — no manual base URL or model spec configuration is needed.

<div align="center">
<img src="./assets/tocodex_step_2.png" width="250" border="1" />
</div>

#### 4. Select a Model and Start

- Open the model selector and choose **deepseek-v4-pro** (most capable) or **deepseek-v4-flash** (faster, lower cost).
- ToCodex supports the full 1M-token context window of the DeepSeek-V4 series, and lets you adjust the **reasoning effort** level for deeper thinking on complex tasks.
- You can also assign a separate DeepSeek model as the auxiliary model for lightweight subtasks.

<div align="center">
<img src="./assets/tocodex_step_3.png" width="250" border="1" />
</div>

After configuration, you can start using ToCodex with DeepSeek across its MCP tools, custom modes, scheduled tasks, and configurable model routing.

> **Models:** `deepseek-v4-pro` and `deepseek-v4-flash` are the current DeepSeek-V4 models. The legacy `deepseek-chat` and `deepseek-reasoner` models are being deprecated.
