[English](./tealkit.md) | [简体中文](./tealkit.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 TealKit CLI

TealKit CLI (`tealkit`) 是一个开源的原生终端 AI 编程智能体、工作流执行引擎与 AgentSkills 运行环境。它提供类似 Claude Code / Roo Code 的自主编码模式（Architect 架构、Code 编码与 Ask 问答模式）、10 项原生文件系统与终端执行工具、Model Context Protocol (MCP) 扩展支持以及本地 RAG 知识检索。

- **GitHub:** <https://github.com/lschaffer/tealkit>
- **官网:** <https://tealkit.dev>

---

#### 1. 安装 TealKit CLI

你可以下载预打包的独立运行包，或使用 Dart SDK 从源码编译构建。

- **Windows x64 独立运行包：**
  从 [tealkit.dev](https://tealkit.dev) 下载并解压 [`tealkit_cli_setup.zip`](https://tealkit.dev/download/tealkit_cli_setup.zip)（约 55MB，内含 `tealkit.exe`、原生运行时动态库及默认模板配置）。

- **源码构建（Dart SDK >= 3.8 / Flutter）：**
  ```bash
  git clone https://github.com/lschaffer/tealkit.git
  cd tealkit/cli
  dart pub get
  dart build cli -o build/cli
  ```

- **验证安装：**
  ```bash
  tealkit --version
  ```

---

#### 2. 配置 DeepSeek

TealKit CLI 在 `llm.yaml`（位于工作目录或全局配置目录 `~/.tealkit/llm.yaml`）中管理模型提供商。

1. 设置 DeepSeek API 密钥：
   - **Linux / macOS:**
     ```bash
     export DEEPSEEK_API_KEY="sk-..."
     ```
   - **Windows (PowerShell):**
     ```powershell
     $env:DEEPSEEK_API_KEY="sk-..."
     ```
   *(或在项目根目录的 `.env` 文件中添加 `DEEPSEEK_API_KEY=sk-...`)*

2. 在 `llm.yaml` 中配置 DeepSeek V4 模型：

```yaml
# TealKit LLM 配置
temperature: 0.2
max_tokens: 8192
max_tool_iterations: 150

llms:
  - name: "deepseek"
    provider: "openai_compatible"
    model: "deepseek-v4-pro"
    api_key: "${DEEPSEEK_API_KEY}"
    base_url: "https://api.deepseek.com/v1"
    context_window: 1000000
    reasoning_effort: "max"

  - name: "deepseek-flash"
    provider: "openai_compatible"
    model: "deepseek-v4-flash"
    api_key: "${DEEPSEEK_API_KEY}"
    base_url: "https://api.deepseek.com/v1"
    context_window: 1000000
```

> **关于 DeepSeek V4 模型特性：**
> - **100 万 Token (1M) 上下文：** DeepSeek V4 系列模型支持高达 **1,000,000 tokens** 上下文窗口（`context_window: 1000000`）。
> - **推理深度控制：** `deepseek-v4-pro` 支持深度思考模式，可配置 `reasoning_effort: "max"` 以获得最优质的复杂编码与架构分析能力。

---

#### 3. 首次运行

在任意项目代码目录下启动 TealKit 自主编程智能体：

```bash
# 启动交互式编程智能体 REPL（使用 llm.yaml 中配置的模型）
tealkit code

# 或者直接传入单次任务提示词
tealkit code "分析当前代码仓库并生成架构摘要"
```

#### 交互命令与快捷操作

在 REPL 交互界面中：
- `/llm deepseek` — 随时无缝切换到 `deepseek-v4-pro`。
- `/cost` 或 `/estimated_costs` — 实时查看 Token 统计与预估成本。
- `/save <name>` / `/resume <name>` — 保存与恢复多轮会话记录。
- `Ctrl+V` — 直接粘贴剪贴板内容到终端提示符。
- `Ctrl+Enter` / `Enter`（可配置） — 发送指令给智能体。

#### 使用 Agent Skills（技能模式 `SKILL.md`）

TealKit 自动从以下路径发现并执行 AgentSkills：
- `~/.tealkit/skills/<name>/SKILL.md`
- `./skills/<name>/SKILL.md`

所有技能无需在 Frontmatter 中手动声明内置工具，系统会自动注入原生文件读写、终端命令执行与网页检索工具。
