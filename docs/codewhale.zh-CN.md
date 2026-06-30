[English](./codewhale.md) | [简体中文](./codewhale.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 CodeWhale（原 DeepSeek-TUI）

CodeWhale 是一个 DeepSeek-first 的开源 Rust 终端编程 Agent。它保留 DeepSeek 作为默认与一等 provider，原生支持 DeepSeek-V4-Pro / DeepSeek-V4-Flash、完整 100 万 token 上下文、推理流、缓存指标与 thinking effort 控制。同时，CodeWhale 也兼容 OpenRouter、本地 vLLM / SGLang / Ollama 部署、OpenAI-compatible 网关以及其他开放模型路由。

- **GitHub：** <https://github.com/Hmbown/CodeWhale>
- **官网：** <https://codewhale.net/zh/>

#### 1. 安装 CodeWhale

任选其一：

```sh
# npm（跨平台预编译二进制）
npm install -g codewhale

# Cargo（从源码构建，需要 Rust 1.88+）
cargo install codewhale-cli --locked   # `codewhale`（入口点）
cargo install codewhale-tui --locked   # `codewhale-tui`（TUI 二进制文件）

# 或从 GitHub Releases 下载预编译二进制：
#   https://github.com/Hmbown/CodeWhale/releases
```

验证安装：

```sh
codewhale --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后保存到 DeepSeek provider：

```sh
codewhale auth set --provider deepseek
codewhale auth status
codewhale doctor
```

你也可以直接设置环境变量 `DEEPSEEK_API_KEY`。保存的配置位于 `~/.codewhale/config.toml`；旧版 `~/.deepseek/` 配置仍会作为兼容回退读取。

#### 3. 进入项目目录并启动

```sh
cd /path/to/my-project
codewhale
```

`codewhale` 是规范的入口命令。默认进入交互式 TUI，也可调用子命令，如 `codewhale doctor`、`codewhale mcp list`、`codewhale serve --http`、`codewhale exec`、`codewhale -p "一次性 prompt"`、`codewhale --yolo` 等。

默认情况下，CodeWhale 使用原生 DeepSeek provider 与 **DeepSeek-V4-Pro**。按 `Shift+Tab` 切换推理强度（`off → high → max`）。按 `Tab` 切换模式：

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

`~/.codewhale/config.toml` 是主配置文件。常用环境变量：

| 变量 | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API Key |
| `DEEPSEEK_BASE_URL` | DeepSeek API 基址，默认 `https://api.deepseek.com` |
| `DEEPSEEK_MODEL` | 覆盖 DeepSeek 模型，例如 `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| `CODEWHALE_PROVIDER` | 选择 provider 路由，例如 `deepseek`、`openrouter`、`vllm`、`sglang` 或 `ollama` |
| `CODEWHALE_MODEL` | 覆盖当前 provider 的模型 |
| `RUST_LOG` | 日志级别，例如 `RUST_LOG=debug` |

`DEEPSEEK_PROVIDER` 仍作为旧版别名兼容，但新配置建议优先使用 `CODEWHALE_PROVIDER`。

#### MCP、Skills 与 Hooks

- **MCP 服务器** —— 在 `~/.codewhale/mcp.json` 中配置，或使用 `codewhale mcp add ...`。CodeWhale 同时是 MCP 客户端与 MCP 服务器（`codewhale mcp serve`）。
- **Skills** —— 将 `SKILL.md` 放入 `~/.codewhale/skills/<name>/`（用户级）或 `./.codewhale/skills/<name>/`（项目级）。
- **Hooks** —— 在 `config.toml` 的 `[hooks]` 中配置生命周期钩子（stdout / jsonl / webhook）。
- **子 Agent / Fleet** —— CodeWhale 可以通过同一套 provider-aware runtime 运行子 Agent 与 Fleet workers。
- **本地与开放模型路由** —— OpenRouter、vLLM、SGLang、Ollama 和其他 provider route 共用同一套审批、沙箱、回滚与工具能力。

#### HTTP 运行时 API

`codewhale serve --http` 暴露 `/v1/*` 运行时 API，便于将 CodeWhale 嵌入 IDE 与 Web UI（sessions、threads、turns、tasks、automations、MCP、skills）。完整接口契约见 [`docs/RUNTIME_API.md`](https://github.com/Hmbown/CodeWhale/blob/main/docs/RUNTIME_API.md)。
