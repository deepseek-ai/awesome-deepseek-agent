[English](./ok.md) | [简体中文](./ok.zh-CN.md) ↩ [← 返回](./../README.zh-CN.md)

# 接入 OK

OK 是一个开源的 **AI Agent 基础设施** —— 单个 15 MB 静态二进制文件，集成了自我
进化技能、多 Agent DAG 编排、OS 级沙箱（macOS Seatbelt、Linux Landlock、Windows
AppContainer）、MCP 原生插件支持，以及密码学 ProofChain 审计追踪。开箱即
提供 TUI、桌面端（Wails）、VS Code 和 JetBrains 前端，外加 7 个聊天平台机器人。

DeepSeek 是 OK 的 **默认且推荐** 的模型提供者。配置预置了 `deepseek-v4-flash`
和 `deepseek-v4-pro`，包含 100 万 token 上下文窗口、最大思考强度，无中间层直
接调用 `api.deepseek.com`。

#### 1. 前置条件

- [Go](https://go.dev/dl/) 1.22+（从源码构建），或下载
  [预编译二进制](https://github.com/NB-Agent/ok/releases)。
- **Windows 用户** —— 建议安装 Git for Windows，使 `bash` 工具开箱即用。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。
将其设置为 `DEEPSEEK_API_KEY` 环境变量——OK 启动时读取，绝不写入磁盘。

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. 安装 OK

```sh
# 从源码构建（推荐 —— 单个静态二进制）
git clone https://github.com/NB-Agent/ok.git
cd ok
make build          # → bin/ok
# 或: make cross    # → dist/ (darwin|linux|windows × amd64|arm64)

# 移动到 PATH 目录
mv bin/ok /usr/local/bin/
```

或从 [releases 页面](https://github.com/NB-Agent/ok/releases) 下载预编译二进制。

#### 4. 配置

运行配置向导（交互式，在当前目录创建 `ok.toml`）：

```sh
ok setup
```

当提示选择提供者时，选择 **DeepSeek**。向导会启用 `deepseek-v4-flash`
（默认执行模型）和 `deepseek-v4-pro`（用于复杂任务）。

或将以下最小 `ok.toml` 复制到项目根目录：

```toml
default_model = "deepseek"

[[providers]]
name           = "deepseek"
kind           = "openai"
base_url       = "https://api.deepseek.com"
models         = ["deepseek-v4-flash", "deepseek-v4-pro"]
default        = "deepseek-v4-flash"
api_key_env    = "DEEPSEEK_API_KEY"
context_window = 1000000
```

> [!TIP]
> 在 `[agent]` 下设置 `planner_model = "deepseek-v4-pro"` 可启用双模型协作
> ——低频规划器（Pro）负责任务分解，快速执行器（Flash）负责具体执行。

OK 通过 OpenAI 兼容的 `reasoning_effort` 参数自动为 `deepseek-v4-pro`
配置 **最大思考强度**，无需额外配置即可获得最佳编码体验。

#### 5. 首次运行

```sh
# 进入项目目录
cd /path/to/my-project

# 交互式聊天
ok chat

# 无头模式（CI / 脚本）
ok run "实现 main.go 中的 TODO"

# 单任务使用 Pro
ok run --model deepseek-v4-pro "为这个函数添加单元测试"
```

在 `ok chat` 中，输入 `/init` 生成 `AGENTS.md`（项目记忆），让 Agent 理解你的
代码库。输入 `/help` 查看完整的 slash 命令参考。

<div align="center">
<img src="https://raw.githubusercontent.com/NB-Agent/ok/main/docs/logo.svg" width='640' />
</div>
