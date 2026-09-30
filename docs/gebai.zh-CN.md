[English](./gebai.md) | [简体中文](./gebai.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 GEBAI（歌白）

GEBAI（歌白智能体）是一个开源 AI 智能体引擎，围绕一条稳定的核心主循环构建：**对话 → 工具调用 → 审批 → 执行**。模型无状态、可替换；记忆与责任长在智体——需跨轮次保留的内容写入文件或会话记录，每次工具调用都经审批执行、留痕可审计。桌面应用、本地浏览器与服务端部署共享同一套代码。

- **GitHub：** <https://github.com/xuxinle/gebai>

#### 1. 安装 GEBAI

GEBAI 需要 [Bun](https://bun.sh) ≥ 1.2。克隆仓库并安装依赖：

```sh
git clone https://github.com/xuxinle/gebai.git
cd gebai
bun install
```

#### 2. 配置 DeepSeek

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后从模板创建环境变量文件：

```sh
cp .env.example .env      # Windows: copy .env.example .env
```

编辑 `.env`，将模型指向 DeepSeek：

```
GEBAI_LLM_API_BASE=https://api.deepseek.com
GEBAI_LLM_API_KEY=sk-your-key-here
GEBAI_LLM_MODEL=deepseek-v4-pro

# 100 万 token 上下文窗口，最高 384K 输出
GEBAI_LLM_MAX_CONTEXT=1000000
GEBAI_LLM_MAX_OUTPUT_TOKENS=384000

# 推理强度拉满（思考模式默认开启）
GEBAI_LLM_EXTRA_PARAMS={"reasoning_effort":"max"}
```

- `deepseek-v4-pro` 推理能力最强；追求更快、更低成本可改用 `deepseek-flash`（旧文档中的 `deepseek-v4-flash` 仍兼容接受）。
- DeepSeek V4 支持 100 万 token 上下文窗口与最高档思考强度，`reasoning_effort` 可取 `low`、`high` 或 `max`，详见 [Thinking Mode 文档](https://api-docs.deepseek.com/guides/thinking_mode)。
- 模型也可完全在浏览器中配置：**设置 → 环境变量**（仅保存在浏览器本地，随消息临时注入）。

#### 3. 首次运行

```sh
bun run dev
```

打开 <http://127.0.0.1:3000> 即可开始对话——GEBAI 将以 DeepSeek 为推理引擎，工具调用、计划审批、子 Agent 与审计留痕开箱即用。

如需构建单文件独立二进制（不依赖 Bun 运行时）替代源码运行，见 [GEBAI 仓库 README](https://github.com/xuxinle/gebai)。

#### 排错

- `401` / 认证错误：检查 `.env` 中的 `GEBAI_LLM_API_KEY`（前后无多余空格），并确认 `GEBAI_LLM_API_BASE=https://api.deepseek.com`；`.env` 需位于仓库根目录。
- `Model Not Found` / `404`：确认 `GEBAI_LLM_MODEL` 使用当前模型名（`deepseek-v4-pro` 或 `deepseek-flash`）。
- 3000 端口被占用：在 `.env` 中设置 `GEBAI_PORT` 为其他端口后再运行 `bun run dev`。
