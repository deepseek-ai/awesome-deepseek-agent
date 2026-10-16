[English](./crawshrimp_harness.md) | [简体中文](./crawshrimp_harness.zh-CN.md) · [← Back](../README.md)

# Integrate with Crawshrimp Harness

Crawshrimp Harness (抓虾) is an open-source, local-first ecommerce operations desktop agent built on DeepSeek Harness (DSH). It combines DSH conversations with browser automation, file and Office tools, reusable operation scripts, and permission approvals. You can connect your own DeepSeek API key through the built-in official provider. Local agent use does not require a Crawshrimp account.

- **GitHub:** <https://github.com/howtimeschange/crawshrimp-harness>
- **Downloads:** <https://github.com/howtimeschange/crawshrimp-harness/releases>
- **License:** Apache-2.0

These instructions follow the **v0.4.0** desktop release. The application uses Chinese interface labels; the labels below include the text to look for.

#### 1. Install Crawshrimp Harness

Download the installer for your computer from the [v0.4.0 release](https://github.com/howtimeschange/crawshrimp-harness/releases/tag/v0.4.0):

| Platform | Installer |
| --- | --- |
| macOS, Apple Silicon | `crawshrimp-harness-v0.4.0-mac-arm64.dmg` |
| macOS, Intel | `crawshrimp-harness-v0.4.0-mac-x64.dmg` |
| Windows, x64 | `crawshrimp-harness-v0.4.0-win-x64.exe` |

On macOS, open the DMG and copy the app to Applications. On Windows, run the installer. Launch Crawshrimp Harness and let its local agent runtime start. The desktop package includes DSH; a separate DSH CLI installation is unnecessary.

For the browser task below, make sure a supported browser, such as [Google Chrome](https://www.google.com/chrome/), is installed. Crawshrimp launches a dedicated browser instance with its own profile; if no supported browser is detected, the app asks you to select the browser executable.

#### 2. Configure the Official DeepSeek Provider

Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys) and ensure your API account has available balance. API usage is billed by DeepSeek; see the [current official pricing](https://api-docs.deepseek.com/quick_start/pricing).

1. Open **Settings (设置) → AI capabilities (AI 能力) → Text models (文本大模型)**.
2. Find the built-in **DeepSeek official (DeepSeek 官方)** provider and click **Edit (编辑)**.
3. In **Connection configuration (连接配置)**, leave **Base URL** as `https://api.deepseek.com` and paste your key into **API Key**. The built-in provider already uses the OpenAI-compatible protocol.
4. Click **Save Provider (保存 Provider)**. This persists the settings and requests a runtime reload. Wait for the runtime to be ready; if a task is still running, finish it and follow the settings notice to restart the runtime.
5. Confirm that the provider shows **Key configured (已配 Key)**. After saving, the actual key is not read back into the settings form; leaving the key field empty on a later edit preserves it.

Use this built-in official provider for the direct DeepSeek API setup described here. Its key and Base URL are configured independently of the other providers in the application.

#### 3. Select a Model and Reasoning Effort

Open a new agent conversation and select a model from the **DeepSeek 官方** provider. The built-in presets are:

| Model preset | DeepSeek API model ID |
| --- | --- |
| DeepSeek V4.1 Flash | `deepseek-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |

Start with **DeepSeek V4.1 Flash**. The app maps the built-in presets to these API IDs automatically. `deepseek-flash` is the current Flash ID listed in the [official model catalog](https://api-docs.deepseek.com/quick_start/pricing).

Both official presets register a **1,000,000-token (1M) context window**. No manual context-window setting or `[1m]` model suffix is needed for this OpenAI-compatible provider. This is the configured model capacity; conversation compaction and your own saved model-budget overrides can affect how much history is retained.

For complex tasks, open the conversation's model selector and choose **Max** under **Reasoning effort (推理等级)**. For these official presets, this enables thinking and sends `reasoning_effort: "max"` to DeepSeek. **Default** follows the provider's default behavior; **Off** explicitly disables thinking. The integration preserves `reasoning_content` in assistant history for tool-calling conversations, as required by the [DeepSeek thinking-mode API](https://api-docs.deepseek.com/guides/thinking_mode).

#### 4. Run Your First Task

Send a small browser task in the new conversation, for example:

```text
Use the browser to open https://api-docs.deepseek.com/ and summarize
the main documentation sections in three bullet points. Keep this task read-only.
```

The agent should open a browser page, inspect it with its browser tools, and return a summary. Check the visible tool results and browser preview to confirm that the page was actually opened. If the current permission mode requests approval, review the proposed action in the conversation before allowing it.

After this works, you can use the same conversation for ecommerce browser tasks, local file processing, and Office work. Office components needed for native preview or conversion are downloaded on demand in the standard lightweight desktop package.

#### 5. Troubleshooting

- **Authentication or balance error:** check the key, the `https://api.deepseek.com` Base URL, and your DeepSeek API balance in the official platform.
- **Model missing:** confirm you saved the **DeepSeek 官方** provider. In its **Model management (模型管理)** tab, **Restore preset models (恢复预设模型)** restores the built-ins; save the provider afterward. You can also use **Fetch latest models (获取最新模型)** and **Add selected models (添加所选模型)** to import selected upstream models.
- **Saved settings have not taken effect:** read the runtime status notice in Settings. An active task can defer a restart; wait for it to finish and restart the runtime before retrying.
