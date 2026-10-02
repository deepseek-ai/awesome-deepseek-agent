[English](./cowagent.md) | [简体中文](./cowagent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 CowAgent

[CowAgent](https://github.com/zhayujie/CowAgent) 是一个开源的 AI Agent，能够主动思考和任务规划，内置工具、技能、长期记忆和个人知识库。支持 DeepSeek、MiniMax、Claude、Gemini、OpenAI、GLM、Qwen、Doubao、Kimi 等主流模型，可运行在 Web 控制台，或接入微信、飞书、钉钉、企业微信、QQ 等聊天通道。CowAgent 的默认模型是 DeepSeek V4，并支持 100 万 token 上下文窗口。

#### 1. 安装 CowAgent

CowAgent 提供一键安装脚本，支持 Linux、macOS、Windows。脚本会自动处理依赖、把项目克隆到 `~/CowAgent`、安装 `cow` CLI、进入交互式配置并启动服务。

Linux / macOS：

```bash
bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)
```

Windows (PowerShell)：

```powershell
irm https://cdn.link-ai.tech/code/cow/run.ps1 | iex
```

安装完成后，Web 控制台运行在 `http://localhost:9899`。

常用管理命令（完整命令见 [CLI 文档](https://docs.cowagent.ai/cli/index)）：

```bash
cow start | stop | restart | status | logs | update
```

#### 2. 在 CowAgent 中配置 DeepSeek

**方式 A — Web 控制台（推荐）**

1. 浏览器打开 `http://localhost:9899`。
2. 进入 **模型管理** 页面。
3. 选择厂商 **DeepSeek**，填入 [DeepSeek API Key](https://platform.deepseek.com/api_keys)，并选择模型名称：`deepseek-v4-flash`（默认）或 `deepseek-v4-pro`。
4. 保存后即时生效，无需重启服务。

如需启用深度思考并调整推理强度，请在 **配置 → Agent** 页面打开 **深度思考** 开关。日常 Agent 任务使用默认的 `reasoning_effort=high` 即可；遇到复杂编码或长链路规划时，建议将模型切换为 `deepseek-v4-pro` 并把 `reasoning_effort` 设置为 `max`。

**方式 B — 修改 `config.json`**

编辑 `~/CowAgent/config.json`：

```json
{
  "model": "deepseek-v4-flash",
  "deepseek_api_key": "YOUR_API_KEY",
  "deepseek_api_base": "https://api.deepseek.com/v1",
  "enable_thinking": true,
  "reasoning_effort": "high"
}
```

| 参数 | 说明 |
| --- | --- |
| `model` | `deepseek-v4-flash`（默认）或 `deepseek-v4-pro` |
| `deepseek_api_key` | 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 |
| `deepseek_api_base` | 可选，默认 `https://api.deepseek.com/v1`，可改为第三方代理地址 |
| `enable_thinking` | 开启 DeepSeek V4 思考模式。Web 控制台会实时展示思考过程；IM 通道虽不展示但同样获得更高的回答质量 |
| `reasoning_effort` | `high`（默认）或 `max`。复杂 Agent 任务建议搭配 `deepseek-v4-pro` 使用 `max`。仅在 `enable_thinking` 为 `true` 时生效 |

DeepSeek V4 最高支持 **1,000,000** token 上下文。可通过 `agent_max_context_tokens` 配置控制 CowAgent 发给模型的上下文上限，处理超长文档时可按需调高。

修改后执行 `cow restart`（或 `./run.sh restart`）生效。

#### 3. 开始使用

打开 Web 控制台即可与 Agent 对话，会实时流式展示思考过程、工具调用和最终回答，技能、记忆、知识库均可在左侧边栏中管理。

如果希望在聊天工具中使用，可以在 **通道管理** 页面配置消息平台，同一个 DeepSeek 模型即可同时服务所有通道。

更多配置请参阅 [CowAgent 文档](https://docs.cowagent.ai/) 和 [DeepSeek 模型说明](https://docs.cowagent.ai/models/deepseek)。
