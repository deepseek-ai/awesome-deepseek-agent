[English](./hermes.md) | [简体中文](./hermes.zh-CN.md) · [← Back](../README.md)

# Integrate with Hermes Agent

Hermes is a self-improving AI agent built by [Nous Research](https://nousresearch.com). It includes a built-in learning loop: it creates skills from experience, improves them during use, persists knowledge across sessions, and builds an evolving model of your preferences over time.

Hermes supports DeepSeek V4 Pro and V4 Flash as its primary models through multiple provider backends, giving you flexibility between maximum capability and cost efficiency.

> **DeepSeek V4 models are the recommended primary models for Hermes.** They offer the best balance of reasoning capability, context length (1M tokens), and cost for agentic workflows.

---

#### 1. Install Hermes

##### Quick Install

Get Hermes Agent up and running in under two minutes with the one-line installer.

###### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

The only prerequisite is Git. The installer automatically handles everything else.

For more installation instructions, please refer to the [Hermes installation page](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

#### 2. Configure DeepSeek as Your Provider

##### Option A: Quick Setup (Auto-Configuration)

Reload your shell and start Hermes configuration:

- Execute the `hermes setup` command
- Choose the **Quick Setup** option
- When prompted for the model provider, select **DeepSeek**
- Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- Enter the Base URL as `https://api.deepseek.com`
- Select `deepseek-v4-pro` (recommended for complex reasoning) or `deepseek-v4-flash` (faster, lower cost)
- Continue with the remaining options

##### Option B: Manual Configuration (Advanced)

For fine-grained control, edit `~/.hermes/config.yaml` directly:

```yaml
model:
  default: deepseek-v4-pro
  provider: deepseek

providers:
  deepseek:
    api_key: ${DEEPSEEK_API_KEY}     # Set via env var or paste directly
    base_url: https://api.deepseek.com
    type: openai_compatible
```

To enable 1M context window, append `[1m]` to the model name:

```yaml
model:
  default: deepseek-v4-pro[1m]           # Enables 1M context
```

##### Option C: OpenCode Go Provider (Recommended for Coding)

For native terminal-based coding with DeepSeek, configure Hermes to use the [OpenCode Go](https://github.com/opencode-ai/opencode) provider. This is the setup used by [GenTech Labs](https://github.com/ProtoJay4789) in production — running 24/7 with DeepSeek V4 Flash as the primary model.

```bash
# Install OpenCode Go
curl -fsSL https://opencode.ai/install.sh | bash
```

Then configure Hermes:

```yaml
model:
  default: deepseek-v4-flash
  provider: opencode-go

providers:
  opencode-go:
    api_key: ${DEEPSEEK_API_KEY}
    base_url: https://api.deepseek.com
    type: openai_compatible
```

#### 3. Model Routing with Multiple Profiles

A powerful pattern is to run two Hermes profiles for cost-optimized model routing — use V4 Flash for drafting and rapid iteration, and V4 Pro for deep analysis:

```bash
# Create a second profile
hermes profile create deepseek-pro
```

Configure each profile with a different model:

| Profile | Model | Use Case |
|---------|-------|----------|
| `default` | `deepseek-v4-flash` | Daily tasks, drafting, rapid iteration |
| `deepseek-pro` | `deepseek-v4-pro[1m]` | Code audits, complex reasoning, 1M context |

Switch between profiles at any time:

```bash
hermes profile switch deepseek-pro
```

#### 4. Thinking / Reasoning Effort

DeepSeek V4 Pro supports configurable reasoning levels. For Claude Code-compatible endpoints, set:

```bash
export CLAUDE_CODE_EFFORT_LEVEL=max
```

For OpenAI-compatible providers, include `reasoning_effort` in request parameters where supported. Hermes automatically handles reasoning content passback by default — no manual configuration needed.

#### 5. Verify Your Setup

```bash
# Check current model and provider
hermes status

# Send a test prompt
hermes run "What DeepSeek model am I using?"
```

Expected output:

```
Model: deepseek-v4-flash (opencode-go)
Provider: opencode-go
```

#### 6. Production Deployment

Hermes with DeepSeek V4 models can run as a 24/7 autonomous agent with:

- **Cron jobs** for scheduled tasks (daily briefings, automated research, portfolio monitoring)
- **Multi-channel gateways** (Telegram, Discord, CLI) running simultaneously
- **Skill auto-learning** — Hermes writes new skills from experience and persists them
- **Cross-session memory** via the built-in Honcho integration

For a real-world reference, [GenTech Labs](https://github.com/ProtoJay4789/genTech-agent-kit) runs Hermes with DeepSeek V4 Flash as its primary production model across 30+ cron jobs, 4 communication channels, and 200+ skills — all on a single VPS instance.

#### 7. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Model not found` error | Ensure model name uses V4 format: `deepseek-v4-pro` or `deepseek-v4-flash` (not deprecated `deepseek-chat`) |
| Context window errors | Use `[1m]` suffix: `deepseek-v4-pro[1m]` |
| Rate limiting | Add a fallback provider in config.yaml to automatically retry on rate limits |
| Reasoning content passback | Update Hermes to latest version — this is handled automatically |

---

#### Resources

- [Hermes Documentation](https://hermes-agent.nousresearch.com/docs)
- [DeepSeek Platform](https://platform.deepseek.com/) — get an API key
- [DeepSeek API Docs](https://api-docs.deepseek.com/) — API reference
- [Hermes GitHub](https://github.com/NousResearch/hermes-agent)
- [OpenCode Go](https://github.com/opencode-ai/opencode) — alternative provider backend
