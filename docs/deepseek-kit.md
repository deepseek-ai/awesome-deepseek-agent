[English](./deepseek-kit.md) | [简体中文](./deepseek-kit.zh-CN.md) · [← Back](../README.md)

# Integrate with deepseek-kit

**deepseek-kit** is a lightweight Agent framework with native-level DeepSeek adaptation — precise tool calling in thinking mode, reliable structured output, and maximum cache hit rate.

Unlike general-purpose frameworks (LangChain.js, AI SDK), deepseek-kit is built from the ground up to handle DeepSeek's unique API mechanisms: automatic `reasoning_content` management for multi-turn tool calling, zero-redundancy request bodies for optimal cache performance, and Zod Schema-driven structured output fully compatible with thinking mode.

#### 1. Install deepseek-kit

- Install [Node.js](https://nodejs.org/en/download/) (>= 18.0.0).
- Run the following command in your project directory:

```bash
npm install deepseek-kit
```

> **Note:** You can also use `pnpm add deepseek-kit` or `yarn add deepseek-kit`.

#### 2. Configure DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Set the environment variable:

Linux / macOS:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Windows:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Or use a `.env` file in your project root:

```
DEEPSEEK_API_KEY=<your DeepSeek API Key>
```

#### 3. Create an Agent and Run

Create a file (e.g., `index.ts`) and write the following:

```ts
import { createAgent, createModel, tool } from 'deepseek-kit'
import { z } from 'zod'

const model = createModel({ model: 'deepseek-v4-flash' })

const weatherTool = tool({
  name: 'get_weather',
  description: 'Get weather information for a city',
  parameters: z.object({
    city: z.string().describe('City name'),
  }),
  execute: async ({ city }) => `${city}: Sunny, 25°C`,
})

const agent = createAgent({ model, tools: [weatherTool] })

const result = await agent.generate({
  prompt: "How's the weather in Chongqing today?",
})

console.log(result.text)
```

Run it:

```bash
npx tsx index.ts
```

#### Key Features

- **Thinking Mode Adaptation** — Automatically tracks and re-sends `reasoning_content` in the agent loop. Zero-config tool calling chains with DeepSeek's thinking mode enabled by default.
- **Maximum Cache Hit Rate** — Zero-redundancy request body with deterministic message construction ensures the same input always produces the same request prefix. Cache efficiency is observable via `prompt_cache_hit_tokens` and `prompt_cache_miss_tokens`.
- **Reliable Structured Output** — Zod Schema-driven structured output with smart retry and formatted error feedback, fully compatible with thinking mode.
- **Subagents** — Encapsulate agents as tools for delegation, with isolated context and parallel execution.
- **Streaming** — Streaming events for text, chain-of-thought, and tool calls.
- **FIM Completion** — Fill-in-the-Middle code completion support.
- **Hook System** — Insert custom logic before and after generation steps.

#### Model Configuration

deepseek-kit supports both DeepSeek V4 models with the full 1M context window:

```ts
import { createModel } from 'deepseek-kit'

const model = createModel({
  model: 'deepseek-v4-pro',
  maxTokens: 384000,
})
```

- **deepseek-v4-pro** — Supports reasoning effort levels (`max` and `high`). Thinking mode is enabled by default for the best coding experience.
- **deepseek-v4-flash** — Fast and cost-effective, also supports thinking mode.

#### Resources

- [npm Package](https://www.npmjs.com/package/deepseek-kit)
- [Documentation](https://deepseek-kit.netlify.app)
- [GitHub Repository](https://github.com/flippedround/deepseek-kit)
