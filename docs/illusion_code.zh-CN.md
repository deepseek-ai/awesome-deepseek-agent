[English](./illusion_code.md) | [简体中文](./illusion_code.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 IllusionCode

IllusionCode 是一款开源的终端 AI 编程助手，继承了 Claude Code 的提示词体系与工具架构，以 Python 重新实现，支持多提供商接入、MCP 动态扩展、中英双语界面以及优化的终端渲染。

- **GitHub：** <https://github.com/YunTaiHua/illusion-code>

#### 1. 安装 IllusionCode

- 安装 [Python](https://www.python.org/downloads/) 3.10+ 版本。
- 安装 [Node.js](https://nodejs.org/en/download/) 18+ 版本（用于 TUI 前端）。
- 克隆并设置项目：

```sh
git clone https://github.com/YunTaiHua/illusion-code.git
cd illusion-code
uv sync
```

- 验证安装是否成功：

```sh
uv run illusion --version
```

> **提示：** 也可以通过 `pip install -e .` 全局安装，然后直接运行 `illusion`。

#### 2. 配置 IllusionCode

**方式 A：交互式登录（推荐）**

首次登录使用 uv run ，后续可直接使用 illusion。

```sh
uv run illusion auth login
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
uv run illusion
```

**命令行选项：**

| 参数 | 说明 |
|------|------|
| `-m env_1.model_2` | 启动时切换模型 |
| `-p "提示词"` | 非交互模式 — 执行单条提示 |
| `--continue` | 继续上一次对话 |
| `--api-format openai` | 覆盖 API 格式 |

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
| `/exit` | 退出 IllusionCode |

#### 特性

- **36 个内置工具** + MCP 动态工具扩展
- **52 个斜杠命令** 和 **7 个内置 Agent**
- **权限模式：** `default` / `plan` / `full_auto`
- **中英双语界面：** 由 `~/.illusion/settings.json` 中的 `ui_language` 字段控制
- **100 万 token 上下文：** DeepSeek V4 模型支持最高 100 万 token 上下文

更多配置选项请参阅 [illusion code 文档](https://github.com/YunTaiHua/illusion-code/blob/main/README.md)。
