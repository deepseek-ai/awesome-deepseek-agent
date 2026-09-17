[English](./reasonix.md) | [简体中文](./reasonix.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Reasonix

Reasonix 是一款以 DeepSeek 为原生后端的终端编程 Agent。设计围绕 DeepSeek API 展开 —— Cache-First 循环、Flash 优先的成本控制、工具调用自动修复 —— 直接对接 `api.deepseek.com`，不需要协议转换层。

#### 1. 安装 Node.js

- 安装 [Node.js](https://nodejs.org/en/download/) 20.10 及以上版本。
- Windows 用户请安装 [Git for Windows](https://git-scm.com/download/win)。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。Reasonix 首次启动会有内置向导询问 Key 并持久化到 `~/.reasonix/config.json` —— 无需配置环境变量。

#### 3. 进入项目目录，执行 `npx reasonix code` 即可开始使用。

```
cd /path/to/my-project
npx reasonix code
```

无需全局安装。Reasonix 默认使用 **DeepSeek-V4.1-Flash**。旧有的 Pro 选项将在 2026 年 9 月 14 日后路由到 V4.1 Flash。输入 `/help` 查看完整 slash 命令参考。

<div align="center">
<img src="https://raw.githubusercontent.com/esengine/reasonix/main/docs/logo.svg" width='640' />
</div>
