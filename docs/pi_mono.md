[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← Back](../README.md)

# Integrate with Pi

Pi (pi-mono) is a minimal, aggressively extensible terminal coding harness. It adapts to your workflows through TypeScript extensions, skills, prompt templates, and themes — with tree-structured sessions and 15+ built-in providers.

#### 1. Install Pi

- Install [Node.js](https://nodejs.org/en/download/).
- Run the following command in your terminal to install Pi:

```bash
npm install -g @mariozechner/pi-coding-agent
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```bash
pi --version
```

> **Note:** Linux / macOS users can also install via the official script:
> ```bash
> curl -fsSL https://pi.dev/install.sh | sh
> ```

#### 2. Configure DeepSeek Provider

Pi supports custom providers via `models.json`. Add DeepSeek as an OpenAI-compatible provider:

- **Linux / macOS**: `~/.pi/agent/models.json`
- **Windows**: `%USERPROFILE%\.pi\agent\models.json`

```json
{
  "providers": {
    "deepseek": {
      "baseUrl": "https://api.deepseek.com",
      "api": "openai-completions",
      "apiKey": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek V4 Pro",
          "contextWindow": 1000000,
          "maxTokens": 384000,
          "input": ["text"],
          "reasoning": true,
          "cost": {
            "input": 1.74,
            "output": 3.48,
            "cacheRead": 0.145,
            "cacheWrite": 0
          },
          "compat": {
            "requiresReasoningContentOnAssistantMessages": true,
            "thinkingFormat": "deepseek",
            "reasoningEffortMap": {
              "minimal": "high",
              "low": "high",
              "medium": "high",
              "high": "high",
              "xhigh": "max"
            }
          }
        },
        {
          "id": "deepseek-v4-flash",
          "name": "DeepSeek V4 Flash",
          "contextWindow": 1000000,
          "maxTokens": 384000,
          "input": ["text"],
          "reasoning": true,
          "cost": {
            "input": 0.14,
            "output": 0.28,
            "cacheRead": 0.028,
            "cacheWrite": 0
          },
          "compat": {
            "requiresReasoningContentOnAssistantMessages": true,
            "thinkingFormat": "deepseek",
            "reasoningEffortMap": {
              "minimal": "high",
              "low": "high",
              "medium": "high",
              "high": "high",
              "xhigh": "max"
            }
          }
        }
      ]
    }
  }
}
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Set the environment variable:

Linux / Mac users:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Windows users:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

#### 3. Run and Select Model

- Enter the project directory and execute the `pi` command:

```bash
cd /path/to/my-project
pi
```

- Type `/model` to open the model switcher.
- Select **deepseek** and choose `DeepSeek-V4-Pro` or `DeepSeek-V4-Flash`.
- Start coding with your minimal terminal harness.

For more configuration options, see the [Pi models documentation](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/docs/models.md).
