[← Back](../README.md)

# deepclaude

A shell script that runs Claude Code's autonomous agent loop with DeepSeek V4 Pro — same UX, 17x cheaper.

**GitHub:** [github.com/aattaran/deepclaude](https://github.com/aattaran/deepclaude)

## What it does

Claude Code is the best autonomous coding agent — but it costs $200/month with usage caps. deepclaude swaps the model to DeepSeek V4 Pro ($0.87/M output) while keeping Claude Code's tool loop, file editing, bash execution, and autonomous multi-step coding.

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

#### 2. Download deepclaude

```bash
git clone https://github.com/aattaran/deepclaude.git
cd deepclaude
chmod +x deepclaude.sh   # Linux/Mac only
```

#### 3. Run it

**Linux / Mac:**
```bash
./deepclaude.sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File deepclaude.ps1
```

## Commands

```bash
deepclaude                      # DeepSeek V4 Pro (default)
deepclaude -b or                # OpenRouter (cheapest, US servers)
deepclaude -b fw                # Fireworks AI (fastest, US servers)
deepclaude -b anthropic         # Normal Claude Code
deepclaude --remote             # Remote control (browser) + DeepSeek
deepclaude --remote -b or       # Remote control + OpenRouter
deepclaude --status             # Show keys and backends
deepclaude --cost               # Pricing comparison
deepclaude --benchmark          # Latency test
```

## Remote Control

`deepclaude --remote` starts a Claude Code remote-control session with DeepSeek as the brain. It launches a local HTTP proxy that routes model API calls to DeepSeek while keeping Anthropic's bridge auth intact.

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
