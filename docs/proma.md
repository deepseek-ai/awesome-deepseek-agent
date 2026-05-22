[English](./proma.md) | [简体中文](./proma.zh-CN.md) · [← Back](../README.md)

# Integrate with Proma

Proma is a local-first, open-source desktop AI agent for macOS and Windows. It bundles a multi-model **Chat** mode, a general-purpose **Agent** mode (built on the Claude Agent SDK), plus workspaces, Skills, MCP servers, memory, and chat-app bot bridges in a single client.

DeepSeek is a **first-class provider** in Proma: a DeepSeek channel is auto-provisioned on first launch, the 1M context beta is enabled automatically for `deepseek-v4-pro` / `deepseek-v4-flash`, and a single key drives both Chat and Agent modes. Combined with Proma's aggressive SubAgent orchestration and a desktop UI that surfaces every step of the run, this is one of the smoothest open-source paths to put DeepSeek V4 to real work — no terminal setup required.

- **GitHub:** <https://github.com/ErlichLiu/Proma>
- **Website:** <https://proma.cool>

#### 1. Install Proma

Download the installer for your platform from the [Proma Releases page](https://github.com/ErlichLiu/Proma/releases).

Available builds:

- macOS Apple Silicon (`Proma-x.y.z-arm64.dmg`)
- macOS Intel (`Proma-x.y.z.dmg`)
- Windows (`Proma-Setup-x.y.z.exe`)

After installing, launch Proma and finish the first-run environment check. Agent mode relies on a working local shell plus Git and Node.js / Bun, so make sure those are available on your `PATH`.

#### 2. Configure the DeepSeek Channel

Open **Settings → Channels** from the sidebar. Proma ships with a pre-created **DeepSeek** channel — you only need to fill in the API key.

1. Locate the **DeepSeek** entry in the channel list (created automatically on first launch). If it is missing, click **Add Channel** and choose **DeepSeek** from the provider dropdown.
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API Key** field. The **Base URL** is preset to `https://api.deepseek.com/anthropic` (DeepSeek's Anthropic-compatible endpoint) — leave it as is.
3. Confirm the **Models** list includes `deepseek-v4-pro` and `deepseek-v4-flash`. Both are seeded by default.
4. Toggle **Enabled** on, then click **Test Connection** to verify the key.

That is all the wiring needed. Proma will route DeepSeek through its Anthropic-compatible adapter for both Chat and Agent modes.

#### 3. Use DeepSeek in Chat Mode

Open the **Chat** tab in the sidebar, start a new conversation, and pick **DeepSeek V4 Pro** (or **DeepSeek V4 Flash**) from the model selector at the top of the input box.

Chat mode supports streaming responses, attachments (PDF, Office, images), Markdown / Mermaid / KaTeX / code highlighting, side-by-side comparison with other models, system prompts, and built-in web search — all working with DeepSeek out of the box.

#### 4. Use DeepSeek in Agent Mode

Open **Settings → Agent** and set the **Default Agent Channel** to your DeepSeek channel and **Default Model** to `deepseek-v4-pro`. Then switch to the **Agent** tab and start a new session.

Proma's Agent mode is built on `@anthropic-ai/claude-agent-sdk` and gives DeepSeek V4 a full agentic loop — tool use, plan mode, permission gating, and SubAgent dispatch — inside a desktop GUI:

- **1M context auto-enabled** for `deepseek-v4-pro` / `deepseek-v4-flash` (`context-1m-2025-08-07` beta).
- **Built-in sub-agents** — `explorer`, `researcher`, `code-reviewer` — that the system prompt actively delegates to, with complexity-aware routing across DeepSeek V4 Pro and V4 Flash. DeepSeek runs as an *orchestrator*, not just an answerer; long tasks never pollute the main context.
- **Workspace-scoped Skills, MCP, memory, files** — switch workspace to switch project context.
- **Plan mode, permission approvals, and live SubAgent activity** — all surfaced inline in the message stream.
- **Remote triggers** — kick off DeepSeek-powered Agent runs from Feishu / Lark, DingTalk, or WeChat groups.

#### 5. Why Proma is the Smoothest Open-Source Path for DeepSeek V4

- **Zero-config DeepSeek.** Preset channel, preset models, 1M context wired in code — paste the key and go.
- **One key, both modes.** The same DeepSeek channel powers Chat and a full agentic Agent in a single client.
- **Aggressive SubAgent orchestration.** Built-in `explorer` / `researcher` / `code-reviewer` plus a system prompt that actively delegates with complexity-aware routing across DeepSeek V4 Pro and V4 Flash — DeepSeek punches well above what a single context window can do alone.
- **GUI beyond terminal agents.** Real-time SubAgent activity, side-by-side Diff preview, multi-session parallel streaming, attachment preview, plan / permission UI, voice input, and Feishu / DingTalk / WeChat bot bridges — all in a desktop app.
- **Local-first.** Sessions, workspaces, and Skills live under `~/.proma/` as JSON / JSONL — easy to back up, easy to inspect.

Proma is fully open source ([Apache-2.0](https://github.com/ErlichLiu/Proma)) and welcomes Skills, MCP configs, and Agent workflow contributions that showcase what DeepSeek V4 can do.
