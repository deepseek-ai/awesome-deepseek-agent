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

##### API Key 准备
 打开[LangRouter官网](https://langrouter.ai/)，注册一个账号，保存api-key。备注：可免费体验的。

##### 运行
```bash
# 启动Langcli
langcli

# 之后在回话中输入:
hi
```
