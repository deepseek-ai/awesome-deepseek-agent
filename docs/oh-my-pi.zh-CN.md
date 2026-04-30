[English](./oh-my-pi.md) | [简体中文](./oh-my-pi.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 Oh My Pi 中使用 DeepSeek

[Oh My Pi](https://github.com/can1357/oh-my-pi) 是终端 AI 编程 Agent。自 v14.5 起内置了 DeepSeek V4 模型条目，但内置条目缺少关键配置，直接使用可能报错，仍需自定义 `models.yml`。

## 前置条件

安装 Oh My Pi：<https://github.com/can1357/oh-my-pi#installation>

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key：

```sh
export DEEPSEEK_API_KEY=<你的 API Key>
```

## 配置

创建 `~/.omp/agent/models.yml`：

```yaml
providers:
  deepseek:
    baseUrl: https://api.deepseek.com
    api: openai-completions
    apiKey: DEEPSEEK_API_KEY
    authHeader: true
    models:
      - id: deepseek-v4-pro
        name: DeepSeek V4 Pro
        reasoning: true
        thinking:
          minLevel: high
          maxLevel: xhigh
          mode: effort
        input: [text]
        contextWindow: 1000000
        maxTokens: 384000
        compat:
          supportsDeveloperRole: false
          supportsReasoningEffort: true
          maxTokensField: max_tokens
          reasoningEffortMap:
            high: high
            xhigh: max
          supportsToolChoice: false
          requiresReasoningContentForToolCalls: true
          requiresAssistantContentForToolCalls: true
          extraBody:
            thinking:
              type: enabled
      - id: deepseek-v4-flash
        name: DeepSeek V4 Flash
        reasoning: true
        thinking:
          minLevel: high
          maxLevel: xhigh
          mode: effort
        input: [text]
        contextWindow: 1000000
        maxTokens: 384000
        compat:
          supportsDeveloperRole: false
          supportsReasoningEffort: true
          maxTokensField: max_tokens
          reasoningEffortMap:
            high: high
            xhigh: max
          supportsToolChoice: false
          requiresReasoningContentForToolCalls: true
          requiresAssistantContentForToolCalls: true
          extraBody:
            thinking:
              type: enabled
```

## 配置要点

### 基础

| 字段 | 说明 |
| ---- | ---- |
| `baseUrl: https://api.deepseek.com` | DeepSeek OpenAI 兼容接口。不要加 `/v1`。 |
| `authHeader: true` | 发送 `Authorization: Bearer $DEEPSEEK_API_KEY`。不经过 OAuth `/login`。 |
| `supportsDeveloperRole: false` | 以 `system` 角色发系统提示词。DeepSeek API 不接受 `developer` 角色。 |
| `maxTokensField: max_tokens` | DeepSeek 的输出限制字段是 `max_tokens`，不是 OpenAI 的 `max_completion_tokens`。 |

### Thinking（思考模式）

| 字段 | 说明 |
| ---- | ---- |
| `thinking.mode: effort` | 使用 effort-based thinking，OMP 会发 `reasoning_effort` 参数。 |
| `thinking.minLevel: high` / `maxLevel: xhigh` | 限制为 DeepSeek 支持的两档。 |
| `reasoningEffortMap: { high: high, xhigh: max }` | OMP 的 `xhigh` 映射为 DeepSeek 的 `max`。不配这个会导致 `xhigh` 不被识别。 |
| `extraBody.thinking.type: enabled` | 显式启用 DeepSeek V4 思考模式。 |
| `supportsReasoningEffort: true` | 允许 OMP 发送 `reasoning_effort`。 |

### 三项关键 compat（必配）

这三个字段是避免报错的关键。不配会导致 DeepSeek V4 在 thinking mode 下带 tool call 时返回 400。

| 字段 | 说明 |
| ---- | ---- |
| `supportsToolChoice: false` | DeepSeek V4 thinking mode 不接受 `tool_choice` 参数。 |
| `requiresReasoningContentForToolCalls: true` | DeepSeek 要求 tool call 对话的历史消息中必须保留 `reasoning_content`。不配会导致 400。 |
| `requiresAssistantContentForToolCalls: true` | 确保 tool call 消息的 `content` 字段不为空。配合上一个字段使用。 |

## 使用

```sh
cd /path/to/your-project
omp --model deepseek/deepseek-v4-pro
```

需要更快响应时：

```sh
omp --model deepseek/deepseek-v4-flash
```

在 Oh My Pi 内输入 `/model` 或按 `Ctrl+L` 切换模型。

## 已知问题

**不推荐依赖内置模型条目。** 较新版本 `omp --list-models deepseek` 能列出 `deepseek-v4-pro` 和 `deepseek-v4-flash`，但内置条目缺少上述三项关键 compat。直接用内置条目在 thinking mode 下带 tool call 的长对话大概率 400。始终使用上方的 `models.yml` 配置。

Oh My Pi 目前没有 DeepSeek 的 OAuth `/login` 入口。只能通过 `DEEPSEEK_API_KEY` 环境变量或 `models.yml` 中的 `apiKey` 字段配置 API Key。

DeepSeek V4 在非官方 provider（DeepInfra、KiloCode、NVIDIA NIM、Zenmux 等）上通过 OpenAI-compatible 接口使用时，reasoning_content 回传规则可能不同，兼容性未收敛。建议优先用官方 `api.deepseek.com`。

`models.yml` 的 `compat` 是整块替换，不跟内置条目合并。所以 compat 必须写全，不能只补缺的字段。
