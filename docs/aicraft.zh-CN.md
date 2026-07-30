[English](./aicraft.md) | [简体中文](./aicraft.zh-CN.md) · [← Back](../README.md)

# 在 AICraft 中集成 DeepSeek

AICraft 是一个 Windows 桌面 AI 能力启动器，通过可视化界面管理 LLM 技能（Skill）、MCP 工具、RAG 和记忆——可以理解为"AI 能力的 Minecraft 启动器"。AICraft 内置**一键 DeepSeek 配置**，通过 Anthropic 兼容 API 端点原生支持 DeepSeek V4 Pro 和 V4 Flash。

- **GitHub：** <https://github.com/Easlie114514/AICraft>
- **下载：** <https://github.com/Easlie114514/AICraft/releases>

## 为什么选择 AICraft + DeepSeek

AICraft 是为 DeepSeek 原生打造的。它从底层使用 Anthropic SDK 通过 `api.deepseek.com/anthropic` 端点连接，为你带来：

- **一键配置** — 粘贴 API Key 即可自动创建 `deepseek-v4-pro` 和 `deepseek-v4-flash` 两个模型配置
- **原生深度思考** — 通过"深度思考"开关控制 DeepSeek 的推理过程
- **Auto 智能路由** — "Auto" 模式自动将简单问题路由到 Flash（省钱），复杂任务切换到 Pro
- **联网搜索** — 直接在聊天界面使用 DeepSeek 的服务端联网搜索能力
- **实时 Token 计费** — 按会话和全生命周期的 Token 用量统计，精确到缓存命中/未命中

#### 1. 下载安装 AICraft

从 [Releases 页面](https://github.com/Easlie114514/AICraft/releases) 下载最新的便携版 EXE。

AICraft 支持 **Windows 10/11**。无需安装——解压后直接运行 `AICraft.exe` 即可。

#### 2. 一键配置 DeepSeek

1. 启动 AICraft，切换到侧边栏的**模型**标签页（第 7 个）。
2. 点击 **DeepSeek** 快速配置卡片。
3. 将你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 API Key 输入框。
4. 点击**保存**。

系统会自动创建两个模型配置：
- `deepseek-v4-pro` — 用于复杂推理、编码和多步骤任务
- `deepseek-v4-flash` — 用于快速响应、简单查询和后台任务

AICraft 通过 Anthropic 兼容端点（`https://api.deepseek.com/anthropic`）连接，从而原生支持深度思考模式和服务端联网搜索。

#### 3. 开启深度思考（推理模式）

在**对话**标签页中，打开**深度思考**开关即可启用 DeepSeek 的推理过程。开启后，AICraft 会显示"思考中..."动画，并展示模型的推理步骤，最后显示"已思考 X.X 秒"摘要。

当模型选择器设置为 Auto 时，深度思考会自动路由到 `deepseek-v4-pro`。

#### 4. 开始对话

切换到**对话**标签页，从模型下拉菜单中选择 `Auto`（推荐）、`deepseek-v4-pro` 或 `deepseek-v4-flash`，即可开始对话。你还可以：

- 启用 **MCP 工具**（文件管理 + 代码执行）获得 Agent 能力
- 开启 **RAG** 获取基于文档的回答
- 开启**联网搜索**获取实时信息
- 加载**技能（Skill）**和**角色（Role）**定制 AI 行为

> **提示：** 建议保持模型为 `Auto`——AICraft 会自动将简单消息路由到 Flash（节省成本），当问题复杂、使用 MCP 工具或开启 RAG/深度思考时自动切换到 Pro。
