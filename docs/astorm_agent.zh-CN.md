[English](./astorm_agent.md) | [简体中文](./astorm_agent.zh-CN.md) · [← Back](../README.md)

# 接入 Astorm Agent

Astorm Agent 是一款开源、本地优先的桌面 AI 智能体，采用 Electron + Vue 3 构建界面、Rust 实现核心能力。它把 DeepSeek V4 与文件、Shell、Git、浏览器、Office、MCP 等工具放进一个带安全沙箱的桌面工作区。

- **GitHub：** <https://github.com/hxuxingy1212/astorm-desktop-electron>
- **Releases：** <https://github.com/hxuxingy1212/astorm-desktop-electron/releases>

#### 1. 安装 Astorm Agent

从 [Releases 页面](https://github.com/hxuxingy1212/astorm-desktop-electron/releases) 下载最新的 macOS 安装包：

- **macOS 12+，Apple Silicon（arm64）：** 打开 `.dmg`，把 **Astorm Agent** 拖入「应用程序」。
- 公开的 macOS 包已使用 Developer ID 签名，并通过 Apple 公证。

如需在 macOS、Windows 或 Linux 上从源码构建，请先安装 Node.js 20.19+（或 22.12+）、pnpm 10 与 Rust 1.85+，然后执行：

```bash
git clone https://github.com/hxuxingy1212/astorm-desktop-electron.git
cd astorm-desktop-electron
pnpm install
pnpm run dev
```

原生组件按宿主平台构建；生产构建使用 `pnpm run build`。

#### 2. 配置 DeepSeek 供应商

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

1. 打开 **设置 → 模型**，点击 **添加供应商**。
2. **名称** 填 `DeepSeek`。
3. **Base URL** 填 `https://api.deepseek.com`。
4. **API 格式** 选择 **Chat Completions (/chat/completions)**。
5. 粘贴 **API Key**。
6. 点击 **新增模型**，添加：
   - `deepseek-v4-pro` — 推理能力最强，纯文本模型，支持 100 万 token 上下文。
   - `deepseek-flash` — 速度更快、成本更低，支持图片输入，同样支持 100 万 token 上下文。
7. 点击 **保存**。第一个供应商及其第一个模型会成为默认模型；可拖动排序手柄调整供应商或模型顺序。

> **关于「检测」按钮：** Astorm 的 **检测** 会发送一段文字 + 一张图片，同时验证指令遵循和图片识别能力。`deepseek-v4-pro` 是纯文本模型，因此检测可能提示「不支持视觉」，但这不影响文本对话。想让检测通过可以使用 `deepseek-flash`，或对 Pro 跳过检测。

> **模型命名说明：** DeepSeek 最新价格页把 Flash 模型列为 `deepseek-flash`；旧的 `deepseek-v4-flash` 仍作为别名被接受，新配置请使用 `deepseek-flash`。

#### 3. 开始对话

1. 新建对话，并选择一个工作区目录。
2. 点击输入框底部的模型胶囊（显示当前模型和推理等级）。
3. 选择 **DeepSeek → `deepseek-v4-pro`**（或 `deepseek-flash`）。
4. 选择 **推理等级 → 最高**（Astorm 0.1.1+；旧版本最高为「高」）。
5. 发送消息。Astorm 会流式输出回答、展示思考过程，并在执行敏感的文件、Shell 或网络操作前请求审批。

DeepSeek V4 支持 **100 万 token** 上下文，长文档和多文件任务无需额外设置上下文窗口。如果希望调整长会话的摘要/压缩策略，可在 **设置 → 会话** 中修改阈值。

#### 4. 推理等级与模型选择

Astorm 提供五档推理等级：**无**、**低**、**中**、**高**、**最高**，并把选中的等级作为 DeepSeek 的 `reasoning_effort` 字段发送。**最高** 对应 `reasoning_effort: "max"`，需要 Astorm **0.1.1 或更高版本**；旧版本的最高档为「高」。

- **`deepseek-v4-pro` + 最高**：适合编码、规划和复杂的工具调用。
- **`deepseek-flash`**：适合更快、更低成本且需要图片输入的对话。

DeepSeek 的价格会调整，因此本指南不内置价格表。请以官方 [价格页面](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 为准。

#### 5. 常见问题

| 现象 | 处理方式 |
| --- | --- |
| `401 Unauthorized` | 检查 API Key，确认它属于当前选中的供应商。 |
| `404` 或 `Model Not Found` | 模型名必须精确为 `deepseek-v4-pro` 或 `deepseek-flash`；Base URL 填 `https://api.deepseek.com`，不要带 `/chat/completions`。 |
| 「检测」提示不支持视觉 | `deepseek-v4-pro` 是纯文本模型。文本对话仍可用；需要图片任务请用 `deepseek-flash`，或跳过检测。 |
| `reasoning_effort` 被拒绝 | 在 Astorm 中使用 **无 / 低 / 中 / 高 / 最高**；最高档需要 0.1.1+，旧版本最高为「高」。 |
| macOS 提示应用已损坏 | 用 `spctl -a -vvv --type execute "/Applications/Astorm Agent.app"` 校验公证，并确认安装包来自官方 Releases 页面。 |

#### 6. 更多能力

Astorm Agent 还提供：

- **安全沙箱工具** — 文件、Shell、Git 与网络操作，带审批和审计日志。
- **内置浏览器** — 让 DeepSeek 导航、点击并提取网页内容。
- **Office 与邮件** — 创建/编辑 Word、Excel、PowerPoint、PDF，管理 IMAP/SMTP 邮箱。
- **MCP 与插件** — 连接外部工具并扩展界面。
- **本地优先数据** — 会话、工作区与 API Key 都保存在本机。
