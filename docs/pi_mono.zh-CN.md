[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Pi

Pi（pi-mono）是一个极简且高度可扩展的终端编码框架。它通过 TypeScript 扩展、技能、提示模板和主题来适配你的工作流，支持树状会话结构和 15+ 内置供应商。

#### 1. 安装 Pi

- 安装 [Node.js](https://nodejs.org/zh-cn/download/)。
- 在命令行界面，执行以下命令安装 Pi：

```bash
npm install -g @mariozechner/pi-coding-agent
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```bash
pi --version
```

> **注意：** Linux / macOS 用户也可以通过官方脚本安装：
> ```bash
> curl -fsSL https://pi.dev/install.sh | sh
> ```

#### 2. 配置 DeepSeek 供应商

Pi 通过 `models.json` 支持自定义供应商。将 DeepSeek 添加为 OpenAI 兼容供应商：

- **Linux / macOS**：`~/.pi/agent/models.json`
- **Windows**：`%USERPROFILE%\.pi\agent\models.json`

```json
{
  "providers": {
    "deepseek": {
      "baseUrl": "https://api.deepseek.com/v1",
      "api": "openai-completions",
      "apiKey": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek-V4-Pro",
          "contextWindow": 1048576,
          "maxTokens": 32768,
          "input": ["text"],
          "reasoning": true,
          "compat": {
            "thinkingFormat": "deepseek"
          }
        },
        {
          "id": "deepseek-v4-flash",
          "name": "DeepSeek-V4-Flash",
          "contextWindow": 1048576,
          "maxTokens": 32768,
          "input": ["text"],
          "reasoning": true,
          "compat": {
            "thinkingFormat": "deepseek"
          }
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

> **提示：** `apiKey` 字段也支持通过 shell 命令动态获取，便于安全密钥管理。如果你使用密码管理器，可以将 `"$DEEPSEEK_API_KEY"` 替换为类似 `"!pass show api/deepseek"` 的命令。

#### 3. 运行并选择模型

- 进入项目目录并执行 `pi` 命令：

```bash
cd /path/to/my-project
pi
```

- 输入 `/model` 打开模型切换器。
- 选择 **deepseek**，然后选择 `DeepSeek-V4-Pro` 或 `DeepSeek-V4-Flash`。
- 开始使用你的极简终端编码框架。

更多配置选项请参阅 [Pi 模型文档](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/docs/models.md)。
