[English](./openagentd.md) | [简体中文](./openagentd.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenAgentd

OpenAgentd 是一个开源的移动优先本地 AI Agent 控制台（Cockpit）。它包含跨平台桌面客户端（macOS、Windows、Linux）、移动端 Shell、FastAPI 后端以及 React Web UI，原生支持多 Agent 协同、命令行交互与 MCP 协议。

#### 1. 安装 OpenAgentd

你可以选择安装 **桌面客户端（Desktop App）** 或 **CLI / 后端服务**。

##### 选项 A：桌面客户端（命令行一键安装）

在终端中运行对应系统的安装命令：

**macOS / Linux**：
```bash
curl -fsSL https://raw.githubusercontent.com/lthoangg/openagentd/main/install.sh | sh
```

**Windows (PowerShell)**：
```powershell
irm https://raw.githubusercontent.com/lthoangg/openagentd/main/install.ps1 | iex
```

**Windows (Command Prompt / CMD)**：
```cmd
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/lthoangg/openagentd/main/install.ps1 | iex"
```

> **说明：** 桌面端独立安装包（DMG、MSI、AppImage、Deb）也可在 [OpenAgentd Releases](https://github.com/lthoangg/openagentd/releases/latest) 页面下载。安装完成后，可从应用程序文件夹或开始菜单启动 **OpenAgentd**。

##### 选项 B：CLI / 后端服务

使用 `uv` 或 `pip` 安装：

```bash
uv tool install openagentd
```

或使用 `pip`：

```bash
pip install openagentd
```

验证安装：

```bash
openagentd --version
```

#### 2. 配置 DeepSeek 提供商

OpenAgentd 原生支持 DeepSeek，既可以使用自备 API Key 直连，也支持开箱即用的免 Key 免费模型（`opencode:deepseek-v4-flash-free`）。

配置 DeepSeek 官方 API Key 直连步骤如下：

1. 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。
2. 设置 `DEEPSEEK_API_KEY` 环境变量：

**macOS / Linux**：
```bash
export DEEPSEEK_API_KEY="sk-..."
```

**Windows (PowerShell)**：
```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

**Windows (CMD)**：
```cmd
set DEEPSEEK_API_KEY=sk-...
```

也可以通过以下方式配置：
- 在 Web / 桌面客户端 UI 中：**设置 → 提供商 → DeepSeek**
- 或在 `~/.config/openagentd/.env` 中添加：
  ```env
  DEEPSEEK_API_KEY=sk-...
  ```

#### 3. 选择模型与配置 Agent

OpenAgentd 的 Agent 配置文件保存在 `~/.config/openagentd/agents/` 目录中（带有 YAML frontmatter 的 Markdown 文件）。

将主控 Agent（Lead Agent）模型设置为 DeepSeek V4：

编辑 `~/.config/openagentd/agents/lead.md`：

```yaml
---
name: lead
description: 主控协调 Agent
model: deepseek:deepseek-v4-flash
---
```

如需进行高难度推理编码任务，可选择 `deepseek-v4-pro`：

```yaml
---
name: lead
description: 主控协调 Agent
model: deepseek:deepseek-v4-pro
---
```

OpenAgentd 原生适配 DeepSeek V4 特性：
- **100 万 Token 上下文**：完整支持 1,048,576 Token 上下文窗口。
- **深度思考/推理模式**：原生支持推理开关（`thinking: {type: "enabled"}`）与推理强度控制，并正确处理工具调用过程中的 `reasoning_content`。

#### 4. 开始使用

从系统菜单启动 OpenAgentd 桌面应用，或在终端中运行后端服务：

```bash
openagentd
```

开启局域网/跨设备连接：

```bash
openagentd start --lan --key
```

或直接启动终端交互式对话：

```bash
openagentd chat
```

你也可以在应用界面或客户端设置中随时动态切换模型。
