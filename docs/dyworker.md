[English](./dyworker.md) | [简体中文](./dyworker.zh-CN.md) · [← Back](../README.md)

# Integrate with DYWorker

DYWorker is a local AI work assistant for everyday office tasks. Pick a folder as your workspace, describe a goal in plain language, and the assistant breaks it down and carries it out step by step — reading documents, drafting files, generating Word/Excel output, and operating desktop apps, always asking for confirmation before risky actions. All data stays on your machine.

![DYWorker main interface](./assets/dyworker-main-interface.png "DYWorker main interface")

- **GitHub:** https://github.com/richardguancn/dyworker
- **Platforms:** macOS (Intel & Apple Silicon), Windows 10/11, and Linux desktops (including Kylin V10, ARM64)

#### 1. Install DYWorker

Download the latest installer for your platform from the [DYWorker Releases page](https://github.com/richardguancn/dyworker/releases):

- **macOS**: `.dmg` or `.zip`
- **Windows**: `setup.exe` (per-user install, no admin rights required)
- **Linux (ARM64 / Kylin V10)**: `.AppImage` or `.deb`

To run from source (requires Node.js 22+ and npm 10+):

```bash
git clone https://github.com/richardguancn/dyworker.git
cd dyworker
npm ci
npm run dev:electron
```

#### 2. Configure the DeepSeek Provider

On first launch, pick an identity profile ("General" or "Government"), then open **Settings → Model** and configure a model connection:

- **API endpoint**: `https://api.deepseek.com`
- **Model name**: `deepseek-v4-flash`
- **API key**: get one from the [DeepSeek Platform](https://platform.deepseek.com/api_keys)

DYWorker ships with a built-in **DeepSeek V4 Flash** preset covering the full **1M-token context window**, and talks to DeepSeek through the Responses API. DeepSeek's thinking mode stays on by default, so the full reasoning quality of V4 Flash is available without any extra configuration. API keys are stored encrypted via the system secure storage — never written to disk in plaintext.

![Model configuration in Settings](./assets/dyworker-model-config.png "Model configuration in Settings")

To use images with DeepSeek V4 Flash, fill in an OpenAI-compatible vision service (address, model name, and key) in the same settings page. DYWorker sends the image to the vision service to produce a description, then hands it to DeepSeek V4 Flash for analysis.

Other OpenAI-compatible providers (Qwen, Zhipu, or an in-house service) work the same way — just point the endpoint, model name, and key. Multiple model configurations can be saved and switched freely.

#### 3. Run and Assign Tasks

Start DYWorker, choose a workspace folder, and describe what you need — for example: *"Read this PDF and turn it into a one-page Word summary."* The assistant will plan the steps, execute them, and save real files into your workspace.

- Risky commands and changes to your desktop ask for confirmation first; all file, command, network, and tool activity is logged for audit.

  ![Risk approval dialog](./assets/dyworker-risk-approval.png "Risk approval dialog")

- Long tasks keep running in the background: DYWorker supports scheduled wake-ups (1 minute to 12 hours) and resumes interrupted tasks automatically.
- DYWorker remembers stable preferences and project rules (five types of long-term memory), and repeated multi-step workflows can be saved as reusable templates.
- Optional chat channels let you send tasks and receive results from your phone via QQ official bots or WeChat ClawBot.
