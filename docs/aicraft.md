[English](./aicraft.md) | [简体中文](./aicraft.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with AICraft

AICraft is a Windows desktop AI capability launcher that manages LLM Skills, MCP tools, RAG, and memory through a visual UI — think of it as a "Minecraft launcher for AI capabilities." It has **built-in one-click DeepSeek setup** with native support for DeepSeek V4 Pro and V4 Flash via the Anthropic-compatible API endpoint.

- **GitHub:** <https://github.com/Easlie114514/AICraft>
- **Releases:** <https://github.com/Easlie114514/AICraft/releases>

## Why AICraft + DeepSeek

AICraft is DeepSeek-native. It was built from the ground up for the DeepSeek API, using the Anthropic SDK to connect through `api.deepseek.com/anthropic`. This gives you:

- **One-click setup** — paste your API key once, both `deepseek-v4-pro` and `deepseek-v4-flash` are configured automatically
- **Native thinking mode** — toggle DeepSeek's reasoning process on/off with the built-in "Deep Think" switch
- **Auto model routing** — the "Auto" model option intelligently routes simple queries to Flash and complex tasks to Pro
- **Web search** — leverage DeepSeek's server-side web search capability directly from the chat interface
- **Real-time token billing** — per-session and lifetime token usage tracking with DeepSeek pricing

#### 1. Download and Install AICraft

Download the latest portable EXE from the [Releases page](https://github.com/Easlie114514/AICraft/releases).

AICraft runs on **Windows 10/11**. No installation required — just extract and run `AICraft.exe`.

#### 2. One-Click DeepSeek Setup

1. Launch AICraft and navigate to the **Model** tab (the 7th tab in the sidebar).
2. Click the **DeepSeek** quick-setup card.
3. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the API Key field.
4. Click **Save**.

Two model configurations are created automatically:
- `deepseek-v4-pro` — for complex reasoning, coding, and multi-step tasks
- `deepseek-v4-flash` — for quick responses, simple queries, and background tasks

AICraft connects via the Anthropic-compatible endpoint (`https://api.deepseek.com/anthropic`), which enables native thinking mode support and server-side web search.

#### 3. Enable Deep Think (Reasoning Mode)

In the **Chat** tab, toggle the **Deep Think** switch to enable DeepSeek's reasoning process. When enabled, AICraft displays a "Thinking..." indicator and shows the model's reasoning steps, with a summary like "Thought for X.X seconds."

Deep Think is automatically routed to `deepseek-v4-pro` when the Auto model selector is active.

#### 4. Start Chatting

Switch to the **Chat** tab, select `Auto` (recommended), `deepseek-v4-pro`, or `deepseek-v4-flash` from the model dropdown, and start chatting. You can:

- Enable **MCP tools** (file manager + code executor) for agentic capabilities
- Toggle **RAG** for document-grounded answers
- Enable **Web Search** for real-time information
- Load **Skills** and **Roles** to customize the AI's behavior

> **Tip:** Keep the model on `Auto` — AICraft will route simple messages to Flash (saving cost) and automatically switch to Pro when you ask complex questions, use MCP tools, or enable RAG/Deep Think.
