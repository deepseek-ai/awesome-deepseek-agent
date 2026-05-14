[English](./whale.md) | [简体中文](./whale.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Whale

Whale 是一款以 DeepSeek 为原生后端的终端编程 Agent。设计围绕 DeepSeek API 展开 —— prefix-cache 友好的会话、thinking 控制、工具调用修复、MCP 与 Agent Skills。

- **GitHub：** <https://github.com/usewhale/whale>
- **平台支持：** Whale 当前支持 macOS 和 Linux，Windows 支持仍在开发中。

#### 1. 安装 Whale

使用脚本安装：

```sh
curl -fsSL https://raw.githubusercontent.com/usewhale/whale/main/scripts/install.sh | sh
```

也可以使用 Homebrew 安装：

```sh
brew install usewhale/tap/whale
```

验证安装：

```sh
whale --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

运行初始化向导：

```sh
whale setup
```

你也可以直接设置环境变量 `DEEPSEEK_API_KEY`。环境变量会优先于 `whale setup` 保存的 key。

#### 3. 配置 DeepSeek V4

Whale 默认使用 **DeepSeek-V4-Flash**，推理强度为 `high`，并启用 thinking。DeepSeek V4 Pro 和 Flash 支持最高 100 万 token 上下文，Whale 直接使用当前 DeepSeek V4 模型名。

如果希望在复杂编程任务中使用最高推理强度，可以创建或编辑 `~/.whale/config.toml`：

```toml
model = "deepseek-v4-pro"
reasoning_effort = "max"
thinking_enabled = true
```

如果希望更快、更低成本地迭代，可以使用 `deepseek-v4-flash`：

```toml
model = "deepseek-v4-flash"
reasoning_effort = "high"
thinking_enabled = true
```

Whale 会向 API 发送 DeepSeek 的 `thinking` 和 `reasoning_effort` 字段。

#### 4. 进入项目目录并启动

```sh
cd /path/to/my-project
whale doctor
whale
```

在 TUI 中常用命令：

| 命令 | 作用 |
|---|---|
| `/model` | 切换模型、推理强度和 thinking |
| `/ask [prompt]` | 只读提问模式 |
| `/plan [prompt]` | 先规划，再决定是否执行 |
| `/permissions` | 调整工具审批模式 |
| `/skills` | 列出、插入、启用或禁用本地 skills |
| `/mcp` | 查看 MCP server 状态 |
| `/status` | 查看 session、模式、模型和配置状态 |

也可以运行一次性 prompt：

```sh
whale exec "解释这个仓库是做什么的"
printf '总结当前目录\n' | whale exec
```

#### MCP 与 Skills

Whale 默认从 `~/.whale/mcp.json` 读取 MCP server 配置。它支持 stdio MCP server 和 Streamable HTTP MCP server，并将 MCP 工具接入与内置工具相同的审批流程。

Whale 会从 `.whale/skills`、`.agents/skills`、`~/.whale/skills` 和 `~/.agents/skills` 发现 Agent Skills。在 TUI 中输入 `$` 可以搜索并插入 skill，也可以运行 `/skills` 进行管理。
