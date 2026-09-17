[English](./open_multi_agent.md) | [简体中文](./open_multi_agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Open Multi-Agent

[Open Multi-Agent](https://github.com/open-multi-agent/open-multi-agent)（简称 OMA）是面向 TypeScript 后端的多智能体编排框架。给定一个目标，coordinator agent 会将其拆解为任务 DAG，并行执行独立任务，合成最终结果。仅 3 个运行时依赖，可直接嵌入任意现有 Node.js 后端。DeepSeek V4 是其原生支持的 provider，包含思考模式下的工具调用。

#### 1. 安装

要求 Node.js 20+。

```bash
npm install @open-multi-agent/core
```

#### 2. 准备 API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/) 申请 API key，然后导出环境变量：

```bash
export DEEPSEEK_API_KEY="sk-..."
```

#### 3. 单 Agent 运行

新建 `hello.ts`：

```typescript
import { OpenMultiAgent } from '@open-multi-agent/core'

const oma = new OpenMultiAgent({
  defaultProvider: 'deepseek',
  defaultModel: 'deepseek-v4-pro',
})

const result = await oma.runAgent(
  {
    name: 'assistant',
    systemPrompt: '你是一个乐于助人的助手，回答简洁。',
  },
  '用 3 句话解释什么是 B 树。',
)

console.log(result.output)
console.log(`Token 用量：输入 ${result.tokenUsage.input_tokens}，输出 ${result.tokenUsage.output_tokens}`)
```

运行：

```bash
npx tsx hello.ts
```

#### 4. 运行一个团队

Coordinator 把目标拆解为任务 DAG，独立任务并行执行。

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
      systemPrompt: '你负责调研一个主题，产出结构化的发现。',
    },
    {
      name: 'writer',
      systemPrompt: '你把调研笔记整理成一篇清晰的短文。',
    },
  ],
  sharedMemory: true,
})

const result = await oma.runTeam(
  team,
  '面向后端工程师，写一段 200 字的向量数据库入门介绍。',
)

for (const [name, agentResult] of result.agentResults) {
  console.log(`\n--- ${name} ---`)
  console.log(agentResult.output)
}
console.log(`\n总 Token：输入 ${result.totalTokenUsage.input_tokens}，输出 ${result.totalTokenUsage.output_tokens}`)
```

更完整的端到端示例（3 个 agent 协作构建一个 Express.js REST API）见 [`examples/providers/deepseek.ts`](https://github.com/open-multi-agent/open-multi-agent/blob/main/examples/providers/deepseek.ts)。

#### 5. 说明

- **模型**：`deepseek-v4-pro`（旗舰，最适合编码）和 `deepseek-v4-flash`（经济款），两者都支持 **1M token 上下文**。OMA 不对 context window 设上限，可使用完整 1M 容量。
- **Reasoning effort**：DeepSeek V4 Pro 支持 `max` 与 `high` 两档。由于 `'max'` 是 DeepSeek 特有取值（不在标准 OpenAI SDK 的类型联合中），需通过 agent config 的 `extraBody` 传入：
  ```typescript
  {
    name: 'architect',
    model: 'deepseek-v4-pro',
    provider: 'deepseek',
    extraBody: { reasoning_effort: 'max' },
  }
  ```
  `'high'` 也可用标准形式：`thinking: { enabled: true, effort: 'high' }`。
- **工具调用中的 reasoning content**：OMA 在 V4 工具调用对话中回传 `reasoning_content`，符合 [DeepSeek 思考模式规范](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。

#### 资源

- [Open Multi-Agent GitHub 仓库](https://github.com/open-multi-agent/open-multi-agent)
- [npm: @open-multi-agent/core](https://www.npmjs.com/package/@open-multi-agent/core)
- [Provider 文档](https://github.com/open-multi-agent/open-multi-agent/blob/main/docs/providers.md)
