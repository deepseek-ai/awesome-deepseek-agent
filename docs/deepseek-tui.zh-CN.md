[English](./deepseek-tui.md) | [简体中文](./deepseek-tui.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeek-TUI

DeepSeek-TUI 是一款采用 Rust 编写的开源终端 AI 编程助手，使用 Codex 风格的 13-crate 工作区架构。原生对接 `api.deepseek.com`，支持 DeepSeek-V4-Pro 与 DeepSeek-V4-Flash 全 100 万 token 上下文，并在 macOS（Seatbelt）、Linux（Landlock）和 Windows 上提供沙箱化的工具执行能力。

- **GitHub：** <https://github.com/Hmbown/DeepSeek-TUI>

#### 1. 安装 DeepSeek-TUI

任选其一：

```sh
# npm（跨平台预编译二进制）
npm install -g deepseek-tui

# Cargo（从源码构建，需要 Rust 1.85+）
cargo install deepseek-tui-cli

# 或从 GitHub Releases 下载预编译二进制：
#   https://github.com/Hmbown/DeepSeek-TUI/releases
```

验证安装：

```sh
deepseek --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。首次运行时 `deepseek auth` 会引导你保存到 `~/.deepseek/config.toml`，也可直接设置环境变量 `DEEPSEEK_API_KEY`。

#### 3. 进入项目目录并启动

```sh
cd /path/to/my-project
deepseek
```

`deepseek` 是规范的入口命令。默认进入交互式 TUI，也可调用子命令，如 `deepseek doctor`、`deepseek mcp list`、`deepseek serve --http`、`deepseek -p "一次性 prompt"`、`deepseek --yolo` 等。

DeepSeek-TUI 默认使用 **DeepSeek-V4-Pro**。按 `Shift+Tab` 切换推理强度（`off → high → max`）。按 `Tab` 切换模式：

| 模式 | 说明 |
|---|---|
| **Plan** | 只读调研模式。不写文件、不执行 shell。 |
| **Agent** | 多步工具调用。具有副作用的工具需要审批。 |
| **YOLO** | 自动批准所有工具，并解除工作区边界限制。 |

#### 快捷键

| 按键 | 操作 |
|-----|------|
| `Enter` | 发送 prompt |
| `Shift+Enter` | 插入换行 |
| `Tab` | 切换模式（Plan / Agent / YOLO） |
| `Shift+Tab` | 切换推理强度（off / high / max） |
| `Esc` | 中断当前模型回合 |
| `/` | 打开 slash 命令菜单 |
| `?` | 显示快捷键帮助 |
| `Ctrl+C`（两次） | 退出 |

#### 配置

`~/.deepseek/config.toml` 是主配置文件（仓库中的 `config.example.toml` 列出了全部可用项）。常用环境变量：

| 变量 | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | API Key（覆盖配置文件中的值） |
| `DEEPSEEK_BASE_URL` | API 基址，默认 `https://api.deepseek.com`；中国区使用 `https://api.deepseeki.com` |
| `DEEPSEEK_MODEL` | 覆盖默认模型 |
| `DEEPSEEK_PROVIDER` | 切换提供商，例如 `nvidia-nim`（使用 `NVIDIA_API_KEY`） |
| `RUST_LOG` | 日志级别，例如 `RUST_LOG=debug` |

#### MCP、Skills 与 Hooks

- **MCP 服务器** —— 在 `~/.deepseek/mcp.json` 中配置，或使用 `deepseek mcp add ...`。DeepSeek-TUI 同时是 MCP 客户端与 MCP 服务器（`deepseek mcp serve`）。
- **Skills** —— 将 `SKILL.md` 放入 `~/.deepseek/skills/<name>/`（用户级）或 `./.deepseek/skills/<name>/`（项目级）。
- **Hooks** —— 在 `config.toml` 的 `[hooks]` 中配置生命周期钩子（stdout / jsonl / webhook）。
- **子 Agent** —— 模型可以通过 `agent_spawn` 派生子 Agent，并使用完整的生命周期工具族（`agent_wait`、`agent_result`、`agent_cancel` 等）。
- **RLM** —— 内置递归 LM 工具，在沙箱化的 Python REPL 中处理超大输入，不会污染父级上下文。

#### HTTP 运行时 API

`deepseek serve --http` 暴露 `/v1/*` 运行时 API，便于将 DeepSeek-TUI 嵌入 IDE 与 Web UI（sessions、threads、turns、tasks、automations、MCP、skills）。完整接口契约见 [`docs/RUNTIME_API.md`](https://github.com/Hmbown/DeepSeek-TUI/blob/main/docs/RUNTIME_API.md)。
