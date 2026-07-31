[简体中文](./polaris.zh-CN.md) · [← Back](../README.md)

# Integrate with Polaris

Polaris is a cross-platform AI development workspace with built-in coding agent engines (Claude Code, Codex, Simple AI, Pi, Mimo) and a flexible Model Provider system. DeepSeek models are integrated through this provider layer — no engine-level code changes required.

**Project**: [https://github.com/misxzaiz/Polaris](https://github.com/misxzaiz/Polaris)

DeepSeek supports all three wire protocols that Polaris's Model Provider exposes: **Anthropic Messages**, **OpenAI Chat Completions**, and **OpenAI Responses**. Users can select the protocol that best fits their workflow.

#### 1. Open Model Provider Settings

Open **Settings → Model Providers** in Polaris. This is where you manage all model provider profiles.

![Model Provider List](./assets/polaris_provider_list.png)

#### 2. Obtain a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Add DeepSeek as a Model Provider

1. Click **Add Provider** (or edit an existing profile).
2. Fill in the configuration:

   | Field | Value |
   |-------|-------|
   | Profile Name | `deepseek-v4-flash` (or `deepseek-v4-pro`) |
   | Model Name | `deepseek-v4-flash` (or `deepseek-v4-pro`) |
   | Auth Method | `Auth Token` (Bearer) |
   | API Key | (paste your DeepSeek API Key) |

3. Choose the **API Endpoint URL** and **Protocol** based on your preferred wire format:

   | Protocol | API Endpoint URL | Description |
   |----------|------------------|-------------|
   | Anthropic Messages (default) | `https://api.deepseek.com/anthropic` | Native reasoning/thinking mode, `thinking: { type: "enabled" }` |
   | OpenAI Chat Completions | `https://api.deepseek.com/v1/chat/completions` | Standard OpenAI-compatible chat |
   | OpenAI Responses | `https://api.deepseek.com/v1/responses` | Responses API |

4. Under **Applicable Engines**, select which engines should use this provider (e.g. Simple AI, Pi, Claude Code, Codex CLI, Mimo).
5. Under **Advanced Options → Context Window**, select **1M** to use DeepSeek V4's full 1M context support.
6. Click **Test Connection** to verify, then **Save**.

![DeepSeek Provider Config](./assets/polaris_provider_config.png)

#### 4. Select DeepSeek as Your Model

1. Open the chat panel in Polaris.
2. In the engine/model selector dropdown (next to the engine toggle), choose your DeepSeek model profile (e.g. `deepseek-v4-flash`).
3. Start a conversation — DeepSeek V4 is now powering your Polaris agent.

![Select DeepSeek Model](./assets/polaris_model_select.png)

#### Notes

- **Model names**: Use `deepseek-v4-pro` or `deepseek-v4-flash` (the current V4 naming). Older V3 names (`deepseek-chat`, `deepseek-reasoner`) are deprecated.
- **1M context window**: DeepSeek V4 supports up to 1M tokens of context. Set the context window to **1M** in Advanced Options to take full advantage.
- **Reasoning / thinking mode**: DeepSeek V4 Pro supports reasoning effort levels. When using the Anthropic Messages endpoint, reasoning mode is available natively via the `thinking` parameter. Configure the reasoning effort level via the model selector's settings in the chat panel.
- **Engine selection**: Polaris's five built-in engines (Claude Code, Codex CLI, Simple AI, Pi, Mimo) can all route through the DeepSeek provider. The choice of engine determines the agent loop and tool-use behavior; the provider determines which model API is called underneath.
- **Windows note**: Polaris runs natively on Windows. No additional environment variable setup is required — the API Key is configured directly in the Model Provider settings UI.
