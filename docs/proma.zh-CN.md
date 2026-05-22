[English](./proma.md) | [简体中文](./proma.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Proma

Proma 是一个本地优先的开源 AI 桌面 Agent，支持 macOS 和 Windows。它把多模型 **Chat 模式**、基于 Claude Agent SDK 的通用 **Agent 模式**，以及工作区、Skills、MCP、记忆、远程机器人等能力放在同一个客户端里。

DeepSeek 是 Proma 的**一等公民渠道**：首次启动自动创建 DeepSeek 预设渠道，`deepseek-v4-pro` / `deepseek-v4-flash` 自动启用 1M 上下文 Beta，同一个 Key 同时驱动 Chat 与 Agent 模式。再叠加 Proma 主动的 SubAgent 编排和把每一步执行都可视化的桌面 UI，这是目前开源里把 DeepSeek V4 真正用起来最丝滑的路径 —— 无需任何终端配置。

- **GitHub:** <https://github.com/ErlichLiu/Proma>
- **官网:** <https://proma.cool>

#### 1. 安装 Proma

从 [Proma Releases 页面](https://github.com/ErlichLiu/Proma/releases) 下载对应平台的安装包。

提供的安装包：

- macOS Apple Silicon (`Proma-x.y.z-arm64.dmg`)
- macOS Intel (`Proma-x.y.z.dmg`)
- Windows (`Proma-Setup-x.y.z.exe`)

安装后启动 Proma 并完成首次运行的环境检查。Agent 模式依赖本机的 Shell、Git 和 Node.js / Bun，请确保这些工具在 `PATH` 中可用。

#### 2. 配置 DeepSeek 渠道

从侧边栏打开 **设置 → 渠道**。Proma 内置了 **DeepSeek** 预设渠道 —— 你只需要填入 API Key。

1. 在渠道列表中找到 **DeepSeek** 条目（首次启动自动创建）。如果不存在，点击 **新建渠道** 并从供应商下拉中选择 **DeepSeek**。
2. 在 **API Key** 字段粘贴你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。**Base URL** 已经预设为 `https://api.deepseek.com/anthropic`（DeepSeek 的 Anthropic 兼容端点），保持默认即可。
3. 确认 **模型列表** 包含 `deepseek-v4-pro` 和 `deepseek-v4-flash`，这两个模型已经预置好。
4. 打开 **启用** 开关，点击 **测试连接** 验证 Key。

到这里渠道配置就完成了。Proma 会通过 Anthropic 兼容适配器，让 DeepSeek 同时驱动 Chat 模式和 Agent 模式。

#### 3. 在 Chat 模式中使用 DeepSeek

打开侧边栏的 **Chat** 标签页，开始一个新会话，在输入框顶部的模型选择器里选择 **DeepSeek V4 Pro**（或 **DeepSeek V4 Flash**）。

Chat 模式支持流式响应、附件（PDF、Office、图片）、Markdown / Mermaid / KaTeX / 代码高亮、多模型并排对比、系统提示词以及内置联网搜索 —— 这些功能在 DeepSeek 上都是开箱即用的。

#### 4. 在 Agent 模式中使用 DeepSeek

打开 **设置 → Agent**，把 **默认 Agent 渠道** 设为你的 DeepSeek 渠道，**默认模型** 设为 `deepseek-v4-pro`。然后切换到 **Agent** 标签页，新建一个会话。

Proma 的 Agent 模式基于 `@anthropic-ai/claude-agent-sdk` 构建，让 DeepSeek V4 在桌面 GUI 里跑完整的 Agent 循环 —— 工具调用、计划模式、权限控制、SubAgent 派发：

- **1M 上下文自动启用**：识别到 `deepseek-v4-pro` / `deepseek-v4-flash` 自动附加 `context-1m-2025-08-07` Beta。
- **内置 SubAgent 体系** —— `explorer` / `researcher` / `code-reviewer`，系统提示词主动派发，配合按复杂度在 DeepSeek V4 Pro 与 V4 Flash 之间路由。DeepSeek 作为**编排者**而非单点应答者，长任务不会污染主上下文。
- **工作区级 Skills / MCP / 记忆 / 文件**，切换工作区即切换项目上下文。
- **计划模式、权限审批、SubAgent 实时活动**全部内联呈现在消息流中。
- **远程触发**：从飞书 / Lark、钉钉、企业微信群里触发 DeepSeek 驱动的 Agent 工作流，桌面端本机执行。

#### 5. 为什么 Proma 是用 DeepSeek V4 最丝滑的开源路径

- **零配置 DeepSeek**：预设渠道、预设模型、1M 上下文写在代码里 —— 粘贴 Key 即可开干。
- **一个 Key，两种模式**：同一个 DeepSeek 渠道同时驱动 Chat 与完整 Agent 循环，一个客户端搞定。
- **主动的 SubAgent 编排**：内置 `explorer` / `researcher` / `code-reviewer`，系统提示词主动派发，按复杂度在 DeepSeek V4 Pro 与 V4 Flash 之间路由 —— DeepSeek 能爆发出远超单一上下文窗口的能力。
- **GUI 超越终端 Agent**：SubAgent 实时活动流、并排 Diff 预览、多会话并发流式、附件预览、计划/权限 UI、语音输入、飞书/钉钉/微信机器人桥接 —— 完整呈现在一个桌面应用里。
- **本地优先**：会话、工作区、Skills 全部以 JSON / JSONL 存在 `~/.proma/`，易于备份、易于审查。

Proma 完全开源（[Apache-2.0](https://github.com/ErlichLiu/Proma)），欢迎贡献能体现 DeepSeek V4 能力的 Skills、MCP 配置和 Agent 工作流。
