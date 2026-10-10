[English](./atlarix.md) | [简体中文](./atlarix.zh-CN.md) · [← Back](../README.md)

# Integrate with Atlarix

Atlarix is an agent workstation desktop app (macOS, Linux, Windows) built by Norah Labs for the open-weight frontier labs — DeepSeek, Qwen, Kimi, and MiniMax. It supports BYOK with OpenAI-compatible providers, parallel sub-agents, MCP servers, and five work modes: Explore, Plan, Build, Debug, and Review.

- **Website:** <https://atlarix.dev>
- **Built by:** Norah Labs (<https://norahlabs.com>)

#### 1. Install Atlarix

Download the installer for your platform from [atlarix.dev](https://atlarix.dev). Available for macOS, Linux, and Windows.

After installation, sign in with Google or GitHub and open a project folder as your workspace — all chat runs inside that workspace.

#### 2. Add DeepSeek as a Provider

Atlarix connects to DeepSeek via its OpenAI-compatible API. Add your DeepSeek API key as a custom provider:

1. Open **Settings** (gear icon in the sidebar) → **AI**.
2. Under custom providers, add an **OpenAI-compatible** provider with these settings:
   - **Base URL:** `https://api.deepseek.com`
   - **API Key:** `<your DeepSeek API Key>`
   - **Models:** `deepseek-v4-pro`, `deepseek-v4-flash`

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Select the Model and Start Working

Once the provider is configured:

1. Open the model picker in the chat area and select **deepseek-v4-pro** or **deepseek-v4-flash**.
2. Choose a work mode — **Plan** to shape the work first, then **Build** to implement with the approval queue.
3. Type your task and send.

DeepSeek V4's full **1 million token** context window is available through Atlarix. For the best coding experience, toggle **Deep Think** in the chat input — Atlarix passes `reasoning_effort: "max"` to the DeepSeek API for the strongest reasoning on complex tasks.

#### 4. Headless CLI (Optional)

For CI pipelines and benchmarking, Atlarix provides a headless CLI that can target DeepSeek directly:

```bash
node /opt/atlarix/dist-headless/atlarix-headless.mjs \
  --workspace /path/to/repo \
  --prompt "Fix the failing test in src/auth.ts" \
  --provider-url https://api.deepseek.com \
  --model deepseek-v4-pro \
  --api-key "$DEEPSEEK_API_KEY"
```

The headless bundle auto-approves file and command operations. Use `--mode ask` for read-only exploration.
