[English](./easy-stock.md) | [简体中文](./easy-stock.zh-CN.md) · [← Back](../README.zh-CN.md)

# 在 easy-stock 中接入 DeepSeek

easy-stock 是一套本地优先的 A 股 AI 智能投研桌面工作台，把行情总览、趋势题材雷达、连板梯队与情绪周期分析、个股 AI 报告、持仓巡检和大 V 复盘收集统一到一个应用里。AI Copilot（Hermes 运行时）使用你自己的 API Key 驱动，全部研究记忆保存在本机。

- **GitHub 仓库**：<https://github.com/jundizhou/easy-stock>
- **下载地址**：<https://github.com/jundizhou/easy-stock/releases/latest>

#### 1. 安装 easy-stock

前往 [Releases 页面](https://github.com/jundizhou/easy-stock/releases/latest) 下载对应系统的安装包（提供 Windows 与 macOS 版本），无需安装 Node.js、Go 或 Python。

#### 2. 配置 DeepSeek 模型

打开 **系统设置 → Hermes 模型运行时**，点击 **新增配置**：

1. 在服务商列表中选择 **DeepSeek**，API 地址自动填入 `https://api.deepseek.com`，接口协议为 `Chat Completions`，默认模型为 `deepseek-v4-pro`。
2. 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key 并粘贴到密钥输入框。
3. 如需切换模型，点击 **获取模型**，选择 **`deepseek-v4-pro`**（推理最强）或 **`deepseek-v4-flash`**（更快更便宜）；如果列表拉取失败，可选择 **手动输入其他模型…** 直接填入模型名。
4. 点击 **保存并测试连接**，看到 **「Hermes 模型连接可用」** 即配置成功。

说明：

- DeepSeek V4 系列支持最高 **100 万 token** 上下文。easy-stock 会把完整的研究上下文（行情、题材结构、分析历史）交给模型，非常适合长复盘与观点共识类任务。
- `deepseek-v4-pro` 在 DeepSeek API 侧默认开启深度思考，easy-stock 走标准 Chat Completions 协议，无需额外配置即可获得该能力。

#### 3. 首次使用：分析一只股票

1. 在顶部搜索框按名称或代码搜索股票，进入个股页面。
2. 打开 **个股 AI 分析** 并生成报告。easy-stock 会先判断个股路径（情绪连板、趋势容量、趋势成长、震荡观察或弱势风险），再产出带确认条件与失效条件、可回溯证据的专属报告。
3. 收盘后进入 **大 V 复盘日记 → 今日观点共识**，从收集到的文章中提炼跨作者共识与分歧。

#### 4. 进阶用法

- **复盘自动化**：在 **系统设置 → 大 V 复盘自动化** 中通过内置浏览器登录雪球或淘股吧，easy-stock 会按计划自动同步订阅作者的新文章。
- **持仓 AI 巡检**：添加最多 10 只持仓并设置仓位，选择交易风格后生成组合健康度报告，识别集中度与联动风险。
- **本地研究记忆**：文章、分析记录与 AI 会话全部保存在本机，API Key 不会离开你的电脑。
- **多服务商切换**：同一设置面板还支持 OpenAI 兼容接口（Kimi、通义千问、智谱 GLM 等）与 Anthropic，可保存多套配置随时切换。
