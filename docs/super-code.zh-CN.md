[English](./super-code.md) | [简体中文](./super-code.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 Super Code

Super Code 是一款基于 Python 的终端 AI 编程助手，支持多 Agent 编排、跨会话持久化记忆、Snippet 编辑安全机制，以及通过 OpenAI 兼容协议接入多种模型。

- **GitHub：** <https://github.com/weiqiang136/super-code>

#### 1. 安装 Super Code

**从源码运行（全平台）**

- 安装 [Python](https://www.python.org/downloads/) 3.11+ 版本。
- 克隆仓库并安装依赖：

```sh
git clone https://github.com/weiqiang136/super-code.git
cd super-code
pip install -r requirements.txt
```

**便携可执行文件（Windows）**

从 [Releases 页面](https://github.com/weiqiang136/super-code/releases) 下载 `super-code.exe`，放到 `PATH` 中的某个目录即可。

#### 2. 配置 Super Code

创建 `~/.config/super-code/super-code.json`（全局）或 `./.super-code.json`（项目级），填入你的 DeepSeek API Key：

```json
{
  "provider": "openai",
  "model": "deepseek-v4-pro",
  "api_key": "sk-...",
  "base_url": "https://api.deepseek.com",
  "max_tokens": 131072,
  "timeout": 300,
  "model_profiles": {
    "deepseek": {
      "extra_body": {
        "reasoning_effort": "max"
      }
    }
  }
}
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

> **注意：** DeepSeek V4 模型支持最高 **100 万 token** 的上下文窗口。Super Code 使用 OpenAI 兼容协议，`base_url` 指向 DeepSeek 的 API 地址。如需使用快速模型，将 `model` 设为 `"deepseek-v4-flash"`。

**配置选项：**

| 选项 | 说明 |
|------|------|
| `provider` | 固定为 `"openai"`（DeepSeek 使用 OpenAI 兼容协议） |
| `model` | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| `api_key` | DeepSeek API Key |
| `base_url` | `https://api.deepseek.com` |
| `max_tokens` | 最大输出 token 数（默认 131072） |
| `timeout` | HTTP 超时时间（秒），默认 300，思考模型建议 ≥ 300 |
| `model_profiles` | 按模型的额外请求体参数。DeepSeek 可通过 `extra_body` 设置 `reasoning_effort` 为 `"max"` 或 `"high"` |
| `coordinator` | 启用多 Agent 协调模式（默认 `false`） |

**便携分发：** 将 `super-code.json` 放在 `super-code.exe` 同级目录即可实现零配置部署，程序会自动检测。

#### 3. 启动 Super Code

```sh
cd /path/to/my-project
python -m src.tui.app
# 或：super-code（使用便携可执行文件时）
```

#### 快捷键

| 按键 | 功能 |
|------|------|
| `Enter` | 发送消息 |
| `Shift+Tab` | 切换 Plan 模式（仅允许只读工具） |
| `Esc` | 中断当前模型回复 |
| `/help` | 查看可用的斜杠命令 |
| `/resume` | 继续之前的会话 |
| `/clear` | 开始新的对话 |
| `/rename <标题>` | 重命名当前会话 |
| `/memory` | 查看记忆索引 |
| `/dream` | 整合会话记忆 |

#### 使用 Agent Skills

Super Code 从以下位置自动发现 Skills：

- **用户级别：** `~/.config/super-code/skills/<name>/SKILL.md`
- **项目级别：** `./.super-code/skills/<name>/SKILL.md`

输入 `/<skill-name>` 直接调用技能，或使用 `Skill` 工具。

#### 多 Agent 协调模式

在配置中将 `coordinator` 设为 `true` 即可启用并行 Agent 编排。协调者可通过 `Agent` 工具创建 Worker、`SendMessage` 发送跟进指令、`TaskStop` 停止 Worker。每个 Worker 在独立的 Engine 中运行，自动批准只读工具调用。
