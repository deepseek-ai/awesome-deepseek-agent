[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Grok Build

Grok Build（`grok`）是 xAI 的终端编程 Agent：一个全屏 TUI，能够读取代码库、编辑文件、执行 shell 命令并调用 MCP 工具。它默认使用 xAI 托管的 Grok 模型，同时支持 OpenAI Chat Completions、OpenAI Responses 与 Anthropic Messages 三种协议，因此可以在 `~/.grok/config.toml` 中把 DeepSeek V4 添加为自定义模型。

对于自定义模型，Grok 默认使用 OpenAI Chat Completions 后端，DeepSeek V4 可直接在其上工作，多轮工具调用同样正常。

#### 1. 安装 Grok Build

macOS / Linux / Windows（Git Bash）：

```shell
curl -fsSL https://x.ai/cli/install.sh | bash
```

Windows（PowerShell）：

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

验证安装：

```shell
grok --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。

#### 3. 将 Key 放入环境变量

Linux / macOS：

```shell
export DEEPSEEK_API_KEY="sk-..."
```

Windows（PowerShell）：

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

请把 Key 放在环境变量里，而不要内联写进 `config.toml`。Grok 的凭据解析顺序是：`api_key` → `env_key` → **已登录的 grok.com 会话令牌** → `XAI_API_KEY`。如果 `env_key` 指定的变量没有设置，Grok **不会**提示缺少 Key，而是会把你的 grok.com 会话令牌静默发送给 DeepSeek 端点，随后报出一个极具误导性的认证错误。请在启动 `grok` 的同一个 shell 会话中设置该变量。

#### 4. 在 `config.toml` 中添加 DeepSeek V4

配置文件：`~/.grok/config.toml`（Windows：`%USERPROFILE%\.grok\config.toml`）；可用 `GROK_HOME` 指定其他目录。文件不存在则新建。

```toml
[models]
default = "deepseek-v4-pro"
default_reasoning_effort = "max"

[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Pro"
env_key = "DEEPSEEK_API_KEY"
context_window = 1000000
reasoning_efforts = ["low", "high", "max"]

[model.deepseek-v4-flash]
model = "deepseek-v4-flash"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Flash"
env_key = "DEEPSEEK_API_KEY"
context_window = 1000000
reasoning_efforts = ["low", "high", "max"]
```

- 这里刻意不写 `api_backend`，它默认为 `chat_completions`。
- `context_window` 决定 Grok 何时触发自动压缩。DeepSeek V4 支持 100 万 token 上下文，其 `/v1/models` 自报 1,048,576，配置成 1,000,000 是安全的。
- `reasoning_efforts` 对 DeepSeek 是必需的。Grok 通常从端点的 `/v1/models` 响应里构建思考强度档位，而 DeepSeek 把档位写成 `effort.supported_levels`，Grok 不识别这种形状；因此不写这一行时，`default_reasoning_effort` 与 `/effort` 会被静默丢弃，模型实际运行在 DeepSeek 自己的默认档 `high`。写上之后，`max` 会以 `reasoning_effort` 出现在请求体中。
- `deepseek-v4-flash` 是当前模型名，DeepSeek 同时接受别名 `deepseek-flash`。

#### 5. 首次运行

```shell
cd /path/to/my-project
grok
```

也可以只在单次运行中指定模型：

```shell
grok -m deepseek-v4-pro --effort max
```

查看模型目录与当前默认模型：

```shell
grok models
```

在 TUI 中：

| 命令 | 作用 |
| --- | --- |
| `/model deepseek-v4-pro` | 为当前会话切换模型 |
| `/effort max` | 为当前会话设置思考强度 |
| `Ctrl+M` | 打开模型选择器（需在回滚窗格中） |

#### 排障

- **报 `Your api key: ****xxxx is invalid` 且伴随 `Auth: Oidc`** —— `env_key` 指定的变量对进程不可见，Grok 已回退到你的 grok.com 会话令牌。重新导出 `DEEPSEEK_API_KEY` 并重启 `grok`；在设置该变量之前就已打开的终端不会带上它。
- **思考强度似乎不起作用** —— 按第 4 步给模型块加上 `reasoning_efforts = ["low", "high", "max"]`。
- **某个模型没有出现在 `grok models` 中** —— `[models] default` 指向一个不存在的模型时会被静默忽略。请同时检查 `[model.<name>]` 段名与 `default` 取值的拼写。
- **不要设置 `[endpoints] models_base_url`** —— 它会连 Grok 内置模型一起重定向，并把认证方式从会话切换为 API Key，导致 `grok login` 失效。
- **只用 BYOK 模型时无需 `grok login`** —— 自带凭据的自定义模型可以独立工作。xAI 侧的功能（模型目录、`grok update`、插件市场）仍然需要已登录的会话。

#### 相关资源

- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
- [DeepSeek 开放平台](https://platform.deepseek.com/)
