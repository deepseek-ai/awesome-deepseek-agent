[English](./go-stock.md) | [简体中文](./go-stock.zh-CN.md) · [← Back](../README.zh-CN.md)
# 接入 go-stock
[go-stock](https://github.com/ArvinLovegood/go-stock) 是一款基于 Wails + Naive UI 的开源桌面股票分析工具，内置三种模式的 AI 智能体（React / 规划执行 / DeepAgents）与 150+ 金融数据工具，覆盖 A股/港股/美股行情、资金流向、龙虎榜、涨停梯队、知识库与定时复盘报告。
- **GitHub：** <https://github.com/ArvinLovegood/go-stock>
#### 1. 安装 go-stock
从 [go-stock Releases](https://github.com/ArvinLovegood/go-stock/releases) 下载对应平台的版本：
- Windows（`go-stock-windows-amd64.exe`，绿色免安装）
- macOS（`go-stock-darwin-universal`，支持 Intel 与 Apple Silicon）
也可以用 Go 1.27+、Node.js 与 Wails CLI 从源码构建：
```bash
wails build
```
#### 2. 配置 DeepSeek 模型服务
启动 go-stock，在左侧导航打开 **AI模型服务** 页面。
1. 点击 **+ 添加AI配置**，在 **接口地址** 下拉中选择 **DeepSeek (https://api.deepseek.com)** 预设，Base URL 自动填充。
2. 将 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 **令牌(apiKey)** 字段。
3. **模型名称** 填写 **`deepseek-v4-pro`**（或 **`deepseek-v4-flash`**）。可点击字段从 API 拉取实时模型列表，也可手动输入。
4. **上下文窗口** 保持 `0`（自动）即可。go-stock 内置模型参数表会自动识别 `deepseek-v4-*` 系列并应用完整的 **100 万 token** 上下文窗口与 384K 输出上限，无需手动配置。
5. 点击页面上方的 **保存配置**。
DeepSeek V4 默认开启深度思考，推理能力开箱即用，无需额外配置。（go-stock 暂未暴露 `reasoning_effort` 选择器，思考模式跟随 API 默认值。）
#### 3. 开始分析
打开悬浮 AI 助手，选择智能体模式：
- **快速模式（React）**：响应最快，推荐搭配 DeepSeek 最新版使用。
- **规划模式（Plan-Execute）**：先规划后逐步执行。
- **DeepAgents**：内置任务规划与子 Agent 委派，适合复杂多步分析。
然后直接用自然语言提问，例如"分析宁德时代的基本面和资金流向，给出明天的操作计划"。智能体会自主调用内置数据工具（行情、财务、资金流向、龙虎榜、涨停梯队、板块轮动等），生成有数据来源支撑的分析报告。
#### 4. 进阶用法
完成 DeepSeek V4 配置后，你可以在 go-stock 的其他场景中复用它：
- **定时报告**：启用每日复盘（18:00）与盘前策略（09:00）定时任务，DeepSeek 自动生成复盘报告与盘前计划，支持飞书 / 钉钉推送。
- **知识库与长期记忆**：基于本地知识库沉淀研究笔记；智能体长期记忆跨会话保留上下文（另建一条向量模型配置即可启用向量检索）。
- **MCP 服务**：通过 MCP 服务管理页接入外部 MCP 工具，扩展智能体能力。
- **视觉理解**：再添加一条模型名称为 `deepseek-v4-flash-vision-exp` 的配置并打开 **视觉理解** 开关，即可在对话中直接分析 K 线截图等图片。
> ⚠️ go-stock 仅供学习研究使用，AI 分析结果不构成投资建议，投资有风险，入市需谨慎。
