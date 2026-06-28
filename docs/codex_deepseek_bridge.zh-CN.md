[English](./codex_deepseek_bridge.md) | [简体中文](./codex_deepseek_bridge.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Codex DeepSeek Bridge

[Codex DeepSeek Bridge](https://github.com/JetXu-LLM/codex-deepseek-bridge) 是一个本地 bridge，可以让 OpenAI Codex app 或 CLI 使用 DeepSeek。Codex 继续使用原生 Responses API 工作流，bridge 负责把模型请求转换为 DeepSeek 的 Chat Completions API。

- **GitHub:** <https://github.com/JetXu-LLM/codex-deepseek-bridge>

bridge 使用稳定的 Codex 侧模型名（`deepseek-pro` 和 `deepseek-flash`），并映射到当前 DeepSeek 模型（`deepseek-v4-pro` 和 `deepseek-v4-flash`）。DeepSeek API Key 保存在本机。

#### 1. 安装 Codex 和 bridge

先安装 [Codex app](https://developers.openai.com/codex/) 或 Codex CLI。如果使用 CLI：

```sh
npm install -g @openai/codex
codex --version
```

然后下载 bridge binary。bridge binary 不需要 Node.js 运行环境。

macOS Apple Silicon:

```sh
curl -L -o codex-deepseek-bridge-macos https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos
./codex-deepseek-bridge-macos --version
```

macOS Intel:

```sh
curl -L -o codex-deepseek-bridge-macos-x64 https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos-x64
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos-x64 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos-x64
./codex-deepseek-bridge-macos-x64 --version
```

Windows PowerShell:

```powershell
$ErrorActionPreference = "Stop"
$url = "https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-win-x64.exe"
$out = ".\codex-deepseek-bridge-win-x64.exe"
Remove-Item $out -ErrorAction SilentlyContinue
curl.exe -L --fail --progress-bar -o $out $url
if ($LASTEXITCODE -ne 0) { throw "Download failed." }
if ((Get-Item $out).Length -lt 10MB) { throw "Download looks incomplete. Run the commands again." }
& $out --version
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

不要把 key 作为命令行参数传入。bridge 会从交互输入、`--from-stdin` 或 `DEEPSEEK_API_KEY` 读取 key，并以仅当前用户可读写的权限保存在本机。

#### 3. 运行 setup

使用你下载的 binary 运行 `setup`：

macOS:

```sh
./codex-deepseek-bridge-macos setup
```

Windows PowerShell:

```powershell
.\codex-deepseek-bridge-win-x64.exe setup
```

setup 会完成以下操作：

- 备份现有 Codex `config.toml`；
- 写入一个受管理的 Codex provider 配置块，指向 `127.0.0.1`；
- 启动本地 bridge；
- 默认向 Codex 发布 `deepseek-pro`；
- 将 `deepseek-pro` 映射到 `deepseek-v4-pro`。

setup 完成后，重启 Codex。

#### 4. 在 Codex 中使用 DeepSeek

打开 Codex app，或者在项目目录中启动 Codex CLI：

```sh
cd /path/to/my-project
codex
```

此时 Codex 会把 Responses API 请求发给本地 bridge，再由 bridge 转换并发送到 `deepseek-v4-pro`。

![Codex composer running deepseek-pro](./assets/codex_deepseek_bridge_composer.png)

DeepSeek V4 的模型元数据会写入 Codex 本地模型目录：

| Codex 模型 | 上游 DeepSeek 模型 | 说明 |
|---|---|---|
| `deepseek-pro` | `deepseek-v4-pro` | 默认编程模型 |
| `deepseek-flash` | `deepseek-v4-flash` | 更快的模型，由 bridge 映射 |

模型目录声明 100 万 token 上下文窗口和 `384000` max output tokens。Codex 的 reasoning effort 会映射到 DeepSeek thinking：

| Codex reasoning | DeepSeek 行为 |
|---|---|
| `xhigh` / max | 最大 thinking |
| `high` | high thinking |
| `none` | 关闭 thinking |

#### 5. 保留 Codex 工具和插件

Codex 仍然负责 app、审批、工作区访问、插件、MCP servers 和工具执行。bridge 只转换模型协议。

它会处理 Codex Responses tool calls，包括 function tools、namespace tools，以及 `apply_patch` 这类 custom/freeform tools，然后把 DeepSeek 返回的 tool calls 转回 Codex 需要的格式。这样 Browser、Chrome、Computer Use、MCP、文档工作流，以及插件提供的搜索类工具，都可以继续留在 Codex 的正常工作流里，由 DeepSeek 负责模型调用。

由于 DeepSeek 公开 API 目前还没有提供兼容的多模态图片输入，image input 默认关闭。bridge 已经保留 vision 路径；当 DeepSeek 支持 image input 后，依赖图片输入的插件流程可以在不改变 Codex 侧工作流的情况下启用。

#### 6. 验证并查看本地报告

检查 bridge 健康状态：

```sh
./codex-deepseek-bridge-macos doctor
```

如果 bridge binary 已经在 `PATH` 中，也可以使用：

```sh
codex-deepseek-bridge doctor
```

打开本地报告：

```sh
codex-deepseek-bridge report
```

报告服务绑定在 `127.0.0.1`，只读，会显示请求、latency、token 使用量、DeepSeek cache hits 和近期调用。

![Codex DeepSeek Bridge report](./assets/codex_deepseek_bridge_report.png)

#### 可选：在 Codex Desktop 中显示两个模型标签

当前 Codex Desktop 版本可能会把本地 custom model 显示为 `Custom`，即使 bridge 已经正常工作。默认 setup 不需要修改 Codex Desktop。

如果你确实想在 Desktop 模型选择器里看到 `deepseek-pro` 和 `deepseek-flash` 的完整标签，请先阅读 bridge README，并且只在接受本地 app bundle 修改的情况下使用可选的 Desktop compatibility mode。

![Codex Desktop picker with DeepSeek models](./assets/codex_deepseek_bridge_picker.jpg)

#### 恢复

如需撤销 setup：

```sh
codex-deepseek-bridge restore
```

`restore` 会移除受管理的 Codex 配置块并停止 bridge。如果还想删除保存的 key、日志和本地状态：

```sh
codex-deepseek-bridge restore --purge
```
