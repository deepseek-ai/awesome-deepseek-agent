[English](./rikkahub.md) | [简体中文](./rikkahub.zh-CN.md) · [← Back](../README.zh-CN.md)

# 接入 RikkaHub

RikkaHub 是一款原生 Android LLM 聊天客户端（Kotlin + Jetpack Compose + Material 3），将 OpenAI、Google Gemini、Anthropic Claude 以及任何 OpenAI 兼容端点整合在同一界面中，内置 MCP、多模态输入、网络搜索、Prompt 变量、消息分支，以及基于 proot 的 Linux Agent 工作环境（Workspace）。

- **官网：** <https://rikka-ai.com>
- **官方文档：** <https://docs.rikka-ai.com>
- **GitHub：** <https://github.com/rikkahub/rikkahub>

#### 1. 安装 RikkaHub

任选一个官方渠道下载：

- **官网（推荐）：** <https://rikka-ai.com/download> —— 始终是最新 APK。
- **Google Play：** 搜索 "RikkaHub"，或直接打开 <https://play.google.com/store/apps/details?id=me.rerere.rikkahub>

RikkaHub 仅支持 Android 平台（minSdk 26 / Android 8.0+）。安装完成后从桌面或抽屉打开 App。

#### 2. 配置 DeepSeek Provider

DeepSeek 在 RikkaHub 中是**预配置 Provider**，无需手动填写 Base URL。

1. 点击侧边栏底部的 **设置** 图标（齿轮），打开设置页。
2. 在设置列表中选择 **Providers（服务商）**，进入 Provider 列表页。
3. 找到 **DeepSeek** 卡片（已预配 `Base URL = https://api.deepseek.com/v1`），点击进入。如果列表里没有，点击右上角 **Add Provider（添加 Provider）**，类型选 **OpenAI**，Base URL 填 `https://api.deepseek.com/v1`。
4. 在 Provider 详情页，把 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 **API Key** 字段。**Base URL** 保持 `https://api.deepseek.com/v1` 不变 —— `/v1` 后缀是必须的，因为 RikkaHub 会在其后追加 chat completions 路径（`/chat/completions`）。
5. 点击 **保存** / **确认** 存储配置，然后用 Provider 卡片上的开关启用它。

> **余额检查。** 内置 DeepSeek Provider 默认已开启 **Balance Checking（余额检查）** —— 通过查询 `/user/balance` 并提取 `balance_infos[0].total_balance` 在卡片上显示剩余额度。如果你是手动添加的 DeepSeek，请在 Provider 设置里手动开启 **Balance Checking**，并填入相同的 API path 与 JSON field path。

> **100 万 token 上下文。** RikkaHub 不暴露 `context_window` 字段；App 每次请求都会把完整消息历史透传给 API（受 Assistant 的 `contextMessageSize` 设置约束，默认 0 = 全部消息）。DeepSeek V4 在 API 侧支持最高 **1,000,000 token** 上下文，RikkaHub 不做任何客户端侧截断，发多少用多少。

#### 3. 添加 DeepSeek V4 模型

1. 在同一 DeepSeek Provider 详情页，滚动到底部的 **Models（模型）** 区域并点击。
2. 点击展开按钮，RikkaHub 会自动从 DeepSeek API 拉取模型列表，勾选 **`deepseek-v4-pro`** 与 **`deepseek-v4-flash`**。
3. （如果自动拉取没列出 V4 模型 —— 比如你用的是尚未跟进的第三方中转 —— 点击 **Add（添加）** 手动输入模型 ID：`deepseek-v4-pro` / `deepseek-v4-flash`。）

RikkaHub 的模型注册表已识别这两个 ID，并自动给它们打上 **Tool** 与 **Reasoning** 能力标签 —— 无需手动勾选。

#### 4. 开始对话

1. 返回主界面。点击顶部对话标题下方的 **模型选择器**（部分屏幕尺寸下位于输入栏内），选择 **`deepseek-v4-pro`**（追求性价比或速度时用 `deepseek-v4-flash`）。
2. 在底部输入栏输入第一条消息，点击 **发送** 按钮（向上箭头）。RikkaHub 会实时流式返回回答。
3. DeepSeek V4 默认会返回思维链内容，RikkaHub 会把推理过程作为可折叠块显示在最终回答上方。

