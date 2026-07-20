[English](./oh-my-pi.md) | [简体中文](./oh-my-pi.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 Oh My Pi 中使用 DeepSeek

[Oh My Pi](https://github.com/can1357/oh-my-pi) 是终端 AI 编程 Agent。自 v17.0.5 起，`deepseek` provider 已内置完整 compat 支持——标准官方 API 配置不再需要自定义 `models.yml`。

> **兼容性快照（2026-07-21）：** 本指南已基于 Oh My Pi v17.0.5 验证。该版本内置的 `deepseek` provider 已支持 API Key 认证、`DEEPSEEK_API_KEY` 环境变量、DeepSeek 官方接口、thinking mode 以及 tool call 兼容处理。旧版本的行为可能不同；在采用历史 workaround 前，请优先升级。

## 前置条件

安装 Oh My Pi：<https://github.com/can1357/oh-my-pi#installation>

验证安装：

```sh
omp --version
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

## 认证

支持两种方式。

### 推荐：OMP 凭据流程

启动 OMP，在会话内执行登录命令：

```text
omp
/login deepseek
```

尽管命令名是 `/login`，这里执行的是 API Key 凭据录入流程，并不是 DeepSeek OAuth 授权。OMP 通过 provider 级别的登录界面安全存储凭据。

### 备选：环境变量

```sh
export DEEPSEEK_API_KEY="<你的 API Key>"
```

PowerShell：

```powershell
$env:DEEPSEEK_API_KEY = "<你的 API Key>"
```

## 配置（参考）

OMP v17.0.5 内置的 `deepseek` provider 已自动处理下述所有 compat 字段。以下 `~/.omp/agent/models.yml` 仅作为高级自定义场景的参考——自定义网关、私有别名、provider 覆盖或实验性第三方 provider。标准配置无需此文件。

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
| `authHeader: true` | 发送 `Authorization: Bearer $DEEPSEEK_API_KEY`。 |
| `supportsDeveloperRole: false` | 以 `system` 角色发送系统提示词。DeepSeek API 不接受 `developer` 角色。 |
| `maxTokensField: max_tokens` | DeepSeek 的输出限制字段是 `max_tokens`，不是 OpenAI 的 `max_completion_tokens`。 |

### Thinking（思考模式）

| 字段 | 说明 |
| ---- | ---- |
| `thinking.mode: effort` | 使用 effort-based thinking，OMP 会发送 `reasoning_effort` 参数。 |
| `thinking.minLevel: high` / `maxLevel: xhigh` | 限制为 DeepSeek 支持的两档。 |
| `reasoningEffortMap: { high: high, xhigh: max }` | OMP 的 `xhigh` 映射为 DeepSeek 的 `max`。不配这个会导致 `xhigh` 不被识别。 |
| `extraBody.thinking.type: enabled` | 显式启用 DeepSeek V4 思考模式。 |
| `supportsReasoningEffort: true` | 允许 OMP 发送 `reasoning_effort`。 |

### Tool Call 兼容

| 字段 | 说明 |
| ---- | ---- |
| `supportsToolChoice: false` | DeepSeek V4 thinking mode 不接受 `tool_choice` 参数。 |
| `requiresReasoningContentForToolCalls: true` | DeepSeek 要求 tool call 对话的历史消息中必须保留 `reasoning_content`。不配会导致 400。 |
| `requiresAssistantContentForToolCalls: true` | 确保 tool call 消息的 `content` 字段不为空。配合上一个字段使用。 |

以上三项在 v17.0.5 内置 provider 中已自动处理。

## 使用

```sh
cd /path/to/your-project
omp --model deepseek/deepseek-v4-pro
```

需要更快响应时：

```sh
omp --model deepseek/deepseek-v4-flash
```

在 OMP 内输入 `/model` 或按 `Ctrl+L` 切换模型。

## 常见问题

检查版本和可用模型：

```sh
omp --version
omp --list-models deepseek
```

然后按以下顺序排查：

1. **优先升级。** 如果 `omp --version` 显示的版本低于 v17.0.5，先升级再尝试旧版 workaround。
2. **检查残留覆盖。** 旧版 `~/.omp/agent/models.yml` 可能覆盖内置 provider。如果依赖内置配置，请移除或重命名该文件。
3. **重新认证。** 再次执行 `/login deepseek`，或确认 `DEEPSEEK_API_KEY` 已正确设置。
4. **优先使用官方接口。** 排查兼容性问题时，请使用官方 `api.deepseek.com` 接口。第三方 OpenAI 兼容网关对 `reasoning_content` 的回传实现可能不同。
5. **第三方 provider 单独对待。** 本指南的兼容性声明仅适用于 DeepSeek 官方 API。
