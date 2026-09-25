[English](./open-multi-agent.md) | [简体中文](./open-multi-agent.zh-CN.md) · [← Back](../README.md)

# 接入 open-multi-agent

open-multi-agent（OMA）是一个 TypeScript 多智能体编排框架：描述一个目标，协调器会将其拆解为多智能体 DAG 并带实时看板。内置 **DeepSeek** 等 provider 快捷方式，只需设置 `provider: 'deepseek'` 和 `DEEPSEEK_API_KEY`。

- **GitHub:** <https://github.com/open-multi-agent/open-multi-agent>

#### 1. 安装

```sh
npm install @open-multi-agent/core
```

无项目快速体验：

```sh
npx tsx packages/core/examples/basics/team-collaboration.ts
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 注册、充值，复制你的 API Key。

#### 3. 配置 DeepSeek provider

OMA 内置 `deepseek` 快捷方式——设置环境变量并在 agent 定义中使用 `provider: 'deepseek'`：

```bash
export DEEPSEEK_API_KEY="sk-your-key-here"
```

```typescript
import { createAdapter } from '@open-multi-agent/core'

const adapter = createAdapter('deepseek', 'deepseek-v4-flash')

const agent = {
  name: 'my-agent',
  provider: 'deepseek',
  model: 'deepseek-v4-flash', // 或 'deepseek-v4-pro'（编程旗舰款）；均支持 1M 上下文、384K 最大输出
  systemPrompt: 'You are a helpful assistant.',
}
```

#### 4. 首次运行

运行一个协作团队——首次运行会展示协调器把一个目标拆解为多智能体 DAG 并打开看板：

```sh
oma "设计一个带测试的重试装饰器"
```

OMA 还支持 Anthropic/OpenAI/Gemini/Bedrock 内置、任意 OpenAI 兼容端点（Ollama/vLLM/OpenRouter/Groq/Mistral）、MCP、AI SDK 桥接，以及一键 Vercel 启动模板——完整列表见 [providers 文档](https://github.com/open-multi-agent/open-multi-agent/blob/main/docs/providers.md)。
