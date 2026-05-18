[English](./callcopilot.md) | [简体中文](./callcopilot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 callCopilot

[callCopilot](https://github.com/qoli/callCopilot) 是一个 GitHub Copilot CLI BYOK provider 独立启动器。它为 Copilot CLI 封装了 DeepSeek V4 别名、本地代理启动、token 上限元数据，以及官方 DeepSeek Anthropic 兼容端点所需的 thinking block 保留逻辑。

如果你希望用 DeepSeek 运行 GitHub Copilot CLI，但不想每次手动导出一组 `COPILOT_PROVIDER_*` 环境变量，可以使用 callCopilot。

#### 1. 安装依赖

安装 GitHub Copilot CLI：

```shell
npm install -g @github/copilot
```

克隆 callCopilot：

```shell
git clone https://github.com/qoli/callCopilot.git
cd callCopilot
```

运行时依赖：

- macOS 系统 Python：`/usr/bin/python3`。
- `node`，用于本地 provider 代理。
- `npm`，首次运行 `ds` 或 `dsf` 时，callCopilot 会在本地安装 `opencode-deepseek-thinking-fix`。
- GitHub Copilot CLI 提供的 `copilot` 命令。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，并复制该 Key。

#### 3. 配置 callCopilot

从示例文件创建 `.env`：

```shell
cp examples/.env.example .env
```

填写 DeepSeek API Key：

```env
DEEPSEEK_API_KEY=sk-your-deepseek-api-key
CALLCOPILOT_DEEPSEEK_PROVIDER_BASE_URL=https://api.deepseek.com/anthropic
```

官方 DeepSeek 别名如下：

| 别名 | Provider | 模型 |
| ---- | -------- | ---- |
| `ds` | DeepSeek Anthropic 兼容 API | `deepseek-v4-pro` |
| `dsf` | DeepSeek Anthropic 兼容 API | `deepseek-v4-flash` |

对于 `ds` 和 `dsf`，callCopilot 会把 Copilot CLI 的 provider type 设置为 `anthropic`，启动本地代理，并把请求转发到 `https://api.deepseek.com/anthropic`。

#### 4. 上下文与 Thinking 配置

DeepSeek V4 支持 100 万 token 上下文窗口。对于官方 DeepSeek 别名，callCopilot 默认向 Copilot CLI 传入以下限制：

```env
COPILOT_PROVIDER_MAX_PROMPT_TOKENS=1048576
COPILOT_PROVIDER_MAX_OUTPUT_TOKENS=393216
```

如有需要，可以覆盖这些值：

```shell
export CALLCOPILOT_DEEPSEEK_MAX_PROMPT_TOKENS=1048576
export CALLCOPILOT_DEEPSEEK_MAX_OUTPUT_TOKENS=393216
```

DeepSeek V4 的 thinking mode 通过本地 Anthropic 兼容代理启用。该代理会在工具调用回合之间保留并重新注入 thinking blocks，使 DeepSeek 能在 Copilot CLI Agent 会话中正确延续推理。

默认 thinking budget 是 `8000` tokens。复杂编程任务可以在启动 callCopilot 前调高该值：

```shell
export DEEPSEEK_THINKING_BUDGET=65536
```

不要把禁用 thinking mode 作为解决 reasoning-content 错误的主要方法。

#### 5. 首次运行

使用 DeepSeek V4 Pro 运行 Copilot CLI：

```shell
bin/callCopilot ds -- -s -p "Reply OK only."
```

使用 DeepSeek V4 Flash：

```shell
bin/callCopilot dsf -- -s -p "Reply OK only."
```

在项目中启动 DeepSeek V4 Pro 的交互式 Copilot CLI Agent 会话：

```shell
cd /path/to/my-project
/path/to/callCopilot/bin/callCopilot ds
```

除非你传入自己的 Copilot CLI 参数，否则 callCopilot 会默认添加 `--autopilot`。

#### 可选：NVIDIA 托管的 DeepSeek

callCopilot 也提供 NVIDIA 托管 DeepSeek 的别名：

```env
NVIDIA_DEEPSEEK_API_KEY=your-nvidia-api-key
CALLCOPILOT_NVIDIA_DEEPSEEK_PROVIDER_BASE_URL=https://integrate.api.nvidia.com/v1
```

运行：

```shell
bin/callCopilot nds -- -s -p "Reply OK only."
```

该路径通过 OpenAI 兼容端点使用 `deepseek-ai/deepseek-v4-pro`。如果需要长上下文，请先确认该 provider 当前的模型限制与可用性。

#### 可选：本地 OpenAI 兼容模型

其他任意模型 ID 会被路由到本地 oMLX OpenAI 兼容后端：

```shell
bin/callCopilot Qwen3.6-35B-A3B-bf16 -- -s -p "Reply OK only."
```

对于本地模型，callCopilot 会从本地 `/v1/models/status` 响应中读取 `max_context_window` 和 `max_tokens`，并把这些值传给 Copilot CLI。因此本地路径受模型服务实际回报的能力限制，而不是固定使用 DeepSeek V4 的 100 万 token 上下文。

#### 相关资源

- [callCopilot GitHub 仓库](https://github.com/qoli/callCopilot)
- [GitHub Copilot CLI BYOK 文档](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models)
- [DeepSeek Thinking Mode 文档](https://api-docs.deepseek.com/guides/thinking_mode)
