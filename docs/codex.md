[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex

Codex is OpenAI's coding agent, available as a CLI and app. Codex communicates with models through the OpenAI Responses API, so it needs a forwarding layer to handle requests.

Choose one of the following solutions:

| Solution | Description |
| -------- | ----------- |
| [@codeproxy/cli](https://github.com/codeproxy-ai/cli) | Lightweight, npm-based proxy. Translates Responses API to Chat Completions or Anthropic Messages. No code generation, no Go required. |
| [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) | Go-based proxy with advanced routing, model catalog auto-generation, and DeepSeek V4 extensions. |

## Resources

- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
