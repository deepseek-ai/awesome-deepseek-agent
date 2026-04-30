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

##### API Key Preparation
 Go to [LangRouter](https://langrouter.ai/), register an account, save your API key. Note: Free trial available.

#### Running
```bash
# Start Langcli (interactive)
langcli

# Then, in the session:
hi
```
