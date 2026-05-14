[English](./snow-cli.md) | [简体中文](./snow-cli.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 Snow CLI

[Snow CLI](https://github.com/MayDay-wpf/snow-cli)（npm 包名：`snow-ai`）是一款开源的终端 AI 编程助手，基于 Ink/React 构建终端 UI，内置丰富的 LLM 适配器、MCP 风格工具、本地离线代码库，并提供完整的 VSCode 与 JetBrains 插件。

- **GitHub：** <https://github.com/MayDay-wpf/snow-cli>
- **npm：** <https://www.npmjs.com/package/snow-ai>
- **VSCode 扩展：** [mufasa.snow-cli](https://marketplace.visualstudio.com/items?itemName=mufasa.snow-cli)
- **JetBrains 插件：** [Snow CLI 插件](https://plugins.jetbrains.com/plugin/28715-snow-cli)

## 核心特性

- **支持 DeepSeek 全部 API 请求方案** —— 内置 OpenAI Chat Completion、OpenAI Responses、Anthropic、Gemini 四种请求适配器，可任选 DeepSeek 兼容端点接入（包括原生 `https://api.deepseek.com` 与 `https://api.deepseek.com/anthropic` Anthropic 兼容端点）。
- **完整的 VSCode 与 JetBrains 插件** —— 通过 WebSocket 与 CLI 同步编辑器上下文、诊断信息、代码导航、终端面板、Git Blame 以及 Commit Message 生成。
- **本地离线代码库** —— 基于 SQLite 的向量检索数据库，可索引源代码与注释，并支持 Agent Review 或 Rerank 模型对结果二次排序，索引完成后可完全离线使用。
- **Agent 工具生态** —— 内置文件系统、终端执行、网页搜索、TODO、Notebook、调度器、IDE 诊断、子 Agent、Skills、ACE Code Search / LSP 等 MCP 风格工具。
- **多种运行模式** —— 交互式 TUI、`--ask` 无头模式、`--task` 后台任务、SSE 服务器、ACP 服务器、YOLO 与 Plan 模式。

#### 1. 安装 Snow CLI

需要 Node.js 18+（推荐 Node 22）。

```sh
npm install -g snow-ai
```

验证安装：

```sh
snow --version
```

> 提示：Windows 用户推荐使用 PowerShell 7+ 搭配 Windows Terminal，获得最佳渲染效果。

#### 2. 配置 DeepSeek

运行 `snow` 启动 TUI，进入 **API 和模型设置**（`/home` → API and Model Settings），按以下任一方案填写。Snow CLI 提供四种请求方式，可按需选择 DeepSeek 端点。

##### 方案 A —— DeepSeek 原生（OpenAI Chat Completion）

| 配置项             | 值                         |
| ------------------ | -------------------------- |
| **请求方式**       | `OpenAI Chat Completion`   |
| **Base URL**       | `https://api.deepseek.com` |
| **API Key**        | `<你的 DeepSeek API Key>`  |
| **Advanced Model** | `deepseek-v4-pro`          |
| **Basic Model**    | `deepseek-v4-flash`        |

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

##### 方案 B —— DeepSeek Anthropic 兼容端点

| 配置项                     | 值                                   |
| -------------------------- | ------------------------------------ |
| **请求方式**               | `Anthropic`                          |
| **Base URL**               | `https://api.deepseek.com/anthropic` |
| **API Key**                | `<你的 DeepSeek API Key>`            |
| **Advanced Model**         | `deepseek-v4-pro[1m]`                |
| **Basic Model**            | `deepseek-v4-flash[1m]`              |
| **Thinking Enabled**       | `true`（推荐 v4-pro 开启）           |
| **Thinking Budget Tokens** | `10000` 起，越大推理越深             |


##### 方案 C —— DeepSeek OpenAI Responses

| 配置项                          | 值                                  |
| ------------------------------- | ----------------------------------- |
| **请求方式**                    | `OpenAI Responses`                  |
| **Base URL**                    | `https://api.deepseek.com`          |
| **API Key**                     | `<你的 DeepSeek API Key>`           |
| **Responses Reasoning Enabled** | `true`                              |
| **Responses Reasoning Effort**  | `HIGH` 或 `XHIGH`，获得最佳编程体验 |

> 建议：将 reasoning effort 设为 `HIGH` / `XHIGH`，让模型在长编码任务中使用 **最大思考强度**。

#### 3. 启用本地离线代码库（可选）

Snow CLI 自带基于 SQLite 的向量检索代码库。先在 `/home` → **Codebase Config** 中配置 DeepSeek 兼容的 Embedding 端点，然后在项目内启用：

```text
/codebase on        # 当前项目启用
/codebase status    # 查看状态
/codebase off       # 关闭
```

- 项目级配置位于 `.snow/codebase.json`（索引参数、Agent Review、Rerank）。
- 全局配置位于 `~/.snow/codebase.json`（Embedding 服务，多项目共享）。
- 索引完成后，语义检索完全在本地 SQLite 中**离线**执行。

#### 4. 启动 Snow CLI

```sh
cd /path/to/my-project
snow
```

其他常用入口：

```sh
# 一次性无头对话
snow --ask "explain this project"

# 继续上一次会话
snow -c

# 后台异步任务
snow --task "review the authentication module"
snow --task-list

# SSE / ACP 服务模式（用于 IDE 与外部集成）
snow --sse --sse-port 3000
snow --acp
```

#### 5. 安装 IDE 插件（可选）

- **VSCode：** 在扩展商店搜索 "Snow CLI"，或安装 [`mufasa.snow-cli`](https://marketplace.visualstudio.com/items?itemName=mufasa.snow-cli)。扩展会在侧边栏 / 分屏中嵌入 Snow 终端，并实时将编辑器上下文、诊断信息、选区推送给 Agent。
- **JetBrains：** 在 JetBrains Marketplace 安装 [Snow CLI](https://plugins.jetbrains.com/plugin/28715-snow-cli)，可在 IntelliJ IDEA、PyCharm、GoLand、WebStorm 等中使用同样的上下文桥接能力。

#### 快捷键（部分）

| 按键          | 功能                |
| ------------- | ------------------- |
| `Enter`       | 发送消息            |
| `Shift+Enter` | 换行                |
| `Esc`         | 中断当前模型回复    |
| `/`           | 打开命令 / 技能菜单 |
| `/clear`        | 开始新对话          |
| `/resume`     | 恢复历史会话        |
| `/codebase`   | 切换本地代码库索引  |
| `/quit`       | 退出 Snow CLI       |

#### 用户配置目录

首次运行后，Snow CLI 会在用户主目录创建 `~/.snow/`，包含 `config.json`、`mcp-config.json`、profiles、sessions、异步任务、hooks 与运行日志。可通过多个 **Profile** 一键切换不同的 DeepSeek 端点或模型组合。

## 完整文档目录

Snow CLI 提供了完整的中英双语用户手册，所有文档位于 [官方仓库](https://github.com/MayDay-wpf/snow-cli/tree/main/docs/usage/zh)。

### 入门

- [01. 安装指南](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/01.%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.md) —— 系统要求、安装 / 更新 / 卸载、IDE 扩展安装
- [02. 首次配置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/02.%E9%A6%96%E6%AC%A1%E9%85%8D%E7%BD%AE.md) —— API 配置、模型选择、基础设置
- [19. 启动参数说明](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/19.%E5%90%AF%E5%8A%A8%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E.md) —— 命令行参数详解、快速启动模式、无头模式、异步任务、开发者模式

### 高级配置

- [03. 代理和浏览器设置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/03.%E4%BB%A3%E7%90%86%E5%92%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E8%AE%BE%E7%BD%AE.md) —— 网络代理配置、浏览器使用设置
- [04. 代码库设置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/04.%E4%BB%A3%E7%A0%81%E5%BA%93%E8%AE%BE%E7%BD%AE.md) —— 本地离线代码库、向量检索、Agent Review、Rerank
- [05. 子代理设置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/05.%E5%AD%90%E4%BB%A3%E7%90%86%E8%AE%BE%E7%BD%AE.md) —— 子代理管理、自定义子代理
- [06. 敏感命令配置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/06.%E6%95%8F%E6%84%9F%E5%91%BD%E4%BB%A4%E9%85%8D%E7%BD%AE.md) —— 敏感命令保护、自定义命令规则
- [07. Hooks 配置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/07.Hooks%E9%85%8D%E7%BD%AE.md) —— 工作流自动化、Hook 类型、实用示例
- [08. 主题设置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/08.%E4%B8%BB%E9%A2%98%E8%AE%BE%E7%BD%AE.md) —— 界面主题、自定义配色、简洁模式
- [16. 第三方中转配置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/16.%E7%AC%AC%E4%B8%89%E6%96%B9%E4%B8%AD%E8%BD%AC%E9%85%8D%E7%BD%AE.md) —— Claude Code 中转、Codex 中转、自定义请求头

### 功能指南

- [09.0 指令面板说明](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.0.%E6%8C%87%E4%BB%A4%E9%9D%A2%E6%9D%BF%E8%AF%B4%E6%98%8E.md) —— 所有指令的详细说明、使用技巧（按类目拆分为 09.1~09.7 子文档）：
  - [09.1 会话管理指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.1.%E4%BC%9A%E8%AF%9D%E7%AE%A1%E7%90%86%E6%8C%87%E4%BB%A4.md)
  - [09.2 模式切换指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.2.%E6%A8%A1%E5%BC%8F%E5%88%87%E6%8D%A2%E6%8C%87%E4%BB%A4.md)
  - [09.3 代码审查与分析指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.3.%E4%BB%A3%E7%A0%81%E5%AE%A1%E6%9F%A5%E4%B8%8E%E5%88%86%E6%9E%90%E6%8C%87%E4%BB%A4.md)
  - [09.4 配置与管理指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.4.%E9%85%8D%E7%BD%AE%E4%B8%8E%E7%AE%A1%E7%90%86%E6%8C%87%E4%BB%A4.md)
  - [09.5 自定义扩展指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.5.%E8%87%AA%E5%AE%9A%E4%B9%89%E6%89%A9%E5%B1%95%E6%8C%87%E4%BB%A4.md)
  - [09.6 特殊指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.6.%E7%89%B9%E6%AE%8A%E6%8C%87%E4%BB%A4.md)
  - [09.7 目标管理指令](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/09.7.%E7%9B%AE%E6%A0%87%E7%AE%A1%E7%90%86%E6%8C%87%E4%BB%A4.md)
- [10. 命令注入模式](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/10.%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5%E6%A8%A1%E5%BC%8F.md) —— 消息中直接执行命令、语法、安全机制
- [11. 漏洞猎人模式](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/11.%E6%BC%8F%E6%B4%9E%E7%8C%8E%E4%BA%BA%E6%A8%A1%E5%BC%8F.md) —— 专业安全分析、漏洞检测、验证脚本、详细报告
- [12. 无头模式](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/12.%E6%97%A0%E5%A4%B4%E6%A8%A1%E5%BC%8F.md) —— 命令行快速对话、会话管理、脚本集成
- [13. 快捷键指南](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/13.%E5%BF%AB%E6%8D%B7%E9%94%AE%E6%8C%87%E5%8D%97.md) —— 编辑操作、导航控制、回滚功能
- [14. MCP 配置](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/14.MCP%E9%85%8D%E7%BD%AE.md) —— MCP 服务管理、启用 / 禁用、故障排查
- [15. 异步任务管理](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/15.%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E7%AE%A1%E7%90%86.md) —— 后台任务、任务面板、敏感命令审批、任务转会话
- [17. LSP 配置与用法](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/17.LSP%E9%85%8D%E7%BD%AE.md) —— LSP 配置文件、语言服务器安装、ACE 工具用法（跳转 / 大纲）
- [18. Skills 指令详细说明](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/18.Skills%E6%8C%87%E4%BB%A4%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.md) —— 技能创建、Claude Code Skills 兼容、工具限制
- [20. SSE 服务模式](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/20.SSE%E6%9C%8D%E5%8A%A1%E6%A8%A1%E5%BC%8F.md) —— SSE 服务器、API 端点、工具确认流程、YOLO 模式、客户端集成
- [21. 自定义 StatusLine 指南](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/21.%E8%87%AA%E5%AE%9A%E4%B9%89StatusLine%E6%8C%87%E5%8D%97.md) —— 用户级状态栏插件、hook 结构、中英文示例
- [22. Team 模式指南](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/22.Team%E6%A8%A1%E5%BC%8F%E6%8C%87%E5%8D%97.md) —— 多智能体协作、并行任务执行、团队管理
- [23. 自定义搜索引擎指南](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/zh/23.%E8%87%AA%E5%AE%9A%E4%B9%89%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E%E6%8C%87%E5%8D%97.md) —— 用户级搜索引擎插件、引擎合约、最小模板
