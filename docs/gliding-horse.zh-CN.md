[English](./gliding-horse.md) | [简体中文](./gliding-horse.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Gliding Horse

Gliding Horse 是一款使用 Rust 编写的开源工业级 AI Agent 操作系统。它通过 PDCA 循环（Plan 计划 → Do 执行 → Check 检查 → Act 改进）编排多个 Agent，并以知识图谱、技能图谱和四层记忆系统（L0 Sled → L1 Session → L2 Blackboard → L3 Projection）作为支撑。项目内置 **Gliding Code** —— 一款终端 AI 编程助手（TUI），支持 DeepSeek-V4-Pro 与 DeepSeek-V4-Flash 全 100 万 token 上下文。其中 DeepSeek-V4-Flash 使用官方原生 **Responses API**（`/v1/responses`），其他模型自动回退到 Chat Completions。

- **GitHub：** <https://github.com/doiito/gliding_horse>

#### 1. 安装 Gliding Code

任选其一：

```sh
# 从 GitHub Releases 下载预编译二进制（Linux musl / macOS / Windows）：
#   https://github.com/doiito/gliding_horse/releases
tar xzf glidingcode-*.tar.gz     # Linux / macOS
./glidingcode --help

# 从源码构建（需要 Rust 工具链）：
git clone https://github.com/doiito/gliding_horse.git
cd gliding_horse
cargo build -p code_cli --release
./target/release/glidingcode --help
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key 并导出：

```sh
export DEEPSEEK_API_KEY="sk-..."
```

API 地址默认使用 `https://api.deepseek.com`（可通过 `DEEPSEEK_API_URL` 覆盖）。

#### 3. 运行一次性任务

```sh
./glidingcode "解释 Rust 的借用检查器是如何工作的"
```

或者启动交互式 TUI：

```sh
./glidingcode
```

默认使用 **DeepSeek-V4-Flash**，走 DeepSeek 官方原生 **Responses API**（`/v1/responses`）——没有 `data: [DONE]` 终止符，使用语义化的 `response.*` SSE 事件。在 TUI 中可用 `/model deepseek-v4-flash|deepseek-v4-pro` 切换模型，也可以在命令行指定默认模型：

```sh
./glidingcode --model deepseek-v4-pro "为待办事项应用设计一个 REST API"
```

DeepSeek-V4 系列模型支持 **100 万 token 上下文**；Gliding Code 对 `deepseek-v4*` 模型启用完整的 100 万上下文（`1_048_576`）。思考模式默认开启（DeepSeek V4 默认 effort 为 `high`，支持 `reasoning_effort: low|high|max`），原生推理模型的推理内容会以思考步骤的形式呈现在 TUI 中。

#### 4. 配置项

| 环境变量 | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | API Key（也接受 `AGENT_OS_GATEWAY_API_KEY`） |
| `DEEPSEEK_API_URL` | API 基础地址，默认 `https://api.deepseek.com` |
| `USE_RESPONSES_API` | `1`/`true` 强制使用 Responses API（`/v1/responses`），`0` 强制使用 Chat Completions。默认对 DeepSeek-V4-Flash 启用。 |
| `GLIDING_HORSE_DATA` | 记忆/知识图谱存储目录（默认 `~/.gliding_horse/data`） |

#### 5. 定价

按每 100 万 token 计价，已于 [DeepSeek API 定价页](https://api-docs.deepseek.com/quick_start/pricing) 核对（2026-08-04）：

| 模型 | 输入（缓存未命中） | 输入（缓存命中） | 输出 |
|---|---|---|---|
| `deepseek-v4-flash` | $0.14 | $0.0028 | $0.28 |
| `deepseek-v4-pro` | $0.435 | $0.003625 | $0.87 |

#### 6. 核心特性

- **PDCA 编排** —— 多 Agent 的 Plan/Do/Check/Act 循环，配合 7 级自适应执行（L0 即时 → L6 紧急），模型会规划、执行、验证并改进，直到任务完成。
- **MCP 支持** —— 通过 `--mcp-server name=url`（HTTP SSE）或 `--mcp-server-stdio name='{"command":"npx","args":[...]}'`（stdio）接入任意 MCP 服务器。
- **知识图谱与技能图谱** —— 任务基于知识图谱展开，完成的工作会沉淀进自我演进的技能图谱。
- **检查点与恢复** —— 使用 `--list-checkpoints` 与 `--resume <task_iri>` 恢复被中断的任务。
- **原生 Responses API 支持** —— DeepSeek-V4-Flash 请求走官方 Responses API，支持流式 `response.*` 事件与工具调用往返。
