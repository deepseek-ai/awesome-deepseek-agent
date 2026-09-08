[English](./yomi.md) | [简体中文](./yomi.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Yomi

[Yomi](https://github.com/Crescent617/yomi) 是一个用 Rust 编写的极简开源 AI 编程助手，提供终端 TUI 与可选的桌面 GUI，可作为 daemon 接入飞书、Telegram 等聊天平台，并可通过 Skill 与 stdio 扩展能力。

#### 1. 安装 Yomi

macOS / Linux 用户可通过 [Homebrew](https://brew.sh) 安装：

```bash
# 命令行（TUI + 无头运行）
brew update && brew install crescent617/tap/yomi

# 可选：桌面 GUI
brew install crescent617/tap/yomi-app
```

也可以从 [Releases 页面](https://github.com/Crescent617/yomi/releases) 下载预编译二进制，或使用 Rust 1.90+ 从源码构建。

> DeepSeek V4 Thinking Mode 需要 yomi **v0.10.0 及以上版本**，该版本起正确处理 `reasoning_content`。可用 `yomi version` 查看版本，用 `brew upgrade crescent617/tap/yomi` 升级。

#### 2. 在 Yomi 中配置 DeepSeek

Yomi 读取 `~/.yomi/config.toml`。先在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后写入：

```toml
#:schema https://raw.githubusercontent.com/Crescent617/yomi/main/docs/config-schema.json

[[models]]
name = "deepseek"
provider = "openai"              # DeepSeek API 兼容 OpenAI 协议
model_id = "deepseek-v4-pro"     # 或 "deepseek-v4-flash"
endpoint = "https://api.deepseek.com/v1"
api_key = "sk-..."               # 你的 DeepSeek API Key
context_window = 1_000_000       # DeepSeek V4 支持最高 100 万 token 上下文
max_tokens = 384_000

[models.thinking]                # Thinking Mode
enabled = true
effort = "max"                   # deepseek-v4-pro 支持 "max" 与 "high"，yomi 将其作为 reasoning_effort 透传

[agent]
default_model = "deepseek"
```

- 如需更轻量、更快的方案，可将 `model_id` 改为 `deepseek-v4-flash`。各模型可用的思考强度见 [Thinking Mode 文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。
- 也可以用环境变量代替配置文件：`OPENAI_API_KEY`、`OPENAI_API_BASE=https://api.deepseek.com/v1`、`OPENAI_API_MODEL=deepseek-v4-pro`、`YOMI_THINKING=true`、`YOMI_THINKING_EFFORT=max`、`YOMI_CONTEXT_WINDOW=1M`。

#### 3. 首次运行

```bash
# 在项目目录中打开交互式 TUI
yomi

# 无头模式执行单条指令
yomi run "用三句话总结这个仓库"
```

桌面应用（Yomi.app）同样读取 `~/.yomi/config.toml`。

随便提问——如果回答以流式返回并带有思考过程，说明 DeepSeek V4 已配置成功。`yomi doctor` 可体检 daemon、频道与配置，`yomi usage` 可查看 token 用量。
