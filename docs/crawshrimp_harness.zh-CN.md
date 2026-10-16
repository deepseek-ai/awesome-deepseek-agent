[English](./crawshrimp_harness.md) | [简体中文](./crawshrimp_harness.zh-CN.md) · [← Back](../README.zh-CN.md)

# 接入 Crawshrimp Harness（抓虾）

Crawshrimp Harness（抓虾）是基于 DeepSeek Harness（DSH）的开源、本地优先电商运营桌面智能体，将 DSH 会话与浏览器自动化、文件和 Office 工具、可复用运营脚本及权限审批集成在一起。用户可通过内置官方 Provider 接入自己的 DeepSeek API Key，本地智能体功能无需登录抓虾账号。

- **GitHub：** <https://github.com/howtimeschange/crawshrimp-harness>
- **下载：** <https://github.com/howtimeschange/crawshrimp-harness/releases>
- **许可证：** Apache-2.0

以下步骤对应 **v0.4.0** 桌面版，使用应用中的实际中文界面名称。

#### 1. 安装抓虾 Harness

从 [v0.4.0 Release](https://github.com/howtimeschange/crawshrimp-harness/releases/tag/v0.4.0) 下载适合自己电脑的安装包：

| 平台 | 安装包 |
| --- | --- |
| macOS，Apple Silicon | `crawshrimp-harness-v0.4.0-mac-arm64.dmg` |
| macOS，Intel | `crawshrimp-harness-v0.4.0-mac-x64.dmg` |
| Windows，x64 | `crawshrimp-harness-v0.4.0-win-x64.exe` |

macOS 打开 DMG 后将应用复制到“应用程序”；Windows 运行安装器。启动抓虾 Harness，等待本地智能体运行时就绪。桌面安装包已集成 DSH，无需单独安装 DSH CLI。

下方的浏览器任务需要已安装受支持的浏览器，例如 [Google Chrome](https://www.google.com/chrome/)。抓虾会启动使用独立用户目录的专用浏览器实例；如果没有检测到受支持的浏览器，应用会提示选择浏览器可执行文件。

#### 2. 配置 DeepSeek 官方 Provider

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，并确保 API 账户有可用余额。API 调用由 DeepSeek 计费，价格以[官方当前定价](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)为准。

1. 打开 **设置 → AI 能力 → 文本大模型**。
2. 找到内置的 **DeepSeek 官方** Provider，点击 **编辑**。
3. 在 **连接配置** 中，将 **Base URL** 保持为 `https://api.deepseek.com`，把密钥粘贴到 **API Key**。内置 Provider 已使用 OpenAI 兼容协议。
4. 点击 **保存 Provider**。设置会保存并请求重新加载运行时，等待运行时就绪；如果还有正在执行的任务，先等待任务结束，再按设置页提示重启运行时。
5. 确认 Provider 显示 **已配 Key**。保存后设置表单不会回读真实密钥；后续编辑时，API Key 留空会保留已有密钥。

本指南使用内置 **DeepSeek 官方** Provider 直连官方 API。它的 Key 和 Base URL 与应用中其他 Provider 独立配置。

#### 3. 选择模型与思考强度

新建智能体会话，在模型菜单中选择 **DeepSeek 官方** Provider 下的模型。内置预设对应关系如下：

| 模型预设 | DeepSeek API 模型 ID |
| --- | --- |
| DeepSeek V4.1 Flash | `deepseek-flash` |
| DeepSeek V4 Pro | `deepseek-v4-pro` |

首次使用建议选择 **DeepSeek V4.1 Flash**。应用会自动将内置预设映射到上述 API ID；`deepseek-flash` 是[官方当前模型目录](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)列出的 Flash ID。

两个官方预设均登记了 **1,000,000 token（1M）上下文窗口**，使用此 OpenAI 兼容 Provider 时无需手工设置上下文窗口，也无需在模型名后添加 `[1m]`。这是模型配置容量，实际保留的历史还会受到会话压缩及用户自行保存的模型预算覆盖值影响。

处理复杂任务时，打开会话的模型选择器，在 **推理等级** 中选择 **Max**。对于这两个官方预设，该选项会开启思考模式，并向 DeepSeek 发送 `reasoning_effort: "max"`。**Default** 沿用供应商默认行为，**Off** 则明确关闭思考。工具调用会话中的助手历史会保留 `reasoning_content` 并回传，遵循 [DeepSeek 思考模式 API](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)的要求。

#### 4. 运行第一个任务

在新会话中发送一个简单的浏览器任务，例如：

```text
用浏览器打开 https://api-docs.deepseek.com/，
查看页面并用三条要点总结文档的主要栏目。这个任务只读取页面。
```

智能体应打开浏览器页面、通过浏览器工具查看内容并返回总结。检查会话中的工具结果和浏览器预览，确认页面确实已打开。若当前权限模式要求审批，请先核对会话中展示的操作，再允许执行。

完成后，可以在同一会话中继续进行电商浏览器任务、本地文件处理和 Office 工作。标准轻量桌面包会在需要原生预览或转换时按需下载 Office 组件。

#### 5. 常见问题

- **鉴权或余额错误：** 检查 API Key、`https://api.deepseek.com` Base URL，以及官方平台中的 API 余额。
- **找不到模型：** 确认已保存 **DeepSeek 官方** Provider。在其 **模型管理** 标签中点击 **恢复预设模型** 可恢复内置模型，之后保存 Provider；也可以通过 **获取最新模型 → 添加所选模型** 导入选中的上游模型。
- **保存后没有生效：** 查看设置页的运行时状态提示。正在执行的任务可能推迟重启，等待任务完成并重启运行时后再重试。
