[English](./exo_agent.md) | [简体中文](./exo_agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Exo-agent

Exo-agent 是一个运行在浏览器中的自主 AI Agent，**单 HTML 文件**交付——零后端、全本地。内置 MCTS 深度规划、流水线引擎、心流模式、世界验证器、自进化系统与 45+ 内置工具。

- **GitHub：** <https://github.com/Xiyinnnnnn/Exo-agent>

#### 1. 打开 Agent

从仓库下载 `index.html`，用任意现代浏览器打开即可。无需安装——没有服务器、没有构建步骤。

#### 2. 在设置面板中配置 DeepSeek

打开设置面板，填写：

| 设置项 | 值 |
|--------|-----|
| Base URL | `https://api.deepseek.com` |
| 模型名称 | `deepseek-v4-flash`（或 `deepseek-v4-pro`） |
| API Key | 你的 DeepSeek API Key |

默认值已指向 `api.deepseek.com` 与 `deepseek-v4-flash`。内置约 100 万 token 的上下文预算（`_model_ctx` = 1048565），与 DeepSeek V4 的 **1M 上下文窗口**对齐，并提供压缩激进程度滑杆控制历史压缩时机。

#### 3. 开启 max 深度思考

在设置中将推理强度设为 `max`（或保持 `high`）。Exo-agent 会随请求发送 `thinking: {type: "enabled"}` 与所选 `reasoning_effort`，让 DeepSeek-V4-Pro 在规划密集型工作流中发挥完整推理能力。

#### 亮点

- **MCTS 深度规划** — 最多 600 次仿真，UCB1 + 信息素，收敛检测
- **流水线引擎 V6** — DAG 编排多子 Agent 并行协作，10 种节点类型、条件路由、错误降级边
- **心流模式** — 根 Agent → 监工 → 干活 Agent 三角模型，审查-修正闭环
- **世界验证器** — 多实体离散事件仿真，嵌套子状态、守卫条件
- **45+ 内置工具** — 搜索、文件系统、代码执行、图表、SQLite、OCR、PDF、邮件、语音、日历……
- **全本地** — 零后端，数据留在浏览器内
