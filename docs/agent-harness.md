# Integrate with Jig

[English](./awesome-deepseek-agent-guide.md) | [简体中文](./awesome-deepseek-agent-guide.zh-CN.md) · [← Back](../README.md)

Jig is a Python multi-agent orchestration framework with 12 preset roles, 4-layer memory architecture, and a hard-constraint Harness layer. It's optimized for DeepSeek V4's API — cache-first prefix hashing, flash-first cost routing, and automatic tool-call repair.

#### 1. Prerequisites

- Python 3.10+
- A DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys)

#### 2. Installation

```bash
# Clone the repository
git clone https://github.com/luyi14-bits/agent-harness.git
cd agent-harness

# Install dependencies
pip install pydantic>=2.0 pydantic-settings>=2.0 pyyaml>=6.0
```

#### 3. Configuration

Set your API key as an environment variable:

```bash
# Linux / macOS
export DEEPSEEK_API_KEY="sk-your-key-here"

# Windows
set DEEPSEEK_API_KEY=sk-your-key-here
```

Or create a `.env` file in the project root:

```
DEEPSEEK_API_KEY=sk-your-key-here
```

#### 4. First Run

```bash
# Launch interactive group-chat mode
python run.py
```

Type `help` to see available commands, or enter a natural-language request like `"Create a PRD for a login feature"`.

#### 5. Run with custom skills

```bash
python run.py --attach my-custom-skill
```

---

## DeepSeek-Specific Optimizations

Jig is purpose-built for DeepSeek V4's API, with optimizations not found in generic agent frameworks:

### Cache-First Prefix Hashing

Jig uses SHA-256 prefix hashing to maximize DeepSeek's context caching discount (cache hits cost ~2% of full price). The immutable context prefix is frozen per session and only rebuilt when the prefix changes — achieving near-100% cache hit rates on stable system prompts.

```python
from jig.adapters.cache_engine import CacheEngine
from jig.adapters.cache_stats import CacheStats

engine = CacheEngine(max_prefix_size=1024)
stats: CacheStats = engine.stats
print(f"Hit rate: {stats.hit_rate:.0%}, Saved: ${stats.estimated_savings_usd}")
```

### Flash-First Cost Routing

All agents default to `deepseek-v4-flash` for cost efficiency. Short queries (<100 tokens) stay on Flash; complex tasks auto-upgrade to `deepseek-v4-pro`. Token budgets prevent runaway costs.

### Reasoning Effort Control

Configure per-agent reasoning depth:

```python
from jig.adapters.deepseek_adapter import DeepSeekAdapter

adapter = DeepSeekAdapter(reasoning_effort="high")  # low / medium / high
```

### Automatic Tool-Call Repair

DeepSeek V4's function calling responses sometimes contain format errors (trailing commas, unquoted keys, code block wrapping). Jig auto-repairs these with a 4-strategy fallback chain:

1. Direct JSON parse
2. Strip markdown code blocks
3. Remove trailing commas
4. Re-quote unquoted keys

If all strategies fail, it degrades gracefully to plain-text mode.

### 1M Context Window

Jig fully supports DeepSeek V4's 1 million token context window. Configure in settings:

```python
from jig.settings import JigSettings

settings = JigSettings()
settings.pro_model = "deepseek-v4-pro"       # Pro for reasoning
settings.flash_model = "deepseek-v4-flash"   # Flash for coding/testing
```

### Hard-Constraint Harness Layer

Unlike prompt-only frameworks (CrewAI, MetaGPT, AutoGPT), Jig enforces behavior through a 3-layer ToolGuard that intercepts tool calls *before* execution — whitelist, denylist, and PreToolUse hooks. Every pipeline stage passes through 5-stage LOOP SOP gating with automatic degradation.

---

## Architecture Overview

```
You: "Build a login flow"
         │
         ▼
  Dispatcher ──── Routes intent (uses deepseek-v4-flash)
         │
         ▼
  PM Agent ────────→ Trinity Review ──→ Spec Pipeline
         │                                    │
         ▼                                    ▼
  Coding Agent ──→ Code-Review ──→ TDD ──→ Acceptance + Security
         │                                            │
         ▼                                            ▼
  DevOps ─────────────────────────────────────→ Secretary
```

All agents use `deepseek-v4-flash` by default. PM, Trinity, Spec, Code-Review, and Security agents auto-upgrade to `deepseek-v4-pro` for complex reasoning.

---

## Pricing Reference

| Model | Input / M tokens | Output / M tokens | Cache Hit / M tokens |
|-------|-----------------|-------------------|----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |

*Cache hit pricing applies when using Jig's prefix-hashing cache engine with immutable session contexts.*
