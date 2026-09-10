[English](./claude_code.md) | [简体中文](./claude_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Claude Code

Claude Code 是一个运行在终端（或 VSCode Extension）内的 AI 编程助手。

### 从零安装 Claude Code

Claude Code 可以通过 CLI 或者 VSCode Extension 的方式运行，按照使用习惯任选即可。

#### 选项一：安装 Claude Code CLI

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 18+。
- Windows 用户需安装 [Git for Windows](https://git-scm.com/download/win)。
- 在命令行界面，执行以下命令安装 Claude Code：

```
npm install -g @anthropic-ai/claude-code
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```
claude --version
```

#### 选项二：安装 Claude Code VSCode Extension

- 安装 [VSCode](https://code.visualstudio.com/)
- 安装 [Claude Code VSCode Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)

安装完成后，搜索 VSCode 的设置项 `claudeCode.disableLoginPrompt` 并将其勾选。

### 配置 Claude Code

Claude Code 可以通过配置文件或环境变量的方法进行配置。在大多数情况下，优先选用配置文件的方法，配置文件中的配置可以被 Claude Code CLI 和 VSCode Extension 共同读取到。

#### 方法一：通过配置文件配置

配置文件位置：
- Linux / Mac 在 `~/.claude/settings.json` 中配置
- Windows 在 `C:\Users\<你的实际用户名>\.claude\settings.json` 中配置
- **以上文件若不存在，自行创建即可**

配置文件内容：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<你的 DeepSeek API Key>",
    "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash[1m]",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_EFFORT_LEVEL": "max"
  }
}
```

#### 方法二：配置环境变量

Linux / Mac 用户执行以下命令配置 [DeepSeek Anthropic API](https://api.deepseek.com/anthropic) 环境变量，其中 API Key 在 [DeepSeek Platform](https://platform.deepseek.com/api_keys) 获取：

```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<你的 DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash[1m]
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
export CLAUDE_CODE_EFFORT_LEVEL=max
```

Windows 用户执行：

```
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN="<你的 DeepSeek API Key>"
$env:ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash[1m]"
$env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"
$env:CLAUDE_CODE_EFFORT_LEVEL="max"
```

### 使用 Claude Code

#### 使用 Claude Code CLI

进入项目目录，执行 `claude` 命令，即可开始使用了。

```
cd /path/to/my-project
claude
```

<div align="center">
<img src="https://cdn.deepseek.com/api-docs/cc_example.png" width='1024' border='1'  />
</div>

#### 使用 Claude Code VSCode Extension

用 VSCode 打开项目目录，点击左侧边栏的 Claude Code 图标，并点击 `New session` 即可开始使用。

![在 VSCode Extension 中使用 Claude Code](./assets/claude_code_vsc_ext.png "在 VSCode Extension 中使用 Claude Code")
## DeepSeek + Claude Code 故障排查

### HTTP 400 错误

使用 DeepSeek Anthropic 兼容接口时，如果 Claude Code 返回 HTTP 400，不要第一时间判断为 API Key 或网络错误。先独立验证 DeepSeek 接口是否可用，再检查 Claude Code 调试输出中的实际模型名称和具体错误文本。

建议先检查：

```powershell
claude --version
$env:ANTHROPIC_BASE_URL
$env:ANTHROPIC_MODEL
```

不要在日志或 Issue 中打印真实的 `ANTHROPIC_AUTH_TOKEN`。

### `unrecognized_model` 或模型相关的 400

模型相关的 400 可能来自 Claude Code 版本与 DeepSeek Anthropic 兼容接口之间的兼容性差异。

本仓库已有一个可复现的版本相关案例：Claude Code v2.1.154 在同一配置下发送了 DeepSeek 不接受的 `system` role，而 v2.1.153 正常工作，详见 [Issue #167](https://github.com/deepseek-ai/awesome-deepseek-agent/issues/167)。

另一个独立测试环境中，Claude Code v2.1.266 使用 DeepSeek V4 Pro/Flash 时出现带有 `unrecognized_model` 的 400；在相同 DeepSeek 接口和凭据下，v2.1.153 后续验证正常，且 Pro/Flash 的工具调用也能工作。

由于兼容性可能与版本有关，建议按以下最小隔离流程排查：

1. 先在 Claude Code 之外验证 DeepSeek Anthropic 接口。
2. 用 `claude --version` 记录准确的 Claude Code 版本。
3. 使用 `--print` 或最短单句 Prompt 做最小请求。
4. 问题仍不明确时开启 `--debug`。
5. 检查实际模型名称和错误正文。
6. 在不删除当前版本的情况下，单独测试另一个 Claude Code 版本。
7. 至少分别验证普通 Prompt 和工具调用，再继续修改其他配置。

不要把某一个版本组合直接写成对所有用户都有效的通用修复。报告问题时，应提供准确的 Claude Code 版本、DeepSeek 模型、接口地址和错误文本，以便复现。

### Windows PowerShell：`.ps1` 执行策略错误

如果 PowerShell 阻止执行 `npm.ps1` 或 `claude.ps1`，优先使用 Windows 的 `.cmd` 包装器：

```powershell
npm.cmd -v
claude.cmd --version
```

这样通常无需为了运行工具而修改系统 ExecutionPolicy。

### Windows 原生 `claude.exe` 被替换问题

如果 Windows 安装后只剩下类似 `claude.exe.old.<timestamp>`，却没有新的 `claude.exe`，先检查安装状态，不要反复执行安装/升级命令。

在一次已验证的 v2.1.153 恢复案例中，原先已经验证过的 `.old` 二进制被恢复为 `claude.exe` 后，程序即可正常启动。

只有在确认 `.old` 文件就是当前安装中、此前已验证成功的同版本二进制后，才建议恢复名称；不要从无关安装目录复制二进制文件。

### 如何提交可复现的问题

提交 Issue 时建议包含：

- 操作系统
- Claude Code 版本
- DeepSeek 模型
- `ANTHROPIC_BASE_URL`
- 独立 API 最小请求是否成功
- HTTP 状态码和完整错误文本
- 普通 Prompt、工具调用是否受影响
- 脱敏后的关键 debug 日志

绝不要提交 API Key、Cookie、账号密码或其他秘密信息。
