[English](./workbuddy.md) | [简体中文](./workbuddy.zh-CN.md) · [← Back](../README.md)

# Integrate with WorkBuddy/CodeBuddy

WorkBuddy/CodeBuddy is an AI agent and coding assistant. It supports custom models through local model configuration files, and DeepSeek V4 can be connected through the OpenAI-compatible Chat Completions API.

#### 1. Install WorkBuddy/CodeBuddy

- Install and sign in to WorkBuddy/CodeBuddy.
- Open a project folder once, so the application can create its local configuration directories.
- Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Configure Local Models

Create or edit the user-level configuration file:

```
C:\Users\<your-username>\.codebuddy\models.json
```

To apply the configuration only to one project, create the project-level configuration file instead:

```
<your-project>\.codebuddy\models.json
```

Set your DeepSeek API Key as an environment variable first:

```powershell
setx DEEPSEEK_API_KEY "<your DeepSeek API Key>"
```

Then add the following configuration:

```json
{
  "models": [
    {
      "id": "deepseek-v4-pro",
      "name": "DeepSeek V4 Pro",
      "vendor": "DeepSeek",
      "url": "https://api.deepseek.com/v1/chat/completions",
      "apiKey": "${DEEPSEEK_API_KEY}",
      "maxInputTokens": 128000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "relatedModels": {
        "lite": "deepseek-v4-flash",
        "reasoning": "deepseek-v4-pro"
      }
    },
    {
      "id": "deepseek-v4-flash",
      "name": "DeepSeek V4 Flash",
      "vendor": "DeepSeek",
      "url": "https://api.deepseek.com/v1/chat/completions",
      "apiKey": "${DEEPSEEK_API_KEY}",
      "maxInputTokens": 128000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false
    }
  ],
  "availableModels": [
    "deepseek-v4-pro",
    "deepseek-v4-flash"
  ]
}
```

Save `models.json` as UTF-8 without BOM. Some desktop versions may fail to read local model configuration files saved with a UTF-8 BOM header.

#### 3. Restart and Select the Model

Fully quit WorkBuddy/CodeBuddy, then open it again.

In the model selector, choose:

```
DeepSeek V4 Pro
DeepSeek V4 Flash
```

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

- `Authentication Fails` or `401`: Check whether `apiKey` is your real DeepSeek API Key. Do not put the API URL in the API Key field.
- `Model Not Found` or `404`: Check whether the model id is exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- `Failed to read local model configuration`: Check whether `models.json` is valid JSON and saved as UTF-8 without BOM.
- The model does not appear in the selector: Fully restart WorkBuddy/CodeBuddy and confirm the file is placed under `.codebuddy\models.json`.
- `${DEEPSEEK_API_KEY}` is shown literally in the UI: Restart WorkBuddy/CodeBuddy from a terminal where `DEEPSEEK_API_KEY` is available. If the desktop UI still does not expand environment variables, paste the actual API Key in the UI or in your local `models.json`.
