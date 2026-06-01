[English](./illusion_code.md) | [简体中文](./illusion_code.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 IllusionCode

IllusionCode 是一款开源的终端 AI 编程助手，继承了 Claude Code 的提示词体系与工具架构，以 Python 重新实现，支持多提供商接入、MCP 动态扩展、中英双语界面以及优化的终端渲染。

- **GitHub：** <https://github.com/YunTaiHua/illusion-code>

#### 1. 安装 IllusionCode

- 安装 [Python](https://www.python.org/downloads/) 3.10+ 版本。
- 安装 [Node.js](https://nodejs.org/en/download/) 18+ 版本（用于 TUI 前端）。

**方式 A：通过 PyPI 安装（推荐）**

```sh
pip install illusion-code
```

验证安装是否成功：

```sh
illusion --version
```

**方式 B：从源码安装**

```sh
git clone https://github.com/YunTaiHua/illusion-code.git
cd illusion-code
uv sync
```

> **提示：** 也可以通过 `pip install .` 从源码安装（自动构建前端），或使用 `pip install -e .` 进行可编辑模式安装。

#### 2. 配置 IllusionCode

**方式 A：交互式登录（推荐）**

```sh
illusion auth login
```

选择**自定义提供商** → 设置 `api_format: openai` → 设置 `base_url: https://api.deepseek.com/v1` → 输入你的 API Key。

**方式 B：直接编辑配置文件**

创建或编辑 `~/.illusion/settings.json`：

```json
{
  "model": "env_1.model_1",
  "env_1": {
    "api_format": "openai",
    "base_url": "https://api.deepseek.com/v1",
    "api_key": "sk-...",
    "model_1": "deepseek-v4-pro",
    "model_2": "deepseek-v4-flash"
  }
}
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

**配置选项：**

| 选项 | 说明 |
|------|------|
| `model` | 当前使用的模型引用，格式为 `env_N.model_N`（如 `env_1.model_2` 表示 Flash） |
| `api_format` | API 格式 — DeepSeek 使用 `"openai"` |
| `base_url` | API 地址 — `https://api.deepseek.com/v1` |
| `api_key` | 你的 DeepSeek API Key |
| `model_1` / `model_2` | 模型名称，如 `deepseek-v4-pro` 或 `deepseek-v4-flash` |

#### 3. 启动 IllusionCode

```sh
cd /path/to/my-project
illusion
```

**命令行选项：**

| 参数 | 说明 |
|------|------|
| `-m env_1.model_2` | 启动时切换模型 |
| `-p "提示词"` | 非交互模式 — 执行单条提示 |
| `--continue` | 继续上一次对话 |
| `--resume <session-id>` | 恢复指定会话 |
| `--permission-mode` | 设置权限模式（`default` / `plan` / `full_auto`） |
| `--api-format openai` | 覆盖 API 格式 |
| `illusion web` | 启动 Web UI（默认端口 3000） |
| `illusion web --port 8080` | 在自定义端口启动 Web UI |

#### 推理强度

IllusionCode 支持通过 `~/.illusion/settings.json` 中的 `effort_level` 设置推理强度：

```json
{
  "effort_level": "max"
}
```

可用级别：`low`、`medium`、`high`、`xhigh`、`max`。使用 `max` 可获得 DeepSeek-V4-Pro 的最佳编程体验。

#### 快捷键

| 按键 | 功能 |
|------|------|
| `Enter` | 发送消息 |
| `Shift+Enter` | 换行 |
| `ctrl+x` | 中断当前模型回复 |
| `/` | 打开斜杠命令菜单 |
| `/new` | 开始新的对话 |
| `/resume` | 选择之前的对话继续 |
| `/model` | 交互式切换模型 |
| `/memory` | 查看和管理持久化记忆 |
| `/config` | 查看和编辑配置 |
| `/skills` | 列出和管理技能 |
| `/hooks` | 管理 Hook 配置 |
| `/mcp` | 管理 MCP 服务器连接 |
| `/exit` | 退出 IllusionCode |

#### 特性

- **34+ 个内置工具** — 文件操作、Shell 执行、搜索、任务管理、Agent 协作等
- **47 个斜杠命令** 和 **7 个内置 Agent**（general-purpose、Explore、Plan、verification、worker、statusline-setup、illusion-guide）
- **双 UI 模式：** 终端 TUI（React + Ink）和 Web UI（React + Vite + Tailwind）
- **权限模式：** `default` / `plan` / `full_auto`，支持按工具和按路径的细粒度规则
- **多提供商支持：** Anthropic Claude、OpenAI 兼容端点、GitHub Copilot OAuth、OpenAI Codex，以及 20+ 自动识别的提供商（OpenRouter、DashScope、Groq、Ollama、vLLM 等）
- **多环境配置：** 通过 `env_N` 分组在不同提供商间切换，无需重新配置
- **MCP 扩展：** 从 MCP 服务器动态注册工具，支持项目级和全局配置
- **插件与技能系统：** 可安装的插件和可加载的技能，用于扩展功能
- **Hook 系统：** 事件驱动的钩子（工具使用前/后、用户提示提交），支持命令、提示、HTTP 和 Agent 钩子类型
- **记忆系统：** 跨会话的持久化项目知识
- **Cron 调度器：** 定时任务，支持任务管理、执行历史和守护进程模式
- **LSP 集成：** 语言服务器协议支持，提供代码智能提示
- **沙箱支持：** 可配置的网络和文件系统限制
- **中英双语界面：** 由 `~/.illusion/settings.json` 中的 `ui_language` 字段控制
- **100 万 token 上下文：** DeepSeek V4 模型支持最高 100 万 token 上下文
- **自动更新：** `illusion update` 从 PyPI 检查并安装新版本

更多配置选项请参阅 [IllusionCode 文档](https://github.com/YunTaiHua/illusion-code/blob/main/README.md)。
