# Configure DeepSeek in Droid

This guide explains how to add DeepSeek models to Droid's `settings.json`.

## Available Models


| Model                      | Provider  | Base URL                             |
| -------------------------- | --------- | ------------------------------------ |
| DeepSeek V4 Pro            | Anthropic | `https://api.deepseek.com/anthropic` |
| DeepSeek V4 Flash          | Anthropic | `https://api.deepseek.com/anthropic` |
| DeepSeek V4 Pro (OpenAI)   | OpenAI    | `https://api.deepseek.com`           |
| DeepSeek V4 Flash (OpenAI) | OpenAI    | `https://api.deepseek.com`           |


## Configuration

Add these entries to the `customModels` array in `~/.factory/settings.json`:

### Anthropic-compatible models

```json
{
  "model": "deepseek-v4-pro",
  "id": "custom:deepseek-v4-pro---Anthropic",
  "index": 1,
  "baseUrl": "https://api.deepseek.com/anthropic",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Pro",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "anthropic"
},
{
  "model": "deepseek-v4-flash",
  "id": "custom:deepseek-v4-flash---Anthropic",
  "index": 2,
  "baseUrl": "https://api.deepseek.com/anthropic",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Flash",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "anthropic"
}
```

### OpenAI-compatible models

```json
{
  "model": "deepseek-v4-pro",
  "id": "custom:deepseek-v4-pro---OpenAI",
  "index": 1,
  "baseUrl": "https://api.deepseek.com",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Pro (OpenAI)",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "openai"
},
{
  "model": "deepseek-v4-flash",
  "id": "custom:deepseek-v4-flash---OpenAI",
  "index": 2,
  "baseUrl": "https://api.deepseek.com",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Flash (OpenAI)",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "openai"
}
```

## Set as Mission Model (Optional)

To use DeepSeek as the default worker/validation model, update `missionModelSettings` in the same file:

```json
"missionModelSettings": {
  "workerModel": "custom:deepseek-v4-pro---Anthropic",
  "workerReasoningEffort": "none",
  "validationWorkerModel": "custom:deepseek-v4-flash---Anthropic",
  "validationWorkerReasoningEffort": "none",
  "skipUserTesting": true,
  "skipScrutiny": true
}
```

## Understanding Providers

Factory supports three provider types that determine API compatibility:


| Provider                      | API Format                           | Use For                                                                                                               | Documentation                                                                      |
| ----------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `anthropic`                   | Anthropic Messages API (v1/messages) | Anthropic models on their official API or compatible proxies                                                          | [Anthropic Messages API](https://docs.anthropic.com/en/api/messages)               |
| `openai`                      | OpenAI Responses API                 | OpenAI models on their official API or compatible proxies. Required for the newest models like GPT-5 and GPT-5-Codex. | [OpenAI Responses API](https://platform.openai.com/docs/api/responses)             |
| `generic-chat-completion-api` | OpenAI Chat Completions API          | OpenRouter, Fireworks, Together AI, Ollama, vLLM, and most open-source providers                                      | [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) |


DeepSeek V4 Pro and V4 Flash support both `anthropic` and `openai` provider types.

## Notes

- Replace `<your DeepSeek API Key>` with your actual DeepSeek API key, or use environment variable syntax: `"apiKey": "${DEEPSEEK_API_KEY}"`
- Max output tokens: 384,000
- Model indices must be unique across all custom models
- Set the environment variable before starting Droid: `export DEEPSEEK_API_KEY=your_key_here`

## Troubleshooting

**Model not appearing in selector**
- Check JSON syntax in `~/.factory/settings.json` (or `config.json` if using legacy format)
- Settings changes are detected automatically via file watching
- Verify all required fields are present

**"Invalid provider" error**
- Provider must be exactly `anthropic`, `openai`, or `generic-chat-completion-api`
- Check for typos and ensure proper capitalization

**Authentication errors**
- Verify your API key is valid and has available credits
- Check that the API key has proper permissions
- Confirm the base URL matches your provider's documentation

**Rate limiting or quota errors**
- Check your provider's rate limits and usage quotas
- Monitor your usage through your provider's dashboard

