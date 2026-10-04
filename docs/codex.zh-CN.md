[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Codex

Codex 是 OpenAI 的编程 Agent，支持 Codex CLI、ChatGPT 桌面应用和 VS Code 的 Codex IDE 扩展。Codex 使用 OpenAI Responses API 与模型通信，而 DeepSeek 原生支持该 API。

> **支持说明：** 目前只有 `deepseek-v4-flash` 支持原生接入 Codex。`deepseek-v4-pro` 预计在 2026 年 8 月初支持。如果现在需要使用 Pro，请使用下方的 [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) 方案。

## 推荐方案：原生 DeepSeek Provider

### 1. 配置 DeepSeek 模型 Provider

运行配置脚本前，请先安装 Codex CLI 或 ChatGPT 桌面应用，并至少启动一次，以便创建 `~/.codex` 目录。

macOS 或 Linux 用户运行：

```shell
bash <(curl -fsSL https://cdn.deepseek.com/api-docs/codex-deepseek-setup-en.sh)
```

Windows PowerShell 用户运行：

```powershell
irm https://cdn.deepseek.com/api-docs/codex-deepseek-setup-en.ps1 | iex
```

在菜单中选择 `deepseek-v4-flash`，并按提示输入 DeepSeek API Key。脚本会备份现有 Codex 配置，写入 `~/.codex/models.json`，更新 `~/.codex/config.toml`，并在保存前校验两个文件。之后可以再次运行脚本恢复安装前的配置，或在原生支持 Pro 后切换模型。

### 2. 手动配置

从 [DeepSeek Codex 接入文档](https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/codex) 中复制完整的 DeepSeek 模型目录，创建 `~/.codex/models.json`，然后将以下内容加入 `~/.codex/config.toml`（不存在时创建）：

```toml
model = "deepseek-v4-flash"
model_provider = "deepseek"
preferred_auth_method = "apikey"
forced_login_method = "api"
model_reasoning_effort = "high"
model_catalog_json = "~/.codex/models.json"

[model_providers.deepseek]
name = "deepseek"
base_url = "https://api.deepseek.com/"
wire_api = "responses"
experimental_bearer_token = "<your DeepSeek API Key>"
```

模型目录会向 Codex 声明上下文窗口、推理档位和工具调用能力。由于 API Key 会直接存储在 `config.toml` 中，请妥善保护该文件。

### 3. 开始使用

Codex CLI、ChatGPT 桌面应用和 VS Code 扩展读取同一份配置，不需要分别设置。在项目目录中运行：

```shell
cd /path/to/my-project
codex
```

Codex CLI 启动横幅应显示 `model: deepseek-v4-flash`。ChatGPT 桌面应用会在模型选择器中显示 **Custom**，这表示正在使用本地配置的模型。VS Code 的 Codex 扩展与 Codex CLI 共享同一份配置。

## 替代方案：Moon Bridge

在原生 Codex 尚未支持 Pro 之前，如果需要使用 `deepseek-v4-pro`，可以使用 Moon Bridge。下面的代理方案同时支持两个 V4 模型。

### 1. 安装依赖

- [Node.js](https://nodejs.org/en/download/) 18+。
- [Go](https://go.dev/dl/) 1.25+。
- 安装 Codex CLI：

```shell
npm install -g @openai/codex
```

验证安装：

```shell
codex --version
go version
```

### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建并复制 API Key。

### 3. 配置 Moon Bridge

克隆 Moon Bridge 并创建本地配置文件：

```shell
git clone https://github.com/ZhiYi-R/moon-bridge.git
cd moon-bridge
```

创建 `config.yml`，并填入 DeepSeek API Key：

```yaml
mode: "Transform"

server:
  addr: "127.0.0.1:38440"

models:
  deepseek-v4-pro:
    context_window: 1000000
    max_output_tokens: 384000
    default_reasoning_level: "high"
    supported_reasoning_levels:
      - effort: "high"
        description: "High reasoning effort"
      - effort: "xhigh"
        description: "Extra high reasoning effort"
    supports_reasoning_summaries: true
    default_reasoning_summary: "auto"
    extensions:
      deepseek_v4:
        enabled: true
  deepseek-v4-flash:
    context_window: 1000000
    max_output_tokens: 384000
    default_reasoning_level: "high"
    supported_reasoning_levels:
      - effort: "high"
        description: "High reasoning effort"
      - effort: "xhigh"
        description: "Extra high reasoning effort"
    supports_reasoning_summaries: true
    default_reasoning_summary: "auto"
    extensions:
      deepseek_v4:
        enabled: true

providers:
  deepseek:
    base_url: "https://api.deepseek.com/anthropic"
    api_key: "sk-your-deepseek-api-key"
    offers:
      - model: deepseek-v4-pro
      - model: deepseek-v4-flash

routes:
  moonbridge:
    model: deepseek-v4-pro
    provider: deepseek

defaults:
  model: moonbridge
  max_tokens: 65536
```

这个最小配置使用当前 Moon Bridge 配置结构，启用 DeepSeek V4 Pro / Flash、Codex 模型元数据和 DeepSeek V4 兼容扩展。**如果需要图片输入、Web Search 或多 Provider 路由**，可以再参考 Moon Bridge 的 `config.example.yml` 扩展配置。

### 4. 启动 Moon Bridge

```shell
go run ./cmd/moonbridge --config config.yml
```

保持这个终端运行。默认情况下，Moon Bridge 监听 `127.0.0.1:38440`，并提供 OpenAI Responses 兼容接口：

```text
http://127.0.0.1:38440/v1/responses
```

### 5. 生成 Codex 配置

另开一个终端，在 Moon Bridge 目录下执行以下命令，将 Codex 的 `config.toml` 和 `models_catalog.json` 写入 `CODEX_HOME_DIR`。

如果你已经有 Codex 配置，建议先**备份当前** `config.toml`：

macOS / Linux:

```shell
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME_DIR"

# 备份当前config.toml
cp "$CODEX_HOME_DIR/config.toml" "$CODEX_HOME_DIR/config.toml.bak" 2>/dev/null || true

# 创建config.toml和models_catalog.json
MODEL="$(go run ./cmd/moonbridge --config config.yml --print-codex-model)"
go run ./cmd/moonbridge \
  --config config.yml \
  --print-codex-config "$MODEL" \
  --codex-base-url "http://127.0.0.1:38440/v1" \
  --codex-home "$CODEX_HOME_DIR" \
  > "$CODEX_HOME_DIR/config.toml"
```

Windows PowerShell:

```powershell
$CODEX_HOME_DIR = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { "$HOME\.codex" }
New-Item -ItemType Directory -Force -Path $CODEX_HOME_DIR | Out-Null

# 备份当前config.toml
if (Test-Path "$CODEX_HOME_DIR\config.toml") {
  Copy-Item "$CODEX_HOME_DIR\config.toml" "$CODEX_HOME_DIR\config.toml.bak" -Force
}

# 创建config.toml和models_catalog.json
$MODEL = go run ./cmd/moonbridge --config config.yml --print-codex-model
go run ./cmd/moonbridge `
  --config config.yml `
  --print-codex-config "$MODEL" `
  --codex-base-url "http://127.0.0.1:38440/v1" `
  --codex-home "$CODEX_HOME_DIR" `
  | Set-Content -Path "$CODEX_HOME_DIR\config.toml"
```

这会创建：

- `config.toml`：Codex provider 配置，使用 `wire_api = "responses"`。
- `models_catalog.json`：Codex 使用的模型能力元数据，包括上下文窗口、推理档位和工具支持。

生成前可以先检查 Moon Bridge 读到的默认 Codex 模型：

```shell
go run ./cmd/moonbridge --config config.yml --print-codex-model
# moonbridge
```

### 6. 启动 Codex

进入要处理的项目目录，然后启动 Codex。

```shell
cd /path/to/my-project
codex
```

此时 Codex 会把 OpenAI Responses 请求发送给 Moon Bridge，再由 Moon Bridge 路由到 DeepSeek V4。

Codex App 也可以使用同一份生成的 Codex 配置。

### 一键启动脚本

Moon Bridge 提供了面向 Codex CLI 的辅助脚本，可以一键构建并启动代理、生成 Codex 配置并启动 Codex：

```shell
./scripts/start_codex_with_moonbridge.sh --project-directory /path/to/my-project
```

Windows PowerShell 用户可以使用：

```powershell
.\scripts\start_codex_with_moonbridge.ps1 -ProjectDirectory C:\path\to\my-project
```

### 验证

查看可用模型：

```shell
curl http://127.0.0.1:38440/v1/models
```

发送一条 Responses 测试请求：

```shell
curl http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonbridge",
    "input": "请用一句话打个招呼。",
    "max_output_tokens": 1024
  }'
```

当 Codex 发出请求后，Moon Bridge 终端应出现 `POST /v1/responses` 日志。

也可以验证推理档位是否进入配置：

```shell
curl http://127.0.0.1:38440/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonbridge",
    "input": "用一句话说明 Moon Bridge 的作用。",
    "reasoning": {"effort": "high"},
    "max_output_tokens": 1024
  }'
```

### 常见问题

- `connection refused`：Moon Bridge 未启动，或 `config.yml` 中的 `server.addr` 使用了其他端口。
- Codex 看不到模型：重新执行第 5 步；Codex 需要 `CODEX_HOME` 目录下的 `models_catalog.json`。
- 配置加载失败且提示 `field provider not found`：你使用的是旧版 `provider.providers` 配置；当前格式是顶层 `providers`、`models`、`routes`、`defaults`。
- `401` 或认证失败：检查 `config.yml` 中的 DeepSeek API Key 是否正确。
- `402` 或余额错误：检查 DeepSeek 开放平台账户余额。
- 图片输入失败：如果启用了 Visual 扩展，需要单独配置视觉 Provider（如 Kimi）的 API Key。你可以配置该 Provider，或移除 `visual.enabled: true` 来禁用 Visual 扩展。

### 相关资源

- [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge)
- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek Codex 接入文档](https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/codex)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
