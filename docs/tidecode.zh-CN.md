[English](./tidecode.md) | [简体中文](./tidecode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 TideCode

[TideCode](https://github.com/ceciliomichael/TideCode) 是一个面向高效软件开发的桌面 AI 工作区。它将对话、项目文件、编辑器、终端、任务规划、差异查看、Git/GitHub、MCP 和可复用 Skills 集中在一个专注的工作区中。

## 1. 安装 TideCode

从 [TideCode Releases](https://github.com/ceciliomichael/TideCode/releases) 下载最新版本。

目前提供以下桌面版本：

- Windows（`.exe` 安装程序）
- macOS（`.dmg` 安装程序）
- Linux（`.AppImage`）

安装后打开 TideCode，并选择要处理的项目文件夹。

## 2. 配置 DeepSeek 提供商

先从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后按以下步骤操作：

1. 打开 **Settings → Providers**。
2. 选择 **DeepSeek**，点击 **Set up DeepSeek**。
3. 粘贴 API Key，然后点击 **Save provider**。

TideCode 内置的 DeepSeek 提供商使用 DeepSeek 的 OpenAI 兼容 API，地址为 `https://api.deepseek.com`，无需修改 Base URL。

## 3. 选择 DeepSeek V4 模型

打开 **Settings → Models**，确认以下一个或两个模型已启用：

- `deepseek-v4-pro`：适合复杂编程和多步骤任务，能力更强。
- `deepseek-v4-flash`：适合日常迭代，响应更快。

TideCode 直接使用当前的 DeepSeek V4 模型 ID。配置提供商或保存模型时，请使用上面列出的模型 ID。

## 4. 配置上下文和推理强度

打开 **Settings → Configuration**，为需要使用的任务选择 DeepSeek 模型：

- **Agent mode model**：用于实现功能和调用工具。
- **Plan mode model**：用于拆解任务并生成实现计划。
- **Summarization**：用于压缩较长的对话上下文。
- **Git commit and pull request**：用于生成源代码管理摘要。

DeepSeek V4 支持最高 **1,000,000 token 的上下文窗口**。TideCode 在同一个 Configuration 面板中提供 `1,000,000 tokens` 的上下文预算选项。处理大型代码仓库时可以选择该选项，同时保留自动压缩功能，以便管理长时间运行的对话。

启用 DeepSeek 模型后，可以使用聊天输入区域中的推理强度控件。选择 **High** 可使用当前支持的最高推理设置；如果不需要思考过程，可以选择 **None**。TideCode 会将该选择转换为 DeepSeek API 的 `thinking` 和 `reasoning_effort` 请求字段。

## 5. 开始第一次 DeepSeek 会话

1. 打开或创建项目工作区。
2. 开始一个对话，并选择 **Agent** 或 **Plan** 模式。
3. 在模型选择器中选择 **DeepSeek V4 Pro** 或 **DeepSeek V4 Flash**。
4. 让 TideCode 检查项目、解释修改、创建计划，或实现一个小的改进。

TideCode 会通过文件变更和差异视图展示建议的修改。提交之前请先检查变更；当项目需要时，还可以使用集成终端、Git 工具、MCP 服务器或 Skills。

TideCode 会在本地保存 API Key。向服务发送敏感项目内容之前，请先阅读 DeepSeek 的服务条款和数据处理政策。
