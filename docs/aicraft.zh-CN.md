[English](./aicraft.md) | [简体中文](./aicraft.zh-CN.md) · [← Back](../README.md)

# 接入 AICraft

AICraft 是一个桌面 AI 能力启动器——通过可视化界面管理 LLM 的 Skill、MCP 工具、RAG 和记忆模块，像加载 Minecraft 模组一样简单。

**核心亮点：**
- 🚀 DeepSeek 一键接入——粘贴 API Key 即可开聊
- 🧩 模块化架构——Skill（提示词）+ MCP（工具）+ RAG（知识库）+ 记忆
- 💰 实时 Token 计费面板，缓存命中单独统计
- 🤖 上下文预算管理——6 级优先级裁剪，充分利用 1M 上下文

### 安装

#### 方式一：下载 Release（推荐）

1. 前往 [AICraft Releases](https://github.com/Easlie114514/AICraft/releases)
2. 下载最新的 `AICraft-x.x.x.zip`
3. 解压后运行 `AICraft.exe`

无需安装 Python、Node.js 或任何其他运行时环境。

#### 方式二：从源码运行

前置条件：Python 3.7+、Node.js 18+

```bash
git clone https://github.com/Easlie114514/AICraft.git
cd AICraft
pip install -r requirements.txt
cd frontend && npm install && npm run build && cd ..
python run.py
```

### 配置 DeepSeek

AICraft 提供 DeepSeek 一键接入功能，无需手动编辑配置文件。

1. 启动 AICraft
2. 点击顶部导航栏的 **「模型」** 选项卡
3. 点击 **「DeepSeek 一键接入」**
4. 粘贴你的 DeepSeek API Key（从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取）
5. 点击 **「保存」**

<div align="center">
<img src="./assets/aicraft_deepseek.png" width="600" />
</div>

系统会自动创建两个模型配置：

| 模型 | 适用场景 | 上下文窗口 |
|------|---------|-----------|
| `deepseek-v4-pro` | 复杂推理、编程、深度分析 | 1M tokens |
| `deepseek-v4-flash` | 快速响应、日常对话 | 1M tokens |

两个模型均使用 OpenAI 兼容端点 `https://api.deepseek.com/`。

### 1M 上下文窗口

DeepSeek V4 模型支持最高 **100 万 tokens** 的上下文。AICraft 充分利用了这一能力：

- **上下文预算管理器**——6 级优先级裁剪，在接近上限时保留最重要的上下文
- **Auto 路由**——根据任务复杂度自动切换 V4 Pro（复杂任务）和 V4 Flash（简单查询）
- **记忆注入**——跨会话记忆按优先级注入上下文，防止记忆溢出

### 深度思考模式

AICraft 支持 DeepSeek 的深度思考模式：

1. 在聊天输入框底部打开 **「深度思考」** 开关
2. 模型会在回复前进行扩展推理
3. 思考内容以可折叠区块展示

为获得最佳体验，开启深度思考时 AICraft 会发送 `reasoning_effort: max`，充分发挥 DeepSeek V4 Pro 的推理能力。

### Token 计费面板

AICraft 内置实时 Token 计费面板，可追踪：

- 输入 tokens（缓存命中 / 缓存未命中分别统计）
- 输出 tokens
- 请求次数
- 预估费用（美元）

定价按模型名前缀自动匹配：

| 模型 | 输入 / 百万 tokens | 缓存命中 / 百万 tokens | 输出 / 百万 tokens |
|------|-------------------|---------------------|-------------------|
| `deepseek-v4-pro` | $0.435 | $0.003625 | $0.87 |
| `deepseek-v4-flash` | $0.14 | $0.0028 | $0.28 |

*定价数据来源于 [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)，请以官方最新数据为准。*

### 开始使用

1. 启动 AICraft
2. 配置 DeepSeek（见上文）
3. 根据需要切换输入框下方的 **RAG**、**记忆**、**深度思考** 开关
4. 开始对话！

<div align="center">
<img src="./assets/aicraft_chat.png" width="600" />
</div>

### 能力模块

| 模块 | 说明 | 出厂预置 |
|------|------|---------|
| **Skill** | 角色风格 prompt 注入 | 4 个：通用 / 技术 / 创作 / 分析 |
| **MCP** | 可执行工具（文件管理 + Python 执行） | 2 个：filesystem / code_executor |
| **RAG** | 本地向量检索（ChromaDB） | 3 篇：使用手册 / 开发指南 / FAQ |
| **记忆** | 三层架构（L0 实时 → L1 短期 → L2 长期） | 自动运行 |
| **角色** | 预设人格模板 | 自由创建 |

### 技术栈

- **后端**：Python · FastAPI · ChromaDB · httpx
- **前端**：React 19 · Vite 8 · TailwindCSS 4 · Shadcn UI
- **打包**：PyInstaller onedir · 316 MB
- **协议**：Apache 2.0
