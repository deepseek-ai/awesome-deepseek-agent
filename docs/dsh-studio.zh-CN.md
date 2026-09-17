[English](./dsh-studio.md) | [简体中文](./dsh-studio.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 DSH Studio 中使用 DeepSeek

[DSH Studio](https://github.com/Moresyl/dsh-studio) 是一个采用 MIT 许可证的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 跨平台桌面外壳。它会把上游 Harness 安装到应用专属的 npm 目录中，监控本地服务，并直接承载未经修改的 Harness Web UI。

- **GitHub：** <https://github.com/Moresyl/dsh-studio>
- **发行版：** <https://github.com/Moresyl/dsh-studio/releases>

## 1. 安装 DSH Studio

DSH Studio 目前要求系统已安装 Node.js 20 或更高版本。请下载适合当前平台的发行包：

| 平台 | 安装包 |
| --- | --- |
| Windows x64 | `.exe`（NSIS）或 `.msi` |
| macOS Apple Silicon / Intel | `.dmg` |
| Linux x64 | `.AppImage`、`.deb` 或 `.rpm` |

macOS 构建目前尚未签名和公证。首次启动时，需要在 **系统设置 → 隐私与安全性** 中允许该应用运行。

也可以从源码构建：

```sh
git clone https://github.com/Moresyl/dsh-studio.git
cd dsh-studio
pnpm install
pnpm tauri build
```

## 2. 启动 DeepSeek Harness

启动 DSH Studio。它会检测已安装的 Node.js 运行时，并检查 `@deepseek-ai/dsh` 是否存在。

如果尚未安装 Harness，请选择 **Install DeepSeek Harness**。DSH Studio 会把它安装到应用数据目录中的专属前缀，而不会修改全局 npm 根目录。安装完成后启动服务，等待 Harness Web UI 显示在同一个窗口中。

桌面外壳会选择一个空闲的回环端口，通过 HTTP 健康检查监控服务，并在服务无响应时使用退避策略重启。它不会分叉或修改上游 Harness UI。

## 3. 配置 DeepSeek 提供商

在嵌入的 Harness Web UI 中：

1. 打开 **Settings → Models**。
2. 找到 **DeepSeek** 卡片。
3. 粘贴从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取的 API Key。
4. 保存提供商。

API Key 在 UI 中只写不可读，由 Harness 保存到凭据存储。模型路由会立即可用，无需重启服务。

Harness 官方适配器默认提供以下模型：

| 模型 ID | 建议用途 |
| --- | --- |
| `deepseek-v4-pro` | 编程、长程推理和困难的 Agent 任务 |
| `deepseek-v4-flash` | 对延迟要求较高的日常任务 |

两个默认模型均使用 **1,000,000 token 上下文窗口**。适配器默认启用思考模式，并支持 `high` 和 `max` 推理强度。对于困难的编程和多步骤任务请使用 `max`；不要把关闭思考模式作为规避提供商错误的方案。

## 4. 选择工作区并运行第一个任务

1. 在模型选择器中选择一个 DeepSeek V4 模型，该选择会成为新会话的默认模型。
2. 选择 **Choose workspace**，添加一个本地项目目录并选中它。
3. 新建会话。
4. 发送类似下面的任务：

> 总结这个代码库，指出主要包，并建议一个能够验证的小型改进。

Harness 可以读取和编辑工作区文件、运行命令、委派工作并维护计划。对于当前权限策略要求审批的操作，Web UI 会先请求确认。

## 故障排查

- **Harness 未安装** — 使用 DSH Studio 中的安装操作，并查看实时输出的 npm 日志。
- **未检测到 Node.js** — 安装 Node.js 20 或更高版本，然后重启 DSH Studio。
- **`MISSING_CREDENTIAL`** — 在 **Settings → Models** 中重新保存 DeepSeek API Key。
- **`UNKNOWN_MODEL`** — 从已配置的提供商中选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- **输入框不可用** — 在发送第一个任务前先选择工作区和模型。
- **本地服务停止响应** — DSH Studio 每 10 秒探测一次，连续三次健康检查失败后会回收并重启服务。
- **重启后端口发生变化** — 这是正常行为。DSH Studio 会请求操作系统分配空闲端口，并自动跟随新的本地地址。

## 安全说明

DSH Studio 只把服务绑定到回环地址，不提供局域网监听选项。从托盘中退出会停止受监控的整个进程树；仅关闭窗口则会让本地服务继续在托盘中运行。
