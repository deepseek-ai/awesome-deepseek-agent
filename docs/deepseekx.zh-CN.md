[English](./deepseekx.md) | [简体中文](./deepseekx.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeekX

DeepSeekX 是 OpenAI Codex CLI 的 DeepSeek 下游适配版本。它不重新设计
Codex core agent workflow；主要改动是增加 DeepSeek `/chat/completions`
接口适配，并默认使用 DeepSeek 相关的 provider、model、打包和用户界面行为。

- **GitHub：** <https://github.com/meomeo-dev/deepseekx>

#### 1. 安装 DeepSeekX

- 安装 [Node.js](https://nodejs.org/en/download/) 18+。
- 通过 npm 安装 CLI：

```sh
npm install -g @meomeo-dev/deepseekx
```

验证安装：

```sh
deepseekx --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API
Key。DeepSeekX 从 `DEEPSEEK_API_KEY` 环境变量读取：

```sh
export DEEPSEEK_API_KEY="sk-..."
```

#### 3. 在项目目录启动

```sh
cd /path/to/my-project
deepseekx
```

DeepSeekX 默认用户目录是 `~/.deepseekx`，项目级配置文件是
`.deepseekx/config.toml`。它不会默认读取上游 Codex 的用户目录。

#### 4. 可选配置

创建 `~/.deepseekx/config.toml`：

```toml
model_provider = "deepseek"
model = "deepseek-v4-pro"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "https://api.deepseek.com"
env_key = "DEEPSEEK_API_KEY"
wire_api = "chat"
requires_openai_auth = false
```

DeepSeekX 暴露 `deepseek-v4-pro` 和 `deepseek-v4-flash`。内置模型元数据
为 DeepSeek V4 配置 384K 默认上下文窗口和 100 万最大上下文窗口。推理强度
支持 `high` 与 `xhigh`；`xhigh` 会映射到 DeepSeek 的 max 推理强度。

由于配置模型保持与上游 Codex 对齐，`config.toml` 中的 profiles、sandbox
mode、approval policy、MCP、tools 与项目级配置等概念，基本可以参考 Codex
配置文档。需要替换的是上方示例中的 DeepSeek provider、model、API key 和
配置目录。

#### 项目 Profile

在仓库根目录创建 `.deepseekx/config.toml`：

```toml
model = "deepseek-v4-flash"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[profiles.pro]
model_provider = "deepseek"
model = "deepseek-v4-pro"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

使用 profile 启动：

```sh
deepseekx --profile pro
```

#### 功能特点

- 直接接入 DeepSeek Chat Completions，无需本地转换代理。
- 支持带审批控制的沙箱化本地命令执行。
- 支持连接已配置的 MCP servers 与 tools。
- 支持仓库级 `.deepseekx/config.toml` 配置。
- 内置 DeepSeek 专用模型目录、工具说明和提示词模板。

#### 故障排查

- `401` 或鉴权错误：检查 `DEEPSEEK_API_KEY`。
- `402` 或余额错误：检查 DeepSeek 开放平台余额。
- 配置未生效：确认该值是否同时存在于命令行、项目配置或用户配置中。
  DeepSeekX 的优先级是命令行、项目配置、用户配置。
- 工具执行被拦截：检查 `approval_policy` 和 `sandbox_mode`。

#### 相关资源

- [DeepSeekX](https://github.com/meomeo-dev/deepseekx)
- [Codex 配置参考](https://developers.openai.com/codex/config-reference)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
