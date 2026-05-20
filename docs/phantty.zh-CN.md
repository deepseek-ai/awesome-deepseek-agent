[English](./phantty.md) | [简体中文](./phantty.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Phantty

Phantty 是一款用 Zig 编写的 Windows 终端模拟器，基于 Ghostty 的 VT 解析器，并内置 DeepSeek 优先的 AI Agent 会话。它可以在终端工作流中运行本地 PowerShell/cmd 命令，配合 WSL 和 SSH 终端，加载本地 Skills，并把 Agent 留在终端环境里使用。

- **GitHub：** <https://github.com/xuzhougeng/phantty>

#### 1. 安装 Phantty

Phantty 仅支持 Windows。请从发布页下载便携版：

```text
https://github.com/xuzhougeng/phantty/releases
```

选择一个 Windows portable zip：

| 文件 | 适用场景 |
|---|---|
| `phantty-windows-portable-webview2-vX.Y.Z.zip` | 推荐选择，适合需要内嵌浏览器面板的用户。 |
| `phantty-windows-portable-no-webview-vX.Y.Z.zip` | 适合没有 WebView2 或希望禁用内嵌浏览器的环境。 |
| `phantty-windows-portable-vX.Y.Z.zip` | 通用便携版。 |

解压后运行：

```powershell
.\phantty.exe
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建并复制 API Key。

Phantty 可以把 API Key 保存在 AI Profile 中；如果 Profile 的 Base URL 指向 DeepSeek，也可以从 `DEEPSEEK_API_KEY` 环境变量读取：

```powershell
$env:DEEPSEEK_API_KEY = "sk-your-deepseek-api-key"

# 可选：持久保存到后续 PowerShell 会话
[Environment]::SetEnvironmentVariable("DEEPSEEK_API_KEY", "sk-your-deepseek-api-key", "User")
```

#### 3. 打开并配置 AI Agent

启动 Phantty 后，按 `Ctrl+Shift+T`，选择 `AI Agent`。

如果还没有 AI Profile，Phantty 会先打开 AI 设置表单。填写：

| 字段 | 值 |
|---|---|
| Profile name | `DeepSeek` |
| Base URL | `https://api.deepseek.com` |
| API key | 你的 DeepSeek API Key；如果已经设置 `DEEPSEEK_API_KEY`，可以留空 |
| Model | `deepseek-v4-pro` |
| Thinking | `enabled` |
| Effort | `max` |
| Stream | `false` |
| Agent | `true` |

也可以使用 `deepseek-v4-flash` 创建更快、更轻量的 Agent Profile。

DeepSeek V4 模型支持最高 100 万 token 上下文。Phantty 不需要额外配置 `context_window`；它会直接向 DeepSeek 发送 OpenAI 兼容的 Chat Completions 请求，并使用所选 DeepSeek V4 模型的上下文能力。

#### 4. 首次运行

保存 Profile 后，Phantty 会打开一个 Agent 标签页。可以尝试：

```text
Inspect this repository and summarize the build and test commands.
```

当 Agent 请求运行工具命令时，如果权限模式不是 full，Phantty 会显示确认提示。这样本地 PowerShell/cmd、WSL 和 SSH 相关工具执行都需要显式确认。

#### 常用快捷键

| 快捷键 | 功能 |
|---|---|
| `Ctrl+Shift+T` | 打开会话启动器 |
| `Ctrl+Shift+P` | 打开命令中心 |
| `Ctrl+Shift+Alt+E` | 切换左侧文件浏览器 / Agent History 面板 |
| `Esc` | 关闭浮层或中断相关 UI 流程 |

#### Agent Skills 与本地命令

Phantty 会从以下位置发现本地 Skills：

- `%APPDATA%\phantty\skills\<skill-name>\SKILL.md`
- 当前工作目录下的 `.\skills\<skill-name>\SKILL.md`
- `phantty.exe` 同级目录下的 `skills\<skill-name>\SKILL.md`

使用 `$skill-name your request` 可以为下一次 Agent 请求加载指定 Skill。

AI Agent 标签页内置本地 slash commands：

| 命令 | 功能 |
|---|---|
| `/skills` | 列出发现的本地 Skills |
| `/commands` | 列出本地 AI Chat 命令 |
| `/reload-skills` | 为后续 Skill 调用重新从磁盘读取 Skills |

#### 故障排查

- `Missing API key`：设置 `DEEPSEEK_API_KEY`，或把 API Key 保存到 AI Profile。
- `401` 或认证错误：检查 API Key 和 Base URL。
- `402` 或余额错误：检查 DeepSeek 开放平台余额。
- 工具无法执行：保持 `Agent = true`，并在权限模式为 `confirm` 时确认工具请求。
- 不要使用旧的 DeepSeek V3 模型名；请使用 `deepseek-v4-pro` 或 `deepseek-v4-flash`。

#### 相关资源

- [Phantty](https://github.com/xuzhougeng/phantty)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
- [DeepSeek 深度思考模式](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)
