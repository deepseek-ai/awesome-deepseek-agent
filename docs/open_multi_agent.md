[English](./open_multi_agent.md) | [简体中文](./open_multi_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with Open Multi-Agent

[Open Multi-Agent](https://github.com/open-multi-agent/open-multi-agent) (OMA) is a TypeScript-native multi-agent orchestration framework. Give it a goal and a coordinator agent decomposes it into a task DAG, parallelizes independents, and synthesizes the result. Three runtime dependencies, drops into any Node.js backend. DeepSeek V4 is a first-class provider, including reasoning-mode tool calls.

#### 1. Installation

Requires Node.js 20+.

```bash
npm install @open-multi-agent/core
```

#### 2. API Key

Get a DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/), then export it:

```bash
export DEEPSEEK_API_KEY="sk-..."
```

#### 3. First Run (single agent)

Create `hello.ts`:

```typescript
import { OpenMultiAgent } from '@open-multi-agent/core'

const oma = new OpenMultiAgent({
  defaultProvider: 'deepseek',
  defaultModel: 'deepseek-v4-pro',
})

const result = await oma.runAgent(
  {
    name: 'assistant',
    systemPrompt: 'You are a helpful assistant. Be concise.',
  },
  'Explain what a B-tree is in 3 sentences.',
)

console.log(result.output)
console.log(`Tokens: ${result.tokenUsage.input_tokens} in / ${result.tokenUsage.output_tokens} out`)
```

Run it:

```bash
npx tsx hello.ts
```

#### 4. Run a Team

The coordinator decomposes the goal into a task DAG; independents run in parallel.

```typescript
import { OpenMultiAgent } from '@open-multi-agent/core'

const oma = new OpenMultiAgent({
  defaultProvider: 'deepseek',
  defaultModel: 'deepseek-v4-flash',
})

const team = oma.createTeam('research-team', {
  name: 'research-team',
  agents: [
    {
      name: 'researcher',
      model: 'deepseek-v4-pro',
      provider: 'deepseek',
      systemPrompt: 'You research a topic and produce structured findings.',
    },
    {
      name: 'writer',
      systemPrompt: 'You turn research notes into a clear short article.',
    },
  ],
  sharedMemory: true,
})

const result = await oma.runTeam(
  team,
  'Write a 200-word intro to vector databases for backend engineers.',
)

for (const [name, agentResult] of result.agentResults) {
  console.log(`\n--- ${name} ---`)
  console.log(agentResult.output)
}
console.log(`\nTotal tokens: ${result.totalTokenUsage.input_tokens} in / ${result.totalTokenUsage.output_tokens} out`)
```

For a fuller end-to-end example (3 agents collaborating to build an Express.js REST API), see [`examples/providers/deepseek.ts`](https://github.com/open-multi-agent/open-multi-agent/blob/main/examples/providers/deepseek.ts).

#### 5. Notes

- **Models**: `deepseek-v4-pro` (flagship, best for coding) and `deepseek-v4-flash` (economical). Both support **1M token context**. OMA does not cap the context window, so the full 1M is available.
- **Reasoning effort**: DeepSeek V4 Pro supports `max` and `high` levels. Because `'max'` is DeepSeek-specific and outside the standard OpenAI SDK type union, pass it via `extraBody` on the agent config:
  ```typescript
  {
    name: 'architect',
    model: 'deepseek-v4-pro',
    provider: 'deepseek',
    extraBody: { reasoning_effort: 'max' },
  }
  ```
  For `'high'`, you can also use the typed form: `thinking: { enabled: true, effort: 'high' }`.
- **Reasoning content on tool calls**: OMA echoes `reasoning_content` on tool-using V4 conversations per the [DeepSeek thinking-mode spec](https://api-docs.deepseek.com/guides/thinking_mode).

#### Resources

- [Open Multi-Agent on GitHub](https://github.com/open-multi-agent/open-multi-agent)
- [npm: @open-multi-agent/core](https://www.npmjs.com/package/@open-multi-agent/core)
- [Provider documentation](https://github.com/open-multi-agent/open-multi-agent/blob/main/docs/providers.md)
