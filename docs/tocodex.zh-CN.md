[English](./tocodex.md) | [简体中文](./tocodex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 ToCodex

[ToCodex](https://tocodex.com) 是一款开源的企业级通用 AI 编程 Agent，提供桌面应用、VS Code 扩展和 CLI 三种形态。DeepSeek 是 ToCodex 内置的**重点供应商**——你只需粘贴 API Key，ToCodex 便会自动拉取可用的 DeepSeek-V4 模型及其上下文窗口、推理等级、规格与价格，无需任何代理或转发层。

#### 1. 安装 ToCodex

按你的工作流选择任一形态：

- **VS Code 扩展**——打开 VS Code，点击**扩展**图标（或按 `Ctrl+Shift+X`），搜索 `ToCodex`，点击**安装**。
- **桌面应用**——从 [ToCodex 官网](https://tocodex.com/download.html) 下载。
- **CLI**——通过 npm 安装：

```shell
npm install -g @tocodex/cli
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)，创建并复制一个 API Key。

#### 3. 选择 DeepSeek 供应商

- 从活动栏启动 ToCodex。
- 在引导页，或之后通过**设置 → 供应商 → API 供应商**，打开供应商列表。
- DeepSeek 已作为内置供应商列出（排在 Anthropic、OpenAI、OpenRouter、Google Gemini 等之前）。选择 **DeepSeek**。

<div align="center">
<img src="./assets/tocodex_step_1.png" width="250" border="1" />
</div>

#### 4. 配置 DeepSeek 供应商

- 在 API 供应商选择 **DeepSeek** 后，粘贴你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- ToCodex 会自动拉取可用的 DeepSeek 模型及其规格与价格，无需手动填写 Base URL 或模型参数。

<div align="center">
<img src="./assets/tocodex_step_2.png" width="250" border="1" />
</div>

#### 5. 选择模型并设置推理强度

- 打开模型选择器，选择 **`deepseek-v4-pro`**（能力最强，推荐用于编程）或 **`deepseek-v4-flash`**（更快、成本更低）。
- **100 万 token 上下文：** ToCodex 完整支持 DeepSeek-V4 系列的 **1,000,000 token** 上下文窗口，并会自动读取模型的上下文窗口，长上下文任务开箱即用。
- **最高推理强度：** 为获得最佳编码体验，建议将**推理强度（reasoning effort）**设为最高级（`max`）。ToCodex 在输入栏将其作为每次任务可调的设置项，让 DeepSeek-V4-Pro 在复杂任务上进行深度思考。请勿为规避报错而关闭思考模式——做 Agent 编程时应保持 `max`/`high`。
- （可选）你还可以为轻量子任务单独指定一个 DeepSeek 模型（如 `deepseek-v4-flash`）作为**辅助模型**。

<div align="center">
<img src="./assets/tocodex_step_3.png" width="250" border="1" />
</div>

#### 6. 首次运行

打开一个项目目录，在 ToCodex 输入框中输入需求并发送。ToCodex 会将请求路由到 DeepSeek-V4，并在其 MCP 工具、自定义模式、定时任务与可配置模型路由中开始工作。

### 价格

DeepSeek-V4 价格快照（每 100 万 token）。请始终以官方价格页的最新数值为准（[English](https://api-docs.deepseek.com/quick_start/pricing) / [中文](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)）。

| 模型 | 输入 | 输出 | 缓存命中 |
|------|------|------|----------|
| `deepseek-v4-pro` | $0.435 | $0.87 | $0.003625 |
| `deepseek-v4-flash` | $0.14 | $0.28 | $0.0028 |

配置好供应商后，ToCodex 会自动显示模型价格。

### 说明

- **模型：** `deepseek-v4-pro` 与 `deepseek-v4-flash` 是当前的 DeepSeek-V4 模型。旧版 `deepseek-chat` 与 `deepseek-reasoner`（V3）正在弃用——请使用 V4 名称。

### 故障排查

- **`401` / 认证错误**——检查**设置 → 供应商**中的 DeepSeek API Key。
- **`402` / 付费错误**——检查 [DeepSeek 开放平台](https://platform.deepseek.com/) 的账户余额。
- **模型列表为空**——重新填入 API Key，并确认可访问 `https://api.deepseek.com`。

### 相关资源

- [ToCodex](https://tocodex.com)
- [ToCodex Community（开源）](https://github.com/tocodex-ai/tocodex-community)
- [DeepSeek 开放平台](https://platform.deepseek.com/)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
