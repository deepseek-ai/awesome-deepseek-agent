[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Codex

Codex 是 OpenAI 的编程 Agent，支持 CLI 和 App 使用。Codex 使用 OpenAI Responses API 与模型通信，因此需要一个转发层处理请求。

请选择以下任意方案：

| 方案 | 说明 |
| ---- | ---- |
| [@codeproxy/cli](https://github.com/codeproxy-ai/cli) | 轻量级 npm 代理。将 Responses API 转换为 Chat Completions 或 Anthropic Messages。无需代码生成，无需 Go。 |
| [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) | 基于 Go 的代理，支持高级路由、模型目录自动生成和 DeepSeek V4 扩展。 |

## 相关资源

- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
