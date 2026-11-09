[English](./revo.md) | [简体中文](./revo.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Revo

Revo 是一款 MIT 协议的**终端 Agent harness**。它不维护 session 列表，而是让同一个 agent 持续活着：启动后第一轮工作循环无需任何提示就自行开始，
每一轮是 `observe -> model -> act -> verify -> update self -> next cycle`；它只保留一份追加式生命日志（append-only life log）和一份带校验和的
休眠快照，因此未完成的工作意图可以在休眠与重启后继续。

Revo 只要求 **OpenAI 兼容的流式 Chat Completions**（带工具调用）。DeepSeek-V4 不需要任何协议转换层：Revo 会发送 `tools`、
`reasoning_effort: "high"`，并读取响应里的 `reasoning_content`；上下文预算默认就是 1,048,576 tokens。

#### 1. 安装 Node.js

- 安装 [Node.js](https://nodejs.org/en/download/) 22.19 或更新版本（`node --version` 确认）。
- Windows 用户：文档中实测的是 PowerShell 7。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 Key。

#### 3. 克隆并安装

```bash
git clone https://github.com/shyringo/revo.git
cd revo
npm ci --ignore-scripts
```

#### 4. 把 Revo 指向 DeepSeek

Revo 默认服务商是 OpenCode Go（`https://opencode.ai/zen/go/v1`）。三个环境变量即可切到 DeepSeek 官方 API：

```powershell
$env:REVO_API_KEY = "<你的 DeepSeek Key>"
$env:REVO_BASE_URL = "https://api.deepseek.com"
$env:REVO_MODEL = "deepseek-v4-flash"
```

需要更强模型时把 `deepseek-v4-flash` 换成 `deepseek-v4-pro`。Revo 每次认知调用都会带 `reasoning_effort: "high"`，
因此支持思考模式的模型会被按预期使用，无需额外配置。

可选项（1M 上下文长跑时）：

```powershell
$env:REVO_CONTEXT_WINDOW_TOKENS = "1048576"   # 默认值；用配置文件时建议显式写上
$env:REVO_MAX_OUTPUT_TOKENS = "65536"         # 默认单次调用 4096
```

#### 5. 唤醒它

```bash
npm start -- --for 5m
```

`--for 5m` 把第一次唤醒限制在 5 分钟。Revo 会打开全屏 TUI：`REVO ● AWAKE`、一行实时的 `attention`、一个 `cycle` 计数器，
`LIFE` 面板开始堆积观察与工具调用。它**不会**等你先说话。随时输入即可打断；`:sleep` 或一次 `Ctrl+C` 会整理记忆并退出。

#### 6. 不花 token 就验证接线

```powershell
npm link
revo --doctor
```

`--doctor` 会检查配置、凭据、模型锁定、宪法文件、状态目录、生命日志完整性和服务商模型目录。这里如果报服务商错误
（例如 HTTP 401），说明 Key 或 base URL 不对，先修好再唤醒。

#### 成本控制

Revo 醒着的时候会持续调用模型。用命令行参数或环境变量给它设上限：

```powershell
npm start -- --for 30m               # 强制醒着的时间上限
npm start -- --token-budget 200000   # 单次唤醒的 token 硬上限
npm start -- --status --json         # 不唤醒模型，读取待办与状态
npm start -- --delivery latest       # 不唤醒模型，打印最近一份已完成交付
```

它休眠之后不会再调用模型。

#### 说明

- 状态存在 `<workspace>/.revo/life.jsonl`（默认被 git 忽略）。在私有配置文件里写一个固定的 `stateDir`，可以让同一个身份跨工作目录复用：
  [config.example.json](https://github.com/shyringo/revo/blob/main/config.example.json)。
- Revo 是 v0.1 实验原型，带护栏但不是沙箱。把它指向不可信内容之前，请先读
  [Status](https://github.com/shyringo/revo#status) 与 [Security](https://github.com/shyringo/revo/blob/main/docs/security.md)。
- 中文 README：[zh-CN.md](https://github.com/shyringo/revo/blob/main/docs/zh-CN.md)。
