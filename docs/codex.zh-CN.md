[English](./codex.md) | [简体中文](./codex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Codex

Codex 是 OpenAI 的编程 Agent，支持 CLI 和 App 使用。Codex 使用 OpenAI Responses API 与模型通信，因此需要一个转发层处理请求，这里使用 [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge) 作为转发层。

#### 1. 安装依赖

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

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建并复制 API Key。

#### 3. 配置 Moon Bridge

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

provider:
  providers:
    deepseek:
      base_url: "https://api.deepseek.com/anthropic"
      api_key: "sk-your-deepseek-api-key"
      models:
        deepseek-v4-pro:
          context_window: 1000000
          max_output_tokens: 384000
          extensions:
            deepseek_v4:
              enabled: true
          default_reasoning_level: "high"
          supported_reasoning_levels:
            - effort: "high"
              description: "High reasoning effort"
            - effort: "xhigh"
              description: "Extra high reasoning effort"
          supports_reasoning_summaries: true
          default_reasoning_summary: "auto"
  routes:
    moonbridge:
      to: "deepseek/deepseek-v4-pro"
  default_model: "moonbridge"
```

这个最小配置启用 DeepSeek V4 Pro、Codex 模型元数据和 DeepSeek V4 兼容扩展；如果需要图片输入、Web Search 或多 Provider 路由，可以再参考 Moon Bridge 的 `config.example.yml` 扩展配置。

#### 4. 启动 Moon Bridge

```shell
go run ./cmd/moonbridge --config config.yml
```

保持这个终端运行。默认情况下，Moon Bridge 监听 `127.0.0.1:38440`，并提供 OpenAI Responses 兼容接口：

```text
http://127.0.0.1:38440/v1/responses
```

#### 5. 生成 Codex 配置

另开一个终端，在 Moon Bridge 目录下生成 Codex 的 `config.toml` 和 `models_catalog.json`：

```shell
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME_DIR"

MODEL="$(go run ./cmd/moonbridge --config config.yml --print-codex-model)"
go run ./cmd/moonbridge \
  --config config.yml \
  --print-codex-config "$MODEL" \
  --codex-base-url "http://127.0.0.1:38440/v1" \
  --codex-home "$CODEX_HOME_DIR" \
  > "$CODEX_HOME_DIR/config.toml"
```

这会写入：

- `config.toml`：Codex provider 配置，使用 `wire_api = "responses"`。
- `models_catalog.json`：Codex 使用的模型能力元数据，包括上下文窗口、推理档位和工具支持。

#### 6. 启动 Codex

进入要处理的项目目录，然后启动 Codex：

```shell
cd /path/to/my-project
CODEX_HOME="$CODEX_HOME_DIR" codex --cd "$PWD"
```

此时 Codex 会把 OpenAI Responses 请求发送给 Moon Bridge，再由 Moon Bridge 路由到 DeepSeek V4。

Codex App 也可以使用同一份生成的 Codex 配置。

#### 一键启动脚本

Moon Bridge 提供了面向 Codex CLI 的辅助脚本，可以一键构建并启动代理、生成 Codex 配置并启动 Codex：

```shell
./scripts/start_codex_with_moonbridge.sh --project-directory /path/to/my-project
```

#### 验证

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
    "max_output_tokens": 100
  }'
```

当 Codex 发出请求后，Moon Bridge 终端应出现 `POST /v1/responses` 日志。

#### 常见问题

- `connection refused`：Moon Bridge 未启动，或 `config.yml` 中的 `server.addr` 使用了其他端口。
- Codex 看不到模型：重新执行第 5 步；Codex 需要 `CODEX_HOME` 目录下的 `models_catalog.json`。
- `401` 或认证失败：检查 `config.yml` 中的 DeepSeek API Key 是否正确。
- `402` 或余额错误：检查 DeepSeek 开放平台账户余额。
- 图片输入失败：如果启用了 Visual 扩展，需要单独配置视觉 Provider（如 Kimi）的 API Key。你可以配置该 Provider，或移除 `visual.enabled: true` 来禁用 Visual 扩展。

#### 相关资源

- [Moon Bridge](https://github.com/ZhiYi-R/moon-bridge)
- [Codex CLI](https://github.com/openai/codex)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
