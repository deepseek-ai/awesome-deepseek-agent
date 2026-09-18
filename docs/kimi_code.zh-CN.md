[English](./kimi_code.md) | [简体中文](./kimi_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Kimi Code

Kimi Code 是月之暗面（Moonshot AI）开发的、运行在终端中的 AI 编程智能体。它可以同时连接多个大模型平台——既包括 Kimi 官方托管服务，也包括 DeepSeek 等兼容 OpenAI 协议的第三方推理服务。

### 从零安装 Kimi Code

Kimi Code 基于 Node.js 并通过 npm 分发，各平台均提供官方安装脚本。

#### 方式一：官方安装脚本（推荐）

- macOS / Linux：

```
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

- Windows（PowerShell）：

```
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

> Windows 用户在首次启动前需安装 [Git for Windows](https://git-scm.com/download/win)，Kimi Code 使用其内置的 Git Bash 作为 shell 环境。

#### 方式二：通过 npm 安装

需要 Node.js 22.19.0 或更高版本：

```
npm install -g @moonshot-ai/kimi-code
```

安装完成后，执行以下命令验证可执行文件已就绪：

```
kimi --version
```

### 配置 Kimi Code

Kimi Code 从 `~/.kimi-code/config.toml` 读取配置（首次运行时自动创建）。按以下步骤添加 DeepSeek 提供商与模型别名。

#### 第一步：添加 DeepSeek 提供商

```toml
[providers.deepseek]
type = "openai"                          # DeepSeek 使用 OpenAI 兼容协议
base_url = "https://api.deepseek.com/v1"
api_key = "sk-<你的DeepSeek API Key>"     # 在 https://platform.deepseek.com/api_keys 获取
```

> **提示：** 如果希望凭据使用提供商惯例的字段名而非 `api_key` 字段，可以把它放进提供商的 `env` 子表中——它仅在 `api_key` 为空时被采用，并且只从配置文件读取（绝不读取你的 shell 环境变量）：
>
> ```toml
> [providers.deepseek.env]
> DEEPSEEK_API_KEY = "sk-<你的DeepSeek API Key>"
> ```
>
> 注意：无论哪种方式，密钥都以明文存储在 `config.toml` 中——Kimi Code 只从配置文件读取提供商凭据，不会回退到 shell 环境变量。若与他人共用机器，请收紧文件权限（`chmod 600`）。

#### 第二步：声明 DeepSeek V4 模型

```toml
[models."deepseek/v4-pro"]
provider = "deepseek"
model = "deepseek-v4-pro"              # 当前模型名称（DeepSeek V4）
max_context_size = 1000000             # 100 万 token 上下文窗口
capabilities = [ "tool_use" ]
display_name = "DeepSeek V4 Pro"

[models."deepseek/v4-flash"]
provider = "deepseek"
model = "deepseek-v4-flash"
max_context_size = 1000000             # 100 万 token 上下文窗口
capabilities = [ "tool_use" ]
display_name = "DeepSeek V4 Flash"
```

#### 第三步：将 DeepSeek 设为默认模型（可选）

```toml
default_model = "deepseek/v4-pro"
```

#### 可选：思考模式 / 推理强度

DeepSeek V4 Pro 支持多个推理强度级别（`max` 和 `high`）。Kimi Code 会自动处理 OpenAI 兼容提供商的 `reasoning_content` 字段并注入 `reasoning_effort`，因此推理能力开箱即用。若希望默认开启思考并采用最高强度：

```toml
[thinking]
enabled = true
effort = "max"
```

> 如果上游 API 拒绝了配置的强度值，请改用该模型实际支持的级别（DeepSeek V4 Pro 支持 `high` / `max`）。

### 使用 Kimi Code + DeepSeek

- 在项目目录中启动交互式 TUI：

```
cd /path/to/my-project
kimi
```

- 不进入交互界面，直接执行单条指令：

```
kimi -p "看一下这个项目的目录结构"
```

- 运行时切换模型：输入 `/model`，选择 `deepseek/v4-pro` 或 `deepseek/v4-flash`。
- 交互式管理提供商：在 TUI 中输入 `/provider`（非交互环境的等价命令为 `kimi provider`）。

DeepSeek V4 支持 100 万 token 上下文窗口，上文 `max_context_size = 1000000` 已如实反映——浏览大型代码库和长时间重构开箱即用。
