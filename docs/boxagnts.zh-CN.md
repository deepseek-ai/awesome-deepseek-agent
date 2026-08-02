# BoxAgnts


BoxAgnts 是一个基于 Rust 构建的开源 AI Agent ToolBox，专注于开箱即用（Out of the Box）的极致体验。它利用 WebAssembly 沙箱（Sandbox）提供兼顾安全与灵活的运行环境，帮助用户轻松处理各种复杂任务，进而成为高效、可信赖的个人智能助理。

## 核心架构

### 🎯 AI Agent Tool**Box**

BoxAgnts 是一个功能完备的 AI Agent 工具箱，提供：

- **多模型支持**：兼容 OpenAI、Anthropic、CodeX、Google、Deepseek、MiniMax、OpenCode 等主流 AI 模型提供商
- **工具系统**：内置文件操作、Web 访问、代码执行等多种工具
- **技能系统**：通过简单的配置即可创建专用 AI 技能

### 🛡️ WebAssembly Sand**Box**

利用 WebAssembly 技术构建安全的运行环境：

- **隔离执行**：所有自定义工具和技能在 WASM 沙箱中运行
- **安全控制**：精细的权限管理和网络访问控制
- **跨平台**：一次编译，多平台运行
- **高性能**：基于 Wasmtime 运行时，接近原生性能

### ✨ Out of the **Box**

开箱即用的极致体验：

- **零配置启动**：下载即可运行，无需复杂配置
- **Web 界面**：内置美观的 Dashboard，可视化管理所有功能
- **内置扩展**：预置常用工具和技能，直接可用
- **快速上手**：简洁的 API 和直观的操作流程

## 主要功能

### 🤖 AI 对话与智能代理（Agents）
- 与多种 AI 模型进行流式对话（支持 20+ 供应商）
- 创建和管理自定义 Agents，每个 Agent 可独立配置模型、提示词和最大轮次
- 保存和管理完整的对话历史记录
- MD 文件驱动 Agent（支持通过 `.md` 文件定义 Agent 行为）

### 🔧 工具执行
- 文件读写与智能编辑（diff 级别修改）
- Shell 命令安全执行（含命令风险解析与分类）
- Web 内容抓取与 HTTP 请求
- 文档读取（PDF、DOCX 等）
- 文件搜索（通配符匹配 + 正则内容搜索）

### 📦 技能系统（Skills）
- 通过 Markdown 文件快速创建专用技能
- 技能组合与复用
- 内置技能：代码审查（code-review）、CSS 重构顾问、DOCX/PPTX/XLSX 生成器、文件压缩、前端组件生成等

### ⏰ 定时任务（Cron）
- 创建和管理定时任务，支持标准 Cron 表达式
- 任务自动执行并记录日志
- 灵活的任务配置：可指定 Agent、消息内容和工作目录

### 🌐 Web 服务
- 自定义静态网站部署与托管
- 自定义 API 端点管理
- 文件系统实时浏览

### 🔌 MCP 协议支持
- 连接外部 MCP（Model Context Protocol）服务
- 通过 MCP 扩展 AI 工具和资源访问能力

### 🛡️ 安全与权限
- WebAssembly 沙箱隔离执行
- 网络访问控制（域名白名单 + IP 黑名单）
- HTTP Basic Auth 认证保护 Dashboard

## 快速上手

### 下载可执行文件

