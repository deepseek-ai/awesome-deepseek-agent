[English](./taco.md) | [简体中文](./taco.zh-CN.md) · [← Back](../README.md)

# Integrate with Taco AI

Taco AI is an open-source desktop AI assistant for macOS and Windows built with Electron + React + TypeScript. It unifies multiple LLM providers in a single interface, with a built-in terminal, code editor, browser automation, image understanding, project memory, and MCP tool integration — giving DeepSeek a full operating environment on your desktop.

- **GitHub:** <https://github.com/Fushengfu/tacoai>
- **Download:** [macOS](https://store.huiyuanjia.net/Taco%20AI-0.3.10-arm64.dmg) · [Windows](https://store.huiyuanjia.net/Taco%20AI%20Setup%200.3.10.exe)

#### 1. Install Taco AI

Download the installer for your platform:

- **macOS** — `.dmg` (Apple Silicon)
- **Windows** — `.exe` (x64 NSIS installer)

Launch Taco AI after installation. On first launch you'll be prompted to log in.

#### 2. Configure the DeepSeek Provider

Click the gear icon in the lower-left corner to open **Settings**, then navigate to the **Model Provider** tab.

1. Find **DeepSeek** in the built-in provider list and select it.
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API Key** field.
3. Set **Context Window** to `1000000` to leverage DeepSeek V4's full 1M token context.
4. Set **Reasoning Effort** to `max` for the strongest reasoning on coding and complex tasks.
5. Toggle the **Vision** switch if you plan to use image understanding with DeepSeek V4's multimodal capabilities.
6. Click **Save** to apply the configuration.

Taco AI uses the OpenAI-compatible API endpoint and automatically maps the configuration to DeepSeek's `reasoning_effort` and `max_tokens` parameters.

#### 3. Start Chatting

Return to the main chat interface. Select **`deepseek-v4-pro`** (for complex reasoning and coding) or **`deepseek-v4-flash`** (for faster, lighter tasks) from the model selector at the bottom of the chat window.

Type your message and press Enter or click the send button. DeepSeek V4 runs with the full **1 million token** context window and `reasoning_effort: "max"` as configured — no per-message setup needed.

#### 4. Going Further

Once DeepSeek V4 is configured, you can use it across all of Taco AI's capabilities:

- **Terminal.** Taco AI can execute shell commands directly on your system. Ask DeepSeek to run builds, manage dependencies, or debug issues — it reads command output and iterates autonomously.
- **Code Editor.** Open any file and Taco AI's built-in Monaco editor highlights syntax with live diff previews. DeepSeek can read, write, and refactor code across your project.
- **Browser Automation.** Taco AI can control a Chromium browser to test web apps, fill forms, scrape data, or verify UI — all driven by DeepSeek's reasoning.
- **Image Understanding.** Paste or upload images and DeepSeek V4 will analyze them — screenshots, diagrams, medical reports, and more.
- **Project Memory.** Taco AI maintains a persistent SQLite-based memory across sessions. DeepSeek recalls past decisions, architecture notes, and task history to provide context-aware assistance.
- **MCP Tools.** Connect external tools via the MCP protocol to let DeepSeek access databases, APIs, and specialized services.
- **Plan & Execute.** For complex multi-step tasks, Taco AI proposes execution plans and waits for your confirmation before proceeding — keeping you in control.
