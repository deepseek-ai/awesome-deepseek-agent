[English](./bernstein.md) | [简体中文](./bernstein.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Bernstein

Bernstein 是一个开源（Apache-2.0）的 AI 编程智能体治理层。它本身不调用模型：它为每个任务在独立的 git worktree 中运行一个智能体 CLI（Claude Code、Codex、Kilo Code、Crush、Aider 等），用测试和策略检查对结果进行门禁，并把每一步写入防篡改的审计日志，生成可离线验证的运行回执。

本指南介绍两种在 Bernstein 下使用 DeepSeek V4 的方式：

- **A. 通过智能体 CLI 调用 DeepSeek API** —— 最常见的用法。示例使用 Claude Code；本仓库其他指南中的任意智能体 CLI，只要已按其指南配置好 DeepSeek，都可以同样接入。
- **B. 自托管 DeepSeek V4 权重**，通过 Bernstein 的 `ollama` 适配器（在自己的硬件上运行 Ollama 或 vLLM）。

### 安装 Bernstein

- 安装 Python 3.11+ 和 [uv](https://docs.astral.sh/uv/)（或 pipx）。
- 安装 Bernstein，并在你的仓库中创建工作区：

```
uv tool install bernstein      # 或：pipx install bernstein
cd your-project
bernstein init                 # 创建 .sdd/ 和 bernstein.yaml
bernstein doctor               # 检查已安装并登录的智能体 CLI
```

`bernstein doctor` 会列出它找到的适配器。方式 A 至少需要安装一个智能体 CLI（下面的示例使用 Claude Code，安装方法见本仓库中它自己的指南）。

### A. 通过智能体 CLI 调用 DeepSeek API

#### 1. 为 DeepSeek 配置智能体 CLI

Bernstein 以过滤后的环境变量启动每个 worker：你在 shell 中 `export` 的变量**不会**传给 worker。请通过智能体 CLI 自己的配置文件进行配置，CLI 会自行读取。

对于 Claude Code，把 DeepSeek 配置写入 `~/.claude/settings.json`（文件不存在则新建）：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<你的 DeepSeek API Key>",
    "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash[1m]",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_EFFORT_LEVEL": "max"
  }
}
```

API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。`[1m]` 后缀启用 100 万 token 上下文窗口。

先确认 CLI 单独可用，再接入 Bernstein：

```
claude -p "请回复你当前运行的模型名称。"
```

#### 2. 让 Bernstein 使用该 CLI 和模型

编辑项目中的 `bernstein.yaml`。`model` 的值会原样传给 CLI（`claude --model deepseek-v4-pro[1m]`），`effort: max` 会变成 `--effort max`：

```yaml
goal: "在这里描述交给智能体的任务。"
cli: claude
max_agents: 2

role_model_policy:
  manager:
    cli: claude
    model: deepseek-v4-pro[1m]
    effort: max
  backend:
    cli: claude
    model: deepseek-v4-pro[1m]
    effort: max
  docs:
    cli: claude
    model: deepseek-v4-flash[1m]
    effort: high

quality_gates:
  enabled: true
  tests: true
  test_command: python -m pytest -q
```

规划、实现和评审类角色使用 `deepseek-v4-pro[1m]`；文档或杂务类角色可以使用更便宜的 `deepseek-v4-flash[1m]`。对于 DeepSeek 模型名，Bernstein 不会添加 `--fallback-model`，因此请求失败会让任务失败，而不是悄悄切换到别的模型。

#### 3. 首次运行

```
bernstein run --audit
```

Bernstein 为每个任务创建一个 worktree，在其中运行智能体 CLI，执行 `test_command`，并把运行记录写入 `.sdd/runs/<run_id>/`。检查审计链和运行回执：

```
bernstein audit verify
bernstein verify receipt .sdd/runs/<run_id>/run-receipt.json
```

回执中记录了每个任务使用的 CLI 和模型名，评审者无需访问你的 API 账号即可确认运行使用的是 `deepseek-v4-pro[1m]`。

#### 其他智能体 CLI

同样的 `bernstein.yaml` 结构适用于 `bernstein adapters list` 列出的任意适配器。先按本仓库中该 CLI 的指南为它配置 DeepSeek，再按角色设置 `cli:` 和 `model:`，例如 `cli: codex` 加上该 CLI 期望的模型名。写代码的角色请保持 `effort: max`。

### B. 自托管 DeepSeek V4 权重

DeepSeek V4 Flash 和 Pro 以开放的 MoE 权重发布。Bernstein 的 `ollama` 适配器支持任何 OpenAI 兼容的 `/v1/chat/completions` 端点，因此 Ollama 守护进程和 vLLM 服务都可以使用：

```
# 单 GPU 上通过 Ollama 运行 Flash
export OLLAMA_API_BASE=http://10.0.0.5:11434

# 多 GPU vLLM 服务上运行 Pro
python -m vllm.entrypoints.openai.api_server \
    --model deepseek-ai/deepseek-v4-pro \
    --tensor-parallel-size 8 --host 10.0.0.5 --port 8000
export OLLAMA_API_BASE=http://10.0.0.5:8000/v1
```

```yaml
cli: ollama
role_model_policy:
  backend:
    cli: ollama
    model: deepseek-v4-pro
    effort: max
```

注意：对于 DeepSeek V4 模型名，`ollama` 适配器会启用数据驻留检查，只接受回环、私有网络或内部后缀的端点（`localhost`、`10.x`、`192.168.x`、`*.internal` 等）。把该适配器指向公网 DeepSeek API 会在启动时被拒绝并报 `RESIDENCY_VIOLATION`；公网 API 请使用方式 A。

### 检查运行结果

- `bernstein status` 显示运行中和已完成的任务。
- `.sdd/runs/<run_id>/` 保存审计日志、血缘记录和运行回执。
- `bernstein verify receipt <file>` 只需要该文件：不联网，不需要 API Key。

### 链接

- Bernstein：https://github.com/sipyourdrink-ltd/bernstein
- 文档：https://docs.bernstein.run
- DeepSeek API 文档：https://api-docs.deepseek.com/
- DeepSeek 思考模式：https://api-docs.deepseek.com/guides/thinking_mode
