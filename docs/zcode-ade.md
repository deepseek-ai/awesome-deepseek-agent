[English](./zcode-ade.md) | [简体中文](./zcode-ade.zh-CN.md) · [← Back](../README.md)

# Integrate with ZCode

ZCode is an agentic development environment (ADE) by Zhipu AI (Z.ai) that combines AI agents with your existing toolchain. It supports multiple LLM providers, and you can add DeepSeek as a custom provider in a few clicks.

- **Official site:** <https://zcode.z.ai>
- **Docs:** <https://zcode.z.ai/cn/docs>

#### 1. Install ZCode

Download the installer from <https://zcode.z.ai> and install it for your platform (Windows / macOS / Linux).

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Add DeepSeek as a provider

Open ZCode and navigate to **Settings → Model Settings → Add Provider**. Fill in the fields as follows:

| Field | Value |
|-------|-------|
| Name | `DeepSeek` |
| Base URL | `https://api.deepseek.com/v1` |
| API Key | `sk-...` (your DeepSeek API key) |
| Model IDs | `deepseek-v4-pro`, `deepseek-v4-flash` |

DeepSeek's OpenAI-compatible endpoint is used under the hood, which matches the Responses API format ZCode speaks.

#### 4. Switch to a DeepSeek model

In the model picker, select `deepseek-v4-flash` or `deepseek-v4-pro`.

You're ready to go. DeepSeek V4's thinking mode is **enabled by default** (reasoning effort defaults to `high`), so deep reasoning is active out of the box — no extra configuration needed.

> **Note:** ZCode's reasoning-effort level selector currently applies to its built-in OpenAI models. For third-party providers like DeepSeek, the selector may not take effect yet; the model's default thinking mode (high effort) is used instead. DeepSeek V4 supports a 1M-token context window.
