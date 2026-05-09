[English](./github_copilot.md) | [简体中文](./github_copilot.zh-CN.md) · [← Back](../README.md)

# Integrate with GitHub Copilot

**OAI Compatible Copilot** is a VS Code extension that lets you bring any OpenAI-compatible model into GitHub Copilot Chat. With it, you can use DeepSeek directly in Copilot Chat without waiting for official integration.

#### 1. Install the Extension

- Install [VS Code](https://code.visualstudio.com/) 1.116 or later.
- Make sure you have a GitHub Copilot subscription (Free / Pro / Enterprise; the free tier works).
- Install OAI Compatible Copilot from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=johnny-zhao.oai-compatible-copilot).

#### 2. Get a DeepSeek API Key

- Go to [DeepSeek Platform](https://platform.deepseek.com/api_keys) and create an API key.
- Copy the key (it starts with `sk-`).

#### 3. Configure the API Key in VS Code

- Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`).
- Run **OAICopilot: Open Configuration UI**.
- In the settings UI, find the **Provider Management** section and click **Add Provider**.
- In the expanded input form, enter a Provider Name such as "DeepSeek", paste the Base URL (default: `https://api.deepseek.com`) and API Key, then click `save`.
- The key is stored securely in the OS keychain and is never written to disk.

#### 4. Register Models

- In the same settings UI, find the **Model Management** section and click **Add Model**.
- Select the Provider ID you just created. Open Model ID and the available model list will appear below. Choose **DeepSeek V4 Pro** and **DeepSeek V4 Flash**. If they do not appear, check that the configuration above is correct. 
- Set `Context Length` to `1000000` and `Max Tokens` to `384000` to enable 1M context support.
- To configure Thinking Mode, go to Advanced Settings, set `Enable Thinking` to `True`, and set `Reasoning Effort` to `max` (supported values: `high`, `max`).
- Configure any other parameters as needed, then click `save`.

#### 5. Select the Model and Start Chatting

- Open Copilot Chat (`Cmd+Shift+I` / `Ctrl+Shift+I`).
- Click the model picker below the chat area, then click the gear settings icon.
- Choose **DeepSeek V4 Pro** or **DeepSeek V4 Flash**, and turn on the eye icon.
- Start chatting — agent mode, tool calling, and all Copilot features are available right away.
