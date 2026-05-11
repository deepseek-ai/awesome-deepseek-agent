[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex

Codex is OpenAI's coding agent, available as a CLI and app. Codex communicates with models through the OpenAI Responses API, so it needs a forwarding layer to handle requests.

## Choose a Proxy

| Solution | Description |
| -------- | ----------- |
| [@codeproxy/cli](https://github.com/codeproxy-ai/cli) | Lightweight, npm-based proxy. Translates Responses API to Chat Completions or Anthropic Messages. No Go required. |
| [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) | Go-based proxy with advanced routing, model catalog auto-generation, and DeepSeek V4 extensions. |

Follow the respective project's README to start the proxy. Once it is running, proceed to configure Codex below.

## Configure Codex

Create or edit `~/.codex/config.toml` to point Codex at your proxy:

```toml
[model_providers.deepseek]
name = "DeepSeek"
base_url = "http://127.0.0.1:8787/v1"
wire_api = "responses"

[profiles.deepseek-pro]
model = "deepseek-v4-pro"
model_provider = "deepseek"
model_context_window = 1000000
model_reasoning_effort = "high"
```

> **Note:** Adjust `base_url` and port to match your proxy's listen address.

## Verify

```shell
curl http://127.0.0.1:8787/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro",
    "input": "Say hello in one short sentence.",
    "max_output_tokens": 100
  }'
```

## Start Codex

```shell
cd /path/to/my-project
codex
```

## Resources

- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