##### 思考强度

RikkaHub 通过 Assistant 的 **Reasoning level（思考级别）** 设置（`设置 → Assistants → <你的 Assistant> → Reasoning level`，默认 `AUTO`）控制思考强度，各档位如下：

| 级别 | Token 预算 | 发给 DeepSeek API 的 effort 字符串 |
|---|---|---|
| OFF | 0 | *（关闭思考）* |
| AUTO | -1 | *（由 Provider 决定，不发送 `reasoning_effort` 字段）* |
| LOW | 1,000 | `low` |
| MEDIUM | 2,000 | `medium` |
| HIGH | 8,000 | `high` |
| XHIGH | 16,000 | `xhigh` |

针对 DeepSeek（Base URL host 为 `api.deepseek.com` 的 Provider），RikkaHub 的请求构建器会同时发送 `thinking: {type: "enabled"}` 与 `reasoning_effort: <effort>`。要在 UI 暴露的范围内获得最强推理，把级别设为 **XHIGH**。

> **关于 `reasoning_effort: "max"`。** RikkaHub 的枚举最高只到 `XHIGH`，所以 UI 自身向 DeepSeek API 发送的是 `reasoning_effort: "xhigh"`，而非 `"max"`。如果你确实需要 `max` 档，使用 Assistant 的**自定义请求体**覆盖：打开 Assistant → **HTTP overrides → Custom Bodies** → 添加键 `reasoning_effort`，值 `"max"`。RikkaHub 的 custom body 是**最后合并**的，会覆盖 Assistant 选定的级别。这是 RikkaHub 官方提供的"固定 UI 未暴露字段"机制，并非针对上游 bug 的 workaround。

#### 5. 进阶用法

完成 DeepSeek V4 配置后，可以在 RikkaHub 的其他场景中复用：

- **Workspace**：进入 **设置 → 扩展管理 → Workspace**，点击右下角 **+** 创建工作区（名称必须为英文），点击新卡片 → **Install Rootfs** 安装系统文件。打开聊天页，点击聊天栏的 **+** 按钮，将 Workspace 绑定到当前 Assistant。由 `deepseek-v4-pro` 驱动的 Assistant 即可在沙箱 Linux 环境里执行 shell 命令、编辑文件、通过 `apt` 安装软件包，甚至克隆 Git 仓库。
- **MCP 服务**：进入 **设置 → MCP**，点击右上角 **+** 添加服务（支持 SSE 与 Streamable HTTP 两种 transport）。连接成功后，打开 Assistant 设置 → **MCP Servers** → 勾选该 Assistant 可调用的服务。工具调用经过审批流 —— 对任何不可逆操作的工具，请打开 **Needs Approval（需要批准）** 选项。
- **网络搜索**：进入 **设置 → Search（搜索）**，点击 **Add（添加）** 选择搜索服务 —— RikkaHub 支持 Bing、Brave、Tavily、Exa、Perplexity、LinkUp、Firecrawl、Jina、Grok、Bocha（博查）、Metaso（秘塔）、Zhipu（智谱）、SearXNG、Ollama、RikkaHub 自有 API 以及 Custom JS。配置完成后，发送消息前在聊天输入栏工具栏点亮搜索图标，RikkaHub 会自动把最新网页结果注入模型上下文。
- **多模态输入**：点击聊天输入栏左侧的 **+** 按钮附加图片、PDF、DOCX、PPTX、EPUB 文件。支持视觉输入的模型会以 base64 形式收到图片；非视觉模型会自动触发 OCR（通过 **设置 → Models → OCR Model** 配置的 OCR 模型完成）。
- **提示词变量与消息分支**：Assistant 的系统提示里可使用 `{model}`、`{time}` 等变量。长按任一助手回复 → **Regenerate（重新生成）** 即可创建分支，探索不同续写而不破坏原会话。
- **二维码 Provider 导出**：打开 DeepSeek Provider → 点击 **Share（分享）** 按钮 → 将配置（API key + base URL + 设置，不含已添加的模型）导出为二维码。在另一台设备扫码即可一键复制整套 Provider 配置。
