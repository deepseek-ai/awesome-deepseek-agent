[English](./zcode-ade.md) | [简体中文](./zcode-ade.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 ZCode

ZCode 是智谱（Z.ai）推出的 Agentic 开发环境（ADE），将 AI Agent 与现有工具链相结合。它支持多种 LLM 供应商，你只需几步即可将 DeepSeek 添加为自定义供应商。

- **官网：** <https://zcode.z.ai>
- **文档：** <https://zcode.z.ai/cn/docs>

#### 1. 安装 ZCode

前往 <https://zcode.z.ai> 下载安装包，并按你的平台（Windows / macOS / Linux）完成安装。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key 并复制。

#### 3. 将 DeepSeek 添加为供应商

打开 ZCode，进入 **设置 → 模型设置 → 添加供应商**，按如下填写：

| 字段 | 值 |
|------|-----|
| 名称 | `DeepSeek` |
| Base URL | `https://api.deepseek.com/v1` |
| API Key | `sk-...`（你的 DeepSeek API Key） |
| 模型 ID | `deepseek-v4-pro`, `deepseek-v4-flash` |

ZCode 底层使用的是 DeepSeek 的 OpenAI 兼容端点，与 ZCode 使用的 Responses API 格式天然匹配。

#### 4. 切换到 DeepSeek 模型

在模型选择器中，选择 `deepseek-v4-flash` 或 `deepseek-v4-pro`。

完成。DeepSeek V4 的**思考模式默认开启**（推理强度默认为 `high`），开箱即用即可获得深度推理能力，无需额外配置。

> **注意：** ZCode 的"思考级别"选择器目前仅对内置的 OpenAI 模型生效。对于 DeepSeek 等第三方供应商，该选择器可能暂不生效，此时使用模型的默认思考模式（high 档）。DeepSeek V4 支持 100 万 token 的上下文窗口。
