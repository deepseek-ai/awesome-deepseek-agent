[English](./zagens.md) | [简体中文](./zagens.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Zagens

Zagens 是一款以 DeepSeek 为原生后端的**桌面 Agent 控制台**：Tauri 2 界面 + 本机 **runtime sidecar**，原生对接 `api.deepseek.com`，支持 **DeepSeek-V4-Pro** 与 **DeepSeek-V4-Flash** 全 **100 万 token** 上下文，并提供工具调用、MCP、技能与会话回放。亦可通过 headless **`zagens`** CLI 做脚本化与自动化；**全屏 TUI 终端（`zagens-tui`）正在开发中，近期推出。**

- **GitHub：** https://github.com/didclawapp-ai/zagens

**特色概览：**

- **长程任务 Harness** — 针对多步编码任务的分层完成门禁，减少半途停手或过早「声称完成」。
- **抗幻觉与可验证输出** — 系统提示要求结论有据可查，没核实就标明「未验证」；任务是否完成，会**自动跑测试、编译验证**并核对**该交付的文件是否真存在**，而不是只听模型说「做完了」。
- **桌面原生控制面** — 按轮**会话回放**、diff 预览、工具执行审批、嵌入式终端与系统托盘通知。
- **Code + Office 一体** — 编码与表格/文档（`write_office`）共用同一 sidecar runtime，无需另开一套工具链。

#### 1. 安装 Zagens

任选其一：

```sh
# Windows 桌面（推荐）：从 GitHub Releases 下载安装包
#   https://github.com/didclawapp-ai/zagens/releases

# CLI（Windows / macOS / Linux，需要 Rust stable）
cargo install zagens-cli --locked --bin zagens
```

验证 CLI 安装：

```sh
zagens --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。桌面版首次启动可在 **设置** 中填写并保存到 `~/.zagens/config.toml`；CLI 可执行 `zagens login`，或设置环境变量 `DEEPSEEK_API_KEY`。

#### 3. 进入项目目录并开始使用

**桌面：** 启动 Zagens，选择工作区文件夹，发送第一条 prompt 即可。

**CLI：**

```sh
cd /path/to/my-project
zagens exec "用三条要点总结本仓库 README.md"
```

Zagens 默认使用 **DeepSeek-V4-Pro**，`reasoning_effort = max` 以发挥 V4 深度推理。可在设置中切换 **Flash** 以降低成本，或调整推理强度（`max` / `high`）。诊断连通性：`zagens doctor`；本地 HTTP API：`zagens serve --http`。

<div align="center">
<img src="https://raw.githubusercontent.com/didclawapp-ai/zagens/master/assets/screenshot.png" width="800" />
</div>
