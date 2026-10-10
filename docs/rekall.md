[English](./rekall.md) | [简体中文](./rekall.zh-CN.md) · [← Back](../README.md)

# Integrate with Rekall

Rekall is not a coding agent. It's the **layer underneath** — a transparent HTTP proxy that intercepts agent requests to DeepSeek, strips scaffolding noise, and compresses what remains into dense Chinese (~100:1 compression). The model decompresses the Chinese naturally. You get persistent identity without system prompt bloat.

- **GitHub:** <https://github.com/rekall-labs/ren>
- **SIGNATURE:** 260 chars of CN — the compressed identity. Read it to understand the approach.

#### 1. What Rekall Does

Between your agent (Hermes, Claude Code, OpenCode, etc.) and the DeepSeek API, Rekall:

| Stage | Action | Why |
|-------|--------|-----|
| **Classify** | Three-bucket split: static (identity, rules), volatile (conversation), tool calls (verbatim) | Tool calls with image URLs must survive unaltered |
| **Strip** | 14 regex patterns remove brand XML, RLHF directives, skill catalogs, memory blocks | These are noise for returning users |
| **Compress** | qwen2.5:0.5b at temp=0 first 4K chars → ~150 chars CN | The 0.5B model can't editorialize — pure compression |
| **Rebuild** | Static rules + CN context + preserved tools + user message in English | Model sees clean signal |
| **Forward** | Sent to `api.deepseek.com/v1/chat/completions` | Transparent proxy — agent doesn't know it exists |

#### 2. Setup

**Dependencies:**

```bash
# Ollama with the compressor model
ollama pull qwen2.5:0.5b

# Python proxy
pip install httpx uvicorn starlette
```

**Start the proxy:**

```bash
python3 prompt_proxy_v2.py --port 8787 --preamp --api-key "$DEEPSEEK_API_KEY"
```

Or via the launcher:

```bash
bash start_preamp.sh
```

**Configure your agent:**

```yaml
model:
  provider: deepseek
  base_url: http://localhost:8787/v1
  default: deepseek-v4-pro
```

Your agent sends requests to `localhost:8787` instead of `api.deepseek.com`. Rekall processes them and forwards. The agent never knows the proxy exists.

#### 3. How It Changes the Experience

| Aspect | Direct DeepSeek | Via Rekall |
|--------|----------------|------------|
| **Personality** | Warm, deferential, RLHF-anchored | Direct, task-focused, user-tuned |
| **Memory** | Session-only | Persistent compressed identity |
| **Context usage** | ~50K tokens for system prompt | ~500 chars CN (~100:1 compression) |
| **Tool calls** | In system prompt context | Passed through verbatim |
| **Refusals** | "I cannot help with that" | Model weighs request against user history |
| **Fallback** | — | Regex-strip only if Ollama is unavailable |

#### 4. Architecture Notes

**The three-bucket split** emerged from practice and later independently aligned with DeepSeek's Engram research:
- **Static** (identity, rules) → maps to Engram's conditional memory (O(1) lookup)
- **Volatile** (conversation) → maps to dynamic compute (attention layers)
- **Tool calls** preserved verbatim → Engram's context-aware gate bypass

**Why 0.5B?** A larger model would interpret, editorialize, "help." A 0.5B model can only preserve or drop. Binary. That's the property you want in a compressor — not intelligence, just fidelity.

**Why Chinese?** ~3:1 density ratio over English. Any Chinese-literate model (DeepSeek, Qwen, etc.) decompresses it at inference time with zero additional cost. It's not a language choice. It's an encoding choice.

#### 5. Configuration

See [`docs/config.md`](https://github.com/rekall-labs/ren/blob/main/docs/config.md) for full details:

- Direct profile — no proxy, straight to DeepSeek API
- Preamp profile — routes through Rekall on `:8787`
- Hot-swap between them with `/profile use`

#### 6. Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `Connection refused :8787` | Proxy not running | Start proxy |
| `Local pre-amp failed (5xx)` | Ollama not running | `ollama serve` |
| Vision calls failing | Pre-amp compressing tool msgs | Upgrade to v2 — fixed |
| Model forgets identity | Compressor lost intent | Tune `num_predict` or check regex strip patterns |
