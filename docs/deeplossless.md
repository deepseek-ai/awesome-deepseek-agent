# DeepLossless — Inference-aware Execution Runtime for DeepSeek

DeepLossless is an **inference-aware coding runtime** that reduces repeated
work in long AI coding sessions. It sits as an HTTPS proxy between
your coding agent and the DeepSeek API, adding:

- **Tool cache interception** — repeated grep/search calls return cached
  results inline, without API round-trips
- **DAG context assembly & compaction** — important details survive across
  hundreds of turns; 3383+ leaf nodes auto-compacted to fit the context window
- **Failure memory** — known-bad fixes are recorded and avoided
- **File claim/conflict detection** — parallel agents coordinate file access
- **Execution replay** — append-only event log enables deterministic replay
  and audit trails
- **Cross-session search** — search DAG summaries and snippets from past
  conversations

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
# Listening on https://127.0.0.1:8080 (HTTPS with auto-generated cert)
# HTTP fallback on http://127.0.0.1:8081 (for sandboxed agents)
```

TLS certificates are auto-generated on first run. Run `deeplossless trust` once
to install the self-signed cert as system-trusted.

Optional flags:

| Flag | Default | Purpose |
|------|---------|---------|
| `--port` | `8080` | HTTPS listen port |
| `--http-port` | `8081` | Plain HTTP port (0 = disable) |
| `--upstream` | `https://api.deepseek.com` | API base URL |
| `--db-path` | `~/.deeplossless/lcm.db` | SQLite database |
| `--api-key` | (from env) | DeepSeek API key |
| `--admin-key` | (none) | Separate admin key for LCM endpoints |
| `--runtime-profile` | `autonomous` | Cache/retry/context strategy |
| `--dag-threshold` | `0.80` | Compaction trigger (fraction of context window) |
| `--summarizer-budget` | `1000` | Max LLM summarizer calls per session |
| `--lcm-context` | (off) | Enable DAG context injection into system messages |
| `--tls-cert` / `--tls-key` | (auto) | Custom TLS certificate |

### 2. Connect your agent

Point any OpenAI-compatible client to `https://127.0.0.1:8080/v1`.
No API key needed — deeplossless auto-injects the server-side key for localhost.

**Codex** (Responses API):
```toml
# ~/.codex/config.toml
[model_providers.localproxy]
name = "deeplossless"
base_url = "https://127.0.0.1:8080/v1"
wire_api = "responses"
env_key = "DEEPSEEK_API_KEY"
```

**OpenCode** (Chat Completions):
```json
{
  "provider": {
    "deeplossless": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "https://127.0.0.1:8080/v1" }
    }
  }
}
```

**OpenClaw** (sandboxed, Responses API):
```json
{
  "api_key": "dummy",
  "base_url": "http://127.0.0.1:8081/v1",
  "wire_api": "responses"
}
```
Use HTTP port 8081 for sandboxed agents — they can't access host env vars
or trust self-signed certs.

**Claude Code** (via SKILL.md):
```bash
cp SKILL.md .claude/skills/deeplossless.md
```

## Model Names

DeepLossless uses DeepSeek's current models:

| Agent requests | Routed to |
|---------------|-----------|
| `deepseek-v4-pro` | `deepseek-v4-pro` (1M context) |
| `deepseek-v4-flash` | `deepseek-v4-flash` (1M context) |

Both support 1M token context windows and `reasoning_effort` control
(DeepSeek's thinking mode). The runtime's DAG assembly and
auto-compaction ensure important context survives even when the raw
conversation history exceeds the context window.

## LCM Endpoints (Lossless Context Management)

All endpoints are localhost-only (no auth needed):

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/lcm/current` | Discover conversation ID |
| `GET /v1/lcm/grep/{id}?query=&limit=20` | Search past context (current session) |
| `GET /v1/lcm/global/search?q=&limit=10` | Cross-session search with excerpts |
| `GET /v1/lcm/cache?tool=&args=` | Check tool cache before executing |
| `POST /v1/lcm/cache/put` | Store tool result |
| `DELETE /v1/lcm/cache?tool=&args=` | Delete cached result |
| `POST /v1/lcm/failure` | Record a failed fix |
| `POST /v1/lcm/plan` | Store execution plan |
| `GET /v1/lcm/plan/{id}` | Get active plan |
| `DELETE /v1/lcm/plan?id=` | Delete plan |
| `POST /v1/lcm/file/claim` | Claim a file before editing |
| `POST /v1/lcm/file/release` | Release file claim |
| `GET /v1/lcm/execution/search?q=` | Search execution memory |
| `GET /v1/lcm/runtime/stats` | Cache hits, tokens, failures |
| `GET /v1/lcm/health/{id}` | DAG integrity check |

## Verification

### Step 1 — Smoke test (no API key)

```bash
deeplossless demo
```

### Step 2 — Start with an API key

```bash
export DEEPSEEK_API_KEY=sk-...
deeplossless

# Expected output:
# deeplossless v0.6.0 listening on 127.0.0.1:8080
# HTTPS on 127.0.0.1:8080
# HTTP on 127.0.0.1:8081 (for sandboxed local agents)
# upstream: https://api.deepseek.com
```

### Step 3 — Non-streaming chat

```bash
curl -sk https://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"Say hello in one word"}]}' \
  | jq '.choices[0].message.content'
```

### Step 4 — Streaming chat

```bash
curl -skN https://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"Count to 3"}],"stream":true}'
```

### Step 5 — Runtime stats

```bash
curl -sk https://127.0.0.1:8080/v1/lcm/runtime/stats | jq .
```

### Step 6 — Search past context

```bash
# Get conversation ID
curl -sk https://127.0.0.1:8080/v1/lcm/current

# Search
curl -sk "https://127.0.0.1:8080/v1/lcm/grep/1?query=your+search&limit=10"
```

### Troubleshooting

If startup fails with `address already in use`, change the port:
```bash
deeplossless --port 8443 --http-port 8082
```

If chat requests return errors, check:
1. The API key has access to DeepSeek V4 models
2. `curl -sk https://127.0.0.1:8080/health` returns `{"status":"healthy"}`
3. Enable `--log-dir /tmp/logs` to see per-request diagnostics

If sandboxed agents get TLS errors, use the HTTP port:
```bash
# Agent config: base_url = http://127.0.0.1:8081/v1
```

## Pricing

See [DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing)
for current pricing. DeepLossless adds no additional API costs.

The runtime can reduce token consumption by:
- Intercepting repeated tool calls (cache hits avoid re-execution)
- Auto-compacting conversation history (DAG context vs raw history)
- Recording failure patterns (fewer retries of known-bad fixes)

Monitor savings with:
```bash
curl -sk https://127.0.0.1:8080/v1/lcm/runtime/stats | jq .
```

## More

- [README](https://github.com/gordonlu/deeplossless) — full documentation
- [Agent Integration Guide](https://github.com/gordonlu/deeplossless/blob/master/agent_integration.md)
- [SKILL.md](https://github.com/gordonlu/deeplossless/blob/master/SKILL.md) — agent-installable skill file
