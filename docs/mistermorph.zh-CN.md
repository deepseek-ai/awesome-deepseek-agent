[English](./mistermorph.md) | [简体中文](./mistermorph.zh-CN.md) | [日本語](./mistermorph.ja.md) · [← 返回](../README.zh-CN.md)

# 接入 Morph

Morph 是一个开源的 Agent 运行时和控制台，可用于构建个人或团队 AI Agent。它支持 CLI、Web Console、聊天频道集成、工具、Skill、记忆、MCP，以及 DeepSeek 这类 OpenAI 兼容模型供应商。

- **GitHub：** <https://github.com/quailyquaily/mistermorph>

#### 1. 安装 Morph

最简单的方式是从 [GitHub Releases](https://github.com/quailyquaily/mistermorph/releases) 下载桌面版。桌面版会启动本地后端，并提供 Console 图形界面。

如果你更希望使用 CLI，或者需要在服务器上运行 Morph，可以使用官方安装脚本：

```sh
curl -fsSL -o /tmp/install-mistermorph.sh https://raw.githubusercontent.com/quailyquaily/mistermorph/refs/heads/master/scripts/install-release.sh
sudo bash /tmp/install-mistermorph.sh
```

安装完成后，确认 CLI 可用：

```sh
mistermorph --help
```

#### 2. 配置 DeepSeek

推荐先使用 Console 图形界面配置。

如果使用桌面版，打开应用后进入 Setup 或 Settings -> LLM。

如果使用本地 CLI 安装，启动 Console：

```sh
mistermorph console serve --allow-empty-password
```

打开命令输出中的本地 URL，然后进入 Setup 或 Settings -> LLM，填写：

- Provider：`deepseek`
- Model：`deepseek-v4-pro`
- API Key：你的 DeepSeek API Key

`--allow-empty-password` 只适合在可信的本地环境使用。如果 Console 会暴露到网络，请改为配置密码。

你可以在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

如果希望默认使用更快、成本更低的模型，可以把 Model 改成 `deepseek-v4-flash`。

如果你更希望直接编辑配置文件，先运行 setup 命令，创建 Morph 默认状态和配置文件：

```sh
mistermorph install
```

然后编辑 `~/.morph/config.yaml`，配置 LLM 供应商：

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-pro
  api_key: ${DEEPSEEK_API_KEY}
```

使用 DeepSeek 官方 API 时，`provider` 写 `deepseek`。只有接入自定义 OpenAI-compatible endpoint 时，才需要把 `provider` 写成 `openai`。

在 shell 中设置 DeepSeek API Key：

```sh
export DEEPSEEK_API_KEY="sk-..."
```

如果使用 `deepseek-v4-flash`：

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
```

#### 3. 运行 Morph

在命令行执行一个任务：

```sh
mistermorph run --task "列出这个项目的文件，并总结它的用途。"
```

或者启动本地 Console 服务：

```sh
mistermorph console serve
```

#### 4. 可选：使用独立 LLM Profile

Morph 支持命名 LLM profile。当你希望将不同任务路由到不同 DeepSeek 模型时，可以这样配置：

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
  profiles:
    deepseek_pro:
      provider: deepseek
      model: deepseek-v4-pro
      api_key: ${DEEPSEEK_API_KEY}
      reasoning_effort: high
```

需要时，可以通过 Morph 的路由配置，把特定工作流分配到这个 profile。
