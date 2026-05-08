[English](./roocode.md) | [简体中文](./roocode.zh-CN.md) · [← Back](../README.md)

# Using DeepSeek with Roo Code

Roo Code is an IDE and CLI-focused coding assistant that supports multiple provider plugins. This guide shows how to configure Roo Code to use DeepSeek V4 models (`deepseek-v4-pro` / `deepseek-v4-flash`).

### Install Roo Code

- VS Code extension: install from the Marketplace: https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline
- For CLI usage or other install methods, see Roo Code's docs: https://docs.roocode.org.cn/

### Get a DeepSeek API key

- Go to the DeepSeek Platform: https://platform.deepseek.com/
- Open the `API Keys` page, create a new key, and copy it. Keep it secret.

### Configure Roo Code (UI)

![roocode_step_1](assets/roocode_step_1.png)

1. Open the Roo Code panel in VS Code and click the gear icon (⚙) .

![roocode_step_2](assets/roocode_step_2.png)

2. In the provider dropdown select `DeepSeek`.
3. Paste your DeepSeek API key into the `DeepSeek API Key` field.
4. Choose a model: `deepseek-v4-pro` (recommended) or `deepseek-v4-flash` (lower cost).

**Notes**:

- The model names `deepseek-chat` and `deepseek-reasoner` are deprecated and will be removed on *2026/07/24*. For compatibility they map to `deepseek-v4-flash`'s non-thinking and thinking modes respectively.
- Roo Code's provider UI may by default only list `deepseek-chat` and `deepseek-reasoner` in the model selector. In that case, manually enter the desired model name (for example, `deepseek-v4-pro`) into the model field to use the current V4 model names.

### Verify the API (optional)

You can test your DeepSeek API key directly before or while configuring Roo Code.

OpenAI-compatible example (non-streaming):

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ],
    "thinking": {"type": "enabled"},
    "reasoning_effort": "max",
    "stream": false
  }'
```

Refer to DeepSeek API docs for Anthropic-style examples: https://api-docs.deepseek.com/guides/anthropic_api

### First run

After saving the Roo Code provider settings, open the Roo Code panel and create a new session. Send a simple prompt (e.g., "Refactor this function") to verify responses come from DeepSeek.

### Tips and notes

- Use `deepseek-v4-pro` for best reasoning; use `deepseek-v4-flash` to reduce cost while iterating.
- Avoid deprecated model names (`deepseek-chat`, `deepseek-reasoner`) — use `deepseek-v4-pro` / `deepseek-v4-flash` instead.
- Pricing and model capabilities change; verify rates and limits on DeepSeek's pricing pages: https://api-docs.deepseek.com/quick_start/pricing
- If Roo Code exposes token-limit settings, configure them to reflect DeepSeek's large context abilities to avoid truncated prompts.

---

For more details see Roo Code's provider docs: https://docs.roocode.org.cn/providers/deepseek
