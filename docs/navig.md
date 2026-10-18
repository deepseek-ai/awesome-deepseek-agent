[English](./navig.md) | [简体中文](./navig.zh-CN.md) · [← Back](../README.md)

# Integrate with NAVIG

NAVIG is a local-first AI operator OS: a Python kernel with a CLI, an installable desktop shell, and
one OpenAI-compatible endpoint (`navig serve`) that any other coding client can point at. Provider
keys live on your machine, in a vault — not in a client's config file — and every call is priced.

#### 1. Install NAVIG

- Install [Python](https://www.python.org/downloads/) 3.10 or newer.
- Run the following command in your terminal:

```bash
pip install navig
```

- Verify the installation:

```bash
navig --version
navig doctor
```

#### 2. Connect DeepSeek

```bash
navig ai connect deepseek
```

The wizard asks for your DeepSeek API key and stores it in NAVIG's vault. If you prefer environment
variables, export `DEEPSEEK_API_KEY` instead — NAVIG discovers it automatically.

Both DeepSeek endpoint shapes are supported, with the same key:

| Shape | Base URL |
|---|---|
| OpenAI (`/v1/chat/completions`) | `https://api.deepseek.com` |
| Anthropic (`/v1/messages`) | `https://api.deepseek.com/anthropic` |

#### 3. First run

```bash
navig ai ask "summarise the failing tests in this repo"
navig cost history
```

`navig cost history` prints a priced receipt per session — token counts and USD — from NAVIG's
audited price table.

#### 4. Use DeepSeek from any other client

`navig serve` exposes NAVIG's providers on a loopback OpenAI-compatible endpoint, so Kilo Code,
Cline, opencode, crush, goose, Continue, Aider or OpenHands can use DeepSeek without holding the key:

```bash
navig serve token new --label crush --budget 5   # prints an nv_… token once
navig serve start                               # http://127.0.0.1:8788/v1
```

Then, in the client:

- **Base URL**: `http://127.0.0.1:8788/v1`
- **API key**: the `nv_…` token
- **Model**: `deepseek:deepseek-v4-pro` or `deepseek:deepseek-flash`

The endpoint answers loopback peers only, refuses a call once the token's budget is spent (before the
request, not after), and writes a priced receipt per request.

> **Claude Code** does not use this endpoint: it speaks Anthropic Messages only. Point it at
> `https://api.deepseek.com/anthropic` directly instead, and append `[1m]` to the model name (see
> below).

#### Notes

- **Current model names.** DeepSeek's pricing page (October 2026) names the two models
  `deepseek-v4-pro` and `deepseek-flash`. The API still accepts `deepseek-v4-flash` and
  `deepseek-v4-flash-vision-exp` as aliases (served by the Flash model); the older `deepseek-chat` /
  `deepseek-r1` names are retired and also served by Flash. NAVIG ships both current ids as
  first-class providers and prices the retired names at the Flash rate rather than dropping them.
- **1M context.** DeepSeek V4 models support up to 1,000,000 tokens of context and 384K output.
  NAVIG's provider entry declares `context_window=1000000`. For Anthropic-compatible clients, append
  `[1m]` to the model name (`deepseek-v4-pro[1m]`) per DeepSeek's guidance.
- **Reasoning.** DeepSeek V4 Pro supports `max` and `high` reasoning effort and defaults to thinking
  mode. NAVIG's provider entry marks both DeepSeek models as reasoning-capable; clients that talk to
  `api.deepseek.com` directly can send `reasoning_effort` in the request body.
- **Vision.** `deepseek-flash` (V4.1) accepts images; `deepseek-v4-pro` does not.
- **Pricing.** NAVIG prices both ids from DeepSeek's published list (off-peak rates, with the peak
  multiplier noted in the source). Always confirm current rates on the
  [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing).

#### Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `401 invalid_api_key` from a client | the token was revoked or never minted — `navig serve token new` |
| `429 budget_exhausted` | that token reached its `--budget`; mint a new token with a larger one |
| `400 … streaming is not implemented` | send `stream: false`; `navig serve` streams in a later release |
| `403 permission_error` | the request did not come from `127.0.0.1` — the endpoint is loopback-only by design |
