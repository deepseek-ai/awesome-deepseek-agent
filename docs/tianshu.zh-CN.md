[English](./tianshu.md) | [简体中文](./tianshu.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 天枢 (Tianshu)

天枢（Tianshu）是一款开源的 Agentic 编程助手，提供终端与桌面端两种形态。它内置 DeepSeek 提供商预设，无需手动填写 endpoint 即可对接 `api.deepseek.com`。

#### 1. 安装 Node.js

- 安装 [Node.js](https://nodejs.org/en/download/) 24 及以上版本。
- Windows 用户请安装 [Git for Windows](https://git-scm.com/download/win)。

#### 2. 安装天枢 TUI

通过 npm 全局安装 CLI：

```bash
npm install -g tianshu-tui
```

#### 3. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

在终端中导出环境变量：

```bash
export DEEPSEEK_API_KEY="sk-..."
```

Windows（PowerShell）：

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

#### 4. 配置天枢使用 DeepSeek

在 TUI 中执行：

```bash
rivet config setup deepseek
```

或在桌面端打开 **设置 → 提供商**，选择 **DeepSeek**。

#### 5. 开始编码

进入项目目录并运行：

```bash
rivet
```

天枢内置支持 **DeepSeek-V4-Pro** 与 **DeepSeek-V4-Flash**，两款模型均支持最高 100 万 token 上下文。V4-Pro 配置为 `reasoningEffort: max`，最高可输出 384K token，适合复杂深度推理任务；V4-Flash 更适合快速、低成本的日常迭代。

<div align="center">
<img src="https://raw.githubusercontent.com/huiliyi37/Tianshu-Tui/main/assets/tianshu-banner-dark.jpg" width='640' />
</div>
