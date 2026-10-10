[English](./crabcode.md) | [简体中文](./crabcode.zh-CN.md) · [← Back](../README.md)

# Integrate with CrabCode

CrabCode (蟹码) is an AI coding assistant and one-person AI workspace built by Acosmi, available as a terminal-native TUI and a desktop GUI. Unlike most tools on this list, **DeepSeek-V4 Pro and DeepSeek-V4 Flash are built in out of the box** — sign in, pick a model, and start coding. No proxy setup or API-key wiring required.

- **Official site:** <https://acosmi.com/zh>
- **Releases (terminal TUI):** <https://github.com/acosmi/crabcode/releases/latest>

#### 1. Install CrabCode

**Terminal TUI — macOS / Linux** (auto-detects platform, verifies SHA-256, configures `PATH`):

```bash
curl -fsSL https://updates.acosmi.com/crabcode/install.sh | sh
```

**Terminal TUI — Windows** (run in PowerShell):

```powershell
irm https://updates.acosmi.com/crabcode/install.ps1 | iex
```

Verify:

```bash
crabcode --version
```

**Desktop GUI** — download the installer from the [official downloads page](https://acosmi.com/zh/downloads) (macOS / Linux), or from the [GitHub Releases](https://github.com/acosmi/crabcode/releases/latest) page (Windows).

#### 2. Sign in — DeepSeek is included

Sign up at <https://acosmi.com/zh>, then run `/login` inside CrabCode to activate your account:

```bash
crabcode
/login
```

New users get a free one-month Basic membership with **60 million Credits**, which already covers DeepSeek, Qwen3.7, MiniMax-M3, GLM-5.2 and more. DeepSeek-V4 Pro and DeepSeek-V4 Flash are part of the built-in model catalog — no API key needed.

#### 3. Switch to a DeepSeek model

Run `/model` in the TUI (or use the model picker in the GUI) and select:

- `deepseek-v4-pro` — the flagship model for complex coding tasks
- `deepseek-v4-flash` — the fast, cost-effective model (also the default)

DeepSeek V4 models support a **1M-token context window**. Thinking mode is enabled automatically for supported models. Cycle reasoning effort with `Tab`, or set it explicitly with `/effort` (`low` → `medium` → `high` → `max`) — use `max` for the best coding experience on DeepSeek-V4 Pro.

#### 4. First run

```bash
cd /path/to/my-project
crabcode
```

Or run a one-shot prompt without the interactive UI:

```bash
crabcode -p "Explain the code structure of this directory"
```

#### Optional: Bring your own DeepSeek API key

If you already have a DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), CrabCode also supports custom OpenAI-/Anthropic-compatible providers. Add DeepSeek as a custom provider (base URL `https://api.deepseek.com/v1`, model IDs `deepseek-v4-pro` / `deepseek-v4-flash`) from the model settings, and CrabCode will route requests to your own DeepSeek account.

#### Quick reference

| Command / key | What it does |
|---|---|
| `/login` | Sign in or switch account |
| `/model` | View and switch models |
| `/effort` | Set reasoning effort (low / medium / high / max) |
| `Tab` | Cycle reasoning effort |
| `Esc` | Interrupt the current turn |
| `/update` | Update CrabCode to the latest version |
