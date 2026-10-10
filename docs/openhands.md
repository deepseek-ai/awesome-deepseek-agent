[English](./openhands.md) | [简体中文](./openhands.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenHands

OpenHands is an open-source AI agent platform for software development. Its Agent Canvas web UI lets you configure LLM profiles, create agent profiles, and run coding agents in isolated workspaces. OpenHands supports any OpenAI-compatible API, making DeepSeek integration straightforward.

#### 1. Install OpenHands

**Prerequisites:** Node.js 22.12.x or later.

```shell
npm install -g @openhands/agent-canvas
```

Start the server:

```shell
agent-canvas
```

Access the web UI at [http://localhost:8000](http://localhost:8000).

For Docker-based installation (recommended for sandboxed execution), see the [OpenHands docs](https://docs.openhands.dev/overview/quickstart).

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure an LLM Profile for DeepSeek

In the Agent Canvas web UI:

1. Click the **Settings** icon (gear) in the sidebar.
2. Go to **LLM Profiles**.
3. Click **Add LLM Profile**.
4. Fill in the following fields:

| Field | Value |
|-------|-------|
| Name | `DeepSeek V4 Pro` (or any name you prefer) |
| Model | `deepseek/deepseek-v4-pro` |
| Base URL | `https://api.deepseek.com/v1` |
| API Key | Your DeepSeek API key |

**Important:** The model name must include the LiteLLM provider prefix (`deepseek/`). Using just `deepseek-v4-pro` without the prefix will result in an error.

**Context window:** DeepSeek V4 models support up to 1 million tokens of context. OpenHands will detect and utilize this automatically from the API response — no manual `max_input_tokens` setting is needed.

5. Click **Save**.

Optionally, add a Flash model profile for lighter tasks:

| Field | Value |
|-------|-------|
| Model | `deepseek/deepseek-v4-flash` |
| Base URL | `https://api.deepseek.com/v1` |
| API Key | (same key) |

#### 4. Start Coding

Click **New Conversation** in the sidebar, select your DeepSeek LLM profile, choose a workspace directory, and start prompting:

> Build a frontend-only TODO app in React. Store all state in localStorage.

OpenHands will write, edit, and run code autonomously inside the workspace.

#### Verify

Create a simple test conversation:

> Output your model name and version in one sentence.

The agent should respond identifying itself as `deepseek-v4-pro` from DeepSeek.

You can also check the LLM profile is active by going to **Settings → LLM Profiles** and confirming your DeepSeek profile shows as active.

#### Troubleshooting

- **"LLM Provider NOT provided"**: You used the model name without the `deepseek/` prefix. Change the model field to `deepseek/deepseek-v4-pro`.
- **401 or authentication errors**: Check your DeepSeek API key in the LLM profile settings.
- **402 or payment errors**: Check your DeepSeek Platform balance.
- **Connection refused**: The `agent-canvas` server is not running. Run `agent-canvas` in a terminal.

#### Resources

- [OpenHands](https://github.com/All-Hands-AI/OpenHands)
- [OpenHands Agent Canvas](https://github.com/OpenHands/agent-canvas)
- [OpenHands Docs](https://docs.openhands.dev/)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
