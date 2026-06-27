[English](./vscode_copilot.md) | [简体中文](./vscode_copilot.zh-CN.md) · [← Back](../README.md)

# Integrate with VS Code Copilot (Native)

VS Code supports configuring custom OpenAI-compatible API endpoints natively via `chatLanguageModels.json` — no third-party extension required. You can use DeepSeek V4 models directly in Copilot Chat's model picker with Agent mode, tool calling, MCP, and all Copilot features intact.

#### 1. Prerequisites

- VS Code 1.100 or later (the custom model feature was introduced around this version).
- A GitHub Copilot subscription (Free / Pro / Enterprise — the free tier works).
- A DeepSeek API key from [platform.deepseek.com](https://platform.deepseek.com/api_keys).

#### 2. Open chatLanguageModels.json

- Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`).
- Run **Preferences: Configure Chat Language Models**.
- This opens `chatLanguageModels.json` in your VS Code user data folder.

> **Tip:** You can also find this file manually at:
> - **macOS:** `~/Library/Application Support/Code/User/chatLanguageModels.json`
> - **Windows:** `%APPDATA%\Code\User\chatLanguageModels.json`
> - **Linux:** `~/.config/Code/User/chatLanguageModels.json`

<div align="center">
<img src="./assets/vscode_add_deepseek_0_open_model_add_plane.png" width="800" border="1" />
</div>

<div align="center">
<img src="./assets/vscode_add_deepseek_1.png" width="800" border="1" />
</div>

#### 3. Add DeepSeek Configuration

Paste the following JSON into the array in `chatLanguageModels.json`. If you already have other custom models configured, add this object alongside them:

```json
{
    "name": "DeepSeek",
    "vendor": "customendpoint",
    "apiKey": "${input:chat.lm.secret.deepseek}",
    "apiType": "chat-completions",
    "models": [
        {
            "id": "deepseek-v4-pro",
            "name": "DeepSeek V4 Pro",
            "url": "https://api.deepseek.com",
            "toolCalling": true,
            "vision": false,
            "thinking": true,
            "maxInputTokens": 1000000,
            "maxOutputTokens": 64000,
            "supportsReasoningEffort": [
                "low",
                "max",
                "xhigh"
            ]
        },
        {
            "id": "deepseek-v4-flash",
            "name": "DeepSeek V4 Flash",
            "url": "https://api.deepseek.com",
            "toolCalling": true,
            "vision": false,
            "thinking": true,
            "maxInputTokens": 1000000,
            "maxOutputTokens": 64000,
            "supportsReasoningEffort": [
                "low",
                "max",
                "xhigh"
            ]
        }
    ],
    "settings": {
        "deepseek-v4-pro": {
            "reasoningEffort": "xhigh"
        },
        "deepseek-v4-flash": {
            "reasoningEffort": "xhigh"
        }
    }
}
```

> **Note:** The `${input:chat.lm.secret.deepseek}` value tells VS Code to prompt you for the API key the first time you select the model. The key is stored securely in the OS keychain.

Here is the step-by-step configuration in VS Code:

<div align="center">
<img src="./assets/vscode_add_deepseek_2_add_group_name.png" width="800" border="1" />
<p><em>Step 1 — Set the group name to "DeepSeek" and choose the vendor type</em></p>
</div>

<div align="center">
<img src="./assets/vscode_add_deepseek_3_add_apikey.png" width="800" border="1" />
<p><em>Step 2 — Configure the API key (stored securely in the OS keychain)</em></p>
</div>

<div align="center">
<img src="./assets/vscode_add_deepseek_4_set_group_api_endpoint.png" width="800" border="1" />
<p><em>Step 3 — Set the API endpoint URL to https://api.deepseek.com</em></p>
</div>

<div align="center">
<img src="./assets/vscode_add_deepseek_5_add_model_config.png" width="800" border="1" />
<p><em>Step 4 — Add model configuration (model ID, token limits, reasoning effort)</em></p>
</div>

#### 4. Set Your API Key

- Open Copilot Chat (`Cmd+Shift+I` / `Ctrl+Shift+I`).
- Click the model picker at the top-right corner.
- Select **DeepSeek V4 Pro** or **DeepSeek V4 Flash**.
- VS Code will prompt you to enter the API key. Paste your DeepSeek API key (starts with `sk-`).

> **Tip:** To change or clear the API key later, run **Preferences: Configure Chat Language Model Secrets** from the Command Palette.

#### 5. Start Chatting

That's it! Agent mode, tool calling, MCP servers, skills, custom instructions — all of Copilot's features now run on DeepSeek V4.

#### Optional: Configure Thinking Effort

VS Code's native model picker supports per-model options. In the model picker, click the gear icon next to a DeepSeek model to adjust the thinking effort:

- **Low** — fastest, minimal reasoning.
- **Max** — balanced deep reasoning.
- **XHigh** — deepest reasoning for complex coding tasks (recommended).

You can also set the default reasoning effort via the `settings` field in `chatLanguageModels.json`. The configuration above sets `"reasoningEffort": "xhigh"` as the default for both models.
