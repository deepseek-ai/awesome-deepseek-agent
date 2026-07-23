[English](./aider.md) | [简体中文](./aider.zh-CN.md) · [← Back](../README.md)
# 集成 Aider
[Aider](https://aider.chat/) 是一款运行在终端中的 AI 结对编程工具。它支持任意 OpenAI 兼容 API，可无缝接入 DeepSeek 模型。

### 安装 Aider
```bash
pip install aider-install
aider-install
```

### 配置 Aider
Aider 通过 OpenAI 兼容端点接入 DeepSeek。推荐使用环境变量配置，也可使用 `.env` 文件。

#### 第一步：设置环境变量
设置 DeepSeek API Key 和端点地址。在 [DeepSeek 平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**Mac / Linux：**
```bash
export OPENAI_API_BASE=https://api.deepseek.com
export OPENAI_API_KEY=<你的 DeepSeek API Key>
```

**Windows (PowerShell)：**
```powershell
$env:OPENAI_API_BASE="https://api.deepseek.com"
$env:OPENAI_API_KEY="<你的 DeepSeek API Key>"
```

**Windows (setx，设置后需重启 shell)：**
```cmd
setx OPENAI_API_BASE https://api.deepseek.com
setx OPENAI_API_KEY <你的 DeepSeek API Key>
```

#### 第二步：添加模型元数据（推荐）
Aider 默认不包含 DeepSeek V4 模型的元数据。在项目根目录创建 `.aider.model.metadata.json`（或通过 `AIDER_MODEL_METADATA_FILE` 指定路径），提供上下文窗口和定价信息：

```json
{
  "openai/deepseek-v4-pro": {
    "max_tokens": 384000,
    "max_input_tokens": 1000000,
    "max_output_tokens": 384000,
    "input_cost_per_token": 4.35e-7,
    "output_cost_per_token": 8.7e-7,
    "input_cost_per_token_cache_hit": 3.625e-9,
    "cache_read_input_token_cost": 3.625e-9,
    "litellm_provider": "openai",
    "mode": "chat",
    "supports_assistant_prefill": true,
    "supports_prompt_caching": true
  },
  "openai/deepseek-v4-flash": {
    "max_tokens": 384000,
    "max_input_tokens": 1000000,
    "max_output_tokens": 384000,
    "input_cost_per_token": 1.4e-7,
    "output_cost_per_token": 2.8e-7,
    "input_cost_per_token_cache_hit": 2.8e-9,
    "cache_read_input_token_cost": 2.8e-9,
    "litellm_provider": "openai",
    "mode": "chat",
    "supports_assistant_prefill": true,
    "supports_prompt_caching": true
  }
}
```

> **说明：** 此文件告知 Aider DeepSeek V4 支持 100 万上下文窗口及当前定价，可消除模型警告并启用准确的 token 统计。

### 使用 Aider
进入项目目录，启动 Aider 并指定 DeepSeek 模型：

```bash
cd /path/to/your/project
aider --model openai/deepseek-v4-pro
```

使用 DeepSeek V4 Flash（更快、更便宜）：
```bash
aider --model openai/deepseek-v4-flash
```

#### 启用最强推理模式
DeepSeek V4 Pro 支持多级推理努力。使用 `max` 级别获得最佳编码体验：

```bash
aider --model openai/deepseek-v4-pro --reasoning-effort max
```

或在 `.aider.model.settings.yml` 中配置：
```yaml
- name: openai/deepseek-v4-pro
  extra_params:
    reasoning_effort: max
```

#### 验证配置
启动时添加 `--verbose` 可查看是否已正确连接到 DeepSeek：
```bash
aider --model openai/deepseek-v4-pro --verbose
```

Aider 会在启动时显示 `API Base: https://api.deepseek.com` 和当前模型名称。

### 模型选择指南

| 模型 | 适用场景 | 核心优势 |
|------|---------|---------|
| `openai/deepseek-v4-pro` | 复杂重构、架构设计 | 深度推理、100 万上下文 |
| `openai/deepseek-v4-flash` | 快速编辑、提交信息、对话摘要 | 低成本、响应快 |

> **提示：** 将 `deepseek-v4-flash` 设为 `--weak-model` 用于提交信息和对话摘要以节省成本，主编码任务仍使用 `deepseek-v4-pro`。
