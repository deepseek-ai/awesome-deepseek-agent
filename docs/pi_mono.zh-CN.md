[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Pi

Pi（pi-mono）是一个极简且高度可扩展的终端编码框架，内置供应商和模型目录。官方网站：[pi.dev](https://pi.dev/)。

#### 1. 安装 Pi

使用 Pi 官方安装脚本：

- **Linux / macOS**

  ```bash
  curl -fsSL https://pi.dev/install.sh | sh
  ```

- **Windows（PowerShell）**

  ```powershell
  irm https://pi.dev/install.ps1 | iex
  ```

> **Windows 注意事项：** Pi 的 shell 工具需要 Bash shell。请安装 [Git for Windows](https://git-scm.com/download/win)，或提供其他 Bash 可执行文件。

安装后执行以下命令验证：

```bash
pi --version
```

#### 2. 配置 DeepSeek 供应商

DeepSeek 是 Pi 内置的 API Key 供应商，无需创建或编辑 `models.json`。

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key 后，进入项目目录并启动 Pi：

```bash
cd /path/to/my-project
pi
```

在 Pi 中依次操作：

1. 输入 `/login`。
2. 选择 **Sign in with an API key**。
3. 搜索并选择 **DeepSeek**。
4. 粘贴 DeepSeek API Key，按 Enter 保存。

Pi 会在本地保存凭据，并自动提供 DeepSeek 模型。

#### 3. 选择模型并开始使用

输入 `/model`（或按 Ctrl+L），搜索 `deepseek` 并选择模型。

Pi 内置目录目前提供 `deepseek-v4-pro` 和 `deepseek-v4-flash`。两者均支持最高 100 万 token 上下文和 38.4 万 token 输出。进行高难度编码任务时，请选择 `deepseek-v4-pro`，然后按 Shift+Tab，直至思考等级显示为 `max`。

现在即可开始编码。

更多用法与配置请参阅 [Pi 文档](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent/docs)。
