[English](./github_copilot.md) | [简体中文](./github_copilot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 GitHub Copilot

**DeepSeek V4 for Copilot Chat** 是一个 VS Code 插件，将 DeepSeek V4 Pro 和 Flash 直接添加到 GitHub Copilot 的模型选择器中。但此插件尚未在扩展商店上架。
**OAI Compatible Copilot** 是一个 VS Code 插件，允许用户将任意兼容 OpenAI API 的模型接入 GitHub Copilot Chat 中使用。

您可以[选择 OAI Compatible Copilot 插件的方式](#以-openai-兼容的方式接入-copilot)接入 DeepSeek，或直接安装[DeepSeek For Copilot 插件](#使用-deepseek-for-copilot-插件接入)（推荐）。


### 以 OpenAI 兼容的方式接入 Copilot 

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

### 使用 Deepseek For Copilot 插件接入

#### 1. 安装插件
- 安装 [VS Code](https://code.visualstudio.com/) 1.116 或更高版本。
- 确保已有 GitHub Copilot 订阅（Free / Pro / Enterprise 均可，免费版即可使用）。
- 从 [Github Release](https://github.com/Vizards/deepseek-v4-for-copilot/releases) 页面下载最新版本的 Deepseek For Copilot 插件（`.vsix` 文件）。
- 在 VS Code 中安装插件：打开命令面板（`Cmd+Shift+P` / `Ctrl+Shift+P`），输入`vsix`，选取 `Extensions: Install from VSIX...`，选择下载的 `deepseek-v4-for-copilot-x.y.z.vsix` 文件进行安装。

#### 2. 获取 DeepSeek API Key
- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
- 复制 Key（以 `sk-` 开头）。

#### 3. 在 VS Code 中配置 API Key
- 打开命令面板（`Cmd+Shift+P` / `Ctrl+Shift+P`）。
- 执行 **Deepseek: Set API Key**
- 在输入框中粘贴 API Key，完成后按回车确认。
- Key 会安全存储在操作系统密钥链中，不会写入磁盘
- 插件会自动将 DeepSeek 注册为 Copilot 的一个模型提供商，无需手动添加 Provider 和 Model。

#### 4. 选择模型并开始对话
- 打开 Copilot Chat（`Cmd+Shift+I` / `Ctrl+Shift+I`）。
- 点击聊天区域下方的模型选择器，点击齿轮设置图标
- 选择 **DeepSeek V4 Pro** 或 **DeepSeek V4 Flash**，将前面的眼睛图标点亮
- 即可开始对话 — Agent 模式、工具调用及所有 Copilot 功能均可直接使用。

#### 可选：配置思考深度

在模型选择器中，点击齿轮图标进入“管理语言模型”界面，点击 DeepSeek 模型旁的齿轮图标可选取思考深度：

- None — 最快，不启用推理。
- High — 平衡模式（默认）。
- Max — 深度推理，适合复杂任务。

#### 可选：视觉支持

DeepSeek V4 为纯文本模型，但插件会自动处理图片。将截图拖入对话后，插件会通过其他已安装的 Copilot 模型（如 Claude、GPT-4o）描述图片内容，再发送给 DeepSeek。执行 DeepSeek: Set Vision Proxy Model 可选择用于图片描述的模型。