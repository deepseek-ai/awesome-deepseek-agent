[English](./zenmind.md) | [简体中文](./zenmind.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 ZenMind

ZenMind 是一个开源 AI Agent 平台，提供桌面端与移动端客户端。它通过 AGWUI 协议进行智能体交互与视口渲染，可接入 DeepSeek V4 等国产模型生态，并支持流式输出、HITL 审批、用量统计、沙箱会话与子 Agent 调用能力。

- **GitHub：** <https://github.com/linlay/zenmind>
- **官网：** <https://www.zenmind.cc>

#### 1. 安装 ZenMind

从 [ZenMind 官网](https://www.zenmind.cc) 下载 ZenMind Desktop 安装包，然后安装并启动。

你也可以从源码构建：

```shell
git clone https://github.com/linlay/zenmind.git
cd zenmind
```

请根据仓库 README 中最新的 Desktop 打包与服务启动说明操作。推荐优先使用 ZenMind Desktop，因为它会准备本地配置、初始化所需服务，并按正确顺序启动运行时。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)，创建一个 API Key，并在后续 ZenMind 模型服务配置中使用。

#### 3. 配置 DeepSeek V4 模型

打开 ZenMind Desktop，进入模型或 Provider 设置，添加 DeepSeek Provider。ZenMind 运行时 registry 会将 Provider 与模型分开保存，一个 DeepSeek Provider 条目如下：

```yaml
key: deepseek
baseUrl: https://api.deepseek.com
apiKey: sk-your-deepseek-api-key
defaultModel: deepseek-v4-pro
protocols:
  OPENAI:
    endpointPath: /chat/completions
    compat:
      messages:
        preserveReasoningContent: true
      response:
        usage:
          promptTokensDetails:
            cacheHitTokens:
              path: prompt_cache_hit_tokens
            cacheMissTokens:
              path: prompt_cache_miss_tokens
          completionTokensDetails:
            reasoningTokens:
              path: completion_tokens_details.reasoning_tokens
```

然后确认 DeepSeek V4 模型条目可用：

```yaml
key: deepseek-v4-pro
name: DS V4 Pro
provider: deepseek
protocol: OPENAI
modelId: deepseek-v4-pro
isVision: false
isReasoner: true
isFunction: true
maxTokens: 1000000
maxInputTokens: 1000000
maxOutputTokens: 384000
```

```yaml
key: deepseek-v4-flash
name: DS V4 Flash
provider: deepseek
protocol: OPENAI
modelId: deepseek-v4-flash
isVision: false
isReasoner: true
isFunction: true
maxTokens: 1000000
maxInputTokens: 1000000
maxOutputTokens: 384000
```

建议将 **`deepseek-v4-pro`** 设为编码 Agent 与长任务会话的默认模型；如果任务较轻、希望获得更低延迟，可以选择 **`deepseek-v4-flash`**。

DeepSeek V4 支持最高 **100 万 token** 上下文。按 OpenAI-compatible 配置口径，上述条目对应 `context_window: 1000000` 与 `max_tokens: 384000`。

#### 4. 启动 ZenMind 服务

在 ZenMind Desktop 的控制中心启动本地运行时。Desktop 会协调以下核心服务：

- `zenmind-app-server`：认证、管理后台与应用访问 token。
- `agent-platform`：模型路由、工具、记忆、HITL、用量统计与子 Agent 编排。
- `agent-webclient`：对话、时间线回放、模型切换、视口渲染与用量展示。
- `agent-container-hub`：本地沙箱会话与工具运行环境。

等待服务状态显示为运行中，再打开 Agent UI。

#### 5. 首次运行

打开 ZenMind Agent UI，创建或选择一个编码 Agent，并将模型切换为 **`deepseek-v4-pro`**。如果通过 Agent 文件配置模型，可开启 reasoning：

```yaml
modelConfig:
  modelKey: deepseek-v4-pro
  reasoning:
    enabled: true
    effort: HIGH
```

然后可以发送如下第一条消息：

```text
Inspect this repository and summarize the main modules before making changes.
```

为了获得更好的编码体验，请保持 reasoning 开启，并在 UI 或模型设置中选择 **HIGH** 或当前构建提供的最高档位。ZenMind 会展示 token、cache、reasoning token、工具调用与预估成本等 usage 快照，你可以据此确认当前会话正在使用 DeepSeek V4。

#### 常见问题

- 出现 `401` 或鉴权错误：检查 DeepSeek API Key 是否有效，并确认已经保存到 ZenMind Provider 设置中。
- 模型选择器中看不到模型：编辑 Provider 或模型配置后，刷新或重启 ZenMind 服务。
- 上下文长度异常偏短：确认模型条目包含 `maxTokens: 1000000`、`maxInputTokens: 1000000` 与 `maxOutputTokens: 384000`。
- 看不到 reasoning 内容：确认当前模型为 `deepseek-v4-pro`，并将 reasoning effort 设置为 `HIGH` 或可选的最高档位。

#### 相关资源

- [ZenMind](https://github.com/linlay/zenmind)
- [ZenMind 官网](https://www.zenmind.cc)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
