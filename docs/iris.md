[English](./iris.md) | [简体中文](./iris.zh-CN.md) · [← Back](../README.md)

# Integrate with Iris

[Iris](https://github.com/Lianues/Iris) is an open-source multi-platform AI agent that runs on Console (TUI), Web, Discord, Telegram, WeChat, WeCom, Lark, and QQ, with built-in tool calling, session storage, image input, OCR fallback, MCP, memory, and multi-agent support. DeepSeek is one of its first-class LLM providers — Iris talks to `api.deepseek.com` directly, no proxy required.

#### 1. Install Iris

Recommended (cross-platform, requires Node.js):

```bash
npm install -g irises
```

The CLI is `iris`; the npm package is `irises`. Other install methods (GitHub Release binary, Linux one-line installer, Docker, source build) are listed in the [Iris install guide](https://github.com/Lianues/Iris/blob/main/docs/install.md).

#### 2. Configure DeepSeek with the onboard wizard

Get an API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then run:

```bash
iris onboard
```

In the interactive TUI wizard:

- When prompted for **LLM provider**, select **DeepSeek**.
- When prompted for **API Key**, paste your DeepSeek API Key.
- When prompted for **Model**, choose `deepseek-v4-pro` (for coding and complex reasoning) or `deepseek-v4-flash` (for fast, lower-cost iteration).
- For the remaining prompts (platforms, model alias, etc.), accept the defaults or configure as needed.

The wizard writes to `~/.iris/configs/llm.yaml` (override the path via the `IRIS_DATA_DIR` environment variable).

If you prefer YAML, the equivalent `~/.iris/configs/llm.yaml` is:

```yaml
defaultModel: deepseek_pro

models:
  deepseek_pro:
    provider: deepseek
    apiKey: sk-your-deepseek-api-key
    model: deepseek-v4-pro
    contextWindow: 1000000
    requestBody:
      thinking:
        type: enabled
      reasoning_effort: max
      max_tokens: 384000

  deepseek_flash:
    provider: deepseek
    apiKey: sk-your-deepseek-api-key
    model: deepseek-v4-flash
    contextWindow: 1000000
    requestBody:
      max_tokens: 384000
```

- `contextWindow: 1000000` enables DeepSeek V4's full **1M-token** context window in Iris's TUI usage gauge.
- `requestBody.thinking.type: enabled` plus `reasoning_effort: max` turn on DeepSeek V4 thinking at the deepest reasoning level. Both are the official OpenAI-format control parameters documented in DeepSeek's [Thinking Mode guide](https://api-docs.deepseek.com/guides/thinking_mode) — recommended for coding and multi-step agent tasks.
- `max_tokens: 384000` lifts the per-response output cap so V4 has enough budget for long chains of thought plus the final answer.

#### 3. Start Iris

```bash
iris or iris start
```

Inside the Console TUI, use `/model` to switch between configured models, `/settings` to open the LLM / System / MCP settings center, and `/exit` to quit. The full Slash-command reference is in [docs/platforms.md](https://github.com/Lianues/Iris/blob/main/docs/platforms.md).

#### Optional: run Iris on chat platforms

Iris can also run as a Web GUI or as a bot on Discord, Telegram, Lark, QQ, WeChat, or WeCom. Update `platform.type` in `~/.iris/configs/platform.yaml`, and install the IM extension if needed:

```bash
iris ext install lark    # example: install the Lark extension
```

Per-platform tokens and bot setup are documented in [docs/platforms.md](https://github.com/Lianues/Iris/blob/main/docs/platforms.md).

#### Troubleshooting

- **`baseUrl` seems ignored.** By design. `provider: deepseek` always hits the official endpoint `https://api.deepseek.com/v1`. If you need to route through a custom proxy or gateway, use `provider: openai-compatible` with your gateway's `baseUrl` instead.
- **`Invalid model` error.** When using `provider: deepseek`, the `model` field accepts only `deepseek-v4-pro` or `deepseek-v4-flash`. Older V3-era model ids are no longer supported.
- **No thoughts visible in the TUI.** Make sure `requestBody.thinking.type: enabled` is nested under your DeepSeek model entry, not at the top level of `llm.yaml`.
