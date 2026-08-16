[English](./opencode.md) | [简体中文](./opencode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenCode

OpenCode 是一个开源 AI 编程助手，提供终端、桌面和网页等运行形式，内置 `deepseek` 供应商，开箱即用支持 DeepSeek。

#### 1. 安装 OpenCode

- **终端（CLI）**：运行 `curl -fsSL https://opencode.ai/install | bash`，或从 [OpenCode 下载页面](https://opencode.ai/zh/download) 下载对应平台的二进制。
- **桌面 / 网页**：从[下载页面](https://opencode.ai/zh/download)获取桌面应用或使用网页版。

> **注意：** 为避免兼容性问题，建议将 OpenCode 升级到最新版本（>= v1.14.24）。

#### 2. 填入 DeepSeek API Key

1. 前往 [DeepSeek 控制台](https://platform.deepseek.com/api_keys) 注册账号，点击**创建新的 API Key**。
2. 运行 `opencode` 命令启动终端界面。
3. 在输入框中输入 `/connect`，然后输入 `deepseek` 并选择 **DeepSeek** 供应商。
4. 粘贴你的 DeepSeek API Key。

也可以在 shell 配置文件中设置 `DEEPSEEK_API_KEY` 环境变量，OpenCode 会自动读取。

#### 3. 选择模型

在输入框中运行 `/models` 命令，选择当前的 DeepSeek V4 模型：

| 模型 | 说明 |
| ---- | ---- |
| `deepseek-v4-pro` | 旗舰模型，适用于编程、推理和智能体任务 |
| `deepseek-v4-flash` | 快速经济的模型，适用于编程和长上下文任务 |

> **注意：** `deepseek-chat` / `deepseek-reasoner` 是已弃用的 V3 模型名，请使用 `deepseek-v4-pro` 或 `deepseek-v4-flash`。

#### 4. 使用全部能力

内置供应商会自动启用 DeepSeek V4 模型的全部能力，无需额外配置：

- **1M 上下文窗口** — 两个模型均支持最多 1,000,000 token 的上下文（输出 384,000 token）。OpenCode 从模型元数据中读取这些限制并自动进行上下文压缩。
- **最大思考 / 推理强度** — 两个模型均支持 `high` 和 `max` 两档推理强度。在 OpenCode 中，可通过模型选择器或 `opencode.json` 中的模型配置设置推理强度（或开关推理）。

#### 5. 验证

新建一个会话，在模型选择器中确认当前模型为 `deepseek-v4-pro`（或 `deepseek-v4-flash`），发送一条消息即可。DeepSeek 的推理内容会以交错的推理输出显示在会话中。
