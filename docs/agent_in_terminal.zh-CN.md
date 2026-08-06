[English](./agent_in_terminal.md) | [简体中文](./agent_in_terminal.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Agent-in-Terminal

Agent-in-Terminal 是一个超轻量 Linux 终端 AI Agent——单个 11.4 KB 的 Python 文件，零依赖，支持机器绑定加密的 API Key 存储，以及唯一一个带安全闸门的 shell 工具。

- **GitHub：** <https://github.com/Xiyinnnnnn/Agent-in-Terminal>

#### 1. 一键安装

```bash
# 全球 CDN（国内直连，无需代理）
curl -fsSL https://cdn.jsdelivr.net/gh/Xiyinnnnnn/Agent-in-Terminal@main/install.sh | bash

# GitHub 直连（海外用户）
curl -fsSL https://raw.githubusercontent.com/Xiyinnnnnn/Agent-in-Terminal/main/install.sh | bash
```

安装脚本自动双源回退。

#### 2. 首次运行——输入 API Key

```bash
python3 ~/.local/bin/term_agent/term_agent.py
```

Key 输入不可见（`getpass`），使用机器指纹种子加密后落盘到 `~/.config/term_agent/key.bin`——唯一落盘项，不出现明文。

#### 3. 使用

输入问题，Agent 以 shell 命令为唯一工具，循环执行 LLM ↔ `tool_calls`（MAX_ROUNDS=30 软上限）。输入 `exit` 退出。

#### DeepSeek 配置

Agent-in-Terminal 直连 `api.deepseek.com/chat/completions`，默认模型 **`deepseek-v4-flash`**——在 `term_agent.py` 中修改 `MODEL` 即可切换 `deepseek-v4-pro`。请求体已内置 `reasoning_effort: "max"` 与 `thinking: {type: "enabled"}`，开箱即用 **max 深度思考**。

**100 万 token 上下文**由 900K 压缩链处理：`compress()` 在 900K 阈值处自动 summarize 历史，长会话持续可用，不超出 DeepSeek V4 的 1M 上下文。

#### 安全模型

`run_terminal()` 是唯一工具——所有能力收敛到 shell 执行。命中黑名单的命令在 `subprocess` 之前被拦截，需 Y/N 确认；N 或 30s 超时=拒绝。LLM 无法绕过闸门。
