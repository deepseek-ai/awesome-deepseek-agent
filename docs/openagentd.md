[English](./openagentd.md) | [简体中文](./openagentd.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenAgentd

[OpenAgentd](https://github.com/lthoangg/openagentd) is an open-source desktop cockpit for local AI agents. It runs a FastAPI sidecar and React UI locally, supports a lead-and-member agent team, and includes a built-in DeepSeek provider.

#### 1. Install OpenAgentd

For the desktop app, install with Homebrew on macOS:

```bash
brew install --cask lthoangg/tap/openagentd
```

Or download the latest macOS / Linux desktop build from the [OpenAgentd releases page](https://github.com/lthoangg/openagentd/releases/latest).

For the CLI / local web server:

```bash
uv tool install openagentd
openagentd init
openagentd
```

OpenAgentd serves the local UI at `http://localhost:4082`.

#### 2. Configure DeepSeek

In the desktop or web UI, open **Settings → Providers**, select **DeepSeek**, paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys), and choose `deepseek-v4-pro` or `deepseek-v4-flash`.

You can also configure the lead agent directly in `~/.config/openagentd/agents/openagentd.md`:

```yaml
---
name: openagentd
role: lead
model: deepseek:deepseek-v4-pro
temperature: 0.2
thinking_level: high
---
```

For coding mode, apply the same model setting to `~/.config/openagentd/agents/coding/openagentd.md`.

OpenAgentd maps `thinking_level` to DeepSeek's thinking mode fields. Use `deepseek-v4-pro` with `thinking_level: high` for stronger coding sessions, or `deepseek-v4-flash` for faster lower-cost runs. DeepSeek V4 supports a 1 million token context window; OpenAgentd does not require a separate context-window setting for the built-in DeepSeek provider.

#### 3. Start Using It

Launch OpenAgentd, start a new session, and send a message. In coding mode, OpenAgentd shows workspace files, tool calls, inline diffs, todos, and spawned team members in the same local UI while DeepSeek drives the agent loop.
