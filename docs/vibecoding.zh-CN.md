[English](./vibecoding.md) | [简体中文](./vibecoding.zh-CN.md) · [← Back](../README.md)

# 接入 VibeCoding

VibeCoding 是一个基于终端的 AI 编程助手，使用约 10,000 行 Go 代码编写，灵感来源于 [pi.dev](https://pi.dev)。它支持多提供商（默认 DeepSeek）、SSE 流式传输、三种运行模式、bubblewrap 沙箱、会话管理，以及带有 Markdown 渲染的丰富终端界面。

- **GitHub:** <https://github.com/startvibecoding/vibecoding>

#### 1. 安装 VibeCoding

**方式一：npm（推荐）**

```bash
npm install -g vibecoding-installer
```

**方式二：一键安装**

Linux / macOS：

```bash
curl -fsSL https://raw.githubusercontent.com/startvibecoding/vibecoding/main/install.sh | bash
```

Windows（PowerShell）：

```powershell
irm https://raw.githubusercontent.com/startvibecoding/vibecoding/main/install.ps1 | iex
```

**方式三：Go 安装**

```bash
go install github.com/startvibecoding/vibecoding/cmd/vibecoding@latest
```

**方式四：从源码构建**

```bash
git clone https://github.com/startvibecoding/vibecoding.git
cd vibecoding
make build
```

验证安装：

```bash
vibecoding --version
```

#### 2. 配置 DeepSeek

VibeCoding 内置 DeepSeek 作为**默认提供商**——无需手动配置 Provider。只需设置 API Key：

```bash
export DEEPSEEK_API_KEY=sk-...
```

> 从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**或**在 `settings.json` 中配置（`~/.vibecoding/settings.json` 为全局配置，`.vibe/settings.json` 为项目级覆盖）：

```json
{
  "defaultProvider": "deepseek-openai",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "high",
  "maxContextTokens": 1000000,
  "maxOutputTokens": 384000
}
```

> DeepSeek V4 模型支持高达 **100 万 token** 的上下文窗口。上述 `maxContextTokens` 和 `maxOutputTokens` 设置反映了这一点。

**主要配置项：**

| 选项 | 说明 |
|------|------|
| `defaultProvider` | `"deepseek-openai"`（OpenAI 兼容，默认）或 `"deepseek-anthropic"`（Anthropic 兼容） |
| `defaultModel` | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| `defaultThinkingLevel` | `off`、`minimal`、`low`、`medium`、`high`、`xhigh` |
| `maxContextTokens` | 上下文窗口大小（DeepSeek V4 为 1000000） |
| `maxOutputTokens` | 最大输出 token 数（384000） |

**完整配置示例**（含沙箱、审批和压缩设置）：

```json
{
  "defaultProvider": "deepseek-openai",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "high",
  "defaultMode": "agent",
  "maxContextTokens": 1000000,
  "maxOutputTokens": 384000,
  "compaction": {
    "enabled": true,
    "reserveTokens": 16384,
    "keepRecentTokens": 20000
  },
  "sandbox": {
    "enabled": true,
    "level": "standard",
    "allowNetwork": false
  },
  "retry": {
    "enabled": true,
    "maxRetries": 3,
    "baseDelayMs": 2000
  },
  "approval": {
    "bashWhitelist": ["go ", "make ", "git ", "npm "],
    "bashBlacklist": ["rm -rf", "sudo"]
  }
}
```

也可以通过环境变量覆盖设置：

| 变量 | 说明 |
|------|------|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 |
| `VIBECODING_DIR` | 覆盖配置目录 |
| `VIBECODING_PROVIDER` | 覆盖默认提供商 |
| `VIBECODING_MODEL` | 覆盖默认模型 |
| `VIBECODING_MODE` | 覆盖默认模式 |
| `VIBECODING_THINKING` | 覆盖默认思考级别 |

#### 3. 运行 VibeCoding

```bash
# 进入项目目录
cd /path/to/my-project

# 启动交互模式
vibecoding

# 指定模型和思考级别
vibecoding --provider deepseek-openai --model deepseek-v4-pro --thinking high

# 非交互模式（打印模式）
vibecoding -p "用 Go 写一个 hello world"

# 继续最近的会话
vibecoding -c
```

#### 三种运行模式

| 模式 | 说明 |
|------|------|
| **Plan** | 只读分析和规划。沙箱化，无文件写入。 |
| **Agent**（默认） | 受控的读写访问。Bash 需要审批（可配置白名单）。沙箱化，无网络。 |
| **YOLO** | 完全系统访问，无限制。 |

使用 `/mode [plan|agent|yolo]` 在交互模式下切换。

#### 交互命令

| 命令 | 说明 |
|------|------|
| `/mode [plan\|agent\|yolo]` | 切换模式 |
| `/model` | 显示当前模型 |
| `/think` | 循环切换思考级别 |
| `/skills` | 列出已加载技能 |
| `/clear` | 清除对话 |
| `/help` | 显示帮助 |

#### 沙箱（Linux）

VibeCoding 使用 [bubblewrap](https://github.com/containers/bubblewrap) 实现 Linux 沙箱化：

```bash
# 安装 bubblewrap
sudo apt install bubblewrap      # Debian/Ubuntu
sudo dnf install bubblewrap      # Fedora
sudo pacman -S bubblewrap        # Arch
```

通过 `--sandbox` 参数或在 settings.json 中启用沙箱。

完整配置参考请参阅 [VibeCoding 文档](https://github.com/startvibecoding/vibecoding/tree/main/docs)。
