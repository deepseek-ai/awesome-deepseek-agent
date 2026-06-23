[English](./rikkahub.md) | [简体中文](./rikkahub.zh-CN.md) · [← Back](../README.md)

# Integrate with RikkaHub

RikkaHub is a native Android LLM chat client (Kotlin + Jetpack Compose + Material 3) that unifies OpenAI, Google Gemini, Anthropic Claude, and any OpenAI-compatible endpoint behind a single interface — with MCP, multimodal input, web search, prompt variables, message branching, and a proot-based Linux agent workspace.

- **Website:** <https://rikka-ai.com>
- **Docs:** <https://docs.rikka-ai.com>
- **GitHub:** <https://github.com/rikkahub/rikkahub>

#### 1. Install RikkaHub

Pick one of the official channels:

- **Website (recommended):** <https://rikka-ai.com/download> — always the latest APK.
- **Google Play:** search "RikkaHub" or open <https://play.google.com/store/apps/details?id=me.rerere.rikkahub>

RikkaHub runs on Android (minSdk 26 / Android 8.0+). After install, open the app from your home screen or app drawer.

#### 2. Add the DeepSeek Provider

DeepSeek ships as a **pre-configured provider** in RikkaHub — you do not need to enter the base URL by hand.

1. Tap the **Settings** icon (gear) at the bottom of the sidebar to open the settings screen.
2. Select **Providers** from the settings list. You'll see all configured providers as cards.
3. Find the **DeepSeek** card (pre-configured with `Base URL = https://api.deepseek.com/v1`) and tap it. If it's missing, tap **Add Provider** in the top-right corner, choose **OpenAI** as the type, and fill in `https://api.deepseek.com/v1` as the Base URL.
4. On the provider detail screen, paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API Key** field. Leave **Base URL** as `https://api.deepseek.com/v1` — the `/v1` suffix is required because RikkaHub appends the chat-completions path (`/chat/completions`) to it.
5. Tap **Save** / **Confirm** to store the configuration, then use the toggle on the provider card to enable it.

> **Balance checking.** The built-in DeepSeek provider has **Balance Checking** enabled by default — the provider card shows your remaining credit by querying `/user/balance` and extracting `balance_infos[0].total_balance`. If you add DeepSeek manually, enable **Balance Checking** in the provider settings and supply the same API path and JSON field path.

> **1M context window.** RikkaHub does not expose an explicit `context_window` field; the app forwards the full message history to the API on every turn (subject to the assistant's `contextMessageSize` setting, which defaults to 0 = all messages). DeepSeek V4 supports up to **1,000,000 tokens** of context on the API side, and RikkaHub will use whatever you send it — there is no client-side truncation to worry about.

#### 3. Add the DeepSeek V4 Models

1. On the same DeepSeek provider detail screen, scroll to the **Models** section at the bottom and tap it.
2. Tap the expand button to fetch the model list automatically from the DeepSeek API, then tick **`deepseek-v4-pro`** and **`deepseek-v4-flash`**.
3. (If the auto-fetch doesn't list V4 models — e.g. you're using a relay that hasn't caught up — tap **Add** to enter the model ID manually: `deepseek-v4-pro` / `deepseek-v4-flash`.)

RikkaHub's model registry already recognises both IDs and automatically tags them with **Tool** and **Reasoning** capabilities — no need to toggle these manually.

#### 4. Start Chatting

1. Head back to the main screen. Tap the **model selector** shown below the conversation title in the top bar (or inside the input bar on some screen sizes) and pick **`deepseek-v4-pro`** (or **`deepseek-v4-flash`** for cheaper / faster turns).
2. Type your first message in the input bar at the bottom and tap the **send** button (arrow-up). Rikka streams the reply back in real time.
3. DeepSeek V4 returns thinking content by default; Rikka renders the reasoning trace as a collapsible block above the final answer.

##### Reasoning effort

RikkaHub exposes reasoning effort through the assistant's **Reasoning level** setting (`Settings → Assistants → <your assistant> → Reasoning level`), which defaults to `AUTO`. The levels are:

| Level | Token budget | Effort string sent to DeepSeek API |
|---|---|---|
| OFF | 0 | *(thinking disabled)* |
| AUTO | -1 | *(provider default — no `reasoning_effort` field sent)* |
| LOW | 1,000 | `low` |
| MEDIUM | 2,000 | `medium` |
| HIGH | 8,000 | `high` |
| XHIGH | 16,000 | `xhigh` |

For DeepSeek specifically (provider whose Base URL host is `api.deepseek.com`), RikkaHub's request builder emits both `thinking: {type: "enabled"}` and `reasoning_effort: <effort>` in the request body. To get the strongest reasoning the UI exposes, set the level to **XHIGH**.

> **About `reasoning_effort: "max"`.** RikkaHub's enum tops out at `XHIGH`, so the UI on its own sends `reasoning_effort: "xhigh"` to the DeepSeek API — not `"max"`. If you need the `max` level, use the assistant's **Custom request body** override: open the assistant → **HTTP overrides → Custom Bodies** → add a key `reasoning_effort` with value `"max"`. RikkaHub merges custom body entries **last**, so this override wins over the level the assistant selected. This is the documented mechanism for pinning request fields RikkaHub does not surface in the UI — not a workaround for an upstream bug.

#### 5. Going Further

Once DeepSeek V4 is configured, you can use it across the rest of RikkaHub:

- **Workspace.** Go to **Settings → Extension Management → Workspace**, tap **+** to create a workspace, enter a name (English only), then tap the new card → **Install Rootfs**. Open a chat, tap the **+** button in the chat bar, and bind the workspace to the current assistant. The assistant (powered by `deepseek-v4-pro`) can then run shell commands, edit files, install packages via `apt`, and even clone Git repos — all inside the sandboxed Linux environment.
- **MCP servers.** Go to **Settings → MCP**, tap the **+** button in the top-right, and add a server (SSE or Streamable HTTP transport). After it connects, open the assistant's settings → **MCP Servers** → toggle on the servers whose tools this assistant should access. Tool calls go through an approval flow — set **Needs Approval** on any tool that performs irreversible actions.
- **Web search.** Go to **Settings → Search**, tap **Add**, and pick a service — RikkaHub supports Bing, Brave, Tavily, Exa, Perplexity, LinkUp, Firecrawl, Jina, Grok, Bocha, Metaso, Zhipu, SearXNG, Ollama, RikkaHub's own API, and Custom JS. With a search service configured, toggle the search icon in the chat input toolbar before sending a message; Rikka injects fresh web results into the model's context automatically.
- **Multimodal input.** Tap the **+** button on the left of the chat input bar to attach images, PDF, DOCX, PPTX, or EPUB files. Vision-capable models receive images as base64; non-vision models trigger automatic OCR via the OCR model you set in **Settings → Models → OCR Model**.
- **Prompt variables & message branching.** Use `{model}`, `{time}`, etc. in your assistant's system prompt. Long-press any assistant message → **Regenerate** to create a branch and explore alternative completions without losing the original thread.
- **QR-code provider export.** Open the DeepSeek provider → tap the **Share** button → export the configuration (API key + base URL + settings, excluding added models) as a QR code. Scan it on another device to replicate the provider in seconds.
