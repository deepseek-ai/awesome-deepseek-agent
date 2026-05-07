[English](./qwen_code.md) | [简体中文](./qwen_code.zh-CN.md) · [← Back](../README.md)

# Integrating with Qwen Code

Qwen Code is an open-source terminal AI agent that helps you understand large codebases, automate tedious tasks, and accelerate delivery.

#### 1. Install Qwen Code

- Linux / macOS
```
curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh | bash
```

- Windows (run as administrator)
```
powershell -Command "Invoke-WebRequest 'https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.bat' -OutFile (Join-Path $env:TEMP 'install-qwen.bat'); & (Join-Path $env:TEMP 'install-qwen.bat')"
```

It is recommended to restart your terminal after installation to ensure environment variables take effect.

#### 2. Obtain a DeepSeek API Key

- Go to the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys) and create an API Key.
- Copy the key (it starts with `sk-`).

#### 3. Configure the API Key in Qwen Code

- Open Qwen Code with the following commands:
```
cd your-project
qwen
```

- Type `/auth` to configure authentication.
- On the "Select authentication method" screen, choose `API Key  Bring your own API key`.
- Then select `Custom API Key  For other OpenAI / Anthropic / Gemini-compatible providers`.
- On the next screen you will have two compatible options:

    - If you choose `OpenAI-compatible`, enter the following Base URL when prompted:
    ```
    https://api.deepseek.com
    ```
    - If you choose `Anthropic-compatible`, enter the following Base URL when prompted:
    ```
    https://api.deepseek.com/anthropic
    ```
- On the "API Key" page, enter the API Key you obtained above (starting with `sk-`).

- On the "Model IDs" page, you can enter the following model IDs, separated by commas:
```
deepseek-v4-flash,deepseek-v4-pro
```
- On the subsequent "Advanced Config" page, you can enable **"Enable thinking"** and **"Enable modality"** according to your needs.

- Finally, on the "Review" page, you can briefly inspect the `settings.json` generated from your configuration. If everything looks correct, press Enter to confirm.

#### 4. Once all settings are complete, you can start using Qwen Code right away.

#### 5. Visual Studio Code Extension

The VS Code extension (Beta) provides a native graphical interface integrated directly into the IDE, allowing you to view Qwen's code changes in real time for a more convenient Qwen Code experience. Search for `Qwen Code Companion` in the VS Code Marketplace, or install it via [this link](https://marketplace.visualstudio.com/items?itemName=qwenlm.qwen-code-vscode-ide-companion).
