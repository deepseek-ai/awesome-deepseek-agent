[English](./agent_for_shell.md) | [简体中文](./agent_for_shell.zh-CN.md) · [← Back](../README.md)

# Integrate with Agent For Shell

Agent For Shell is a DeepSeek-powered terminal agent that ships as a **single `.sh` file**. It runs on Android terminals (幻·实验室 / Huàn Lab) and `adb shell`, using only `curl`, `awk`, `sed` and `grep` — all built into Android — with zero external dependencies.

- **GitHub:** <https://github.com/Xiyinnnnnn/Agent-For-Shell>

#### 1. Download the script

```bash
curl -L -o agent.sh "https://raw.githubusercontent.com/Xiyinnnnnn/Agent-For-Shell/main/Agent%20For%20Shell.sh"
```

#### 2. Configure the header parameters

Edit the `#param` lines at the top of the script:

```sh
#param: API_KEY|DeepSeek API Key|sk-xxx
#param: QUESTION|本次问题|帮我看看设备信息
#param: MODEL|模型名|deepseek-v4-flash
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `API_KEY` | — | DeepSeek API key (required) |
| `QUESTION` | `你好` | The prompt for this run |
| `MODEL` | `deepseek-v4-flash` | Model name — `deepseek-v4-flash` or `deepseek-v4-pro` |

#### 3. Run

```bash
sh agent.sh
```

Agent For Shell talks to `api.deepseek.com` directly and supports the **DeepSeek-V4** family. Its context budget defaults to `MAX_TOK=900000` — near DeepSeek V4's full **1M-token context window** — with automatic summarization when the budget is exceeded so long sessions stay alive. Set `REASONING_EFFORT=max` at the top of the script to enable DeepSeek-V4-Pro's deepest thinking for complex tasks.

#### Features

- **Batch tool calls** — one response can issue up to 8 `tool_calls`; the script executes them in order and backfills results without waiting for the previous one.
- **Physical-key approval** — dangerous commands (see blacklist) require a physical volume-key confirmation: Volume Up = allow, Volume Down = deny, 60s timeout = deny.
- **Zero dependencies** — pure POSIX sh, no Python / Node / third-party libraries.
- **Context compression** — history is summarized to a digest when the token budget is exceeded.
- **Memory system** — automatically reads/writes `/data/local/tmp/agent_mem/YYYYMMDD.md` for cross-session reuse.
- **Inherits adb permissions** — can run `dumpsys` / `getprop` / `settings` / `pm` / `am` directly.

#### Security model

Blacklist commands (`rm`, `dd`, `su`, `pm uninstall`, `pm clear`, `chmod -R 777`, `:(){` ...) require physical-key authorization before execution — the LLM cannot bypass it.
