[English](./aurora.md) | [简体中文](./aurora.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Aurora

Aurora 是 **AI 应用时代的控制中枢** —— 一个账号、一个网关，所有受支持的智能体和客户端都能通过它触达全球最强的模型。自带你的 DeepSeek API Key，创建一个 Aurora Key，即可从你已有的客户端或 Aurora Assistant 开始用 DeepSeek-V4 构建。

- **官网:** <https://auroramos.com>

#### 1. 下载 Aurora

前往 <https://auroramos.com>，下载对应平台的 Aurora 客户端（macOS / Windows）并安装。

#### 2. 创建 Aurora 账号

打开 Aurora 并注册账号。新账号自带试用权益与注册赠送积分。

#### 3. 导入 DeepSeek API Key

1. 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 DeepSeek API Key。
2. 在 Aurora 控制台的 **API Platforms** 中，导入你的 DeepSeek API Key 作为 API Platform 资源。

之后 Aurora 会通过你的账号路由 DeepSeek 流量 —— 身份、用量与审计统一收口在一处。

#### 4. 创建 Aurora 个人 API Key

在 **API Keys** 中创建一个 **Personal（个人）** Key。你的客户端会用这把 Key 作为访问 Aurora 网关的凭据。

#### 5. 开始用 DeepSeek-V4 构建

**方式 A —— 从你已有的客户端接入（经由 Aurora Desktop）：**

1. 打开 Aurora 桌面端的**本机调用页**。
2. 选择你已经安装的客户端 —— Claude Code、Codex 或 Claude Desktop。
3. 在 **Key 选择器**中，选择刚才创建的 **Personal（个人）** Aurora Key。
4. 在**模型选择器**中，选择 `deepseek/deepseek-v4-flash` 或 `deepseek/deepseek-v4-pro`。
5. 开始调用。请求会经过你的 Aurora 账号路由到 DeepSeek。

**方式 B —— 直接在 Aurora Assistant（终端）中选择：**

1. 启动 Aurora Assistant。
2. 运行 `/key`，在 Key 选择器中选择刚才创建的 **Personal（个人）** Aurora Key。
3. 运行 `/model`，在模型选择器中选择 `deepseek/deepseek-v4-flash` 或 `deepseek/deepseek-v4-pro`。
4. 可用 `/effort` 调整推理力度。
5. 开始构建。

#### 说明

- DeepSeek-V4 支持 **1M token** 上下文窗口。
- 思考模式默认开启；Aurora 会跨提供商映射推理力度档位。
