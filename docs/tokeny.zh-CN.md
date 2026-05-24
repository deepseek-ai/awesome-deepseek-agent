[English](./tokeny.md) | [简体中文](./tokeny.zh-CN.md) · [← Back](../README.zh-CN.md)

# 接入 Tokeny

Tokeny 是一款跨平台（Windows / macOS / Linux）的**桌面 AI 助手**，在对话工作区中集成了内置工具（文件、Shell 命令、网页搜索）、开放的 Skill 技能系统与 MCP 插件。它**内置 DeepSeek 渠道**，只需填入 API Key 即可开始使用 DeepSeek V4。

- **官网：** <https://tokeny-ai.com>
- **文档：** <https://tokeny-ai.com/docs>

#### 1. 安装 Tokeny

请从 [Tokeny 官网下载页](https://tokeny-ai.com) 下载对应平台的安装包：

- Windows（`.exe`，Windows 10+）
- macOS（`.dmg`，支持 Apple Silicon 与 Intel）
- Linux（`.AppImage`）

#### 2. 配置 DeepSeek 模型服务

打开 Tokeny，进入 **设置 → AI 模型配置**（左侧边栏的大脑图标）。DeepSeek 已经在渠道列表中，无需新建自定义渠道。

1. 找到 **DeepSeek** 渠道，**API 协议** 保持 **OpenAI 兼容**，**API Base URL** 已预填为 `https://api.deepseek.com/v1`。
2. 将 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 **API Key** 字段，点击 **测试** 验证连通性。
3. 在 **模型管理** 中，确认 **`deepseek-v4-pro`** 与 **`deepseek-v4-flash`** 已勾选启用。
4. 打开 DeepSeek 渠道右上角的开关，启用该渠道。

<div align="center">
<img src="./assets/tokeny_provider.png" width="720" border="1" />
</div>

> 旧的 `deepseek-chat` / `deepseek-reasoner` 别名仍保留以兼容历史配置，但请选择 **`deepseek-v4-pro`** 或 **`deepseek-v4-flash`** —— 这才是当前的模型名称。

#### 3. 开始对话

回到工作区，点击对话输入框底部的模型选择器，选择 **`deepseek-v4-pro`**（编码与推理最强）或 **`deepseek-v4-flash`**（速度快、性价比高），输入消息即可发送。

<div align="center">
<img src="./assets/tokeny_chat.png" width="720" border="1" />
</div>

DeepSeek V4 在 Tokeny 中默认即可使用完整的 **100 万 token** 上下文窗口，无需额外配置。两款 V4 模型均支持**可切换的思考模式**：保持思考模式开启，即可在编码与复杂任务中获得最强推理表现。Tokeny 会自动把该开关映射为 DeepSeek 原生的 `thinking` 参数，并在对话中实时渲染模型的推理过程。

如需按模型微调参数（上下文窗口、最大输出、思考模式），可点击 **模型管理** 中每个模型旁的扳手图标进行设置。

#### 4. 进阶用法

完成 DeepSeek V4 配置后，你可以在 Tokeny 的其他场景中复用它：

- **Skill 技能**：通过 `/指令` 触发深度研究、代码审查、前端设计、PPT 生成等内置技能，也可让 Agent 自动选择；社区技能支持粘贴 GitHub 链接一键安装。
- **MCP 插件**：添加 MCP 服务（SSE 或 stdio），为 DeepSeek 扩展更多工具，Agent 可在对话中随时调用。
- **内置工具**：DeepSeek 可在工作空间中读写文件、执行 Shell 命令、搜索网页，并通过权限确认机制让你对风险操作进行授权。
