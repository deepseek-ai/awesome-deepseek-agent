[English](./octomind.md) | [简体中文](./octomind.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Octomind

Octomind 是一个用 Rust 编写的开源（Apache-2.0）AI 编程 Agent 运行时。它以命令行为核心，以单一二进制文件发布，支持任意模型，并原生支持 MCP。内置的 `deepseek` 供应商直接调用 DeepSeek API，支持 DeepSeek-V4-Pro 与 DeepSeek-V4-Flash，以及 100 万 token 上下文窗口和 `max` 推理强度。

- **GitHub：** <https://github.com/muvon/octomind>
- **官网：** <https://octomind.run>

#### 1. 安装 Octomind

- 在命令行界面，执行以下命令安装 Octomind（适用于 Linux 和 macOS；Windows 用户请在 Git Bash 或 MSYS2 中执行）：

```bash
curl -fsSL https://raw.githubusercontent.com/muvon/octomind/master/install.sh | bash
```

- 脚本会安装到 `~/.local/bin/`。如果安装后提示找不到命令，请将该目录加入 `PATH`：

```bash
export PATH="$HOME/.local/bin:$PATH"
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```bash
octomind --version
```

> **注意：** macOS 用户也可以通过 Homebrew 安装：`brew install muvon/tap/octomind`。

#### 2. 配置 DeepSeek 供应商

Octomind 使用 `provider:model` 格式的字符串选择模型，因此 DeepSeek 模型分别为 `deepseek:deepseek-v4-pro` 和 `deepseek:deepseek-v4-flash`。无需配置 Base URL：内置供应商直接使用 DeepSeek 官方接口地址。

其中 API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

设置环境变量：

Linux / Mac 用户：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows 用户：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

生成默认配置：

```bash
octomind config
```

Octomind 会合并配置目录中的所有 `*.toml` 文件，因此可以将 DeepSeek 相关设置单独放在 `config.toml` 旁边的文件中：

- **Linux / macOS**：`~/.local/share/octomind/config/deepseek.toml`
- **Windows**：`%LOCALAPPDATA%\octomind\config\deepseek.toml`

```toml
# 顶层键必须写在第一个 [table] 标题之前。
# 启用 100 万 token 上下文窗口（默认上限为 200,000 token）。
max_session_tokens_threshold = 1000000

[model]
name = "deepseek:deepseek-v4-pro"
reasoning_effort = "max"

[supervisor.model]
name = "deepseek:deepseek-v4-flash"

[compression.model]
name = "deepseek:deepseek-v4-flash"
```

- `[model]` 是主 Agent 使用的模型。`reasoning_effort = "max"` 会以 `reasoning_effort: "max"` 发送给 DeepSeek；`"high"` 对应 `high`，`"none"` 则关闭思考模式。
- `[supervisor.model]` 和 `[compression.model]` 默认使用 `octohub:auto`（Octomind Cloud）。请同样将它们指向 DeepSeek，确保所有请求都使用你的 DeepSeek Key。
- Octomind 会将会话上限限制在模型的 100 万上下文窗口减去预留的输出长度（即 `[model]` 中的 `max_tokens`，默认 32,768；DeepSeek V4 最多支持 384K 输出 token）。

检查配置：

```bash
octomind config --validate
```

#### 3. 运行并选择模型

- 进入项目目录，启动编程 Agent `developer:general`（直接执行 `octomind run` 则会启动通用助手）。首次运行时，Octomind 可能会自动安装该 Agent 所需的工具：

```bash
cd /path/to/my-project
octomind run developer:general
```

- 输入 `/model deepseek:deepseek-v4-flash`（或 `/model deepseek:deepseek-v4-pro`）可在会话中切换模型。
- 输入 `/effort max`（或 `/effort high`）可调整当前会话的推理强度。
- 输入 `/info` 可查看 token 用量和费用。

如需在单次运行中临时使用其他模型而不修改配置，可传入 `-m` 参数：

```bash
octomind run -m deepseek:deepseek-v4-flash developer:general
```

> **注意：** DeepSeek 价格页面目前将 Flash 模型列为 `deepseek-flash`（DeepSeek-V4.1-Flash）；`deepseek-v4-flash` 名称仍可使用，并按 Flash 价格计费。Octomind 两个名称均支持。

更多配置选项请参阅 Octomind 的 [供应商指南](https://github.com/muvon/octomind/blob/master/doc/usage/04-providers.md) 和 [配置参考](https://github.com/muvon/octomind/blob/master/doc/reference/03-config-reference.md)。
