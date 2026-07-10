[English](./hara.md) | [简体中文](./hara.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Hara CLI

Hara CLI 是一个开源终端编码 Agent，支持多个模型提供商，并可通过 DeepSeek 的 OpenAI 兼容接口接入 DeepSeek。

- **GitHub:** <https://github.com/hara-cli/hara>
- **文档:** <https://docs.hara.run/zh/getting-started/installation>

#### 1. 安装 Hara CLI

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 20 或更高版本。
- 安装 Hara CLI 0.113.0 或更高版本：

```bash
npm i -g @nanhara/hara@0.113.0
```

- 验证：

```bash
hara --version
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek Platform](https://platform.deepseek.com/api_keys)，创建 API Key，并妥善保管。

#### 3. 配置 DeepSeek

Hara 内置了 `deepseek` provider。该 provider 的默认 endpoint 是 `https://api.deepseek.com`。

你可以使用交互式配置向导：

```bash
hara setup
```

选择 DeepSeek，输入你的 API Key，并选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`。

也可以使用命令配置：

```bash
hara config set provider deepseek
hara config set model deepseek-v4-pro
hara config set reasoningEffort max
```

然后通过环境变量提供 API Key：

```bash
export DEEPSEEK_API_KEY="your-api-key"
```

也可以让 Hara 将 API Key 写入 `~/.hara/config.json`：

```bash
hara config set apiKey "your-api-key"
```

不要将 `~/.hara/config.json` 或任何 API Key 提交到项目仓库。

#### 4. 验证配置

运行：

```bash
hara doctor
```

输出中应出现：

```text
provider deepseek · model deepseek-v4-pro · https://api.deepseek.com
auth configured
```

#### 5. 首次运行

在项目中交互式启动 Hara：

```bash
cd your-project
hara
```

也可以执行一次性任务：

```bash
hara -p "summarize this repository"
```

#### DeepSeek V4 说明

- 建议使用 `deepseek-v4-pro` 处理复杂编码与 Agent 任务；如需更快、更低成本的运行，可使用 `deepseek-v4-flash`。
- DeepSeek V4 模型支持 1M token 上下文窗口。Hara 当前没有针对 DeepSeek provider 暴露 `context_window` 配置项，因此无需在 Hara 中额外配置。
- Hara CLI 0.113.0 及更高版本支持 DeepSeek V4 thinking 控制。`hara config set reasoningEffort max` 会在 OpenAI 兼容 chat endpoint 请求中发送 DeepSeek 的 `thinking: { type: "enabled" }` 和 `reasoning_effort: "max"`。
- 不要使用已弃用的 DeepSeek V3 模型名。
