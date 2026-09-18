[English](./qwenpaw.md) | [简体中文](./qwenpaw.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 QwenPaw 中接入 DeepSeek

QwenPaw 是 AgentScope 团队开发的开源个人 AI 助手，提供 Web 控制台和终端界面，可连接聊天平台，并能通过技能、记忆和 MCP 工具扩展能力。DeepSeek 已作为内置模型提供商集成其中。

- **GitHub：** <https://github.com/agentscope-ai/QwenPaw>
- **文档：** <https://qwenpaw.agentscope.io/docs/>

#### 1. 安装 QwenPaw

QwenPaw 需要 Python 3.11–3.13。安装 QwenPaw v2.0.1 或更高版本，完成初始化并启动 Web 控制台：

```bash
python -m pip install --upgrade "qwenpaw>=2.0.1"
qwenpaw init --defaults
qwenpaw app
```

在浏览器中打开 <http://127.0.0.1:8088/>。

> QwenPaw 还提供安装脚本、Docker 和桌面应用等安装方式。如果你更喜欢这些方式，请参阅 [QwenPaw 快速开始](https://qwenpaw.agentscope.io/docs/quickstart/)。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)，创建并复制 API Key。

#### 3. 配置 DeepSeek 提供商

在 QwenPaw 控制台中：

1. 进入 **设置 → 模型**。
2. 打开内置 **DeepSeek** 提供商的设置，填写并保存 API Key，然后点击**测试连接**。
3. 打开该提供商的模型列表，测试 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
4. 打开所选模型的配置并填写：
   - **最大输出 Tokens：** `384000`
   - **最大上下文长度：** `1000000`
   - **转发推理内容：** 开启
5. 在该模型的生成参数 JSON 输入框中填写：

```json
{
  "reasoning_effort": "max",
  "extra_body": {
    "thinking": {
      "type": "enabled"
    }
  }
}
```

保存模型设置。在**设置 → 模型 → 默认 LLM** 中选择刚刚配置的模型，或者通过**聊天**页面右上角的模型选择器仅为当前对话选择它。

DeepSeek V4 Pro 和 Flash 支持 100 万 Token 上下文窗口，最大输出为 38.4 万 Token。思考模式默认开启，上面的显式配置可以确保 QwenPaw 请求当前可用的最高推理强度。

#### 4. 首次运行

新建对话并发送一个会触发工具调用的提示词，例如：

```text
请使用当前时间工具告诉我本地时间，然后说明你使用了哪个工具。
```

你也可以在 QwenPaw 的终端界面中使用同一个已配置的 Agent：

```bash
qwenpaw
```

#### 常见问题

- **返回 401 或 403：** 检查 API Key 是否正确，并确认 DeepSeek 账户余额充足。
- **找不到模型：** 运行 `python -m pip install --upgrade qwenpaw` 完成升级。QwenPaw v2.0.1 已内置 DeepSeek V4 Pro 和 Flash。
- **出现包含 `reasoning_content` 的 400 错误：** 升级到 QwenPaw v2.0.1 或更高版本。当前版本会在多轮工具调用中保留 DeepSeek 所需的推理内容，不要把关闭思考模式作为解决方案。

有关最新的模型能力与限制，请参阅 DeepSeek 官方的[模型与价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)和[思考模式](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode/)文档。
