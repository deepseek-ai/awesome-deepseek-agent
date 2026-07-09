[English](./tianshu.md) | [简体中文](./tianshu.zh-CN.md) · [← Back](../README.md)

# Integrate with 天枢 (Tianshu)

天枢 (Tianshu) is an open-source agentic coding assistant that runs in the terminal and as a desktop app. It ships with a built-in DeepSeek provider preset, so you can connect to `api.deepseek.com` without manual endpoint configuration.

#### 1. Install Node.js

- Install [Node.js](https://nodejs.org/en/download/) 24+.
- Windows users also need [Git for Windows](https://git-scm.com/download/win).

#### 2. Install Tianshu TUI

Install the CLI globally from npm:

```bash
npm install -g tianshu-tui
```

#### 3. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Export it in your shell:

```bash
export DEEPSEEK_API_KEY="sk-..."
```

On Windows (PowerShell):

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

#### 4. Configure Tianshu for DeepSeek

In the TUI, run:

```bash
rivet config setup deepseek
```

Or open the desktop app, go to **Settings → Provider**, and select **DeepSeek**.

#### 5. Start coding

Enter your project directory and run:

```bash
rivet
```

Tianshu has built-in support for **DeepSeek-V4-Pro** and **DeepSeek-V4-Flash**. Both models support up to 1M context tokens. V4-Pro is configured with `reasoningEffort: max` and up to 384K output tokens for complex deep-reasoning tasks; V4-Flash offers fast, cost-efficient iteration.

<div align="center">
<img src="https://raw.githubusercontent.com/huiliyi37/Tianshu-Tui/main/assets/tianshu-banner-dark.jpg" width='640' />
</div>
