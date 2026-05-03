[English](./dscli.md) | [简体中文](./dscli.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 dscli

dscli 是一个 AI 增强的开发者工具箱，运行在终端内。它直接对接 DeepSeek API，支持 AI 对话与工具调用（文件操作、Git、代码搜索等）、代码补全等功能。

- **GitCode：** <https://gitcode.com/dscli/dscli>

#### 1. 安装 Go

- 安装 [Go](https://go.dev/dl/) 1.26 及以上版本。

#### 2. 安装 dscli

```bash
# 使用 go install 安装（推荐）
go install gitcode.com/dscli/dscli@latest

# 或从源码克隆并构建
git clone https://gitcode.com/dscli/dscli.git
cd dscli
make install
```

验证安装：

```bash
dscli version
```

#### 3. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

#### 4. 配置

通过 `dscli config edit` 或 `vim ~/.dscli/config.dscli` 设置 API Key 到 `~/.dscli/config.dscli` ：

```text
deepseek-api-key = sk-...
```

配置文件存储在 `~/.dscli/` 目录下：

- `config.dscli` — 环境变量覆盖配置
- `sqlite.db` — 对话历史数据库
- `skills` — 全局技能目录

#### 5. 使用 dscli

**AI 对话与工具调用：**

```bash
# 单行对话
echo "帮我创建一个包含 HTTP 服务器的 main.go 文件" | dscli chat

# 多行对话
dscli chat <<EOF
帮我创建一个 HTTP 服务器的 main.go 文件，其中监听端口号从环境
变量获取，对/websocket使用websocket监听，任何不清楚问题直接问我。
EOF
```

**代码补全：**

```bash
echo "func fibonacci(n int) int {" | dscli fim
```

**查看模型和余额：**

```bash
# 查看可用模型
dscli models

# 查看账户余额
dscli balance

# JSON 格式输出
dscli models --format json
dscli balance --format json
```

#### 核心特性

- **工具调用** — AI 可直接读写文件、执行 Git 命令、搜索代码等
- **项目感知** — 自动识别 Git 仓库根目录，按项目隔离对话历史
- **多格式输出** — 支持 Markdown（默认）和 Org 模式
- **流式输出** — 通过 `--stream` 实现逐 Token 实时输出
- **SQLite 存储** — 持久化对话历史，支持上下文感知的连续对话

#### IDE 集成

dscli 提供编辑器插件，让你在编辑器中无缝使用 AI 辅助：

- **Emacs** — [dscli.el](https://gitcode.com/dscli/dscli.el)
- **Vim** — [dscli.vim](https://gitcode.com/dscli/dscli.vim)
- **VSCode** — [dscli.vscode](https://gitcode.com/dscli/dscli.vscode)

#### 快捷键 / 参数

| 参数 | 说明 |
| --- | --- |
| `--model` | 使用的模型：`deepseek-v4-pro`（默认）或 `deepseek-v4-flash` |
| `--mode` | 输出模式：`markdown`（默认）或 `org` |
| `--stream` | 启用流式输出 |
| `--histsize` | 加载的历史消息数量（默认：8） |
| `--verbose` | 启用详细/调试输出 |
| `--no-color` | 禁用颜色输出 |
| `--no-timestamp` | 禁用时间戳显示 |
