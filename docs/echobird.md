[English](./echobird.md) | [简体中文](./echobird.zh-CN.md) · [← Back](../README.md)

# Integrate with EchoBird

EchoBird is a desktop control center for AI coding tools on Windows, macOS, and Linux. Instead of editing config files by hand, you add a model provider once and apply it to Claude Code, Codex, or Claude Desktop in one click. EchoBird also ships with a built-in **Install & Repair** assistant and a quant-analysis workspace that can run on the same model.

DeepSeek is a built-in provider: both its OpenAI-compatible endpoint (`https://api.deepseek.com`) and its Anthropic-compatible endpoint (`https://api.deepseek.com/anthropic`) are pre-filled, so EchoBird can point Anthropic-protocol tools like Claude Code and Claude Desktop straight at DeepSeek V4.

- **GitHub:** <https://github.com/edison7009/EchoBird>
- **Website:** <https://echobird.ai>

#### 1. Install EchoBird

Download the installer for your platform from the [official website](https://echobird.ai) or the [GitHub releases page](https://github.com/edison7009/EchoBird/releases).

#### 2. Add DeepSeek as a model

Open **App Manager**, go to the **Model Providers** panel, and select **DeepSeek** from the built-in provider list. Its **OpenAI URL** (`https://api.deepseek.com`) and **Anthropic URL** (`https://api.deepseek.com/anthropic`) are filled in for you.

1. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys).
2. Set **Model ID** to **`deepseek-v4-pro`** for the strongest coding and reasoning, or **`deepseek-v4-flash`** for a faster, cheaper option.
3. For Claude Code / Claude Desktop, append `[1m]` to the model name to use the full **1-million-token** context window, e.g. **`deepseek-v4-pro[1m]`**.
4. Save.

#### 3. Apply DeepSeek to a tool

In **App Manager**, select the tool you want — **Claude Code**, **Codex**, or **Claude Desktop** — open its **MODELS** tab, pick your DeepSeek model, and click **Update model config** (or **Launch app directly**). EchoBird writes the right config for that tool: Anthropic-protocol tools use the `/anthropic` endpoint, OpenAI-compatible tools use `https://api.deepseek.com`.

Keep EchoBird running after switching the Codex / Claude Desktop model.

#### 4. Chat in Install & Repair

Open the **Install & Repair** page and pick your DeepSeek model from the right-hand panel. The built-in assistant runs on DeepSeek V4 — use it to install tools, fix broken configs, and get onboarded.

#### Notes

- **Don't enable API Router for DeepSeek.** When you point a tool directly at DeepSeek, leave the **API Router** toggle off. It is only for relay/router endpoints and will break a direct DeepSeek connection.
- **Reasoning effort.** DeepSeek V4 Pro runs with deep thinking enabled. For the strongest coding results, keep it at the `max` reasoning level.
- **1M context.** DeepSeek V4 supports up to 1 million tokens; use the `[1m]` model-name suffix for Anthropic-protocol tools as shown above.
