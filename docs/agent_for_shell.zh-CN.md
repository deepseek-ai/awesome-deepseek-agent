[English](./agent_for_shell.md) | [简体中文](./agent_for_shell.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Agent For Shell

Agent For Shell 是一个由 DeepSeek 驱动的终端 Agent，整个 Agent 只用一个 **`.sh` 文件**交付。它运行在 Android 终端（幻·实验室）和 `adb shell` 中，仅依赖 Android 内置的 `curl`、`awk`、`sed`、`grep`，零外部依赖。

- **GitHub：** <https://github.com/Xiyinnnnnn/Agent-For-Shell>

#### 1. 下载脚本

```bash
curl -L -o agent.sh "https://raw.githubusercontent.com/Xiyinnnnnn/Agent-For-Shell/main/Agent%20For%20Shell.sh"
```

#### 2. 配置头部参数

编辑脚本顶部的 `#param` 参数行：

```sh
#param: API_KEY|DeepSeek API Key|sk-xxx
#param: QUESTION|本次问题|帮我看看设备信息
#param: MODEL|模型名|deepseek-v4-flash
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `API_KEY` | — | DeepSeek API Key（必填） |
| `QUESTION` | `你好` | 本次问题 |
| `MODEL` | `deepseek-v4-flash` | 模型名——`deepseek-v4-flash` 或 `deepseek-v4-pro` |

#### 3. 运行

```bash
sh agent.sh
```

Agent For Shell 直连 `api.deepseek.com`，支持 **DeepSeek-V4** 系列模型。上下文预算默认 `MAX_TOK=900000`，接近 DeepSeek V4 的 **100 万 token 上下文**上限，超限自动压缩历史摘要，长会话不断链。将脚本顶部的 `REASONING_EFFORT` 设为 `max`，即可启用 DeepSeek-V4-Pro 的深度思考模式，适合复杂任务。

#### 特性

- **批量工具调用** — 一次响应可发最多 8 条 `tool_calls`，脚本按序执行、逐条回填，无需等上一条返回
- **物理按键授权** — 危险命令（见黑名单）需物理按键确认：音量上=同意 / 音量下=拒绝 / 60s 超时=拒绝
- **零依赖** — 纯 POSIX sh，无 Python / Node / 第三方库
- **上下文压缩** — token 超限自动 summarize 历史为摘要
- **记忆系统** — 自动读写 `/data/local/tmp/agent_mem/YYYYMMDD.md`，跨会话复用结论
- **默认继承 adb 权限** — 可直接运行 `dumpsys` / `getprop` / `settings` / `pm` / `am` 等系统命令

#### 安全模型

黑名单命令（`rm`、`dd`、`su`、`pm uninstall`、`pm clear`、`chmod -R 777`、`:(){` 等）执行前必须经过物理按键授权，LLM 无法绕过。
