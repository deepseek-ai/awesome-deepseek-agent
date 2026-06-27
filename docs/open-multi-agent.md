[English](./open-multi-agent.md) | [简体中文](./open-multi-agent.zh-CN.md) · [← Back](../README.md)

# Integrate with open-multi-agent

open-multi-agent (OMA) is a TypeScript multi-agent orchestration framework: describe a goal, and a coordinator turns it into a multi-agent DAG with a live dashboard. It ships built-in provider shortcuts including **DeepSeek**, so you only set `provider: 'deepseek'` and `DEEPSEEK_API_KEY`.

- **GitHub:** <https://github.com/open-multi-agent/open-multi-agent>

#### 1. Install

```sh
npm install @open-multi-agent/core
```

For a quick run without a project:

```sh
npx tsx packages/core/examples/basics/team-collaboration.ts
```

#### 2. Get a DeepSeek API Key

Sign up at the [DeepSeek Platform](https://platform.deepseek.com/api_keys), add credit, and copy your API key.

#### 3. Configure the DeepSeek provider

OMA has a bundled `deepseek` shortcut — set the env var and use `provider: 'deepseek'` in your agent definition:

```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```

```typescript
import { createAdapter } from '@open-multi-agent/core'

const adapter = createAdapter('deepseek', 'deepseek-v4-flash')

const agent = {
  name: 'my-agent',
  provider: 'deepseek',
  model: 'deepseek-v4-flash', // or 'deepseek-v4-pro' (flagship for coding); both support 1M context, 384K max output
  systemPrompt: 'You are a helpful assistant.',
}
```

#### 4. First run

Run a coordinated team — the first run shows the coordinator turn one goal into a multi-agent DAG and open a dashboard:

```sh
oma "design a retry decorator with tests"
```

OMA also supports Anthropic/OpenAI/Gemini/Bedrock built-ins, any OpenAI-compatible endpoint (Ollama/vLLM/OpenRouter/Groq/Mistral), MCP, an AI SDK bridge, and a one-click Vercel starter — see the [providers docs](https://github.com/open-multi-agent/open-multi-agent/blob/main/docs/providers.md) for the full list.
