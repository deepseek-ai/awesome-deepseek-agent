[English](./atlarix.md) | [简体中文](./atlarix.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Atlarix

Atlarix 是由 Norah Labs 打造的 Agent 工作站桌面应用（支持 macOS、Linux、Windows），专为开源权重前沿模型（DeepSeek、Qwen、Kimi、MiniMax）而设计。它支持 BYOK（自带密钥）接入 OpenAI 兼容接口、并行子 Agent、MCP 服务器，以及五种工作模式：探索、规划、构建、调试与审查。

- **官网：** <https://atlarix.dev>
- **开发团队：** Norah Labs（<https://norahlabs.com>）

#### 1. 安装 Atlarix

从 [atlarix.dev](https://atlarix.dev) 下载适用于你平台的安装包，支持 macOS、Linux 和 Windows。

安装后使用 Google 或 GitHub 账号登录，并打开一个项目文件夹作为工作区——所有对话均在该工作区内进行。

#### 2. 添加 DeepSeek 提供商

Atlarix 通过 OpenAI 兼容接口连接 DeepSeek。添加你的 DeepSeek API Key 作为自定义提供商：

1. 打开 **Settings**（侧边栏齿轮图标）→ **AI**。
2. 在自定义提供商中添加一个 **OpenAI-compatible** 提供商，填入以下配置：
   - **Base URL：** `https://api.deepseek.com`
   - **API Key：** `<你的 DeepSeek API Key>`
   - **模型：** `deepseek-v4-pro`、`deepseek-v4-flash`

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 选择模型并开始工作

配置好提供商后：

1. 在聊天区域的模型选择器中，选择 **deepseek-v4-pro** 或 **deepseek-v4-flash**。
2. 选择工作模式——先使用 **Plan（规划）** 梳理任务，再切换到 **Build（构建）** 通过审批队列进行实现。
3. 输入你的任务并发送。

DeepSeek V4 完整的 **100 万 token** 上下文窗口在 Atlarix 中开箱即用。为获得最佳编程体验，在聊天输入中开启 **Deep Think（深度思考）**——Atlarix 会向 DeepSeek API 传递 `reasoning_effort: "max"`，以在处理复杂任务时获得最强的推理能力。

#### 4. Headless CLI（可选）

适用于 CI 流水线和基准测试，Atlarix 提供了可直接对接 DeepSeek 的无头 CLI：

```bash
node /opt/atlarix/dist-headless/atlarix-headless.mjs \
  --workspace /path/to/repo \
  --prompt "修复 src/auth.ts 中的失败测试" \
  --provider-url https://api.deepseek.com \
  --model deepseek-v4-pro \
  --api-key "$DEEPSEEK_API_KEY"
```

无头版会自动批准文件和命令操作。使用 `--mode ask` 可切换为只读探索模式。
