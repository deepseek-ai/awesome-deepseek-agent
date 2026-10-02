[English](./limitcode.md) | [简体中文](./limitcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Limitcode

Limitcode 是一个面向 Sublime Text 的轻量级 AI 编程助手 —— 侧边流式对话、多供应商支持，以及刻意精简、便于审查的工具集。

#### 1. 安装 Limitcode

打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`），运行 `Package Control: Install Package`，搜索 `Limitcode`。

#### 2. 运行与配置

- 在命令面板运行 `Limitcode: Setup Provider API Key`<br/>
- 选择 `deepseek` 供应商，粘贴你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)<br/>
- 运行 `Limitcode: Change Model`，选择 `deepseek-v4-pro`（或选择 `deepseek-v4-flash`，更快更省）<br/>
- 运行 `Limitcode: Open Chat`，开始对话

#### 3. 推理强度

为获得最佳编程体验，运行 `Limitcode: Set Reasoning Effort` 并选择 `high` —— 这是 Limitcode 提供的最高档位，会映射到请求体中的 `reasoning_effort` 字段。

#### 上下文窗口

DeepSeek-V4 模型最高支持 **100 万 token** 上下文。Limitcode 不提供上下文窗口设置项，会直接使用模型支持的上下文长度，因此处理大文件和长会话开箱即用。

#### 说明

- Agent 只能读取和编辑已在标签页中打开的文件 —— 发送请求前请先打开你希望它处理的所有文件。
- 可选：如果已安装 [LSP](https://packagecontrol.io/packages/LSP) 包，Limitcode 会在每次编辑后使用其诊断信息，让 Agent 自动发现语法和类型错误。
