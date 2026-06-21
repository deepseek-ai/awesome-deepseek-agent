[English](./jyycode.md) | [简体中文](./jyycode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 JYY-Code

JYY-Code 是一款开源终端编程 Agent，基于 OpenCode 深度扩展，支持多 Agent 编排、持久记忆、Agent Skills、MCP 和通信工具。

- **GitHub：** <https://github.com/Reon-Jin/JYY-Code>
- **npm：** <https://www.npmjs.com/package/jyycode-ai>

#### 1. 安装 JYY-Code

- 安装 [Node.js](https://nodejs.org/en/download/) 20+ 版本。
- 安装已发布的 CLI 包：

```sh
npm install -g jyycode-ai
```

- 验证安装是否成功：

```sh
jyycode --version
```

`jyy` 和 `jyycode` 会启动同一个 CLI。

#### 2. 配置 DeepSeek

最简单的方式是使用内置 provider 登录命令保存 DeepSeek API Key：

```sh
jyycode auth login --provider deepseek
jyycode models deepseek --refresh
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

你也可以直接写入全局配置文件 `~/.config/jyycode/jyycode.jsonc`：

```jsonc
{
  "$schema": "https://jyycode.ai/config.json",
  "model": "deepseek/deepseek-v4-pro",
  "small_model": "deepseek/deepseek-v4-flash",
  "provider": {
    "deepseek": {
      "options": {
        "apiKey": "sk-..."
      },
      "models": {
        "deepseek-v4-pro": {
          "reasoning": true,
          "limit": {
            "context": 1000000,
            "output": 384000
          }
        },
        "deepseek-v4-flash": {
          "limit": {
            "context": 1000000,
            "output": 384000
          }
        }
      }
    }
  }
}
```

配置说明：

| 选项 | 说明 |
|------|------|
| `model` | 默认模型，格式为 `provider/model`。推荐使用 `deepseek/deepseek-v4-pro` 作为主力编程模型。 |
| `small_model` | 轻量任务模型，例如标题、摘要等，可使用 `deepseek/deepseek-v4-flash`。 |
| `provider.deepseek.options.apiKey` | DeepSeek API Key。如果使用 `jyycode auth login --provider deepseek` 保存凭证，可以省略此项。 |
| `limit.context` | DeepSeek V4 支持 100 万 token 上下文窗口。 |
| `limit.output` | JYY-Code 模型元数据中的最大输出 token 限制。 |

JYY-Code 会为 OpenAI-compatible reasoning 模型识别推理强度变体。使用 `deepseek-v4-pro` 时，如需最大推理强度，请选择 `max` 变体。

#### 3. 在项目中启动 JYY-Code

```sh
cd /path/to/my-project
jyy
```

在 TUI 中：

- 如果想交互式配置 DeepSeek API Key，运行 `/connect`。
- 运行 `/models` 选择 `deepseek/deepseek-v4-pro`。
- 运行 `/variants` 并选择 `max`，启用 DeepSeek V4 Pro 的最大推理强度。

#### 4. 首次运行

可以先让 JYY-Code 检查当前仓库：

```text
阅读这个项目并总结它的架构，然后建议一个安全的首个改进点。
```

JYY-Code 会在当前终端目录中运行，并按照你的权限配置使用文件系统、Shell、MCP、记忆、技能和多 Agent 工具。
