[English](./mini_agent.md) | [简体中文](./mini_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with mini-agent

[mini-agent](https://github.com/ftfw0621/mini-agent) is an open-source terminal coding agent written in TypeScript and modeled on Claude Code: Ink TUI, skills, MCP (stdio + HTTP), allow / ask / deny permissions, plan and auto modes, context compaction, and a non-interactive `-p` mode. It talks to `api.deepseek.com` by default. The npm package is `agent-from-zero`.

#### 1. Install Node.js

Install [Node.js](https://nodejs.org/en/download/) 20.6 or later.

#### 2. Set the API key and model

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then add it to your shell profile (`~/.zshrc` or `~/.bashrc`) together with the model:

```bash
export DEEPSEEK_API_KEY=sk-...
export MINI_AGENT_MODEL=deepseek-flash   # or deepseek-v4-pro for harder tasks
```

Run `source ~/.zshrc` or open a new terminal.

#### 3. Run it in your project

```bash
cd /path/to/my-project
npx agent-from-zero --effort max
```

- **Reasoning effort**: `--effort max` sends `reasoning_effort: "max"` with thinking enabled. Inside a session, use `/effort` to switch between `none`, `low`, `high` (the API default), and `max`. `reasoning_content` is passed back across tool calls automatically.
- **1M context**: the context window defaults to DeepSeek's 1M tokens, and compaction starts at 80%. No configuration is needed.
- **Switching models**: `/model` switches to another model the API serves for the current session.

Type `/help` to see all commands.
