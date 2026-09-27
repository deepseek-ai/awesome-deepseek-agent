[English](./codelf.md) | [简体中文](./codelf.zh-CN.md) · [← Back](../README.md)

# Integrating Codelf

Codelf is a lightweight desktop IDE (Electron + React) with a built-in autonomous AI agent. You drive it in natural language to build projects, process documents, and automate the browser and desktop apps, while it also works as a full-featured code editor. Codelf ships with a **native DeepSeek provider** — just pick the DeepSeek type in settings and paste your API key. No Base URL hacks or compatibility shims required.

- **GitHub:** <https://github.com/Liuchun-oss/codelf-agent>

#### Key Features

- **Multi-Agent Team Rooms**: Create AI teams (product squad, writing group, brainstorm panel) where each seat has its own persona, model, and tool permissions. The host auto-routes speaking turns with three collaboration strategies: host-routed, round-robin, and free.
- **Browser Automation**: Built-in Playwright-powered browser — the agent navigates, clicks, fills forms, and takes screenshots autonomously, handling login-gated or captcha pages.
- **Desktop Automation**: Control Windows / macOS desktop apps via accessibility APIs — click, type, drag, send shortcuts, and more.
- **Scheduled Tasks**: Cron / interval / one-shot scheduling with WeChat push delivery — run 24/7 unattended.
- **Local RAG Knowledge Base**: Import documents and query via semantic search across PDFs, Markdown, Office files, and more.
- **Skills Ecosystem**: Dozens of built-in skills (product design, document conversion, PPTX / DOCX / PDF processing, etc.) plus community skill installation.
- **MCP Protocol + Plugin System**: Full MCP support and installable Codex / Claude community plugins.
- **Plan Mode + Checkpoint Rollback**: Research complex tasks in read-only Plan mode before execution; every turn has a checkpoint you can roll back.
- **WeChat Integration**: Chat with your agent from your phone after binding WeChat; get push notifications when tasks complete.
- **Persistent Memory**: Cross-session knowledge accumulation — the agent learns your project conventions over time.

#### 1. Install Codelf

Codelf runs on Windows and macOS. Download a prebuilt package or run from source.

**Option A: Download a prebuilt package**

Grab the package for your platform from the [Releases page](https://github.com/Liuchun-oss/codelf-agent/releases):

- Windows: NSIS installer or portable directory build
- macOS: dmg (arm64 / x64)

**Option B: Run from source**

- Install [Node.js](https://nodejs.org/en/download/) 18+.
- Windows users should install [Git for Windows](https://git-scm.com/download/win).
- Clone the repository, install dependencies, and start:

```bash
git clone https://github.com/Liuchun-oss/codelf-agent.git
cd codelf-agent
npm install
npm run dev
```

#### 2. Configure Codelf to use DeepSeek

Open **Settings → AI** inside the app, create a new profile, and fill in the fields:

| Field           | Value                                    |
| --------------- | ---------------------------------------- |
| Type            | `DeepSeek`                               |
| Base URL        | `https://api.deepseek.com` (default)     |
| Model           | `deepseek-v4-pro`                        |
| API Key         | `<your DeepSeek API key>`                |
| Context window  | `1M` (1,000,000 tokens)                  |

Get your DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Click **Test connection** to verify, then **Save** and **Set as active**.

#### Recommended settings

- **Context window**: choose `1M` from the dropdown to take full advantage of DeepSeek V4's 1-million-token context.
- **Thinking mode**: enable thinking and set the reasoning effort to `max` for the best coding experience.
- **Model roles** (optional): create a second profile with `deepseek-v4-flash` for chat and high-frequency completion to save cost, and switch back to `deepseek-v4-pro` for complex tasks.
- **Tab completion (FIM)**: enable "Tab completion (FIM)" in the DeepSeek profile if you want inline completions.

> Codelf optimizes how conversations are organized to produce stable cache keys, significantly improving DeepSeek's prompt-cache hit rate and cutting cost noticeably over long coding sessions.

#### Pricing reference

| Model | Input / M tokens | Output / M tokens | Cache Hit / M tokens |
|-------|-----------------|-------------------|----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |

> The pricing above is a reference snapshot. Use the latest values from the [official DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing).

#### 3. Use Codelf

Once configured, describe what you want in the AI chat panel in plain language. Codelf autonomously reads and writes files, runs terminal commands, searches for information, and calls tools to complete multi-step tasks. For complex work, start in the read-only Plan mode to research an approach, confirm it, then execute — every turn has a checkpoint you can roll back.
