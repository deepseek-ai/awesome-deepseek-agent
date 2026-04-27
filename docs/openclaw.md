[English](./openclaw.md) | [简体中文](./openclaw.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenClaw

OpenClaw is an open-source personal AI assistant that can connect to popular chat tools like Feishu and WeChat, and can be extended through Skills.

#### 1. Install OpenClaw

Linux / Mac users, run the following command from the [OpenClaw install script](https://openclaw.ai/install.ps1) to install:

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

Windows users, run the following command from the [OpenClaw install script](https://openclaw.ai/install.ps1) to install:

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

#### 2. Configure the Default Model in OpenClaw

After the initial installation, you will automatically enter the setup phase. Users who have already installed OpenClaw can enter the configuration phase via the `openclaw onboard --install-daemon` command.

- When prompted: `I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?` Select **Yes**.
- When prompted: `Setup mode` It is recommended to select **QuickStart**.
- When prompted: `Model/auth provider` Select **DeepSeek**.
- When prompted: `Enter DeepSeek API key` Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys).
- When prompted: `Default model` Navigate to **Enter model** and enter the model name (`deepseek-v4-pro` or `deepseek-v4-flash`).
- For the remaining configuration (message channels, Skills, etc.), configure as needed. Beginners can select **Skip for now**.

#### 3. Get Started

Open the Web UI and interact on the Chat page:

```
openclaw dashboard
```

Open the TUI in the terminal:

```
openclaw tui
```

Chat with OpenClaw in the terminal:

```
openclaw terminal
```
