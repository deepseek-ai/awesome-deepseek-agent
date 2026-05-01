[English](./mateclaw.md) | [简体中文](./mateclaw.zh-CN.md) · [← Back](../README.md)

# Integrate with MateClaw

<img src="./assets/mateclaw_preview.png" width="1024" border="1" />

> **Most AI tools die when their vendor has a bad day. Most forget you the moment the tab closes. Most give you a chatbox and call it a product.**

MateClaw is an open-source personal AI operating system. One JAR. Apache 2.0. Spring Boot 3.5 + Spring AI Alibaba under the hood. Same brain answers in the **web console**, the **desktop app**, the **embeddable widget**, the **Java plugin SDK**, and **eight IM channels** — DingTalk, Feishu, WeChat Work, WeChat, Telegram, Discord, QQ, Slack. Same memory. Same skills. Same tools. Different doors.

DeepSeek V4 plugs straight in — V4 Pro for hard reasoning, V4 Flash for fast turns, both with thinking-mode reasoning streamed alongside the answer and preserved across the conversation.

#### Why this exists

When a major LLM provider goes dark for hours, every team locked into a single vendor stares at a red error card. AI is becoming infrastructure. Infrastructure can't be tied to one supplier.

In MateClaw you drag DeepSeek, DashScope, OpenAI, Anthropic, Gemini, Kimi, Ollama, LM Studio, MLX into a priority chain. When the primary returns 401 or times out, the next picks up mid-sentence and the user sees the answer finish. A health tracker (`vip.mate.llm.failover.ProviderHealthTracker`) parks bad vendors in a cooldown window so they don't waste seconds on every turn.

You don't write a retry script. You drag.

#### The whole widget

- **Agent runtime** — **ReAct** for iterative reasoning, **Plan-and-Execute** for multi-step work. Built on Spring AI Alibaba's StateGraph: nodes for reasoning / action / observation / planning / step-execution, conditional edges between them. Dynamic context pruning, smart truncation, stale-stream cleanup — the boring stuff that makes long conversations actually work.
- **LLM Wiki** — drop in PDFs, markdown, scraped pages. The wiki digests them into linked pages with `[[wiki-style links]]` and per-sentence citations. Click a citation, see the source chunk. The difference between a warehouse and a library.
- **Memory lifecycle** — post-conversation extraction, scheduled consolidation, dreaming workflows that re-read the day. Plus per-workspace `AGENTS.md` / `SOUL.md` / `PROFILE.md` / `MEMORY.md` files. Memory you don't have to babysit.
- **Skills + MCP + Tool Guard** — `SKILL.md` packages from the ClawHub marketplace. MCP servers over stdio / SSE / Streamable HTTP. ACP endpoints register as Skill cards. An RBAC + approval-flow guard layer that pauses risky tool calls for review before they run. Capability needs boundaries.
- **Multimodal creation** — TTS, STT, image, music, video, Tencent Hunyuan 3D. Unified async pipeline streams progress over SSE.
- **Enterprise basics** — JWT auth. RBAC per agent / per model / per tool. Full audit trail. Flyway migrations that auto-heal on upgrade.

#### Install

Three paths. Pick the one that doesn't make you sigh.

**Desktop — no Java, no setup:**

Download from [GitHub Releases](https://github.com/matevip/mateclaw/releases). Bundles JRE 21. Double-click. Mac, Windows, Linux.

**Docker — production-style:**

```bash
git clone https://github.com/matevip/mateclaw.git
cd mateclaw
cp .env.example .env
docker compose up -d
```

Console at `http://localhost:18080`. Default login `admin` / `admin123` — change it.

**Source — for developers:**

```bash
git clone https://github.com/matevip/mateclaw.git
cd mateclaw/mateclaw-server
mvn spring-boot:run
```

Console at `http://localhost:18088`.

#### Add DeepSeek

In the admin console:

1. **Settings → Model Providers** → find **DeepSeek** → paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) → enable. Drag DeepSeek to the top of the failover chain to make it primary, or slot it after another provider as a fallback.
2. **Settings → Models** — two builtins are already there: **DeepSeek V4 Pro** (`deepseek-v4-pro`) and **DeepSeek V4 Flash** (`deepseek-v4-flash`). 1M context. Thinking-mode reasoning.
3. **Agents** → edit any agent → set its model to V4 Pro (hard reasoning) or V4 Flash (fast turns) → save.

That's the whole setup. Reasoning content streams alongside the answer and is preserved across the conversation, not thrown away after the turn.

#### Use it

- **Web / Desktop** — open the console, pick the agent, talk. SSE streaming; tool calls and reasoning render live.
- **IM channels** — under **Channels**, attach a webhook for any of the 8 supported platforms. Same agent. Same memory. Same skills.
- **Wiki** — under **Wiki**, create a knowledge base, upload raw materials, let the digester build linked pages with citations.
- **Skills** — under **Skills → Marketplace**, install or upload a Skill bundle. Loaded at runtime, no restart. Subject to Tool Guard approval.
- **Embed** — `mateclaw-webchat` is a one-`<script>` widget. Drop it on any site to expose a specific agent.

#### Notes

- For production, switch to MySQL via the `mysql` Spring profile. Put the DeepSeek key in your secret store, not in `.env`.
- Documentation: <https://claw.mate.vip/docs>
- Source: <https://github.com/matevip/mateclaw>
- Desktop downloads: <https://github.com/matevip/mateclaw/releases>

---

The point isn't the channel list. The point is that the AI on the other end remembers you, runs your tools, and reasons under your control — not in someone else's cloud. Plug DeepSeek V4 into it and you have an engine that's both fast and willing to think.

Same brain. Five doors. That's the whole idea.
