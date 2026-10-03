[English](./langcli.md) | [简体中文](./langcli.zh-CN.md) · [← Back](../README.md)

# Integrate with Langcli

[Langcli](https://langcli.com) is an AI coding assistant that supports CLI and Zed ACP Agent.

#### 1. Installation

##### Quick Install (Recommended)

For macOS, Linux and WSL users, run the following command to install Langcli:

```bash
bash -c "$(curl -fsSL https://assets.langcli.com/installation/install-langcli.sh)"
```

For Windows users, run the following command instead (Run as Administrator CMD):

```cmd
cmd /c "curl -fsSL -o %TEMP%\install-langcli.bat https://assets.langcli.com/installation/install-langcli.bat && %TEMP%\install-langcli.bat"
```
> **Note**: It's recommended to restart your terminal after installation to ensure environment variables take effect.

##### Manual Installation

Make sure you have Node.js 20 or later installed. Otherwise download it from [nodejs.org](https://nodejs.org/en/download) and install first.
```bash
npm i -g langcli-com
```

#### 2. Quick Start

##### API Key and Provider (recommended — DeepSeek Official)

Option A — DeepSeek Official (recommended)

1. Get a DeepSeek API Key: open [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys) and create or copy your key.
2. Configure Langcli to use DeepSeek via the Anthropic-compatible endpoint. Set the following environment variables:

```bash
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="<your DeepSeek API Key>"
export ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash[1m]"
```

Set the model to `deepseek-v4-pro[1m]` or `deepseek-v4-flash[1m]`. The `[1m]` suffix enables the full 1M context window. See the [Langcli docs](https://langcli.com/docs) for additional configuration options.

Option B — Third-party routers (optional)

Langcli users can also route requests through third-party services such as LangRouter. These are third-party offerings, **not maintained or endorsed by DeepSeek**. If you choose to use a third-party router, obtain credentials from that provider and follow their instructions. Use such services at your own risk — we recommend the official DeepSeek endpoint for best compatibility and security.

#### Running
```bash
# Start Langcli (interactive)
langcli

# Then, in the session:
hi
```
