[English](./dshandroid.md) | [简体中文](./dshandroid.zh-CN.md) · [← Back](../README.md)

# Integrate with DShAndroid

[DShAndroid](https://github.com/kekejiang114514/deepseek-harness-android) is an Android agent client that runs DeepSeek on the phone itself — no Termux, no root, no computer. It is a pure-Java app on top of the Android platform APIs: the agent loop, the tools and the UI all run on the device, and the phone's own screen can be operated through the accessibility service.

- **GitHub:** <https://github.com/kekejiang114514/deepseek-harness-android>

Chat alone needs nothing but a network connection. The extra capabilities are optional and each one is opt-in.

#### 1. Install DShAndroid

Download the latest `DeepSeekHarness-*.apk` from the [Releases page](https://github.com/kekejiang114514/deepseek-harness-android/releases/latest) and open it; allow "install unknown apps" when Android asks.

- Android 6.0 (API 23) or newer. Gesture dispatch on the screen needs Android 7.0+ — below that, taps fall back to node-level actions, which fail on some custom-drawn controls.
- The app has no bundled runtime and no third-party dependencies, so it starts immediately after install.
- Permissions are optional: **accessibility** (screen reading, taps, typing), **overlay** (the floating status capsule), **notifications**. Deny them all and you still get a normal chat client.

#### 2. Configure DeepSeek

Open **Settings → Endpoint and key**.

1. Leave **Base URL** at the default `https://api.deepseek.com` (the OpenAI-compatible endpoint; add `/anthropic` only if you want the Anthropic wire format).
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the key field and save.
3. The model list is read live from the endpoint's `/models`, so the current catalog appears as-is — no model names are hard-coded in the picker. Choose **`deepseek-v4-pro`** for coding and reasoning, or **`deepseek-flash`** when you want lower latency and vision input.

Both models accept a **1,000,000-token** context window and up to **384K** output tokens on DeepSeek's side. DShAndroid does not send a context-window parameter; instead it keeps history small on purpose — see step 3.

**Reasoning effort**

Thinking mode is enabled by default on DeepSeek V4 with effort `high`, and DShAndroid streams the returned `reasoning_content` into a collapsible block above the answer, so you can watch the model think and fold it away afterwards.

Under the chat title sits a `model · effort ▾` popup with six levels: `off / low / medium / high / xhigh / max`. The level is sent to the API as `reasoning_effort`; the popover label shows the literal value being sent, so `max` means `reasoning_effort: "max"` and `off` means thinking mode is turned off (`thinking: {"type": "disabled"}`).

The API accepts `low`, `high` and `max`, so the six levels collapse onto those three — the same mapping the official docs specify: `low → low`, `medium/high/xhigh → high`, `max → max`. Output budget scales with the level as well (`4096` up to `65536` tokens, well inside the 384K ceiling), because the chain of thought counts toward `max_tokens`.

One thing worth knowing if you use tool calling: once `tools` is in the request, `reasoning_content` from earlier assistant turns has to be sent back on every subsequent request, otherwise the API answers `400`. DShAndroid keeps it in history and replays it automatically.

#### 3. First run

Send a message. A few things are worth knowing before you do:

- **Context compacts itself.** The app folds old turns into a rolling summary once history passes ~24k estimated tokens, truncating oversized tool results first. A grey line such as `↻ folded 5 turns 24.1k → 13.8k tokens` appears in the chat, so you can see it happen. This is why a 1M-token window is rarely needed here: long sessions stay small and cheap instead of growing to the full window. If the server still rejects a request for length, the app compacts aggressively and retries once rather than surfacing the raw error.
- **Tool calls render as cards.** File reads, shell commands and web fetches each appear as a card you can expand; the agent loop has no step limit, and read-only tools within one step run concurrently.
- **File access is scoped.** Choose **workspace** (only the app's own directory) or **device** (the whole shared storage) in Settings; the tools respect that boundary.
- **It can ask you a question.** When a decision is needed the model calls `ui.ask` and you get an inline card with 2–6 options; the answer goes back into the same turn.

#### 4. Optional capabilities

- **Screen control.** Enable the accessibility service from **Settings → Accessibility** (the app deep-links to your system's page for its own service — Android does not let an app grant itself this). The model can then read the screen (`a11y.screen` returns a compact outline, `a11y.dump` the full tree), tap, swipe, type, wait for text to appear, and launch apps. Actions degrade rather than fail: clicking a text node walks up to the nearest clickable ancestor, typing walks up to the nearest editable field.
- **Floating capsule.** An overlay shows what the agent is doing while a turn runs — status, current tool, elapsed time, plus a pause button. It hides itself when the app is in the foreground.
- **Plugins.** Two kinds share `/sdcard/DShAndroid/plugins/`. A declarative `plugin.json` connects any HTTP API without code; tool plugins written for DeepSeek Harness (`import { defineTool } from '@deepseek-ai/dsh-tools'`) run as-is.
- **Pause and continue.** While a reply streams, the send button becomes a pause button; pausing keeps the partial text and tells the model it was interrupted, so continuing resumes mid-sentence instead of regenerating.

#### 5. Troubleshooting

| Symptom | Meaning |
| --- | --- |
| The model list is empty after saving | The key or base URL is wrong, or the endpoint does not expose `/models`. Enter the model id manually. |
| `401` / `invalid api key` | The key was pasted with surrounding whitespace, or it belongs to a different account. |
| The screen tools refuse to run | Accessibility is not enabled, or the service was turned off by the system. Android removes the accessibility entry of a package when that package is force-stopped (closing the app from the recents screen, or a "clean up" action), so re-enable it after a full stop. |
| A retry after an error repeats the same tool call | The agent flags repeated identical results to the model as a stall; ask it to take a different approach. |

---

*Guide verified against DShAndroid 1.4.1 (versionCode 88). Model names, context window and output limits follow the [DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing) page as of November 2026.*
