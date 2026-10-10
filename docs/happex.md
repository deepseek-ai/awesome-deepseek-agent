[English](./happex.md) | [简体中文](./happex.zh-CN.md) · [← 返回](../README.md)

# Connecting to Happex

> **Happex Desktop AI Engineering Platform** — A cross-platform desktop application for AI-assisted software engineering, supporting task management, tool execution, and multi-vendor models.



## Download & Installation

### System Requirements

| Platform | Minimum Version |
| -------- | --------------- |
| macOS | 10.15+ (Catalina) |
| Windows | Windows 10+ |

### Download

1. Visit the [GitHub Releases page](https://github.com/huangsongyuan/happex/releases/latest)
2. Download the installer for your platform:
   - **macOS (Apple Silicon)**: `happex_<version>_aarch64.dmg`
   - **macOS (Intel)**: `happex_<version>_x86_64.dmg`
   - **Windows**: `happex_<version>_x64-setup.exe` (NSIS installer)
3. Open/run the installer and follow the prompts to complete installation


## Updating

### Auto-Update (Recommended)

Happex has a built-in auto-update mechanism based on Tauri Updater.

1. Open the app, go to **About** (gear icon → "About")
2. Click **"Check for Updates"**
3. If a new version is found:
   - The version number and release notes are displayed
   - Click **"Install Now"**
4. A progress bar is shown during download
5. After download completes, the app automatically restarts to apply the update

### Manual Update

Download the latest installer from [GitHub Releases](https://github.com/huangsongyuan/happex/releases/latest) and install over the existing version.


## DeepSeek Provider Configuration

Get your API Key from the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys).
Get the URL and configuration instructions from the [DeepSeek Open Platform Model Documentation](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/).

### Page Configuration (UI)

#### Adding a Provider

1. Go to **Settings** → **Provider & Model Settings**
2. Click the **+** button in the top-right corner of the provider panel
3. Fill in the form:
   - **Provider Type**: Select OpenAI Compatible or Anthropic
   - **Display Name**: A human-readable label (e.g., "My DeepSeek")
   - **Base URL** (OpenAI protocol: `https://api.deepseek.com/v1`;
   - Anthropic protocol: `https://api.deepseek.com/anthropic`)
   - **API Key**: Your API key (stored in the system keychain)
4. Click **"Add Provider"**

#### Editing a Provider

- Click the **edit (pencil)** icon next to a provider in the list
- You can update the display name, Base URL, and API key
- The API key field in edit mode is optional — leave it empty to keep the existing key


#### Deleting a Provider

Click the **trash** icon next to a provider. Deleting a provider also removes all model configurations under it.



## Model Configuration

Each provider account can have multiple model configurations. Models are managed per-provider and can be set as the global default model.

### Page Configuration (UI)

#### Adding a DeepSeek Model

1. Select a provider from the left-hand list
2. Click **"Add Model"** in the top-right of the model panel
3. Fill in the form:
   - **Model ID**: The exact model identifier sent to the API (e.g., `deepseek-v4-pro`, `deepseek-v4-flash`)
   - **Display Name**: A human-readable label (e.g., "deepseek-v4-pro", "deepseek-v4-flash")
   - **Context Window**: Maximum context length in tokens (refer to DeepSeek model documentation, recommended value: 1000000)
   - **Max Output Tokens**: Maximum output length in tokens (refer to DeepSeek model documentation, recommended value: 384000)
   - **Capabilities**: Toggle each capability on/off:
     - `chat` — Conversational chat
     - `tool_use` — Function/tool calling
     - `streaming` — Streaming responses
     - `vision` — Image input support
     - `reasoning` — Extended reasoning/thinking
     - `embedding` — Embedding generation
4. Click **"Add Model"**

#### Setting a Default Model

- Click the **star** icon next to a model to set it as the default
- The default model is used for newly created tasks
- Only one model can be the default at a time

#### Editing a Model

Click the **edit (pencil)** icon next to a model in the table to update its parameters.

#### Deleting a Model

Click the **trash** icon next to a model to remove it.


## Frequently Asked Questions

### "No model selected" Error

1. Go to **Settings** → **Provider & Model Settings**
2. Ensure at least one provider is configured
3. Add at least one model configuration under the provider
4. Click the **star** icon to set a default model
---
