[English](./cline.md) | [简体中文](./cline.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Cline

Cline 是一款运行在 VS Code 中的 AI 编程助手扩展，支持多种 API 供应商和模型。

#### 1. 安装 Cline 扩展

- 打开 VS Code。
- 点击活动栏中的 **扩展** 图标（或按 `Ctrl+Shift+X`）。
- 搜索 `cline`。
- 在搜索结果中找到 **Cline** 扩展。

<div align="center">
<img src="./assets/cline_step_1.png" width="250" border="1" />
</div>

#### 2. 安装并信任扩展

- 点击 **Install** 按钮进行安装。
- 安装完成后，根据提示选择信任开发者。

#### 3. 选择 API Key 模式

- 在 Cline 设置中，选择 **Bring my own API Key**。

<div align="center">
<img src="./assets/cline_step_3.png" width="250" border="1" />
</div>

#### 4. 配置 API 供应商

**方法一：DeepSeek 供应商**

- 选择 **API Provider** 为 **DeepSeek**。
- 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- 选择要使用的模型。

> **注意：** `deepseek-reasoner` 和 `deepseek-chat` 模型即将废弃，请等待 Cline 官方添加 `deepseek-v4-pro` 和 `deepseek-v4-flash` 模型。

<div align="center">
<img src="./assets/cline_step_4_a.png" width="250" border="1" />
</div>

配置完成后即可开始使用：

<div align="center">
<img src="./assets/cline_step_5_a.png" width="250" border="1" />
</div>

**方法二：OpenAI Compatible**

- 选择 **API Provider** 为 **OpenAI Compatible**。
- **Base URL** 填入 `https://api.deepseek.com`。
- 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- 填入 **Model ID**，如 `deepseek-v4-pro`。
- （选做）点击 **Model Configuration**，调整窗口大小、温度、价格和限量等参数。

<div align="center">
<img src="./assets/cline_step_4_b.png" width="250" border="1" />
</div>

配置完成后即可开始使用：

<div align="center">
<img src="./assets/cline_step_5_b.png" width="250" border="1" />
</div>
