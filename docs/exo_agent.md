[English](./exo_agent.md) | [简体中文](./exo_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with Exo-agent

Exo-agent is a browser-based autonomous agent in a **single HTML file** — no backend, fully local. It ships MCTS deep planning, a DAG pipeline engine, flow mode, a world validator, self-evolution and 45+ built-in tools.

- **GitHub:** <https://github.com/Xiyinnnnnn/Exo-agent>

#### 1. Open the agent

Download `index.html` from the repository and open it in any modern browser. Nothing to install — no server, no build step.

#### 2. Configure DeepSeek in the settings panel

Open the settings panel and set:

| Setting | Value |
|---------|-------|
| Base URL | `https://api.deepseek.com` |
| Model | `deepseek-v4-flash` (or `deepseek-v4-pro`) |
| API Key | your DeepSeek API key |

The defaults already point to `api.deepseek.com` with `deepseek-v4-flash`. A context budget of ~1M tokens (`_model_ctx` = 1048565) is built in, matching DeepSeek V4's **1M-token context window**, with a compression-aggressiveness slider that controls how early history is compacted.

#### 3. Enable max thinking

In the settings, set the reasoning effort to `max` (or keep `high`). Exo-agent sends `thinking: {type: "enabled"}` together with the selected `reasoning_effort`, so DeepSeek-V4-Pro's full reasoning is available for planning-heavy workflows.

#### Highlights

- **MCTS deep planner** — up to 600 simulations with UCB1 + pheromone and convergence detection.
- **Pipeline engine V6** — DAG orchestration of multiple sub-agents, 10 node types, conditional routing, error-degradation edges.
- **Flow mode** — root agent → supervisor → worker triangle with review-fix loops.
- **World validator** — multi-entity discrete-event simulation with nested substates and guard conditions.
- **45+ built-in tools** — search, filesystem, code execution, charts, SQLite, OCR, PDF, email, voice, calendar...
- **Fully local** — zero backend, data stays in your browser.
