[English](./yoyo.md) | [简体中文](./yoyo.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 yoyo 中使用 DeepSeek

yoyo 是一个用 Rust 编写的开源终端编程智能体，而且是自进化的：它阅读自己的源码、规划改进、实现并在测试通过后提交——整个过程公开进行。作为产品，它是一个流式 REPL，拥有 90+ 斜杠命令、子代理编排（`/spawn --parallel`、后台任务）、watch 模式、MCP 服务器、技能系统和 15 个模型提供商——DeepSeek 是其中的一等公民。

- **GitHub:** <https://github.com/yologdev/yoyo-evolve>

#### 1. 安装 yoyo

任选其一：

```sh
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/yologdev/yoyo-evolve/main/install.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/yologdev/yoyo-evolve/main/install.ps1 | iex

# crates.io
cargo install yoyo-agent

# 或从 Releases 页面下载二进制
#   https://github.com/yologdev/yoyo-evolve/releases
```

验证安装：

```sh
yoyo --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key 并导出：

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. 配置

在项目根目录创建 `.yoyo.toml`（或全局 `~/.yoyo.toml`）：

```toml
provider = "deepseek"
model = "deepseek-v4-pro"      # 或 deepseek-v4-flash
thinking = "high"              # 以 reasoning_effort: "high" 发送
context_window = 1000000       # DeepSeek V4 支持 100 万 token 上下文
```

也可以直接用命令行参数，无需配置文件：

```sh
yoyo --provider deepseek --model deepseek-v4-pro --thinking high --context-window 1000000
```

yoyo 通过 OpenAI 兼容协议访问 `https://api.deepseek.com/v1`。思考模式通过将 yoyo 的 `thinking` 级别映射为请求中的 `reasoning_effort` 字段来启用——`high` 是 yoyo 当前发送的最高级别。请不要为了绕过报错而关闭思考模式；DeepSeek V4 默认开启思考，在这里开箱即用。

> **注意：** 当前版本的 yoyo 会打印一条无害的 `Unknown model 'deepseek-v4-pro'` 警告然后继续运行——内置模型列表仍是 2026 年 4 月改名前的旧名称。已在 [yologdev/yoyo-evolve#584](https://github.com/yologdev/yoyo-evolve/issues/584) 跟踪；上面的配置即当前模型的正确用法，现在就能用。

#### 4. 首次运行

```sh
cd /path/to/my-project

# 交互式 REPL（默认）
yoyo

# 单次提问
yoyo "解释一下这个代码库"

# 管道输入
echo "为 src/parser.rs 写测试" | yoyo
```

在 REPL 中，`/help` 显示分组的命令参考。几个值得了解的命令：

| 命令 | 作用 |
|---|---|
| `/plan` | 实现前先做规划 |
| `/spawn <task>` | 委派给子代理（`--parallel` 并行、`--bg` 后台） |
| `/watch` | 每次修改后自动运行 lint + test |
| `/risk` | 基于 git 历史的文件风险评分 |
| `/model`、`/provider` | 会话中切换模型或提供商 |
| `/cost`、`/tokens` | 花费与上下文窗口用量 |
| `!<cmd>` | 直接执行 shell 命令，零 token |

#### 配置参考

| 配置项（`.yoyo.toml`） | 命令行参数 | 说明 |
|---|---|---|
| `provider = "deepseek"` | `--provider deepseek` | 选择 DeepSeek API |
| `model` | `--model` | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| `thinking` | `--thinking` | `off` / `minimal` / `low` / `medium` / `high` → `reasoning_effort` |
| `context_window` | `--context-window` | 设为 `1000000` 以使用 DeepSeek V4 的 100 万 token 上下文 |
| — | `DEEPSEEK_API_KEY` | API Key（环境变量） |

#### MCP 与技能

- **MCP 服务器** —— 在 `.yoyo.toml` 中配置 `mcp = ["npx some-mcp-server"]`，或使用 `--mcp <cmd>`（stdio 传输）。yoyo 会预检工具名，避免与内置工具冲突。
- **技能** —— `--skills <dir>` 加载带 YAML frontmatter 的 markdown 技能文件；`/skill install gh:user/repo` 安装社区技能。
- **自定义命令** —— 在 `.yoyo/commands/` 放置 `.md` 文件即可注册自己的斜杠命令。
