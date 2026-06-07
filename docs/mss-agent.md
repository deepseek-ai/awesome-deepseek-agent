[English](/deepseek-ai/awesome-deepseek-agent/blob/main/docs/mss-agent.md) | [简体中文](/deepseek-ai/awesome-deepseek-agent/blob/main/docs/mss-agent.zh-CN.md) · [← Back](/deepseek-ai/awesome-deepseek-agent/blob/main/README.md)

MSS-Agent is the first open-source Agent framework with built-in "meaning-field self-audit." Unlike traditional agents that blindly execute tasks, MSS-Agent evaluates every task through three layers of "heat tax" — physical, logical, and meaning — before deciding whether to proceed.

## Prerequisites

- Python 3.10+
- A [DeepSeek API Key](https://platform.deepseek.com/api_keys)

## Step 1: Install

```bash
pip install mss-agent openai
```

## Step 2: Set API Key

```bash
# Linux / Mac
export DEEPSEEK_API_KEY="sk-your-api-key"

# Windows (PowerShell)
$env:DEEPSEEK_API_KEY="sk-your-api-key"
```

Or set it in code:

```python
import os
os.environ["DEEPSEEK_API_KEY"] = "sk-your-api-key"
```

## Step 3: Use MSS-Agent with DeepSeek

### Basic: Check if a task is meaningful

```python
from mss_agent import MSSAgent
from mss_agent.llm.deepseek import DeepSeekLLM

agent = MSSAgent(
    name="my-agent",
    llm=DeepSeekLLM(model="deepseek-chat"),
)

# Meaningful task — passes, LLM is called
result = agent.run("Design a secure REST API with rate limiting")
print(f"Passed: {result.output}")

# Busywork — rejected BEFORE any API call (saves tokens)
result = agent.run("改写一下：你好")
print(f"Rejected: {result.reason}")
```

### MSS-Agent auto-rejects these tasks

```python
tasks = [
    "改写一下：你好",           # Busywork pattern → ABORT
    "把刚才那句话重写一遍",      # Waste signal → ABORT
    "Again",                   # Too short → ABORT
    "Design OAuth2 auth flow",  # Meaningful → PASS
]
for t in tasks:
    r = agent.run(t)
    print(f"{t[:30]}: {'ABORT' if r.aborted else 'PASS'}")
```

### With DeepSeek Reasoner (V4-Pro)

```python
from mss_agent.llm.deepseek import DeepSeekReasoner

agent = MSSAgent(
    name="thinker",
    llm=DeepSeekReasoner(model="deepseek-reasoner"),
)
result = agent.run("Analyze the security implications of JWT in browser storage")
```

### Check agent health

```python
print(agent.health_report())
# {
#   "runs": 15, "aborts": 3,
#   "abort_rate": 0.2,
#   "delta_status": "HEALTHY"
# }
```

## CLI Quick Start

```bash
pip install mss-agent

# Check a task
mss-agent check "改写一下：你好"
# Output: 🛑 ABORTED: Busywork detected

# Run through DeepSeek
export DEEPSEEK_API_KEY="sk-..."
```

## How It Works

MSS-Agent applies a **3-layer defense** before any LLM call:

1. **A3 Heat Tax** — Scores task meaningfulness. Busywork (rewrite/retranslate/shorten) gets high tax → rejected before LLM invocation (saves API cost)
2. **A6 Delta Protocol** — Tracks agent health. If stuck repeating similar tasks, triggers "molting" (pattern reset)
3. **Memory System** — Remembers but also forgets. Closed patterns evicted to maintain diversity

DeepSeek API is only called for tasks that actually matter — saving tokens and ensuring output quality.

## Resources

- [MSS-Agent GitHub](https://github.com/mysama1/MSS-AI-Project)
- [MSS-Agent PyPI](https://pypi.org/project/mss-agent/)
- [MSS Wiki](https://mssai.miraheze.org) — full documentation
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
