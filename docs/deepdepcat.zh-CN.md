[English](./deepdepcat.md) | [简体中文](./deepdepcat.zh-CN.md) · [↩ 返回](../README.zh-CN.md)

# 集成 DeepDepCat

DeepDepCat 是一款一体化的 AI 桌面工作台（Tauri + React + Rust 原生应用），内置两个工作空间：**编码工作空间**——权限模式、子代理编排、多会话并行；**文档/办公自动化工作空间**——Word/PPT/Excel 生成、OCR、表格处理、媒体转换、网页抓取，附实时任务面板。两者均基于 DeepSeek V4，支持 1M 上下文与可调推理强度。

- **GitHub:** <https://github.com/hanmirage/deepdepcat>
- **平台:** Windows / macOS / Linux

#### 1. 安装 DeepDepCat

从 [releases 页面](https://github.com/hanmirage/deepdepcat/releases) 下载对应平台的安装包，或从源码构建：

```sh
git clone https://github.com/hanmirage/deepdepcat.git
cd deepdepcat
npm install
npm run tauri dev
```

#### 2. 配置 DeepSeek 提供商

打开 **设置 → 模型提供商**，选中内置的 **DeepSeek** 提供商（已预置）：

| 字段 | 值 |
|-------|-------|
| API Key | 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 `sk-...` |
| Base URL | `https://api.deepseek.com`（默认） |
| API 格式 | `OpenAI 兼容`（默认） |
| 模型 | 添加 `deepseek-v4-pro` 和/或 `deepseek-v4-flash`——模型选择器直接读取此列表 |

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

> **提示：** 新添加的模型默认使用 **1,000,000 token（1M）上下文窗口**——DeepSeek V4 支持最高 1M 上下文。可在提供商设置中按模型核对/调整该值。

#### 3. 开启深度思考

DeepSeek V4 Pro 支持多档推理强度。在 DeepDepCat 中：

- **设置 → 常规 →「DeepSeek 自动优化」**——开启后智能体默认使用 `max` 推理强度，获得最佳编码体验。
- **输入栏推理强度选择器**（Code 工作台）——按对话显式选择 `auto` / `high` / `max`；`auto` 跟随上方设置。

#### 4. 首次使用

- **Code 工作台**：输入任务（如"介绍一下这个仓库"），从输入栏选择交互模式（确认 / 计划 / 接受编辑 / 自动）与执行策略（标准 / 计划执行 / 反思优化 / 思维树 / 协调器）。
- **Depwork 工作台**：描述文档任务（如"根据这些笔记生成 Word 报告"）——右侧任务面板自动展开，实时显示步骤进度，可随时收起。

#### 核心特性

| 特性 | 说明 |
|---------|-------------|
| 双工作台 | 编码 + 文档/办公自动化一体化，各自独立工具集与系统提示词 |
| 多会话并行 | 会话间互不阻塞并发运行；侧边栏显示每个会话的实时运行状态与停止按钮 |
| 子代理编排 | 将复杂任务拆解为并行子代理，实时追踪活动状态 |
| 生态技能复用 | 直接复用现有 Agent 技能生态（Claude/Cursor 技能与插件布局，如 `~/.claude/skills`、`~/.cursor/skills`） |
| 1M 上下文 | 完整支持 DeepSeek V4 上下文窗口，输入栏实时显示上下文用量环 |
| 静默更新 | 小版本在后台自动下载、退出应用时自动安装，零打扰 |
| 沙箱与权限 | 按交互模式审批文件修改；可配置沙箱档案 |

#### 配置项（设置 → 模型提供商）

| 选项 | 说明 |
|--------|-------------|
| `baseUrl` | API 基础地址，默认 `https://api.deepseek.com` |
| `apiFormat` | `openai`（OpenAI 兼容）或 `anthropic` |
| `context_window` | 按模型设置的上下文窗口（token），DeepSeek V4 填 `1000000` |
| `reasoning_effort` | `auto` / `high` / `max`——控制模型回答前的思考深度 |

价格以官方 [DeepSeek 价格页面](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 为准。
