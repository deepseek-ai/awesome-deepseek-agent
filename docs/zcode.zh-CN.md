[English](./zcode.md) | [简体中文](./zcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Z Code

Z Code 是一款用 Zig 编写的开源 AI 编程 Agent —— **1.7 MB 原生二进制**，零依赖。提供交互式 REPL、7 个内置工具、流式输出、会话持久化与多供应商支持（DeepSeek、Moonshot、Ollama）。无需运行时、无需 npm install，一个静态可执行文件即可运行。

- **GitHub：** <https://github.com/RenovZ/zcode>

#### 1. 安装 Z Code

**环境要求：** Zig ≥ 0.16.0

```sh
# 克隆并构建
git clone https://github.com/RenovZ/zcode.git
cd zcode
zig build
```

编译产物是单个静态可执行文件 `./zig-out/bin/zcode`。将其复制到 `PATH` 中的任意位置：

```sh
cp ./zig-out/bin/zcode /usr/local/bin/
```

验证安装：

```sh
zcode --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

设置为环境变量：

```sh
export DEEPSEEK_API_KEY="sk-..."
```

如需使用中国区节点：

```sh
export DEEPSEEK_BASE_URL="https://api.deepseeki.com"
```

Z Code 启动时自动检测 `DEEPSEEK_API_KEY` 并启用 DeepSeek 供应商。也可将凭证存放在 `~/.zig-code/agent/auth.json` 中。

#### 3. 进入项目目录并启动

```sh
cd /path/to/my-project
zcode
```

Z Code 进入交互式 REPL 模式，默认使用第一个可用 DeepSeek 模型（通常为 **deepseek-v4-pro**）。输入 prompt 后按 `Enter` 即可，响应会实时流式输出。

**非交互模式**（单次对话）：

```sh
zcode "解释一下 src/main.zig"
```

**继续上次会话：**

```sh
zcode -c
```

#### 交互命令（REPL）

| 命令 | 说明 |
|---|---|
| `/help` | 显示可用命令 |
| `/quit`、`/exit` | 退出程序 |
| `/session` | 显示当前会话信息（ID、模型、思考等级） |
| `/stats` | 显示 Token 用量、费用估算和内存占用 |
| `/new` | 开启新会话 |
| `/model <id>` | 切换模型（例如 `deepseek-v4-flash`） |
| `/thinking <level>` | 设置思考等级：`off`、`low`、`medium`、`high`、`xhigh` |
| `/name <name>` | 为当前会话命名 |
| `/clear` | 清屏 |

#### 快捷键

| 按键 | 操作 |
|-----|------|
| `Enter` | 发送 prompt |
| `Shift+Enter` | 插入换行（多行输入） |
| `Ctrl+C` | 中断当前模型回合 |
| `Ctrl+D` | 退出程序 |

#### CLI 参数

| 参数 | 说明 |
|---|---|
| `--provider <name>` | 指定供应商：`deepseek`、`moonshot` 或 `ollama` |
| `--model <id>` | 模型 ID（例如 `deepseek-v4-pro`、`deepseek-v4-flash`） |
| `--thinking <level>` | 思考等级：`off`、`low`、`medium`、`high`、`xhigh` |
| `-c`、`--continue` | 继续最近一次会话 |
| `-r`、`--resume <id>` | 恢复到指定 ID 的会话 |
| `--tools <list>` | 用逗号分隔指定启用的工具 |
| `--debug` | 显示调试输出 |
| `--help` | 显示帮助 |

#### 配置

设置文件位于 `~/.zig-code/agent/settings.json`：

```json
{
  "defaultProvider": "deepseek",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "xhigh",
  "hideThinkingBlock": false
}
```

| 键 | 类型 | 说明 |
|---|---|---|
| `defaultProvider` | string | 默认供应商（`deepseek`、`moonshot`、`ollama`） |
| `defaultModel` | string | 默认模型 ID |
| `defaultThinkingLevel` | string | 默认思考等级（`off`、`low`、`medium`、`high`、`xhigh`） |
| `hideThinkingBlock` | bool | 流式输出时隐藏思考过程 |

> **100 万 Token 上下文：** Z Code 原生识别 DeepSeek-V4 的 1,000,000 token 上下文窗口和 384,000 token 最大输出。在 REPL 中使用 `/stats` 监控上下文用量。

> **思考等级：** DeepSeek-V4-Pro 支持多级推理强度。建议设置 `--thinking xhigh`（或在 REPL 中使用 `/thinking xhigh`）以获得最佳编程体验。详见 [Thinking Mode 文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。

#### 内置工具

交互模式下默认启用全部 7 个工具：

| 工具 | 说明 |
|---|---|
| `bash` | 执行 Shell 命令 |
| `edit` | 使用精确的查找替换编辑文件 |
| `read` | 读取文件内容 |
| `write` | 创建或覆盖文件 |
| `ls` | 列出目录内容 |
| `find` | 按 glob 模式查找文件 |
| `grep` | 搜索文件内容 |

#### 会话持久化

会话以 SQLite 数据库形式存储在 `~/.zig-code/agent/sessions/`。使用 `-c` 继续上次会话，或使用 `-r <id>` 恢复指定会话。每次会话的 Token 统计和费用估算都会被跟踪记录。
