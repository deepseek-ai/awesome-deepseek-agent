[English](./github_copilot.md) | [简体中文](./github_copilot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 GitHub Copilot

**OAI Compatible Copilot** 是一个 VS Code 插件，允许用户将任意兼容 OpenAI API 的模型接入 GitHub Copilot Chat 中使用。通过这个插件，用户可以在 Copilot Chat 中直接使用 DeepSeek 的强大功能，无需等待官方集成。

#### 1. 安装插件

- 安装 [VS Code](https://code.visualstudio.com/) 1.116 或更高版本。
- 确保已有 GitHub Copilot 订阅（Free / Pro / Enterprise 均可，免费版即可使用）。
- 从 [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=johnny-zhao.oai-compatible-copilot) 安装 OAI Compatible Copilot 插件。

#### 2. 获取 DeepSeek API Key

- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
- 复制 Key（以 `sk-` 开头）。

#### 3. 在 VS Code 中配置 API Key

- 打开命令面板（`Cmd+Shift+P` / `Ctrl+Shift+P`）。
- 执行 **OAICopilot: Open Configuration UI** 
- 在新打开的设置界面中，在下方找到 **Provider Management** 区域，点击 **Add Provider**。
- 在新展开的输入框中，自定义 Provider Name（如 "DeepSeek"）并粘贴 Base URL（默认为 `https://api.deepseek.com`）和 API Key。完成后点击`save`。
- Key 会安全存储在操作系统密钥链中，不会写入磁盘。

#### 4. 注册模型
- 在同一设置界面，找到 **Model Management** 区域，点击 **Add Model**。
- 选取刚刚创建的 Provider ID，点开 Model ID，下方会自动显示可用模型列表，选择 **DeepSeek V4 Pro** 和 **DeepSeek V4 Flash**（如果没有，请检查上面的配置是否正确）
- 将 `Context Length` 设置为 `1000000` ，`Max Tokens` 设置为 `384000` 以启用 1M 上下文支持
- 若要子定义配置 Thinking Mode，请在 Advanced Settings 中将 `Enable Thinking` 设置为 `True`，并将 `Reasoning Effort` 设置为 `max`（支持的字段：`high` `max`）
- 按需配置其他参数，点击 `save`。


#### 4. 选择模型并开始对话

- 打开 Copilot Chat（`Cmd+Shift+I` / `Ctrl+Shift+I`）。
- 点击聊天区域下方的模型选择器，点击齿轮设置图标
- 选择 **DeepSeek V4 Pro** 或 **DeepSeek V4 Flash**，将前面的眼睛图标点亮
- 即可开始对话 — Agent 模式、工具调用及所有 Copilot 功能均可直接使用。


