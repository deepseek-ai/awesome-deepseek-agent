[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← Back](../README.md)

# Integrate with Pi

Pi (pi-mono) is a minimal, aggressively extensible terminal coding harness. It adapts to your workflows through TypeScript extensions, skills, prompt templates, and themes — with tree-structured sessions and 15+ built-in providers.

#### 1. Install Pi

- Install [Node.js](https://nodejs.org/en/download/).
- Run the following command in your terminal to install Pi:

```bash
npm install -g @earendil-works/pi-coding-agent
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
          "thinkingLevelMap": { "minimal": null, "low": null, "medium": null, "high": "high", "xhigh": "max" },
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
          "thinkingLevelMap": { "minimal": null, "low": null, "medium": null, "high": "high", "xhigh": "max" },
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
- For V4 Pro coding work, set thinking / reasoning effort to **xhigh** (mapped to `max` in the `thinkingLevelMap` / `reasoningEffortMap` above). V4 models support a 1M context window; the snippet already sets `contextWindow: 1000000`.
- Start coding with your minimal terminal harness.

#### 4. Optional: official Harness minimal surface (V4 Pro)

The DeepSeek V4 Pro model card evaluates code-agent tasks with DeepSeek Harness **minimal** mode: the complete system prompt is `You are a helpful software engineer assistant.`, and the tool catalog is persistent `bash` + `str_replace_editor`. Pi's default catalog is richer, which can change V4 Pro's first-request trajectory.

To use that official surface inside Pi:

```bash
pi install npm:pi-dsh-minimal
```

Then `/reload` or restart Pi, start a **new** session, and select DeepSeek V4 Pro. The extension is on by default but only activates when the model matches V4 Pro (`deepseek-v4-flash` does not match). Open `/dsh` to change the trigger.

This is a [community extension](https://github.com/Averyyy/pi-dsh-minimal), not an official DeepSeek or Pi preset.

For more configuration options, see the [Pi models documentation](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/docs/models.md).
