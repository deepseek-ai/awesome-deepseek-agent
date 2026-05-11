[English](./operit.md) | [简体中文](./operit.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Operit

Operit 是一款开源 Android AI Agent，提供全方位的助理能力。DeepSeek V4 可以通过 Operit 内置的 DeepSeek 引导接入，也可以通过 OpenAI 兼容端点手动配置。

#### 1. 安装 Operit

- 前往 [Operit 官网](https://operit.app/) 下载最新 APK，也可以使用 [GitHub Releases 页面](https://github.com/AAswordman/Operit/releases)。
- 启动 Operit，并完成首次引导。

完整首次引导可参考官方 [Operit 新手指南](https://operit.app/#/guide/new)。

#### 2. 配置 DeepSeek

首次启动时，点击 `获取 token`，Operit 会自动跳转到软件内置的 DeepSeek 官网页面。创建 API Key 后，回到 Operit 粘贴即可开始对话。

Operit 会自动填写 `deepseek-v4-flash`。

DeepSeek V4 支持最高 100 万 token 上下文，可以在 Operit 的上下文压缩设置里修改想要使用的上下文量。

如果需要手动配置，打开 `设置` -> `模型与参数配置`，新建一个配置，并填写：

```text
供应商: DeepSeek
端点: https://api.deepseek.com/v1/chat/completions
API Key: <你的 DeepSeek API Key>
模型: deepseek-v4-pro 或 deepseek-v4-flash
```

#### 3. 开始使用

回到聊天页，选择 DeepSeek 模型，发送一条消息测试即可。
