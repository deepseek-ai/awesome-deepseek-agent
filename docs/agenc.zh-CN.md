[English](./agenc.md) | [简体中文](./agenc.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 AgenC Core

AgenC Core 是一款开源的终端 AI 编程 Agent，采用 MIT 许可证。它内置 `deepseek` 提供商，直接调用 DeepSeek API。模型目录包含 `deepseek-flash`（DeepSeek-V4.1-Flash）和 `deepseek-v4-pro`，两者都默认开启思考模式，并支持完整的 100 万 token 上下文窗口。你可以在终端界面中交互使用，也可以在脚本和 CI 中用 `agenc -p` 无界面运行，或者启动后台 Agent。

在 `deepseek-flash` 搭配 `max` 推理强度并开启轻量模式（`agenc --light`，实验性功能）的配置下，AgenC Core 在 Terminal-Bench 2.1 上得分 76.2%（445 次试验中通过 339 次），Harbor Hub 列出的花费为 34 美元（[公开运行记录](https://hub.harborframework.com/jobs/71f39f3b-22f8-4dbe-9f25-2b039d3a4534)）。

- **GitHub：** <https://github.com/tetsuo-ai/agenc-core>
- **官网：** <https://get.agenc.ag>

#### 1. 安装 AgenC Core

macOS / Linux：

```bash
curl -fsSL https://get.agenc.ag/install.sh | sh
```

安装脚本自带经过校验的 Node.js 运行时，会把 `agenc` 命令安装到 `~/.local/bin`，并以用户服务的形式启动 AgenC 守护进程。

Windows（PowerShell）：

```powershell
iwr -useb https://get.agenc.ag/install.ps1 | iex
```

Windows 需要先安装 [Git for Windows](https://git-scm.com/download/win)，因为会话通过其中的 `bash.exe` 运行 shell。AgenC 目前还没有原生的 Windows 沙箱。如需沙箱化会话，请在 WSL2 中（并安装 bubblewrap）使用上面的 macOS / Linux 命令安装并运行 AgenC。

npm（需要 Node.js 26.x，且版本不低于 26.5）：

```bash
npm install -g @tetsuo-ai/agenc
```

验证安装：

```bash
agenc --version
```

#### 2. 配置 DeepSeek 提供商

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**方式 A：设置向导（推荐）**

```bash
agenc onboard
```

- 在 **provider** 步骤中选择 **DeepSeek**。
- 在 **model access** 步骤中粘贴你的 DeepSeek API Key。AgenC 会先用 DeepSeek API 验证该 Key，再把它保存到操作系统的安全存储中。
- 随后的 **connection-test** 步骤会向 DeepSeek 发送一次真实请求。

**方式 B：环境变量**

Linux / Mac 用户：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows 用户：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

**设置默认模型与推理强度**

无论使用哪种方式，都执行一次以下命令：

```bash
agenc config set model_provider deepseek
agenc config set model deepseek-flash
agenc config set reasoning_effort max
```

这些命令会把下列配置写入 `~/.agenc/config.toml`（执行 `agenc config path` 可查看实际路径）：

```toml
config_version = 2
model_provider = "deepseek"
model = "deepseek-flash"
reasoning_effort = "max"
```

可用模型：

| 模型 ID | DeepSeek 模型 | 上下文窗口 | 单次输出 | 推理强度 | 图片输入 |
| --- | --- | --- | --- | --- | --- |
| `deepseek-flash`（默认） | DeepSeek-V4.1-Flash | 100 万 token | 默认 64,000，最高 384K | `low`、`high`（默认）、`max` | 支持 |
| `deepseek-v4-pro` | DeepSeek-V4-Pro | 100 万 token | 默认 64,000，最高 384K | `low`、`high`（默认）、`max` | 不支持 |

- **100 万上下文：** AgenC 的模型目录为两个模型都设置了 1,048,576 token 的上下文窗口，无需额外配置。如果你通过代理访问 DeepSeek，并且需要从第一轮起就使用固定上限，可以设置 `providers.deepseek.context_window_tokens` 和 `providers.deepseek.max_output_tokens`。
- **最高推理强度：** AgenC 在每次请求中都会发送 `thinking: {"type": "enabled"}`，并把你设置的强度作为 `reasoning_effort` 发送。`max` 会原样传给 DeepSeek。如果不设置推理强度，模型使用默认值 `high`。
- **多轮工具调用：** 按照 [思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode) 对工具调用的要求，AgenC 会在后续请求中把 `reasoning_content` 回传给 DeepSeek。
- **旧模型 ID：** `deepseek-v4-flash` 仍然可用，DeepSeek 会用 DeepSeek-V4.1-Flash 处理该请求。新配置请使用 `deepseek-flash`。
- **Base URL：** AgenC 默认使用 `https://api.deepseek.com/v1`。只有通过代理访问时，才需要设置 `DEEPSEEK_BASE_URL` 或 `providers.deepseek.base_url`。

#### 3. 运行并选择模型

进入项目目录并启动 AgenC：

```bash
cd /path/to/my-project
agenc
```

在终端界面中：

- `/effort` 查看或修改推理强度。`/effort max` 会立即作用于当前会话，并保存为新会话的默认值。
- `/model` 在 `deepseek-flash` 和 `deepseek-v4-pro` 之间切换。
- `/provider` 用于接入其他提供商或保存新的 API Key。
- `/help` 列出全部 slash 命令。

也可以在命令行中为单次运行指定提供商和模型：

```bash
# 使用 DeepSeek-V4-Pro 的交互式会话
agenc --provider deepseek --model deepseek-v4-pro

# 无界面的一次性运行，适用于脚本和 CI
agenc --provider deepseek --model deepseek-flash -p "运行测试并修复失败的用例"
```

请同时传入 `--provider deepseek` 和 `--model`。部分模型 ID（例如 `deepseek-v4-pro`）在 AgenC 的模型目录中也属于其他提供商，如果只指定模型且匹配到多个提供商，AgenC 会拒绝这种选择。

最新价格请查看 DeepSeek 的 [模型与价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 页面。AgenC 的会话费用估算按 DeepSeek 的高峰时段价格计算，因此在低峰时段调用的实际费用会低于估算值。

#### 4. 进阶用法

- **MCP 服务：** 使用 `agenc mcp add <name> <command-or-url>` 添加服务，使用 `agenc mcp list` 查看已添加的服务。
- **后台 Agent：** 使用 `agenc agent start "<目标>"` 启动后台 Agent。使用 `agenc --continue` 继续之前的会话。
- **聊天渠道：** 执行 `agenc onboard channel`，即可通过 Telegram、Discord、Slack 或 WebChat 使用你的 Agent。

#### 常见问题

- 执行 `agenc providers` 查看各提供商的凭据状态。完成配置后，`deepseek` 一行应显示已有凭据。
- 如果环境中设置了 `DEEPSEEK_MODEL`（部分其他 DeepSeek 工具会使用该变量），AgenC 会拒绝启动。请取消该变量，改用 `--model`、`AGENC_MODEL` 或 `config.toml` 中的 `model` 选择模型。
- 在原生 Windows 上，沙箱化的权限模式会拒绝启动会话（`sandbox_required_unavailable`）。请改在 WSL2 中运行 AgenC。
- 执行 `agenc doctor` 检查安装本身是否正常。
