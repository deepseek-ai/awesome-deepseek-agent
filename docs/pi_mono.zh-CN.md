[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Pi

Pi（pi-mono）是一个极简且高度可扩展的终端编码框架。它通过 TypeScript 扩展、技能、提示模板和主题来适配你的工作流，支持树状会话结构和 15+ 内置供应商。

#### 1. 安装 Pi

- 安装 [Node.js](https://nodejs.org/zh-cn/download/)。
- 在命令行界面，执行以下命令安装 Pi：

```bash
npm install -g @earendil-works/pi-coding-agent
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
      "baseUrl": "https://api.deepseek.com",
      "api": "openai-completions",
      "apiKey": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek V4 Pro",
          "contextWindow": 1000000,
          "maxTokens": 384000,
          "input": ["text"],
          "reasoning": true,
          "thinkingLevelMap": { "minimal": null, "low": null, "medium": null, "high": "high", "xhigh": "max" },
          "cost": {
            "input": 1.74,
            "output": 3.48,
            "cacheRead": 0.145,
            "cacheWrite": 0
          },
          "compat": {
            "requiresReasoningContentOnAssistantMessages": true,
            "thinkingFormat": "deepseek",
            "reasoningEffortMap": {
              "minimal": "high",
              "low": "high",
              "medium": "high",
              "high": "high",
              "xhigh": "max"
            }
          }
        },
        {
          "id": "deepseek-v4-flash",
          "name": "DeepSeek V4 Flash",
          "contextWindow": 1000000,
          "maxTokens": 384000,
          "input": ["text"],
          "reasoning": true,
          "thinkingLevelMap": { "minimal": null, "low": null, "medium": null, "high": "high", "xhigh": "max" },
          "cost": {
            "input": 0.14,
            "output": 0.28,
            "cacheRead": 0.028,
            "cacheWrite": 0
          },
          "compat": {
            "requiresReasoningContentOnAssistantMessages": true,
            "thinkingFormat": "deepseek",
            "reasoningEffortMap": {
              "minimal": "high",
              "low": "high",
              "medium": "high",
              "high": "high",
              "xhigh": "max"
            }
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

#### 3. 运行并选择模型

- 进入项目目录并执行 `pi` 命令：

```bash
cd /path/to/my-project
pi
```

- 输入 `/model` 打开模型切换器。
- 选择 **deepseek**，然后选择 `DeepSeek-V4-Pro` 或 `DeepSeek-V4-Flash`。
- 用 V4 Pro 做代码任务时，把 thinking / reasoning effort 设为 **xhigh**（对应上面配置里的 `max`）。V4 支持 1M 上下文；上面的片段已经写了 `contextWindow: 1000000`。
- 开始使用你的极简终端编码框架。

#### 4. 可选：官方 Harness 极简表面（V4 Pro）

DeepSeek V4 Pro 的模型卡在代码 Agent 任务上使用 DeepSeek Harness **极简模式**：完整系统提示词为 `You are a helpful software engineer assistant.`，工具目录为持久 `bash` + `str_replace_editor`。Pi 默认工具目录更丰富，可能改变 V4 Pro 第一次请求的轨迹。

若要在 Pi 里使用这套官方表面：

```bash
pi install npm:pi-dsh-minimal
```

然后 `/reload` 或重启 Pi，**新建会话**并选择 DeepSeek V4 Pro。扩展默认开启，但只在模型匹配 V4 Pro 时生效（`deepseek-v4-flash` 不会匹配）。可用 `/dsh` 改触发条件。

这是一个[社区扩展](https://github.com/Averyyy/pi-dsh-minimal)，不是 DeepSeek 或 Pi 的官方预设。

更多配置选项请参阅 [Pi 模型文档](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/docs/models.md)。
