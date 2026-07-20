[English](./openhands.md) | [简体中文](./openhands.zh-CN.md) · [← Back](../README.zh-CN.md)

# 接入 OpenHands

OpenHands 是一个开源的 AI 代理软件开发平台。其 Agent Canvas 网页界面可让你配置 LLM 模型、创建 Agent 配置文件，并在隔离的工作空间中运行编程代理。OpenHands 支持任何兼容 OpenAI 的 API，因此接入 DeepSeek 非常简单。

#### 1. 安装 OpenHands

**前置条件：** Node.js 22.12.x 或更高版本。

```shell
npm install -g @openhands/agent-canvas
```

启动服务：

```shell
agent-canvas
```

在浏览器中访问 [http://localhost:8000](http://localhost:8000)。

如需 Docker 沙箱方式安装（推荐用于隔离执行环境），请参阅 [OpenHands 文档](https://docs.openhands.dev/overview/quickstart)。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)，创建 API Key 并复制。

#### 3. 配置 DeepSeek 的 LLM Profile

在 Agent Canvas 网页界面中：

1. 点击侧边栏的 **设置** 图标（齿轮）。
2. 进入 **LLM Profiles**（LLM 配置文件）。
3. 点击 **Add LLM Profile**（添加 LLM 配置文件）。
4. 填写以下字段：

| 字段 | 值 |
|------|-----|
| 名称 | `DeepSeek V4 Pro`（或任意你喜欢的名称） |
| 模型 | `deepseek/deepseek-v4-pro` |
| 基础 URL | `https://api.deepseek.com/v1` |
| API 密钥 | 你的 DeepSeek API Key |

**重要：** 模型名称必须包含 LiteLLM 提供商前缀（`deepseek/`）。仅使用 `deepseek-v4-pro` 不带前缀会导致报错。

**上下文窗口：** DeepSeek V4 模型支持最高 100 万 token 上下文。OpenHands 会自动从 API 响应中检测并使用，无需手动设置 `max_input_tokens`。

5. 点击 **Save**（保存）。

你也可以为轻量任务添加 Flash 模型配置：

| 字段 | 值 |
|------|-----|
| 模型 | `deepseek/deepseek-v4-flash` |
| 基础 URL | `https://api.deepseek.com/v1` |
| API 密钥 |（同上） |

#### 4. 开始编程

在侧边栏点击 **New Conversation**（新建对话），选择你的 DeepSeek LLM Profile，指定工作目录，然后开始输入提示：

> 用 React 构建一个纯前端的 TODO 应用。所有状态存储在 localStorage 中。

OpenHands 会在工作空间内自主编写、编辑和运行代码。

#### 验证

创建一个简单的测试对话：

> 用一句话输出你的模型名称和版本号。

Agent 应回复表明自己是 DeepSeek 的 `deepseek-v4-pro`。

你也可以在 **设置 → LLM Profiles** 中确认你的 DeepSeek 配置已显示为活跃状态。

#### 常见问题

- **"LLM Provider NOT provided"（未提供 LLM 提供商）**：模型名称缺少 `deepseek/` 前缀。请将模型字段改为 `deepseek/deepseek-v4-pro`。
- **401 或鉴权错误**：检查 LLM Profile 中的 DeepSeek API Key 是否正确。
- **402 或付款错误**：检查 DeepSeek 平台账户余额。
- **连接被拒绝**：`agent-canvas` 服务未启动。请在终端中执行 `agent-canvas`。

#### 相关资源

- [OpenHands](https://github.com/All-Hands-AI/OpenHands)
- [OpenHands Agent Canvas](https://github.com/OpenHands/agent-canvas)
- [OpenHands 文档](https://docs.openhands.dev/)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
