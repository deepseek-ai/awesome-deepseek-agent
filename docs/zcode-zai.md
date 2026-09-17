[English](./zcode-zai.md) | [简体中文](./zcode-zai.zh-CN.md) · [← Back](../README.md)

# Integrate with ZCode

ZCode is an AI coding agent with a desktop app and a CLI. It supports custom model providers through OpenAI-compatible (Chat Completions / Responses) and Anthropic-compatible (Anthropic Messages) APIs, and ships with a built-in DeepSeek provider in its provider catalog, so DeepSeek V4 can be connected in a few clicks.

#### 1. Install ZCode

- Download the desktop installer from the [official ZCode site](https://zcode.z.ai) and install it.
- Launch ZCode and sign in.
- Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Add the DeepSeek Provider

Open **Settings → Model Providers** (模型供应商) and click **Add model provider** (添加模型供应商).

**Option 1 — From the provider catalog (built-in):**

Select **Provider catalog** (供应商目录), search for `DeepSeek`, and pick the DeepSeek provider entry. It is pre-configured with:

- Base URL: `https://api.deepseek.com`
- Models: `deepseek-v4-pro`, `deepseek-v4-flash`
- Context window: 1,000,000 tokens
- Max output tokens: 384,000

Enter your DeepSeek API Key and save.

**Option 2 — Custom endpoint:**

Select **Custom endpoint** (自定义端点) and fill in:

- **Name**: `DeepSeek`
- **API format**: `Chat Completions` (OpenAI-compatible)
- **Base URL**: `https://api.deepseek.com`
- **API Key**: `<your DeepSeek API Key>`

Then add the two models:

| Model ID | Context window | Max output tokens |
| -------- | -------------- | ----------------- |
| `deepseek-v4-pro` | 1,000,000 | 384,000 |
| `deepseek-v4-flash` | 1,000,000 | 384,000 |

Both models support the `max` reasoning level by default (DeepSeek V4's full thinking mode), which ZCode exposes as `off` / `high` / `max` variants.

#### 3. Select the Model

Open a chat or a new task, and use the model switcher in the chat toolbar to select:

```
DeepSeek V4 Pro
DeepSeek V4 Flash
```

`deepseek-v4-pro` is the best choice for complex agentic coding work; `deepseek-v4-flash` is the fast, low-cost option for simple tasks.

#### 4. Optional: Verify the API Key

Windows users can verify the API Key in PowerShell:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"

curl https://api.deepseek.com/v1/chat/completions `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:DEEPSEEK_API_KEY" `
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

If the request succeeds, the API Key and model name are valid.

#### Troubleshooting

- `401` / authentication error: Check whether the API Key is your real DeepSeek API Key. Do not put the API URL in the API Key field.
- `Model Not Found` / `404`: Check that the model id is exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- The provider does not appear in the model switcher: Make sure the provider is enabled and the API Key is set, then restart ZCode.
- `402` / quota error: Check the balance of your DeepSeek Platform account.

#### Related Resources

- [ZCode](https://zcode.z.ai)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
