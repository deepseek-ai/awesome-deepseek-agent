[English](/deepseek-ai/awesome-deepseek-agent/blob/main/docs/mss-agent.md) | [简体中文](/deepseek-ai/awesome-deepseek-agent/blob/main/docs/mss-agent.zh-CN.md) · [← 返回](/deepseek-ai/awesome-deepseek-agent/blob/main/README.zh-CN.md)

MSS-Agent 是世界上第一个内置"意义场自检"的开源 Agent 框架。与传统盲目执行任务的 Agent 不同，MSS-Agent 在执行前通过三层"热税"（物理、逻辑、意义）评估每个任务。

## 前置条件

- Python 3.10+
- [DeepSeek API Key](https://platform.deepseek.com/api_keys)

## 第一步：安装

```bash
pip install mss-agent openai
```

## 第二步：设置 API Key

```bash
# Linux / Mac
export DEEPSEEK_API_KEY="sk-your-api-key"

# Windows (PowerShell)
$env:DEEPSEEK_API_KEY="sk-your-api-key"
```

或在代码中设置：

```python
import os
os.environ["DEEPSEEK_API_KEY"] = "sk-your-api-key"
```

## 第三步：使用 MSS-Agent

### 基础用法：检查任务是否会被拦截

```python
from mss_agent import MSSAgent
from mss_agent.llm.deepseek import DeepSeekLLM

agent = MSSAgent(
    name="my-agent",
    llm=DeepSeekLLM(model="deepseek-chat"),
)

# 有意义的任务 — 通过
result = agent.run("设计一个带限流的安全REST API")
print(f"通过: {result.output}")

# 废话任务 — 拦截（不消耗 API token）
result = agent.run("改写一下：你好")
print(f"拦截: {result.reason}")
```

### MSS-Agent 会自动拦截以下任务

```python
tasks = [
    "改写一下：你好",           # 废话模式 → 拦截
    "把刚才那句话重写一遍",      # 废话语义 → 拦截
    "Again",                   # 过短 → 拦截
    "设计OAuth2认证流程",       # 有意义 → 通过
]
for t in tasks:
    r = agent.run(t)
    print(f"{t[:20]}: {'拦截' if r.aborted else '通过'}")
```

### 使用 DeepSeek Reasoner (V4-Pro)

```python
from mss_agent.llm.deepseek import DeepSeekReasoner

agent = MSSAgent(
    name="thinker",
    llm=DeepSeekReasoner(model="deepseek-reasoner"),
)
result = agent.run("分析JWT在浏览器存储中的安全隐患")
```

### 查看 Agent 健康状态

```python
print(agent.health_report())
# {
#   "runs": 15, "aborts": 3,
#   "abort_rate": 0.2,
#   "delta_status": "HEALTHY"
# }
```

## CLI 快速开始

```bash
pip install mss-agent

# 检查任务
mss-agent check "改写一下：你好"
# 输出: 🛑 ABORTED: Busywork detected

mss-agent run "解释CAP定理"
```

## 原理

MSS-Agent 在 LLM 调用前执行**三层防御**：

1. **A3 热税** — 对任务打分。废话任务（改写/重翻/缩写）获高热税 → 调用前拦截（节省 API 费用）
2. **A6 Δ 协议** — 追踪 Agent 健康。若 Agent 陷入重复模式 → 触发"蜕壳"（模式重置）
3. **记忆系统** — 记住但也遗忘。闭合模式被逐出以维持多样性

这意味着 DeepSeek API 只会为真正有意义的任务调用 — 节省 token 并确保输出质量。

## 资源

- [MSS-Agent GitHub](https://github.com/mysama1/MSS-AI-Project)
- [MSS-Agent PyPI](https://pypi.org/project/mss-agent/)
- [MSS Wiki](https://mssai.miraheze.org)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
