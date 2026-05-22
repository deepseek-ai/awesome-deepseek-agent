[English](./leagent.md) | [简体中文](./leagent.zh-CN.md) · [← Back](../README.md)

# Integrate with LeAgent

LeAgent is a self-hostable, local-first platform for building LLM-powered office automation — conversational AI, visual workflows, and 100+ tools in one deployable stack. DeepSeek is the most thoroughly validated provider and is recommended for first use.

#### 1. Install LeAgent

**Prerequisites:** git, uv, Node.js 20+

Clone the repository and start with the launch script:

```
git clone https://github.com/vixues/LeAgent.git
cd LeAgent
./start.sh
```

This starts the backend on port 7860 and the frontend on port 5173.

Alternatively, use Docker:

```
cd LeAgent/deploy
cp .env.example .env
docker compose up -d --build
```

Or use the one-line installer:

```
curl -fsSL https://vixues.com.cn/install.sh | bash
```

#### 2. Configure DeepSeek as the LLM Provider

1. Open the LeAgent Web UI at `http://localhost:5173`.
2. Navigate to **Settings → Model Provider**.
3. Select **DeepSeek** from the provider list.
4. Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys).
5. Choose a model — `deepseek-v4-pro` for best quality or `deepseek-v4-flash` for faster responses.
6. Set **context window** to `1000000` (DeepSeek V4 supports up to 1M tokens).
7. Enable **Thinking Mode** and set reasoning effort to `max` for best results with `deepseek-v4-pro`.
8. Save the configuration.

#### 3. Get Started

- **Chat:** Open the Chat page to start a multi-turn conversation powered by DeepSeek.
- **Workflows:** Use the visual ReactFlow editor to build drag-and-drop automation workflows with DeepSeek as the reasoning engine.
- **Tools:** Explore the 100+ built-in tools (documents, web, data, code execution, databases, and more) that the agent can invoke during conversations.

For more information, see the [LeAgent documentation](https://github.com/vixues/LeAgent).
