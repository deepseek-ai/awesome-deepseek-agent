[English](./chatbox.md) | [简体中文](./chatbox.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Chatbox

Chatbox 是一款开源、本地优先的 AI 聊天客户端，支持桌面、网页与移动端。它支持 30+ 模型服务商、知识库、文件与链接上下文、MCP 服务、提示词管理和多模型对话。

- **GitHub：** <https://github.com/chatboxai/chatbox>
- **官网：** <https://chatboxai.app>

#### 1. 安装 Chatbox

请从 [Chatbox 官网](https://chatboxai.app) 或 [GitHub Releases](https://github.com/chatboxai/chatbox/releases) 下载对应平台的安装包。

可用版本：

- Windows（`.exe`）
- macOS（`.dmg`，支持 Intel 与 Apple Silicon）
- Linux（`.AppImage`）
- iOS / Android

#### 2. 配置 DeepSeek 模型服务

打开 Chatbox，进入 **设置 → 模型提供方 → DeepSeek**。

1. 将 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 **API Key**。
2. 保持默认 DeepSeek API 地址。
3. 在 **模型** 区域点击 **Fetch**，添加 **`deepseek-v4-pro`** 与 **`deepseek-v4-flash`**。
4. 如果拉取列表中暂时没有这两个模型，点击 **New** 手动添加。

手动添加时，请为两个模型分别填写：

| 字段 | `deepseek-v4-pro` | `deepseek-v4-flash` |
| ---- | ----------------- | ------------------- |
| Model ID | `deepseek-v4-pro` | `deepseek-v4-flash` |
| Model Type | `Chat` | `Chat` |
| Capabilities | `Reasoning`、`Tool use` | `Reasoning`、`Tool use` |
| Context Window | `1000000` | `1000000` |
| Max Output Tokens | `384000` | `384000` |

DeepSeek V4 支持 **100 万 token** 上下文窗口。在 Chatbox 中设置正确的上下文窗口后，token 计数、自动压缩、文件上下文与长对话提醒都会按正确上限工作。

#### 3. 开始对话

回到主对话页面，打开输入框中的模型选择器，选择 **DeepSeek → `deepseek-v4-pro`** 或 **DeepSeek → `deepseek-v4-flash`**。

编码、Agent 工作流和复杂推理建议使用 **`deepseek-v4-pro`**；日常对话、总结和轻量工具调用建议使用 **`deepseek-v4-flash`**。

当所选模型标记了 **Reasoning** 能力时，Chatbox 会为 DeepSeek V4 启用思考模式。为了获得更强的编码体验，建议保留 `deepseek-v4-pro` 的 **Reasoning** 能力。

#### 4. 进阶用法

完成 DeepSeek V4 配置后，你可以在 Chatbox 的其他场景中复用它：

- **知识库**：添加本地文档后，即可用 DeepSeek V4 基于知识库进行问答。
- **文件与链接**：上传文件或粘贴 URL，Chatbox 会解析内容并加入对话上下文。
- **MCP 服务**：在 **设置 → MCP** 中添加 MCP 服务，让 DeepSeek 驱动的对话调用外部工具。
- **提示词库**：保存常用提示词，并在任一 DeepSeek V4 模型上复用。
