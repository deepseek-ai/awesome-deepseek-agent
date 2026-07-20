[English](./orca.md) | [简体中文](./orca.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 Orca

Orca 是一款开源的 DeepSeek 原生终端编程 Agent，使用 Rust 编写、单二进制分发。它直接对接 `api.deepseek.com`：SSE 流式输出、面向前缀缓存优化的提示词组装、完整 1M token 上下文窗口与自动压缩，以及操作系统级沙箱（macOS 用 Seatbelt，Linux 用 bubblewrap / Landlock + seccomp）。

- **GitHub:** <https://github.com/echoVic/blade-deepseek>
- **官网:** <https://orcaagent.dev/>

#### 1. 安装 Orca

任选其一：

```sh
# npm（macOS / Linux 预编译二进制，支持 ARM64 和 x64）
npm install -g @blade-ai/orca

# 或使用原生安装脚本
curl -fsSL https://orcaagent.dev/install.sh | sh
```

验证安装：

```sh
orca --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后导出环境变量：

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. 进入项目目录并启动

```sh
cd /path/to/my-project
orca                              # 交互式 TUI
orca exec "fix the failing test"  # 无头模式，适用于脚本和 CI
```

Orca 默认将主循环路由到 **DeepSeek-V4-Pro**（推理强度 **`max`**），摘要、压缩等辅助任务路由到 **DeepSeek-V4-Flash**。在 TUI 中使用 `/model` 菜单可分步切换模型和推理强度（`high` / `max`），也可以写入配置：

```toml
# ~/.orca/config.toml
model = "deepseek-v4-pro"
reasoning_effort = "max"
```

Orca 使用完整的 **1M token 上下文窗口**，在使用量达到 80% 时自动压缩，并保留系统提示词和最近消息。

#### 常用命令

| 命令 | 作用 |
|---|---|
| `/mode` | 切换审批模式：`suggest` / `auto-edit` / `full-auto` |
| `/plan` | 只读规划模式 |
| `/goal` | 设定持久化目标；Orca 以停滞检测（而非固定轮数上限）持续推进 |
| `/trust` | 管理文件夹信任（陌生目录默认只读、断网） |
| `/workflows` | 运行后台 JavaScript 工作流 |
| `/cost` | 查看会话 token 用量与预估费用 |
| `@` | 搜索文件、技能、插件和 MCP 资源 |

#### 配置

主配置文件为 `~/.orca/config.toml`。常用环境变量：

| 变量 | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | API Key |
| `ORCA_MODEL` | 覆盖默认模型 |
| `ORCA_BASE_URL` | API 地址，默认 `https://api.deepseek.com` |
| `ORCA_REASONING_EFFORT` | 推理强度（`high` / `max`） |

#### MCP、技能与验证

- **MCP 服务器** —— 支持 stdio 和 SSE 传输；MCP 工具和资源统一进入 `@` 提及搜索。MCP elicitation 请求会路由到 TUI 交互式弹窗。
- **技能** —— 在 `~/.orca/skills/<name>/` （用户级）或受信任项目内放置 `SKILL.md` 即可。
- **验证门** —— `orca exec --verifier "cargo test" "fix it"`，以真实命令通过与否作为任务完成的验收条件。
- **沙箱** —— Shell 命令在操作系统级隔离中执行；严格策略下若无可用沙箱后端则拒绝执行，绝不降级裸跑。
