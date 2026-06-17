[English](./rtrvr.md) | [简体中文](./rtrvr.zh-CN.md) · [← Back](../README.md)

# Integrate with rtrvr.ai

rtrvr.ai is a browser-native AI web agent for scraping, form filling, monitoring, and multi-step web automation. You can run it from the Chrome extension with your own DeepSeek API Key, so browser-extension runs can use your DeepSeek account directly.

- **Website:** <https://www.rtrvr.ai/>
- **Extension:** <https://chromewebstore.google.com/detail/retriever-ai-web-agent/jldogdgepmcedfdhgnmclgemehfhpomg>
- **Docs:** <https://www.rtrvr.ai/docs>

#### 1. Prepare rtrvr.ai and a DeepSeek API Key

1. Install the [Retriever: AI Web Agent](https://chromewebstore.google.com/detail/retriever-ai-web-agent/jldogdgepmcedfdhgnmclgemehfhpomg) browser extension.
2. Sign in to rtrvr.ai from the extension.
3. Create an API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

rtrvr.ai supports BYO model keys and OpenAI-compatible or local endpoints. Use the browser extension when you want free local browser automation with your own DeepSeek key.

#### 2. Add DeepSeek as a Custom Provider

Open the rtrvr.ai extension settings and add a custom OpenAI-compatible model provider.

Use these values:

```text
Provider name: DeepSeek
API Key: <your DeepSeek API Key>
Base URL: https://api.deepseek.com/v1
Chat Completions URL, if requested: https://api.deepseek.com/v1/chat/completions
```

Add the current DeepSeek V4 model ids:

```text
deepseek-v4-pro
deepseek-v4-flash
```

Choose `deepseek-v4-pro` for difficult browser workflows, coding research, and long multi-step tasks. Choose `deepseek-v4-flash` for faster everyday scraping and page interaction.

#### 3. Run a Browser Task

1. Open the page you want rtrvr.ai to work on.
2. Open the extension.
3. Select your DeepSeek provider and model.
4. Describe the browser task in plain English, for example:

```text
Extract the product name, price, rating, and availability from this page and return a JSON table.
```

The extension runs in your browser session, so it can use pages you are already logged in to. Your DeepSeek usage is billed through your DeepSeek API account.

#### 4. Notes for DeepSeek V4

- DeepSeek V4 models support up to a 1M token context window. rtrvr.ai compresses browser pages into structured page data before sending model calls, so there is no separate context-window field to configure in the extension flow.
- For the strongest reasoning behavior, use `deepseek-v4-pro` for planning-heavy tasks. If your rtrvr.ai build exposes advanced provider request options, set `reasoning_effort` to `max`.
- Keep `deepseek-v4-flash` available as a faster fallback for simple extraction and navigation.

#### Troubleshooting

- Authentication fails: recheck the API Key copied from the DeepSeek Platform.
- Model not found: confirm the model id is exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- Provider connection fails: use `https://api.deepseek.com/v1` as the base URL, or `https://api.deepseek.com/v1/chat/completions` only if the field asks for the full chat-completions endpoint.
- The extension does not run on a logged-in page: make sure you are using the same browser profile where the rtrvr.ai extension is installed and signed in.
