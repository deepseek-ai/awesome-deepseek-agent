# SandBase Harness with DeepSeek

This guide connects DeepSeek Harness to a local SandBase Harness runtime over MCP. SandBase owns durable sessions, tool governance, approvals, credentials, audit, and replay; it is not a hosted model provider. The DeepSeek model remains configured in DeepSeek Harness.

## Prerequisites

- Node.js 22+ and npm 10+
- DeepSeek Harness with stdio MCP support
- A DeepSeek API key or another provider supported by DeepSeek Harness
- Docker when using the published bridge image

Use the current DeepSeek V4 model names `deepseek-v4-pro` or `deepseek-v4-flash`; do not use deprecated V3 model names. DeepSeek V4 supports up to 1 million tokens of context. When DeepSeek Harness exposes these controls, use its documented 1M context setting and maximum thinking/reasoning level. Provider-specific keys belong in DeepSeek Harness configuration and are not invented here.

## 1. Install and start SandBase Harness

```bash
git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness
npm ci
npm run build:runtime
mkdir ../sandbase-workspace && cd ../sandbase-workspace
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
```

The default local provider runs as the OS user. For stronger isolation, configure Docker or Kubernetes using the [deployment guide](https://github.com/sandbaseai/sandbase-harness/blob/main/docs/deployment.md); isolation and resource boundaries depend on the selected backend and deployment.

## 2. Configure MCP and the model

From the sibling workspace, install the source checkout into the DeepSeek Harness Web profile:

```bash
export MANAGED_AGENTS_URL=http://127.0.0.1:3000
# Set MANAGED_AGENTS_API_KEY only when runtime authentication is enabled.
cd ../sandbase-workspace
dsh plugin --profile web add -w ../sandbase-harness
dsh web
```

In DeepSeek Harness' own provider settings, select `deepseek-v4-pro` for maximum reasoning or `deepseek-v4-flash` for lower latency. Follow its current documentation for endpoint, API key, context-window, and thinking controls. SandBase is the MCP/runtime layer and does not replace model configuration.

The bridge connects only to `MANAGED_AGENTS_URL`; keep API keys out of committed files and screenshots. The source-checkout path also avoids confusion with the unrelated unscoped npm package named `managed-agents`.

## 3. First run

Ask the DeepSeek Harness Web session to list agents, create a session, run a short task, inspect the result, and list artifacts. The bridge exposes `list_agents`, `create_session`, `run_session`, `get_session`, `list_artifacts`, and `stop_session`.

Verify the runtime before troubleshooting MCP:

```bash
curl --fail --silent --show-error "$MANAGED_AGENTS_URL/v1/x/health"
curl --fail --silent --show-error "$MANAGED_AGENTS_URL/v1/agents"
```

If the second request requires authentication, repeat it with the runtime's accepted bearer key. A successful health check does not prove MCP data-API access.

## Troubleshooting and scope

- `MCP startup failed`: run `npm run build:runtime` and confirm `dist/mcp/index.js` exists.
- `fetch failed`: start the runtime and check `MANAGED_AGENTS_URL`.
- `401` or `403`: set `MANAGED_AGENTS_API_KEY` only when required.
- No SandBase tools: verify that the Web profile installed the sibling checkout and inspect DSH startup logs.

Session data and artifacts remain in the configured SandBase workspace. Local process, Docker, Kubernetes, and worker backends do not provide identical isolation; evaluate the selected backend and deployment configuration before running untrusted work. This is not a security certification.

## Sources

- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness)
- [v0.3.8 release](https://github.com/sandbaseai/sandbase-harness/releases/tag/v0.3.8)
- [Installation and MCP configuration](https://github.com/sandbaseai/sandbase-harness/blob/main/llms-install.md)
- [DeepSeek Harness integration example](https://github.com/sandbaseai/sandbase-harness/tree/main/examples/deepseek-harness)
- [DeepSeek API documentation](https://api-docs.deepseek.com/)
