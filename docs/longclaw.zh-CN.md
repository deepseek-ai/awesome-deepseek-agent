# LongClaw 接入 DeepSeek 指南

[English](./longclaw.md)

## 简介

[LongClaw](https://longclaw.cc) 是一款跨平台 AI 桌面助手，支持 Windows、macOS 和 Linux。它内置 ClawHub 技能市场，可通过技能扩展能力，同时支持 MCP（Model Context Protocol）协议接入外部工具。LongClaw 可接入微信、QQ、飞书等聊天工具，让 AI 能力无缝融入你的日常沟通。

## 准备工作

1. 访问 [DeepSeek 开放平台](https://platform.deepseek.com/) 注册并获取 API Key。
2. 下载并安装 LongClaw：[https://longclaw.cc/download](https://longclaw.cc/download)

## 安装

### Windows

下载 Windows 安装包（`.exe`），双击运行安装向导。

### macOS

下载 macOS 安装包（`.dmg`），拖拽到 Applications 文件夹。

### Linux

下载 Linux 安装包（`.AppImage` 或 `.deb`），赋予执行权限后运行：

```bash
chmod +x LongClaw-*.AppImage
./LongClaw-*.AppImage
```

## 配置 DeepSeek

1. 打开 LongClaw，进入「设置」→「模型配置」。
2. 点击「添加模型」，选择「OpenAI 兼容」类型。
3. 填写以下配置：
   - **API 端点**：`https://api.deepseek.com/v1`
   - **模型名称**：`deepseek-v4-pro`（推荐）或 `deepseek-v4-flash`
   - **API Key**：你的 DeepSeek API Key
   - **上下文窗口**：`1000000`（1M 上下文支持）
   - **最大 Token**：`384000`
4. 保存配置。

## 启用深度思考模式

DeepSeek V4 Pro 支持多种推理强度（`max` 和 `high`）。在 LongClaw 中：

1. 进入「设置」→「模型配置」→ 选择 DeepSeek 模型 →「高级选项」。
2. 在「额外参数」中添加：
   ```json
   {
     "reasoning_effort": "max"
   }
   ```
3. 保存后，所有使用该模型的对话将自动启用最高推理强度。

## 首次运行

1. 在 LongClaw 主界面，点击输入框上方的模型选择器，切换至 `deepseek-v4-pro`。
2. 开始对话，测试 DeepSeek 的回复效果。
3. 如需接入聊天工具，进入「设置」→「聊天工具」，按指引配置微信/QQ/飞书机器人。

## 技能市场扩展

LongClaw 支持通过 [ClawHub](https://clawhub.ai) 安装技能，扩展 AI 能力：

1. 点击侧边栏「技能市场」。
2. 搜索需要的技能（如「代码审查」「文档生成」）。
3. 一键安装，即刻使用。

## MCP 协议支持

LongClaw 原生支持 MCP 协议，可接入外部工具：

1. 进入「设置」→「MCP 工具」。
2. 添加 MCP 服务器配置（如文件系统、数据库、搜索等）。
3. AI 将自动调用这些工具完成任务。

## 相关资源

- [LongClaw 官网](https://longclaw.cc)
- [LongClaw 文档](https://docs.longclaw.cc)
- [ClawHub 技能市场](https://clawhub.ai)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
