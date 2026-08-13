[English](./hermes.md) | [简体中文](./hermes.zh-CN.md) · [← Back](../README.md)

# Integrate with Hermes Agent

Hermes is a self-improving AI agent built by Nous Research. It includes a built-in learning loop: it creates skills from experience, improves them during use, persists knowledge, and builds an evolving model of your preferences across sessions.

#### 1. Install Hermes

##### Quick Install

Get Hermes Agent up and running in under two minutes with the one-line installer.

###### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

The only prerequisite is Git. The installer automatically handles everything else.

For more installation instructions, please refer to the [Hermes installation page](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

###### Windows (native)

Hermes also ships a native Windows desktop app and a PowerShell install path:

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

The desktop app provides a chat surface, terminal/preview panes, voice support (STT/TTS), and background task scheduling (cron jobs) on top of the same agent core.

#### 2. Run and Configure

Reload your shell and start Hermes configuration:

- Execute the `hermes setup` command
- Choose the Quick Setup option
- When prompted for the model provider, select **DeepSeek**
- Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- Enter the Base URL as `https://api.deepseek.com`
- Select the `deepseek-v4-pro` model
- Continue with the remaining options

#### 3. Choose a Model

| Model | Strengths | Use when |
| ----- | --------- | -------- |
| `deepseek-v4-pro` | Deepest reasoning, best agentic planning | Default; complex multi-step tasks, long-horizon autonomy |
| `deepseek-v4-flash` | High throughput, low cost | Bulk/batch jobs, cron automation, high-frequency tool calling |

Model choice is configurable per session via `hermes config`, so it is easy to switch without re-running setup.

#### 4. Real-World Usage Example

Beyond interactive chat, Hermes shines as a background agent. A practical pattern is a fully automated pipeline driven by scheduled jobs:

1. **Skills** — capture a working procedure once (e.g. "produce a short video: script → TTS → assets → ffmpeg → publish"); the agent reuses it on every later run.
2. **Cron jobs** — schedule the workflow with `hermes cron` (e.g. daily content production at a fixed time).
3. **Human-in-the-loop** — gate irreversible actions (publishing) behind an approval step; the agent verifies its own output before delivering.

An example open-source pipeline built on this pattern with DeepSeek as the planning brain: [douyin-agent-pipeline](https://github.com/xiaozhang-iu/douyin-agent-pipeline) (TTS → asset retrieval → music research → ffmpeg compose → CDP publish, fully automated with a review gate).

#### 5. Multilingual & Voice

Hermes supports Chinese (and other languages) end-to-end: Chinese STT for voice input, Chinese TTS for spoken replies, and Chinese prompt conventions — useful when driving the agent hands-free.

