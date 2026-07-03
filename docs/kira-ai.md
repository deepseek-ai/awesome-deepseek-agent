[English](./kira-ai.md) | [简体中文](./kira-ai.zh-CN.md) · [← Back](../README.md)

# Integrate with KiraAI

[KiraAI](https://github.com/xxynet/KiraAI) is an open-source modular AI digital life platform that connects LLMs to multiple chat platforms (QQ, Telegram, WeChat, Discord). It features a WebUI for management, a plugin system, Agent capabilities with MCP support, and dedicated DeepSeek integration with thinking mode and reasoning effort control.

#### 1. Install KiraAI

##### Install via Scripts (Recommended)

Prerequisites: Python 3.10+ must be available in your PATH.

Download the latest source code from [GitHub Releases](https://github.com/xxynet/KiraAI/releases), then run:

```bash
# Windows
scripts\run.bat

# Linux / macOS
bash scripts/run.sh
```

The script automatically creates a virtual environment, detects the fastest pip mirror, installs dependencies, and starts KiraAI.

##### Install via Docker

```bash
docker pull xxynet/kira-ai:latest
docker compose up -d
```

Or clone the repository and build locally:

```bash
git clone https://github.com/xxynet/KiraAI.git --depth 1
cd KiraAI
docker compose up -d
```

KiraAI will be available at `http://localhost:5267`.

For more details, see the [KiraAI Documentation](https://docs.kira-ai.top/).

#### 2. Configure DeepSeek in KiraAI

Open the KiraAI WebUI at `http://localhost:5267` and log in.

**Add the DeepSeek Provider:**

1. Navigate to the **Providers** page in the sidebar.
2. Click **Add Provider** and select **DeepSeek**.
3. Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys) in the `API Key` field.
4. The `Base URL` defaults to `https://api.deepseek.com` — no change is needed.
5. Click **Save**.

**Add a Model:**

1. In the provider you just created, click **Add Model**.
2. Select a model from the auto-discovered list, or manually enter the model name:
   - `deepseek-v4-pro` — for complex reasoning, Agent tasks, and multi-step workflows
   - `deepseek-v4-flash` — for fast, lightweight responses
3. In the model settings, configure:
   - **Thinking Mode**: Enabled by default. This activates DeepSeek's chain-of-thought reasoning.
   - **Reasoning Effort**: Set to `max` for the best coding and Agent experience, or `high` for balanced performance.
4. Click **Save**.

**Set as Default Model:**

1. Go to **Settings** > **Models**.
2. Set `Default LLM` to the DeepSeek model you just configured.

#### 3. Get Started

Return to the chat interface and start a conversation. KiraAI will use the configured DeepSeek model for all interactions.

You can also connect chat platforms (QQ, Telegram, WeChat, Discord) in the **Adapters** settings to use KiraAI as a digital assistant on your preferred messaging app. See the [KiraAI Documentation](https://docs.kira-ai.top/) for platform setup guides.
