[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex

Codex is OpenAI's coding agent, available as a CLI and app. Codex communicates with models through the OpenAI Responses API, so it needs a forwarding layer to handle requests. This guide uses [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) as that forwarding layer.

#### 1. Install Requirements

- [Node.js](https://nodejs.org/en/download/) 18+.
- [Go](https://go.dev/dl/) 1.25+.
- Install Codex CLI:

```shell
npm install -g @openai/codex
```

Verify the installation:

```shell
codex --version
go version
```

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure Moon Bridge

Clone Moon Bridge and create a local config file:

```shell
git clone https://github.com/ZhiYi-R/moon-bridge.git
cd moon-bridge
```

Create `config.yml` and set your DeepSeek API key:

```yaml
mode: "Transform"

server:
  addr: "127.0.0.1:38440"

models:
  deepseek-v4-pro:
    context_window: 1000000
    max_output_tokens: 384000
    default_reasoning_level: "high"
    supported_reasoning_levels:
      - effort: "high"
        description: "High reasoning effort"
      - effort: "xhigh"
        description: "Extra high reasoning effort"
    supports_reasoning_summaries: true
    default_reasoning_summary: "auto"
    extensions:
      deepseek_v4:
        enabled: true
  deepseek-v4-flash:
    context_window: 1000000
    max_output_tokens: 384000
    default_reasoning_level: "high"
    supported_reasoning_levels:
      - effort: "high"
        description: "High reasoning effort"
      - effort: "xhigh"
        description: "Extra high reasoning effort"
    supports_reasoning_summaries: true
    default_reasoning_summary: "auto"
    extensions:
      deepseek_v4:
        enabled: true

providers:
  deepseek:
    base_url: "https://api.deepseek.com/anthropic"
    api_key: "sk-your-deepseek-api-key"
    offers:
      - model: deepseek-v4-pro
      - model: deepseek-v4-flash

routes:
  # Add more routes here for Codex-recognizable model ID alias (e.g., gpt-5.5, gpt-5.2)
  moonbridge:
    model: deepseek-v4-pro
    provider: deepseek
  # gpt-5.5:
  #   model: deepseek-v4-pro
  #   provider: deepseek
  # gpt-5.2:
  #   model: deepseek-v4-flash
  #   provider: deepseek

defaults:
  model: moonbridge
  max_tokens: 65536
```

This minimal config uses the current Moon Bridge configuration structure and enables DeepSeek V4 Pro / Flash, Codex model metadata, and the DeepSeek V4 compatibility extension. **For image input, Web Search, or multi-provider routing**, extend it with the options from Moon Bridge's `config.example.yml`.

#### 4. Start Moon Bridge

```shell
go run ./cmd/moonbridge --config config.yml
```

Keep this terminal open. By default Moon Bridge listens on `127.0.0.1:38440` and exposes an OpenAI Responses-compatible endpoint at:

```text
http://127.0.0.1:38440/v1/responses
```

#### 5. Generate Codex Configuration

In another terminal, run the following commands from the Moon Bridge directory to write Codex's `config.toml` and `models_catalog.json` into `CODEX_HOME_DIR`.

If you already have a Codex config, **back up your current** `config.toml` first:

macOS / Linux:

```shell
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME_DIR"

# Back up the current config.toml
cp "$CODEX_HOME_DIR/config.toml" "$CODEX_HOME_DIR/config.toml.bak" 2>/dev/null || true

# Create config.toml and models_catalog.json
MODEL="$(go run ./cmd/moonbridge --config config.yml --print-codex-model)"
go run ./cmd/moonbridge \
  --config config.yml \
  --print-codex-config "$MODEL" \
  --codex-base-url "http://127.0.0.1:38440/v1" \
  --codex-home "$CODEX_HOME_DIR" \
  > "$CODEX_HOME_DIR/config.toml"
```

Windows PowerShell:

```powershell
$CODEX_HOME_DIR = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { "$HOME\.codex" }
New-Item -ItemType Directory -Force -Path $CODEX_HOME_DIR | Out-Null

# Back up the current config.toml
if (Test-Path "$CODEX_HOME_DIR\config.toml") {
  Copy-Item "$CODEX_HOME_DIR\config.toml" "$CODEX_HOME_DIR\config.toml.bak" -Force
}

# Create config.toml and models_catalog.json
$MODEL = go run ./cmd/moonbridge --config config.yml --print-codex-model
go run ./cmd/moonbridge `
  --config config.yml `
  --print-codex-config "$MODEL" `
  --codex-base-url "http://127.0.0.1:38440/v1" `
  --codex-home "$CODEX_HOME_DIR" `
  | Set-Content -Path "$CODEX_HOME_DIR\config.toml"
```

This creates:

- `config.toml`: Codex provider configuration using `wire_api = "responses"`.
- `models_catalog.json`: model capability metadata for Codex, including context window, reasoning levels, and tool support.

Before generating the files, you can check the default Codex model read by Moon Bridge:

```shell
go run ./cmd/moonbridge --config config.yml --print-codex-model
# moonbridge
```

#### 6. Start Codex

Enter the project you want to work on and launch Codex:

```shell
cd /path/to/my-project
codex
```

Codex now sends OpenAI Responses requests to Moon Bridge, and Moon Bridge routes them to DeepSeek V4.

Codex App can use the same generated Codex configuration.

#### One-Command Launcher

Moon Bridge provides a helper script for Codex CLI that can build and start the proxy, generate the Codex config, and launch Codex in one command:

```shell
./scripts/start_codex_with_moonbridge.sh --project-directory /path/to/my-project
```

Windows PowerShell users can use:

```powershell
.\scripts\start_codex_with_moonbridge.ps1 -ProjectDirectory C:\path\to\my-project
```

#### Verify

Check the available models:

```shell
curl http://127.0.0.1:38440/v1/models
```

Send a direct Responses test request:

```shell
curl http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonbridge",
    "input": "Say hello in one short sentence.",
    "max_output_tokens": 1024
  }'
```

After Codex sends a message, the Moon Bridge terminal should show a `POST /v1/responses` log line.

You can also verify that the reasoning level is passed through:

```shell
curl http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonbridge",
    "input": "Explain what Moon Bridge does in one sentence.",
    "reasoning": {"effort": "high"},
    "max_output_tokens": 1024
  }'
```

#### Troubleshooting

- `connection refused`: Moon Bridge is not running, or `server.addr` in `config.yml` uses a different port.
- Codex cannot see the model: rerun step 5; Codex needs `models_catalog.json` in `CODEX_HOME`. If it still doesn't appear, add Codex-recognizable model IDs (e.g., `gpt-5.5`, `gpt-5.2`) to the `routes` section in `config.yml`, for example:
  ```yaml
  routes:
    gpt-5.4:
      model: deepseek-v4-pro
      provider: deepseek
    gpt-5.2:
      model: deepseek-v4-flash
      provider: deepseek
  ```
- Config loading fails with `field provider not found`: you are using the old `provider.providers` format. The current format uses top-level `providers`, `models`, `routes`, and `defaults`.
- `401` or authentication errors: check the DeepSeek API key in `config.yml`.
- `402` or payment errors: check your DeepSeek Platform balance.
- Image input fails: if you enabled the Visual extension, configure a separate visual provider (e.g., Kimi) with its API key. You can configure that provider, or remove `visual.enabled: true` to disable the Visual extension.

#### Resources

- [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge)
- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
