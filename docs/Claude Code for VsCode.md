# How to Integrate DeepSeek V4 Flash/Pro into Claude Code for VS Code

This guide shows you how to configure the Claude Code extension in VS Code to use DeepSeek models (`deepseek-v4-pro` or `deepseek-v4-flash`), giving you cost‑effective and powerful AI‑assisted coding.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/) installed
- **Claude Code** extension installed from the VS Code Marketplace
- A valid DeepSeek API Key obtained from the [DeepSeek Platform](https://platform.deepseek.com)

## Setup Instructions

### 1. Open VS Code Settings

Press `Ctrl + ,` (`Cmd + ,` on macOS) to open Settings, then type `claude code` in the search bar. Click **Edit in settings.json** to open your configuration file.

### 2. Paste the JSON Configuration

Copy the complete JSON snippet below and paste it into your `settings.json` file (merge it carefully with your existing settings). **Make sure to replace the `ANTHROPIC_AUTH_TOKEN` value with your real DeepSeek API Key.**

```json
{
  "claudeCode.selectedModel": "deepseek-v4-pro",
  "claudeCode.environmentVariables": [
    {
      "name": "ANTHROPIC_BASE_URL",
      "value": "https://api.deepseek.com/anthropic"
    },
    {
      "name": "ANTHROPIC_AUTH_TOKEN",
      "value": "sk-xxx"   // ⚠️ Replace with your actual API Key
    },
    {
      "name": "ANTHROPIC_MODEL",
      "value": "deepseek-v4-pro[1m]"
    },
    {
      "name": "ANTHROPIC_DEFAULT_OPUS_MODEL",
      "value": "deepseek-v4-pro[1m]"
    },
    {
      "name": "ANTHROPIC_DEFAULT_SONNET_MODEL",
      "value": "deepseek-v4-flash[1m]"
    },
    {
      "name": "ANTHROPIC_DEFAULT_HAIKU_MODEL",
      "value": "deepseek-v4-pro"
    },
    {
      "name": "CLAUDE_CODE_SUBAGENT_MODEL",
      "value": "deepseek-v4-flash"
    },
    {
      "name": "API_TIMEOUT_MS",
      "value": "600000"
    },
    {
      "name": "CLAUDE_CODE_EFFORT_LEVEL",
      "value": "max"
    },
    {
      "name": "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC",
      "value": "1"
    }
  ],
  "claudeCode.preferredLocation": "panel",
  "claudeCode.disableLoginPrompt": true
}
```

### 3. Restart and Apply Configuration

After saving `settings.json`, **fully quit and restart VS Code** (or reload the window via `Ctrl + Shift + P` → `Developer: Reload Window`) to ensure all environment variables take effect.

### 4. Verify the Integration

Open the Claude Code panel (sidebar or bottom panel) and type `/model`. If you see `deepseek-v4-pro` or `deepseek-v4-flash` in the model list, the configuration has been applied successfully. You can test it with a simple prompt (e.g., “Write a Python function for quicksort”) to confirm everything works as expected.

## Configuration Reference

| Environment Variable / Setting | Description |
| :--- | :--- |
| `ANTHROPIC_BASE_URL` | DeepSeek‑compatible Anthropic endpoint; **must be** `https://api.deepseek.com/anthropic` |
| `ANTHROPIC_AUTH_TOKEN` | Your DeepSeek API Key from the [platform](https://platform.deepseek.com) |
| `ANTHROPIC_MODEL` | Primary model used for conversations. `[1m]` enables 1M‑token context window |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Model mapped to the Opus tier, set to `deepseek-v4-pro[1m]` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Model mapped to the Sonnet tier, set to `deepseek-v4-flash[1m]` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Model mapped to the Haiku tier, set to `deepseek-v4-pro` (or `flash`) |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model used by sub‑agents; `deepseek-v4-flash` is recommended for speed |
| `API_TIMEOUT_MS` | Request timeout in milliseconds; use `600000` (10 min) for complex tasks |
| `CLAUDE_CODE_EFFORT_LEVEL` | Reasoning depth; `max` gives the most thorough analysis (slower) |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Set to `1` to disable telemetry, improving privacy |
| `claudeCode.preferredLocation` | UI location: `panel` (bottom) or `sidebar` |
| `claudeCode.disableLoginPrompt` | Set to `true` to skip the default login prompt and use your custom API key |

> **Note**: If your DeepSeek plan does not support the 1M context window, simply remove the `[1m]` suffix from the model names (e.g. use `deepseek-v4-pro`). `pro` models excel at complex reasoning, while `flash` models offer faster responses; you can mix them according to your needs.

## Troubleshooting

- **“Not Authenticated” error**  
  Verify that `ANTHROPIC_AUTH_TOKEN` is set to a valid API Key with sufficient balance.

- **Model does not appear in `/model` list**  
  Double‑check the model name spelling and restart VS Code completely.

- **Request timeouts**  
  Increase `API_TIMEOUT_MS` (e.g., to `900000`) or switch to the faster `deepseek-v4-flash` model.

- **Other unexpected errors**  
  Ensure the Claude Code extension is up to date, and try running `Claude Code: Clear Cache` from the command palette before retrying.
```
