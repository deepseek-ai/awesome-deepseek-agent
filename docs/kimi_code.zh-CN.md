[English](./kimi_code.md) | [简体中文](./kimi_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Kimi Code

Kimi Code 是月之暗面开发的一款开源的终端 AI Agent。

- **GitHub：** <https://github.com/MoonshotAI/kimi-code>
- **文档：** <https://moonshotai.github.io/kimi-code/zh/>

#### 1. 安装 Kimi Code

运行对应平台的官方安装脚本。

Linux / macOS：

```shell
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

Windows PowerShell：

```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

也可以通过 npm 安装 Kimi Code。此方式要求 Node.js 22.19.0 或更高版本：

```shell
npm install -g @moonshot-ai/kimi-code
```

确认安装成功：

```shell
kimi --version
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建并复制 API Key。

#### 3. 配置 DeepSeek

创建或编辑 Kimi Code 配置文件：

- Linux / macOS：`~/.kimi-code/config.toml`
- Windows：`C:\Users\<name>\.kimi-code\config.toml`

如果文件中已有其他设置，请把下面的配置块合并进去，不要覆盖整个文件。将 `YOUR_DEEPSEEK_API_KEY` 替换为你的 DeepSeek API Key：

```toml
default_model = "deepseek-v4-pro"

[thinking]
enabled = true
effort = "max"
keep = "all"

[providers.deepseek]
type = "openai"
base_url = "https://api.deepseek.com"
api_key = "YOUR_DEEPSEEK_API_KEY"

[models.deepseek-v4-pro]
provider = "deepseek"
model = "deepseek-v4-pro"
display_name = "DeepSeek V4 Pro"
max_context_size = 1000000
capabilities = ["always_thinking", "tool_use"]
support_efforts = ["high", "max"]
default_effort = "max"

[models.deepseek-v4-flash]
provider = "deepseek"
model = "deepseek-v4-flash"
display_name = "DeepSeek V4 Flash"
max_context_size = 1000000
capabilities = ["always_thinking", "tool_use"]
support_efforts = ["high", "max"]
default_effort = "max"
```

这份配置会添加 DeepSeek V4 Pro 和 DeepSeek V4 Flash，设置模型的 100 万 token 上下文窗口，启用工具调用与 Thinking 模式，并默认使用 DeepSeek V4 Pro 和 `max` 推理强度。

Kimi Code 的 OpenAI 兼容 Provider 会自动在工具调用轮次之间保留 DeepSeek 的 `reasoning_content`，确保 Thinking 模式可以正常执行多步骤 Agent 任务。

#### 4. 校验配置

无需启动 TUI，直接运行以下命令校验配置：

```shell
kimi doctor config
```

配置有效时，Kimi Code 会报告 `config.toml` 状态为 OK。

#### 5. 启动 Kimi Code

进入项目目录并启动 Kimi Code：

```shell
cd /path/to/your-project
kimi
```

Kimi Code 默认使用 DeepSeek V4 Pro。在交互会话中输入 `/model`，可在 DeepSeek V4 Pro 和 DeepSeek V4 Flash 之间切换。

如需跳过交互式 TUI，直接运行单次任务：

```shell
kimi -p "检查这个项目的顶层文件，并总结项目用途。"
```

#### 常见问题

- 出现 `401` 或认证错误：确认 `api_key` 中填写了有效的 DeepSeek API Key。
- 出现 `402` 或余额不足：检查 DeepSeek 开放平台余额。
- 出现 `404` 或找不到模型：确认模型 ID 严格写成 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- 提示 `No model configured`：确认 `default_model` 与 `[models]` 下的某个 key 完全一致，然后运行 `kimi doctor config`。
