[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Codex

Codex 是 OpenAI 的编程 Agent，支持 CLI 和 App 使用。Codex 使用 OpenAI Responses API 与模型通信，因此需要一个转发层处理请求。

## 选择代理方案

| 方案 | 说明 |
| ---- | ---- |
| [@codeproxy/cli](https://github.com/codeproxy-ai/cli) | 轻量级 npm 代理。将 Responses API 转换为 Chat Completions 或 Anthropic Messages。无需 Go。 |
| [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) | 基于 Go 的代理，支持高级路由、模型目录自动生成和 DeepSeek V4 扩展。 |

按对应项目的 README 启动代理后，按下方步骤配置 Codex。

## 配置 Codex

创建或编辑 `~/.codex/config.toml`，指向你启动的代理：

```toml
[model_providers.deepseek]
name = "DeepSeek"
base_url = "http://127.0.0.1:8787/v1"
wire_api = "responses"

[profiles.deepseek-pro]
model = "deepseek-v4-pro"
model_provider = "deepseek"
model_context_window = 1000000
model_reasoning_effort = "high"
```

> **注意：** 请根据代理实际监听的地址调整 `base_url` 和端口。

## 验证

```shell
curl http://127.0.0.1:8787/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro",
    "input": "请用一句话打个招呼。",
    "max_output_tokens": 100
  }'
```

## 启动 Codex

```shell
cd /path/to/my-project
codex
```

## 相关资源

- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
