[English](./achbit.md) | [简体中文](./achbit.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 Achbit 中使用 DeepSeek

[Achbit](https://github.com/Achbite/Achbit) 是采用 MIT 许可证的本地优先编程 Agent，提供桌面 GUI、TUI 和 CLI。本指南通过 **Responses API** 接入 **DeepSeek Flash**。

Achbit 在同一个会话中连接项目编辑、命令执行、浏览器交互和可视结果检查。GUI、TUI、CLI 共享模型连接与 Session 状态。Computer Use 提供内置浏览器、可选的 Chrome DevTools MCP 接入，以及经授权的 macOS 和 Windows 原生桌面操作。

## 1. 安装并打开 Achbit

从 [Releases](https://github.com/Achbite/Achbit/releases) 下载对应平台的制品。

| 平台 | 安装包或解压包 | GUI 入口 |
| --- | --- | --- |
| macOS Apple Silicon | `Achbit-<version>-macos-arm64.pkg` 或 `Achbit-<version>-macos-arm64.tar.gz` | `/Applications/Achbit.app`，或解压目录中的 `Achbit.app` |
| Windows x64 | `Achbit-<version>-win64-setup.exe` 或 `Achbit-<version>-win64.zip` | 开始菜单，或解压目录中的 `Achbit.exe` |
| Linux ARM64 | `Achbit-<version>-linux-arm64.tar.gz` | 解压目录中的 `./Achbit` |

制品包含运行时。Windows 解压版 GUI 需要 WebView2；Linux GUI 需要 GTK、WebKitGTK 和 ALSA。macOS 制品使用项目本地开发签名，未经过 Apple 公证。详见[安装与用户目录](https://github.com/Achbite/Achbit/blob/0.6.60/docs/distribution.md)。

从源码构建需安装 Docker 与 GNU Make；Windows 使用启用 Docker 集成的 WSL2。macOS 打包还需要宿主机上的 Xcode Command Line Tools、仓库指定的 Rust 工具链和 Node.js。

在宿主机执行：

```sh
git clone https://github.com/Achbite/Achbit.git Achbit
cd Achbit
# 仅 macOS：首次打包前执行一次
bash scripts/setup-macos-signing.sh
make shell
```

Windows、Linux 跳过签名命令。进入开发容器后执行 `bash ./build.sh` 更新当前宿主平台的可运行程序；分发打包选择 `bash ./build.sh --stage package-macos`、`--stage package-windows` 或 `--stage package-linux`。构建完成后退出容器，在目标宿主机启动产物。详见[构建指南](https://github.com/Achbite/Achbit/blob/0.6.60/README.zh-CN.md#从源码构建)。

## 2. 保存 DeepSeek 连接与模型

从 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取 API Key。

1. 打开 **设置 → 模型与服务 → API 连接**。
2. 打开 **DeepSeek** 连接，或新增服务类型为 DeepSeek 的 API 连接。
3. API 地址填写 `https://api.deepseek.com`，输入密钥并保存。
4. 打开或新增该连接下的模型，保存以下配置：

| 配置 | 值 |
| --- | --- |
| 显示名称 | `DeepSeek Flash` |
| 模型 | `deepseek-flash` |
| API 协议 | Responses API |
| 上下文窗口 | `1000000` |
| 最大输出 | `384000` |
| 思考 | 启用 |
| 推理强度 | `max` |
| 图片输入 | 启用 |
| 联网搜索 | 关闭 |

API 模型名使用 `deepseek-flash`。当前能力和价格见 [DeepSeek 模型文档](https://api-docs.deepseek.com/quick_start/pricing/)。

DeepSeek 支持 1M 上下文和最多 384K 输出 token。最大输出是预算上限，不是要求生成这么长的回答。已有会话的推理强度可能覆盖模型配置，此时也需在会话中选择 `max`。截图任务需要开启图片输入。模型编辑器的“联网搜索”开关控制供应商托管的 Responses 工具，Flash 会忽略它；Achbit 自身搜索工具的可用性单独管理。参见 [Responses API](https://api-docs.deepseek.com/guides/responses_api/) 和[思考模式](https://api-docs.deepseek.com/guides/thinking_mode/)。

## 3. 运行首个任务并继续会话

选择项目和已保存的 DeepSeek 模型，发送：

> 阅读本项目 README，说明项目用途、入口和运行方法。引用你实际读过的文件。不要修改文件。

然后在同一会话中发送：

> 阅读你刚才确定的入口相关的一份源码，说明它与 README 的关系，并引用一小段代码。不要修改文件。

确认必要的访问请求，检查实际工具结果。接下来体验[发布清单 Computer Use 项目](https://github.com/Achbite/Achbit/tree/0.6.60/examples/launch-checklist)：将该目录打开为项目，使用提供的提示词。Agent 会打开本地 HTML、勾选两项任务、确认 **2 / 4 和 50%**，筛选已完成项目，再重载检查状态保持。无需启动服务器或安装依赖。

![Achbit 中的 DeepSeek Computer Use 任务](assets/achbit-computer-use.jpg)

项目附带[运行摘要](https://github.com/Achbite/Achbit/blob/0.6.60/examples/launch-checklist/run-summary.json)和浏览器截图。要体验查阅公开网页并生成作品，可继续尝试[浏览器调研示例](https://github.com/Achbite/Achbit/tree/0.6.60/examples/deepseek-browser-checklist)。

## 4. 在 CLI、TUI 使用同一连接

通过 macOS PKG 或 Windows Setup 安装后，可直接使用 `achbit-cli`、`achbit-tui`；Windows 安装后重新打开终端。解压包提供以下入口：

| 平台 | CLI | TUI |
| --- | --- | --- |
| macOS | `./Achbit-CLI.command` | `./Achbit-TUI.command` |
| Windows | `.\achbit-cli.bat` | `.\achbit-tui.bat` |
| Linux | `./achbit-cli` | `./achbit-tui` |

```sh
achbit-cli connections
achbit-cli --model <profile-id> chat -C /path/to/project
achbit-tui -C /path/to/project
```

解压版按需替换为表中的入口。`<profile-id>` 从 `connections` 输出中复制，它是已保存配置的 ID，不是 API 模型名。TUI 中使用 `/model` 选择模型，`/sessions`、`/resume` 继续已有会话，`/language en-US` 或 `/language zh-CN` 切换界面语言。

## Computer Use 与 Loop 设计带来的能力

Achbit 通过本地执行的工具提供 Computer Use。观察、图片和执行结果与项目工具结果进入同一个 Session Loop，再返回 DeepSeek。

| 设计 | 实际价值 |
| --- | --- |
| **代码与界面操作在同一任务中衔接。** 程序化操作使用文件工具、命令或 MCP，交互与检查使用内置浏览器或原生桌面工具。 | 修改代码后检查实际界面行为，实现、工具结果和视觉证据保留在同一会话。 |
| **GUI、TUI、CLI 共用一个 Session 引擎。** Session 负责模型轮次、上下文、等待、取消和持久化日志，各界面消费同一投影。 | 切换入口后，可以沿用已有历史和执行状态继续任务。 |
| **按当前运行加载工具。** 按需发现、激活插件，将选中的工具 schema 与指导加入本轮。 | 为任务扩展精简核心工具集，无需另建 Agent Loop，也无需每次请求加载全部插件。 |
| **按执行事实调度。** Kernel 提供文件调用依赖，Loop 对符合条件的调用有限并行，并等待后续步骤所依赖的长命令。 | 在操作允许时并行，同时明确区分已启动、等待、完成、失败、取消与未知结果。 |
| **原生输入绑定已观察的目标。** 观察绑定应用、窗口和当前 run；后台观察与前台鼠标键盘输入有不同要求。 | 拒绝过期目标观察；动作派发后即使截图失败，也保留派发结果，不能据此重复输入。 |

实现参考：[Session loop](https://github.com/Achbite/Achbit/blob/0.6.60/userspace/session-core/src/local-agent/loop.ts)、[工具目录](https://github.com/Achbite/Achbit/blob/0.6.60/crates/achbit-kernel-daemon/src/local_agent_tool_catalog.rs)和 [Computer Use 文档](https://github.com/Achbite/Achbit/blob/0.6.60/plugins/computer-use/README.md)。清单示例的运行记录覆盖 macOS 内置浏览器，没有覆盖外部原生应用或 Windows。

内置浏览器依赖发起它的 GUI 窗口。原生桌面工具由共享 Host 提供，可在平台支持并获授权时供 CLI/TUI/GUI 使用。macOS 原生桌面控制要求 macOS 15.2+、辅助功能和屏幕录制权限；Windows 普通权限会话不能控制提权应用。Linux 支持内置浏览器的不依赖截图的页面操作，不支持原生桌面控制或浏览器截图工具。[Chrome 接入](https://github.com/Achbite/Achbit/blob/0.6.60/plugins/chrome-devtools/README.md)使用浏览器自身的确认流程。激活插件不等于取得执行或系统权限。

## 参考资料

- [Achbit DeepSeek 配置指南](https://github.com/Achbite/Achbit/blob/0.6.60/docs/product/deepseek.zh-CN.md)
- [Computer Use 示例项目](https://github.com/Achbite/Achbit/tree/0.6.60/examples/launch-checklist)
- [DeepSeek Responses API](https://api-docs.deepseek.com/guides/responses_api/)
- [DeepSeek 思考模式](https://api-docs.deepseek.com/guides/thinking_mode/)
- [当前模型与价格](https://api-docs.deepseek.com/quick_start/pricing/)
