[English](./dscode.md) | [简体中文](./dscode.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 dscode

不同于面向开发者的通用编程 Agent，dscode 是一款开源终端 AI Agent，产品定位是链接创作类 MCP 工具，服务创作者而非开发者。作为 DeepSeek 原生 Harness，提供文件操作、Shell 执行、代码搜索、权限控制、会话持久化、上下文管理、记忆系统、Skills 系统以及 MCP 协议支持。

- **GitHub：** <https://github.com/wangcan26/dscode>

#### 1. 安装 dscode

- 安装 [Node.js](https://nodejs.org/en/download/) 20.6+ 版本。
- 克隆仓库并安装依赖：

```bash
git clone https://github.com/wangcan26/dscode.git
cd dscode
npm install
cp .env.example .env
```

#### 2. 配置 DeepSeek API Key

编辑 `.env` 文件，填入你的 DeepSeek API Key：

```bash
DEEPSEEK_API_KEY=sk-...
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

#### 3. 配置模型与思考模式

dscode 支持两级配置（用户级和项目级）：

- **用户级：** `~/.dscode/config.json`
- **项目级：** `<project>/.dscode/config.json`

优先级：**环境变量 > 项目级 config.json > 用户级 config.json > 默认值**

```jsonc
{
  "modelId": "deepseek-v4-pro",
  "thinkingLevel": "xhigh",
  "maxTokens": 16384
}
```

**核心配置选项：**

| 选项 | 环境变量 | 默认值 | 说明 |
|------|---------|--------|------|
| `modelId` | `AGENT_MODEL` / `DEEPSEEK_MODEL` | `deepseek-v4-flash` | 模型 ID — `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| `thinkingLevel` | `AGENT_THINKING_LEVEL` | Pro: `medium`，Flash: `off` | 思考强度 — `off`、`medium`、`high` 或 `xhigh`（最大推理） |
| `maxTokens` | `DSCODE_MAX_TOKENS` | `16384` | 单次最大输出 token 数 |

> **思考模式：** 设置 `thinkingLevel` 为 `xhigh` 或 `AGENT_THINKING_LEVEL=xhigh` 即可启用最大推理强度（`reasoning_effort: "max"`）。底层 pi-ai 框架自动配置 100 万 token 上下文窗口（`contextWindow: 1000000`）和 DeepSeek 专有的 thinking 格式。

#### 4. 运行 dscode

```bash
npm start
```

或指定项目路径：

```bash
DSCODE_PROJECT_PATH=/path/to/my-project npm start
```

启动后将看到 `you ›` 提示符：

```
dscode  (deepseek-v4-pro)
Type a message. /help for commands. exit to quit.

you ›
```

#### Slash 命令

| 命令 | 说明 |
|------|------|
| `/help` | 显示所有命令 |
| `/reset` | 清空对话历史 |
| `/session list` | 列出已保存会话 |
| `/session save` | 保存当前会话 |
| `/session load <id>` | 恢复历史会话 |
| `/memory list` | 查看记忆 |
| `/memory add <内容>` | 手动添加记忆 |
| `/skills` | 列出 Skills 及状态 |
| `/skills activate <name>` | 激活 Skill |
| `/drivers` | 列出已加载的驱动 |
| `/permissions` | 查看当前权限授予 |
| `/cost` | 显示 token 用量 |
| `/compact` | 手动压缩上下文 |

输入 `exit` 或按 `Ctrl+C` 两次退出。按 `Ctrl+C` 一次中断生成。
