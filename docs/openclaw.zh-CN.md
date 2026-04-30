[English](./openclaw.md) | [简体中文](./openclaw.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenClaw

OpenClaw 是一个开源的个人 AI 助手，可以接入飞书、微信等常用聊天工具，可以通过 Skill 扩展能力。

#### 1. 安装 OpenClaw

Linux / Mac 用户执行以下命令，从 [OpenClaw 安装脚本](https://openclaw.ai/install.ps1) 安装：

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

Windows 用户执行以下命令，从 [OpenClaw 安装脚本](https://openclaw.ai/install.ps1) 安装：

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

#### 2. 配置 OpenClaw 中的默认模型

首次安装完成后，会自动进入 setup（配置）阶段；已经安装过 OpenClaw 的用户可以通过 `openclaw onboard --install-daemon` 命令进入配置阶段。

- 遇到提示：`I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?` 请选择 **Yes**。
- 遇到提示：`Setup mode` 推荐选择 **QuickStart**。
- 遇到提示：`Model/auth provider` 请选择 **DeepSeek**。
- 遇到提示：`Enter DeepSeek API key` 请填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- 遇到提示：`Default model` 请将光标指向 **Enter model**，填写模型名称（`deepseek-v4-pro` 或 `deepseek-v4-flash`）。
- 后续的其余配置（消息频道、Skill 等）请根据需求配置，新手可以先选择 **Skip for now**。

为避免兼容性问题，强烈建议将 OpenClaw 升级到最新版本，确保版本号 >= [v2026.4.24](https://github.com/openclaw/openclaw/releases/tag/v2026.4.24)，该版本新增了对 DeepSeek V4 Thinking Mode 的正确支持。如果遇到关于 `reasoning_content` 的 400 报错，更新到最新版本即可解决。

#### 3. 开始使用

打开 Web UI，在 Chat 页面进行交互：

```
openclaw dashboard
```

在终端中打开 TUI：

```
openclaw tui
```

在终端中与 Openclaw 对话：

```
openclaw terminal
```
