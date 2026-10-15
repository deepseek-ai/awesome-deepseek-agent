[English](./orca-desktop.md) | [简体中文](./orca-desktop.zh-CN.md) · [返回](../README.zh-CN.md)

# 集成 O.R.C.A. Desktop

[O.R.C.A.](https://github.com/nanbo0ne/O.R.C.A-for-Windows)（Open Reasoning & Computing Agent）是使用 Go 和 Wails 开发的开源桌面助手与编程工作区，支持 DeepSeek 对话、项目文件、工具调用、子代理、MCP 和 Skills，并提供 Modern 与 Classic 两种界面。

本指南适用于桌面正式版 **3.0.13**。项目地址为 `nanbo0ne/O.R.C.A-for-Windows`，与 `echoVic/blade-deepseek` 的 Rust 终端工具 Orca 是不同项目。

## 1. 安装

在 [3.0.13 发布页](https://github.com/nanbo0ne/O.R.C.A-for-Windows/releases/tag/desktop-v3.0.13)下载对应平台的安装包：

- Windows x64：安装器或便携 ZIP。便携包需要解压后运行 `Orca.exe`；系统需要 WebView2。
- macOS 12 及以上：适用于 Intel 与 Apple Silicon 的 Universal DMG。
- Linux x64：Debian/Ubuntu 使用 DEB，并准备对应的 GTK/WebKitGTK 运行库。

核对发布页的摘要与安装说明。Windows 安装包尚无 Authenticode 发布者签名，macOS 包尚未公证；更新签名与操作系统发布者签名是两回事。

## 2. 配置 DeepSeek

1. 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)获取 API Key。
2. 启动 O.R.C.A.，在首次配置页的 **DEEPSEEK_API_KEY** 输入框填写密钥并提交验证。此桌面配置流程无需另外设置终端环境变量。
3. 内置供应商直连 `https://api.deepseek.com`。新安装默认选择 **DeepSeek V4.1 Flash**，其 API 模型 ID 为 `deepseek-flash`，O.R.C.A. 完整模型引用为 `deepseek/deepseek-flash`。
4. 如果首次启动时跳过了配置，可以在模型与供应商设置中配置内置 DeepSeek。跳过配置不代表附送免费密钥。

密钥只填写到凭据输入框，不要发送到聊天或写入项目文件。API 调用由 DeepSeek 计费。

## 3. 选择模型与思考强度

使用消息输入框旁的模型选择器：

| 模型 | API ID | O.R.C.A. 完整引用 | 图片 |
| --- | --- | --- | --- |
| DeepSeek V4.1 Flash | `deepseek-flash` | `deepseek/deepseek-flash` | 支持 |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `deepseek/deepseek-v4-pro` | 仅文本 |

此版本为以上官方模型提供 **1M token 上下文窗口**支持。实际上下文还包含指令与工具结果；模型允许的最大输出量并不等于应用每次请求的默认输出额度。

需要最高思考强度时，在强度选择器中选择 **max**，也可以按任务选择 **low**、**high** 或 **auto**。内置 DeepSeek 配置的 auto 使用 high。“简略/详细”只控制 reasoning 的显示，不改变思考强度。

旧 ID `deepseek-v4-flash` 和 `deepseek-v4-flash-vision-exp` 为兼容别名，无需当作额外模型添加。服务端最新可用性与协议以[官方模型目录](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)和[思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode/)为准。

## 4. 第一次使用

新建会话并发送：

> 用三个简短要点解释进程与线程的区别。

要测试编程工具，打开一个临时项目目录，选择编程模式，并将权限保持为“询问”：

> 列出这个项目的文件并解释入口。不要修改文件，不要安装依赖。

检查工具请求后再批准。文字回答可以验证对话链路，查看实际工具结果可以验证工具执行。子代理、MCP 和 Skills 可稍后配置，首次使用无需启用。

要测试识图，选择 Flash，添加一张愿意发送给 DeepSeek 的合成图片，让模型抄录可见文字。图片会发送给已配置的供应商，并受到附件权限控制；Pro 不支持图片输入。

## 故障排查与范围

- 认证失败或余额不足：在 DeepSeek 开放平台检查密钥和余额，不要将密钥贴到 Issue。
- 模型不可用：核对当前供应商与准确 API 模型 ID。自定义网关可能提供不同模型，显示名称相同不代表协议兼容。
- reasoning 或工具协议错误：使用较新的正式版本，报告版本号及脱敏错误。不要把关闭思考当作通用修复方法。
- 工具审批被拒绝：检查请求动作和工作区范围。完成配置不要求开启完全访问权限。
- 3.0.13 的托管本地 AI 与整机 Computer Use 仍处于禁用状态。本指南不包含尚未发布的内置浏览器预览版。

更多配置、平台依赖与限制请查看项目的[中文文档](https://github.com/nanbo0ne/O.R.C.A-for-Windows/blob/desktop-v3.0.13/README.md)。
