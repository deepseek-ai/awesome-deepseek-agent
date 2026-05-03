[← Back](../README.md)

# cheapclaude

A shell script that runs Claude Code's autonomous agent loop with DeepSeek V4 Pro — same UX, 17x cheaper.

**GitHub:** [github.com/aattaran/cheapclaude](https://github.com/aattaran/cheapclaude)

## What it does

Claude Code is the best autonomous coding agent — but it costs $200/month with usage caps. cheapclaude swaps the model to DeepSeek V4 Pro ($0.87/M output) while keeping Claude Code's tool loop, file editing, bash execution, and autonomous multi-step coding.

Supports DeepSeek (direct), OpenRouter, and Fireworks AI as backends.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- [DeepSeek API key](https://platform.deepseek.com/api_keys) (or OpenRouter/Fireworks key)

## Quick Start

#### 1. Set your API key

**Linux / Mac:**
```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```

**Windows (PowerShell):**
```powershell
setx DEEPSEEK_API_KEY "sk-your-key-here"
```

#### 2. Download cheapclaude

```bash
git clone https://github.com/aattaran/cheapclaude.git
cd cheapclaude
chmod +x cheapclaude.sh   # Linux/Mac only
```

#### 3. Run it

**Linux / Mac:**
```bash
./cheapclaude.sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File cheapclaude.ps1
```

## Commands

```bash
cheapclaude                      # DeepSeek V4 Pro (default)
cheapclaude -b or                # OpenRouter (cheapest, US servers)
cheapclaude -b fw                # Fireworks AI (fastest, US servers)
cheapclaude -b anthropic         # Normal Claude Code
cheapclaude --remote             # Remote control (browser) + DeepSeek
cheapclaude --remote -b or       # Remote control + OpenRouter
cheapclaude --status             # Show keys and backends
cheapclaude --cost               # Pricing comparison
cheapclaude --benchmark          # Latency test
```

## Remote Control

`cheapclaude --remote` starts a Claude Code remote-control session with DeepSeek as the brain. It launches a local HTTP proxy that routes model API calls to DeepSeek while keeping Anthropic's bridge auth intact.

```
claude remote-control
  ├── Bridge WebSocket → Anthropic (hardcoded, auth)
  └── Model API calls  → local proxy → DeepSeek ($0.87/M)
```

Requires a claude.ai subscription (the bridge is Anthropic infrastructure).

## Pricing

| Backend | Input/M | Output/M | Cache Hit/M |
|---|---|---|---|
| DeepSeek | $0.44 | $0.87 | $0.004 |
| OpenRouter | $0.44 | $0.87 | (provider) |
| Fireworks | $1.74 | $3.48 | (provider) |
| Anthropic | $3.00 | $15.00 | $0.30 |

Heavy daily use costs ~$2-5/day vs $200/month on Anthropic Max.
