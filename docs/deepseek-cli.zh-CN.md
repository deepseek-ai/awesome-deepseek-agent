[English](./deepseek-cli.md) | [简体中文](./deepseek-cli.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeek-CLI

DeepSeek-CLI 是一款由 DeepSeek 驱动的开源 **Agent 化** 终端 AI 编程助手。使用 TypeScript 编写，通过 [Bun](https://bun.sh) 打包为约 60 MB 的单个二进制文件。它将流式对话与工具调用相结合——模型可以读取文件、执行 shell 命令、编辑代码、搜索仓库、抓取网页，真正完成任务，而不只是「纸上谈兵」。

- **GitHub：** <https://github.com/charsdavy/deepseek-cli>

#### 1. 安装 DeepSeek-CLI

任选其一：

```sh
# Homebrew（推荐）
brew tap charsdavy/tap
brew install deepseek

# 从源码构建（需要 Bun ≥ 1.1）
git clone https://github.com/charsdavy/deepseek-cli.git
cd deepseek-cli
bun install
bun run build          # → ./dist/deepseek
```

如果从源码构建，请将 `./dist/deepseek` 复制到 `PATH` 中的某个目录。使用 `deepseek -V` 验证安装。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。运行一次 `deepseek auth` 将其保存到 `~/.deepseek-cli/config.json`（文件权限 `0600`），也可以直接设置环境变量 `DEEPSEEK_API_KEY`。

#### 3. 启动

```sh
cd /path/to/my-project
deepseek                                 # 交互式 REPL
deepseek "summarize the architecture"    # 一次性 prompt
deepseek -m deepseek-v4-pro "prove 7 is prime"
deepseek -m deepseek-v4-flash "explain this test file"
deepseek --yolo "fix the failing tests"  # 自动批准工具调用
```

默认情况下 DeepSeek-CLI 使用 `auto` 模型，会根据任务复杂度自动选择 **DeepSeek-V4-Pro** 或 **DeepSeek-V4-Flash**。传入 `-m deepseek-v4-pro` / `-m deepseek-v4-flash` 可固定模型。在 REPL 内，`/model` 会打开方向键配置向导，可设置模型、推理强度（`off/high/max`）与上下文裁剪预算——预算预设最高支持完整的 **100 万 token** 上下文窗口。DeepSeek-V4-Pro 默认即思考模型；使用 `--reasoning-effort max`（或 `/reasoning effort max`）可开启最深推理级别。

#### 内置工具

Agent 通过工具循环驱动工作——每一轮它都可以调用 14 个内置工具中的任意组合（相互独立、可并行执行）：

| 工具 | 作用 |
|---|---|
| `read_file` / `read_files` | 读取单个文件，或一次批量读取多个文件 |
| `write_file` / `edit_file` | 创建/覆盖文件，或进行精确字符串替换 |
| `bash` | 执行 shell 命令，支持工作目录、超时与输出截断 |
| `glob` / `grep` | 匹配文件路径，或搜索文件内容（ripgrep，含 Node 回退） |
| `list_dir` | 单层目录列表 |
| `web_fetch` / `web_search` | 抓取 URL（HTML 转 Markdown），或通过 DuckDuckGo 搜索——无需 API Key |
| `git_diff` / `git_status` | 只读的结构化 `git diff` / `git status` |
| `task` | 为子任务派生嵌套子 Agent；独立的子任务并行执行 |
| `todo_write` | 维护模型可读写的内存任务清单 |

#### 常用 REPL 命令

| 命令 | 作用 |
|---|---|
| `/model [name]` | 配置向导（模型 → 推理强度 → 上下文），或快速切换模型 |
| `/reasoning [on|off|effort high|max]` | 查看/设置思考默认值与推理强度 |
| `/context [tokens]` | 查看/设置上下文裁剪预算 |
| `/mcp [name]` | 列出 MCP 服务器，或切换某服务器的工具 |
| `/skill [name]` | 为本会话挑选/启用 Skills |
| `/allow [tool|all|reset]` | 在本会话内授权某个工具 |
| `/approve [auto|ask]` | 切换 bash 审批模式 |
| `/tokens` | 查看 token 用量（估算值 + API 真实值） |
| `/new` · `/save` · `/undo` · `/retry` | 新建会话、保存、撤销上一轮、重跑上一个 prompt |
| `/export [path]` | 导出对话记录到 stdout 或文件 |
| `/sessions [query]` | 列出或搜索已保存的会话 |

#### 配置

配置文件位于 `~/.deepseek-cli/config.json`。环境变量优先于配置文件：

| 变量 | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | API Key（优先于配置文件） |
| `DEEPSEEK_BASE_URL` | 覆盖 API 基址 |
| `DEEPSEEK_MODEL` | 默认模型 ID |

常用 CLI 参数：

| 参数 | 说明 |
|---|---|
| `-m, --model <name>` | 模型 ID（默认 `auto`） |
| `--yolo` / `--approval-mode <ask|auto|yolo>` | 跳过 / 配置权限确认 |
| `--reasoning-effort <high|max>` | 推理强度（默认 `high`；`max` 更深） |
| `--max-context <tokens>` | 上下文裁剪预算（默认 60000） |
| `--max-iterations <n>` | 限制 Agent 循环次数（默认 30） |
| `--base-url <url>` | 覆盖 API 基址（用于代理 / 自建端点） |
| `-c` / `--resume <id>` | 恢复最近一次或指定会话 |
| `--output-format <text|json>` | 一次性模式：输出单个 JSON 结果，便于 CI 使用 |

#### MCP、Skills 与项目指令

- **MCP 服务器** —— 通过 `deepseek mcp add ...` 添加（保存在 `~/.deepseek-cli/mcp.json` 或 `<repo>/.mcp.json`）；其工具以 `mcp_<server>_<tool>` 形式暴露。将服务器标记为 `--dangerous` 可要求每次调用都需批准。
- **Skills** —— 可从 deepseek、Claude Code 与 Codex 的技能目录加载指令包（支持扁平 `<name>.md` 或 `<name>/SKILL.md` 目录两种布局）。用 `deepseek skill create <name>` 生成模板，用 `/skill` 激活。
- **项目指令** —— Agent 会自动将仓库根目录下的 `AGENTS.md`、`deepseek.md`、`.cursorrules`、`CLAUDE.md` 或 `.deepseek` 载入系统提示词。`deepseek init` 会生成 `AGENTS.md` 模板。
- **会话持久化** —— 每一轮交互都会自动保存到 `~/.deepseek-cli/sessions/`；可通过 `@path/to/file` 在 prompt 中内联引用文件。

DeepSeek-CLI 基于 MIT 协议开源，零运行时依赖（API 客户端为原生 `fetch` + SSE），并支持带推理轨迹的流式输出。完整的命令参考见 [README](https://github.com/charsdavy/deepseek-cli)。
