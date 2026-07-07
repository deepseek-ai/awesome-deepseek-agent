[English](./waveloom.md) | [简体中文](./waveloom.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 Waveloom

Waveloom 是一个开源的 Go 终端 AI 编程 Agent，默认使用 DeepSeek V4 作为 LLM —— 无需额外配置供应商，设置 API Key 即可开始使用。基于 Think-Act-Observe 循环，内置 12 个工具，兼容 Claude Code Skill 格式（`.claude/skills/` 可直接迁移），完整支持 MCP 客户端，四级前缀稳定压缩引擎专为 DeepSeek 缓存设计。

- **GitHub:** <https://github.com/Menfre01/waveloom>

#### 1. 安装 Waveloom

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/Menfre01/waveloom/main/install.sh | sh

# 或 Homebrew
brew install Menfre01/tap/waveloom

# Windows（PowerShell — 需安装 Git for Windows）
powershell -c "irm https://raw.githubusercontent.com/Menfre01/waveloom/main/install.ps1 | iex"
```

验证：

```bash
waveloom --version
```

> 查看[完整安装指南](https://github.com/Menfre01/waveloom#readme)了解源码编译、手动下载等方式。

#### 2. 配置 DeepSeek

在项目目录（推荐）或 `~/.waveloom/` 下创建 `settings.json`：

```json
{
    "llm": {
        "api_key": "<你的 DeepSeek API Key>",
        "provider": "deepseek",
        "model": "deepseek-v4-pro",
        "base_url": "https://api.deepseek.com",
        "timeout": "600s",
        "extra_params": {
            "thinking": {"type": "enabled"},
            "reasoning_effort": "max"
        }
    }
}
```

关键字段：

| 字段 | 默认值 | 说明 |
|------|--------|------|
| `api_key` | — | 你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| `model` | `deepseek-v4-pro` | 也支持 `deepseek-v4-flash` 用于更快、更轻量的任务 |
| `extra_params.thinking` | `{"type": "enabled"}` | 启用思维链推理 |
| `extra_params.reasoning_effort` | `"max"` | 最佳编码效果；也支持 `"high"` |

也可以通过 `LLM_API_KEY` 环境变量设置 Key，适合 CI/CD 场景。

> **上下文窗口：** Waveloom 默认适配 DeepSeek 100 万 token 上下文。前缀稳定压缩系统确保最长公共前缀在多轮对话中持续命中缓存，同时拥有长上下文和低延迟。

#### 3. 首次运行

```bash
cd /path/to/my-project
waveloom
```

首次使用时可通过交互式向导完成配置：

```bash
waveloom setup
```

向导会引导你设置 API Key、选择模型并配置思考模式。

启动后用自然语言输入指令 —— 让 Waveloom 写代码、修 Bug、解释逻辑或探索代码库。Waveloom 会在 Think-Act-Observe 循环中持续运行，直到任务完成。

```text
给 UserSignup 函数增加输入校验
为什么邮箱为空时登录接口返回 500？
将支付模块重构成策略模式
```

#### 快捷键

| 按键 | 功能 |
|------|------|
| `Enter` | 发送消息 |
| `Shift+Enter` | 插入换行 |
| `Shift+Tab` | 进入 / 退出 Plan Mode |
| `Esc` | 中断当前轮次 |
| `/` | 打开指令菜单 |
| `@` | 模糊文件选择器 |
| `Tab` | 切换交互区域 |
| `Ctrl+C`（两次） | 退出 |

#### 为什么选择 Waveloom

- **Claude Code Skill 兼容** — `.claude/skills/` 目录可直接使用，无需修改。支持全部 9 个 SKILL.md frontmatter 字段、`$ARGUMENTS` 变量替换和 `` !`cmd` `` 注入。
- **完整 MCP 客户端** — 连接外部 MCP Server，与 12 个内置工具并列显示。兼容 Claude Code 的 `.claude.json` MCP 配置格式。
- **Plan Mode 先规划后执行** — 探索设计先行，审批通过后再实施。`Shift+Tab` 切换；规划期间 Guard 强制写保护。
- **前缀缓存优化压缩** — 固定系统提示词、仅追加消息历史、四级水位线压缩（Snip → Prune → Summarize），最长公共前缀跨轮次持续命中缓存。
- **权限安全引擎** — 三级决策（允许 / 拒绝 / 询问）加模式匹配规则。每次写操作需你确认。
- **会话持久化** — 关闭终端数天后 `waveloom --continue` 即可恢复，所有上下文完整保留。
- **模型随时切换** — TUI 内 `/model deepseek-v4-flash`，或 `waveloom --model deepseek-v4-flash`。
