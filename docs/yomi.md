[English](./yomi.md) | [简体中文](./yomi.zh-CN.md) · [← Back](../README.md)

# Integrate with Yomi

[Yomi](https://github.com/Crescent617/yomi) is a minimalist open-source AI coding assistant built in Rust. It provides a terminal TUI and an optional desktop GUI, can run as a daemon that connects chat platforms such as Feishu and Telegram, and is extensible through skills and stdio-based extensions.

#### 1. Install Yomi

macOS / Linux users can install via [Homebrew](https://brew.sh):

```bash
# CLI (TUI + headless runner)
brew update && brew install crescent617/tap/yomi

# Optional: desktop GUI
brew install crescent617/tap/yomi-app
```

Alternatively, download prebuilt binaries from the [releases page](https://github.com/Crescent617/yomi/releases), or build from source with Rust 1.90+.

> DeepSeek V4 thinking mode requires yomi **v0.10.0 or later**, which handles `reasoning_content` correctly. Check your version with `yomi version` and upgrade with `brew upgrade crescent617/tap/yomi`.

#### 2. Configure DeepSeek in Yomi

Yomi reads `~/.yomi/config.toml`. Get your API key from the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys), then add:

```toml
#:schema https://raw.githubusercontent.com/Crescent617/yomi/main/docs/config-schema.json

[[models]]
name = "deepseek"
provider = "openai"              # DeepSeek API is OpenAI-compatible
model_id = "deepseek-v4-pro"     # or "deepseek-v4-flash"
endpoint = "https://api.deepseek.com/v1"
api_key = "sk-..."               # your DeepSeek API key
context_window = 1_000_000       # DeepSeek V4 supports up to 1M tokens of context
max_tokens = 384_000

[models.thinking]                # thinking mode
enabled = true
effort = "max"                   # deepseek-v4-pro supports "max" and "high"; yomi forwards it as reasoning_effort

[agent]
default_model = "deepseek"
```

- For a lighter, faster setup, set `model_id = "deepseek-v4-flash"`. The thinking effort levels available for each model are listed in the [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode).
- Environment variables work as an alternative to the config file: `OPENAI_API_KEY`, `OPENAI_API_BASE=https://api.deepseek.com/v1`, `OPENAI_API_MODEL=deepseek-v4-pro`, `YOMI_THINKING=true`, `YOMI_THINKING_EFFORT=max`, `YOMI_CONTEXT_WINDOW=1M`.

#### 3. First Run

```bash
# Interactive TUI (run in your project directory)
yomi

# Headless single prompt
yomi run "Summarize this repository in three sentences"
```

The desktop app (Yomi.app) reads the same `~/.yomi/config.toml`.

Ask a question — if the reply streams in with a thinking section, DeepSeek V4 is up and running. `yomi doctor` health-checks the daemon, channels, and configuration; `yomi usage` shows token consumption.
