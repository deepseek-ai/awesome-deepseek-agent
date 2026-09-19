[English](./maka.md) | [简体中文](./maka.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Maka

[Maka](https://github.com/maka-agent/maka-agent) 是一个开源、本地优先的桌面与终端 AI Agent 工作台，提供持久化项目会话、文件与 Shell 工具、Skills 和多模型连接。

- **GitHub：** <https://github.com/maka-agent/maka-agent>
- **Releases：** <https://github.com/maka-agent/maka-agent/releases/latest>

#### 1. 安装 Maka

目前公开安装包支持 Apple Silicon macOS。前往 [Maka 最新 Release](https://github.com/maka-agent/maka-agent/releases/latest)，下载 `Maka-<version>-mac-arm64.dmg` 及其 `.sha256` 文件。

打开安装包前可以先校验文件：

```shell
shasum -a 256 -c Maka-<version>-mac-arm64.dmg.sha256
```

打开 DMG，将 **Maka** 拖入 **Applications（应用程序）**，然后从 Finder 启动。

#### 2. 获取 DeepSeek API Key

打开 [DeepSeek API Keys 页面](https://platform.deepseek.com/api_keys)，创建并复制 API Key。Maka 会将模型凭据保存在本机，不会把 Key 写入项目文件。

#### 3. 添加 DeepSeek 连接

1. 在 Maka 中打开 **设置 → 模型**。
2. 选择 **API** 标签页，找到并打开 **DeepSeek** 供应商卡片。
3. 粘贴 API Key，点击 **保存供应商**。Maka 默认使用官方服务地址 `https://api.deepseek.com`，并自动拉取实时模型目录。
4. 打开新建的 DeepSeek 连接，在 **模型管理** 中启用 `deepseek-v4-flash` 和 `deepseek-v4-pro`。如果暂时看不到这两个模型，点击 **更新模型目录**。
5. 将 **DeepSeek V4 Flash**（`deepseek-v4-flash`）设为此连接的默认模型，点击 **测试连接**，成功后再点击 **设为默认连接**。

Maka 内置的模型元数据会为两个 DeepSeek V4 模型配置 **100 万 token 上下文窗口**和最高 **38.4 万输出 token**，无需手动填写 context window。

#### 4. 选择最高推理强度

新建任务，在输入框旁的模型选择器中选择 **DeepSeek V4 Flash**。打开模型选择器里的 **思考级别**，选择 **最高**。

对于 `deepseek-v4-flash`，Maka 会将该选项映射为 `reasoning_effort: "max"`。需要使用 Pro 模型时，可以在同一个模型选择器中切换到 **DeepSeek V4 Pro**。

#### 5. 执行第一个 Agent 任务

打开一个临时项目目录，发送一个会使用工具的小任务，例如：

```text
创建文件 deepseek-maka-smoke.txt，内容必须恰好为：
DeepSeek V4 works in Maka
然后重新读取该文件并报告结果。
```

工具执行前如果出现权限提示，请先检查操作内容再批准。运行成功后，Maka 会创建文件、重新读取，并返回相同文本。

#### 常见问题

- **看不到 V4 模型：** 打开该连接并点击 **更新模型目录**，确认模型 ID 分别为 `deepseek-v4-flash` 和 `deepseek-v4-pro`。
- **没有“最高”选项：** 在当前任务中选择 `deepseek-v4-flash`，再重新打开模型选择器里的 **思考级别**。
- **鉴权失败：** 在 DeepSeek 开放平台重新创建 API Key，然后更新连接中的模型密钥。
- **返回余额错误：** 前往 DeepSeek 开放平台检查账户余额和计费状态。
- **无法安装应用：** 当前公开版本仅支持 Apple Silicon macOS，暂未提供 Intel macOS、Windows 或 Linux 安装包。

#### 相关资源

- [Maka 仓库](https://github.com/maka-agent/maka-agent)
- [Maka Releases](https://github.com/maka-agent/maka-agent/releases/latest)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
- [DeepSeek 思考模式](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)
