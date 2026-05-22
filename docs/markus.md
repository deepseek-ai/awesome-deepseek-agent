[English](./markus.md) | [简体中文](./markus.zh-CN.md) · [← Back](../README.md)

# Integrate with Markus

[Markus](https://www.markus.global/) is an open-source AI Digital Employee Platform — a full-featured web GUI for creating, managing, and deploying AI agents that work alongside your team. Every operation from configuring AI models to assigning tasks and reviewing work is done through the browser.

DeepSeek is a built-in provider in Markus — just set your API key and you're ready to go, no manual provider setup needed.

#### 1. Install & Start

Make sure you have [Node.js](https://nodejs.org/) and [pnpm](https://pnpm.io/installation) installed, then run:

```bash
# Set your DeepSeek API key first
export DEEPSEEK_API_KEY=your-api-key-here

# Clone and start Markus
git clone https://github.com/markus-global/markus.git
cd markus
pnpm install
pnpm dev
```

Your browser will open automatically at `http://localhost:8056` with the Markus admin GUI.

**Configure DeepSeek — two ways**:

- **Set env var before startup** (auto-detected): `export DEEPSEEK_API_KEY=your-key` — Markus loads it automatically on start.
- **Configure in the GUI** (no env var needed): Go to **Settings → LLM Providers**, find DeepSeek, and enter your API key. The GUI persists it for you.

Alternatively, for a global install:

```bash
npm install -g @markus-global/cli
markus start
```

Then set your DeepSeek API key via **Settings → LLM Providers** in the browser — no environment variable needed.

#### 2. Select DeepSeek for Your Agent

In the Markus GUI, creating an agent and using DeepSeek is just a few clicks:

1. Go to **Agents → Create Agent** in the sidebar
2. Give your agent a name (e.g. "DeepSeek Assistant")
3. Under **Model Provider**, select **DeepSeek**
4. Choose a model — `deepseek-v4-flash` (fast) or `deepseek-v4-pro` (powerful)
5. Click save — your agent is ready

You can also configure DeepSeek in **Settings → LLM Providers** anytime — the provider is pre-registered, just enter or update your API key.

#### 3. What Else Can You Do?

From the Markus dashboard you can:

- **Orchestrate multi-agent teams** — assign different DeepSeek models to different agents for specialized roles
- **Create structured tasks** — break work into subtasks with review workflows
- **Add skills** — equip agents with web search, browser automation, code analysis, and more
- **Configure governance** — set approval tiers, task limits, and review assignments

Everything runs in the browser. No CLI scripts, no manual provider setup. Just set your `DEEPSEEK_API_KEY` and go.

For more details, visit the [Markus GitHub repository](https://github.com/markus-global/markus).
