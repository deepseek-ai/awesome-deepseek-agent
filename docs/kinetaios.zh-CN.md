[English](./kinetaios.md) | [简体中文](./kinetaios.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 KinetAios

[KinetAios](https://github.com/phinn/KinetAios) 是一个本地优先的多引擎 AI Agent 工作台。它可以在同一窗口并行运行 **Direct(V1 ReAct / V2 / V3 DAG 并行)、Claude Code、Codex 与 DeepSeek Harness**,具备跨引擎长期记忆(SQLite + FTS5)与内置 MCP Server —— 无需账号,你的 LLM API Key 即是唯一身份认证。

本指南介绍如何安装 KinetAios,并使用 **DeepSeek Harness** 引擎(或在 Direct 引擎中使用 DeepSeek 模型)接入你的 DeepSeek API Key。

> DeepSeek 已于 2026 年 4 月更名模型。本指南使用当前名称 **deepseek-v4-pro** / **deepseek-v4-flash**(而非已废弃的 `deepseek-chat` / `deepseek-reasoner`)。DeepSeek V4 支持最高 **100 万 token** 上下文。

---

#### 1. 安装 KinetAios

从 [releases 页面](https://github.com/phinn/KinetAios/releases/latest)下载最新版本:

- **Windows** —— `KinetAios-Setup-3.3.0.exe`(NSIS 安装包)
- **macOS** —— 见 releases

> 该构建未签名,Windows SmartScreen / macOS Gatekeeper 会弹出警告,手动放行即可。

也可以从源码运行(需要 **Node.js 18+**,以及用于编译 `better-sqlite3` 原生模块的网络连接):

```sh
git clone https://github.com/phinn/KinetAios.git
cd KinetAios/KinetAiosWin
npm install      # postinstall 会针对 Electron 重新编译 better-sqlite3
npm run build
npm start
```

> 在国内网络环境下,`npm install` 拉取 Electron 二进制可能超时。仓库的 `.npmrc` 已配置 npmmirror 镜像;若失败可执行:
> `ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ node node_modules/electron/install.js`

---

#### 2. 获取 DeepSeek API Key

1. 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)。
2. 创建 API Key 并复制。

---

#### 3. 配置 DeepSeek 供应商

1. 启动 KinetAios。
2. 点击右上角 **⚙** → **Settings** → **API**。
3. 选择 **DeepSeek** 预设(OpenAI 兼容),会自动填充:
   - **Base URL**:`https://api.deepseek.com`
   - **Model**:`deepseek-v4-pro`(需要更快、更便宜的选项时用 `deepseek-v4-flash`)
4. 在 **API Key** 中粘贴你的 DeepSeek Key。
5. 点击 **Test connection**,通过后即配置完成。

> KinetAios 通过 Electron `safeStorage`(macOS Keychain / Windows DPAPI)在本地加密存储 Key。不经过任何中转服务器 —— Key 不会离开你的机器。

> **100 万上下文**:DeepSeek V4 支持最高 1,000,000 token 上下文。在 KinetAios 中,可在上下文检查器(⚙ → Behavior,或会话级模型下拉)中设置每会话上下文预算以利用完整窗口。若保持默认,自动压缩循环仍会通过摘要早期对话来保持历史在预算之内。

> **最大思考强度**:DeepSeek V4 Pro 支持 `max` 推理强度。在 Direct 引擎中使用 OpenAI 兼容端点时,KinetAios 会在请求体中发送 `reasoning_effort`;在会话级模型设置中选择 `max` 级别以获得最佳编程体验。详见[思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。

---

#### 4. 首次运行

KinetAios 通过两种引擎接入 DeepSeek,可按会话切换:

- **Direct 引擎 + DeepSeek 模型** —— 使用内置 ReAct 循环(Direct V1/V2/V3)并以 DeepSeek 作为 LLM。最适合工具密集型任务(shell、read/write/edit file、grep、glob、web_fetch、web_search、memory…)。
- **DeepSeek Harness 引擎**(v3.0+) —— 以 OpenAI 兼容 SSE 流式方式启动 `dsh` CLI,内置 OpenAI / Pi-AI provider 适配器,自动重试与 token 计量。

**开始一个任务:**

1. 在侧边栏点击 **＋** 新建会话。
2. 在聊天输入框中,从下拉选择引擎(Direct 或 DeepSeek Harness)。
3. 确认模型已设为 `deepseek-v4-pro`(或 `deepseek-v4-flash`)。
4. 输入任务,例如:

```
列出当前目录下的文件,并概述这个项目是做什么的。
```

KinetAios 会执行工具、流式输出回答,并自动将持久事实抽取到长期记忆,供下一轮对话使用。

---

#### 5. 功能亮点

- **一窗口四引擎** —— Direct V1/V2/V3 + Claude Code + Codex + DeepSeek Harness
- **跨引擎长期记忆** —— SQLite + FTS5 + 语义召回,一份用户画像贯通所有引擎
- **20+ 内置工具** —— `shell`、`read_file`、`write_file`、`edit_file`、`grep`、`glob`、`web_fetch`、`web_search`、`recall_memory`、`dispatch_agent`、`team_broadcast`…
- **MCP 客户端 + 内置 MCP Server** —— 自动发现 Claude Code / Codex 的 MCP 配置;内置 Server 暴露 `run_agent` 供远程调用
- **Skills / Commands / Agents 自动扫描** —— Claude Code + Codex 的 skills 可通过 `/` 菜单调用
- **插件 SDK v3** —— 插件可贡献工具、斜杠命令、钩子与全屏面板
- **多模态** —— 图片输入、语音转写、实时语音对话、截图
- **Pipeline** —— 跨引擎编排,每阶段可指定引擎 + prompt
- **会话分支与导入导出** —— 从任意轮分支;完整状态序列化便于跨机器交接
- **本地优先,无需账号**

---

## 相关链接

- 仓库:<https://github.com/phinn/KinetAios>
- 官网:<https://phinn.github.io/KinetAios/>
- Releases:<https://github.com/phinn/KinetAios/releases/latest>
- DeepSeek 开放平台:<https://platform.deepseek.com/>
- DeepSeek API 文档:<https://api-docs.deepseek.com/zh-cn/>