从 [Releases](https://github.com/guyoung/boxagnts/releases) 页面下载最新版本的压缩包文件，解压后即可运行。

### 启动服务

```bash
# 启动服务
boxagnts

# 指定工作空间目录
boxagnts --workspace-dir /path/to/workspace

# 指定端口
boxagnts --workspace-dir /path/to/workspace --port 30002
```

> 建议：BoxAgnts 支持多工作空间，每个工作空间都有自己的配置文件和数据目录，建议不要在默认目录下运行，而是指定一个工作空间目录，或者指定workspace-dir。

命令行参数：

```bash
BoxAgnts is an open-source AI Agent ToolBox built with Rust.

Usage: boxagnts [OPTIONS]

Options:
      --port <PORT>          Port to run the web server on [default: 30001]
      --host <HOST>          Host to bind to (0.0.0.0 for all interfaces) [default: 127.0.0.1]
      --workspace-dir <DIR>  Set workspace dir, default current dir
      --app-dir <DIR>        Set app dir, default Boxagnts executable file dir
      --admin-user <USERNAME>  Set admin username
      --admin-pass <PASSWORD>  Set admin password
  -h, --help                 Print help
  -V, --version              Print version
```

### 访问 Dashboard

打开浏览器访问 `http://127.0.0.1:30001/dashboard`

### 配置模型

在设置页面添加 AI 模型以及 API Key

## 项目结构与源代码编译

本项目是基于 [claurst](https://github.com/Kuberwastaken/claurst) 项目代码开发

### 目录结构

```
boxagnts-pub/
├── boxagnts/                 # Rust 后端核心代码
│   ├── api/                 # 多供应商 AI 模型 API 适配层
│   ├── core/                # 核心类型、常量、错误处理与成本追踪
│   ├── gateway/             # API 网关（含 Cron 任务调度 + 站点管理）
│   ├── mcp/                 # MCP 协议客户端实现
│   ├── query/               # Agent 查询编排引擎（查询循环、上下文压缩）
│   ├── server/              # Web 服务器（Axum REST API + WebSocket）
│   ├── tools/               # 工具系统（Tool trait + 内置工具）
│   ├── tools-manager/       # 工具管理器（Shell 命令解析器等）
│   ├── wasm-sandbox/        # WebAssembly 沙箱运行时（Wasmtime）
│   ├── wasm-tools/          # WASM 工具注册、解析与执行封装
│   └── workspace/           # 工作空间管理（配置/认证/历史记录）
├── boxagnts-dashboard-web/  # Vue 3 前端源码
│   ├── src/
│   │   ├── api/            # API 接口封装与类型定义
│   │   ├── components/     # 通用 Vue 组件
│   │   ├── composables/    # 组合式函数（聊天/滚动/会话/Markdown）
│   │   ├── stores/         # Pinia 状态管理（11 个业务 Store）
│   │   ├── views/          # 页面组件（13 个页面）
│   │   ├── types/          # TypeScript 类型导出
│   │   └── router/         # Vue Router 路由配置
│   └── package.json        # 前端依赖配置
├── app/                     # 应用资源
│   ├── dashboard-web/      # 编译后的 Web 界面静态资源
│   └── extensions/         # 内置扩展（WASM 工具 + 技能定义）
├── docs/                    # 文档
├── examples/                # 示例（WASM 工具开发示例）
├── Cargo.toml              # Rust 工作区配置
└── Cargo.lock              # 依赖锁定文件
```

### 后端代码分析

后端采用 Rust 语言开发，使用 Tokio 异步运行时和 Axum Web 框架，主要模块如下：

- **api/**：多供应商适配层。封装了 OpenAI、Anthropic、Google、Azure、Bedrock、DeepSeek、MiniMax、Cohere、GitHub Copilot 等 20+ 个 AI 提供商的 API，提供统一的接口调用和流式/非流式消息格式转换
- **core/**：核心层。定义核心数据类型（Message、ContentBlock、ToolDefinition 等）、常量、错误处理、成本追踪和系统提示词
- **gateway/**：API 网关层。处理业务逻辑路由，包含 Cron 定时任务调度系统（cron/ 子目录）和用户自定义站点管理（site/ 子目录）
- **mcp/**：MCP（Model Context Protocol）协议客户端实现，支持连接外部 MCP 服务以扩展工具能力
- **query/**：查询编排引擎。实现 Agent 核心查询循环，包含多供应商动态路由、工具调用循环、流式响应处理、上下文自动压缩、预算控制等功能
- **server/**：Web 服务器层。基于 Axum 提供 Dashboard 的 REST API 和 WebSocket 支持，包含 HTTP Basic Auth 安全认证
- **tools/**：工具系统。定义统一的 Tool trait 接口和内置工具（文件操作、Shell 命令、MCP 资源、技能调用、计划模式等）
- **tools-manager/**：工具管理器。包含 Bash 工具的完整 Shell 命令解析器（词法分析器 + 语法分析器 + AST）
- **wasm-sandbox/**：WebAssembly 沙箱运行时。基于 Wasmtime 实现安全的隔离执行环境，支持目录映射、网络访问控制、资源限制（超时/内存/Fuel）
- **wasm-tools/**：WASM 工具封装。提供 WASM 组件的注册、解析、参数校验和执行封装
- **workspace/**：工作空间管理。处理配置文件、OAuth 认证、会话历史记录存储和权限管理

### 前端代码分析

前端采用 Vue 3 + TypeScript + Vuetify 技术栈：

- 使用 **Pinia** 进行状态管理，stores/ 目录包含 11 个业务 Store（会话、文件、Agent、技能、工具、Cron、站点、MCP、用量、设置、全局状态），均继承自 `baseCrud` 泛型基类
- 使用 **Vue Router** 进行路由管理（Hash 模式，router/ 目录）
- 主要页面：聊天主页、首页、Agents 管理、技能管理、工具列表、Cron 定时任务、站点管理、MCP 服务、用量统计、设置（模型/API端点/安全/Agents.md）等
- 支持 Markdown 渲染（Marked + DOMPurify）、代码编辑器（CodeMirror 6）、图表（Chart.js + vue-chartjs）等功能
- 与后端通过 REST API 和 WebSocket 进行双向通信，支持流式消息实时推送和文件变更通知

### 源代码编译方法

#### 环境要求

- Rust 1.75+（安装：https://www.rust-lang.org/tools/install）
- Node.js 18+（安装：https://nodejs.org/）
- npm 或 pnpm

#### 编译后端

```bash
# 进入项目根目录
cd boxagnts-pub

# 编译 Debug 版本
cargo build

# 编译 Release 版本（优化体积和性能）
cargo build --release

# 编译后的可执行文件位于 target/release/boxagnts
```

#### 编译前端

```bash
# 进入前端目录
cd boxagnts-dashboard-web

# 安装依赖
npm install

# 开发模式启动（热重载）
npm run dev

# 编译生产版本
npm run build

# 编译后的静态文件会输出到 app/dashboard-web/
```

#### 完整构建流程

```bash
# 1. 编译前端
cd boxagnts-dashboard-web
npm install
npm run build

# 2. 编译后端
cd ..
cargo build --release

# 3. 运行
./target/release/boxagnts
```

## 许可证

MIT


---

**Repository**: [https://github.com/guyoung/boxagnts](https://github.com/guyoung/boxagnts)