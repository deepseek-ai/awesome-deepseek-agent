[English](./crush.md) | [简体中文](./crush.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Crush

Crush 是由 Charm 开发的华丽开源 AI 编程 Agent，运行在终端中。支持多模型切换、LSP 集成、MCP 服务器和代理式编码工作流。

#### 1. 安装 Crush

- 安装 [Node.js](https://nodejs.org/zh-cn/download/)。
- 在命令行界面，执行以下命令安装 Crush：

```bash
npm install -g @charmland/crush
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```bash
crush --version
```

> **注意：** macOS 用户也可以通过 Homebrew 安装：`brew install charmbracelet/tap/crush`。

#### 2. 配置 DeepSeek 供应商

Crush 支持通过 OpenAI 兼容 API 添加自定义供应商。在配置文件中添加 DeepSeek：

- **Linux / macOS**：`~/.config/crush/crush.json`
- **Windows**：`%USERPROFILE%\.config\crush\crush.json`

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "deepseek": {
      "type": "openai-compat",
      "base_url": "https://api.deepseek.com",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek-V4-Pro",
          "context_window": 1048576,
          "default_max_tokens": 32768,
          "can_reason": true
        },
        {
          "id": "deepseek-v4-flash",
          "name": "DeepSeek-V4-Flash",
          "context_window": 1048576,
          "default_max_tokens": 32768,
          "can_reason": true
        }
      ]
    }
  }
}
```

其中 API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

设置环境变量：

Linux / Mac 用户：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows 用户：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

#### 3. 运行并选择模型

- 进入项目目录并执行 `crush` 命令：

```bash
cd /path/to/my-project
crush
```

- 按 `Ctrl+L`（或输入 `/model`）打开模型切换器。
- 选择 **DeepSeek** 供应商，然后选择 `DeepSeek-V4-Pro` 或 `DeepSeek-V4-Flash`。
- 开始与你的终端编程新搭档一起编码 💘
