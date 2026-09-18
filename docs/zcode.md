[English](./zcode.md) | [简体中文](./zcode.zh-CN.md) · [← Back](../README.md)

# Integrate with ZCode

ZCode is an AI coding agent desktop application. Besides its built-in models, it supports **custom model providers**, so you can register the DeepSeek API and drive the agent with DeepSeek models.

DeepSeek serves an **Anthropic-compatible** endpoint (`/v1/messages`), which ZCode supports natively — no proxy or extra tooling is needed.

#### 1. Install ZCode

Download and install ZCode from the [official site](https://zcode.z.ai/), then sign in.

#### 2. Get a DeepSeek API Key

Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Open the model settings

Click the **model name** at the bottom of the chat box, then choose **Manage models** in the menu.

![Open the model menu](./assets/zcode_model_menu.png)

The **Model Settings** page opens. Under **Custom Providers**, click **Add Provider**.

![Custom providers](./assets/zcode_model_settings.png)

#### 4. Add a DeepSeek provider

Fill in the form as below. **API Format** already defaults to `Anthropic Messages (/v1/messages)` — that is exactly what DeepSeek's endpoint speaks.

![Add provider](./assets/zcode_add_provider.png)

| Field | Value |
| --- | --- |
| Name | `deepseek` |
| Base URL | `https://api.deepseek.com/anthropic` |
| API Key | your DeepSeek API Key |
| API Format | `Anthropic Messages (/v1/messages)` |

![Provider form filled in](./assets/zcode_fill_provider.png)

#### 5. Add the model

The **Add Provider** button stays disabled until the provider contains at least one model. Click **Add Model** and fill in:

![Add a model](./assets/zcode_add_model.png)

| Field | Value |
| --- | --- |
| Model ID | `deepseek-flash` |
| Context window | `1000000` |
| Max output tokens | `128000` |
| Input / Output types | `Text` (default) |

`deepseek-flash` is the current DeepSeek V4.1 Flash model and supports a **1M-token context window** — set the context window to `1000000` so ZCode can use the full window. For maximum coding capability, register a second model with the ID `deepseek-v4-pro`.

> Older guides may refer to `deepseek-v4-flash`; that name has been retired and now resolves to the same V4.1 Flash model. Use `deepseek-flash` as shown on the [pricing page](https://api-docs.deepseek.com/quick_start/pricing).

Click **Save**, then click **Add Provider** to create the provider.

#### 6. Use DeepSeek in a chat

The provider is now enabled and lists the model you registered:

![DeepSeek provider configured](./assets/zcode_provider_ready.png)

Select it from the model menu at the bottom of the chat box:

![Select the DeepSeek model](./assets/zcode_select_model.png)

#### 7. Set the reasoning effort to Max

DeepSeek reasons before answering. In the chat toolbar, set **Reasoning effort** to **Max** so the model uses its full thinking budget (`deepseek-v4-pro` supports the highest effort levels):

> Toolbar → **Reasoning effort** → **Max**

If the entry is greyed out, the selected model does not expose reasoning levels — switch to a DeepSeek reasoning-capable model first.

#### Notes

- The Base URL must end with `/anthropic`. Use the `Anthropic Messages (/v1/messages)` API format rather than an OpenAI-compatible one.
- ZCode sends the key in the `x-api-key` header; the key is stored locally and only ever displayed masked.
- DeepSeek maps unrecognized model names to `deepseek-flash`, so a typo in the Model ID will not fail loudly — double-check it.
- Anthropic-only parameters such as `anthropic-version`, `container`, `mcp_servers`, `top_k` and `cache_control` are ignored by DeepSeek's endpoint; `top_p` only applies in thinking mode.

#### References

- [DeepSeek — Using the Anthropic API](https://api-docs.deepseek.com/guides/anthropic_api)
- [DeepSeek Platform — API Keys](https://platform.deepseek.com/api_keys)
- [ZCode official site](https://zcode.z.ai/)
