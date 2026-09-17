[English](./sandbase_harness.md) | [简体中文](./sandbase_harness.zh-CN.md) · [← Back](../README.md)

# Integrate SandBase Harness with DeepSeek V4

SandBase Harness is a local-first runtime for persistent and auditable AI agent sessions. It supports DeepSeek V4 through DeepSeek's OpenAI-compatible API and can expose the runtime to DeepSeek Harness through a stdio MCP bridge.

- **GitHub:** <https://github.com/sandbaseai/sandbase-harness>
- **Runtime documentation:** <https://github.com/sandbaseai/sandbase-harness/blob/main/docs/deepseek-v4.md>

#### 1. Install SandBase Harness

Use the tagged source release so the runtime and its MCP integration are reproducible:

```sh
git clone --branch v0.3.8 --depth 1 https://github.com/sandbaseai/sandbase-harness.git
cd sandbase-harness
npm ci
npm run build:runtime
mkdir ../my-agents
cd ../my-agents
node ../sandbase-harness/dist/index.js init
node ../sandbase-harness/dist/index.js start
```

SandBase Harness requires Node.js 22 or newer. The runtime serves its local API on `http://127.0.0.1:3000` by default.

#### 2. Configure DeepSeek V4

Create an API key at the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then export it for the runtime process:

```sh
export DEEPSEEK_API_KEY="<your DeepSeek API key>"
```

Open `http://127.0.0.1:3000/dashboard`, go to **Settings > Models**, switch to JSON, and save:

```json
{
  "vendor": "openai_compatible",
  "base_url": "https://api.deepseek.com/v1",
  "api_key": "${DEEPSEEK_API_KEY}",
  "options": {
    "reasoning_effort": "max"
  }
}
```

Create an agent with model `deepseek-v4-pro` for the strongest coding and agent performance, or `deepseek-v4-flash` for lower latency. DeepSeek V4 supports up to 1 million tokens of context; SandBase Harness compacts long sessions automatically.

#### 3. Run the first session

In the Console, select the agent and start a session with a small verification task, such as:

```text
Inspect this project, summarize its test command, and do not modify any files.
```

The runtime keeps the session, tool activity, artifacts, and terminal metadata available for inspection and replay. Do not commit API keys to the workspace.

#### Optional: connect DeepSeek Harness through MCP

Build the runtime as above, then from a DeepSeek Harness workspace run:

```sh
export MANAGED_AGENTS_URL=http://127.0.0.1:3000
curl --fail --silent --show-error "$MANAGED_AGENTS_URL/v1/x/health"
dsh plugin --profile web add -w ../sandbase-harness
dsh web
```

The installed bundle exposes managed agents, persistent sessions, streamed turns, artifacts, and cancellation through the `mcp__sandbase__*` namespace. If runtime authentication is enabled, also set `MANAGED_AGENTS_API_KEY` before starting DeepSeek Harness.

