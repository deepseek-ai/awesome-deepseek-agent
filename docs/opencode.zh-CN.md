[English](./opencode.md) | [简体中文](./opencode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenCode

OpenCode 是一个开源 AI 编程助手，提供终端、网页等运行形式。

#### 1. 安装 OpenCode 终端

OpenCode 通过 npm 安装，请先安装 [Node.js](https://nodejs.org/zh-cn/download)（LTS 版本即可）。

Node.js 安装完毕后，在终端键入

```bash
npm i -g opencode-ai
```

> 也可通过 `curl -fsSL https://opencode.ai/install | bash`、`brew install anomalyco/tap/opencode` 等方式安装，详见[官方下载页](https://opencode.ai/zh/download)。

为避免兼容性问题，强烈建议升级至最新版本，确保版本号 >= v1.14.24。

#### 2. 运行与配置

- 执行 `opencode` 命令<br/>
- 输入框中输入 `/connect`，然后输入 `deepseek` 并选择供应商<br/>
- 填入 [DeepSeek API Key](https://platform.deepseek.com/api_keys)<br/>
- 选择 DeepSeek-V4-Pro 模型
- 在 Select variant 对话框中，选择 max
