[English](./rtrvr.md) | [简体中文](./rtrvr.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 rtrvr.ai

rtrvr.ai 是一个浏览器原生 AI Web Agent，可用于网页抓取、表单填写、监控与多步骤网页自动化。你可以在 Chrome 扩展中使用自己的 DeepSeek API Key，因此浏览器扩展运行时可以直接走你的 DeepSeek 账号。

- **官网：** <https://www.rtrvr.ai/>
- **浏览器扩展：** <https://chromewebstore.google.com/detail/retriever-ai-web-agent/jldogdgepmcedfdhgnmclgemehfhpomg>
- **文档：** <https://www.rtrvr.ai/docs>

#### 1. 准备 rtrvr.ai 与 DeepSeek API Key

1. 安装 [Retriever: AI Web Agent](https://chromewebstore.google.com/detail/retriever-ai-web-agent/jldogdgepmcedfdhgnmclgemehfhpomg) 浏览器扩展。
2. 在扩展中登录 rtrvr.ai。
3. 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。

rtrvr.ai 支持自带模型 Key，也支持 OpenAI 兼容端点或本地端点。如果你想用自己的 DeepSeek Key 免费运行本地浏览器自动化任务，优先使用浏览器扩展。

#### 2. 添加 DeepSeek 自定义服务商

打开 rtrvr.ai 扩展设置，添加一个 OpenAI 兼容的自定义模型服务商。

使用以下配置：

```text
服务商名称：DeepSeek
API Key：<你的 DeepSeek API Key>
Base URL：https://api.deepseek.com/v1
如果要求填写 Chat Completions URL：https://api.deepseek.com/v1/chat/completions
```

添加当前 DeepSeek V4 模型 id：

```text
deepseek-v4-pro
deepseek-v4-flash
```

复杂浏览器工作流、编码研究与长程多步骤任务建议选择 `deepseek-v4-pro`；日常网页抓取和页面操作建议选择响应更快的 `deepseek-v4-flash`。

#### 3. 运行浏览器任务

1. 打开你希望 rtrvr.ai 操作的网页。
2. 打开浏览器扩展。
3. 选择你的 DeepSeek 服务商和模型。
4. 用自然语言描述浏览器任务，例如：

```text
提取当前页面的商品名称、价格、评分和库存状态，并返回 JSON 表格。
```

扩展会在你的浏览器会话中运行，因此可以使用你已经登录的网页。DeepSeek 用量会通过你的 DeepSeek API 账号计费。

#### 4. DeepSeek V4 注意事项

- DeepSeek V4 模型支持最高 100 万 token 上下文窗口。rtrvr.ai 会先将浏览器页面压缩为结构化页面数据再调用模型，因此扩展流程中通常不需要单独配置上下文长度。
- 需要更强推理能力时，规划型任务优先使用 `deepseek-v4-pro`。如果你的 rtrvr.ai 版本提供高级请求参数，可以将 `reasoning_effort` 设置为 `max`。
- 保留 `deepseek-v4-flash` 作为简单提取和导航任务的高速备选模型。

#### 常见问题

- 鉴权失败：重新检查从 DeepSeek 开放平台复制的 API Key。
- 找不到模型：确认模型 id 严格写为 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- 服务商连接失败：Base URL 使用 `https://api.deepseek.com/v1`；只有当字段明确要求完整 Chat Completions 端点时，才填写 `https://api.deepseek.com/v1/chat/completions`。
- 扩展无法操作已登录页面：确认你正在使用已安装并登录 rtrvr.ai 扩展的同一个浏览器配置文件。
