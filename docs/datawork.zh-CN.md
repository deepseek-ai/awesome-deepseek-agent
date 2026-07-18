[English](./datawork.md) · [← 返回 README](../README.zh-CN.md)

# 在 DataWork 中使用 DeepSeek V4

DataWork 是一个**本地优先的个人 AI Agent 系统（Windows 桌面应用）**——
是你本地上下文中心与行动层，把文件、AI 对话、笔记、待办和其他工具连接在一起。

每一项功能都从个人真实需求出发——帮助你持续积累和复用上下文、经验、工具和工作流。

在持续探索人机协作的最佳方式——所有设计既对人友好，也对 Agent 友好。

普通用户和开发者均合适，没有使用门槛；尤其适合已经在与 AI 深度协作的人。

> DataWork 开发时主要以 DeepSeek 作为测试模型，Agent 环境与模型的适配度很好。

**DataWork 的独特优势：**

- **无需注册、无需登录** — 完全离线、完全本地，数据只留在你的电脑上。
- **中英文双语界面** — 兼顾国内外用户。
- **原生 Windows 桌面应用** — 界面清晰直观。
- **双 Agent 系统** — 通用 Agent（日常对话、信息整理）+ Code Agent（编码、调试、多轮工具调用）；两者共享模型、记忆、待办、插件和 MCP 配置。
- **MCP 生态** — 既可接入外部 MCP Server，也可将自身记忆库和 Todo 系统开放为 MCP Server，供 Cursor、Claude Desktop、Claude Code 等其他 Agent 工具直接连接调用。
- **Python 插件系统** — 写一个 `.py` 文件即插件，两个 Agent 立刻能调用。
- **10 家 AI 供应商** — DeepSeek、Kimi、小米 MiMo、Qwen、GLM、OpenAI、Claude、Gemini、OpenRouter、Ollama，统一在一个工作台中管理。
- **记忆 + 待办 + 笔记 + Coder 编辑器 + Python + 插件** — 全内置，保持极致的开放性，能力拓展方便，也适合与其他 Agent 集成。
- **Code Agent 能力完整** — Skill、Claw、Workflow、ACP 等功能一应俱全，与行业前沿对齐，实用性极强。接入 DeepSeek 时，缓存命中率可达 95%。

通过 DeepSeek 供应商，DataWork 支持 `deepseek-v4-flash` 和 `deepseek-v4-pro`
两个 V4 模型，包括流式输出、思考模式、思考强度控制和工具调用能力。

## 1. 安装 DataWork

- **项目仓库**：<https://github.com/jkjoker/datawork>
- **下载页面**：<https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout>

下载安装包（`datawork_setup.exe`），解压后运行即可。DataWork 支持 **Windows 10 及以上**
系统，无需注册或登录。

## 2. 获取 DeepSeek API Key

1. 打开 <https://platform.deepseek.com/api_keys>。
2. 登录并创建 API Key。
3. 复制并妥善保管，不要公开。

## 3. 添加模型

1. 启动 DataWork，进入 **设置** → **模型管理**。
2. 在添加区域填写：

| 字段 | 值 |
|---|---|
| 供应商 | `deepseek` |
| Model Name | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| Base URL | `https://api.deepseek.com/chat/completions` |
| API Key | 你的 DeepSeek API Key |

选择 `deepseek` 后 Base URL 会自动填入。点击**添加模型**保存。

模型添加后，DataWork 会自动识别这两个模型的内置价格信息，无需手动填写。

## 4. 创建 Agent

1. 进入 **设置** → **通用 Agent** → **Agent 管理**。
2. 填写名称、选择刚添加的 DeepSeek 模型、设置权限，点击**添加Agent**。

现在就可以在主 AI 选项卡（Expert / Code 模式）、Coder 编辑器或内置
Web 服务中使用这个 Agent 了。

在 **专家模式** 下，选择 Agent、选择推理深度（`High` / `Max`），
发送消息即可开始使用。

## 其他能力

DataWork 的 DeepSeek V4 集成还支持：

- **思考模式**：在 **Tips** → **对话特性** 中勾选启用。
- **思考强度**：模型支持时底部显示 `High` / `Max` 选择器。
- **1M 上下文**：两个 V4 模型均已登记 100 万 token 上下文预算。
- **MCP 工具调用**：Agent 可多轮调用已配置的工具。
- **Code Agent**：切换到 `Code` 模式处理编码任务。

## 相关链接

- DataWork：<https://github.com/jkjoker/datawork>
- DeepSeek API Key：<https://platform.deepseek.com/api_keys>
- DeepSeek API 文档：<https://api-docs.deepseek.com/>
