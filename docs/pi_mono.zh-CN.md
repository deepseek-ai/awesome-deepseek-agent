[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Pi

Pi 是一个极简且高度可扩展的终端编码框架。它通过 TypeScript 扩展、技能、提示模板和主题来适配你的工作流，支持树状会话结构，并内置 DeepSeek 支持。

#### 1. 安装 Pi

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 22.19 或更高版本。
- 在命令行界面，执行以下命令安装 Pi：

```bash
npm install -g @earendil-works/pi-coding-agent
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```bash
pi --version
```

本指南要求使用 Pi 0.83.0 或更高版本。如果 `pi --version` 显示的版本较旧，请升级到最新版本：

```bash
npm install -g @earendil-works/pi-coding-agent@latest
```

> **注意：** Linux / macOS 用户也可以通过官方脚本安装：
> ```bash
> curl -fsSL https://pi.dev/install.sh | sh
> ```

#### 2. 配置 DeepSeek

Pi 已将 DeepSeek 作为内置供应商，因此无需创建或编辑 `models.json`。请先从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后选择以下任一认证方式。

**方式一：环境变量**

Linux / macOS 用户：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows 用户：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

**方式二：Pi 登录**

跳过环境变量，在下一步启动 Pi 后使用 `/login`。Pi 会将 API Key 保存到 `auth.json`：Linux 和 macOS 路径为 `~/.pi/agent/auth.json`，Windows 路径为 `%USERPROFILE%\.pi\agent\auth.json`。

#### 3. 运行并选择模型

进入项目目录并启动 Pi：

```bash
cd /path/to/my-project
pi
```

首次启动时，Pi 会初始化其 `.pi` 配置目录。如果你选择了上面的 **Pi 登录**，请输入以下命令，选择 **DeepSeek**，然后粘贴 API Key：

```text
/login
```

输入以下命令打开模型切换器：

```text
/model
```

选择 **deepseek**，然后选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`。

DeepSeek 默认使用 `high` 推理强度。对于复杂的编码和 Agent 任务，可以打开设置并选择 `max`：

```text
/settings
```

一般任务保持 `high` 即可。Pi 的内置 DeepSeek 配置已包含 100 万 token 上下文窗口和最大 38.4 万 token 输出。

有关供应商认证和自定义模型覆盖的更多信息，请参阅 [Pi 供应商文档](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/providers.md)和[自定义模型文档](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md)。
