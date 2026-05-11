[English](./xpro.md) | [简体中文](./xpro.zh-CN.md) · [← Back](../README.md)

# Integrate with Xpro

Xpro is an open-source AI-powered desktop IDE built with Electron, TypeScript, and Rust. It features an autonomous agent mode that reads/writes files, runs shell commands, and manages sub-agents — with full DeepSeek V4 support including thinking mode and the 1M-token context window.

- **GitHub:** <https://github.com/HopkeyEZ/Xpro>

#### 1. Install Xpro

**From source (requires Node.js 18+ and Rust 1.70+):**

```bash
git clone https://github.com/HopkeyEZ/Xpro.git
cd Xpro
npm install

# Build the Rust native module
cd native && npm install && npm run build && cd ..

# Build and launch
npm run build:main
npm start
```

**Or download a prebuilt Windows installer** from the [Releases](https://github.com/HopkeyEZ/Xpro/releases) page.

#### 2. Get a DeepSeek API Key

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure DeepSeek in Xpro

1. Launch Xpro
2. Click the **Settings** button in the toolbar
3. Set the following fields:

| Field | Value |
|-------|-------|
| Protocol | `OpenAI` |
| Base URL | `https://api.deepseek.com` |
| API Key | Your DeepSeek API key |
| Model | `deepseek-v4-pro` or `deepseek-v4-flash` |

Settings are saved to `~/.xpro/config.json` and persist across sessions.

#### 4. Enable Thinking Mode

In the Settings dialog, check the **Thinking Mode** checkbox to enable DeepSeek's reasoning mode. When enabled:

- The agent sends `thinking: { type: "enabled" }` with each request
- Reasoning content (`reasoning_content`) is automatically passed back in subsequent turns
- A thinking indicator appears in the chat when the model is reasoning

Set reasoning effort to `max` for the best coding experience with `deepseek-v4-pro`.

#### 5. Start Coding

1. Open a project folder via the **Open Folder** button
2. Type a task in the AI chat panel (e.g. "add error handling to all API routes")
3. The agent autonomously reads files, edits code, runs commands, and verifies results

Switch between modes using the model selector:

| Mode | What it does |
|------|-------------|
| **Ask** | Read-only Q&A. No file modifications. |
| **Agent** | Full autonomous mode. Reads, writes, runs commands, spawns sub-agents. |

#### Key Features with DeepSeek

| Feature | Description |
|---------|-------------|
| **1M context** | DeepSeek V4's full context window is available for large codebases |
| **Thinking mode** | Toggle chain-of-thought reasoning on/off from the settings UI |
| **Project memory** | Memories extracted from conversations are stored locally and recalled in future sessions |
| **Sub-agents** | Complex tasks are split across parallel child agents |
| **Visual annotation** | Screenshot your screen, draw annotations, and the AI edits the corresponding code |
| **File change tracking** | Every AI edit creates a checkpoint with diff view and one-click undo/redo |
| **AI change categorization** | File changes are automatically grouped by impact area (Frontend UI, Backend API, etc.) |
| **Rust-native search** | File traversal and full-text search powered by Rust via napi-rs |

#### Configuration Reference

All settings are stored in `~/.xpro/config.json`:

```json
{
  "openaiKey": "sk-your-deepseek-key",
  "openaiBase": "https://api.deepseek.com",
  "anthropicKey": "",
  "anthropicBase": "https://api.anthropic.com",
  "thinking": true
}
```

Any OpenAI-compatible endpoint can be used as the base URL (e.g. local Ollama, vLLM, LM Studio).
