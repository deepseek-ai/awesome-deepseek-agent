[English](./deepseekcode.md) | [简体中文](./deepseekcode.zh-CN.md) · [← Back](../README.md)

# 接入 DeepSeekCode

DeepSeekCode 是一个基于 TypeScript + Bun 构建的本地优先 AI 编程助手。一个统一的 Server 后端同时驱动三种界面——终端（Ink TUI）、React 网页端和 Tauri 桌面端——你也可以在 IM 渠道（微信、飞书、Slack、Discord、Telegram、WhatsApp 等）里随时恢复任务并审批挂起的操作。它开箱即用对接 `api.deepseek.com`，支持 DeepSeek-V4-Pro 与 DeepSeek-V4-Flash 的完整 100 万 token 上下文，并原生流式回传推理内容（`reasoning_content`）。Server 仅绑定 `127.0.0.1`，代码始终留在你的电脑上。

- **下载 / 文档:** <https://deepseekcode.github.io/deepseekwork/>
- **npm:** `@deepseekcode/cli`

#### 1. 安装 DeepSeekCode

**CLI（开发者首选）** —— 需要 Node.js 18+ 或 Bun：

```sh
npm install -g @deepseekcode/cli
```

验证安装：

```sh
dscode --version
```

`dscode` 与 `deepseekcode` 指向同一个二进制。

**桌面版（Windows / macOS / Linux）** —— 从 <https://deepseekcode.github.io/deepseekwork/> 下载 Tauri 2 安装包（`.exe` / `.msi` / `.dmg` / `.deb` / `.rpm` / `.AppImage`）。桌面版内置同一套本地 Server 与 Web UI，无需安装 Node.js 或 Bun。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 配置 DeepSeekCode

DeepSeekCode 从 `~/.agent/config.yaml` 读取供应商配置（Windows 为 `%USERPROFILE%\.agent`）。创建该文件并填入你的 Key 与模型：

```yaml
provider:
  provider: deepseek
  baseUrl: https://api.deepseek.com/v1
  apiKey: sk-...
  model: deepseek-v4-pro          # 或 deepseek-v4-flash
  apiType: openai-chat-completions
  maxTokens: 384000
  contextWindow: 1000000          # DeepSeek V4 完整 100 万 token 上下文
  temperature: 0.2
```

配置项说明：

| 配置项 | 说明 |
|--------|------|
| `provider` | `deepseek`（默认）、`openai` 或 `openai-compatible` |
| `baseUrl` | API 基础地址，默认为 `https://api.deepseek.com/v1` |
| `apiKey` | DeepSeek API Key（也可设置环境变量 `DEEPSEEKCODE_API_KEY`） |
| `model` | `deepseek-v4-pro` 或 `deepseek-v4-flash`（也可设置 `DEEPSEEKCODE_MODEL`） |
| `apiType` | `openai-chat-completions`（默认）、`openai-completions` 或 `openai-responses` |
| `maxTokens` | 最大输出 token 数（最高 1,024,000） |
| `contextWindow` | 上下文窗口 token 数——设为 `1000000` 即启用完整 100 万上下文 |
| `temperature` | 采样温度，默认 `0.2` |

首次运行若未配置供应商，DeepSeekCode 会引导你完成配置；也可用 Web UI 的图形化供应商编辑器，或直接编辑 `~/.agent/config.yaml`。

#### 4. 进入项目目录并启动

```sh
cd /path/to/my-project
dscode
```

DeepSeekCode 会启动本地服务（HTTP `:8080`、WebSocket `:8081`）并打开终端 TUI。可用 `dscode run --backend <url>` 连接已有后端，用 `dscode exec '<prompt>'` 做非交互执行（JSONL 输出），用 `dscode test-fix` 跑自愈测试闭环。

#### 常用命令

| 命令 | 作用 |
|------|------|
| `dscode` / `dscode start` | 启动本地核心 + 交互式终端 |
| `dscode run --backend <url>` | 将界面连接到已有后端 |
| `dscode exec '<prompt>'` | 非交互执行，JSONL 输出 |
| `dscode test-fix` | 自愈测试闭环（测试 → 分析 → 修复 → 验证） |
| `dscode codeview` | AI 代码审查（缺陷 + 未接线功能） |
| `/mode act\|plan\|goal` | 切换执行模式 |
| `/pipeline on\|off\|auto` | ReAct ↔ 工作流自动路由覆盖 |
| `/auto` | 切换钩子自动审批 |
| `/mcp <action>` | 管理 MCP 服务器 |
| `/weixin` | 扫码绑定微信 |

#### 工作流、MCP 与 IM 渠道

- **Plan / Act / Goal 模式** —— 计划模式只读；写 / 执行 / 网络等高风险操作由风险分级权限引擎把关，并支持精确到目标的放行审批。
- **ReAct ↔ 工作流自动路由** —— 路由器为每个请求判断任务是走自由探索的 ReAct 循环还是结构化 DAG 工作流，支持推测并行执行与安全回退。
- **MCP** —— 通过 `/mcp` 挂载外部 MCP Server，内置健康检查端点（`/api/mcp/health`）。
- **IM 渠道** —— 内置 16+ 渠道适配器（微信、飞书、Slack、Discord、Telegram、WhatsApp 等），可在聊天工具里恢复并审批挂起任务。
- **技能（Skills）** —— 通过项目级与用户级的 `.skill.md` 技能文件扩展可复用的 Agent 能力。
- **思考 / 推理** —— 对 DeepSeek V4 默认开启思考模式，`reasoning_content` 会流式回传并在界面中渲染。使用 `deepseek-v4-pro` 可获得最佳编程体验。
