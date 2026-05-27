# 在 Factory AI Droid 中配置 DeepSeek

本指南介绍如何将 DeepSeek 模型添加到 Factory AI Droid 的 `settings.json` 中。

## 可用模型


| 模型                         | 提供商       | Base URL                             |
| -------------------------- | --------- | ------------------------------------ |
| DeepSeek V4 Pro            | Anthropic | `https://api.deepseek.com/anthropic` |
| DeepSeek V4 Flash          | Anthropic | `https://api.deepseek.com/anthropic` |
| DeepSeek V4 Pro (OpenAI)   | OpenAI    | `https://api.deepseek.com`           |
| DeepSeek V4 Flash (OpenAI) | OpenAI    | `https://api.deepseek.com`           |


## 配置

将以下内容添加到 `~/.factory/settings.json` 的 `customModels` 数组中：

### Anthropic 兼容模型

```json
{
  "model": "deepseek-v4-pro",
  "id": "custom:deepseek-v4-pro---Anthropic",
  "index": 1,
  "baseUrl": "https://api.deepseek.com/anthropic",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Pro",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "anthropic"
},
{
  "model": "deepseek-v4-flash",
  "id": "custom:deepseek-v4-flash---Anthropic",
  "index": 2,
  "baseUrl": "https://api.deepseek.com/anthropic",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Flash",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "anthropic"
}
```

### OpenAI 兼容模型

```json
{
  "model": "deepseek-v4-pro",
  "id": "custom:deepseek-v4-pro---OpenAI",
  "index": 1,
  "baseUrl": "https://api.deepseek.com",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Pro (OpenAI)",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "openai"
},
{
  "model": "deepseek-v4-flash",
  "id": "custom:deepseek-v4-flash---OpenAI",
  "index": 2,
  "baseUrl": "https://api.deepseek.com",
  "apiKey": "<your DeepSeek API Key>",
  "displayName": "DeepSeek V4 Flash (OpenAI)",
  "maxOutputTokens": 384000,
  "noImageSupport": false,
  "provider": "openai"
}
```

## 设置为 Mission Model（可选）

要将 DeepSeek 设为默认的 worker/validation 模型，请在同一文件中更新 `missionModelSettings`：

```json
"missionModelSettings": {
  "workerModel": "custom:deepseek-v4-pro---Anthropic",
  "workerReasoningEffort": "none",
  "validationWorkerModel": "custom:deepseek-v4-flash---Anthropic",
  "validationWorkerReasoningEffort": "none",
  "skipUserTesting": true,
  "skipScrutiny": true
}
```

## 了解 Provider 类型

Factory 支持三种 Provider 类型，决定 API 兼容性：


| Provider                      | API 格式                               | 适用场景                                                              | 文档                                                                                 |
| ----------------------------- | ------------------------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `anthropic`                   | Anthropic Messages API (v1/messages) | Anthropic 官方 API 或兼容代理上的 Anthropic 模型                             | [Anthropic Messages API](https://docs.anthropic.com/en/api/messages)               |
| `openai`                      | OpenAI Responses API                 | OpenAI 官方 API 或兼容代理上的 OpenAI 模型。新模型如 GPT-5 和 GPT-5-Codex 必须使用此类型。 | [OpenAI Responses API](https://platform.openai.com/docs/api/responses)             |
| `generic-chat-completion-api` | OpenAI Chat Completions API          | OpenRouter、Fireworks、Together AI、Ollama、vLLM 及大多数开源 providers     | [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) |


DeepSeek V4 Pro 和 V4 Flash 支持 `anthropic` 和 `openai` 两种 Provider 类型。

## 注意事项

- 将 `<your DeepSeek API Key>` 替换为您的实际 DeepSeek API Key，或使用环境变量语法：`"apiKey": "${DEEPSEEK_API_KEY}"`
- 最大输出 tokens：384,000
- Model indices 在所有 custom models 中必须唯一
- 启动 Droid 前设置环境变量：`export DEEPSEEK_API_KEY=your_key_here`

## 故障排除

**模型未出现在选择器中**

- 检查 `~/.factory/settings.json`（或旧版格式的 `config.json`）中的 JSON 语法
- 设置更改通过文件监视自动检测
- 验证所有必需字段都存在

**"Invalid provider" 错误**

- Provider 必须恰好是 `anthropic`、`openai` 或 `generic-chat-completion-api`
- 检查拼写并确保大小写正确

**认证错误**

- 验证您的 API Key 有效且有可用配额
- 检查 API Key 具有适当的权限
- 确认 Base URL 与您的 provider 文档匹配

**速率限制或配额错误**

- 检查您的 provider 的速率限制和配额
- 通过 provider 的仪表板监控使用情况

