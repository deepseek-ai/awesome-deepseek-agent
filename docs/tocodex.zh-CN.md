[English](./tocodex.md) | [简体中文](./tocodex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 ToCodex

ToCodex 是一款开源的企业级通用 AI 编程 Agent，提供桌面应用、VS Code 扩展和 CLI 三种形态。DeepSeek 是 ToCodex 内置的重点模型供应商，你只需填入 API Key 即可使用，无需手动配置接口地址或模型参数。

#### 1. 安装 ToCodex

- 打开 VS Code。
- 点击活动栏中的**扩展**图标（或按 `Ctrl+Shift+X`）。
- 搜索 `ToCodex`。
- 在结果中找到 **ToCodex** 扩展并点击**安装**。

> 你也可以从 [ToCodex 官网](https://tocodex.com) 下载桌面应用或安装 CLI。

#### 2. 打开供应商选择器

- 从活动栏启动 ToCodex。
- 在引导页（或**设置 → 供应商 → API 供应商**）中打开供应商列表。
- DeepSeek 已作为内置供应商列出 —— 选择 **DeepSeek**。

<div align="center">
<img src="./assets/tocodex_step_1.png" width="250" border="1" />
</div>

#### 3. 配置 DeepSeek 供应商

- 在 API 供应商选择 **DeepSeek** 后，粘贴你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- ToCodex 会自动拉取可用的 DeepSeek 模型及其规格与价格，无需手动填写 Base URL 或模型参数。

<div align="center">
<img src="./assets/tocodex_step_2.png" width="250" border="1" />
</div>

#### 4. 选择模型并开始使用

- 打开模型选择器，选择 **deepseek-v4-pro**（能力最强）或 **deepseek-v4-flash**（更快、成本更低）。
- ToCodex 完整支持 DeepSeek-V4 系列的 100 万 token 上下文窗口，并可调节**推理强度（reasoning effort）**等级，让模型在复杂任务上进行更深入的思考。
- 你还可以为轻量子任务单独指定一个 DeepSeek 模型作为辅助模型。

<div align="center">
<img src="./assets/tocodex_step_3.png" width="250" border="1" />
</div>

完成配置后，你就可以在 ToCodex 的 MCP 工具、自定义模式、定时任务与可配置模型路由中全面使用 DeepSeek。

> **模型说明：** `deepseek-v4-pro` 与 `deepseek-v4-flash` 是当前的 DeepSeek-V4 模型。旧版 `deepseek-chat` 与 `deepseek-reasoner` 正在逐步弃用。
