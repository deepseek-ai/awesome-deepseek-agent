[English](./dsh_session_recall.md) | [简体中文](./dsh_session_recall.zh-CN.md) · [← Back](../README.md)

# Integrate with dsh-session-recall

dsh-session-recall is an open-source plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) — DeepSeek's official agent runtime. It gives the agent a `recall` tool that full-text searches its own past session transcripts: "that bug we fixed last week", "the font we chose for my resume". The official `@deepseek-ai/dsh-session-query` service deliberately ships no model-facing tool and no caller authorization; this plugin fills both gaps through the trusted `ctx.sessionQuery` seam — scoping every call to the calling agent's project directory by default — and turns the harness's opt-in FTS index into a persistent on-disk database.

#### 1. Prerequisite: a DeepSeek Harness installation

This is an out-of-tree DSH plugin, so it rides on an existing [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) setup. No extra API key — it searches sessions through DSH's own query engine and inherits whatever provider your harness already uses.

#### 2. Install the plugin into a profile

```
dsh plugin --profile web add dsh-session-recall
```

The package declares `dsh.bundle`, so it joins the profile's plugin layer stack automatically. Its bundle patch additionally enables the FTS index (`openAt: first-search`) and points it at a persistent database under `<DSH_HOME>/session-recall/`, replacing the shipped in-memory default. Restart the `dsh web` process afterwards so the freshly installed layer is loaded.

#### 3. Ask about the past

Just talk to the agent:

> "What did we do about the resume template font last week?"

The model calls `recall` on its own whenever the user refers to earlier work or when prior context was compacted away. Each hit returns the best-matching event snippet per session — title, date, session id — and renders as a native search card in the Web UI. Variants the model uses as needed:

- `all_projects: true` — search sessions from every project directory, not just the current one
- `session_id` — search the events of one specific session
- `limit` / `cursor` — page through results
