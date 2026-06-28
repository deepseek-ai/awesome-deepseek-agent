[English](./codex_deepseek_bridge.md) | [简体中文](./codex_deepseek_bridge.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 让 Codex App 使用 DeepSeek

[Codex DeepSeek Bridge](https://github.com/JetXu-LLM/codex-deepseek-bridge) 可以让官方 OpenAI Codex app 通过一条本地 setup 命令使用 DeepSeek。你继续使用 Codex Desktop、approvals、plugins、MCP servers 和工具工作流；模型调用交给 DeepSeek。

- **一条命令完成设置。** 下载后直接运行，不需要 build，bridge binary 不需要 Node.js 运行环境。
- **不需要 ChatGPT 订阅。** 使用你自己的 DeepSeek API key。
- **Key 留在本机。** 不作为命令行参数传入，不打印，不写日志。
- **Codex 还是你的 Codex。** 插件和工具继续留在 Codex 里，DeepSeek 负责模型调用。
- **一条命令恢复。** `restore` 会移除受管理的 Codex 配置块。

![Codex composer running deepseek-pro](./assets/codex_deepseek_bridge_composer.png)

#### 1. 快速开始

你需要一个来自 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 的 API key，以及 macOS 或 Windows 上的 Codex app。复制对应平台的命令并运行，按提示粘贴 DeepSeek API key，然后重启 Codex。

macOS Apple Silicon:

```sh
curl -L -o codex-deepseek-bridge-macos https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos
./codex-deepseek-bridge-macos setup
```

macOS Intel:

```sh
curl -L -o codex-deepseek-bridge-macos-x64 https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos-x64
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos-x64 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos-x64
./codex-deepseek-bridge-macos-x64 setup
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
& $out setup
```

setup 完成后，重启 Codex。默认会使用 `deepseek-pro`。

#### 2. setup 做了什么

`setup` 会在 Codex 的 `config.toml` 里写入一个可恢复的配置块，把 Codex 指向 `127.0.0.1` 上的本地 bridge，启动 bridge，并把 Codex 默认的 `deepseek-pro` 映射到 `deepseek-v4-pro`。

它也会备份你已有的 Codex 配置。DeepSeek key 从终端提示、`--from-stdin` 或 `DEEPSEEK_API_KEY` 读取，并以仅当前用户可读写的权限保存在本机。

#### 3. 模型和 reasoning

bridge 使用稳定的 Codex 侧模型名，并映射到当前 DeepSeek V4 模型：

| Codex 模型 | DeepSeek 模型 | 说明 |
|---|---|---|
| `deepseek-pro` | `deepseek-v4-pro` | 默认编程模型 |
| `deepseek-flash` | `deepseek-v4-flash` | 更快的模型，由 bridge 映射 |

本地模型元数据声明 100 万 token 上下文窗口和 `384000` max output tokens。Codex reasoning effort 会映射到 DeepSeek thinking：

| Codex reasoning | DeepSeek 行为 |
|---|---|
| `xhigh` / max | 最大 thinking |
| `high` | high thinking |
| `none` | 关闭 thinking |

#### 4. 保留 Codex 工具和插件

Codex 仍然负责 app、审批、工作区访问、插件、MCP servers 和工具执行。bridge 只转换模型协议。

它会处理 Codex Responses tool calls，包括 function tools、namespace tools，以及 `apply_patch` 这类 custom/freeform tools，然后把 DeepSeek 返回的 tool calls 转回 Codex 需要的格式。当你的 Codex 环境里有 Browser、Chrome、Computer Use、MCP、文档工作流或插件提供的搜索类工具时，它们都可以继续留在正常 Codex 工作流里。

由于 DeepSeek 公开 API 目前还没有提供兼容的多模态图片输入，image input 默认关闭。bridge 已经保留 vision 路径；未来 DeepSeek 支持 image input 后，可以沿用同一套 Codex 侧工作流。

#### 5. 查看每次调用

每次请求都会经过 bridge。本地 report 可以看到 latency、token 使用量、DeepSeek cache hits 和近期调用：

```sh
codex-deepseek-bridge report
```

如果你使用的是下载的 binary，并且它不在 `PATH` 中，就用和 setup 相同的方式调用，例如 `./codex-deepseek-bridge-macos report`。

![Codex DeepSeek Bridge report](./assets/codex_deepseek_bridge_report.png)

#### 6. 恢复

移除受管理的 Codex 配置块并停止 bridge：

```sh
codex-deepseek-bridge restore
```

如果还想删除保存的 key、日志和本地状态：

```sh
codex-deepseek-bridge restore --purge
```

#### 可选：Codex Desktop 中的模型标签

当前 Codex Desktop 版本可能会把本地 custom model 显示为 `Custom`，即使 bridge 已经正常工作。默认 setup 不需要修改 Codex Desktop；如果你确实想在模型选择器里看到两个模型的完整标签，bridge README 里有一个可选的 Desktop compatibility mode。

![Codex Desktop picker with DeepSeek models](./assets/codex_deepseek_bridge_picker.jpg)
