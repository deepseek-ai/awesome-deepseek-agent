[English](./echobird.md) | [简体中文](./echobird.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 EchoBird

EchoBird 是一款面向 AI 编程工具的桌面端控制中心，支持 Windows、macOS 和 Linux。无需手动修改配置文件——添加一次模型供应商，即可一键应用到 Claude Code、Codex 或 Claude Desktop。EchoBird 还内置「安装与修复」助手和量化分析工作台，都能运行在同一个模型上。

DeepSeek 是内置供应商：其 OpenAI 兼容端点（`https://api.deepseek.com`）与 Anthropic 兼容端点（`https://api.deepseek.com/anthropic`）均已预填，因此 EchoBird 能把 Claude Code、Claude Desktop 这类 Anthropic 协议工具直接指向 DeepSeek V4。

- **GitHub：** <https://github.com/edison7009/EchoBird>
- **官网：** <https://echobird.ai>

#### 1. 安装 EchoBird

从[官网](https://echobird.ai)或 [GitHub Releases](https://github.com/edison7009/EchoBird/releases) 下载对应平台的安装包。

#### 2. 添加 DeepSeek 模型

打开 **应用管理（App Manager）**，进入 **模型供应商（Model Providers）** 面板，从内置供应商列表中选择 **DeepSeek**。它的 **OpenAI URL**（`https://api.deepseek.com`）与 **Anthropic URL**（`https://api.deepseek.com/anthropic`）已为你预填。

1. 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
2. **Model ID** 填 **`deepseek-v4-pro`**（编程与推理最强），或 **`deepseek-v4-flash`**（更快、更省）。
3. 用于 Claude Code / Claude Desktop 时，在模型名后追加 `[1m]` 即可启用完整的 **100 万 token** 上下文，例如 **`deepseek-v4-pro[1m]`**。
4. 保存。

#### 3. 把 DeepSeek 应用到工具

在 **应用管理** 中选择目标工具——**Claude Code**、**Codex** 或 **Claude Desktop**——打开它的 **MODELS** 标签页，选中你的 DeepSeek 模型，点击 **更新模型配置（Update model config）**（或 **直接启动应用**）。EchoBird 会为该工具写入正确的配置：Anthropic 协议工具走 `/anthropic` 端点，OpenAI 兼容工具走 `https://api.deepseek.com`。

切换 Codex / Claude Desktop 的模型后，请保持 EchoBird 运行。

#### 4. 在「安装与修复」中对话

打开 **安装与修复** 页面，在右侧面板选中你的 DeepSeek 模型，内置助手即运行在 DeepSeek V4 上——用它来安装工具、修复损坏的配置、完成上手引导。

#### 注意事项

- **DeepSeek 请勿开启 API Router。** 直接指向 DeepSeek 时，请关闭 **API Router** 开关。它仅用于中转 / 路由端点，开启会破坏与 DeepSeek 的直连。
- **推理强度。** DeepSeek V4 Pro 默认开启深度思考。追求最佳编程效果时，请保持 `max` 推理档。
- **100 万上下文。** DeepSeek V4 支持最高 100 万 token；Anthropic 协议工具请按上文使用 `[1m]` 模型名后缀。
