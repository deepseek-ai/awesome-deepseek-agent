# 集成泰深

泰深（Taishen）是一款专为 DeepSeek 深度优化的桌面 AI 工作台——一个完整的 GUI 应用（Electron），能将你的资料和想法直接转化为可交付的结构化产出，而非仅仅聊天。内置 Commander 形态智能体引擎，支持自主规划、子代理调度、IM 远程接入（飞书/微信/QQ），以及基于开放标准（agentskills.io Skills + MCP）的扩展生态。

- **GitHub:** [https://github.com/EricXu20266/taishen](https://github.com/EricXu20266/taishen)

#### 1. 安装泰深

从 [GitHub Releases](https://github.com/EricXu20266/taishen/releases) 下载最新版本：

- **Windows:** `taishen_setup_x.x.x.exe`（安装包，推荐）或 `taishen_x.x.x免安装.zip`（解压即用）
- **macOS:** `taishen_x.x.x.dmg`

> **系统要求：** Windows 10+ / macOS 12+，8 GB 内存，500 MB 磁盘空间。

安装后启动泰深，首次启动将显示设置面板。

#### 2. 配置 DeepSeek

泰深以 DeepSeek 为主要且经过最完整测试的模型供应商。所有配置通过 GUI 完成——无需编辑配置文件。

**添加 API Key：**

1. 打开 **设置**（侧边栏齿轮图标）。
2. 在 **Provider 配置** 中，DeepSeek 已预配置——直接粘贴你的 API Key 即可。
3. 从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**模型选择：**

泰深内置了对两种 DeepSeek V4 模型的精细调校：

| 模型 | 适用场景 | 上下文 | 推理 |
|------|----------|--------|------|
| `deepseek-v4-pro` | 深度研究、论文写作、代码开发 | 1M tokens | Max 级别（已启用） |
| `deepseek-v4-flash` | 日常问答、轻量任务 | 1M tokens | High 级别（已启用） |

两个模型均默认配置 `context_window: 1000000` 和 `max_tokens: 384000`。推理强度映射将泰深的思考级别选择器直接对应到 DeepSeek 的 `reasoning_effort` 参数（`xhigh` → `max`，`high` → `high`）。

**定价（每百万 token，人民币）：**

泰深内置了与 DeepSeek 官方同步的定价表。你可以在设置中自行编辑单价，费用按会话实时统计。

| 模型 | 缓存命中 | 缓存未命中 | 输出 |
|------|----------|------------|------|
| `deepseek-v4-pro` | ¥0.025 | ¥3 | ¥6 |
| `deepseek-v4-flash` | ¥0.02 | ¥1 | ¥2 |

**峰谷定价（v1.1）：** 泰深支持 DeepSeek 的峰谷定价策略。在高峰时段（北京时间工作日 09:00–12:00 和 14:00–18:00），自动应用可配置倍率（默认 2×）。峰谷定价默认启用，可在设置中开关。

**可选供应商：**

泰深还支持 OpenAI、Mimo 及其他 OpenAI 兼容接口。你也可以使用 **FlexDog**——内置子代理，可在同一会话中动态切换模型——在同一对话中对比 DeepSeek 与其他供应商的效果。

#### 3. 首次使用

配置好 API Key 后：

1. 返回主聊天界面。
2. 输入需求或直接拖入文件（`.docx`、`.pdf`、`.pptx`、`.xlsx`、图片均可）。
3. 泰深的 Commander 智能体将自主完成：规划 → 执行 → 验证 → 交付。

**试试复杂任务**来体验完整工作流——让泰深研究一个话题、撰写报告、生成 PPT、或跨多个文件重构代码。右侧面板实时展示每个阶段的进展。

#### DeepSeek 专项优化

泰深包含多项针对 DeepSeek 的深度优化，这些是一般通用客户端不具备的：

**缓存优化的 Prompt 架构**——系统提示词和工具定义经过专门设计，最大化利用 DeepSeek 的前缀缓存机制。在超长会话（两亿+ token）中，缓存命中率稳定在 ~99%，每轮成本不随会话长度增长。

**DeepSeek 原生思考格式**——泰深原生使用 `deepseek` 思考格式，在 assistant 消息上正确回传 `reasoning_content`。无需任何 workaround——思考模式开箱即用。

**1M 上下文默认开启**——`deepseek-v4-pro` 和 `deepseek-v4-flash` 均配置了完整 1M 上下文窗口。长文档、大型代码库、马拉松式会话均为原生支持。

**成本透明**——会话头部实时显示 token 用量和预估费用。缓存命中节省的 token 单独统计，可直观看到 Prompt 优化的实际效果。

#### 核心能力（DeepSeek 驱动）

- **Commander 智能体引擎**——五阶段工作流（Plan → Todo → Execute → Verify → Done），自主编排工具链。AI 读取文件、执行 Shell 命令、搜索网络，并自我验证产出质量。
- **IM 远程接入**——通过飞书、微信或 QQ 连接。手机即刻变成泰深终端，流式回复、文件传输、审批弹窗全部打通——全部经由 DeepSeek。
- **子代理调度**——同时派发最多 3 个子代理并行工作：代码探索、架构设计、内容创作等。每个子代理拥有独立的 Skill 集、记忆和 MCP 工具。
- **Skill 技能生态**——兼容 [agentskills.io](https://agentskills.io/) 开放标准（Claude Code、Cursor、GitHub Copilot 等 35+ 工具通用）。从 GitHub/Gitee 安装社区 Skill，或让 AI 自主创建新 Skill。
- **MCP 协议**——通过 Streamable HTTP、SSE 或 stdio 接入外部工具（网页搜索、浏览器自动化、学术数据库）。
- **文档全流程**——拖入 Word、PDF、PPT、Excel 文件；AI 阅读、分析，并生成任意格式的新文档。
- **三级沙箱安全**——L1（每步审批）→ L2（自动审查，默认）→ L3（完全信任）。所有文件编辑自动备份；所有 Shell 命令执行前标注风险等级。
