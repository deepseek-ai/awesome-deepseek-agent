[English](./crush.md) | [简体中文](./crush.zh-CN.md) · [← Back](../README.md)

# Integrate with Crush

Crush is a glamorous open-source AI coding agent that runs in your terminal, built by Charm. It supports multi-model switching, LSP integration, MCP servers, and agentic coding workflows.

#### 1. Install Crush

- Install [Node.js](https://nodejs.org/en/download/).
- Run the following command in your terminal to install Crush:

```bash
npm install -g @charmland/crush
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```bash
crush --version
```

> **Note:** macOS users can also install via Homebrew: `brew install charmbracelet/tap/crush`.

#### 2. Configure DeepSeek Provider

Crush supports custom providers via OpenAI-compatible APIs. Add DeepSeek to your configuration file:

- **Linux / macOS**: `~/.config/crush/crush.json`
- **Windows**: `%USERPROFILE%\.config\crush\crush.json`

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "deepseek": {
      "type": "openai-compat",
      "base_url": "https://api.deepseek.com/v1",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek-V4-Pro",
          "context_window": 1048576,
          "default_max_tokens": 32768,
          "can_reason": true
        },
        {
          "id": "deepseek-v4-flash",
          "name": "DeepSeek-V4-Flash",
          "context_window": 1048576,
          "default_max_tokens": 32768,
          "can_reason": true
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

- Enter the project directory and execute the `crush` command:

```bash
cd /path/to/my-project
crush
```

- Press `Ctrl+L` (or type `/model`) to open the model switcher.
- Select the **DeepSeek** provider and choose `DeepSeek-V4-Pro` or `DeepSeek-V4-Flash`.
- Start coding with your new terminal bestie 💘
