[English](./synergy.md) | [简体中文](./synergy.zh-CN.md) · [← Back](../README.md)

# Integrate with Synergy

Synergy is an open-source AI agent workspace that keeps sessions, agents, files, Browser, tools, MCP servers, and automation connected in one runtime, usable from the Web workbench, Desktop app, and CLI. DeepSeek is a built-in provider — you only need a [DeepSeek API Key](https://platform.deepseek.com/api_keys).

#### 1. Install Synergy

Desktop users on Linux, Windows, or macOS can download the desktop installer directly from [GitHub Releases](https://github.com/SII-Holos/synergy/releases/latest).

Headless users, or users who need the CLI, can install with:

```
curl -fsSL https://raw.githubusercontent.com/SII-Holos/synergy/main/install | bash
```

Or install via npm:

```
npm install -g @ericsanchezok/synergy --registry https://registry.npmjs.org
```

#### 2. Configure DeepSeek

Desktop users can open Synergy directly. CLI users can open the web workbench with:

```
synergy start
synergy web
```

Open the Synergy workbench, go to **Settings**, select **Providers**, click **Add provider**, and enter your DeepSeek API Key under `deepseek`.

#### 3. Use DeepSeek V4

In **Settings**, open **Models**, set `deepseek/deepseek-v4-pro` as the default model, and select the **max** thinking effort.

Notes:

- The built-in `deepseek` provider already points at `https://api.deepseek.com` with an OpenAI-compatible transport — no base URL configuration is needed.
- DeepSeek V4 enables thinking mode by default (default effort `high`). Synergy exposes the declared efforts as model variants; the `max` variant sends `reasoning_effort: "max"` for the best coding experience.
- DeepSeek V4 supports a 1M-token context window.
- Settings changes are watched automatically — no restart is needed; after saving, the next request uses the new configuration.

#### 4. Get Started

Start the runtime and open the workbench, and you're ready to go.
