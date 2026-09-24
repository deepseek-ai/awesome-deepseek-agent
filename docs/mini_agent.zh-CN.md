[English](./mini_agent.md) | [简体中文](./mini_agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 mini-agent

[mini-agent](https://github.com/ftfw0621/mini-agent) 是一个仿照 Claude Code 实现的开源终端编程 Agent，使用 TypeScript 编写，支持 Ink 终端界面、Skill、MCP（stdio + HTTP）、allow / ask / deny 权限、plan 与 auto 模式、上下文压缩，以及非交互的 `-p` 模式。默认直接连接 `api.deepseek.com`。npm 包名为 `agent-from-zero`。

#### 1. 安装 Node.js

安装 [Node.js](https://nodejs.org/zh-cn/download/) 20.6 或更高版本。

#### 2. 配置 API Key 和模型

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后和模型一起写进 shell 配置文件（`~/.zshrc` 或 `~/.bashrc`）：

```bash
export DEEPSEEK_API_KEY=sk-...
export MINI_AGENT_MODEL=deepseek-flash   # 复杂任务可改用 deepseek-v4-pro
```

执行 `source ~/.zshrc`，或新开一个终端。

#### 3. 在项目目录中运行

```bash
cd /path/to/my-project
npx agent-from-zero --effort max
```

- **推理强度**：`--effort max` 会开启思考模式并发送 `reasoning_effort: "max"`。会话中可用 `/effort` 在 `none`、`low`、`high`（API 默认值）和 `max` 之间切换。工具调用之间会自动回传 `reasoning_content`。
- **1M 上下文**：上下文窗口默认就是 DeepSeek 的 100 万 token，用到 80% 时自动压缩，无需额外配置。
- **切换模型**：`/model` 可在当前会话中切换到 API 提供的其他模型。

输入 `/help` 查看全部命令。
