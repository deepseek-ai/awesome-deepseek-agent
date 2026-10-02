# Integrate with Taishen

Taishen is a desktop AI workbench purpose-built for DeepSeek — a full GUI application (Electron) that turns your materials and ideas into structured deliverables, not just chat. It features a Commander-style agent engine with autonomous planning, sub-agent delegation, IM remote access (Feishu/WeChat/QQ), and an extension ecosystem built on open standards (agentskills.io Skills + MCP).

- **GitHub:** [https://github.com/EricXu20266/taishen](https://github.com/EricXu20266/taishen)

#### 1. Install Taishen

Download the latest release from [GitHub Releases](https://github.com/EricXu20266/taishen/releases):

- **Windows:** `taishen_setup_x.x.x.exe` (installer, recommended) or `taishen_x.x.x免安装.zip` (portable)
- **macOS:** `taishen_x.x.x.dmg`

> **System Requirements:** Windows 10+ / macOS 12+, 8 GB RAM, 500 MB disk.

After installation, launch Taishen. On first launch you'll see the settings panel.

#### 2. Configure DeepSeek

Taishen uses DeepSeek as its primary and best-tested provider. Configuration is done entirely through the GUI — no config files to edit.

**Add your API Key:**

1. Open **Settings** (gear icon in the sidebar).
2. Under **Provider Profiles**, DeepSeek is pre-configured — just paste your API Key.
3. Get your key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Model selection:**

Taishen ships with pre-tuned configurations for both DeepSeek V4 models:

| Model | Best For | Context | Thinking |
|-------|----------|---------|----------|
| `deepseek-v4-pro` | Deep research, paper writing, code development | 1M tokens | Max effort (enabled) |
| `deepseek-v4-flash` | Quick Q&A, lightweight tasks | 1M tokens | High effort (enabled) |

Both models are configured with `context_window: 1000000` and `max_tokens: 384000` by default. The reasoning effort map routes Taishen's thinking level selector directly to DeepSeek's `reasoning_effort` parameter (`xhigh` → `max`, `high` → `high`).

**Pricing (per 1M tokens, RMB):**

Taishen includes built-in pricing that matches DeepSeek's official rates. You can edit prices in Settings, and costs are tracked per session in real time.

| Model | Cache Hit | Cache Miss | Output |
|-------|-----------|------------|--------|
| `deepseek-v4-pro` | ¥0.025 | ¥3 | ¥6 |
| `deepseek-v4-flash` | ¥0.02 | ¥1 | ¥2 |

**Peak / Off-Peak Pricing (v1.1):** Taishen supports DeepSeek's peak/off-peak pricing strategy. During peak hours (Beijing time 09:00–12:00 and 14:00–18:00 on weekdays), a configurable multiplier (default 2×) is applied. Peak pricing is enabled by default and can be toggled in Settings.

**Optional providers:**

Taishen supports OpenAI, Mimo, and other OpenAI-compatible providers. You can also use **FlexDog** — a built-in sub-agent that dynamically switches models mid-session — to compare DeepSeek against other providers within the same conversation.

#### 3. First Run

After configuring your API Key:

1. Return to the main chat view.
2. Type a prompt or drag in a file (`.docx`, `.pdf`, `.pptx`, `.xlsx`, images).
3. Taishen's Commander agent will plan → execute → verify → deliver.

**Try a complex task** to see the full workflow — ask Taishen to research a topic, write a report, generate a PowerPoint deck, or refactor code across multiple files. The right-side panel shows real-time progress through each phase.

#### DeepSeek-Specific Optimizations

Taishen includes several DeepSeek-first optimizations not found in general-purpose clients:

**Cache-Optimized Prompt Architecture** — The system prompt and tool definitions are structured to maximize DeepSeek's prefix caching. In long-running sessions (200M+ tokens), cache hit rates stay at ~99%, keeping per-turn costs constant regardless of session length.

**DeepSeek-Native Thinking Format** — Taishen uses the `deepseek` thinking format natively, with proper `reasoning_content` passback on assistant messages. No workarounds needed — thinking mode works out of the box.

**1M Context by Default** — Both `deepseek-v4-pro` and `deepseek-v4-flash` are configured with the full 1M context window. Long documents, large codebases, and marathon sessions are first-class use cases.

**Cost Transparency** — Per-session token usage and estimated cost are displayed in the conversation header. Cache hit savings are tracked separately so you can see the real impact of prompt optimization.

#### Key Features (DeepSeek-Powered)

- **Commander Agent Engine** — Five-phase workflow (Plan → Todo → Execute → Verify → Done) with autonomous tool orchestration. The agent reads files, runs shell commands, searches the web, and validates its own output.
- **IM Remote Access** — Connect via Feishu, WeChat, or QQ. Your phone becomes a Taishen terminal with streaming replies, file transfer, and approval dialogs — all through DeepSeek.
- **Sub-Agent Delegation** — Spawn up to 3 sub-agents in parallel for code exploration, architecture design, content creation, and more. Each sub-agent has its own Skill set, memory, and MCP tools.
- **Skill Ecosystem** — Compatible with the [agentskills.io](https://agentskills.io/) open standard (used by Claude Code, Cursor, GitHub Copilot, and 35+ other tools). Install community Skills from GitHub/Gitee or let the AI create new ones on the fly.
- **MCP Protocol** — Connect external tools (web search, browser automation, academic databases) via Streamable HTTP, SSE, or stdio.
- **Document Pipeline** — Drag in Word, PDF, PPT, Excel files; AI reads, analyzes, and generates new documents in any format.
- **Three-Tier Sandbox** — L1 (approve every action) → L2 (auto-review, default) → L3 (full trust). All file edits are auto-backed up; all shell commands are risk-rated before execution.
