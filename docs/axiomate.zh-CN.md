[English](./axiomate.md) | [简体中文](./axiomate.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Axiomate

Axiomate 是一个多 Provider AI Agent CLI，支持在终端中聊天、编程和控制桌面。它通过统一配置连接 DeepSeek、OpenRouter、SiliconFlow、ollama、vLLM、Anthropic 等多种后端。针对 DeepSeek V4，Axiomate 提供交互式 TUI 向导实现零摩擦配置，自动在工具调用间 round-trip `reasoning_content`，并通过 UIA/AX 原生绑定 + Set-of-Mark 覆盖层为纯文本模型提供桌面自动化能力。

## 1. 安装

**前置条件：** Node.js 20+、Git。Windows 还需要 Visual Studio 2022 Build Tools（bootstrap 脚本会自动安装）。

从 [GitHub Releases](https://github.com/axiomates/axiomate-agent/releases/tag/0.6.2) 下载最新版本，或从源码构建：

```bash
git clone https://github.com/axiomates/axiomate-agent.git
cd axiomate-agent
npm run bootstrap   # 自动安装 pnpm + Bun + Rust + 依赖，构建所有工作区
pnpm run start      # 启动 Axiomate
```

## 2. 配置 DeepSeek（交互式 TUI）

### 首次启动 — Onboarding 向导

首次启动 Axiomate 且未配置任何模型时，会进入多步骤 TUI 向导：

| 步骤 | 字段 | DeepSeek 填写内容 |
|------|------|-------------------|
| 1 | 协议 | **OpenAI Chat Completions** |
| 2 | API 基础 URL | `https://api.deepseek.com` |
| 3 | API Key | 从 [platform.deepseek.com](https://platform.deepseek.com/api_keys) 获取（掩码输入） |
| 4 | 模型 ID | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| 5 | 上下文窗口 | `1000000`（100 万 token） |
| 6 | 图像输入支持 | **否** — DeepSeek V4 为纯文本模型 |
| 7 | 供应商模板 | `Auto-detect`（自动选择 `openai-chat-deepseek-official`） |
| 8 | 推理深度 | **High** 或 **Max**（DeepSeek V4 Pro 仅支持这两个级别） |

验证连接成功后，配置保存至 `~/.axiomate.json`，即可开始使用。

### 后续添加模型 — `/model add`

在 TUI 中输入 `/model add` 可重新进入相同向导，添加更多模型（例如 `deepseek-v4-flash` 用于低成本迭代）。新模型添加后立即激活。随时通过 `/model` 命令切换模型。

### 手动配置（可选）

也可以直接编辑 `~/.axiomate.json`：

```jsonc
{
  "models": {
    "deepseek-v4-pro": {
      "model": "deepseek-v4-pro",
      "protocol": "openai-chat",
      "baseUrl": "https://api.deepseek.com",
      "apiKey": "sk-...",
      "contextWindow": 1000000,
      "supportsImages": false,
      "thinking": { "enabled": true, "effort": "max" }
    }
  },
  "currentModel": "deepseek-v4-pro"
}
```

## 3. 开始使用

```bash
cd /path/to/my-project
axiomate
```

Axiomate 进入项目目录，加载 DeepSeek 模型，启动 Agent 编程会话 — 支持文件编辑、Shell 执行、代码搜索等，全部由 DeepSeek V4 的 100 万 token 上下文窗口和扩展推理驱动。

## 4. 桌面自动化：UIA/AX Computer Use（适用于纯文本模型）

DeepSeek V4 不支持视觉输入，但 Axiomate 的 Computer Use 层通过 **UIAutomation / 无障碍（UIA/AX）原生绑定** 和 **Set-of-Mark (SOM) 覆盖层** 进行补偿：

- **`screenshot`** — 截取屏幕并附加坐标标尺，让模型通过文本描述推理空间布局
- **`zoom`** — 截取区域并在每个检测到的 UI 元素上叠加编号 SOM 标记，模型可通过索引引用元素而非像素坐标
- **UIA 元素检测**（Windows）— 使用原生 UIAutomation 识别按钮、文本框、菜单等控件，提供像素级精确边界框
- **无障碍树**（macOS）— 使用 AX API 实现等效的元素发现

这意味着 DeepSeek V4 Pro 可以驱动桌面应用 — 点击、输入、滚动、读取 UI 状态 — 无需视觉模型。SOM 覆盖层将视觉信息转换为结构化文本，推理模型可以很好地处理。

## 相关资源

- [Axiomate GitHub](https://github.com/axiomates/axiomate-agent)
- [DeepSeek 开放平台](https://platform.deepseek.com/) — 获取 API Key
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/) — 模型参考
