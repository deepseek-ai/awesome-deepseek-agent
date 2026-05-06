[English](./anda_bot.md) | [简体中文](./anda_bot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Anda Bot

Anda Bot 是一个 Rust 编写的开源智能体，运行在终端内，也可以接入微信、飞书/Lark、Telegram、Discord、IRC 等 IM 平台。它的核心是基于 Anda Hippocampus 的知识图谱长期记忆系统：能从经验中自主学习精华，在跨会话中召回关系与时间线，执行长程推理任务，擅长使用 Claude Code、Codex 等外部工具，并通过强大的 Subagents 系统协同完成复杂工作。

#### 1. 安装 Anda Bot

通过 Homebrew 安装最新发布版：

```bash
brew install ldclabs/tap/anda
```

或通过一行安装脚本安装：

```bash
curl -fsSL https://raw.githubusercontent.com/ldclabs/anda-bot/main/scripts/install.sh | sh
```

Windows PowerShell：

```powershell
irm https://raw.githubusercontent.com/ldclabs/anda-bot/main/scripts/install.ps1 | iex
```

也可以使用较新的 Rust 工具链从源码运行：

```bash
git clone https://github.com/ldclabs/anda-bot.git
cd anda-bot
cargo run -p anda_bot --
```

#### 2. 配置 DeepSeek

先启动一次 Anda Bot，生成默认配置文件：

```bash
anda
```

编辑 `~/.anda/config.yaml`，将 DeepSeek 配置为当前模型提供方：

```yaml
model:
  active: "deepseek-v4-pro"
  providers:
    - family: anthropic
      model: "deepseek-v4-pro"
      api_base: "https://api.deepseek.com/anthropic"
      api_key: "YOUR_API_KEY" # 设置 DEEPSEEK_API_KEY 时可留空
      labels: ["pro", "hippocampus"]
      disabled: false
```

你也可以在启动 Anda Bot 前导出 API Key：

```bash
export DEEPSEEK_API_KEY="YOUR_API_KEY"
```

`hippocampus` 标签表示这一路模型可优先用于长期记忆的生成与召回支持。

#### 3. 开始使用

运行终端 UI：

```bash
anda
```

修改 `config.yaml` 后，可以在终端 UI 中输入 `/reload` 重新加载模型配置，或者运行 `anda restart` 重启智能体。

如需接入聊天平台，可在 `~/.anda/config.yaml` 中配置 `channels`。当前支持 IRC、Telegram、WeChat、Discord、Lark/飞书 等渠道。
