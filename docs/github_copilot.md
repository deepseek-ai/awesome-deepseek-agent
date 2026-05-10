[English](./github_copilot.md) | [简体中文](./github_copilot.zh-CN.md) · [← Back](../README.md)

# Integrate with GitHub Copilot

**DeepSeek V4 for Copilot Chat** is a VS Code extension that adds DeepSeek V4 Pro and Flash directly into GitHub Copilot's model picker. However, this extension is not yet available on the Marketplace.
**OAI Compatible Copilot** is a VS Code extension that lets you bring any OpenAI-compatible model into GitHub Copilot Chat.

You can [use OAI Compatible Copilot](#integrate-with-copilot-in-an-openai-compatible-way) to connect DeepSeek, or install the [DeepSeek For Copilot extension](#integrate-with-deepseek-for-copilot-extension) directly instead (recommended).


### Integrate with Copilot in an OpenAI-Compatible Way

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

### Integrate with the Deepseek For Copilot Extension

#### 1. Install the Extension
- Install [VS Code](https://code.visualstudio.com/) 1.116 or later.
- Make sure you have a GitHub Copilot subscription (Free / Pro / Enterprise; the free tier works).
- Download the latest Deepseek For Copilot extension (`.vsix` file) from the [GitHub Release](https://github.com/Vizards/deepseek-v4-for-copilot/releases) page.
- In VS Code, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`), type `vsix`, choose `Extensions: Install from VSIX...`, and select the downloaded `deepseek-v4-for-copilot-x.y.z.vsix` file to install it.

#### 2. Get a DeepSeek API Key
- Go to [DeepSeek Platform](https://platform.deepseek.com/api_keys) and create an API key.
- Copy the key (it starts with `sk-`).

#### 3. Configure the API Key in VS Code
- Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`).
- Run **Deepseek: Set API Key**.
- Paste the API key into the input box and press Enter to confirm.
- The key is stored securely in the OS keychain and is never written to disk.
- The extension automatically registers DeepSeek as a Copilot model provider, so there is no need to manually add a Provider or Model.

#### 4. Select the Model and Start Chatting
- Open Copilot Chat (`Cmd+Shift+I` / `Ctrl+Shift+I`).
- Click the model picker below the chat area, then click the gear settings icon.
- Choose **DeepSeek V4 Pro** or **DeepSeek V4 Flash**, and turn on the eye icon.
- Start chatting — agent mode, tool calling, and all Copilot features are available right away.

#### Optional: Configure Thinking Depth

In the model picker, click the gear icon to open the "Manage Language Models" view. Then click the gear icon next to the DeepSeek model to choose the thinking depth:

- None — fastest, no reasoning.
- High — balanced mode (default).
- Max — deep reasoning, suited for complex tasks.

#### Optional: Vision Support

DeepSeek V4 is a text-only model, but the extension automatically handles images. When you drag a screenshot into the chat, the extension uses another installed Copilot model (such as Claude or GPT-4o) to describe the image content before sending it to DeepSeek. Run Deepseek: Set Vision Proxy Model to choose the model used for image descriptions.
