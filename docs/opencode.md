[English](./opencode.md) | [简体中文](./opencode.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenCode

OpenCode is an open-source AI coding assistant available in terminal, desktop, and web form. It supports DeepSeek out of the box through the built-in `deepseek` provider.

#### 1. Install OpenCode

- **Terminal (CLI)**: run `curl -fsSL https://opencode.ai/install | bash`, or download the binary for your platform from the [OpenCode download page](https://opencode.ai/download).
- **Desktop / Web**: grab the desktop app or use the web version from the [download page](https://opencode.ai/download).

> **Note:** to avoid compatibility issues, upgrade OpenCode to the latest version (>= v1.14.24).

#### 2. Add Your DeepSeek API Key

1. Head over to the [DeepSeek console](https://platform.deepseek.com/api_keys), create an account, and click **Create new API key**.
2. Run the `opencode` command to start the TUI.
3. Type `/connect` in the input box, then enter `deepseek` and select the **DeepSeek** provider.
4. Paste your DeepSeek API key.

Alternatively, set the `DEEPSEEK_API_KEY` environment variable in your shell profile — OpenCode picks it up automatically.

#### 3. Select a Model

Run the `/models` command in the input box and choose one of the current DeepSeek V4 models:

| Model | Description |
| ----- | ----------- |
| `deepseek-v4-pro` | Flagship model for coding, reasoning, and agentic work |
| `deepseek-v4-flash` | Fast and economical lane for coding and long-context work |

> **Note:** `deepseek-chat` / `deepseek-reasoner` are deprecated V3 names. Use `deepseek-v4-pro` or `deepseek-v4-flash`.

#### 4. Use the Full Capabilities

DeepSeek V4 models are enabled automatically by the built-in provider — no extra config needed:

- **1M context window** — both models accept up to 1,000,000 tokens of context (384,000 output tokens). OpenCode reads these limits from the model metadata and handles compaction for you.
- **Max thinking / reasoning effort** — both models support `high` and `max` reasoning effort levels. In OpenCode, set the reasoning effort (or toggle reasoning on/off) from the model picker or the model configuration in `opencode.json`.

#### 5. Verify

Start a new session, confirm the selected model is `deepseek-v4-pro` (or `deepseek-v4-flash`) in the model picker, and send a message. DeepSeek will respond with its interleaved reasoning output shown in the session.
