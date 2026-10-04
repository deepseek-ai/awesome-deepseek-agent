[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex

Codex is OpenAI's coding agent, available through Codex CLI, the ChatGPT desktop app, and the Codex IDE extension for VS Code. Codex communicates with models through the OpenAI Responses API, which DeepSeek natively supports.

> **Support note:** At the moment, only `deepseek-v4-flash` supports native Codex integration. Native `deepseek-v4-pro` support is expected in early August 2026. If you need Pro today, use the [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) alternative below.

## Recommended: Native DeepSeek Provider

### 1. Configure DeepSeek as the Model Provider

Before running the setup script, install Codex CLI or the ChatGPT desktop app and launch it at least once so that the `~/.codex` directory exists.

On macOS or Linux, run:

```shell
bash <(curl -fsSL https://cdn.deepseek.com/api-docs/codex-deepseek-setup-en.sh)
```

On Windows PowerShell, run:

```powershell
irm https://cdn.deepseek.com/api-docs/codex-deepseek-setup-en.ps1 | iex
```

Choose `deepseek-v4-flash` from the menu and enter your DeepSeek API key when prompted. The script backs up the existing Codex configuration, writes `~/.codex/models.json`, updates `~/.codex/config.toml`, and validates both files before saving. Run it again to restore the pre-installation configuration or switch models after native Pro support becomes available.

### 2. Configure Manually

Create `~/.codex/models.json` with the full DeepSeek model catalog from the [DeepSeek Codex integration documentation](https://api-docs.deepseek.com/quick_start/agent_integrations/codex), then add the following to `~/.codex/config.toml` (create it if needed):

```toml
model = "deepseek-v4-flash"
model_provider = "deepseek"
preferred_auth_method = "apikey"
forced_login_method = "api"
model_reasoning_effort = "high"
model_catalog_json = "~/.codex/models.json"

[model_providers.deepseek]
name = "deepseek"
base_url = "https://api.deepseek.com/"
wire_api = "responses"
experimental_bearer_token = "<your DeepSeek API Key>"
```

The model catalog supplies Codex with the model's context window, reasoning levels, and tool-call capabilities. Keep the API key private because this configuration stores it directly in `config.toml`.

### 3. Get Started

All Codex clients read the same configuration, so no per-client setup is required. In a project directory, run:

```shell
cd /path/to/my-project
codex
```

The Codex CLI startup banner should show `model: deepseek-v4-flash`. In the ChatGPT desktop app, locally configured models appear under the **Custom** model picker. The VS Code Codex extension shares the same configuration as Codex CLI.

## Alternative: Moon Bridge

Moon Bridge remains useful when you want to use `deepseek-v4-pro` with Codex before native Pro support is available. The proxy setup below also supports both V4 models.

### 1. Install Requirements

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

### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

### 3. Configure Moon Bridge

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
  moonbridge:
    model: deepseek-v4-pro
    provider: deepseek

defaults:
  model: moonbridge
  max_tokens: 65536
```

This minimal config uses the current Moon Bridge configuration structure and enables DeepSeek V4 Pro / Flash, Codex model metadata, and the DeepSeek V4 compatibility extension. **For image input, Web Search, or multi-provider routing**, extend it with the options from Moon Bridge's `config.example.yml`.

### 4. Start Moon Bridge

```shell
go run ./cmd/moonbridge --config config.yml
```

Keep this terminal open. By default Moon Bridge listens on `127.0.0.1:38440` and exposes an OpenAI Responses-compatible endpoint at:

```text
http://127.0.0.1:38440/v1/responses
```

### 5. Generate Codex Configuration

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

### 6. Start Codex

Enter the project you want to work on and launch Codex:

```shell
cd /path/to/my-project
codex
```

Codex now sends OpenAI Responses requests to Moon Bridge, and Moon Bridge routes them to DeepSeek V4.

Codex App can use the same generated Codex configuration.

### One-Command Launcher

Moon Bridge provides a helper script for Codex CLI that can build and start the proxy, generate the Codex config, and launch Codex in one command:

```shell
./scripts/start_codex_with_moonbridge.sh --project-directory /path/to/my-project
```

Windows PowerShell users can use:

```powershell
.\scripts\start_codex_with_moonbridge.ps1 -ProjectDirectory C:\path\to\my-project
```

### Verify

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

### Troubleshooting

- `connection refused`: Moon Bridge is not running, or `server.addr` in `config.yml` uses a different port.
- Codex cannot see the model: rerun step 5; Codex needs `models_catalog.json` in `CODEX_HOME`.
- Config loading fails with `field provider not found`: you are using the old `provider.providers` format. The current format uses top-level `providers`, `models`, `routes`, and `defaults`.
- `401` or authentication errors: check the DeepSeek API key in `config.yml`.
- `402` or payment errors: check your DeepSeek Platform balance.
- Image input fails: if you enabled the Visual extension, configure a separate visual provider (e.g., Kimi) with its API key. You can configure that provider, or remove `visual.enabled: true` to disable the Visual extension.

### Resources

- [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge)
- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek Codex Integration](https://api-docs.deepseek.com/quick_start/agent_integrations/codex)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
