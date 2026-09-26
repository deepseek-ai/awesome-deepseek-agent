[English](./dassi.md) | [简体中文](./dassi.zh-CN.md) · [← Back](../README.md)

# Integrate with Dassi

Dassi is an AI agent for Chrome that runs in the browser side panel. It supports browser automation, writing, and analysis, with a built-in DeepSeek provider for using your own API key.

- **Website:** <https://dassi.ai/>
- **Documentation:** <https://docs.dassi.ai/>

#### 1. Install Dassi

1. Install [Dassi from the Chrome Web Store](https://chromewebstore.google.com/detail/dassi-ai-agent-for-chrome/bjcngahpcjeililljmfegmlanlpgibdi).
2. Pin the extension, click its toolbar icon to open the side panel, and sign in to Dassi.
3. Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys). Your DeepSeek account needs API access and sufficient balance.

Using your own key requires an active Dassi trial or a plan that includes BYOK. Dassi access and DeepSeek API usage are billed separately; see [Dassi plans](https://dassi.ai/pricing/) for current terms.

#### 2. Connect DeepSeek

1. Open **Settings** from the side-panel menu and select **Models**.
2. Expand **API keys** and find **DeepSeek** under **Other providers**.
3. Click **API Key**, paste your DeepSeek key, and click **Save**.
4. Wait for the connection confirmation. The built-in provider uses `https://api.deepseek.com`; no custom endpoint or configuration file is needed.
5. For browser tasks, select the **vision-capable Flash entry** in the model selector. In Dassi catalogs using older names, this is `deepseek-v4-flash-vision-exp`, which DeepSeek now serves with current Flash. For text-only tasks, you can also choose **DeepSeek V4 Pro** (`deepseek-v4-pro`). Confirm your selection before sending the next message.

#### 3. Choose a Model and Understand Its Limits

- **DeepSeek V4 Pro** (`deepseek-v4-pro`) is the default for a new DeepSeek connection. It is suitable for text, code, and reasoning tasks.
- **Current DeepSeek Flash** (`deepseek-flash`, V4.1 Flash) supports both text and **vision**, including reading screenshots and analyzing images. See the [DeepSeek vision guide](https://api-docs.deepseek.com/guides/vision/). Some Dassi releases list the older IDs `deepseek-v4-flash` or `deepseek-v4-flash-vision-exp`; DeepSeek still accepts these aliases and serves them with current Flash. See the [current model details](https://api-docs.deepseek.com/quick_start/pricing/).
- DeepSeek V4 supports **1 million tokens of context**. Dassi uses its model catalog for context limits; there is no separate context-window field to set in the provider card.
- **Vision in Dassi:** For screenshot-based browser tasks, use a Flash entry that Dassi marks as vision-capable. Older Dassi catalogs may still mark `deepseek-v4-flash` as text-only; that is a catalog limitation, not a limitation of current Flash. Update the extension if needed and check the model selector. V4 Pro remains text-only.
- **Thinking:** Dassi's main agent uses `high` reasoning with thinking enabled. DeepSeek supports `reasoning_effort: "max"`, but Dassi currently has no user-facing effort selector or request-body editor to enable it. This guide does not claim `max` support in Dassi. See [DeepSeek thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/) for the API's available levels.

#### 4. Run Your First Task

With the **vision-capable Flash entry** selected, open a public article and send:

```text
Read this page and summarize its main points in five bullets.
Include the page title and URL. Do not change anything on the website.
```

Confirm that Dassi reads the page and returns a summary with the source URL. See the [Dassi browser automation guide](https://docs.dassi.ai/guides/browser-automation/) for more tasks.

For a text-only connection check with **DeepSeek V4 Pro**, send:

```text
Write a JavaScript function that removes duplicate objects by their id while
preserving the original order. Include an example with duplicate IDs.
```

Confirm that Dassi returns the function and example. This checks the connection without requiring screenshot input or changes to a website.

For writing and analysis, paste the relevant text into the conversation.

#### 5. Troubleshooting

- **Key rejected:** Check that you copied a DeepSeek API key and that the account has API access and balance. Enter keys in the provider settings, not in chat.
- **Connected, but another model answers:** Saving a provider key and selecting the active model are separate steps. Choose the DeepSeek model explicitly.
- **Text-only warning:** This refers to screenshot support. Use a text-only task to verify the connection, or switch to a vision-capable model for visual browser work.
- **Model missing:** Update the extension and check the model selector again. Available entries depend on Dassi's model catalog.
