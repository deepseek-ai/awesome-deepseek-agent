[English](./tocodex.md) | [简体中文](./tocodex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 ToCodex

ToCodex 是一款 AI 编程助手，提供 VS Code 扩展、IDE、桌面客户端和 CLI 等多种形态。它支持 OpenAI 兼容供应商、多模型路由、MCP 工具和定时自动化，几分钟即可接入 DeepSeek-V4-Pro 或 DeepSeek-V4-Flash。

- **官网：** <https://tocodex.com>
- **VS Code 市场：** <https://marketplace.visualstudio.com/items?itemName=ToCodex.tocodex>
- **开源（社区版）：** <https://github.com/tocodex-ai/tocodex-community>

#### 1. 安装 ToCodex

**方式一：从 VS Code 市场安装**

- 打开 VS Code。
- 点击活动栏中的 **扩展** 图标（或按 `Ctrl+Shift+X`）。
- 搜索 `ToCodex`。
- 找到 **ToCodex** 扩展并点击 **Install**。

也可以使用命令行安装：

```sh
code --install-extension tocodex.tocodex
```

**方式二：使用 ToCodex 桌面版或 IDE**

从 <https://tocodex.com/download.html> 下载，桌面客户端开箱即用，支持 Windows 10/11 与 macOS。

#### 2. 获取 DeepSeek API Key

- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。

#### 3. 添加 DeepSeek 作为 API 供应商

- 打开 ToCodex 的设置 / 供应商管理页面。
- 选择 **OpenAI Compatible**（如果有 DeepSeek 预设也可以直接选）。
- 填写以下字段：

| 字段 | 值 |
|------|----|
| Base URL | `https://api.deepseek.com` |
| API Key | 你的 DeepSeek API Key（`sk-...`） |
| Model ID | `deepseek-v4-pro`（或 `deepseek-v4-flash`） |

> **注意：** 当前可用的模型 ID 是 `deepseek-v4-pro` 和 `deepseek-v4-flash`，旧的 `deepseek-chat`、`deepseek-reasoner` 已废弃。

#### 4. 配置上下文窗口与思考模式

DeepSeek V4 模型支持最多 **100 万 tokens** 上下文，最大输出 384K tokens。如果 ToCodex 的模型配置允许设置这些值，请填写：

- `context_window: 1000000`
- `max_tokens: 384000`

DeepSeek V4 同时支持思考模式与非思考模式（默认开启思考模式）。在 ToCodex 中请保持思考模式开启，并使用较高的推理强度（如 `max`），以获得最佳编程体验。不要为了规避 API 报错而关闭思考模式，那会降低模型性能。

#### 5. 首次运行

- 在 VS Code 中打开你的项目文件夹。
- 在模型选择器中选择 `deepseek-v4-pro`。
- 发送一条提示，例如 `解释一下这个代码库`，验证连接是否正常。

配置完成，开始用 DeepSeek 在 ToCodex 中编程吧。

#### 常见问题

- **401 Unauthorized**：检查 API Key 是否正确，确认没有多余空格。
- **模型不存在**：确认 Model ID 精确填写为 `deepseek-v4-pro` 或 `deepseek-v4-flash`（旧的 `deepseek-chat` / `deepseek-reasoner` 已停止服务）。
- **超长上下文**：ToCodex 支持 1M 上下文；如果超大输入请求失败，请缩小输入规模或查看官方[限速与隔离](https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit)文档。
