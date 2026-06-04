[English](./kimi_code.md) | [简体中文](./kimi_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Kimi Code CLI

Kimi Code CLI 是一个运行在终端中的 AI 编程 Agent，它可以读取和编辑代码、运行 shell 命令、搜索文件、获取网页内容，并根据反馈选择下一步操作。

### 安装 Kimi Code CLI

#### 方式一：脚本安装（推荐）

最快的安装方式，无需预装 Node.js。

**macOS / Linux：**

```bash
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

**Windows（PowerShell）：**

```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

#### 方式二：npm 安装

需要 Node.js 24.15.0 或更高版本。

```bash
npm install -g @moonshot-ai/kimi-code
```

或使用 pnpm：

```bash
pnpm add -g @moonshot-ai/kimi-code
```

#### 验证安装

安装完成后，验证 CLI 是否就绪：

```bash
kimi --version
```

#### 升级与卸载

**升级：**
- 脚本安装的用户：重新运行安装脚本
- npm 用户：`npm install -g @moonshot-ai/kimi-code@latest`

**卸载：**
- 脚本安装的用户：删除 `kimi` 可执行文件即可
- npm 用户：`npm uninstall -g @moonshot-ai/kimi-code`

### 配置 Kimi Code CLI

Kimi Code CLI 开箱即用支持 Moonshot AI 的 Kimi 模型，也可以配置其他兼容的提供商，如 DeepSeek。

在交互界面中运行 `/connect`，然后：

1. 搜索并选择 **DeepSeek**
2. 选择要使用的模型（如 `deepseek-v4-pro` 或 `deepseek-v4-flash`）
3. 按回车并填入你的 DeepSeek API Key

你可以在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

> **注意：** DeepSeek V4 模型支持最高 **100 万 token** 的上下文窗口。你还可以开启 thinking 模式以获得更强的推理能力。

### 使用 Kimi Code CLI

进入项目目录，启动交互式界面：

```bash
cd /path/to/your-project
kimi
```

首次使用 DeepSeek 时，可以尝试以下任务：

```
看看这个项目，解释一下它的主要目录结构。
```

### 主要特性

- **单文件分发**：一条命令即可安装，无需 Node.js 环境配置、PATH 设置或全局模块冲突。
- **极速启动**：TUI 在毫秒级内就绪，启动会话毫无延迟感。
- **专用 TUI 界面**：精心调优的界面，专为长时间专注的 Agent 会话设计。
- **视频输入**：将屏幕录制或演示视频拖入聊天，让 Agent 观看难以用文字描述的内容。
- **AI 原生 MCP 配置**：通过 `/mcp-config` 对话式添加、编辑和认证 MCP 服务器，无需手动编辑 JSON。
- **子代理并行工作**：在隔离上下文中调度内置的 coder、explore 和 plan 子代理，保持主对话简洁。
- **生命周期钩子**：在关键节点运行本地命令，用于拦截危险工具调用、审计决策、触发桌面通知或连接自定义自动化流程。

### 相关资源

- [Kimi Code GitHub 仓库](https://github.com/MoonshotAI/kimi-code)
- [Kimi Code 文档](https://moonshotai.github.io/kimi-code/zh/)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
- [DeepSeek 开放平台](https://platform.deepseek.com/)
