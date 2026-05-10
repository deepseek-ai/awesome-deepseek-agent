[English](./zot.md) | [简体中文](./zot.zh-CN.md) · [← Back](../README.md)

# Integrate with zot

zot is a lightweight coding agent harness written in Go, shipped as a single static binary. It comes with built-in DeepSeek support through DeepSeek's OpenAI-compatible chat API, four built-in tools (read, write, edit, bash), three run modes (interactive TUI, print, JSON), and an extension system in any language via subprocess + JSON-RPC.

#### 1. Install zot

- **Linux / macOS** (one-liner):

```bash
curl -fsSL https://www.zot.sh/install.sh | bash
```

- **Windows** (PowerShell):

```powershell
iwr -useb https://www.zot.sh/install.ps1 | iex
```

- **Via Go**:

```bash
go install github.com/patriceckhart/zot/cmd/zot@latest
```

- After installation, verify by running:

```bash
zot --help
```

#### 2. Configure DeepSeek Provider

zot has built-in DeepSeek support, so no manual provider configuration is required. The default settings are:

- **model**: `deepseek-v4-pro`
- **base URL**: `https://api.deepseek.com/v1`

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

Alternatively, run `zot` and type `/login`, then pick **api key** to paste your DeepSeek key. zot probes `/v1/models` once and stores the key under `deepseek` in `$ZOT_HOME/auth.json` (mode 0600).

Credential lookup order for DeepSeek:

1. `--api-key` flag
2. `DEEPSEEK_API_KEY` environment variable
3. `$ZOT_HOME/auth.json`

> **Note:** DeepSeek does not offer a subscription OAuth flow. Authentication is API-key only.

#### 3. Run and Select Model

- Enter the project directory and run zot with the DeepSeek provider:

```bash
cd /path/to/my-project
zot --provider deepseek
```

- Catalog ships with two models, both selectable via `/model` in the TUI:
  - `deepseek-v4-pro` (reasoning)
  - `deepseek-v4-flash`

- To pick a specific model directly:

```bash
zot --provider deepseek --model deepseek-v4-flash
```

- To use a custom-compatible endpoint (mirror, gateway, self-host):

```bash
zot --provider deepseek \
    --base-url https://my-deepseek-mirror.example.com/v1 \
    --api-key "$DEEPSEEK_API_KEY"
```

#### 4. Add Custom Models (Optional)

Place a `models.json` in `$ZOT_HOME` to add models that aren't in the baked-in catalog:

- **macOS**: `~/Library/Application Support/zot/models.json`
- **Linux**: `~/.local/state/zot/models.json`
- **Windows**: `%LOCALAPPDATA%\zot\models.json`

```json
{
  "providers": {
    "deepseek": {
      "models": [
        {
          "id": "deepseek-v5-preview",
          "name": "DeepSeek V5 Preview",
          "reasoning": true,
          "contextWindow": 128000,
          "maxTokens": 8192
        }
      ]
    }
  }
}
```

> **Note on text-only mode:** DeepSeek's chat-completions endpoint currently rejects the multimodal content schema. When the active provider is `deepseek`, zot silently drops image parts from outgoing messages and keeps only the text. Switching back to a vision-capable model re-sends the image normally because the session file still stores it.

For more configuration options, see the [zot README](https://github.com/patriceckhart/zot/blob/main/README.md).
