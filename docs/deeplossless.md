# DeepLossless — Inference-aware Execution Runtime for DeepSeek

DeepLossless is an **inference-aware coding runtime** that reduces repeated
work in long AI coding sessions. It sits as an OpenAI-compatible proxy between
your coding agent and the DeepSeek API, adding:

- **Tool cache interception** — repeated grep/search calls return cached
  results inline, without API round-trips
- **DAG context assembly** — important details survive across hundreds of
  turns, even when the chat window overflows
- **Failure memory** — known-bad fixes are recorded and avoided
- **Execution replay** — append-only event log enables deterministic replay
  and audit trails

DeepSeek V4 Pro and V4 Flash (both with 1M context) make long coding
sessions economically viable. DeepLossless adds execution memory on top.

## Installation

```bash
cargo install deeplossless
```

Requirements: Rust 1.85+, SQLite (bundled).

## Configuration

### 1. Start the proxy

```bash
export DEEPSEEK_API_KEY=sk-...
deeplossless
# Listening on http://127.0.0.1:8080
```

Optional flags:

| Flag | Default | Purpose |
|------|---------|---------|
| `--port` | `8080` | Listen port |
| `--upstream` | `https://api.deepseek.com` | API base URL |
| `--db-path` | `~/.deeplossless/lcm.db` | SQLite database |
| `--log-dir` | (disabled) | Per-request JSON metrics |
| `--runtime-profile` | `autonomous` | Cache/retry/context strategy |

### 2. Connect your agent

Point any OpenAI-compatible client to `http://127.0.0.1:8080/v1`.

**Codex** (Responses API):
```toml
# ~/.codex/config.toml
[model_providers.localproxy]
name = "deeplossless"
base_url = "http://127.0.0.1:8080/v1"
wire_api = "responses"
env_key = "DEEPSEEK_API_KEY"
```

**OpenCode** (Chat Completions):
```json
{
  "provider": {
    "deeplossless": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://127.0.0.1:8080/v1" }
    }
  }
}
```

**Any OpenAI-compatible client**:
```bash
export OPENAI_BASE_URL=http://127.0.0.1:8080/v1
export OPENAI_API_KEY=sk-...
```

## Model Names

DeepLossless uses DeepSeek's current models and auto-maps third-party names:

| Agent requests | Routed to |
|---------------|-----------|
| `deepseek-v4-pro` | `deepseek-v4-pro` (1M context) |
| `deepseek-v4-flash` | `deepseek-v4-flash` (1M context) |
| `gpt-5`, `gpt-5.5`, `o3` | `deepseek-v4-pro` |
| `gpt-*-mini` | `deepseek-v4-flash` |

Both DeepSeek V4 Pro and V4 Flash support 1M token context windows. The
runtime's DAG assembly ensures important context survives even when the raw
conversation history exceeds the context window.

## Verification

### Step 1 — Smoke test (no API key)

```bash
deeplossless demo
```

This runs a local smoke test to verify the binary installed correctly. No API
key or network access required.

### Step 2 — Start with an API key

```bash
export DEEPSEEK_API_KEY=sk-...
deeplossless

# Expected output:
# deeplossless listening on 127.0.0.1:8080
# upstream: https://api.deepseek.com
```

### Step 3 — Non-streaming chat

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"Say hello in one word"}]}' \
  | jq '.choices[0].message.content'
```

Should return a simple greeting.

### Step 4 — Streaming chat

```bash
curl -sN http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"Count to 3"}],"stream":true}'
```

Should output SSE chunks (`data: {...}`) ending with `data: [DONE]`.

### Step 5 — Responses API (Codex path)

```bash
curl -sN http://127.0.0.1:8080/v1/responses \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"input":"Say hi","model":"deepseek-v4-flash"}' \
  | head -20
```

Should output Responses API SSE events (`event: response.created`, etc.).

### Step 6 — Runtime stats

```bash
curl -s http://127.0.0.1:8080/v1/lcm/runtime/stats \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  | jq .
```

Shows cache hit/miss, token counts, runtime profile.

### Troubleshooting

If step 2 fails with `address already in use`, change the port:

```bash
deeplossless --port 8081
```

If steps 3-5 return errors, check:

1. The API key has access to DeepSeek V4 models
2. The proxy log shows `upstream response received status=200` for successful requests
3. Enable `--log-dir /tmp/logs` to see per-request diagnostics

## Pricing

See [DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing)
for current pricing. DeepLossless adds no additional API costs — it runs
locally and only forwards requests to your DeepSeek account.

The runtime can reduce token consumption by:
- Intercepting repeated tool calls (cache hits avoid re-execution)
- Injecting DAG context (fewer re-reads of unchanged files)
- Recording failure patterns (fewer retries of known-bad fixes)

Monitor savings with:
```bash
curl http://127.0.0.1:8080/v1/lcm/runtime/stats | jq .
```

## More

- [README](https://github.com/gordonlu/deeplossless) — full documentation
- [Agent Integration Guide](https://github.com/gordonlu/deeplossless/blob/master/agent_integration.md)
- [Contributing](https://github.com/gordonlu/deeplossless/blob/master/CONTRIBUTING.md)
