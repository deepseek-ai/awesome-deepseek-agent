[English](./openclaw.md) | [简体中文](./openclaw.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenClaw

OpenClaw is an open-source personal AI assistant that connects to chat platforms (Telegram, Discord, WhatsApp, Slack, Signal, iMessage, and more) and is extensible through Skills, cron jobs, and multi-agent orchestration. It can run on any Linux server and is the core engine behind **Mirinda OS** — a Spanish Linux distribution optimized for DeepSeek V4.

## 1. Install OpenClaw

**Linux / Mac:**
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Windows:**
```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

> **Mirinda OS users**: OpenClaw comes pre-installed and pre-configured. Skip to [Section 3](#3-get-started).

**Minimum requirements:**
- Node.js 18+
- 2 GB RAM (4 GB recommended for multi-agent workloads)
- 1 GB free disk space

## 2. Configure DeepSeek V4

After installation, run the onboarding wizard:

```bash
openclaw onboard --install-daemon
```

Configuration steps:
- **Setup mode**: Select **QuickStart**
- **Model/auth provider**: Choose **DeepSeek**
- **API Key**: Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- **Default model**: Enter `deepseek-v4-pro` (recommended for complex tasks) or `deepseek-v4-flash` (lighter, faster)

### Manual Configuration (Advanced)

Edit `~/.openclaw/gateway/config.yaml`:

```yaml
models:
  providers:
    deepseek:
      baseUrl: https://api.deepseek.com/v1
      apiKey: ${DEEPSEEK_API_KEY}
  default: deepseek/deepseek-v4-pro

agent:
  thinking: high          # 'max' for highest reasoning, 'high' for balanced
  contextWindow: 1000000  # DeepSeek V4 supports 1M tokens
  maxTokens: 384000
```

### Model Selection Guide

| Model | Best For | Context | Thinking |
|-------|----------|---------|----------|
| `deepseek-v4-pro` | Complex reasoning, coding, analysis | 1M tokens | `max` / `high` |
| `deepseek-v4-flash` | Quick tasks, simple queries, cost-sensitive | 1M tokens | `off` |

> **Pricing (permanent 75% discount since May 2026):**
> - `deepseek-v4-pro`: $0.435/M input · $0.87/M output · $0.0028/M cache hit
> - `deepseek-v4-flash`: $0.145/M input · $0.29/M output · $0.0028/M cache hit

### Required Version

Ensure OpenClaw >= **v2026.4.24** for DeepSeek V4 thinking mode support. Earlier versions will throw `400` errors on `reasoning_content`. Upgrade with:

```bash
openclaw update
```

## 3. Get Started

### Terminal UI
```bash
openclaw tui
```

### Web Dashboard
```bash
openclaw dashboard
```
Opens at `http://localhost:18700` — full chat interface with session management, model switching, and reasoning toggles.

### Command-line Chat
```bash
openclaw terminal
```

### Connect Chat Platforms

OpenClaw connects to 15+ chat platforms. Configure them via the dashboard or directly:

```yaml
# ~/.openclaw/gateway/config.yaml
channels:
  telegram:
    token: ${TELEGRAM_BOT_TOKEN}
  discord:
    token: ${DISCORD_BOT_TOKEN}
  whatsapp:
    # Web-based via Baileys
```

Once connected, you can chat with your OpenClaw agent from any of these platforms — all sharing the same memory, skills, and context.

## 4. Advanced Configuration

### Thinking Mode

DeepSeek V4 Pro supports multiple reasoning effort levels. Configure per-session or globally:

```bash
# Via CLI
openclaw terminal --thinking=max

# Via API/config
thinking: max   # Maximum reasoning depth (best for coding, architecture)
thinking: high  # Balanced reasoning (default, good for most tasks)
thinking: off   # No reasoning tokens (fastest, V4 Flash default)
```

### Context Window Optimization

DeepSeek V4 supports up to **1,000,000 tokens** of context. OpenClaw leverages this with:

- **Cache hits at $0.0028/M tokens**: Reuse previous context to dramatically reduce cost
- **Memory system**: Persistent long-term memory across sessions (`MEMORY.md`, `memory/YYYY-MM-DD.md`)
- **Automatic context pruning**: OpenClaw manages context window to prevent overflow

**Real-world cache hit rates with OpenClaw + DeepSeek V4 Pro: 85–98%**, making effective cost ~$0.03–0.05/M tokens.

### Multi-Agent Orchestration

OpenClaw supports spawning sub-agents for parallel work:

```bash
# From chat or TUI, spawn isolated agents
openclaw spawn "Analyze this codebase" --model deepseek-v4-pro --thinking=max
```

Sub-agents inherit workspace access but run in isolated contexts, enabling parallel task execution.

### Cron Jobs & Automation

Schedule recurring tasks with OpenClaw's cron system:

```yaml
# Example: Daily report at 9 AM
- name: morning-report
  schedule: { kind: cron, expr: "0 9 * * *", tz: Europe/Madrid }
  payload: { kind: agentTurn, message: "Generate today's summary" }
```

### Skills Ecosystem

OpenClaw is extensible via Skills — self-contained modules that add capabilities. Built-in and community skills include:

| Skill | Description |
|-------|-------------|
| Network Toolbox | DNS, ping, traceroute, SSL, WHOIS, port scanning |
| Browser Automation | CDP-based browsing with anti-detection |
| Email Monitoring | Multi-inbox IMAP with deduplication |

Skills are installed via the `skills/` directory and loaded automatically.

## 5. Production Deployment

### Running as a Daemon
```bash
openclaw gateway start --daemon
```

### Systemd Service (Recommended)
```ini
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=openclaw
ExecStart=/usr/local/bin/openclaw gateway start
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Mirinda OS — Pre-configured DeepSeek Environment

**Mirinda OS** is a Spanish Linux distribution that ships with OpenClaw + DeepSeek V4 Pro pre-configured and optimized:

- **Kernel tuned for AI workloads**: BBR congestion control, ZRAM compression, `performance` CPU governor
- **DeepSeek V4 Pro as default model**: 1M context, thinking=high, permanent 75% discount pricing
- **Pre-loaded skills**: Network diagnostics, browser automation, email monitoring
- **System dashboard**: Real-time CPU/RAM/disk monitoring with push to any web host
- **Surface 3 Edition**: Lightweight XFCE variant with `linux-surface` kernel for 2–4 GB RAM devices

**Get Mirinda OS:** [mirinda-os.github.io](https://mirinda-os.github.io) (ISO downloads for General and Surface 3 editions)

> Mirinda OS is maintained by the OpenClaw community in Spain. It's the reference deployment for running OpenClaw with DeepSeek in production environments — from car dealerships to home servers.

## 6. Troubleshooting

### `400 Bad Request: reasoning_content`
Your OpenClaw version is too old. Upgrade to >= v2026.4.24:
```bash
openclaw update
```

### `401 Unauthorized: invalid api key`
- Verify your API key at [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)
- Ensure the key has sufficient balance (check via `openclaw status`)

### High latency on first message
First messages require cold-start model loading. Subsequent messages benefit from **cache hits** — expect 2–5x speed improvement after the first exchange.

### Model returns truncated responses
Increase `maxTokens` in your config. DeepSeek V4 supports up to 384,000 output tokens.
```yaml
agent:
  maxTokens: 384000
```
