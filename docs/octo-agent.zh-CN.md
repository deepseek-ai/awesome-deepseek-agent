[English](./octo-agent.md) | [简体中文](./octo-agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 octo-agent

octo-agent 是一款开源的通用 AI Agent，同时具备 Coding Agent 与 General Agent 能力。它内置终端交互（TUI）、本地 Web UI、工具调用、MCP 支持、Skills 以及人工确认审批机制，开箱即用。

- **GitHub：** <https://github.com/open-octo/octo-agent>

#### 1. 安装 octo-agent

```sh
# macOS / Linux
curl -fsSL https://octo-agent.dev/install.sh | sh

# Windows：从最新 release 下载安装器
# https://github.com/open-octo/octo-agent/releases/latest
```

或从 [GitHub Releases](https://github.com/open-octo/octo-agent/releases/latest) 页面下载对应平台的预编译二进制。

验证安装：

```sh
octo --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。推荐将其设置为环境变量：

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. 将 DeepSeek 配置为默认 Provider

octo-agent 原生支持 OpenAI 与 Anthropic 两种通信协议。DeepSeek 同时提供两种兼容端点，任选其一即可。

**方案 A：OpenAI 兼容端点（推荐）**

```sh
octo config
# 选择：OpenAI-compatible → base URL 填 https://api.deepseek.com/v1 → model 填 deepseek-chat
```

或使用 `custom` provider 配合 OpenAI 协议：

```sh
CUSTOM_BASE_URL=https://api.deepseek.com/v1 \
CUSTOM_API_KEY=$DEEPSEEK_API_KEY \
  octo --provider custom --protocol openai --model deepseek-chat "..."
```

**方案 B：Anthropic 兼容端点**

```sh
octo config
# 选择：Custom → 协议选 Anthropic → base URL 填 https://api.deepseek.com/anthropic → model 填 deepseek-chat
```

保存为默认值后，后续无需重复输入 flag：

```sh
octo config
octo config show   # 打印生效配置
octo config path   # 打印配置文件路径
```

#### 4. 开始使用 octo-agent

在终端执行一次性任务：

```sh
octo "解释 README 并给出三条改进建议"
```

启动交互式 TUI：

```sh
octo
```

启动本地 Web 服务（默认 `http://127.0.0.1:8088`）：

```sh
octo serve
```

#### 5. 模式与权限控制

octo-agent 支持三种权限模式：

| 模式 | 行为 |
|---|---|
| **interactive** | 执行 shell、修改文件等副作用操作前需人工确认（默认） |
| **strict** | 更保守的审批策略 |
| **auto** | 自动批准工具调用，请谨慎使用 |

可通过 `octo config` 交互设置，也可每次运行单独指定：

```sh
octo --permission-mode interactive "..."
```

#### 配置参考

常用环境变量与 CLI flag：

| 变量 / flag | 说明 |
|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API Key |
| `OPENAI_API_KEY` | 选择 `--provider openai` 时使用 |
| `CUSTOM_BASE_URL` | `custom` provider 的 Base URL |
| `CUSTOM_API_KEY` | `custom` provider 的 API Key |
| `--model` | 按配置中的 `model` 名称选择模型 |
| `--reasoning-effort` | `low` \| `medium` \| `high` \| `xhigh` \| `max` |
| `--show-reasoning` | 在 Web UI 中展示推理/思考过程 |
| `--no-tools` | 纯聊天模式，不触发工具循环 |

完整配置 schema 位于 `~/.octo/config.yml`。全部选项见 [octo-agent 配置参考](https://octo-agent.dev/docs/reference/config-file/)。

#### 本地服务与 API

`octo serve` 会启动本地 HTTP + WebSocket 服务。默认监听 `127.0.0.1:8088`，回环地址无需认证；如需暴露到非本地网络，请在 `~/.octo/config.yml` 中设置 `access_key`。

```sh
octo serve
```

该服务同时驱动 Web UI、会话管理和流式对话。接口契约见 [HTTP API 参考](https://octo-agent.dev/docs/reference/http-api/)。

#### MCP 与 Skills

- **MCP 服务器** —— 在 `~/.octo/mcp.json` 中配置，或在聊天中通过 slash 命令管理。
- **Skills** —— 将 `SKILL.md` 放入 `~/.octo/skills/<name>/`（用户级）或 `./.octo/skills/<name>/`（项目级）。
- **子 Agent** —— 模型可派生子 Agent 以委派任务。

更多用法见 [octo-agent 指南](https://octo-agent.dev/docs/guides/)。
