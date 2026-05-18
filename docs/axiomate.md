[English](./axiomate.md) | [简体中文](./axiomate.zh-CN.md) · [← Back](../README.md)

# Integrate with Axiomate

Axiomate is a multi-provider AI agent CLI that lets you chat, code, and control your computer — all from the terminal. It connects to DeepSeek, OpenRouter, SiliconFlow, ollama, vLLM, Anthropic, and more via a single unified config. For DeepSeek V4, Axiomate provides an interactive TUI wizard for zero-friction setup, automatic `reasoning_content` round-trip across tool calls, and UIA/AX-based computer use with Set-of-Mark overlays designed for text-only models.

## 1. Install

**Prerequisites:** Node.js 20+, Git. Windows also needs Visual Studio 2022 Build Tools (auto-installed by bootstrap).

Download the latest release from [GitHub Releases](https://github.com/axiomates/axiomate-agent/releases/tag/0.6.2), or build from source:

```bash
git clone https://github.com/axiomates/axiomate-agent.git
cd axiomate-agent
npm run bootstrap   # installs pnpm + Bun + Rust + deps, builds all workspaces
pnpm run start      # launch Axiomate
```

## 2. Configure DeepSeek (Interactive TUI)

### First Run — Onboarding Wizard

The first time you launch Axiomate with no models configured, a multi-step TUI wizard guides you through setup:

| Step | Field | What to enter for DeepSeek |
|------|-------|---------------------------|
| 1 | Protocol | **OpenAI Chat Completions** |
| 2 | API base URL | `https://api.deepseek.com` |
| 3 | API key | Your key from [platform.deepseek.com](https://platform.deepseek.com/api_keys) (masked input) |
| 4 | Model ID | `deepseek-v4-pro` or `deepseek-v4-flash` |
| 5 | Context window | `1000000` (1M tokens) |
| 6 | Image input support | **No** — DeepSeek V4 is text-only |
| 7 | Vendor template | `Auto-detect` (auto-selects `openai-chat-deepseek-official`) |
| 8 | Reasoning depth | **High** or **Max** (DeepSeek V4 Pro only supports these two levels) |

After verification succeeds, the config is saved to `~/.axiomate.json` and you're ready to go.

### Add More Models Later — `/model add`

Inside the TUI, type `/model add` to re-enter the same wizard and add another model (e.g., `deepseek-v4-flash` for cost-efficient iteration). The new model becomes active immediately. Switch between models anytime with `/model`.

### Manual Config (Optional)

You can also edit `~/.axiomate.json` directly:

```jsonc
{
  "models": {
    "deepseek-v4-pro": {
      "model": "deepseek-v4-pro",
      "protocol": "openai-chat",
      "baseUrl": "https://api.deepseek.com",
      "apiKey": "sk-...",
      "contextWindow": 1000000,
      "supportsImages": false,
      "thinking": { "enabled": true, "effort": "max" }
    }
  },
  "currentModel": "deepseek-v4-pro"
}
```

## 3. First Run

```bash
cd /path/to/my-project
axiomate
```

Axiomate enters the project directory, loads your DeepSeek model, and starts an agentic coding session with file editing, shell execution, grep, and more — all powered by DeepSeek V4's 1M context window and extended reasoning.

## 4. Computer Use with UIA/AX (for Text-Only Models)

DeepSeek V4 does not support vision input, but Axiomate's computer-use layer compensates with **UIAutomation / Accessibility (UIA/AX) bindings** and **Set-of-Mark (SOM) overlays**:

- **`screenshot`** — captures the screen with coordinate rulers so the model can reason about spatial layout from text descriptions
- **`zoom`** — captures a region and overlays numbered SOM markers on every detected UI element, letting the model reference elements by index instead of pixel coordinates
- **UIA element detection** (Windows) — uses native UIAutomation to identify buttons, text fields, menus, and other controls with pixel-accurate bounding boxes
- **Accessibility tree** (macOS) — uses the AX API for equivalent element discovery

This means DeepSeek V4 Pro can drive desktop applications — clicking, typing, scrolling, reading UI state — without needing a vision model. The SOM overlays translate visual information into structured text that reasoning models handle well.

## Resources

- [Axiomate GitHub](https://github.com/axiomates/axiomate-agent)
- [DeepSeek Platform](https://platform.deepseek.com/) — get an API key
- [DeepSeek API Docs](https://api-docs.deepseek.com/) — model reference
