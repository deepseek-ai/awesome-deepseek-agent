[English](./taco.md) | [简体中文](./taco.zh-CN.md) · [← Back](../README.zh-CN.md)

# 接入 Taco AI

Taco AI 是一款面向 macOS 和 Windows 的开源桌面 AI 助手，基于 Electron + React + TypeScript 构建。它在统一界面中集成多模型支持，内置终端、代码编辑器、浏览器自动化、图片理解、项目记忆和 MCP 工具——为 DeepSeek 提供完整的桌面端运行环境。

- **GitHub：** <https://github.com/Fushengfu/tacoai>
- **下载：** [macOS](https://store.huiyuanjia.net/Taco%20AI-0.3.10-arm64.dmg) · [Windows](https://store.huiyuanjia.net/Taco%20AI%20Setup%200.3.10.exe)

#### 1. 安装 Taco AI

下载对应平台的安装包：

- **macOS** — `.dmg`（Apple Silicon）
- **Windows** — `.exe`（x64 NSIS 安装包）

安装后启动 Taco AI，首次启动会提示登录。

#### 2. 配置 DeepSeek 模型服务

点击左下角的齿轮图标打开 **设置**，进入 **模型服务** 标签页。

1. 在内置 Provider 列表中找到 **DeepSeek** 并选中。
2. 将 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 **API Key** 字段。
3. 将 **上下文窗口** 设置为 `1000000`，以充分利用 DeepSeek V4 的 100 万 token 上下文。
4. 将 **推理强度** 设置为 `max`，在编码和复杂任务中获得最强推理能力。
5. 如需使用 DeepSeek V4 的多模态图片理解能力，打开 **视觉** 开关。
6. 点击 **保存** 应用配置。

Taco AI 使用 OpenAI 兼容的 API 端点，会自动将配置映射为 DeepSeek 的 `reasoning_effort` 和 `max_tokens` 参数。

#### 3. 开始对话

返回主聊天界面。在聊天窗口底部的模型选择器中，选择 **`deepseek-v4-pro`**（适用于复杂推理和编码任务）或 **`deepseek-v4-flash`**（适用于更快速、轻量的任务）。

输入消息后按 Enter 或点击发送按钮。DeepSeek V4 将以配置的完整 **100 万 token** 上下文窗口和 `reasoning_effort: "max"` 运行，无需每次对话单独设置。

#### 4. 进阶用法

配置好 DeepSeek V4 后，你可以在 Taco AI 的所有功能中使用它：

- **终端**：Taco AI 可以直接在你的系统上执行 Shell 命令。让 DeepSeek 运行构建、管理依赖或调试问题——它会自动读取命令输出并迭代执行。
- **代码编辑器**：打开任意文件，Taco AI 内置的 Monaco 编辑器会高亮语法并实时预览差异。DeepSeek 可以跨项目读写和重构代码。
- **浏览器自动化**：Taco AI 可以操控 Chromium 浏览器来测试 Web 应用、填写表单、抓取数据或验证 UI——全部由 DeepSeek 驱动。
- **图片理解**：粘贴或上传图片，DeepSeek V4 会对其进行分析——截图、图表、医疗报告等均支持。
- **项目记忆**：Taco AI 维护基于 SQLite 的持久化记忆库，跨会话保留。DeepSeek 会回顾过往决策、架构笔记和任务历史，提供上下文感知的协助。
- **MCP 工具**：通过 MCP 协议连接外部工具，让 DeepSeek 访问数据库、API 和专业服务。
- **计划与执行**：对于复杂的多步骤任务，Taco AI 会先提出执行计划并等待确认，让你始终掌握控制权。
