[English](./ante.md) | [简体中文](./ante.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Ante

> **最能发挥 DeepSeek-V4 实力的 Agent 框架** —— 在 Terminal-Bench 2.1 上以 DeepSeek-V4-Pro 取得领先成绩，仅 15 MB、零依赖的 Rust 二进制。

Ante 是 Antigma Labs 出品的 AI 原生、本地优先的 Agent 运行时，以单个自包含的 Rust 二进制分发，无任何外部依赖。它与模型提供商无关 —— 每次会话启动时都会从 catalog 中解析提供商与模型 —— 并内置 **`deepseek` 提供商**，原生对接 `api.deepseek.com`，支持 **DeepSeek-V4-Pro** 与 **DeepSeek-V4-Flash** 全 100 万 token 上下文。你可以通过 API Key、OAuth 或自定义 catalog 条目进行鉴权，并在会话中随时切换模型、提供商与推理强度。

**在 Terminal-Bench 2.1 上，框架决定差距。** 知名第三方独立评测 [vals.ai](https://www.vals.ai/benchmarks/terminal-bench-2-1) 给出 **DeepSeek-V4 在 Terminal-Bench 2.1 上 50.19%** 的成绩。而 Ante 在同一基准上将 **DeepSeek-V4-Pro 提升到 64%**，即便是 **DeepSeek-V4-Flash 也达到 62%**（公开可复现的 Harbor Hub 运行：[Pro](https://hub.harborframework.com/jobs/b56ccc56-1e77-4ba9-b1b2-3b0df51c4d49)、[Flash](https://hub.harborframework.com/jobs/f4c08d76-7d36-4b9e-afe6-0720f20b5269)）。两个结果都超过 vals.ai 的数字，因此无论那 50.19% 对应哪个 DeepSeek-V4 档位，框架都在实打实地发挥作用。[^vals] 能力主要来自模型，而 Ante 的职责是忠实地释放它 —— *改进框架，而非调教 prompt*。此外，Ante 仅约 15 MB，内存与磁盘占用远低于同类 Agent，与 DeepSeek 的低 token 成本相得益彰，适合低成本、高频次的 Agent 运行。

<div align="center">
  <img src="./assets/ante_deepseek_auto_mode.gif" alt="Ante 在终端中以 auto 模式执行 Agent 任务" width="640" />
</div>

- **文档：** <https://docs.antigma.ai>（别名：<https://ante.run>）
- **GitHub：** <https://github.com/AntigmaLabs/ante-preview>

#### 1. 安装 Ante

```sh
curl -fsSL https://ante.run/install.sh | bash
```

默认安装到 `~/.ante/bin`。如需安装到其他目录，设置 `ANTE_INSTALL_DIR`：

```sh
curl -fsSL https://ante.run/install.sh | ANTE_INSTALL_DIR=/usr/local/bin bash
```

Ante 支持 macOS 与 Linux；Windows 用户请在 **WSL**（或 Git Bash）中安装。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后导出 —— 内置的 `deepseek` 提供商会读取 `DEEPSEEK_API_KEY`：

```sh
export DEEPSEEK_API_KEY="sk-..."
```

#### 3. 使用 DeepSeek 运行 Ante

`deepseek` 提供商已内置，无需修改 catalog。进入项目目录并启动：

```sh
cd /path/to/my-project

# 在 DeepSeek-V4-Pro 上启动交互式 TUI
ante --provider deepseek --model deepseek-v4-pro

# 或使用更快、更省的 Flash 模型
ante --provider deepseek --model deepseek-v4-flash

# 无界面一次性执行
ante --provider deepseek --model deepseek-v4-pro -p "为 src/main.rs 添加错误处理"
```

两个模型均开箱即用支持 **完整的 100 万 token 上下文**。若要把 DeepSeek 设为默认（让直接运行 `ante` 即使用它），在 `~/.ante/settings.json` 中设置 `provider` 与 `model`。

#### 4. 使用最高推理强度

DeepSeek-V4-Pro 支持扩展推理。为获得最佳编程效果，建议以 **`max`** 思考强度运行。通过环境变量为本次会话设置：

```sh
MODEL_THINKING=max ante --provider deepseek --model deepseek-v4-pro
```

`MODEL_THINKING` 可取值 `none`、`enabled`、`deep`、`max`。若要永久生效，在 `~/.ante/catalog.json` 中覆盖该模型（启动时会合并到内置预设之上）：

```json
{
  "models": {
    "deepseek-v4-pro": { "thinking": "Max", "context_limit": 1000000, "max_tokens": 64000 }
  }
}
```

你也可以在 TUI 中按 `/model` 随时切换模型/提供商并调整思考预算。

#### Anthropic 协议（可选）

Ante 同样支持 **Anthropic** 协议，因此可经由 DeepSeek 的 [Anthropic 兼容端点](https://api-docs.deepseek.com/guides/anthropic_api) 接入。在 `~/.ante/catalog.json` 中添加：

```json
{
  "providers": {
    "deepseek-anthropic": {
      "id": "deepseek-anthropic",
      "display_name": "DeepSeek (Anthropic wire)",
      "base_url": "https://api.deepseek.com/anthropic",
      "wire_style": "AnthropicMessage",
      "auth": { "header": { "name": "x-api-key", "env_key": "DEEPSEEK_API_KEY" } },
      "preferred_models": [
        {
          "id": "claude-opus-4",
          "display_name": "DeepSeek-V4-Pro（Anthropic 协议）",
          "description": "在 DeepSeek 端点上映射为 deepseek-v4-pro",
          "max_tokens": 64000,
          "thinking": "Max"
        }
      ]
    }
  }
}
```

```sh
# 选用该提供商即采用推荐默认（claude-opus-4 → deepseek-v4-pro）
ante --provider deepseek-anthropic
```

**为什么用 `claude-opus-4`？** DeepSeek 的 Anthropic 端点按名称解析模型：`claude-opus-*` → `deepseek-v4-pro`，`claude-sonnet-*` / `claude-haiku-*` → `deepseek-v4-flash`，无法识别的名称回退到 `deepseek-v4-flash`。上面的推荐默认使用 `claude-opus-*` 名称，从而稳定获得 **V4-Pro**，避免被静默降级到 Flash。如需完整的 **100 万 token 上下文**，请优先使用第 3 步中的原生 `deepseek` 提供商 —— 这是更简单、也是本指南推荐的方式。

#### 模式与扩展

Ante 不只是一个交互式 TUI —— 以下能力都可在选用 `deepseek` 提供商时使用：

- **无界面（Headless）** —— `ante -p "..."` 执行任务后退出；也可通过 stdin 传入文件（`cat src/lib.rs | ante -p "审查这段代码"`）。见 [Headless Mode](https://docs.antigma.ai/usage/headless)。
- **服务端（Server）** —— `ante serve` 启动常驻守护进程，可通过 JSONL 以编程方式驱动。见 [Server Mode](https://docs.antigma.ai/usage/serve)。
- **MCP** —— 接入 [MCP 服务器](https://docs.antigma.ai/extend/mcp) 以扩展工具与上下文。
- **Skills** —— 通过可移植的 [Agent Skills](https://docs.antigma.ai/extend/skills) 扩展行为。
- **子 Agent** —— 将范围明确、可并行的工作委派给 [subagents](https://docs.antigma.ai/extend/subagents)。
- **离线推理** —— 通过内置的 llama.cpp 引擎在本地运行 GGUF 模型，无需 API Key。见 [Offline Mode](https://docs.antigma.ai/experimental/offline)。

#### 价格

Ante 通过原生 `deepseek` 提供商直接调用 DeepSeek API，因此你按 **DeepSeek 的标准价格计费，没有任何加价** —— 费用直接从你自己的 DeepSeek 账户扣除。

| 模型 | 输入（缓存未命中） | 输入（缓存命中） | 输出 |
|---|---|---|---|
| `deepseek-v4-pro` | $0.435 | $0.003625 | $0.87 |
| `deepseek-v4-flash` | $0.14 | $0.0028 | $0.28 |

单位为每 100 万 token；最新价格请以 [DeepSeek 官方定价](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 为准。

#### 配置参考

| 配置项 | 位置 | 说明 |
|---|---|---|
| `DEEPSEEK_API_KEY` | 环境变量 | 内置 `deepseek` 提供商的 API Key |
| `DEEPSEEK_BASE_URL` | 环境变量 | 覆盖 API 基址（默认 `https://api.deepseek.com`） |
| `MODEL_THINKING` | 环境变量 | 推理强度 —— `none` / `enabled` / `deep` / `max` |
| `provider` / `model` | `~/.ante/settings.json` | 未传 `--provider`/`--model` 时使用的默认值 |
| `providers` / `models` | `~/.ante/catalog.json` | 添加/覆盖提供商与模型默认值（合并到内置预设之上） |

完整 schema 见 [Providers](https://docs.antigma.ai/configuration/providers) 与 [Catalog Reference](https://docs.antigma.ai/reference/catalog-reference) 文档。

[^vals]: 据 [vals.ai Terminal-Bench 2.1 榜单](https://www.vals.ai/benchmarks/terminal-bench-2-1)，DeepSeek-V4 的评测使用提供商 **DeepSeek**，超参数为：推理强度 `max`、最大输出 token 384,000、temperature 1、top-p / top-k 默认。vals.ai 未标注 V4 的具体档位，但这并不影响结论：Ante 在 **两个档位** 上都超过 50.19% —— V4-Pro 64%、V4-Flash 62%，均在同一基准、`max` 推理强度下取得（Ante 构建评测于 2026-06-16），因此无论 50.19% 对应哪个档位，框架优势都成立。
