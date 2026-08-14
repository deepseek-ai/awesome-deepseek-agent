[English](./sandbase_harness.md) | [简体中文](./sandbase_harness.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek V4 with SandBase Harness

[SandBase Harness](https://github.com/sandbaseai/sandbase-harness) is an open-source agent runtime with persistent sessions, sandboxed tool execution, MCP tools, skills, audit, replay, and a local web console.

## Install SandBase Harness

Install Node.js 22 or later, then create a workspace:

```bash
mkdir my-sandbase-agents
cd my-sandbase-agents
npx managed-agents init
```

Set a DeepSeek API key without writing it into the workspace:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API key>"
```

Start the runtime:

```bash
npx managed-agents start
```

Open `http://127.0.0.1:3000/dashboard`.

## Configure DeepSeek V4

In the dashboard, open **Settings > Models**, switch to the JSON editor, and use:

```json
{
  "vendor": "openai_compatible",
  "base_url": "https://api.deepseek.com/v1",
  "api_key": "${DEEPSEEK_API_KEY}",
  "options": {
    "reasoning_effort": "max"
  }
}
```

Save and activate the settings. SandBase Harness forwards `reasoning_effort` to the OpenAI-compatible chat-completions request. `max` enables the strongest reasoning mode available for `deepseek-v4-pro`.

DeepSeek V4 supports up to 1 million tokens of context. SandBase Harness compacts long-running sessions automatically and does not expose a separate context-window setting, so no ineffective `context_window` key is needed.

## Create an Agent and Run the First Task

Create `agents/sandbase-coding-agent.yaml`:

```yaml
name: sandbase-coding-agent
model: deepseek-v4-pro
system: You are a careful coding agent. Inspect the repository, make focused changes, and verify them.
tools:
  - type: agent_toolset_20260401
```

Restart the runtime or run `npx managed-agents reload`, open the agent in the dashboard, create a session, and send a task such as:

```text
Inspect this repository, explain its architecture, and identify one small improvement with tests.
```

Use `deepseek-v4-flash` instead when lower latency is more important than maximum reasoning depth.

## Security Notes

- Keep `DEEPSEEK_API_KEY` in the runtime environment; do not commit it.
- The default local sandbox executes commands as your operating-system user and is intended for trusted development. Use the Docker or Kubernetes sandbox provider when you need a stronger isolation boundary.
