[English](./iris.md) | [简体中文](./iris.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Iris

[Iris](https://github.com/Lianues/Iris) 是一款开源的多平台 AI 代理 Agent，支持 Console（TUI）、Web、Discord、Telegram、微信、企业微信、飞书、QQ 等平台，内置工具调用、会话存储、图片输入、OCR 回退、MCP、记忆与多 Agent 能力。Iris 原生支持 DeepSeek 作为 LLM 提供商 —— 直接对接 `api.deepseek.com`，无需任何代理层。

#### 1. 安装 Iris

推荐方式（跨平台，需要 Node.js）：

```bash
npm install -g irises
```

命令行入口是 `iris`，npm 包名是 `irises`。其他安装方式（GitHub Release 二进制、Linux 一键脚本、Docker、源码编译）请参阅 [Iris 安装文档](https://github.com/Lianues/Iris/blob/main/docs/install.md)。

#### 2. 通过交互式向导配置 DeepSeek

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后执行：

```bash
iris onboard
```

在 TUI 向导中：

- 当提示 **LLM 提供商** 时，选择 **DeepSeek**。
- 当提示 **API Key** 时，粘贴你的 DeepSeek API Key。
- 当提示 **模型** 时，在 `deepseek-v4-pro`（编程与复杂推理）和 `deepseek-v4-flash`（快速、低成本日常任务）之间二选一。
- 剩余选项（平台、模型别名等）按需配置或保留默认值。

向导会把配置写入 `~/.iris/configs/llm.yaml`（可通过 `IRIS_DATA_DIR` 环境变量覆盖路径）。

如果你习惯直接编辑 YAML，对应的 `~/.iris/configs/llm.yaml` 是：

```yaml
defaultModel: deepseek_pro

models:
  deepseek_pro:
    provider: deepseek
    apiKey: sk-your-deepseek-api-key
    model: deepseek-v4-pro
    contextWindow: 1000000
    requestBody:
      thinking:
        type: enabled
      reasoning_effort: max
      max_tokens: 384000

  deepseek_flash:
    provider: deepseek
    apiKey: sk-your-deepseek-api-key
    model: deepseek-v4-flash
    contextWindow: 1000000
    requestBody:
      max_tokens: 384000
```

- `contextWindow: 1000000` 在 Iris TUI 的上下文用量条上启用 DeepSeek V4 完整的 **100 万 Token** 窗口。
- `requestBody.thinking.type: enabled` 配合 `reasoning_effort: max` 启用 DeepSeek V4 思考模式并使用最深推理强度，这两个字段都来自 DeepSeek 官方 [Thinking Mode 文档](https://api-docs.deepseek.com/guides/thinking_mode) 中列出的 OpenAI 格式控制参数，推荐用于编程与多步骤 Agent 任务。
- `max_tokens: 384000` 放开单次响应的输出上限，让 V4 有足够预算容纳长链思考加上最终回复。

#### 3. 启动 Iris

```bash
iris 或 iris start
```

进入 Console TUI 后，常用命令：`/model` 切换模型、`/settings` 打开设置中心（LLM / System / MCP）、`/exit` 退出。完整 Slash 命令参考见 [docs/platforms.md](https://github.com/Lianues/Iris/blob/main/docs/platforms.md)。

#### 可选：在聊天平台上运行 Iris

Iris 还可以作为 Web GUI 或聊天机器人运行在 Discord、Telegram、飞书、QQ、微信、企业微信 上。修改 `~/.iris/configs/platform.yaml` 中的 `platform.type`，并在需要时安装对应的 IM extension：

```bash
iris ext install lark    # 示例：安装飞书 extension
```

各平台的 Token 与机器人配置详见 [docs/platforms.md](https://github.com/Lianues/Iris/blob/main/docs/platforms.md)。

#### 常见问题

- **`baseUrl` 似乎被忽略了。** 这是预期行为。`provider: deepseek` 固定请求官方接口 `https://api.deepseek.com/v1`。如果需要通过自定义代理或网关访问，请改用 `provider: openai-compatible` 并填入你网关的 `baseUrl`。
- **报 `Invalid model` 错误。** 使用 `provider: deepseek` 时，`model` 字段只接受 `deepseek-v4-pro` 或 `deepseek-v4-flash`。V3 时代的旧模型 id 已不再支持。
- **TUI 看不到思考内容。** 确认 `requestBody.thinking.type: enabled` 写在了 DeepSeek 模型条目下，而不是 `llm.yaml` 的顶层。
