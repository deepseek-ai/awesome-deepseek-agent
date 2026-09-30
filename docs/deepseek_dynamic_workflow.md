[English](./deepseek_dynamic_workflow.md) | [简体中文](./deepseek_dynamic_workflow.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Dynamic Workflow

DeepSeek Dynamic Workflow (DDW) is a cache-first dynamic workflow runtime for DeepSeek agents. It is built for multi-agent runs where agents fan out across phases, reuse stable context, write artifacts, and expose prompt-cache hit/miss metrics in a dashboard.

- **GitHub:** <https://github.com/giao-123-sun/DeepSeek-Dynamic-Workflow>
- **Best for:** cache-aware multi-agent research, codebase audits, policy/legal comparison, web evidence extraction, and workflow observability.

#### 1. Install Node.js

- Install [Node.js](https://nodejs.org/en/download/) 22+.
- Windows users should also install [Git for Windows](https://git-scm.com/download/win).

#### 2. Install DDW from source

```sh
git clone https://github.com/giao-123-sun/DeepSeek-Dynamic-Workflow.git
cd DeepSeek-Dynamic-Workflow
npm install
npm run build
npm run check
```

Optional: expose the local CLI commands in your shell:

```sh
npm link
ddw-agent --help
```

The historical `cf-dw-*` command names are also kept as compatibility aliases, but new users should prefer the `ddw-*` commands.

#### 3. Get a DeepSeek API key

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). Create a local `.env` file in the DDW repo:

```text
DEEPSEEK_API_KEY=sk-...
```

Do not commit `.env`. DDW loads it locally and writes run artifacts under `.cf-dw/`.

#### 4. Choose a model

DDW examples use current DeepSeek V4 model names:

| Use case | Model |
|---|---|
| Cost-efficient workflow agents | `deepseek-v4-flash` |
| High-value synthesis or complex agent work | `deepseek-v4-pro` |

DeepSeek V4 supports up to a **1 million token** context window. DDW's cache-first design is meant to keep stable prefixes reusable across many agents, so large shared context can become cheaper on warm runs.

For autonomous harness runs, DDW exposes reasoning effort levels including `max`:

```sh
node dist/reasonix-agent.js \
  --cwd . \
  --prompt "Inspect this repository and summarize DDW's runtime model." \
  --cache-group-id ddw_harness_quickstart_v1 \
  --session-id auto \
  --model deepseek-v4-pro \
  --effort max \
  --budget 0.20 \
  --no-proxy
```

#### 5. First native run

Run a lightweight native DDW agent:

```sh
node dist/index.js \
  --cwd . \
  --prompt "List the top-level files and summarize this project." \
  --cache-group-id ddw_quickstart_v1 \
  --session-id quickstart_native \
  --model deepseek-v4-flash \
  --max-turns 4
```

The run writes observable artifacts under:

```text
.cf-dw/runs/quickstart_native/
  session.json
  usage.jsonl
```

#### 6. Build a stable prefix

Stable prefixes are the core of DDW's prompt-cache strategy:

```sh
node dist/prefix-cli.js \
  --cwd . \
  --output .cf-dw/prefix/cache-prefix.xml \
  --style xml \
  --include "src/**/*.ts,README.md,package.json,odw*.json,examples/**/*.js,examples/**/*.json,examples/**/*.md" \
  --compress
```

Use the prefix in a follow-up run:

```sh
node dist/index.js \
  --cwd . \
  --prompt "Explain the workflow dashboard and cache metrics." \
  --prefix-file ./.cf-dw/prefix/cache-prefix.xml \
  --cache-group-id ddw_quickstart_v1 \
  --session-id quickstart_with_prefix \
  --model deepseek-v4-flash
```

#### 7. Inspect cache metrics and dashboard

Generate a cache report:

```sh
node dist/report.js --runs-root ./.cf-dw/runs
```

Generate a static workflow dashboard:

```sh
node dist/dashboard.js \
  --runs-root ./.cf-dw/runs \
  --latest-per-agent \
  --output ./.cf-dw/reports/ddw-dashboard.html
```

Open `.cf-dw/reports/ddw-dashboard.html` in a browser. The dashboard shows workflow status, phases, agents, tokens, tool calls, runtime, cache hit rate, effective tokens, and artifact previews.

#### 8. Demo suite

DDW ships a practical demo suite:

```sh
npm run demo:dashboards
npm run release:audit
```

The current release audit checks five demos and reports aggregate prompt-cache metrics. At the time this guide was written, the local release audit reported 23 agents and an 88.20% cache hit rate across the demo suite.

#### Notes

- DDW is source-available for non-commercial use. See the project's `LICENSE.md`.
- Live DeepSeek runs require `DEEPSEEK_API_KEY` and may incur API cost.
- The project keeps `.cf-dw/` as the runtime artifact directory for compatibility with existing reports and dashboards.
