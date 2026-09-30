[English](./deepseek_dynamic_workflow.md) | [简体中文](./deepseek_dynamic_workflow.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeek Dynamic Workflow

DeepSeek Dynamic Workflow（DDW）是一个面向 DeepSeek agents 的 cache-first 动态工作流 runtime。它适合多 agent 分阶段并行运行：多个 agent 可以 fan-out 探索、复用稳定上下文、写入产物，并在 dashboard 中展示 prompt cache hit/miss 指标。

- **GitHub:** <https://github.com/giao-123-sun/DeepSeek-Dynamic-Workflow>
- **适用场景:** cache-aware 多 agent 研究、代码库审计、政策/法规对比、网页证据提取、工作流观测。

#### 1. 安装 Node.js

- 安装 [Node.js](https://nodejs.org/en/download/) 22+。
- Windows 用户建议同时安装 [Git for Windows](https://git-scm.com/download/win)。

#### 2. 从源码安装 DDW

```sh
git clone https://github.com/giao-123-sun/DeepSeek-Dynamic-Workflow.git
cd DeepSeek-Dynamic-Workflow
npm install
npm run build
npm run check
```

可选：把本地 CLI 暴露到当前 shell：

```sh
npm link
ddw-agent --help
```

历史命令名 `cf-dw-*` 仍作为兼容别名保留；新用户建议使用 `ddw-*` 命令。

#### 3. 获取 DeepSeek API Key

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。在 DDW 仓库中创建本地 `.env`：

```text
DEEPSEEK_API_KEY=sk-...
```

不要提交 `.env`。DDW 会从本地加载它，并把运行产物写入 `.cf-dw/`。

#### 4. 选择模型

DDW 示例使用当前 DeepSeek V4 模型名：

| 用途 | 模型 |
|---|---|
| 成本友好的工作流 agent | `deepseek-v4-flash` |
| 高价值 synthesis 或复杂 agent 工作 | `deepseek-v4-pro` |

DeepSeek V4 支持最高 **100 万 token** 上下文窗口。DDW 的 cache-first 设计会让多个 agent 复用稳定 prefix，使大块共享上下文在 warm run 中更便宜。

对于自治 harness run，DDW 暴露了包括 `max` 在内的 reasoning effort：

```sh
node dist/reasonix-agent.js \
  --cwd . \
  --prompt "Inspect this repository and summarize DDW's runtime model." \
  --cache-group-id ddw_harness_quickstart_v1 \
  --session-id auto \
  --model deepseek-v4-pro \
  --effort max \
  --budget 0.20 \
  --no-proxy
```

#### 5. 第一次 Native 运行

运行一个轻量 Native DDW agent：

```sh
node dist/index.js \
  --cwd . \
  --prompt "List the top-level files and summarize this project." \
  --cache-group-id ddw_quickstart_v1 \
  --session-id quickstart_native \
  --model deepseek-v4-flash \
  --max-turns 4
```

运行产物会写到：

```text
.cf-dw/runs/quickstart_native/
  session.json
  usage.jsonl
```

#### 6. 构建稳定 prefix

稳定 prefix 是 DDW prompt cache 策略的核心：

```sh
node dist/prefix-cli.js \
  --cwd . \
  --output .cf-dw/prefix/cache-prefix.xml \
  --style xml \
  --include "src/**/*.ts,README.md,package.json,odw*.json,examples/**/*.js,examples/**/*.json,examples/**/*.md" \
  --compress
```

在后续运行中使用 prefix：

```sh
node dist/index.js \
  --cwd . \
  --prompt "Explain the workflow dashboard and cache metrics." \
  --prefix-file ./.cf-dw/prefix/cache-prefix.xml \
  --cache-group-id ddw_quickstart_v1 \
  --session-id quickstart_with_prefix \
  --model deepseek-v4-flash
```

#### 7. 查看缓存指标和 dashboard

生成 cache report：

```sh
node dist/report.js --runs-root ./.cf-dw/runs
```

生成静态 workflow dashboard：

```sh
node dist/dashboard.js \
  --runs-root ./.cf-dw/runs \
  --latest-per-agent \
  --output ./.cf-dw/reports/ddw-dashboard.html
```

在浏览器中打开 `.cf-dw/reports/ddw-dashboard.html`。Dashboard 会展示 workflow status、phases、agents、tokens、tool calls、runtime、cache hit rate、effective tokens 和 artifact previews。

#### 8. Demo suite

DDW 提供了一组实用 demo：

```sh
npm run demo:dashboards
npm run release:audit
```

当前 release audit 会检查 5 个 demo 并汇总 prompt-cache 指标。撰写本指南时，本地 release audit 在 demo suite 上显示 23 个 agents，整体 cache hit rate 为 88.20%。

#### 说明

- DDW 是 source-available 的非商业项目，详见项目中的 `LICENSE.md`。
- 真实 DeepSeek 运行需要 `DEEPSEEK_API_KEY`，可能产生 API 成本。
- 项目保留 `.cf-dw/` 作为 runtime artifact 目录，以兼容已有 reports 和 dashboards。
