[English](./goink.md) | [简体中文](./goink.zh-CN.md) · [← Back](../README.md)

# Integrate with Goink

Goink is an open-source desktop AI novel-writing system for Windows, macOS, and Linux. It pairs a ReAct agent engine with a structured memory database — characters, foreshadowing, story arcs, locations, and reader perspective — plus offline semantic search, Git version control, and 30+ MCP tools. Built with Wails (Go + React), installable under 60 MB.

- **GitHub:** <https://github.com/sigpanic/goink>

#### 1. Install Goink

Download the installer for your platform from the [Goink releases page](https://github.com/sigpanic/goink/releases):

- Windows (`.exe`)
- macOS (`.dmg` — Apple Silicon)
- Linux (`.AppImage`)

Launch the application. On first run you will see the onboarding screen where you can choose your theme and configure a model provider.

#### 2. Configure the DeepSeek Provider

Open Goink and click the gear icon in the lower-left corner to open **Settings**.

1. In the **Model Provider** tab, select **DeepSeek** from the built-in providers list on the left.
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API Key** field. The API endpoint defaults to `https://api.deepseek.com/v1` — no change needed.
3. Toggle on the models you want to use. **`deepseek-v4-pro`** is recommended for maximum reasoning quality in novel writing; **`deepseek-v4-flash`** is a faster, more affordable option.
4. Click **Save** to confirm the configuration.

<div align="center">
<img src="./assets/goink_deepseek_config.png" width="720" border="1" />
</div>

#### 3. Start Writing

Goink's agent is conversation-driven:

1. Click **New Novel** in the sidebar, give it a title and genre, then click **Create**.
2. In the chat panel, start a conversation — describe your story idea, characters, or outline. Goink's ReAct agent will call tools to look up existing settings, search past chapters, and maintain story state as it writes.
3. DeepSeek V4 Pro's deep thinking mode is enabled by default in Goink. The agent uses structured chain-of-thought during writing and state maintenance — you can see the thinking stream inline in the chat UI.
4. With DeepSeek V4's **1 million token** context window, Goink can reference extensive novel context in a single session, keeping long-form narrative coherent across chapters.

#### 4. Going Further

- **Structured Memory.** After each chapter, Goink's agent automatically inspects and updates character traits, foreshadowing progress, story arc nodes, and reader-perspective tracking — all surfaced for your review via diff approval.
- **Offline Semantic Search.** Goink uses ONNX Runtime with a local BGE Chinese embedding model. Search "the first time the protagonist shows their power" and find relevant passages even with completely different wording — no network required.
- **Git Version Control.** Every AI conversation is auto-committed. All AI-generated changes are shown as diffs for you to accept or revert — full traceability for every word.
- **More Providers.** Goink ships with 7 built-in LLM providers (DeepSeek, GLM, Kimi, Qwen, Doubao, MiniMax, MiMo) and supports custom OpenAI-compatible endpoints.
