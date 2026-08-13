[English](./synergy.md) | [简体中文](./synergy.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Synergy

Synergy 是一个开源的 AI Agent 工作台，将会话、Agents、文件、浏览器、工具、MCP 服务器与自动化统一到一个运行时中，可在 Web 工作台、桌面应用与 CLI 中使用。DeepSeek 是内置的模型提供商，只需一个 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 即可接入。

#### 1. 安装 Synergy

Linux / Windows / Mac 桌面版用户可从 [GitHub Releases](https://github.com/SII-Holos/synergy/releases/latest) 直接下载桌面版安装包。

无头环境用户、有 CLI 需求用户可执行以下命令安装：

```
curl -fsSL https://raw.githubusercontent.com/SII-Holos/synergy/main/install | bash
```

或通过 npm 安装：

```
npm install -g @ericsanchezok/synergy --registry https://registry.npmjs.org
```

#### 2. 配置 DeepSeek

桌面版直接打开 Synergy，如果是 CLI 用户，请执行以下命令打开 web 工作台：

```
synergy start
synergy web
```

打开 Synergy 工作台，点击 `设置`，选择 `提供商`，点击 `添加提供商`，在 `deepseek` 中填写 DeepSeek API Key。

#### 3. 使用 DeepSeek V4

在 `设置` 中点击 `模型`，将 `deepseek/deepseek-v4-pro` 设置为默认模型，并选择 max 思考。

说明：

- 内置的 `deepseek` 提供商已指向 `https://api.deepseek.com`，使用 OpenAI 兼容传输，无需额外配置 base URL。
- DeepSeek V4 默认开启思考模式（默认强度 `high`）。Synergy 将声明的强度暴露为模型变体，`max` 变体会发送 `reasoning_effort: "max"`，获得最佳编码体验。
- DeepSeek V4 支持 1M 上下文窗口。
- 设置修改会被自动监听，修改后无需重启，点击保存后下一次请求即生效。

#### 4. 开始使用

启动运行时并打开工作台，即可开始使用。
