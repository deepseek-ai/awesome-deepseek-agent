[English](./deepseek-kit.md) | [简体中文](./deepseek-kit.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 deepseek-kit

**deepseek-kit** 是一个 DeepSeek 原生级适配的轻量 Agent 框架——思考模式精准工具调用、可靠结构化输出、极致缓存命中。

与通用框架（LangChain.js、AI SDK）不同，deepseek-kit 从底层开始解决 DeepSeek API 的独特机制：自动管理 `reasoning_content` 实现多轮工具调用、零冗余请求体实现最优缓存性能、基于 Zod Schema 的结构化输出完全兼容思考模式。

#### 1. 安装 deepseek-kit

- 安装 [Node.js](https://nodejs.org/zh-cn/download/)（>= 18.0.0）。
- 在项目目录下执行以下命令：

```bash
npm install deepseek-kit
```

> **注意：** 也可以使用 `pnpm add deepseek-kit` 或 `yarn add deepseek-kit`。

#### 2. 配置 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

设置环境变量：

Linux / macOS：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

或在项目根目录创建 `.env` 文件：

```
DEEPSEEK_API_KEY=<你的 DeepSeek API Key>
```

#### 3. 创建 Agent 并运行

创建文件（如 `index.ts`），写入以下代码：

```ts
import { createAgent, createModel, tool } from 'deepseek-kit'
import { z } from 'zod'

const model = createModel({ model: 'deepseek-v4-flash' })

const weatherTool = tool({
  name: 'get_weather',
  description: '获取指定城市的天气信息',
  parameters: z.object({
    city: z.string().describe('城市名称'),
  }),
  execute: async ({ city }) => `${city}：晴，25°C`,
})

const agent = createAgent({ model, tools: [weatherTool] })

const result = await agent.generate({
  prompt: '杭州今天天气怎么样？',
})

console.log(result.text)
```

运行：

```bash
npx tsx index.ts
```

#### 核心特性

- **思考模式适配** — 在 Agent 循环中自动追踪并回传 `reasoning_content`，根据是否发生工具调用采用差异化策略，默认启用思考模式——零配置即可正常工作。
- **极致缓存命中率** — 零冗余请求体 + 确定性消息构建，确保相同输入始终产生相同的请求前缀。通过 `prompt_cache_hit_tokens` 和 `prompt_cache_miss_tokens` 可实时观测缓存效率。
- **可靠的结构化输出** — 基于 Zod Schema 的结构化输出，支持智能重试和格式化错误反馈，完全兼容思考模式——格式化步骤中思维链上下文不会丢失。
- **子智能体** — 将智能体封装为工具进行委派，支持上下文隔离与并行执行。
- **流式输出** — 支持文本、思维链、工具调用的流式事件。
- **FIM 补全** — 支持 Fill-in-the-Middle 代码补全。
- **Hook 机制** — 在生成步骤前后插入自定义逻辑。

#### 模型配置

deepseek-kit 支持两款 DeepSeek V4 模型，均支持完整的 1M 上下文窗口：

```ts
import { createModel } from 'deepseek-kit'

const model = createModel({
  model: 'deepseek-v4-pro',
  maxTokens: 384000,
})
```

- **deepseek-v4-pro** — 支持多级推理强度（`max` 和 `high`），默认启用思考模式以获得最佳编程体验。
- **deepseek-v4-flash** — 快速且经济，同样支持思考模式。

#### 相关资源

- [npm 包](https://www.npmjs.com/package/deepseek-kit)
- [文档](https://deepseek-kit.netlify.app/zh)
- [GitHub 仓库](https://github.com/flippedround/deepseek-kit)
