[English](./github-copilot.md) | [简体中文](./github-copilot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 GitHub Copilot

**DeepSeek V4 for Copilot Chat** 是一个 VS Code 插件，将 DeepSeek V4 Pro 和 Flash 直接添加到 GitHub Copilot 的模型选择器中。你仍可使用 Copilot 的 Agent 模式、工具调用、Skills 和 MCP — 全部由 DeepSeek 驱动。

#### 1. 安装插件

- 安装 [VS Code](https://code.visualstudio.com/) 1.116 或更高版本。
- 确保已有 GitHub Copilot 订阅（Free / Pro / Enterprise 均可，免费版即可使用）。
- 从 [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Vizards.deepseek-v4-for-copilot) 安装插件。

#### 2. 获取 DeepSeek API Key

- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
- 复制 Key（以 `sk-` 开头）。

#### 3. 在 VS Code 中配置 API Key

- 打开命令面板（`Cmd+Shift+P` / `Ctrl+Shift+P`）。
- 执行 **DeepSeek: Set API Key** 并粘贴你的 Key。
- Key 会安全存储在操作系统密钥链中，不会写入磁盘。

#### 4. 选择模型并开始对话

- 打开 Copilot Chat（`Cmd+Shift+I` / `Ctrl+Shift+I`）。
- 点击聊天面板右上角的模型选择器。
- 选择 **DeepSeek V4 Pro** 或 **DeepSeek V4 Flash**。
- 即可开始对话 — Agent 模式、工具调用及所有 Copilot 功能均可直接使用。

#### 可选：配置思考深度

在模型选择器中，点击 DeepSeek 模型旁的齿轮图标可选择思考深度：
- **None** — 最快，不启用推理。
- **High** — 平衡模式（默认）。
- **Max** — 深度推理，适合复杂任务。

#### 可选：视觉支持

DeepSeek V4 为纯文本模型，但插件会自动处理图片。将截图拖入对话后，插件会通过其他已安装的 Copilot 模型（如 Claude、GPT-4o）描述图片内容，再发送给 DeepSeek。执行 **DeepSeek: Set Vision Proxy Model** 可选择用于图片描述的模型。

<div align="center">
<img src="https://raw.githubusercontent.com/Vizards/deepseek-v4-for-copilot/main/resources/screenshots/01-picker.png" width='1024' border='1'  />
</div>
