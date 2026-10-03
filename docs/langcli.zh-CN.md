[English](./langcli.md) | [简体中文](./langcli.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Langcli

[Langcli](https://langcli.com) 是一个 AI 编程助手，支持 CLI 和 Zed ACP Agent。

#### 1. 安装

##### 快速安装 (推荐)

macOS、Linux 和 WSL 用户执行以下命令安装 Langcli：

```bash
bash -c "$(curl -fsSL https://assets.langcli.com/installation/install-langcli.sh)"
```

Windows 用户执行以下命令安装(请以Administrator身份运行Power shell)：

```cmd
cmd /c "curl -fsSL -o %TEMP%\install-langcli.bat https://assets.langcli.com/installation/install-langcli.bat && %TEMP%\install-langcli.bat"
```
> **注意：建议安装后重启终端，以确保环境变量生效。

##### 手动安装

请确保你已安装 Node.js 20 或更高版本。如果还没安装，请到[nodejs.org](https://nodejs.org/en/download)下载和安装.
```bash
npm i -g langcli-com
```

#### 2. 快速开始

##### API Key 与提供商（建议使用 DeepSeek 官方）

方案 A — DeepSeek 官方（推荐）

1. 获取 DeepSeek API Key：访问 [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)，创建或复制你的 API Key。
2. 将 Langcli 配置为使用 DeepSeek 的 Anthropic 兼容端点。设置以下环境变量：

```bash
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="<你的 DeepSeek API Key>"
export ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash[1m]"
```

将模型设置为 `deepseek-v4-pro[1m]` 或 `deepseek-v4-flash[1m]`。`[1m]` 后缀用于启用 100 万 token 的完整上下文窗口。更多配置选项请参阅 [Langcli 文档](https://langcli.com/docs)。

方案 B — 第三方路由器（可选）

部分用户也会通过第三方服务（例如 LangRouter）中转 API 请求。这些为第三方服务，**不由 DeepSeek 维护或背书**。如选择使用，请向该服务提供商获取凭证并按说明操作。使用第三方路由器需自行评估风险——官方端点兼容性与安全性最佳，建议优先使用。

##### 运行
```bash
# 启动Langcli
langcli

# 之后在回话中输入:
hi
```
