[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex

Codex is OpenAI's coding agent, available as a CLI and app. Codex communicates with models through the OpenAI Responses API, so it needs a forwarding layer to handle requests.

There are two approaches — choose the one that fits your setup:

- **[@codeproxy/cli](https://github.com/codeproxy-ai/cli)** — lightweight, npm-based, zero-config (recommended)
- [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) — Go-based, supports advanced routing

---

## Option 1: @codeproxy/cli (Recommended)

> **`@codeproxy/cli`** is a zero-dependency, open-source (MIT) proxy that translates OpenAI Responses API requests into Chat Completions or Anthropic Messages on the fly. No Go, no config generation — just npm.

#### 1. Install Codex CLI

```shell
npm install -g @openai/codex
```

Verify the installation:

```shell
codex --version
```

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Start the Proxy

Run `@codeproxy/cli` with a single command — no clone, no config file needed:

```shell
npx @codeproxy/cli --upstream-format openai-chat \
  --base-url https://api.deepseek.com/v1 \
  --apikey sk-your-deepseek-api-key \
  --port 8787
```

Keep this terminal open. The proxy now listens on `http://127.0.0.1:8787/v1/responses` and translates every request to DeepSeek's Chat Completions API.

#### 4. Configure Codex

Create or edit `~/.codex/config.toml`:

```toml
[model_providers.deepseek]
name = "DeepSeek"
base_url = "http://127.0.0.1:8787/v1"
wire_api = "responses"

[profiles.deepseek-pro]
model = "deepseek-v4-pro"
model_provider = "deepseek"
model_context_window = 1000000
```

For reasoning support:

```toml
[profiles.deepseek-pro]
model = "deepseek-v4-pro"
model_provider = "deepseek"
model_context_window = 1000000
model_reasoning_effort = "high"
```

#### 5. Start Codex

```shell
cd /path/to/my-project
codex
```

#### 6. Verify

```shell
curl http://127.0.0.1:8787/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro",
    "input": "Say hello in one short sentence.",
    "max_output_tokens": 100
  }'
```

#### Tips

- **Multiple upstreams**: Use a config file to switch between DeepSeek, Kimi, Claude, and more — see [config.example.json](https://github.com/codeproxy-ai/cli/blob/main/config.example.json).
- **Vision auto-fallback**: Set `dropImages: true` and a `fallback` upstream to route image requests to a vision-capable model like Kimi K2.6.
- **Reasoning effort**: `@codeproxy/cli` automatically maps `reasoning.effort` to the upstream's native format.

---

## Option 2: Moon Bridge

[View Original Guide](#) (scroll down)

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

provider:
  providers:
    deepseek:
      base_url: "https://api.deepseek.com/anthropic"
      api_key: "sk-your-deepseek-api-key"
      models:
        deepseek-v4-pro:
          context_window: 1000000
          max_output_tokens: 384000
          extensions:
            deepseek_v4:
              enabled: true
          default_reasoning_level: "high"
          supported_reasoning_levels:
            - effort: "high"
              description: "High reasoning effort"
            - effort: "xhigh"
              description: "Extra high reasoning effort"
          supports_reasoning_summaries: true
          default_reasoning_summary: "auto"
  routes:
    moonbridge:
      to: "deepseek/deepseek-v4-pro"
  default_model: "moonbridge"
```

This minimal config enables DeepSeek V4 Pro, Codex model metadata, and the DeepSeek V4 compatibility extension. For image input, Web Search, or multi-provider routing, extend it with the options from Moon Bridge's `config.example.yml`.

#### 4. Start Moon Bridge

```shell
go run ./cmd/moonbridge --config config.yml
```

Keep this terminal open. By default Moon Bridge listens on `127.0.0.1:38440` and exposes an OpenAI Responses-compatible endpoint at:

```text
http://127.0.0.1:38440/v1/responses
```

#### 5. Generate Codex Configuration

In another terminal, from the Moon Bridge directory, generate Codex's `config.toml` and `models_catalog.json`:

```shell
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME_DIR"

MODEL="$(go run ./cmd/moonbridge --config config.yml --print-codex-model)"
go run ./cmd/moonbridge \
  --config config.yml \
  --print-codex-config "$MODEL" \
  --codex-base-url "http://127.0.0.1:38440/v1" \
  --codex-home "$CODEX_HOME_DIR" \
  > "$CODEX_HOME_DIR/config.toml"
```

This writes:

- `config.toml`: Codex provider configuration using `wire_api = "responses"`.
- `models_catalog.json`: model capability metadata for Codex, including context window, reasoning levels, and tool support.

#### 6. Start Codex

Enter the project you want to work on and launch Codex:

```shell
cd /path/to/my-project
CODEX_HOME="$CODEX_HOME_DIR" codex --cd "$PWD"
```

Codex now sends OpenAI Responses requests to Moon Bridge, and Moon Bridge routes them to DeepSeek V4.

Codex App can use the same generated Codex configuration.

#### One-Command Launcher

Moon Bridge provides a helper script for Codex CLI that can build and start the proxy, generate the Codex config, and launch Codex in one command:

```shell
./scripts/start_codex_with_moonbridge.sh --project-directory /path/to/my-project
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
    "max_output_tokens": 100
  }'
```

After Codex sends a message, the Moon Bridge terminal should show a `POST /v1/responses` log line.

#### Troubleshooting

- `connection refused`: Moon Bridge is not running, or `server.addr` in `config.yml` uses a different port.
- Codex cannot see the model: rerun step 5; Codex needs `models_catalog.json` in `CODEX_HOME`.
- `401` or authentication errors: check the DeepSeek API key in `config.yml`.
- `402` or payment errors: check your DeepSeek Platform balance.
- Image input fails: if you enabled the Visual extension, configure a separate visual provider (e.g., Kimi) with its API key. You can configure that provider, or remove `visual.enabled: true` to disable the Visual extension.

#### Resources

- [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge)
- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
