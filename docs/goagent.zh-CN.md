[English](./goagent.md) | [简体中文](./goagent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 GoAgent 中接入 DeepSeek

[GoAgent](https://github.com/wimi321/GoAgent) 是一个开源的围棋智能体，面向 Go / Weiqi / Baduk 学习与复盘场景。它结合 KataGo 分析、棋盘证据、本地知识库、学生画像和 LLM 工具调用，让老师基于证据讲棋，而不是凭空猜测。

GoAgent 可以通过 OpenAI-compatible LLM Provider 接入 DeepSeek。对于需要棋盘截图的当前手讲解，请使用支持图片输入的 DeepSeek 兼容端点或代理；如果你的端点只支持文本，DeepSeek 仍然可以用于 SGF、KataGo 数据、知识库和工具结果驱动的讲解任务。

#### 1. 安装 GoAgent

从 [GoAgent Releases](https://github.com/wimi321/GoAgent/releases) 下载最新版桌面应用。

也可以从源码运行：

```
git clone https://github.com/wimi321/GoAgent.git
cd GoAgent
pnpm install
pnpm dev
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。

#### 3. 在 GoAgent 中配置 DeepSeek

打开 GoAgent 的 **设置**，配置 LLM Provider：

- **Base URL**：`https://api.deepseek.com`
- **API Key**：你的 DeepSeek API Key
- **模型**：`deepseek-v4-pro` 或 `deepseek-v4-flash`

保存后，如果 GoAgent 提供模型刷新或连接测试按钮，可以先执行一次测试。

做长棋局复盘时，如果端点支持 DeepSeek V4 的 100 万 token 上下文，建议优先开启。若兼容代理支持 `reasoning_effort`，深度复盘可为 `deepseek-v4-pro` 选择 `max`；日常快速讲棋可选择 `high` 或保持服务商默认设置。

#### 4. 开始讲棋

在 GoAgent 中：

1. 导入 SGF，或从棋谱库载入棋局。
2. 确认 KataGo 已配置，并且胜率图已有分析数据。
3. 让老师分析当前手、指定手数区间或整盘棋。

示例：

```
结合 KataGo 证据和本地知识库分析当前手。
找出这盘棋最重要的三个转折点。
复盘 80-120 手，并告诉我学生下一步应该练什么。
```

GoAgent 老师可以调用棋谱、KataGo 分析、Trace Packet、棋盘图片、知识库检索和学生画像等工具。最终讲解应以工具结果为依据，而不是没有证据的判断。

#### 5. 注意事项

- 如果棋谱包含隐私内容，请确认你愿意把相关文本或图片发送给所选择的模型服务商。
- 想要更低延迟，可以使用 `deepseek-v4-flash`；想要更深入的复盘，可以使用 `deepseek-v4-pro`。
- 如果需要基于棋盘截图读图，请确认当前 OpenAI-compatible 端点支持图片消息。
